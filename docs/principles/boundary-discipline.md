# /pstack:principle-boundary-discipline

<small>ประเภท: **Principle** · สถานการณ์: `สร้างฟีเจอร์` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

วาง validation และ error handling ที่ขอบระบบ (CLI, config, network, external API) แล้วเชื่อ internal type และให้ business logic เป็น pure function

## ใช้เมื่อ

เช่นเมื่อกำลังเขียน handler ที่รับ JSON จากภายนอกและเริ่มใส่ null check ซ้ำในทุก function ภายใน

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply boundary discipline" หรือโหลดตรงด้วย /pstack:principle-boundary-discipline`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode add the import endpoint. apply boundary discipline. parse input once at the edge and keep the core pure.
```
