# Playbook: Investigation

<small>ประเภท: **Playbook** · สถานการณ์: `เข้าใจโค้ด`</small>

## ใช้ทำอะไร

คำถามแบบอ่านอย่างเดียว (X ทำงานอย่างไร, ทำไม Y ถูกสร้างแบบนี้, แน่ใจไหมว่า Z, ควรทำ X หรือ Y) ได้คำอธิบายพร้อมอ้างอิงหรือคำแนะนำพร้อมตาราง tradeoff โดยไม่แก้โค้ด

## ใช้เมื่อ

เช่นเมื่อถามว่า "retry ทำงานอย่างไรและทำไมถึงใช้ 30 วินาที" และยังไม่ต้องการแก้อะไร

## ต่างจาก / ข้อควรรู้

ไม่ต้องมี PR ถ้าสืบเพื่อเตรียมแก้โค้ด จะส่งกลับให้ผู้ใช้แล้ว route ไปที่ Bug fix หรือ Feature ใช้ how (และ why สำหรับเรื่องเหตุผล)

## วิธีเรียก

`/pstack:poteto-mode investigate why <symptom>. don't change any code yet.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode investigate why the export retries three times before failing. give me what we know, what data you used, and your best hypotheses. don't change any code yet.
```
