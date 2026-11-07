---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:blast-radius

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<PromptBlock text="/pstack:blast-radius ของการลบ cache reset ใน src/session.ts พิสูจน์ข้อเท็จจริงข้อเดียวที่ทำให้มันปลอดภัยด้วยการรันโค้ดจริง ถ้าพิสูจน์ไม่ได้ให้ mark ว่า unproven" />

<div class="spec-row">

## ใช้ทำอะไร

หาว่า change จะทำให้ที่อื่นพังตรงไหนนอก diff แล้วพิสูจน์ "fact เดียวที่ทำให้ change ปลอดภัย" ด้วยการรันโค้ดจริง ไม่ใช่แค่เขียนสรุป

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อเห็น diff เล็กๆ ที่ลบการเรียก cache reset หนึ่งบรรทัดแล้วไม่แน่ใจว่าปลอดภัยจริง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

interrogate รีวิวตัว diff ส่วน blast-radius มองหาสิ่งที่พังนอก diff ถ้าพิสูจน์ fact ไม่ได้ ผลต้องระบุว่า unproven

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:blast-radius`

</div>
