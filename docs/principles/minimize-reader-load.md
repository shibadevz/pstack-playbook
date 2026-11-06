# /pstack:principle-minimize-reader-load

<small>ประเภท: **Principle** · สถานการณ์: `Refactor/เก็บกวาด` `Review`</small>

## ใช้ทำอะไร

เมื่อรีวิวหรือปรับโค้ดที่ตามยาก ให้นับ layer ระหว่างคำถามกับคำตอบและ hidden state ในหัวผู้อ่าน แล้วยุบ wrapper ที่มี caller เดียวและลด scope ของ mutable state

## ใช้เมื่อ

เช่นเมื่อต้องเปิด 5 ไฟล์เพื่อตามว่าค่า timeout มาจากไหน

## ต่างจาก / ข้อควรรู้

ใน playbook Refactoring ตัวชี้วัดความสำเร็จคือ reader load ลดลง ถ้าไม่ลดให้ revert

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply minimize reader load" หรือโหลดตรงด้วย /pstack:principle-minimize-reader-load`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode review src/billing/ for hard-to-trace code. apply minimize reader load and collapse one-caller wrappers.
```
