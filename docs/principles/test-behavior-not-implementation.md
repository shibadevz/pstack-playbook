# /pstack:principle-test-behavior-not-implementation

<small>ประเภท: **Principle** · สถานการณ์: `Verify/เทส`</small>

## ใช้ทำอะไร

เมื่อเขียน แก้ หรือคง test ให้เรียกโค้ดแบบที่ผู้ใช้เรียกและ assert ผลที่ผู้ใช้เห็นจริง และเขียนใหม่หรือลบ test ที่ยังผ่านแม้ทุก function ที่ import คืน undefined

## ใช้เมื่อ

เช่นเมื่อเจอ test ที่ mock ทุกอย่างจนไม่มีโค้ดจริงถูกรัน

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply test behavior not implementation" หรือโหลดตรงด้วย /pstack:principle-test-behavior-not-implementation`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode review the tests in tests/export/. apply test behavior not implementation. rewrite or delete any test that would pass if every function returned undefined.
```
