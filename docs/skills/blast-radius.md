# /pstack:blast-radius

<small>ประเภท: **Workflow skill** · สถานการณ์: `Review` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

หาว่า change จะทำให้ที่อื่นพังตรงไหนนอก diff แล้วพิสูจน์ "fact เดียวที่ทำให้ change ปลอดภัย" ด้วยการรันโค้ดจริง ไม่ใช่แค่เขียนสรุป

## ใช้เมื่อ

เช่นเมื่อเห็น diff เล็กๆ ที่ลบการเรียก cache reset หนึ่งบรรทัดแล้วไม่แน่ใจว่าปลอดภัยจริง

## ต่างจาก / ข้อควรรู้

interrogate รีวิวตัว diff ส่วน blast-radius มองหาสิ่งที่พังนอก diff ถ้าพิสูจน์ fact ไม่ได้ ผลต้องระบุว่า unproven

## วิธีเรียก

`/pstack:blast-radius`

## ตัวอย่าง prompt

```text
/pstack:blast-radius of removing the cache reset in src/session.ts. prove the one fact it is safe because of by running real code, or mark it unproven.
```
