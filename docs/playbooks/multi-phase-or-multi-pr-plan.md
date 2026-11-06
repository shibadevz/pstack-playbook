# Playbook: Multi-phase or multi-PR plan

<small>ประเภท: **Playbook** · สถานการณ์: `ออกแบบ/วางแผน`</small>

## ใช้ทำอะไร

เขียนแผนสำหรับงานที่ข้ามหลาย phase หรือ PR ซ้อนกัน ให้เป็น checklist ที่ owner รันทีละช่องและผู้ใช้ตรวจจากหลักฐาน แผนคือ deliverable และไม่ implement

## ใช้เมื่อ

เช่นเมื่อ design นิ่งแล้วและต้องการแผน migration เป็น PR เล็กที่ตรวจได้ทีละอัน

## ต่างจาก / ข้อควรรู้

ถ้างานแค่หนึ่งสองไฟล์และวิธีชัดเจนจะข้ามแผน pstack ไม่มี planning skill ให้ใช้ plan mode ของ runtime ควบคู่ถ้ามี แผนรันสคริปต์ตรวจ `check-plan.mjs` และเริ่มทำเมื่อผู้ใช้สั่ง go เท่านั้น

## วิธีเรียก

`/pstack:poteto-mode turn this design into a plan.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode turn this design into a plan. small verifiable PRs, each with its own verification steps.
```
