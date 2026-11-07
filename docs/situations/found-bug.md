# เจอ bug

ใช้เมื่อมี defect ที่รายงานมาและต้องการ repro, หา root cause และ fix ด้วยหลักฐาน

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- [**Playbook: Bug fix**](/playbooks/bug-fix) — ค่าเริ่มต้นสำหรับ bug: repro เอง, ไล่หา cause, fix และตรวจบน surface เดิม ให้ failing repro อยู่ก่อน fix ใน git history

   <PromptBlock compact text="/pstack:poteto-mode ตอน retry แล้ว export สร้างแถวซ้ำ ช่วย repro ให้เห็นก่อน แล้วค่อย fix และ verify" />
- [**/pstack:tdd**](/skills/tdd) — ถ้า bug มี test path ในเครื่องที่ถูกและชัด ให้เขียน test ที่ fail ก่อนแก้ ถ้าไม่ชัดให้ข้าม

   <PromptBlock compact text="/pstack:tdd เขียน regression test ที่ fail ก่อน สำหรับ bug ที่ export เขียนแถวซ้ำตอน retry แล้วค่อย fix ให้ test ผ่าน และ rerun เพื่อยืนยัน" />
- [**/pstack:why**](/skills/why) — ถ้า bug เพิ่งเกิดหลัง release ให้ดูประวัติการเปลี่ยนที่เกี่ยวข้อง

   <PromptBlock compact text="/pstack:why ทำไม export retry ถึงใช้ timeout 30 วินาที ช่วยดูประวัติและ incident ที่เกี่ยวข้อง" />
- [**/pstack:control-ui**](/skills/control-ui) — ใช้ repro bug ที่ต้องมี browser, focus หรือ rendering จริง (ส่วน CLI ใช้ control-cli)

   <PromptBlock compact text="/pstack:control-ui เปิดหน้า settings ในเครื่อง repro focus bug ที่เกิดหลังกด Tab และถ่าย screenshot ก่อนกับหลังแก้" />
- [**/pstack:principle-fix-root-causes**](/principles/fix-root-causes) — กัน agent จากการใส่ null check ที่ปิดเสียง crash โดยไม่แก้ต้นเหตุ

   <PromptBlock compact text="/pstack:poteto-mode หน้า profile crash เมื่อไม่มี avatar apply fix root causes อย่าแค่เติม null check" />

## ตัวอย่าง prompt รวม

<PromptBlock text="/pstack:poteto-mode ตอน retry แล้ว export สร้างแถวซ้ำ ช่วย repro ก่อน ถ้ามีทางเขียน test ที่ถูกให้ /pstack:tdd แล้วค่อย fix และ rerun" />

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
