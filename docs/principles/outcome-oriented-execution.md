# /pstack:principle-outcome-oriented-execution

<small>ประเภท: **Principle** · สถานการณ์: `ออกแบบ/วางแผน` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

ใน rewrite หรือ migration ที่วางแผนไว้มี phase ชัด ให้มุ่งไปที่สถาปัตยกรรมเป้าหมาย ไม่ต้องรักษาสถานะระหว่างทางให้ราบรื่นด้วยโค้ดชั่วคราว

## ใช้เมื่อ

เช่นเมื่อกำลังย้าย storage layer ในสามขั้นและไม่ควรเขียน adapter ที่จะลบทิ้งในขั้นถัดไป

## ต่างจาก / ข้อควรรู้

ต่างจาก migrate-callers-then-delete-legacy-apis ที่เป็นกฎของ API ภายในหนึ่งตัวและ caller เก่า

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply outcome oriented execution" หรือโหลดตรงด้วย /pstack:principle-outcome-oriented-execution`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode phase 2 of the storage rewrite. apply outcome oriented execution. no throwaway compatibility code between phases.
```
