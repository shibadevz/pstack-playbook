# Playbook: Hillclimb

<small>ประเภท: **Playbook** · สถานการณ์: `Performance` `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

ปรับปรุง metric เดียวอย่างต่อเนื่องและเป็นวิทยาศาสตร์จนถึงเป้า: วน loop สมมติฐานทีละอัน วัดก่อน-หลังด้วย harness ที่ freeze แล้ว บันทึก `decision.tsv` และ commit ต่อหนึ่ง win ที่ยอมรับ

## ใช้เมื่อ

เช่นเมื่อต้องการลดเวลา cold start จาก 3.2 วินาทีให้ต่ำกว่า 1.5 วินาที และไม่ใช่การแก้ครั้งเดียว

## ต่างจาก / ข้อควรรู้

ต่างจาก Perf issue ที่เป็นการแก้ครั้งเดียว Hillclimb คือ loop หนึ่งการเปลี่ยน หนึ่งการวัด เก็บหรือ revert และถ้าไม่มี case ที่ repro อาการได้ ให้แก้ repro ก่อน

## วิธีเรียก

`/pstack:poteto-mode keep improving <metric> until it reaches <target>.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode keep improving cold start time until it is under 1.5s on the benchmark fixture. keep a decision log, one commit per accepted win.
```
