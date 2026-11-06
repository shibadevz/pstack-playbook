# /pstack:poteto-mode

<small>ประเภท: **Workflow skill** · สถานการณ์: `เริ่มงาน/ตั้งค่า` `เจอ bug` `สร้างฟีเจอร์` `Refactor/เก็บกวาด` `Performance` `PR & Ship`</small>

## ใช้ทำอะไร

จับคู่งานกับ playbook, คัดลอกขั้นตอนของ playbook เข้า todo list แล้วเรียก skill อื่นตามที่ขั้นตอนต้องการ ขั้นที่ข้ามจะค้างใน list เป็น `skip: <reason>`

## ใช้เมื่อ

เช่นเมื่อมีงาน non-trivial ที่อยากให้ทำอย่างเข้มงวด เช่น "fix the duplicate export on retry"

## ต่างจาก / ข้อควรรู้

ถ้าขึ้นต้นข้อความด้วย `/pstack:poteto-mode` hook จะบันทึกโหมดและเปิดต่อทุก turn จนกว่าจะส่ง `/pstack:poteto-mode off` การพิมพ์ชื่อกลางประโยคหรือใน code block ไม่เปิดโหมด ใช้ subagent `pstack:poteto-agent` ตอนทำ step ของ playbook และจะแปลงเป็นงานใหม่เมื่อพิมพ์ "new task"

## วิธีเรียก

`/pstack:poteto-mode <goal และ done check>`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode fix the duplicate export on retry. repro first, then fix and verify the real user path.
```
