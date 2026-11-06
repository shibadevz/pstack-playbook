# PStack Playbook

รวม skill, playbook และ principle ของ PStack ว่ามีอะไรบ้าง ใช้ทำอะไร และเรียกอย่างไร ค้นหาได้จากช่องค้นหาด้านซ้าย

## Workflow skills

| Name | ใช้ทำอะไร |
|---|---|
| [/pstack:architect](/skills/architect.md) | ร่าง type, signature และโครง module โดยให้ body เป็น `not implemented` ก่อน ให้หลาย candidate ออกแบบผ่าน arena แล้ว implement ตาม sketch ที่เลือก |
| [/pstack:arena](/skills/arena.md) | ให้ candidate N ตัวทำ brief เดียวกัน ให้ judge ข้าม model ตัดสิน เลือก base แล้วเก็บส่วนที่ดีที่สุดของตัวอื่นมาต่อเข้าไป |
| [/pstack:automate-me](/skills/automate-me.md) | ร่างหรืออัปเดต personal `-mode` skill จากนิสัยการทำงานของผู้ใช้ โดยขุดประวัติแชตล่าสุด ถามเพิ่ม แล้วเขียนผ่าน pstack-create-skill และ unslop |
| [/pstack:benchmark-checklist](/skills/benchmark-checklist.md) | ตรวจตัวเลข performance ด้วยคำถาม 7 ข้อ (limiter, tuning, เกิน limit, error, ทำซ้ำได้, สำคัญจริงไหม, งานเกิดขึ้นจริงไหม) ก่อนรายงานหรือนำไปใช้ ผลคือ faster, slower, no measurable difference หรือ inconclusive |
| [/pstack:blast-radius](/skills/blast-radius.md) | หาว่า change จะทำให้ที่อื่นพังตรงไหนนอก diff แล้วพิสูจน์ "fact เดียวที่ทำให้ change ปลอดภัย" ด้วยการรันโค้ดจริง ไม่ใช่แค่เขียนสรุป |
| [/pstack:bro](/skills/bro.md) | เล่าข้อความล่าสุดของ agent ใหม่เป็นภาษาคนธรรมดา สั้นลง ไม่มี jargon |
| [/pstack:control-cli](/skills/control-cli.md) | สร้างหรือปรับ harness ในเครื่อง (tmux หรือ PTY script) เพื่อขับ ตรวจ และ profile CLI/TUI แบบ interactive โดยไม่ต้องใช้ service ภายนอก |
| [/pstack:control-ui](/skills/control-ui.md) | สร้างหรือปรับ harness แบบ browser/CDP ในเครื่องเพื่อขับและตรวจ UI ของ web, IDE หรือ Electron พร้อม screenshot, accessibility snapshot, profile และ visual diff |
| [/pstack:correct](/skills/correct.md) | หาความผิดพลาดที่ agent ทำซ้ำใน repo แล้วทำให้เป็นไปไม่ได้ โดยลองระดับสูงสุดที่ใช้ได้ก่อน: architecture, type, lint ที่ error บอกวิธีแก้, test และเขียน docs เป็นอย่างสุดท้าย พร้อมพิสูจน์ว่า check ใหม่ fail กับความผิดพลาดจริงในอดีต |
| [/pstack:create-verification-skill](/skills/create-verification-skill.md) | สร้าง project-local skill ที่ `.claude/skills/verify-<app>/` ซึ่งสอน agent ขับ app จริงเหมือนผู้ใช้ (Launch, Doctor, Drive, Evidence, Cleanup) พร้อม feature map และพิสูจน์ว่าใช้ได้หนึ่งรอบก่อนส่งมอบ |
| [/pstack:deslop](/skills/deslop.md) | ลบ AI slop ที่เพิ่มใน branch เทียบกับ main เช่น comment เกินจำเป็น, defensive check ที่ผิดปกติ, การ cast เป็น `any` และ nesting ที่ลึกเกิน โดยรักษา behavior เดิม |
| [/pstack:figure-it-out](/skills/figure-it-out.md) | ออกแบบ playbook เฉพาะงานเมื่อไม่มี playbook ไหนพอดี: Frame, ออกแบบ workflow, วน loop แบบสมมติฐาน-วัด-เก็บหรือ revert และจดการตัดสินใจไว้ให้คนตรวจทีหลัง |
| [/pstack:how](/skills/how.md) | อธิบายว่าโค้ดทำงานอย่างไรในระดับ senior engineer ที่ onboard subsystem (Overview, Key Concepts, How It Works, Where Things Live, Gotchas) และตอบคำถามว่าโค้ดใหม่ควรอยู่ที่ไหนหรือ package ไหนเป็นเจ้าของ |
| [/pstack:in-your-own-words](/skills/in-your-own-words.md) | ให้ agent เล่าด้วยคำของตัวเองว่าเข้าใจเป้าหมายและปัญหาของผู้ใช้ว่าอะไร |
| [/pstack:interrogate](/skills/interrogate.md) | ให้ reviewer หลายตัว (หนึ่งตัวต่อ model ที่ตั้งค่าไว้) รีวิวการเปลี่ยนแปลงแบบ adversarial จากมุมอิสระ แล้วสรุป verdict ที่แยกเป็นหมวด act-on และ dismissed โดยไม่แก้โค้ดเอง |
| [/pstack:ketchup](/skills/ketchup.md) | ตามผู้ใช้ให้ทันสิ่งที่เปลี่ยนในแชตนี้ตั้งแต่ข้อความล่าสุดของเขา ด้วยประโยคสั้นๆ และ visual เล็กๆ พร้อมบริบทพอให้ตัดสินใจแต่ละ action item (reply ยาวไม่เกินประมาณ 150 คำ) |
| [/pstack:maintain-verification-skill](/skills/maintain-verification-skill.md) | รอบดูแลที่ทำให้ verification skill และ feature map ตรงกับ app: source reader ขนานต่อ feature, หนึ่ง session ขับทุก feature และส่ง PR แก้ที่พิสูจน์แล้วไม่เกินหนึ่งอัน ผลเป็น clean, changed หรือ blocked |
| [/pstack:make-bot-ui](/skills/make-bot-ui.md) | สร้างหน้า UI (page, dashboard, ปุ่ม) ที่เมื่อกดแล้ว server ในเครื่อง POST JSON ไปปลุก Grok Bot ผ่าน webhook โดยเก็บ sender key ไว้ฝั่ง server เท่านั้น |
| [/pstack:no-comments](/skills/no-comments.md) | spawn `pstack:comment-sicko` เพื่อลบ comment และชี้โค้ด workaround ใน diff แล้วแก้ finding ที่ยอมรับ และเสนอ encode constraint ที่ comment อ้างไว้เป็น type, test หรือ lint |
| [/pstack:poteto-help](/skills/poteto-help.md) | ตอบคำถามเรื่อง setup, `/pstack:poteto-mode` และการเลือก skill, playbook หรือ principle พร้อมให้ prompt ที่ส่งต่อได้และลิงก์ไปไฟล์ต้นทาง โดยไม่เริ่มงานจริง |
| [/pstack:poteto-mode](/skills/poteto-mode.md) | จับคู่งานกับ playbook, คัดลอกขั้นตอนของ playbook เข้า todo list แล้วเรียก skill อื่นตามที่ขั้นตอนต้องการ ขั้นที่ข้ามจะค้างใน list เป็น `skip: <reason>` |
| [/pstack:pstack-automate](/skills/pstack-automate.md) | ตั้งค่า automation source pack แบบ dormant (Benny) ไว้ใน `.pstack/automations/benny/` ผ่าน scheduler ที่ผู้ใช้อนุญาต แล้วรัน test report หนึ่งครั้งเพื่อพิสูจน์ |
| [/pstack:pstack-create-skill](/skills/pstack-create-skill.md) | เขียน project skill ที่ `.claude/skills/<name>/SKILL.md` พร้อม frontmatter (`name`, `description`), ลำดับขั้น, กรณี error และเงื่อนไขเสร็จที่ตรวจได้ แล้วลองเรียกใช้จริงกับงานเล็กหนึ่งครั้ง |
| [/pstack:recall](/skills/recall.md) | สร้าง context งานล่าสุดใหม่จากประวัติแชตของตัวเอง สถานะจริงใน git/gh และ "shared record" (user report, fix ที่ถูก revert, incident) แล้วคืน capsule สั้นๆ ว่าตอนนี้อยู่ตรงไหนและควรทำอะไรต่อ |
| [/pstack:reflect](/skills/reflect.md) | spawn reviewer สามตัวพร้อมกัน (judgment, tooling, divergent) ไล่ดู transcript ของแชตปัจจุบัน แล้วส่งบทเรียนแต่ละข้อไปเป็นการแก้ skill ที่มีอยู่ |
| [/pstack:setup-pstack](/skills/setup-pstack.md) | ตั้งค่าว่า pstack ใช้ model ไหนในแต่ละ role (17 role) และ reasoning budget ระดับไหน โดยตรวจ model ที่ launch ได้จริงแล้วเขียน `.pstack/claude/models.json` |
| [/pstack:sharpen](/skills/sharpen.md) | ยกระดับงานก่อนเริ่ม: ถามว่าผู้เชี่ยวชาญจะทำอย่างไร ผู้ใช้ต้องการอะไรจริงๆ และ spec ละเอียดพอดีหรือเกินไป พร้อมคลายข้อจำกัดที่ไม่ช่วยเป้าหมาย |
| [/pstack:show-me-your-work](/skills/show-me-your-work.md) | เก็บ decision trail เป็นไฟล์ TSV หนึ่งแถวต่อหนึ่งการตัดสินใจ (ts, phase, decision, why, evidence, result) และจบ reply ด้วยหัวข้อ Attention ที่ชี้ flag ตามแถวหรือจังหวะที่เกิด |
| [/pstack:swarm](/skills/swarm.md) | กระจาย worker N ตัวที่แยกกัน (ตามชิ้นงาน, แข่ง brief เดียวกัน หรือผสม) รอให้ครบแล้วรวมเป็นรายงานเดียวที่ใช้ `PASS`, `ISSUES` หรือ `BLOCKED` พร้อมหลักฐาน |
| [/pstack:tdd](/skills/tdd.md) | แก้ bug แบบ test-first: เขียน regression test ที่ fail ด้วยเหตุผลที่ถูกต้องก่อน แล้วแก้ production code ให้ผ่าน และถ้า test ไม่คุ้มก็ใช้ check ที่ใกล้เคียงที่สุดแทน |
| [/pstack:teach](/skills/teach.md) | อธิบายงานก้อนหนึ่ง (subsystem หรือ change) ให้ผู้ใช้เข้าใจจริง โดยรัน how และ why แล้วถักเป็นคำอธิบายเดียวที่เริ่มจากนิยามง่ายๆ แล้วต่อด้วยวาดภาพทีละขั้น |
| [/pstack:technical-writing](/skills/technical-writing.md) | มาตรฐานงานเขียนเทคนิคแบบหลายชั้น (Diátaxis, Google developer style, STE, Global English) สำหรับ docs, RFC, README, PR description และ commit message |
| [/pstack:typescript-best-practices](/skills/typescript-best-practices.md) | กฎ TypeScript สำหรับงาน `.ts`/`.tsx`: discriminated union, branded type, `unknown` แทน `any`, schema ก่อน type guard, ไม่ใช้ `as` cast และ exhaustive switch ซึ่งอ้างอิง principle type-system-discipline ก่อน |
| [/pstack:unslop](/skills/unslop.md) | ตัดร่องรอยแบบ AI ออกจากข้อความ เช่นคำฟุ่มเฟือย (additionally, crucial, delve), "serves as", rule of three และแหล่งอ้างอิงลอยๆ โดยคงความหมายและโทนเดิม |
| [/pstack:why](/skills/why.md) | สืบเหตุผลและเจตนาเบื้องหลังโค้ด: ค้นหลายแหล่งขนาน (source control, issue tracker, docs, chat, observability ฯลฯ ตาม MCP ที่มี) แล้วสรุปพร้อมอ้างอิงและบอกระดับความมั่นใจ |

## Playbooks

| Name | ใช้ทำอะไร |
|---|---|
| [Playbook: Investigation](/playbooks/investigation.md) | คำถามแบบอ่านอย่างเดียว (X ทำงานอย่างไร, ทำไม Y ถูกสร้างแบบนี้, แน่ใจไหมว่า Z, ควรทำ X หรือ Y) ได้คำอธิบายพร้อมอ้างอิงหรือคำแนะนำพร้อมตาราง tradeoff โดยไม่แก้โค้ด |
| [Playbook: Bug fix](/playbooks/bug-fix.md) | แก้ defect ที่รายงานมา: repro เองบน surface ที่ตรงกัน, ไล่หา cause แบบ binary search ด้วยหลักฐานตอนรัน, วางแผนและ delegate fix, ตรวจบน surface เดิมและ stage commit ให้ failing repro อยู่ก่อน fix |
| [Playbook: Perf issue](/playbooks/perf-issue.md) | แก้ความช้าที่วัดได้: จับ baseline trace, ตรวจ baseline ด้วย benchmark-checklist, ไล่ลองหลัก performance mantra เรียงจากถูกสุด, วัดหลังแก้ แล้วอ้างตัวเลขใน PR |
| [Playbook: Hillclimb](/playbooks/hillclimb.md) | ปรับปรุง metric เดียวอย่างต่อเนื่องและเป็นวิทยาศาสตร์จนถึงเป้า: วน loop สมมติฐานทีละอัน วัดก่อน-หลังด้วย harness ที่ freeze แล้ว บันทึก `decision.tsv` และ commit ต่อหนึ่ง win ที่ยอมรับ |
| [Playbook: Runtime forensics](/playbooks/runtime-forensics.md) | วินิจฉัยอาการตอนรัน (leak, idle-CPU spin, glitch) จาก instrumentation ของ process จริง ผลคือคำวินิจฉัยที่อ้างอิงได้ ไม่ใช่ fix |
| [Playbook: Trace forensics](/playbooks/trace-forensics.md) | วินิจฉัยจาก artifact ที่จับมาแล้ว (cpuprofile, trace, spindump, heap snapshot) โดย dump ลง sqlite เพื่อ query หาเส้นทางร้อนหรือ retainer chain แล้วอ้างถึง source |
| [Playbook: Feature](/playbooks/feature.md) | สร้างหรือเปลี่ยน behavior จากรูปข้อมูลที่ตั้งชื่อ: ใช้ how กับ subsystem, architect, เขียน throughput checkpoint, delegate โค้ดให้ subagent, ตรวจบน surface ที่ตรงกัน และ rebase เป็น commit เล็กเรียงลำดับ |
| [Playbook: Refactoring](/playbooks/refactoring.md) | เปลี่ยนโครงสร้างโดยไม่เปลี่ยน behavior (rename, extract, inline, dedupe, move): ตรึง behavior ด้วย characterization test ก่อน แล้วลบ ย้ายเป็นก้าวเล็ก และพิสูจน์ว่า behavior เดิมกับของจริง |
| [Playbook: Prototype](/playbooks/prototype.md) | ร่างต้นแบบทิ้งขว้างเพื่อตัดสินใจ design หรือ behavior อย่างถูก: สร้างใน scratch dir แยก, เทียบหลายแบบหลัง switcher เดียว, ถ่าย screenshot แล้วสรุปตัวเลือก tradeoff และคำแนะนำ |
| [Playbook: Visual parity](/playbooks/visual-parity.md) | ทำให้ UI เหมือนกันแบบ pixel-exact ระหว่างสอง implementation หรือเมื่อย้ายระบบ styling: สร้าง baseline ด้วย visual regression harness ก่อน แล้วย้ายทีละ component และตรวจด้วย image diff จนเป็นศูนย์ |
| [Playbook: Authoring or modifying a skill](/playbooks/authoring-or-modifying-a-skill.md) | เขียนหรือแก้ SKILL.md ผ่าน pstack-create-skill, validate frontmatter และ link อ้างอิง, ทำ test ถ้าเป็นโครงสร้าง และเปิด PR |
| [Playbook: Eval](/playbooks/eval.md) | ทดสอบว่าการเปลี่ยน skill, โครงสร้าง หรือ prompt ส่งผลต่อพฤติกรรม agent อย่างไรก่อนนำไปใช้ โดยทดลองแบบ blind: หลาย candidate บน prompt เดียวกัน, judge แบบ blind และตรวจ chain จาก transcript |
| [Playbook: Babysit](/playbooks/babysit.md) | ขับ PR หรือ stack ไปจนถึง merge-ready: ประกาศโหมด (drive, background, threads-only, check), เคลียร์ทีละ PR จากล่างสุด โดยเรียงลำดับ conflict, review thread, CI และหยุดตรงที่เป็นการตัดสินใจของมนุษย์ |
| [Playbook: Shipping](/playbooks/shipping.md) | ครึ่งหลังของ Babysit: ตรวจ PR ที่เขียวแต่ละอันแยกอิสระ แล้ว land เฉพาะช่วงที่ verified ต่อเนื่องจากล่างสุดขึ้นไป ทีละ PR ผ่าน `gh` (หรือ `origin` ถ้ามี) แล้วหยุดที่ ceiling |
| [Playbook: Autonomous run](/playbooks/autonomous-run.md) | ขับงานยาวงานเดียวจนถึงเงื่อนไขที่ตรวจได้โดยไม่หยุด: ตั้ง predicate, เลือกกลไกปลุก (scheduler หรือ watcher), ทำการเปลี่ยนเล็กที่สุดต่อ iteration และ checkpoint ลง log |
| [Playbook: Orchestrate](/playbooks/orchestrate.md) | ให้ coordinator แชตเดียวเป็นเจ้าของ program ใหญ่ (หลายวัน, PR ซ้อนกันมาก, subagent หลายสิบถึงร้อย): เขียน brief, ระบายคิว, รักษา frontier ให้เขียว และไม่เขียนโค้ดเอง |
| [Playbook: Autopilot-full](/playbooks/autopilot-full.md) | ผลักคิวของ PR อิสระจนถึง merged ด้วย autonomy เต็ม: หนึ่ง owner ต่อ PR ตั้งแต่ build ถึง merge และ root ใช้ swarm ที่ไม่เคยเขียนโค้ดตรวจก่อน owner merge |
| [Playbook: Autopilot-stack](/playbooks/autopilot-stack.md) | สร้างและตรวจคิวของการเปลี่ยนแปลงด้วย autonomy เต็ม แล้วส่งมอบเป็น stack เส้นตรงของ PR ที่ chain ด้วย base branch ให้ผู้ใช้รีวิวและ land เอง |
| [Playbook: Session pickup](/playbooks/session-pickup.md) | รับช่วงงานของ agent ก่อนหน้าจาก transcript, URL ของ cloud agent หรือ branch ที่ push แล้ว: อ่าน trail, สร้างสถานะใหม่, เทียบ done กับ pending และเริ่มจาก resume point โดยไม่ทำงานที่เสร็จซ้ำ |
| [Playbook: Pause safely](/playbooks/pause-safely.md) | หยุดงานที่ค้างอยู่อย่างสะอาดเพื่อให้กลับมาต่อได้: หยุดที่ขอบที่ปลอดภัย, commit เป็น `wip:` เดียว และเขียน resume note ที่ agent ที่เริ่มใหม่อ่านต่อได้ |
| [Playbook: Multi-phase or multi-PR plan](/playbooks/multi-phase-or-multi-pr-plan.md) | เขียนแผนสำหรับงานที่ข้ามหลาย phase หรือ PR ซ้อนกัน ให้เป็น checklist ที่ owner รันทีละช่องและผู้ใช้ตรวจจากหลักฐาน แผนคือ deliverable และไม่ implement |
| [Playbook: Worktree and simulator cleanup](/playbooks/worktree-and-simulator-cleanup.md) | เคลียร์พื้นที่ดิสก์ด้วยการ prune git worktree ที่ merge แล้วหรือถูกทิ้ง และ iOS simulator เก่า โดยตรวจการใช้งานก่อนลบ |
| [Playbook: Opening a PR](/playbooks/opening-a-pr.md) | ขั้นตอนเปิด PR ที่ใช้ปิดท้ายทุก playbook อื่น: ทำงานจาก worktree แยก, commit เล็กเรียงลำดับ, deslop และ no-comments ก่อนรีวิว, เขียน title แบบ Conventional Commits และ description 6 หัวข้อ (Why, What changed, Scope, Tradeoffs, Blast Radius, Verification) |

## Principles

| Name | ใช้ทำอะไร |
|---|---|
| [/pstack:principle-attack-the-premise](/principles/attack-the-premise.md) | เมื่อ fix สองอันขึ้นไปที่อยู่บน premise เดียวกันไม่ผ่าน gate เดิม ให้สำรวจก่อนว่า actor ไหนถือความไม่สมดุลอยู่ แล้วตั้งคำถามกับ premise แทนการเขียน fix ที่สามบน premise เดิม |
| [/pstack:principle-boundary-discipline](/principles/boundary-discipline.md) | วาง validation และ error handling ที่ขอบระบบ (CLI, config, network, external API) แล้วเชื่อ internal type และให้ business logic เป็น pure function |
| [/pstack:principle-build-the-lever](/principles/build-the-lever.md) | กับงาน non-trivial ทุกชนิด ให้สร้างเครื่องมือที่ทำหรือพิสูจน์งาน (codemod, script, generator หรือ skill ที่ subagent ทำตาม) แทนการทำมือ เครื่องมือคือ artifact ที่ผู้รีวิวรันซ้ำได้ |
| [/pstack:principle-encode-lessons-in-structure](/principles/encode-lessons-in-structure.md) | เมื่อเขียนคำสั่งเดิมซ้ำเป็นครั้งที่สอง หรือเห็นการแก้ที่เกิดซ้ำ ให้เข้ารหัสกฎเป็น lint, metadata flag, runtime check หรือ script แทนการเพิ่มข้อความ |
| [/pstack:principle-exhaust-the-design-space](/principles/exhaust-the-design-space.md) | เมื่อเจอ interaction ใหม่หรือการตัดสินใจเชิงสถาปัตยกรรมที่ไม่มีแบบอย่างใน codebase ให้ build prototype 2-3 แบบที่แข่งกันแล้วเทียบข้างกันก่อนตัดสินใจ |
| [/pstack:principle-experience-first](/principles/experience-first.md) | เมื่อต้องแลก product, UX หรือขอบเขตฟีเจอร์ ให้เลือกความพอใจของผู้ใช้เหนือความสะดวกของ implementation และส่งฟีเจอร์น้อยแต่เนี้ยบ ดีกว่ามากแต่หยาบ |
| [/pstack:principle-explain-the-number](/principles/explain-the-number.md) | ก่อนเชื่อ รายงาน หรือลงมือตามตัวเลขที่วัดมา (speedup, regression, throughput, latency, eval result) ให้หาสิ่งที่จำกัดตัวเลข และตัดความเป็นไปได้ว่าวัดสิ่งอื่นที่ไม่ใช่งานจริง |
| [/pstack:principle-fix-root-causes](/principles/fix-root-causes.md) | เวลา debug ให้ไล่แต่ละอาการไปถึง root cause แล้วแก้ที่นั่น: repro ก่อน ถาม why จนถึงต้นทาง และต้านการใส่ nil-check ที่แค่ปิดเสียง crash |
| [/pstack:principle-foundational-thinking](/principles/foundational-thinking.md) | ก่อนเขียน logic ให้เลือกชนิดข้อมูลและโครงข้อมูลหลัก ลำดับงานระหว่าง scaffold กับ feature และถามว่า actor พร้อมกันใช้อะไรร่วมกัน เพื่อให้โค้ดที่ตามมาชัดเจนเอง |
| [/pstack:principle-guard-the-context-window](/principles/guard-the-context-window.md) | เมื่อ context กำลังเต็ม (output ใหญ่ ไฟล์ยาว อ่านซ้ำ วางแผน fan-out) ให้ส่งงานก้อนใหญ่ให้ subagent และเก็บแค่สรุปใน main thread ไม่ใช่ payload ดิบ |
| [/pstack:principle-laziness-protocol](/principles/laziness-protocol.md) | เมื่อ refactor, ประเมินขนาด diff หรืออยากเพิ่ม abstraction, layer: เอนไปทางการลบและการเปลี่ยนที่เล็กที่สุดที่แก้ปัญหาได้ ตัดสินใจเรื่องเดียวกันที่เดียว |
| [/pstack:principle-make-operations-idempotent](/principles/make-operations-idempotent.md) | เมื่อออกแบบ command, lifecycle step หรือ loop ที่ทำงานท่ามกลาง crash, restart และ retry ให้บรรจบที่ end state เดียวกันไม่ว่าจะเคยรันค้างไว้แค่ไหน |
| [/pstack:principle-migrate-callers-then-delete-legacy-apis](/principles/migrate-callers-then-delete-legacy-apis.md) | เมื่อเพิ่ม internal API ใหม่แต่ยังมี caller เก่า ให้ย้าย caller และลบ API เก่าใน wave เดียวกัน แทนการเก็บ compatibility layer |
| [/pstack:principle-minimize-reader-load](/principles/minimize-reader-load.md) | เมื่อรีวิวหรือปรับโค้ดที่ตามยาก ให้นับ layer ระหว่างคำถามกับคำตอบและ hidden state ในหัวผู้อ่าน แล้วยุบ wrapper ที่มี caller เดียวและลด scope ของ mutable state |
| [/pstack:principle-model-the-domain](/principles/model-the-domain.md) | เมื่อเขียน logic ที่มี state หรือโค้ดแตกแขนงมากและซ้ำการสมมติรูปข้อมูลหลายไฟล์ ให้ใส่ domain ลงโครงสร้าง (state machine, typed model, table/registry) แทนเงื่อนไขกระจัดกระจาย |
| [/pstack:principle-never-block-on-the-human](/principles/never-block-on-the-human.md) | เมื่ออยากถามว่า "ทำ X ดีไหม" กับงานที่ย้อนกลับได้ ให้ทำไปแล้วอธิบายเหตุผล ให้มนุษย์แก้ทางทีหลัง ส่วนงานย้อนกลับไม่ได้ (force-push, ลบ data จริง, ส่งข้อความออกนอก) ยังต้องขออนุญาต |
| [/pstack:principle-outcome-oriented-execution](/principles/outcome-oriented-execution.md) | ใน rewrite หรือ migration ที่วางแผนไว้มี phase ชัด ให้มุ่งไปที่สถาปัตยกรรมเป้าหมาย ไม่ต้องรักษาสถานะระหว่างทางให้ราบรื่นด้วยโค้ดชั่วคราว |
| [/pstack:principle-prove-it-works](/principles/prove-it-works.md) | หลังงานเสร็จและก่อนประกาศว่าเสร็จ ให้ตรวจกับของจริง (รัน feature, อ่านค่าที่เก็บจริง, ดู diff) ไม่ใช่ proxy, self-report หรือ "compile ผ่าน" |
| [/pstack:principle-redesign-from-first-principles](/principles/redesign-from-first-principles.md) | เมื่อใส่ requirement ใหม่ลงใน design เดิม ให้ออกแบบใหม่เหมือน requirement นั้นเป็นข้อสมมติฐานตั้งแต่วันแรก ส่งผลไปทุกจุดที่อ้างถึง (type, docs, ตัวอย่าง) และคิดทั้ง redesign แล้วส่งมอบทีละส่วน |
| [/pstack:principle-separate-before-serializing-shared-state](/principles/separate-before-serializing-shared-state.md) | เมื่อ actor พร้อมกันอาจเขียนไฟล์, branch, key หรือ state object เดียวกัน ให้กำจัดการแชร์ก่อน และใช้ serialize ก็ต่อเมื่อ writer เดียวร่วมเป็น invariant จริง |
| [/pstack:principle-sequence-verifiable-units](/principles/sequence-verifiable-units.md) | กับงานหลายขั้น (sweep, migration, edit ซ้ำๆ) และการ stack commit/PR ให้แตกเป็นหน่วยเล็กที่จบด้วยสถานะที่ตรวจได้ ตรวจแต่ละหน่วยก่อนไปหน่วยถัดไป และเรียงการส่งมอบให้ลำดับพิสูจน์ตัวเองให้ผู้รีวิวเห็น |
| [/pstack:principle-subtract-before-you-add](/principles/subtract-before-you-add.md) | เมื่อจะเพิ่ม, refactor หรือ rewrite ให้ลบก่อน (dead code, validator ซ้ำซ้อน, stub ที่ไม่มีเนื้อหา) แล้วค่อยสร้างบนฐานที่ง่ายกว่า |
| [/pstack:principle-test-behavior-not-implementation](/principles/test-behavior-not-implementation.md) | เมื่อเขียน แก้ หรือคง test ให้เรียกโค้ดแบบที่ผู้ใช้เรียกและ assert ผลที่ผู้ใช้เห็นจริง และเขียนใหม่หรือลบ test ที่ยังผ่านแม้ทุก function ที่ import คืน undefined |
| [/pstack:principle-type-system-discipline](/principles/type-system-discipline.md) | เมื่อออกแบบ type หรือ signature ในภาษา static type ให้ทำให้ state ที่เป็นไปไม่ได้แสดงไม่ได้ brand primitive ที่มีความหมาย parse ข้อมูลภายนอกที่ขอบ ไม่โกหก compiler และ exhaust ทุก variant |
