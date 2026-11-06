# /pstack:recall

<small>ประเภท: **Workflow skill** · สถานการณ์: `เข้าใจโค้ด` `เริ่มงาน/ตั้งค่า`</small>

## ใช้ทำอะไร

สร้าง context งานล่าสุดใหม่จากประวัติแชตของตัวเอง สถานะจริงใน git/gh และ "shared record" (user report, fix ที่ถูก revert, incident) แล้วคืน capsule สั้นๆ ว่าตอนนี้อยู่ตรงไหนและควรทำอะไรต่อ

## ใช้เมื่อ

เช่นเมื่อเปิดแชตใหม่เพื่อทำต่อจากงานสัปดาห์ก่อนและ agent ใหม่ไม่รู้อะไรเลย

## ต่างจาก / ข้อควรรู้

recall สร้าง context ข้ามหลายแชตล่าสุด (ค่าเริ่มต้นย้อนหลัง 7 วัน ใน workspace ปัจจุบัน) ส่วน ketchup ครอบคลุมเฉพาะแชตนี้ตั้งแต่ข้อความล่าสุด การกลับไปทำต่อแชตเดียวเฉพาะคือ playbook Session pickup

## วิธีเรียก

`/pstack:recall`

## ตัวอย่าง prompt

```text
/pstack:recall my work on the export pipeline from last week, then read the open issue about duplicate rows.
```
