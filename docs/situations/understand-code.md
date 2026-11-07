# เข้าใจโค้ด

ใช้เมื่อต้องรู้ก่อนว่าโค้ดทำงานอย่างไรหรือทำไมถึงเป็นแบบนี้ และยังไม่ต้องการแก้อะไร

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:how**](/skills/how) — อธิบายกลไกปัจจุบันของ subsystem เช่น flow ของ scheduler และ Where Things Live.

   <PromptBlock compact text="/pstack:how อธิบายว่า job scheduler ใน src/scheduler/ ทำงานอย่างไร ตั้งแต่ flow หลัก ไฟล์ที่เกี่ยวข้อง ไปจนถึง gotcha ที่ควรระวัง ก่อนที่ฉันจะแก้ แล้วใช้ /pstack:why หาว่าทำไมมันพังเมื่อไม่นานมานี้" />
2. [**/pstack:why**](/skills/why) — สืบเหตุผลจาก git, issue และแหล่งอื่นที่มี เช่นทำไม timeout เป็น 30 วินาที.

   <PromptBlock compact text="/pstack:why ทำไม export retry ถึงใช้ timeout 30 วินาที ช่วยดูประวัติและ incident ที่เกี่ยวข้อง" />
3. [**/pstack:teach**](/skills/teach) — เรียก how และ why แล้วถักเป็นคำอธิบายเดียวที่เข้าใจง่าย เหมาะเมื่อเป้าหมายคือเข้าใจ ไม่ใช่แก้.

   <PromptBlock compact text="/pstack:teach ช่วยอธิบายว่าทำไมคุณ implement แบบนี้ ไม่ใช้ queue แลกอะไรไปบ้าง" />
4. [**/pstack:recall**](/skills/recall) — เปิดแชตใหม่แล้วอยากได้ context งานสัปดาห์ก่อนจากประวัติแชตและสถานะ git.

   <PromptBlock compact text="/pstack:recall งานของฉันเรื่อง export pipeline เมื่อสัปดาห์ที่แล้ว แล้วอ่าน open issue เรื่องแถวซ้ำ" />
5. [**Playbook: Investigation**](/playbooks/investigation) — คำถามแบบอ่านอย่างเดียวภายใต้ poteto-mode ได้ผลสรุปที่อ้างอิงได้โดยไม่มีโค้ดเปลี่ยน.

   <PromptBlock compact text="/pstack:poteto-mode ช่วยสืบว่าทำไม export retry สามครั้งก่อน fail บอกว่าเรารู้อะไรบ้าง ใช้ data อะไร และ hypothesis ที่ดีที่สุดคืออะไร ยังไม่ต้องแก้โค้ด" />

## ตัวอย่าง prompt รวม

<PromptBlock text="ใช้ /pstack:how เพื่อทำความเข้าใจ job scheduler ใน src/scheduler/ แล้วใช้ /pstack:why หาว่าทำไมมันพังเมื่อไม่นานมานี้" />

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
