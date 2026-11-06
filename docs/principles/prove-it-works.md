# /pstack:principle-prove-it-works

<small>ประเภท: **Principle** · สถานการณ์: `Verify/เทส` `PR & Ship`</small>

## ใช้ทำอะไร

หลังงานเสร็จและก่อนประกาศว่าเสร็จ ให้ตรวจกับของจริง (รัน feature, อ่านค่าที่เก็บจริง, ดู diff) ไม่ใช่ proxy, self-report หรือ "compile ผ่าน"

## ใช้เมื่อ

เช่นเมื่อ build เขียว แต่ยังไม่มีใครกดปุ่ม export จริง

## ต่างจาก / ข้อควรรู้

เป็น principle ที่ใช้บ่อยสุดสำหรับแก้ run ที่รายงานสำเร็จจาก build เขียว ส่วน explain-the-number ตรวจว่าตัวเลขวัดอะไรอยู่

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply prove it works" หรือโหลดตรงด้วย /pstack:principle-prove-it-works`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode fix the export button. apply prove it works. show me the real output, not the build log.
```
