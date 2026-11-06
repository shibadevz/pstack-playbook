# /pstack:principle-never-block-on-the-human

<small>ประเภท: **Principle** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

เมื่ออยากถามว่า "ทำ X ดีไหม" กับงานที่ย้อนกลับได้ ให้ทำไปแล้วอธิบายเหตุผล ให้มนุษย์แก้ทางทีหลัง ส่วนงานย้อนกลับไม่ได้ (force-push, ลบ data จริง, ส่งข้อความออกนอก) ยังต้องขออนุญาต

## ใช้เมื่อ

เช่นเมื่อกำลังจะถามว่า "ตั้งชื่อ branch แบบนี้ได้ไหม" ทั้งที่เปลี่ยนทีหลังได้

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply never block on the human" หรือโหลดตรงด้วย /pstack:principle-never-block-on-the-human`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode I'm stepping away. keep going on the migration. apply never block on the human. only stop for irreversible actions.
```
