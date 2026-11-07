---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-boundary-discipline"
---

# boundary-discipline

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-boundary-discipline</code></p>

<PromptBlock text="/pstack:poteto-mode เพิ่ม import endpoint apply boundary discipline parse input ครั้งเดียวที่ขอบระบบ และให้ core บริสุทธิ์" />

<div class="spec-row">

## ใช้ทำอะไร

วาง validation และ error handling ที่ขอบระบบ (CLI, config, network, external API) แล้วเชื่อ internal type และให้ business logic เป็น pure function

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังเขียน handler ที่รับ JSON จากภายนอกและเริ่มใส่ null check ซ้ำในทุก function ภายใน

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply boundary discipline" หรือโหลดตรงด้วย `/pstack:principle-boundary-discipline`

</div>
