# /pstack:arena

<small>ประเภท: **Workflow skill** · สถานการณ์: `ออกแบบ/วางแผน` `สร้างฟีเจอร์`</small>

## ใช้ทำอะไร

ให้ candidate N ตัวทำ brief เดียวกัน ให้ judge ข้าม model ตัดสิน เลือก base แล้วเก็บส่วนที่ดีที่สุดของตัวอื่นมาต่อเข้าไป

## ใช้เมื่อ

เช่นเมื่อ artifact ที่ไม่ง่ายถ้าลองแค่ครั้งเดียวอาจล็อกรูปผิด หรืออยากได้ความเห็นที่สองเรื่อง design

## ต่างจาก / ข้อควรรู้

arena ให้ทุก worker ทำ brief เดียวกันแล้วรวมส่วนดี ส่วน swarm แบ่งงานเป็น slice หรือแข่งกันแล้วรายงานเดียว อย่าใช้ arena เพื่อ coverage ถ้า model-family diversity ยังยืนยันไม่ได้ ตาม runtime contract ของ port จะรายงานข้อจำกัดนี้

## วิธีเรียก

`/pstack:arena`

## ตัวอย่าง prompt

```text
ask /pstack:arena for a second opinion on this thread and our approach.
```
