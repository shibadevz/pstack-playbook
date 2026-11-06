# /pstack:principle-make-operations-idempotent

<small>ประเภท: **Principle** · สถานการณ์: `สร้างฟีเจอร์` `ออกแบบ/วางแผน`</small>

## ใช้ทำอะไร

เมื่อออกแบบ command, lifecycle step หรือ loop ที่ทำงานท่ามกลาง crash, restart และ retry ให้บรรจบที่ end state เดียวกันไม่ว่าจะเคยรันค้างไว้แค่ไหน

## ใช้เมื่อ

เช่นเมื่อ job import รันครึ่งทางแล้ว process ตาย แล้ว retry ต้องไม่ทำให้แถวซ้ำ

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply make operations idempotent" หรือโหลดตรงด้วย /pstack:principle-make-operations-idempotent`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode make the nightly import safe to rerun after a crash. apply make operations idempotent. a second run must leave the same rows.
```
