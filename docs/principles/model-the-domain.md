---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-model-the-domain"
---

# model-the-domain

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-model-the-domain</code></p>

<PromptBlock text="/pstack:poteto-mode ตอนนี้สถานะ order เป็น boolean หกตัว apply model the domain แล้วแทนที่ด้วย state machine ที่ชัดเจน" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อเขียน logic ที่มี state หรือโค้ดแตกแขนงมากและซ้ำการสมมติรูปข้อมูลหลายไฟล์ ให้ใส่ domain ลงโครงสร้าง (state machine, typed model, table/registry) แทนเงื่อนไขกระจัดกระจาย

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ order มีธง boolean 6 ตัวและไม่มีใครรู้ว่าการรวมกันแบบไหนถูก

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

playbook Feature และ Refactoring อ้างหลักการนี้เมื่อเลือกโครงข้อมูล

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply model the domain" หรือโหลดตรงด้วย `/pstack:principle-model-the-domain`

</div>
