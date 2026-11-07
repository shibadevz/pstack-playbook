# เขียนเอกสาร/สื่อสาร

ใช้เมื่อต้องเขียนหรือเล่าให้คนอ่านเข้าใจ เช่น docs, PR description หรือ reply ของ agent

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:technical-writing**](/skills/technical-writing) — มาตรฐานเขียน docs, RFC, README, PR description และ commit message.

   <PromptBlock compact text="/pstack:technical-writing เขียน PR description สำหรับ branch นี้ ให้มี why, what changed, scope, blast radius และ verification" />
2. [**/pstack:unslop**](/skills/unslop) — ตัวคำและรูปประโยคที่ดูเหมือน AI เขียนออกจากข้อความ.

   <PromptBlock compact text="/pstack:unslop ข้อความนั้น ไม่เอา emdash" />
3. [**/pstack:bro**](/skills/bro) — ให้ agent เล่า reply ล่าสุดใหม่เป็นภาษาคนธรรมดาและสั้นลง.

   <PromptBlock compact text="/pstack:bro ช่วยเล่าข้อความล่าสุดเป็นภาษาคนธรรมดา สั้นๆ ไม่มี jargon" />
4. [**/pstack:ketchup**](/skills/ketchup) — สรุปสิ่งที่เปลี่ยนในแชตตั้งแต่ข้อความล่าสุดของคุณ.

   <PromptBlock compact text="/pstack:ketchup ช่วยตามให้ทันว่าในแชตนี้มีอะไรเปลี่ยนไปบ้าง" />

## ตัวอย่าง prompt รวม

<PromptBlock text="/pstack:technical-writing เขียนหัวข้อ README ที่อธิบายวิธีรันคำสั่ง export แล้ว /pstack:unslop อีกรอบ" />

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
