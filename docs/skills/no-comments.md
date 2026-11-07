---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:no-comments

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<PromptBlock text="/pstack:no-comments review diff เทียบกับ main" />

<div class="spec-row">

## ใช้ทำอะไร

spawn `pstack:comment-sicko` เพื่อลบ comment และชี้โค้ด workaround ใน diff แล้วแก้ finding ที่ยอมรับ และเสนอ encode constraint ที่ comment อ้างไว้เป็น type, test หรือ lint

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะส่งรีวิวและ diff มี comment อธิบาย workaround เต็มไปหมด

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้ reviewer ที่ไม่ได้เป็นคนเขียน comment ต่างจาก deslop ที่ล้าง slop ทั่วไป ถ้า root cause อยู่นอก scope จะแก้เท่าที่อยู่ใน scope และรายงานส่วนที่เหลือเป็น open

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:no-comments`

</div>
