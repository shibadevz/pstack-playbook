# /pstack:principle-encode-lessons-in-structure

<small>ประเภท: **Principle** · สถานการณ์: `ปรับแต่ง PStack` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เมื่อเขียนคำสั่งเดิมซ้ำเป็นครั้งที่สอง หรือเห็นการแก้ที่เกิดซ้ำ ให้เข้ารหัสกฎเป็น lint, metadata flag, runtime check หรือ script แทนการเพิ่มข้อความ

## ใช้เมื่อ

เช่นเมื่อต้องบอก agent "อย่าลืม register flag ใน schema" เป็นครั้งที่สามแล้ว

## ต่างจาก / ข้อควรรู้

ถ้ากฎต้องใช้ดุลยพินิจและเข้ารหัสไม่ได้ ให้ทำคำสั่งเด่นขึ้นและเพิ่มตัวอย่างความผิดพลาด ส่วน /pstack:correct เป็น skill เต็มที่ใช้หลักนี้ทั่ว repo

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply encode lessons in structure" หรือโหลดตรงด้วย /pstack:principle-encode-lessons-in-structure`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode this is the third time an agent forgot to register a flag in the schema. apply encode lessons in structure.
```
