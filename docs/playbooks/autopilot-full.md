# Playbook: Autopilot-full

<small>ประเภท: **Playbook** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน` `PR & Ship`</small>

## ใช้ทำอะไร

ผลักคิวของ PR อิสระจนถึง merged ด้วย autonomy เต็ม: หนึ่ง owner ต่อ PR ตั้งแต่ build ถึง merge และ root ใช้ swarm ที่ไม่เคยเขียนโค้ดตรวจก่อน owner merge

## ใช้เมื่อ

เช่นเมื่อมีรายการ PR สิบอัน แต่ละอันเป็นอิสระ และผู้ใช้ให้สิทธิ์ land เอง

## ต่างจาก / ข้อควรรู้

ใช้เมื่อ PR อิสระต่อกันและให้สิทธิ์ land แล้ว ถ้าต้องการรีวิวก่อน land หรืองานต่อเนื่องกัน ใช้ Autopilot-stack รายการที่ผู้ใช้ระบุว่าเป็นของตัวเองจะหยุดที่ merge-ready

## วิธีเรียก

`/pstack:poteto-mode full autopilot on this queue. each item is independent.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode full autopilot on this queue. each item is independent.
```
