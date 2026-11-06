# Playbook: Eval

<small>ประเภท: **Playbook** · สถานการณ์: `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

ทดสอบว่าการเปลี่ยน skill, โครงสร้าง หรือ prompt ส่งผลต่อพฤติกรรม agent อย่างไรก่อนนำไปใช้ โดยทดลองแบบ blind: หลาย candidate บน prompt เดียวกัน, judge แบบ blind และตรวจ chain จาก transcript

## ใช้เมื่อ

เช่นเมื่อแก้ skill แล้วอยากรู้ว่า agent ทำตามจริงหรือไม่ก่อนรวมเข้า main

## ต่างจาก / ข้อควรรู้

candidate ต้องไม่เห็นคำว่า eval, test, judge, rubric หรือ arena และ prompt ต้องเหมือนคำขอปกติของผู้ใช้ judge เห็นผลลัพธ์ตาม label ที่ปิดชื่อ model

## วิธีเรียก

`/pstack:poteto-mode run the eval playbook on <change>.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode run the eval playbook on my change to the babysit skill. compare it against the current version, blind.
```
