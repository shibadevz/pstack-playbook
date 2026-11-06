# Playbook: Shipping

<small>ประเภท: **Playbook** · สถานการณ์: `PR & Ship`</small>

## ใช้ทำอะไร

ครึ่งหลังของ Babysit: ตรวจ PR ที่เขียวแต่ละอันแยกอิสระ แล้ว land เฉพาะช่วงที่ verified ต่อเนื่องจากล่างสุดขึ้นไป ทีละ PR ผ่าน `gh` (หรือ `origin` ถ้ามี) แล้วหยุดที่ ceiling

## ใช้เมื่อ

เช่นเมื่อ stack เขียวและผู้ใช้สั่งให้ land

## ต่างจาก / ข้อควรรู้

เขียวไม่เท่ากับปลอดภัย: ต้องมี verdict อิสระต่อ PR ก่อน และไม่แตะ stack ระหว่าง land ยกเว้นย้าย PR ถัดไปหลัง merge ถ้ามี verdict ไม่ครบ จะหยุดที่ PR ล่างสุดที่ยังไม่ผ่าน

## วิธีเรียก

`/pstack:poteto-mode land the stack.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode land the stack.
```
