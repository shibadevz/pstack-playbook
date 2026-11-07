#!/usr/bin/env python3
"""Regenerate the VitePress sources in ./docs (config included) from pstack-playbook.csv and pages/*.md.

Run: python3 -I site-build.py [--force]
--force replaces docs/ even if it holds files the generator does not produce.
PSTACK_PORT_DIR=<pstack-port checkout> refreshes upstream/pstack-cursor-plugin.json first.
"""
import csv
import html
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
FINAL = ROOT / "docs"
SITE = ROOT / "docs.tmp"  # generated here first, swapped into docs/ only after every check passes
PAGES = ROOT / "pages"
UPSTREAM_PROVENANCE = ROOT / "upstream" / "pstack-cursor-plugin.json"  # committed copy; PSTACK_PORT_DIR refreshes it
KEEP = (".vitepress/cache", ".vitepress/dist")  # gitignored build outputs, carried over to the new docs/
TH_MONTHS = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
THEME_SRC = ROOT / "theme-src"  # hand-written theme (css, index.ts, components) copied into docs/.vitepress/theme

# situation page file stem -> ascii slug (00-* and the Notion import page are ignored)
SITUATIONS = {
    "เริ่มงาน-ตั้งค่า": "start-setup",
    "เข้าใจโค้ด": "understand-code",
    "ออกแบบ-วางแผน": "design-plan",
    "สร้างฟีเจอร์": "build-feature",
    "เจอ bug": "found-bug",
    "Review": "review",
    "Verify-เทส": "verify-test",
    "Refactor-เก็บกวาด": "refactor-cleanup",
    "Performance": "performance",
    "เขียนเอกสาร-สื่อสาร": "docs-communication",
    "PR & Ship": "pr-ship",
    "ปล่อยรันเอง-ข้ามคืน": "autonomous-overnight",
    "ปรับแต่ง-PStack": "customize-pstack",
    "ปัญหาที่เจอบ่อย": "troubleshooting",
}
TYPES = {"Workflow skill": "skills", "Playbook": "playbooks", "Principle": "principles"}

def slug_of(name):
    if name.startswith("/pstack:"):
        s = name[len("/pstack:"):]
        return s.removeprefix("principle-")
    s = name.removeprefix("Playbook: ")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def short_of(name):
    if name.startswith("Playbook: "):
        return name[len("Playbook: "):]
    return slug_of(name)


def cell(s):
    return " ".join(s.split()).replace("|", "\\|")


def code(s):
    s = " ".join(s.split())
    return f"`` {s} ``" if "`" in s else f"`{s}`"


ESC_RE = re.compile(r"(`+[^`]*`+)")


def esc(text):
    """Escape '<' outside code spans/fences so Vue does not parse <symptom> as a tag."""
    out, fenced = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            line = "".join(p if p.startswith("`") else p.replace("<", "&lt;") for p in ESC_RE.split(line))
        out.append(line)
    return "\n".join(out)


def prompt_tag(prompt, compact=False):
    """Single-line <PromptBlock> tag; the text is attribute-escaped so markdown/Vue never touch it."""
    text = html.escape(prompt.strip(), quote=True).replace("{", "&#123;").replace("\n", "&#10;")
    return f'<PromptBlock{" compact" if compact else ""} text="{text}" />'


ITEM_RE = re.compile(r"^((?:\d+\.|-) \*\*(.+?)\*\*.*?)\s*วิธีเรียก:.*$", re.M)


def inline_prompts(text, stem, prompt_of, hold):
    """Replace each item's trailing 'วิธีเรียก: ...' with that entity's CSV example prompt as a nested code block."""
    def sub(m):
        name = m.group(2)
        assert name in prompt_of, f"{stem}: item has no CSV row: {name}"
        return f"{m.group(1).rstrip().removesuffix('.')}\n\n   {hold(prompt_tag(prompt_of[name], compact=True))}"
    return ITEM_RE.sub(sub, text)


def invoke(v):
    """วิธีเรียก cell: inline code only for a real command; prose stays text with just the commands in it as code."""
    v = " ".join(v.split())
    if v.startswith("/pstack:"):
        return code(v)
    return esc(re.sub(r"/pstack:[\w-]+", lambda m: code(m.group(0)), v))


def typeline(cmd):
    return ('<p class="typeline"><span class="typeline-label">พิมพ์</span>'
            f'<code>{html.escape(cmd).replace("{", "&#123;")}</code></p>')


PROMPT_SEC = re.compile(r"## ตัวอย่าง prompt\n\n```text\n(.*?)\n```\n", re.S)


def link(d, slug):
    return f"/{d}/{slug}"


CONFIG = """import { defineConfig } from 'vitepress'
import { thaiTokenize } from './theme/thai-tokenize'

export default defineConfig({
  base: '/pstack-playbook/',
  lang: 'th-TH',
  title: 'PStack Playbook',
  description: 'รวม skill, playbook และ principle ของ PStack ว่ามีอะไรบ้าง ใช้ทำอะไร และเรียกอย่างไร',
  cleanUrls: true,
  themeConfig: {
    search: {
      provider: 'local',
      options: {
        detailedView: true,
        // indexing only: functions in themeConfig are dropped from the client bundle, so theme/index.ts sets the query tokenizer
        miniSearch: { options: { tokenize: thaiTokenize } },
        // index-only: <EntityMeta> keeps its situation names in an attribute, so expand them to text, else searching a situation never finds its entities
        _render: async (src, env, md) => {
          const html = md.render(src, env)
          if (env.frontmatter?.search === false) return ''
          return html.replace(/<EntityMeta[^>]*:sits="([^"]*)"[^>]*>/, (_, a) => {
            try { return '<p>' + JSON.parse(a.replace(/&quot;/g, '"').replace(/&amp;/g, '&')).map(s => s.title).join(' ') + '</p>' } catch { return '' }
          })
        },
        translations: {
          button: { buttonText: 'ค้นหา', buttonAriaLabel: 'ค้นหา' },
          modal: {
            displayDetails: 'แสดงรายละเอียด',
            resetButtonTitle: 'ล้างคำค้นหา',
            backButtonTitle: 'ปิดการค้นหา',
            noResultsText: 'ไม่พบผลลัพธ์สำหรับ',
            footer: {
              selectText: 'เลือก',
              selectKeyAriaLabel: 'enter',
              navigateText: 'เลื่อน',
              navigateUpKeyAriaLabel: 'ลูกศรขึ้น',
              navigateDownKeyAriaLabel: 'ลูกศรลง',
              closeText: 'ปิด',
              closeKeyAriaLabel: 'esc'
            }
          }
        }
      }
    },
    outline: { level: [2, 3], label: 'ในหน้านี้' },
    docFooter: { prev: 'ก่อนหน้า', next: 'ถัดไป' },
    nav: __NAV__,
    sidebar: __SIDEBAR__,
    socialLinks: []
  }
})
"""

def main():
    # validate every input before writing anything
    if os.environ.get("PSTACK_PORT_DIR"):
        src = Path(os.environ["PSTACK_PORT_DIR"]) / "dist/claude/provenance/pstack-cursor-plugin.json"
        UPSTREAM_PROVENANCE.parent.mkdir(exist_ok=True)
        shutil.copyfile(src, UPSTREAM_PROVENANCE)
    upstream_version = json.loads(UPSTREAM_PROVENANCE.read_text(encoding="utf-8"))["version"]  # KeyError/FileNotFoundError = fail loudly
    missing = [str(PAGES / f"{st}.md") for st in SITUATIONS if not (PAGES / f"{st}.md").is_file()]
    assert not missing and THEME_SRC.is_dir(), f"missing inputs: {missing or THEME_SRC}"
    with open(ROOT / "pstack-playbook.csv", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    ents, seen = [], set()  # (row, dir, slug)
    for r in rows:
        d = TYPES[r["ประเภท"].strip()]
        slug = slug_of(r["Name"].strip())
        assert slug and (d, slug) not in seen, f"slug collision/empty: {r['Name']}"
        seen.add((d, slug))
        ents.append((r, d, slug))
    link_of = {r["Name"].strip(): link(d, slug) for r, d, slug in ents}
    prompt_of = {r["Name"].strip(): " ".join(r["ตัวอย่าง prompt"].split()) for r, _, _ in ents}

    # generate into a scratch dir; docs/ is untouched until the end
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / ".vitepress" / "theme").mkdir(parents=True)
    shutil.copytree(THEME_SRC, SITE / ".vitepress" / "theme", dirs_exist_ok=True)

    (SITE / "situations").mkdir()
    names_re = re.compile(r"\*\*(" + "|".join(re.escape(n) for n in sorted(link_of, key=len, reverse=True)) + r")\*\*")
    sit = []  # (title, slug, blurb)
    for stem, slug in SITUATIONS.items():
        text = (PAGES / f"{stem}.md").read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        text = text.replace(" หน้านี้อ่านได้โดยไม่ต้องใช้ database", "")
        blurb = next(p for p in text.split("\n\n")[1:] if p.strip()).strip()
        # prompts become placeholders so esc() does not turn the component tags into &lt;PromptBlock
        tags = []
        def hold(tag):
            tags.append(tag)
            return f"@@PB{len(tags) - 1}@@"
        text = inline_prompts(text, stem, prompt_of, hold)
        known = set(prompt_of.values())  # a combined prompt that repeats an item's prompt is dropped, only the tip stays

        def tail(m):
            if " ".join(m.group(1).split()) in known:
                return "## วิธีเขียน prompt\n"
            return "## ตัวอย่าง prompt รวม\n\n" + hold(prompt_tag(m.group(1))) + "\n"
        text = PROMPT_SEC.sub(tail, text)
        text = esc(names_re.sub(lambda m: f"[**{m.group(1)}**]({link_of[m.group(1)]})", text))
        text = re.sub(r"@@PB(\d+)@@", lambda m: tags[int(m.group(1))], text)
        (SITE / "situations" / f"{slug}.md").write_text(text, encoding="utf-8")
        sit.append((title, slug, cell(blurb)))

    norm = lambda t: re.sub(r"[\s/\-]+", "-", t.strip())
    sit_link = {norm(t): link("situations", sl) for t, sl, _ in sit}
    for r, d, slug in ents:
        (SITE / d).mkdir(exist_ok=True)
        sits = []
        for t in r["สถานการณ์"].split(","):
            if t.strip():
                assert norm(t) in sit_link, f"unknown situation: {t}"
                sits.append({"title": t.strip(), "link": sit_link[norm(t)]})
        meta = (f'<EntityMeta type="{d}" label="{r["ประเภท"].strip()}" '
                f'sits="{html.escape(json.dumps(sits, ensure_ascii=False), quote=True)}" />').replace('sits="', ':sits="', 1)
        def row(title, *body):
            return ['<div class="spec-row">', "", f"## {title}", "", *body, "", "</div>", ""]
        name = r["Name"].strip()
        fm = ["---", f"pageClass: entity-page entity-{d}", "outline: false"]
        if d != "skills":  # short H1, full name stays in <title>
            fm.append(f"title: {json.dumps(name, ensure_ascii=False)}")
        out = fm + ["---", "", f"# {name if d == 'skills' else short_of(name)}", "", meta, ""]
        if d == "playbooks":
            assert r["วิธีเรียก"].startswith("/pstack:poteto-mode"), name
            out += [typeline(" ".join(r["วิธีเรียก"].split())), ""]
        elif d == "principles":
            out += [typeline(name), ""]
        out += [prompt_tag(r["ตัวอย่าง prompt"]), "",
               *row("ใช้ทำอะไร", esc(r["ใช้ทำอะไร"].strip())),
               *row("ใช้เมื่อ", esc(r["ใช้เมื่อ"].strip()))]
        extra = r["ต่างจาก / ข้อควรรู้"].strip()
        if extra:
            out += row("ต่างจาก / ข้อควรรู้", esc(extra))
        out += row("วิธีเรียก", invoke(r["วิธีเรียก"]))
        (SITE / d / f"{slug}.md").write_text("\n".join(out), encoding="utf-8")

    # overview pages
    groups = (("Workflow skill", "Workflow skills", "skills"), ("Playbook", "Playbooks", "playbooks"),
              ("Principle", "Principles", "principles"))
    counts = {}
    for typ, heading, d in groups:
        sel = [(r, slug) for r, dd, slug in ents if dd == d]
        counts[d] = len(sel)
        page = ["---", "pageClass: overview overview-cmd", "---", "", f"# {heading}", "", "| คำสั่ง | ใช้ทำอะไร |", "|---|---|"]
        page += [f"| [{r['Name'].strip() if d == 'skills' else short_of(r['Name'].strip())}]({link(d, slug)}) "
                 f"| {esc(cell(r['ใช้ทำอะไร']))} |" for r, slug in sel]
        (SITE / d / "index.md").write_text("\n".join(page) + "\n", encoding="utf-8")
    page = ["---", "pageClass: overview", "---", "", "# ตามสถานการณ์", "", "| สถานการณ์ | ใช้ทำอะไร |", "|---|---|"]
    page += [f"| [{t}]({link('situations', s)}) | {esc(b)} |" for t, s, b in sit]
    (SITE / "situations" / "index.md").write_text("\n".join(page) + "\n", encoding="utf-8")

    home_groups = []
    for typ, heading, d in groups:
        its = [(r["Name"].strip(), short_of(r["Name"].strip()), r, slug) for r, dd, slug in ents if dd == d]
        if d != "playbooks":
            its.sort(key=lambda x: x[0].lower())
        home_groups.append({"key": d, "title": heading, "items": [
            {"cmd": nm if d == "skills" else sh, "what": cell(r["ใช้ทำอะไร"]).replace("`", ""), "link": link(d, slug)}
            for nm, sh, r, slug in its]})
    today = datetime.now(ZoneInfo("Asia/Bangkok"))
    upstream = f"อ้างอิง PStack {upstream_version} · อัปเดต {today.day} {TH_MONTHS[today.month - 1]} {today.year}"
    home_data = {"upstream": upstream, "upstreamVersion": f"PStack {upstream_version}", "groups": home_groups, "situations": [{"title": t, "link": link("situations", sl)} for t, sl, _ in sit]}
    (SITE / ".vitepress" / "theme" / "home-data.json").write_text(
        json.dumps(home_data, ensure_ascii=False, indent=1), encoding="utf-8")
    home_links = [i["link"] for g in home_groups for i in g["items"]] + [x["link"] for x in home_data["situations"]]
    (SITE / "index.md").write_text('---\nlayout: home\nmarkdownStyles: false\n---\n\n<HomeSheet />\n', encoding="utf-8")

    # config: nav + one shared sidebar
    nav = [{"text": "หน้าแรก", "link": "/"}, {"text": "Skills", "link": "/skills/"},
           {"text": "Playbooks", "link": "/playbooks/"}, {"text": "Principles", "link": "/principles/"},
           {"text": "ตามสถานการณ์", "link": "/situations/"}]
    sidebar = [{"text": "ตามสถานการณ์", "collapsed": False,
                "items": [{"text": t, "link": link("situations", s)} for t, s, _ in sit]}]
    for typ, heading, d in groups:
        items = [(short_of(r["Name"].strip()), slug) for r, dd, slug in ents if dd == d]
        if d != "playbooks":  # playbooks keep CSV (workflow) order
            items.sort(key=lambda x: x[0].lower())
        sidebar.append({"text": heading, "collapsed": True, "items": [{"text": n, "link": link(d, s)} for n, s in items]})
    dump = lambda o: json.dumps(o, ensure_ascii=False, indent=2).replace("\n", "\n    ")
    (SITE / ".vitepress" / "config.mts").write_text(
        CONFIG.replace("__NAV__", dump(nav)).replace("__SIDEBAR__", dump(sidebar)), encoding="utf-8")

    broken = 0
    link_re = re.compile(r"\]\(([^)\s]+)\)")
    pages = [p for p in SITE.rglob("*.md")]
    for md in sorted(pages):
        targets = link_re.findall(md.read_text(encoding="utf-8"))
        if md == SITE / "index.md":
            targets = home_links
        for target in targets:
            if target.startswith(("http", "#")):
                continue
            t = target.lstrip("/")
            f = SITE / (t + "index.md" if t.endswith("/") or not t else t + ".md")
            if not f.is_file():
                print(f"BROKEN: {md.relative_to(SITE)} -> {target}")
                broken += 1
    n_ent = sum(len([p for p in (SITE / d).glob("*.md") if p.name != "index.md"]) for d in TYPES.values())
    n_sit = len([p for p in (SITE / "situations").glob("*.md") if p.name != "index.md"])
    print(f"{n_ent} entity pages, {n_sit} situation pages, {broken} broken links")
    assert broken == 0, "broken links found"
    assert n_ent == len(rows), "entity page count mismatch"
    assert n_sit == len(SITUATIONS), "situation page count mismatch"

    # swap: refuse to drop hand-made files in docs/ unless --force
    def files(base):
        return {p.relative_to(base).as_posix() for p in base.rglob("*")
                if p.is_file() and not any(p.relative_to(base).as_posix().startswith(k + "/") for k in KEEP)}
    if FINAL.exists():
        extra = sorted(files(FINAL) - files(SITE))
        if extra and "--force" not in sys.argv:
            shutil.rmtree(SITE)
            sys.exit(f"ABORT: docs/ has files the generator does not produce: {', '.join(extra)}\nMove them away or pass --force. docs/ left untouched.")
        for k in KEEP:
            if (FINAL / k).exists():
                (SITE / k).parent.mkdir(parents=True, exist_ok=True)
                shutil.move(FINAL / k, SITE / k)
        old = ROOT / "docs.old"
        shutil.rmtree(old, ignore_errors=True)
        FINAL.rename(old)
        SITE.rename(FINAL)
        shutil.rmtree(old)
    else:
        SITE.rename(FINAL)


if __name__ == "__main__":
    sys.exit(main())
