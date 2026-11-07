---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-redesign-from-first-principles"
---

# redesign-from-first-principles

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-redesign-from-first-principles</code></p>

<PromptBlock text="/pstack:poteto-mode ตอนนี้เราต้องรองรับ multi-tenant ใน src/storage/ apply redesign from first principles อย่าแปะเพิ่มเข้าไป" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อใส่ requirement ใหม่ลงใน design เดิม ให้ออกแบบใหม่เหมือน requirement นั้นเป็นข้อสมมติฐานตั้งแต่วันแรก ส่งผลไปทุกจุดที่อ้างถึง (type, docs, ตัวอย่าง) และคิดทั้ง redesign แล้วส่งมอบทีละส่วน

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องรองรับ multi-tenant ใน module ที่เขียนไว้สำหรับผู้ใช้คนเดียว

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply redesign from first principles" หรือโหลดตรงด้วย `/pstack:principle-redesign-from-first-principles`

</div>
