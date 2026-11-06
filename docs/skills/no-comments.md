# /pstack:no-comments

<small>ประเภท: **Workflow skill** · สถานการณ์: `Review` `PR & Ship` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

spawn `pstack:comment-sicko` เพื่อลบ comment และชี้โค้ด workaround ใน diff แล้วแก้ finding ที่ยอมรับ และเสนอ encode constraint ที่ comment อ้างไว้เป็น type, test หรือ lint

## ใช้เมื่อ

เช่นเมื่อกำลังจะส่งรีวิวและ diff มี comment อธิบาย workaround เต็มไปหมด

## ต่างจาก / ข้อควรรู้

ใช้ reviewer ที่ไม่ได้เป็นคนเขียน comment ต่างจาก deslop ที่ล้าง slop ทั่วไป ถ้า root cause อยู่นอก scope จะแก้เท่าที่อยู่ใน scope และรายงานส่วนที่เหลือเป็น open

## วิธีเรียก

`/pstack:no-comments`

## ตัวอย่าง prompt

```text
/pstack:no-comments review the diff against main
```
