# Refactor/เก็บกวาด

ใช้เมื่อเปลี่ยนโครงสร้างหรือเก็บกวาดโดยไม่เปลี่ยน behavior

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- [**Playbook: Refactoring**](/playbooks/refactoring) — ตรึง behavior ด้วย characterization test ก่อน แล้วเปลี่ยนเป็นก้าวเล็กและพิสูจน์ว่า behavior เดิม

   <PromptBlock compact text="/pstack:poteto-mode ย้ายโค้ด pricing จากสามไฟล์เข้า src/pricing/ โดย behavior ต้องไม่เปลี่ยนเลย บันทึก output ปัจจุบันก่อน แล้วพิสูจน์ว่าไม่เปลี่ยนหลังย้าย" />
- [**/pstack:deslop**](/skills/deslop) — ลบ comment เกินจำเป็น, defensive check และ cast `any` ที่ AI เพิ่มใน diff

   <PromptBlock compact text="/pstack:deslop ช่วยล้าง AI slop ใน branch นี้เทียบกับ main" />
- [**/pstack:no-comments**](/skills/no-comments) — ให้ reviewer ที่ไม่ได้เขียน comment ลบ comment และชี้ workaround

   <PromptBlock compact text="/pstack:no-comments review diff เทียบกับ main" />
- [**/pstack:principle-subtract-before-you-add**](/principles/subtract-before-you-add) — ลบ dead code และ validator ซ้ำซ้อนก่อนสร้างโครงใหม่

   <PromptBlock compact text="/pstack:poteto-mode เพิ่ม retry option ให้ client apply subtract before you add ลบ option ที่ไม่ได้ใช้ก่อน" />
- [**/pstack:correct**](/skills/correct) — ถ้าต้องแก้ agent เรื่องเดิมซ้ำๆ ให้แก้ที่ repo ด้วย type, lint หรือ test

   <PromptBlock compact text="/pstack:correct agent ชอบเพิ่ม config flag ใหม่โดยไม่ลงทะเบียนใน schema" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
