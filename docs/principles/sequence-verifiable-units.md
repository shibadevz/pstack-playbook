# /pstack:principle-sequence-verifiable-units

<small>ประเภท: **Principle** · สถานการณ์: `สร้างฟีเจอร์` `PR & Ship`</small>

## ใช้ทำอะไร

กับงานหลายขั้น (sweep, migration, edit ซ้ำๆ) และการ stack commit/PR ให้แตกเป็นหน่วยเล็กที่จบด้วยสถานะที่ตรวจได้ ตรวจแต่ละหน่วยก่อนไปหน่วยถัดไป และเรียงการส่งมอบให้ลำดับพิสูจน์ตัวเองให้ผู้รีวิวเห็น

## ใช้เมื่อ

เช่นเมื่อต้องแก้ 40 ไฟล์ และควรตรวจทีละกลุ่มแทนรวมตรวจตอนท้าย

## ต่างจาก / ข้อควรรู้

playbook Bug fix ใช้หลักนี้โดยให้ failing repro อยู่ก่อน fix ใน git history

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply sequence verifiable units" หรือโหลดตรงด้วย /pstack:principle-sequence-verifiable-units`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode update all 40 call sites to the new signature. apply sequence verifiable units. one verified commit per group.
```
