# /pstack:principle-subtract-before-you-add

<small>ประเภท: **Principle** · สถานการณ์: `Refactor/เก็บกวาด` `สร้างฟีเจอร์`</small>

## ใช้ทำอะไร

เมื่อจะเพิ่ม, refactor หรือ rewrite ให้ลบก่อน (dead code, validator ซ้ำซ้อน, stub ที่ไม่มีเนื้อหา) แล้วค่อยสร้างบนฐานที่ง่ายกว่า

## ใช้เมื่อ

เช่นเมื่อกำลังจะเพิ่ม option ใหม่ให้ config แต่ใน module นั้นมี option เก่าที่ไม่มีใครใช้อยู่สามตัว

## ต่างจาก / ข้อควรรู้

playbook Refactoring แยก commit ลบออกก่อน commit ปรับรูป

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply subtract before you add" หรือโหลดตรงด้วย /pstack:principle-subtract-before-you-add`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode add the retry option to the client. apply subtract before you add. remove the dead options first.
```
