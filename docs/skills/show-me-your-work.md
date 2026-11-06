# /pstack:show-me-your-work

<small>ประเภท: **Workflow skill** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

เก็บ decision trail เป็นไฟล์ TSV หนึ่งแถวต่อหนึ่งการตัดสินใจ (ts, phase, decision, why, evidence, result) และจบ reply ด้วยหัวข้อ Attention ที่ชี้ flag ตามแถวหรือจังหวะที่เกิด

## ใช้เมื่อ

เช่นเมื่อสั่งงานยาวให้ทำข้ามคืนแล้วตอนเช้าอยากตรวจว่าตัดสินใจอะไรไปบ้าง

## ต่างจาก / ข้อควรรู้

เก็บเป็น local โดยค่าเริ่มต้น และ commit เมื่อผู้รีวิวต้องใช้ trail เพื่อเชื่อผล evidence ต้องเป็น pointer (SHA, PR, `file:line`, path) ไม่ใช่ย่อหน้า

## วิธีเรียก

`/pstack:show-me-your-work`

## ตัวอย่าง prompt

```text
/pstack:show-me-your-work catch me up on what you did last night.
```
