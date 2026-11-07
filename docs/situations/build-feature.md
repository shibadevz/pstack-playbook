# สร้างฟีเจอร์

ใช้เมื่อต้องเพิ่มหรือเปลี่ยน behavior ใหม่

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Feature**](/playbooks/feature) — ค่าเริ่มต้น: ใช้ how กับ subsystem, ออกแบบ, delegate โค้ด และตรวจบน surface ที่ตรงกัน.

   <PromptBlock compact text="/pstack:poteto-mode เพิ่ม flag --json ให้คำสั่ง export ผลลัพธ์แบบ text ต้องเหมือนเดิมแบบ byte-identical และ verify ทั้งสองแบบ" />
2. [**/pstack:architect**](/skills/architect) — ถ้า change ข้าม function boundary ให้ร่าง type และ module ก่อนเขียนโค้ด.

   <PromptBlock compact text="/pstack:architect with checkpoint ช่วยร่าง type และ module boundary ของ retry queue ใน src/jobs/ แล้วให้ดู design ก่อนค่อย implement" />
3. [**/pstack:arena**](/skills/arena) — ถ้า implementation มีหลายรูปแบบที่ใช้ได้ ให้หลาย candidate ทำแล้วเลือก base.

   <PromptBlock compact text="/pstack:arena ขอความเห็นที่สองเรื่อง design ของ thread นี้ ให้ candidate หลายตัวทำจาก brief เดียวกัน แล้วให้ judge ต่าง model เลือกแนวทางที่ดีที่สุดพร้อมเก็บส่วนดีของตัวอื่นมารวม" />
4. [**/pstack:principle-model-the-domain**](/principles/model-the-domain) — เมื่อ logic มี state หรือเงื่อนไขกระจัดกระจาย ให้ใส่ domain ลงโครงสร้างก่อนเขียน.

   <PromptBlock compact text="/pstack:poteto-mode ตอนนี้สถานะ order เป็น boolean หกตัว apply model the domain แล้วแทนที่ด้วย state machine ที่ชัดเจน" />
5. [**/pstack:typescript-best-practices**](/skills/typescript-best-practices) — ถ้างานอยู่ในไฟล์ `.ts` หรือ `.tsx`.

   <PromptBlock compact text="/pstack:typescript-best-practices ปรับ type ใน src/api/response.ts ให้เข้มงวดขึ้น ใช้ discriminated union และ unknown แทน any โดยไม่เปลี่ยน behavior" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
