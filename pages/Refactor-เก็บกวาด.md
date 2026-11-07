# Refactor/เก็บกวาด

ใช้เมื่อเปลี่ยนโครงสร้างหรือเก็บกวาดโดยไม่เปลี่ยน behavior หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- **Playbook: Refactoring** — ตรึง behavior ด้วย characterization test ก่อน แล้วเปลี่ยนเป็นก้าวเล็กและพิสูจน์ว่า behavior เดิม. วิธีเรียก: พิมพ์ `/pstack:poteto-mode move <code> into one module, zero behavior change. record the current output first.`
- **/pstack:deslop** — ลบ comment เกินจำเป็น, defensive check และ cast `any` ที่ AI เพิ่มใน diff. วิธีเรียก: พิมพ์ `/pstack:deslop`
- **/pstack:no-comments** — ให้ reviewer ที่ไม่ได้เขียน comment ลบ comment และชี้ workaround. วิธีเรียก: พิมพ์ `/pstack:no-comments`
- **/pstack:principle-subtract-before-you-add** — ลบ dead code และ validator ซ้ำซ้อนก่อนสร้างโครงใหม่. วิธีเรียก: สั่งด้วยชื่อใน poteto-mode เช่น "apply subtract before you add" หรือพิมพ์ `/pstack:principle-subtract-before-you-add`
- **/pstack:correct** — ถ้าต้องแก้ agent เรื่องเดิมซ้ำๆ ให้แก้ที่ repo ด้วย type, lint หรือ test. วิธีเรียก: พิมพ์ `/pstack:correct`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode ย้ายโค้ด pricing จากสามไฟล์เข้า src/pricing/ โดย behavior ต้องไม่เปลี่ยนเลย บันทึก output ปัจจุบันก่อน แล้วพิสูจน์ว่าไม่เปลี่ยนหลังย้าย
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
