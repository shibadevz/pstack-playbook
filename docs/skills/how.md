# /pstack:how

<small>ประเภท: **Workflow skill** · สถานการณ์: `เข้าใจโค้ด`</small>

## ใช้ทำอะไร

อธิบายว่าโค้ดทำงานอย่างไรในระดับ senior engineer ที่ onboard subsystem (Overview, Key Concepts, How It Works, Where Things Live, Gotchas) และตอบคำถามว่าโค้ดใหม่ควรอยู่ที่ไหนหรือ package ไหนเป็นเจ้าของ

## ใช้เมื่อ

เช่นเมื่อต้องแก้ระบบ scheduler ที่ไม่เคยแตะและอยากรู้ flow ก่อนลงมือ

## ต่างจาก / ข้อควรรู้

how ตอบว่าตอนนี้ทำงานอย่างไร, why ตอบว่าทำไมเป็นแบบนี้, teach เรียกทั้งสองแล้วอธิบายให้เข้าใจ งานเล็ก (module เดียว) ใช้ explainer ตัวเดียว งานใหญ่แตกเป็น explorer หลายมุม

## วิธีเรียก

`/pstack:how`

## ตัวอย่าง prompt

```text
use /pstack:how to understand the job scheduler in src/scheduler/. then use /pstack:why to find out why it broke recently.
```
