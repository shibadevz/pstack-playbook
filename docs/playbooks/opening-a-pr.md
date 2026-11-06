# Playbook: Opening a PR

<small>ประเภท: **Playbook** · สถานการณ์: `PR & Ship`</small>

## ใช้ทำอะไร

ขั้นตอนเปิด PR ที่ใช้ปิดท้ายทุก playbook อื่น: ทำงานจาก worktree แยก, commit เล็กเรียงลำดับ, deslop และ no-comments ก่อนรีวิว, เขียน title แบบ Conventional Commits และ description 6 หัวข้อ (Why, What changed, Scope, Tradeoffs, Blast Radius, Verification)

## ใช้เมื่อ

เช่นเมื่อแก้เสร็จแล้วและต้องเปิด PR ที่ผู้รีวิวอ่านจบในหนึ่งนาที

## ต่างจาก / ข้อควรรู้

เปิด PR เป็น ready เสมอ ไม่ใช่ draft และการเปิด PR ไม่เริ่ม babysit ให้เอง ต้องขอ babysit แยกเมื่อ stack ครบ ใช้ `gh` เป็นค่าเริ่มต้น และใช้ `origin` ถ้ามี

## วิธีเรียก

`/pstack:poteto-mode open the pr.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode open the pr. small ordered commits, evidence in the description.
```
