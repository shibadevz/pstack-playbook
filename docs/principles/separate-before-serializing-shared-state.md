# /pstack:principle-separate-before-serializing-shared-state

<small>ประเภท: **Principle** · สถานการณ์: `ออกแบบ/วางแผน` `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

เมื่อ actor พร้อมกันอาจเขียนไฟล์, branch, key หรือ state object เดียวกัน ให้กำจัดการแชร์ก่อน และใช้ serialize ก็ต่อเมื่อ writer เดียวร่วมเป็น invariant จริง

## ใช้เมื่อ

เช่นเมื่อมี subagent สามตัวจะแก้ไฟล์ config เดียวกันพร้อมกัน และควรแยกไฟล์หรือ worktree ให้ก่อน

## ต่างจาก / ข้อควรรู้

ต่างจากการใช้ lock หลังเกิดปัญหา เพราะหลักการนี้ให้แยกตั้งแต่ต้น playbook Feature และ Visual parity อ้างหลักการนี้

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply separate before serializing shared state" หรือโหลดตรงด้วย /pstack:principle-separate-before-serializing-shared-state`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode migrate these 12 components in parallel. apply separate before serializing shared state. one worktree per owner.
```
