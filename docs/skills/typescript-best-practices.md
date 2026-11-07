---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:typescript-best-practices

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<PromptBlock text="/pstack:typescript-best-practices ปรับ type ใน src/api/response.ts ให้เข้มงวดขึ้น ใช้ discriminated union และ unknown แทน any โดยไม่เปลี่ยน behavior" />

<div class="spec-row">

## ใช้ทำอะไร

กฎ TypeScript สำหรับงาน `.ts`/`.tsx`: discriminated union, branded type, `unknown` แทน `any`, schema ก่อน type guard, ไม่ใช้ `as` cast และ exhaustive switch ซึ่งอ้างอิง principle type-system-discipline ก่อน

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังแก้ไฟล์ `.ts` ที่มี optional field เต็มไปหมดจนแสดง state ที่เป็นไปไม่ได้ได้

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

frontmatter ของ skill นี้กำหนด `paths` เป็น `**/*.ts` และ `**/*.tsx` และไม่ได้ปิดการเรียกอัตโนมัติ (ไม่มี `disable-model-invocation`) จึงต่างจาก skill ส่วนใหญ่ แต่พิมพ์เรียกเองได้

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:typescript-best-practices`

</div>
