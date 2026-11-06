# /pstack:interrogate

<small>ประเภท: **Workflow skill** · สถานการณ์: `Review`</small>

## ใช้ทำอะไร

ให้ reviewer หลายตัว (หนึ่งตัวต่อ model ที่ตั้งค่าไว้) รีวิวการเปลี่ยนแปลงแบบ adversarial จากมุมอิสระ แล้วสรุป verdict ที่แยกเป็นหมวด act-on และ dismissed โดยไม่แก้โค้ดเอง

## ใช้เมื่อ

เช่นเมื่อ branch ใกล้เสร็จและอยากให้ต่างคนต่างโมเดลลองพังก่อนเปิด PR

## ต่างจาก / ข้อควรรู้

interrogate รีวิวตัว diff ส่วน blast-radius หาสิ่งที่พังนอก diff panel มาจาก role `interrogate reviewers` ใน models.json ถ้าไม่ได้ตั้งค่า seat จะ inherit model ของแชต ซึ่งไม่ใช่ความหลากหลายของ model-family

## วิธีเรียก

`/pstack:interrogate`

## ตัวอย่าง prompt

```text
/pstack:interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's a real bug or regression.
```
