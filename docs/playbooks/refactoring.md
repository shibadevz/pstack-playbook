# Playbook: Refactoring

<small>ประเภท: **Playbook** · สถานการณ์: `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เปลี่ยนโครงสร้างโดยไม่เปลี่ยน behavior (rename, extract, inline, dedupe, move): ตรึง behavior ด้วย characterization test ก่อน แล้วลบ ย้ายเป็นก้าวเล็ก และพิสูจน์ว่า behavior เดิมกับของจริง

## ใช้เมื่อ

เช่นเมื่อต้องย้ายโค้ดกระจายสามไฟล์มารวม module เดียวโดยผลลัพธ์ต้องเหมือนเดิมทุกอย่าง

## ต่างจาก / ข้อควรรู้

ต่างจาก Feature ที่เพิ่ม behavior และ Bug fix ที่แก้ behavior ถ้าเจอ bug จริงระหว่างทางให้แยกออกและ ship โครงสร้างก่อน งานโครงสร้างที่ใหญ่ข้ามหลายจุดให้ใช้ figure-it-out

## วิธีเรียก

`/pstack:poteto-mode move <code> into one module, zero behavior change. record the current output first.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode move the pricing code from three files into src/pricing/, zero behavior change. record the current output first and prove it's unchanged after.
```
