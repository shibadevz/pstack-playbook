# /pstack:principle-model-the-domain

<small>ประเภท: **Principle** · สถานการณ์: `สร้างฟีเจอร์` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เมื่อเขียน logic ที่มี state หรือโค้ดแตกแขนงมากและซ้ำการสมมติรูปข้อมูลหลายไฟล์ ให้ใส่ domain ลงโครงสร้าง (state machine, typed model, table/registry) แทนเงื่อนไขกระจัดกระจาย

## ใช้เมื่อ

เช่นเมื่อ order มีธง boolean 6 ตัวและไม่มีใครรู้ว่าการรวมกันแบบไหนถูก

## ต่างจาก / ข้อควรรู้

playbook Feature และ Refactoring อ้างหลักการนี้เมื่อเลือกโครงข้อมูล

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply model the domain" หรือโหลดตรงด้วย /pstack:principle-model-the-domain`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode order status is six booleans today. apply model the domain and replace them with an explicit state machine.
```
