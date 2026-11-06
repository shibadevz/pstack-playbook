# /pstack:principle-attack-the-premise

<small>ประเภท: **Principle** · สถานการณ์: `เจอ bug` `ออกแบบ/วางแผน`</small>

## ใช้ทำอะไร

เมื่อ fix สองอันขึ้นไปที่อยู่บน premise เดียวกันไม่ผ่าน gate เดิม ให้สำรวจก่อนว่า actor ไหนถือความไม่สมดุลอยู่ แล้วตั้งคำถามกับ premise แทนการเขียน fix ที่สามบน premise เดิม

## ใช้เมื่อ

เช่นเมื่อแก้ race ด้วย lock สองรอบแล้ว test ยังพังที่เดิม และควรถามว่า lock คือคำตอบจริงหรือเปล่า

## ต่างจาก / ข้อควรรู้

ใช้เฉพาะตอน fix ซ้ำล้มเหลว ถ้าเพิ่งเริ่มแก้ให้ใช้ fix-root-causes

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply attack the premise" หรือโหลดตรงด้วย /pstack:principle-attack-the-premise`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode the flaky sync test still fails after two fixes that both assume the cache is the cause. apply attack the premise.
```
