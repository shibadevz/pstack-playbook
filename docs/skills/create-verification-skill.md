# /pstack:create-verification-skill

<small>ประเภท: **Workflow skill** · สถานการณ์: `Verify/เทส` `เริ่มงาน/ตั้งค่า`</small>

## ใช้ทำอะไร

สร้าง project-local skill ที่ `.claude/skills/verify-<app>/` ซึ่งสอน agent ขับ app จริงเหมือนผู้ใช้ (Launch, Doctor, Drive, Evidence, Cleanup) พร้อม feature map และพิสูจน์ว่าใช้ได้หนึ่งรอบก่อนส่งมอบ

## ใช้เมื่อ

เช่นเมื่อโปรเจกต์ไม่มีวิธี script ไว้พิสูจน์พฤติกรรมของ UI, CLI หรือ service

## ต่างจาก / ข้อควรรู้

`/pstack:setup-pstack` จะเสนอสร้างให้ตอนท้ายถ้าไม่พบ verify-* skill หรือ harness ใน project ถ้าสร้างแล้วต้องการดูแลให้ตรงกับ app ใช้ maintain-verification-skill

## วิธีเรียก

`/pstack:create-verification-skill`

## ตัวอย่าง prompt

```text
/pstack:create-verification-skill make a verify skill for this repo's web app, and prove it works once before handing it over.
```
