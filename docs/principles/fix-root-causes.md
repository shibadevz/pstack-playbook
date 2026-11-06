# /pstack:principle-fix-root-causes

<small>ประเภท: **Principle** · สถานการณ์: `เจอ bug`</small>

## ใช้ทำอะไร

เวลา debug ให้ไล่แต่ละอาการไปถึง root cause แล้วแก้ที่นั่น: repro ก่อน ถาม why จนถึงต้นทาง และต้านการใส่ nil-check ที่แค่ปิดเสียง crash

## ใช้เมื่อ

เช่นเมื่อ app crash ด้วย null pointer และมีคนเสนอให้ใส่ `if (x)` ครอบแล้วจบ

## ต่างจาก / ข้อควรรู้

ถ้า fix ซ้ำล้มเหลวบน premise เดียวกันให้ใช้ attack-the-premise

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply fix root causes" หรือโหลดตรงด้วย /pstack:principle-fix-root-causes`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode the profile page crashes when avatar is missing. apply fix root causes. do not just add a null check.
```
