# Playbook: Session pickup

<small>ประเภท: **Playbook** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน` `เริ่มงาน/ตั้งค่า`</small>

## ใช้ทำอะไร

รับช่วงงานของ agent ก่อนหน้าจาก transcript, URL ของ cloud agent หรือ branch ที่ push แล้ว: อ่าน trail, สร้างสถานะใหม่, เทียบ done กับ pending และเริ่มจาก resume point โดยไม่ทำงานที่เสร็จซ้ำ

## ใช้เมื่อ

เช่นเมื่อมี branch ที่ agent อีกแชตทำค้างไว้ และต้องรับต่อโดยไม่รื้อของเดิม

## ต่างจาก / ข้อควรรู้

ต่างจาก recall ที่สร้าง context ข้ามหลายแชต Session pickup กลับไปทำต่องานหนึ่งแชตหรือ branch ที่เจาะจง เป็นคู่กับ Pause safely และ trail ของงานก่อนหน้าถือเป็นข้อมูลที่เชื่อได้

## วิธีเรียก

`/pstack:poteto-mode take over this branch.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode take over this branch. read the decision log, find what's done, and continue. don't redo finished work.
```
