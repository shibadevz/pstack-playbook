# Playbook: Visual parity

<small>ประเภท: **Playbook** · สถานการณ์: `Verify/เทส` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

ทำให้ UI เหมือนกันแบบ pixel-exact ระหว่างสอง implementation หรือเมื่อย้ายระบบ styling: สร้าง baseline ด้วย visual regression harness ก่อน แล้วย้ายทีละ component และตรวจด้วย image diff จนเป็นศูนย์

## ใช้เมื่อ

เช่นเมื่อกำลังย้าย styling ของปุ่มและ card ไประบบใหม่และผลต้องตรงเดิมทุกพิกเซล

## ต่างจาก / ข้อควรรู้

baseline คือ spec ห้ามแก้ harness, ห้ามแตะ baseline และห้ามปรับโครงสร้าง component เพื่อให้ diff ผ่าน diff ที่ไม่ใช่ศูนย์คือ fail ถ้าไม่มี baseline จะไม่รับรอง parity

## วิธีเรียก

`/pstack:poteto-mode migrate <components> with pixel-exact parity.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode migrate the Button and Card components to the new styling system with pixel-exact parity. capture the baseline screenshots first and verify with image diff.
```
