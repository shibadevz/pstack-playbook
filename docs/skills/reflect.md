# /pstack:reflect

<small>ประเภท: **Workflow skill** · สถานการณ์: `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

spawn reviewer สามตัวพร้อมกัน (judgment, tooling, divergent) ไล่ดู transcript ของแชตปัจจุบัน แล้วส่งบทเรียนแต่ละข้อไปเป็นการแก้ skill ที่มีอยู่

## ใช้เมื่อ

เช่นเมื่อจบงานที่มี agent ทำผิดซ้ำแล้วอยากให้บทเรียนไม่หายไป

## ต่างจาก / ข้อควรรู้

ข้ามถ้าแชตไม่มีสาระหรือบทเรียนมีใน skill อยู่แล้ว (เรื่องที่เกิดครั้งเดียวไม่ใช่บทเรียน) อนุมัติเฉพาะการแก้ที่เปลี่ยนการตัดสินใจครั้งต่อไป ต่างจาก automate-me ที่สร้าง skill ส่วนตัวจากนิสัยโดยรวม

## วิธีเรียก

`/pstack:reflect`

## ตัวอย่าง prompt

```text
/pstack:reflect capture what we learned so the next run doesn't repeat it.
```
