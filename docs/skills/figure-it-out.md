# /pstack:figure-it-out

<small>ประเภท: **Workflow skill** · สถานการณ์: `ออกแบบ/วางแผน` `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

ออกแบบ playbook เฉพาะงานเมื่อไม่มี playbook ไหนพอดี: Frame, ออกแบบ workflow, วน loop แบบสมมติฐาน-วัด-เก็บหรือ revert และจดการตัดสินใจไว้ให้คนตรวจทีหลัง

## ใช้เมื่อ

เช่นเมื่อต้อง migrate ทุก caller ของ API เก่าข้ามหลายจุด หรือเป็นงานที่คนจะมารีวิวหลังเดินไปไหนแล้ว

## ต่างจาก / ข้อควรรู้

figure-it-out ออกแบบ run หนึ่งครั้งที่เข้มงวด ส่วน playbook Orchestrate รันทั้ง program ที่กินหลายวันและหลาย PR และ playbook Autonomous run ขับ task เดียวไปจนถึงเงื่อนไขที่ตรวจได้

## วิธีเรียก

`/pstack:figure-it-out`

## ตัวอย่าง prompt

```text
/pstack:figure-it-out migrate every caller of the old logger API to the new one. done means the old API is deleted and the full test suite passes.
```
