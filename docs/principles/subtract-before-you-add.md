---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-subtract-before-you-add"
---

# subtract-before-you-add

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}, {&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-subtract-before-you-add</code></p>

<PromptBlock text="/pstack:poteto-mode เพิ่ม retry option ให้ client apply subtract before you add ลบ option ที่ไม่ได้ใช้ก่อน" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อจะเพิ่ม, refactor หรือ rewrite ให้ลบก่อน (dead code, validator ซ้ำซ้อน, stub ที่ไม่มีเนื้อหา) แล้วค่อยสร้างบนฐานที่ง่ายกว่า

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะเพิ่ม option ใหม่ให้ config แต่ใน module นั้นมี option เก่าที่ไม่มีใครใช้อยู่สามตัว

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

playbook Refactoring แยก commit ลบออกก่อน commit ปรับรูป

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply subtract before you add" หรือโหลดตรงด้วย `/pstack:principle-subtract-before-you-add`

</div>
