# Playbook: Autopilot-stack

<small>ประเภท: **Playbook** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน` `PR & Ship`</small>

## ใช้ทำอะไร

สร้างและตรวจคิวของการเปลี่ยนแปลงด้วย autonomy เต็ม แล้วส่งมอบเป็น stack เส้นตรงของ PR ที่ chain ด้วย base branch ให้ผู้ใช้รีวิวและ land เอง

## ใช้เมื่อ

เช่นเมื่ออยากให้ agent สร้าง stack ให้ครบแต่ยังไม่ merge อะไรเอง

## ต่างจาก / ข้อควรรู้

ต่างจาก Autopilot-full ตรงที่ owner รายงาน STACK-READY แทน merge-ready และไม่ retarget, rebase หรือ merge เอง มีแค่ root ที่แตะ topology และผู้ใช้เป็นคน land

## วิธีเรียก

`/pstack:poteto-mode stack them, don't ship.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode autopilot these changes but stack them, don't ship. i'll land the stack.
```
