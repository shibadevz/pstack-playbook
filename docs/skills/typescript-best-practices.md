# /pstack:typescript-best-practices

<small>ประเภท: **Workflow skill** · สถานการณ์: `สร้างฟีเจอร์` `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

กฎ TypeScript สำหรับงาน `.ts`/`.tsx`: discriminated union, branded type, `unknown` แทน `any`, schema ก่อน type guard, ไม่ใช้ `as` cast และ exhaustive switch ซึ่งอ้างอิง principle type-system-discipline ก่อน

## ใช้เมื่อ

เช่นเมื่อกำลังแก้ไฟล์ `.ts` ที่มี optional field เต็มไปหมดจนแสดง state ที่เป็นไปไม่ได้ได้

## ต่างจาก / ข้อควรรู้

frontmatter ของ skill นี้กำหนด `paths` เป็น `**/*.ts` และ `**/*.tsx` และไม่ได้ปิดการเรียกอัตโนมัติ (ไม่มี `disable-model-invocation`) จึงต่างจาก skill ส่วนใหญ่ แต่พิมพ์เรียกเองได้

## วิธีเรียก

`/pstack:typescript-best-practices`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode tighten the types in src/api/response.ts. use /pstack:typescript-best-practices. no behavior change.
```
