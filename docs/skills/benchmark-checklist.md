# /pstack:benchmark-checklist

<small>ประเภท: **Workflow skill** · สถานการณ์: `Performance` `Verify/เทส`</small>

## ใช้ทำอะไร

ตรวจตัวเลข performance ด้วยคำถาม 7 ข้อ (limiter, tuning, เกิน limit, error, ทำซ้ำได้, สำคัญจริงไหม, งานเกิดขึ้นจริงไหม) ก่อนรายงานหรือนำไปใช้ ผลคือ faster, slower, no measurable difference หรือ inconclusive

## ใช้เมื่อ

เช่นเมื่อกำลังจะเขียนใน PR ว่า "export เร็วขึ้น 40%" และยังไม่รู้ว่า cache อุ่นอยู่หรือเปล่า

## ต่างจาก / ข้อควรรู้

principle-explain-the-number เป็นกฎสั้น ส่วน skill นี้คือขั้นตอนเต็มสำหรับตัวเลข perf ถ้าแค่ขอ ballpark ครั้งเดียวก็พอ แต่ยังต้องเช็กข้อ 4 (error) และข้อ 7 (งานเกิดขึ้นจริง)

## วิธีเรียก

`/pstack:benchmark-checklist`

## ตัวอย่าง prompt

```text
/pstack:benchmark-checklist vet this 40% speedup before it goes in the pr description
```
