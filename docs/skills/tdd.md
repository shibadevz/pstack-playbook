# /pstack:tdd

<small>ประเภท: **Workflow skill** · สถานการณ์: `เจอ bug` `Verify/เทส`</small>

## ใช้ทำอะไร

แก้ bug แบบ test-first: เขียน regression test ที่ fail ด้วยเหตุผลที่ถูกต้องก่อน แล้วแก้ production code ให้ผ่าน และถ้า test ไม่คุ้มก็ใช้ check ที่ใกล้เคียงที่สุดแทน

## ใช้เมื่อ

เช่นเมื่อ bug มี test target ในเครื่องที่ถูกและชัด เช่น function เดียวที่คืนค่าผิดเมื่อ input ซ้ำ

## ต่างจาก / ข้อควรรู้

ใช้เมื่อผู้ใช้ขอ TDD หรือ test ที่ fail เอง หรือเมื่อ test path ถูกและชัดเท่านั้น ถ้าต้องตั้ง harness ใหญ่ ใช้ mock เปราะ หรือ repro ไม่ชัด ให้ข้ามการเพิ่ม test (no new test ดีกว่า test ที่แย่)

## วิธีเรียก

`/pstack:tdd`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode repro the duplicate write first. if there's a cheap test path, /pstack:tdd it. then fix and rerun.
```
