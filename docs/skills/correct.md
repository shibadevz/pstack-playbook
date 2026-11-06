# /pstack:correct

<small>ประเภท: **Workflow skill** · สถานการณ์: `ปรับแต่ง PStack` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

หาความผิดพลาดที่ agent ทำซ้ำใน repo แล้วทำให้เป็นไปไม่ได้ โดยลองระดับสูงสุดที่ใช้ได้ก่อน: architecture, type, lint ที่ error บอกวิธีแก้, test และเขียน docs เป็นอย่างสุดท้าย พร้อมพิสูจน์ว่า check ใหม่ fail กับความผิดพลาดจริงในอดีต

## ใช้เมื่อ

เช่นเมื่อต้องแก้ agent เรื่องเดิมซ้ำๆ เช่นเพิ่ม config flag แล้วไม่ลงทะเบียนใน schema

## ต่างจาก / ข้อควรรู้

การแก้ในแชตช่วยได้แค่ run เดียว ส่วน /pstack:correct แก้ที่ repo เพื่อให้ run ถัดไปทำผิดไม่ได้ class ของความผิดพลาดต้องเกิดอย่างน้อยสองครั้งจึงนับ

## วิธีเรียก

`/pstack:correct`

## ตัวอย่าง prompt

```text
/pstack:correct agents keep adding new config flags without registering them in the schema
```
