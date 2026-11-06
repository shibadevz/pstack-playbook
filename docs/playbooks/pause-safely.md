# Playbook: Pause safely

<small>ประเภท: **Playbook** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

หยุดงานที่ค้างอยู่อย่างสะอาดเพื่อให้กลับมาต่อได้: หยุดที่ขอบที่ปลอดภัย, commit เป็น `wip:` เดียว และเขียน resume note ที่ agent ที่เริ่มใหม่อ่านต่อได้

## ใช้เมื่อ

เช่นเมื่อกำลังจะ offline หรือ context ใกล้ถูก compact และอยากให้งานต่อได้

## ต่างจาก / ข้อควรรู้

ใช้เมื่อสั่งหยุดชัดเจนเท่านั้น ถ้าพูดว่า "keep going" หรือ "going to bed, keep going" จะไม่หยุด ไม่ push หรือเปิด PR ใหม่เพื่อหยุด เป็นคู่กับ Session pickup

## วิธีเรียก

`/pstack:poteto-mode pause safely.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode pause safely. commit what you have as a wip commit and write a resume note.
```
