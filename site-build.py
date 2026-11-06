#!/usr/bin/env python3
"""Regenerate the Docsify site in ./docs (GitHub Pages source) from pstack-playbook.csv and pages/*.md.

Run: python3 -I /Users/r00t3r21/Documents/pstack-playbook/site-build.py
"""
import csv
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "docs"
PAGES = ROOT / "pages"

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

INDEX_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PStack Playbook</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=IBM+Plex+Sans+Thai:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4.13.1/lib/themes/vue.css">
  <style>
    :root { --theme-color: #3884ff; }
    body, .sidebar, .markdown-section {
      font-family: "Sarabun", "IBM Plex Sans Thai", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    body { background: #fff; }
    .sidebar { background: #f7f8fa; border-right: 1px solid #e6e8eb; }
    .sidebar ul li a { color: #4a5565; font-size: 14px; }
    .sidebar ul li.active > a { color: var(--theme-color); font-weight: 600; border-right: 2px solid var(--theme-color); }
    /* group headings: top-level bold items */
    .sidebar-nav > ul > li > p,
    .sidebar-nav > ul > li > strong {
      display: block; margin: 18px 0 4px; padding-left: 16px; font-size: 11px; font-weight: 700;
      letter-spacing: .08em; text-transform: uppercase; font-variant: small-caps; color: #1f2937;
    }
    .content { background: #fff; }
    .markdown-section { max-width: 800px; line-height: 1.75; font-size: 16px; color: #1f2937; }
    .markdown-section h1 { font-weight: 700; }
    .markdown-section h2 { border-bottom: 1px solid #eef0f2; padding-bottom: .3em; margin-top: 1.8em; }
    .markdown-section table { display: table; width: 100%; }
    .markdown-section th { background: #f7f8fa; }
    .search { border-bottom: 1px solid #e6e8eb; }
    .search input { font-family: inherit; }
  </style>
</head>
<body>
  <div id="app">กำลังโหลด…</div>
  <script>
    window.$docsify = {
      name: 'PStack Playbook',
      loadSidebar: true,
      subMaxLevel: 2,
      auto2top: true,
      alias: { '/.*/_sidebar.md': '/_sidebar.md' },
      search: { placeholder: 'ค้นหา skill…', noData: 'ไม่พบผลลัพธ์', depth: 2 }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4.13.1/lib/docsify.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4.13.1/lib/plugins/search.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify-copy-code@3.0.0/dist/docsify-copy-code.min.js"></script>
</body>
</html>
"""


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


def main():
    with open(ROOT / "pstack-playbook.csv", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    ents, seen = [], set()  # (row, dir, slug)
    for r in rows:
        d = TYPES[r["ประเภท"].strip()]
        slug = slug_of(r["Name"].strip())
        assert slug and (d, slug) not in seen, f"slug collision/empty: {r['Name']}"
        seen.add((d, slug))
        ents.append((r, d, slug))
    link_of = {r["Name"].strip(): f"/{d}/{slug}.md" for r, d, slug in ents}

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    (SITE / ".nojekyll").write_text("")
    (SITE / "index.html").write_text(INDEX_HTML, encoding="utf-8")

    for r, d, slug in ents:
        (SITE / d).mkdir(exist_ok=True)
        tags = " ".join(code(t.strip()) for t in r["สถานการณ์"].split(",") if t.strip())
        out = [f"# {r['Name'].strip()}", "",
               f"<small>ประเภท: **{r['ประเภท'].strip()}**" + (f" · สถานการณ์: {tags}" if tags else "") + "</small>", "",
               "## ใช้ทำอะไร", "", r["ใช้ทำอะไร"].strip(), "",
               "## ใช้เมื่อ", "", r["ใช้เมื่อ"].strip(), ""]
        extra = r["ต่างจาก / ข้อควรรู้"].strip()
        if extra:
            out += ["## ต่างจาก / ข้อควรรู้", "", extra, ""]
        out += ["## วิธีเรียก", "", code(r["วิธีเรียก"]), "",
                "## ตัวอย่าง prompt", "", "```text", r["ตัวอย่าง prompt"].strip(), "```", ""]
        (SITE / d / f"{slug}.md").write_text("\n".join(out), encoding="utf-8")

    (SITE / "situations").mkdir()
    names_re = re.compile(r"\*\*(" + "|".join(re.escape(n) for n in sorted(link_of, key=len, reverse=True)) + r")\*\*")
    sit_titles = []
    for stem, slug in SITUATIONS.items():
        text = (PAGES / f"{stem}.md").read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        text = text.replace(" หน้านี้อ่านได้โดยไม่ต้องใช้ database", "")
        text = names_re.sub(lambda m: f"[**{m.group(1)}**]({link_of[m.group(1)]})", text)
        (SITE / "situations" / f"{slug}.md").write_text(text, encoding="utf-8")
        sit_titles.append((title, slug))

    readme = ["# PStack Playbook", "",
              "รวม skill, playbook และ principle ของ PStack ว่ามีอะไรบ้าง ใช้ทำอะไร และเรียกอย่างไร ค้นหาได้จากช่องค้นหาด้านซ้าย", ""]
    for typ, heading in (("Workflow skill", "Workflow skills"), ("Playbook", "Playbooks"), ("Principle", "Principles")):
        readme += [f"## {heading}", "", "| Name | ใช้ทำอะไร |", "|---|---|"]
        readme += [f"| [{r['Name'].strip()}](/{d}/{slug}.md) | {cell(r['ใช้ทำอะไร'])} |"
                   for r, d, slug in ents if r["ประเภท"].strip() == typ]
        readme.append("")
    (SITE / "README.md").write_text("\n".join(readme), encoding="utf-8")

    sb = ["- **หน้าแรก**", "  - [PStack Playbook](/README.md)", "", "- **ตามสถานการณ์**"]
    sb += [f"  - [{t}](/situations/{s}.md)" for t, s in sit_titles]
    for heading, d in (("Workflow skills", "skills"), ("Playbooks", "playbooks"), ("Principles", "principles")):
        items = [(short_of(r["Name"].strip()), slug) for r, dd, slug in ents if dd == d]
        if d != "playbooks":  # playbooks keep CSV (workflow) order
            items.sort(key=lambda x: x[0].lower())
        sb += ["", f"- **{heading}**"] + [f"  - [{n}](/{d}/{s}.md)" for n, s in items]
    (SITE / "_sidebar.md").write_text("\n".join(sb) + "\n", encoding="utf-8")

    broken = 0
    link_re = re.compile(r"\]\(([^)\s]+)\)")
    for md in [SITE / "_sidebar.md", SITE / "README.md", *sorted((SITE / "situations").glob("*.md"))]:
        for target in link_re.findall(md.read_text(encoding="utf-8")):
            if target.startswith(("http", "#")):
                continue
            if not (SITE / target.lstrip("/")).is_file():
                print(f"BROKEN: {md.relative_to(SITE)} -> {target}")
                broken += 1
    n_ent = sum(len(list((SITE / d).glob("*.md"))) for d in TYPES.values())
    n_sit = len(list((SITE / "situations").glob("*.md")))
    print(f"{n_ent} entity pages, {n_sit} situation pages, {broken} broken links")
    assert broken == 0, "broken links found"
    assert n_ent == len(rows), "entity page count mismatch"
    assert n_sit == len(SITUATIONS), "situation page count mismatch"


if __name__ == "__main__":
    sys.exit(main())
