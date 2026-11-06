# /pstack:principle-laziness-protocol

<small>ประเภท: **Principle** · สถานการณ์: `Refactor/เก็บกวาด` `Review`</small>

## ใช้ทำอะไร

เมื่อ refactor, ประเมินขนาด diff หรืออยากเพิ่ม abstraction, layer: เอนไปทางการลบและการเปลี่ยนที่เล็กที่สุดที่แก้ปัญหาได้ ตัดสินใจเรื่องเดียวกันที่เดียว

## ใช้เมื่อ

เช่นเมื่อแค่เพิ่ม flag เดียวแต่ draft แรกสร้าง factory กับ config object ขึ้นมา

## ต่างจาก / ข้อควรรู้

การใช้ arena กับ implementation ที่มีหลายรูปแบบใน playbook Feature ยังต้องทำแม้ protocol นี้ เพราะผลคือการแยกผู้รีวิว ไม่ได้ลดจำนวนบรรทัด

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply laziness protocol" หรือโหลดตรงด้วย /pstack:principle-laziness-protocol`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode add a --json flag. apply laziness protocol. smallest diff that works.
```
