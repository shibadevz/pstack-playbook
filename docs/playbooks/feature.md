# Playbook: Feature

<small>ประเภท: **Playbook** · สถานการณ์: `สร้างฟีเจอร์`</small>

## ใช้ทำอะไร

สร้างหรือเปลี่ยน behavior จากรูปข้อมูลที่ตั้งชื่อ: ใช้ how กับ subsystem, architect, เขียน throughput checkpoint, delegate โค้ดให้ subagent, ตรวจบน surface ที่ตรงกัน และ rebase เป็น commit เล็กเรียงลำดับ

## ใช้เมื่อ

เช่นเมื่อต้องเพิ่ม flag `--json` ให้ command และผลแบบ text ต้องไม่เปลี่ยนแม้แต่ byte เดียว

## ต่างจาก / ข้อควรรู้

ถ้า implementation มีหลายรูปแบบที่ใช้ได้ จะ delegate ผ่าน arena ถ้า design ยังถูกโต้แย้งให้รัน interrogate ก่อน ship งานที่ใหญ่ข้ามหลายจุดหรือต้องไปตรวจทีหลัง ให้ใช้ figure-it-out

## วิธีเรียก

`/pstack:poteto-mode add <behavior>. <current output> stays byte-identical. verify both.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode add a --json flag to the export command. text output stays byte-identical. verify both.
```
