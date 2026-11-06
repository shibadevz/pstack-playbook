# /pstack:architect

<small>ประเภท: **Workflow skill** · สถานการณ์: `ออกแบบ/วางแผน` `สร้างฟีเจอร์`</small>

## ใช้ทำอะไร

ร่าง type, signature และโครง module โดยให้ body เป็น `not implemented` ก่อน ให้หลาย candidate ออกแบบผ่าน arena แล้ว implement ตาม sketch ที่เลือก

## ใช้เมื่อ

เช่นเมื่อกำลังเพิ่ม module ใหม่ที่หลายส่วนต้องเรียกข้าม function boundary และกลัวว่าการเขียนโค้ดทันทีจะล็อกรูปแบบผิด

## ต่างจาก / ข้อควรรู้

ค่าเริ่มต้นคือ implement ต่อทันทีหลังเลือก design ถ้าอยากตรวจก่อนให้เติม "with checkpoint" ถ้า implementation ชนกับ sketch ซ้ำๆ skill นี้ให้ทิ้ง sketch แล้วออกแบบใหม่

## วิธีเรียก

`/pstack:architect`

## ตัวอย่าง prompt

```text
/pstack:architect with checkpoint. sketch the types and module boundaries for a retry queue in src/jobs/. show me the design before you implement.
```
