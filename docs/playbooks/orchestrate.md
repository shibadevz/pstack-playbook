# Playbook: Orchestrate

<small>ประเภท: **Playbook** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน` `ออกแบบ/วางแผน`</small>

## ใช้ทำอะไร

ให้ coordinator แชตเดียวเป็นเจ้าของ program ใหญ่ (หลายวัน, PR ซ้อนกันมาก, subagent หลายสิบถึงร้อย): เขียน brief, ระบายคิว, รักษา frontier ให้เขียว และไม่เขียนโค้ดเอง

## ใช้เมื่อ

เช่นเมื่อมอบทั้ง migration ที่ต้อง land หลายสิบ PR ให้ coordinator ดูแลจนจบ

## ต่างจาก / ข้อควรรู้

ต่างจาก Autonomous run ที่ขับ task เดียวถึง predicate และต่างจาก figure-it-out ที่ออกแบบ run เดียว ถ้างานที่ agent ตัวเดียวทำจบในงบของ session ได้ จะไม่ route มาที่นี่ pstack ไม่มี skill `/orchestrate` ถ้าเมนู slash แสดงว่าเป็นของ plugin อื่น

## วิธีเรียก

`/pstack:poteto-mode run this whole project. own this migration until it lands.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode own this migration until it lands. run this whole project through stacked PRs. check in with me twice a day.
```
