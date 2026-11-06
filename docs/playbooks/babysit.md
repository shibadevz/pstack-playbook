# Playbook: Babysit

<small>ประเภท: **Playbook** · สถานการณ์: `PR & Ship`</small>

## ใช้ทำอะไร

ขับ PR หรือ stack ไปจนถึง merge-ready: ประกาศโหมด (drive, background, threads-only, check), เคลียร์ทีละ PR จากล่างสุด โดยเรียงลำดับ conflict, review thread, CI และหยุดตรงที่เป็นการตัดสินใจของมนุษย์

## ใช้เมื่อ

เช่นเมื่อ stack สร้างเสร็จแล้วและ CI แดง หรือมี review comment ค้าง

## ต่างจาก / ข้อควรรู้

ไม่ merge เว้นแต่ผู้ใช้ขอ merge, land หรือ ship ซึ่งเป็น Shipping ถ้าไม่ใช้ผ่าน poteto-mode วลีอย่าง "babysit this pr" อาจไปเรียก skill อื่นที่ติดตั้งไว้แทน Opening a PR ไม่เริ่ม babysit ให้เอง

## วิธีเรียก

`/pstack:poteto-mode babysit this pr. get it green.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode babysit this pr. get it green.
```
