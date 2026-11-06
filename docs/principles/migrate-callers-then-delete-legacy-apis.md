# /pstack:principle-migrate-callers-then-delete-legacy-apis

<small>ประเภท: **Principle** · สถานการณ์: `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เมื่อเพิ่ม internal API ใหม่แต่ยังมี caller เก่า ให้ย้าย caller และลบ API เก่าใน wave เดียวกัน แทนการเก็บ compatibility layer

## ใช้เมื่อ

เช่นเมื่อมี `logger.warn()` ใหม่ แต่ code อีก 30 ที่ยังเรียก `log.warning()` เก่า

## ต่างจาก / ข้อควรรู้

ต่างจาก outcome-oriented-execution ที่เน้นการ rewrite ที่มี phase ชัดเจน

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply migrate callers then delete legacy apis" หรือโหลดตรงด้วย /pstack:principle-migrate-callers-then-delete-legacy-apis`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode move every caller of log.warning to logger.warn and delete the old API in the same change. apply migrate callers then delete legacy apis.
```
