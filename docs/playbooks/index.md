---
pageClass: overview overview-cmd
---

# Playbooks

| คำสั่ง | ใช้ทำอะไร |
|---|---|
| [Investigation](/playbooks/investigation) | คำถามแบบอ่านอย่างเดียว (X ทำงานอย่างไร, ทำไม Y ถูกสร้างแบบนี้, แน่ใจไหมว่า Z, ควรทำ X หรือ Y) ได้คำอธิบายพร้อมอ้างอิงหรือคำแนะนำพร้อมตาราง tradeoff โดยไม่แก้โค้ด |
| [Bug fix](/playbooks/bug-fix) | แก้ defect ที่รายงานมา: repro เองบน surface ที่ตรงกัน, ไล่หา cause แบบ binary search ด้วยหลักฐานตอนรัน, วางแผนและ delegate fix, ตรวจบน surface เดิมและ stage commit ให้ failing repro อยู่ก่อน fix |
| [Perf issue](/playbooks/perf-issue) | แก้ความช้าที่วัดได้: จับ baseline trace, ตรวจ baseline ด้วย benchmark-checklist, ไล่ลองหลัก performance mantra เรียงจากถูกสุด, วัดหลังแก้ แล้วอ้างตัวเลขใน PR |
| [Hillclimb](/playbooks/hillclimb) | ปรับปรุง metric เดียวอย่างต่อเนื่องและเป็นวิทยาศาสตร์จนถึงเป้า: วน loop สมมติฐานทีละอัน วัดก่อน-หลังด้วย harness ที่ freeze แล้ว บันทึก `decision.tsv` และ commit ต่อหนึ่ง win ที่ยอมรับ |
| [Runtime forensics](/playbooks/runtime-forensics) | วินิจฉัยอาการตอนรัน (leak, idle-CPU spin, glitch) จาก instrumentation ของ process จริง ผลคือคำวินิจฉัยที่อ้างอิงได้ ไม่ใช่ fix |
| [Trace forensics](/playbooks/trace-forensics) | วินิจฉัยจาก artifact ที่จับมาแล้ว (cpuprofile, trace, spindump, heap snapshot) โดย dump ลง sqlite เพื่อ query หาเส้นทางร้อนหรือ retainer chain แล้วอ้างถึง source |
| [Feature](/playbooks/feature) | สร้างหรือเปลี่ยน behavior จากรูปข้อมูลที่ตั้งชื่อ: ใช้ how กับ subsystem, architect, เขียน throughput checkpoint, delegate โค้ดให้ subagent, ตรวจบน surface ที่ตรงกัน และ rebase เป็น commit เล็กเรียงลำดับ |
| [Refactoring](/playbooks/refactoring) | เปลี่ยนโครงสร้างโดยไม่เปลี่ยน behavior (rename, extract, inline, dedupe, move): ตรึง behavior ด้วย characterization test ก่อน แล้วลบ ย้ายเป็นก้าวเล็ก และพิสูจน์ว่า behavior เดิมกับของจริง |
| [Prototype](/playbooks/prototype) | ร่างต้นแบบทิ้งขว้างเพื่อตัดสินใจ design หรือ behavior อย่างถูก: สร้างใน scratch dir แยก, เทียบหลายแบบหลัง switcher เดียว, ถ่าย screenshot แล้วสรุปตัวเลือก tradeoff และคำแนะนำ |
| [Visual parity](/playbooks/visual-parity) | ทำให้ UI เหมือนกันแบบ pixel-exact ระหว่างสอง implementation หรือเมื่อย้ายระบบ styling: สร้าง baseline ด้วย visual regression harness ก่อน แล้วย้ายทีละ component และตรวจด้วย image diff จนเป็นศูนย์ |
| [Authoring or modifying a skill](/playbooks/authoring-or-modifying-a-skill) | เขียนหรือแก้ SKILL.md ผ่าน pstack-create-skill, validate frontmatter และ link อ้างอิง, ทำ test ถ้าเป็นโครงสร้าง และเปิด PR |
| [Eval](/playbooks/eval) | ทดสอบว่าการเปลี่ยน skill, โครงสร้าง หรือ prompt ส่งผลต่อพฤติกรรม agent อย่างไรก่อนนำไปใช้ โดยทดลองแบบ blind: หลาย candidate บน prompt เดียวกัน, judge แบบ blind และตรวจ chain จาก transcript |
| [Babysit](/playbooks/babysit) | ขับ PR หรือ stack ไปจนถึง merge-ready: ประกาศโหมด (drive, background, threads-only, check), เคลียร์ทีละ PR จากล่างสุด โดยเรียงลำดับ conflict, review thread, CI และหยุดตรงที่เป็นการตัดสินใจของมนุษย์ |
| [Shipping](/playbooks/shipping) | ครึ่งหลังของ Babysit: ตรวจ PR ที่เขียวแต่ละอันแยกอิสระ แล้ว land เฉพาะช่วงที่ verified ต่อเนื่องจากล่างสุดขึ้นไป ทีละ PR ผ่าน `gh` (หรือ `origin` ถ้ามี) แล้วหยุดที่ ceiling |
| [Autonomous run](/playbooks/autonomous-run) | ขับงานยาวงานเดียวจนถึงเงื่อนไขที่ตรวจได้โดยไม่หยุด: ตั้ง predicate, เลือกกลไกปลุก (scheduler หรือ watcher), ทำการเปลี่ยนเล็กที่สุดต่อ iteration และ checkpoint ลง log |
| [Orchestrate](/playbooks/orchestrate) | ให้ coordinator แชตเดียวเป็นเจ้าของ program ใหญ่ (หลายวัน, PR ซ้อนกันมาก, subagent หลายสิบถึงร้อย): เขียน brief, ระบายคิว, รักษา frontier ให้เขียว และไม่เขียนโค้ดเอง |
| [Autopilot-full](/playbooks/autopilot-full) | ผลักคิวของ PR อิสระจนถึง merged ด้วย autonomy เต็ม: หนึ่ง owner ต่อ PR ตั้งแต่ build ถึง merge และ root ใช้ swarm ที่ไม่เคยเขียนโค้ดตรวจก่อน owner merge |
| [Autopilot-stack](/playbooks/autopilot-stack) | สร้างและตรวจคิวของการเปลี่ยนแปลงด้วย autonomy เต็ม แล้วส่งมอบเป็น stack เส้นตรงของ PR ที่ chain ด้วย base branch ให้ผู้ใช้รีวิวและ land เอง |
| [Session pickup](/playbooks/session-pickup) | รับช่วงงานของ agent ก่อนหน้าจาก transcript, URL ของ cloud agent หรือ branch ที่ push แล้ว: อ่าน trail, สร้างสถานะใหม่, เทียบ done กับ pending และเริ่มจาก resume point โดยไม่ทำงานที่เสร็จซ้ำ |
| [Pause safely](/playbooks/pause-safely) | หยุดงานที่ค้างอยู่อย่างสะอาดเพื่อให้กลับมาต่อได้: หยุดที่ขอบที่ปลอดภัย, commit เป็น `wip:` เดียว และเขียน resume note ที่ agent ที่เริ่มใหม่อ่านต่อได้ |
| [Multi-phase or multi-PR plan](/playbooks/multi-phase-or-multi-pr-plan) | เขียนแผนสำหรับงานที่ข้ามหลาย phase หรือ PR ซ้อนกัน ให้เป็น checklist ที่ owner รันทีละช่องและผู้ใช้ตรวจจากหลักฐาน แผนคือ deliverable และไม่ implement |
| [Worktree and simulator cleanup](/playbooks/worktree-and-simulator-cleanup) | เคลียร์พื้นที่ดิสก์ด้วยการ prune git worktree ที่ merge แล้วหรือถูกทิ้ง และ iOS simulator เก่า โดยตรวจการใช้งานก่อนลบ |
| [Opening a PR](/playbooks/opening-a-pr) | ขั้นตอนเปิด PR ที่ใช้ปิดท้ายทุก playbook อื่น: ทำงานจาก worktree แยก, commit เล็กเรียงลำดับ, deslop และ no-comments ก่อนรีวิว, เขียน title แบบ Conventional Commits และ description 6 หัวข้อ (Why, What changed, Scope, Tradeoffs, Blast Radius, Verification) |
