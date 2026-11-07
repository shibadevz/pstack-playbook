---
pageClass: overview overview-cmd
---

# Workflow skills

| คำสั่ง | ใช้ทำอะไร |
|---|---|
| [/pstack:architect](/skills/architect) | ร่าง type, signature และโครง module โดยให้ body เป็น `not implemented` ก่อน ให้หลาย candidate ออกแบบผ่าน arena แล้ว implement ตาม sketch ที่เลือก |
| [/pstack:arena](/skills/arena) | ให้ candidate N ตัวทำ brief เดียวกัน ให้ judge ข้าม model ตัดสิน เลือก base แล้วเก็บส่วนที่ดีที่สุดของตัวอื่นมาต่อเข้าไป |
| [/pstack:automate-me](/skills/automate-me) | ร่างหรืออัปเดต personal `-mode` skill จากนิสัยการทำงานของผู้ใช้ โดยขุดประวัติแชตล่าสุด ถามเพิ่ม แล้วเขียนผ่าน pstack-create-skill และ unslop |
| [/pstack:benchmark-checklist](/skills/benchmark-checklist) | ตรวจตัวเลข performance ด้วยคำถาม 7 ข้อ (limiter, tuning, เกิน limit, error, ทำซ้ำได้, สำคัญจริงไหม, งานเกิดขึ้นจริงไหม) ก่อนรายงานหรือนำไปใช้ ผลคือ faster, slower, no measurable difference หรือ inconclusive |
| [/pstack:blast-radius](/skills/blast-radius) | หาว่า change จะทำให้ที่อื่นพังตรงไหนนอก diff แล้วพิสูจน์ "fact เดียวที่ทำให้ change ปลอดภัย" ด้วยการรันโค้ดจริง ไม่ใช่แค่เขียนสรุป |
| [/pstack:bro](/skills/bro) | เล่าข้อความล่าสุดของ agent ใหม่เป็นภาษาคนธรรมดา สั้นลง ไม่มี jargon |
| [/pstack:control-cli](/skills/control-cli) | สร้างหรือปรับ harness ในเครื่อง (tmux หรือ PTY script) เพื่อขับ ตรวจ และ profile CLI/TUI แบบ interactive โดยไม่ต้องใช้ service ภายนอก |
| [/pstack:control-ui](/skills/control-ui) | สร้างหรือปรับ harness แบบ browser/CDP ในเครื่องเพื่อขับและตรวจ UI ของ web, IDE หรือ Electron พร้อม screenshot, accessibility snapshot, profile และ visual diff |
| [/pstack:correct](/skills/correct) | หาความผิดพลาดที่ agent ทำซ้ำใน repo แล้วทำให้เป็นไปไม่ได้ โดยลองระดับสูงสุดที่ใช้ได้ก่อน: architecture, type, lint ที่ error บอกวิธีแก้, test และเขียน docs เป็นอย่างสุดท้าย พร้อมพิสูจน์ว่า check ใหม่ fail กับความผิดพลาดจริงในอดีต |
| [/pstack:create-verification-skill](/skills/create-verification-skill) | สร้าง project-local skill ที่ `.claude/skills/verify-<app>/` ซึ่งสอน agent ขับ app จริงเหมือนผู้ใช้ (Launch, Doctor, Drive, Evidence, Cleanup) พร้อม feature map และพิสูจน์ว่าใช้ได้หนึ่งรอบก่อนส่งมอบ |
| [/pstack:deslop](/skills/deslop) | ลบ AI slop ที่เพิ่มใน branch เทียบกับ main เช่น comment เกินจำเป็น, defensive check ที่ผิดปกติ, การ cast เป็น `any` และ nesting ที่ลึกเกิน โดยรักษา behavior เดิม |
| [/pstack:figure-it-out](/skills/figure-it-out) | ออกแบบ playbook เฉพาะงานเมื่อไม่มี playbook ไหนพอดี: Frame, ออกแบบ workflow, วน loop แบบสมมติฐาน-วัด-เก็บหรือ revert และจดการตัดสินใจไว้ให้คนตรวจทีหลัง |
| [/pstack:how](/skills/how) | อธิบายว่าโค้ดทำงานอย่างไรในระดับ senior engineer ที่ onboard subsystem (Overview, Key Concepts, How It Works, Where Things Live, Gotchas) และตอบคำถามว่าโค้ดใหม่ควรอยู่ที่ไหนหรือ package ไหนเป็นเจ้าของ |
| [/pstack:in-your-own-words](/skills/in-your-own-words) | ให้ agent เล่าด้วยคำของตัวเองว่าเข้าใจเป้าหมายและปัญหาของผู้ใช้ว่าอะไร |
| [/pstack:interrogate](/skills/interrogate) | ให้ reviewer หลายตัว (หนึ่งตัวต่อ model ที่ตั้งค่าไว้) รีวิวการเปลี่ยนแปลงแบบ adversarial จากมุมอิสระ แล้วสรุป verdict ที่แยกเป็นหมวด act-on และ dismissed โดยไม่แก้โค้ดเอง |
| [/pstack:ketchup](/skills/ketchup) | ตามผู้ใช้ให้ทันสิ่งที่เปลี่ยนในแชตนี้ตั้งแต่ข้อความล่าสุดของเขา ด้วยประโยคสั้นๆ และ visual เล็กๆ พร้อมบริบทพอให้ตัดสินใจแต่ละ action item (reply ยาวไม่เกินประมาณ 150 คำ) |
| [/pstack:maintain-verification-skill](/skills/maintain-verification-skill) | รอบดูแลที่ทำให้ verification skill และ feature map ตรงกับ app: source reader ขนานต่อ feature, หนึ่ง session ขับทุก feature และส่ง PR แก้ที่พิสูจน์แล้วไม่เกินหนึ่งอัน ผลเป็น clean, changed หรือ blocked |
| [/pstack:make-bot-ui](/skills/make-bot-ui) | สร้างหน้า UI (page, dashboard, ปุ่ม) ที่เมื่อกดแล้ว server ในเครื่อง POST JSON ไปปลุก Grok Bot ผ่าน webhook โดยเก็บ sender key ไว้ฝั่ง server เท่านั้น |
| [/pstack:no-comments](/skills/no-comments) | spawn `pstack:comment-sicko` เพื่อลบ comment และชี้โค้ด workaround ใน diff แล้วแก้ finding ที่ยอมรับ และเสนอ encode constraint ที่ comment อ้างไว้เป็น type, test หรือ lint |
| [/pstack:poteto-help](/skills/poteto-help) | ตอบคำถามเรื่อง setup, `/pstack:poteto-mode` และการเลือก skill, playbook หรือ principle พร้อมให้ prompt ที่ส่งต่อได้และลิงก์ไปไฟล์ต้นทาง โดยไม่เริ่มงานจริง |
| [/pstack:poteto-mode](/skills/poteto-mode) | จับคู่งานกับ playbook, คัดลอกขั้นตอนของ playbook เข้า todo list แล้วเรียก skill อื่นตามที่ขั้นตอนต้องการ ขั้นที่ข้ามจะค้างใน list เป็น `skip: <reason>` |
| [/pstack:pstack-automate](/skills/pstack-automate) | ตั้งค่า automation source pack แบบ dormant (Benny) ไว้ใน `.pstack/automations/benny/` ผ่าน scheduler ที่ผู้ใช้อนุญาต แล้วรัน test report หนึ่งครั้งเพื่อพิสูจน์ |
| [/pstack:pstack-create-skill](/skills/pstack-create-skill) | เขียน project skill ที่ `.claude/skills/<name>/SKILL.md` พร้อม frontmatter (`name`, `description`), ลำดับขั้น, กรณี error และเงื่อนไขเสร็จที่ตรวจได้ แล้วลองเรียกใช้จริงกับงานเล็กหนึ่งครั้ง |
| [/pstack:recall](/skills/recall) | สร้าง context งานล่าสุดใหม่จากประวัติแชตของตัวเอง สถานะจริงใน git/gh และ "shared record" (user report, fix ที่ถูก revert, incident) แล้วคืน capsule สั้นๆ ว่าตอนนี้อยู่ตรงไหนและควรทำอะไรต่อ |
| [/pstack:reflect](/skills/reflect) | spawn reviewer สามตัวพร้อมกัน (judgment, tooling, divergent) ไล่ดู transcript ของแชตปัจจุบัน แล้วส่งบทเรียนแต่ละข้อไปเป็นการแก้ skill ที่มีอยู่ |
| [/pstack:setup-pstack](/skills/setup-pstack) | ตั้งค่าว่า pstack ใช้ model ไหนในแต่ละ role (17 role) และ reasoning budget ระดับไหน โดยตรวจ model ที่ launch ได้จริงแล้วเขียน `.pstack/claude/models.json` |
| [/pstack:sharpen](/skills/sharpen) | ยกระดับงานก่อนเริ่ม: ถามว่าผู้เชี่ยวชาญจะทำอย่างไร ผู้ใช้ต้องการอะไรจริงๆ และ spec ละเอียดพอดีหรือเกินไป พร้อมคลายข้อจำกัดที่ไม่ช่วยเป้าหมาย |
| [/pstack:show-me-your-work](/skills/show-me-your-work) | เก็บ decision trail เป็นไฟล์ TSV หนึ่งแถวต่อหนึ่งการตัดสินใจ (ts, phase, decision, why, evidence, result) และจบ reply ด้วยหัวข้อ Attention ที่ชี้ flag ตามแถวหรือจังหวะที่เกิด |
| [/pstack:swarm](/skills/swarm) | กระจาย worker N ตัวที่แยกกัน (ตามชิ้นงาน, แข่ง brief เดียวกัน หรือผสม) รอให้ครบแล้วรวมเป็นรายงานเดียวที่ใช้ `PASS`, `ISSUES` หรือ `BLOCKED` พร้อมหลักฐาน |
| [/pstack:tdd](/skills/tdd) | แก้ bug แบบ test-first: เขียน regression test ที่ fail ด้วยเหตุผลที่ถูกต้องก่อน แล้วแก้ production code ให้ผ่าน และถ้า test ไม่คุ้มก็ใช้ check ที่ใกล้เคียงที่สุดแทน |
| [/pstack:teach](/skills/teach) | อธิบายงานก้อนหนึ่ง (subsystem หรือ change) ให้ผู้ใช้เข้าใจจริง โดยรัน how และ why แล้วถักเป็นคำอธิบายเดียวที่เริ่มจากนิยามง่ายๆ แล้วต่อด้วยวาดภาพทีละขั้น |
| [/pstack:technical-writing](/skills/technical-writing) | มาตรฐานงานเขียนเทคนิคแบบหลายชั้น (Diátaxis, Google developer style, STE, Global English) สำหรับ docs, RFC, README, PR description และ commit message |
| [/pstack:typescript-best-practices](/skills/typescript-best-practices) | กฎ TypeScript สำหรับงาน `.ts`/`.tsx`: discriminated union, branded type, `unknown` แทน `any`, schema ก่อน type guard, ไม่ใช้ `as` cast และ exhaustive switch ซึ่งอ้างอิง principle type-system-discipline ก่อน |
| [/pstack:unslop](/skills/unslop) | ตัดร่องรอยแบบ AI ออกจากข้อความ เช่นคำฟุ่มเฟือย (additionally, crucial, delve), "serves as", rule of three และแหล่งอ้างอิงลอยๆ โดยคงความหมายและโทนเดิม |
| [/pstack:why](/skills/why) | สืบเหตุผลและเจตนาเบื้องหลังโค้ด: ค้นหลายแหล่งขนาน (source control, issue tracker, docs, chat, observability ฯลฯ ตาม MCP ที่มี) แล้วสรุปพร้อมอ้างอิงและบอกระดับความมั่นใจ |
