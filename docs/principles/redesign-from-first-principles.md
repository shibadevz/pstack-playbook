# /pstack:principle-redesign-from-first-principles

<small>ประเภท: **Principle** · สถานการณ์: `ออกแบบ/วางแผน` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เมื่อใส่ requirement ใหม่ลงใน design เดิม ให้ออกแบบใหม่เหมือน requirement นั้นเป็นข้อสมมติฐานตั้งแต่วันแรก ส่งผลไปทุกจุดที่อ้างถึง (type, docs, ตัวอย่าง) และคิดทั้ง redesign แล้วส่งมอบทีละส่วน

## ใช้เมื่อ

เช่นเมื่อต้องรองรับ multi-tenant ใน module ที่เขียนไว้สำหรับผู้ใช้คนเดียว

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply redesign from first principles" หรือโหลดตรงด้วย /pstack:principle-redesign-from-first-principles`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode we now need multi-tenant support in src/storage/. apply redesign from first principles. don't bolt it on.
```
