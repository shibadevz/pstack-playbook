# /pstack:pstack-automate

<small>ประเภท: **Workflow skill** · สถานการณ์: `ปรับแต่ง PStack` `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

ตั้งค่า automation source pack แบบ dormant (Benny) ไว้ใน `.pstack/automations/benny/` ผ่าน scheduler ที่ผู้ใช้อนุญาต แล้วรัน test report หนึ่งครั้งเพื่อพิสูจน์

## ใช้เมื่อ

เช่นเมื่อมี scheduler ที่ใช้งานได้และอยากให้ทีมมี automation triage รายงานเข้า thread เดิม

## ต่างจาก / ข้อควรรู้

ต้องมี scheduler หรือ automation tool ที่เปิดใช้จริงและผู้ใช้อนุญาตให้ตั้งค่า port นี้ไม่มี daemon, bot token หรือ cloud account มาให้ ขั้นตอนนี้ใช้สร้างใหม่เท่านั้น (ถ้ามีอยู่แล้วให้ validate และทำ checklist) skill นี้ไม่อยู่ในตารางเลือก skill ของ poteto-help ควรอ่านไฟล์ SKILL.md ก่อนใช้

## วิธีเรียก

`/pstack:pstack-automate`

## ตัวอย่าง prompt

```text
/pstack:pstack-automate set up the Benny automation pack for this repo using the scheduler I have authorized.
```
