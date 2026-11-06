# /pstack:principle-type-system-discipline

<small>ประเภท: **Principle** · สถานการณ์: `สร้างฟีเจอร์` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เมื่อออกแบบ type หรือ signature ในภาษา static type ให้ทำให้ state ที่เป็นไปไม่ได้แสดงไม่ได้ brand primitive ที่มีความหมาย parse ข้อมูลภายนอกที่ขอบ ไม่โกหก compiler และ exhaust ทุก variant

## ใช้เมื่อ

เช่นเมื่อ `userId` และ `orderId` เป็น string ทั้งคู่ และเคยสลับกันจน bug หลุด

## ต่างจาก / ข้อควรรู้

ใน TypeScript ให้ใช้คู่กับ typescript-best-practices

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply type system discipline" หรือโหลดตรงด้วย /pstack:principle-type-system-discipline`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode the ids in src/ are all plain strings. apply type system discipline and brand userId and orderId.
```
