---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-migrate-callers-then-delete-legacy-apis"
---

# migrate-callers-then-delete-legacy-apis

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-migrate-callers-then-delete-legacy-apis</code></p>

<PromptBlock text="/pstack:poteto-mode ย้ายทุก caller ของ log.warning ไปใช้ logger.warn และลบ API เก่าใน change เดียวกัน apply migrate callers then delete legacy apis" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อเพิ่ม internal API ใหม่แต่ยังมี caller เก่า ให้ย้าย caller และลบ API เก่าใน wave เดียวกัน แทนการเก็บ compatibility layer

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมี `logger.warn()` ใหม่ แต่ code อีก 30 ที่ยังเรียก `log.warning()` เก่า

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก outcome-oriented-execution ที่เน้นการ rewrite ที่มี phase ชัดเจน

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply migrate callers then delete legacy apis" หรือโหลดตรงด้วย `/pstack:principle-migrate-callers-then-delete-legacy-apis`

</div>
