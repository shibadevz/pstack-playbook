# Playbook: Bug fix

<small>ประเภท: **Playbook** · สถานการณ์: `เจอ bug`</small>

## ใช้ทำอะไร

แก้ defect ที่รายงานมา: repro เองบน surface ที่ตรงกัน, ไล่หา cause แบบ binary search ด้วยหลักฐานตอนรัน, วางแผนและ delegate fix, ตรวจบน surface เดิมและ stage commit ให้ failing repro อยู่ก่อน fix

## ใช้เมื่อ

เช่นเมื่อมีรายงานว่า export สร้างแถวซ้ำตอน retry

## ต่างจาก / ข้อควรรู้

ทุกบรรทัดที่ ship ต้องสืบกลับไปถึงหลักฐานตอนรัน การแก้แบบ "อาจช่วย" ไม่ถูก ship ถ้ามี test path ที่ถูกให้ใช้ tdd ถ้ายังไม่รู้สาเหตุและต้องการแค่วินิจฉัย ใช้ Runtime forensics

## วิธีเรียก

`/pstack:poteto-mode <symptom>. repro first, then fix and verify.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode the export creates duplicate rows when a retry happens. repro first, then fix and verify.
```
