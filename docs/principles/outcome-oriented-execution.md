---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-outcome-oriented-execution"
---

# outcome-oriented-execution

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-outcome-oriented-execution</code></p>

<PromptBlock text="/pstack:poteto-mode phase 2 ของ storage rewrite apply outcome oriented execution ไม่เอา compatibility code ชั่วคราวระหว่าง phase" />

<div class="spec-row">

## ใช้ทำอะไร

ใน rewrite หรือ migration ที่วางแผนไว้มี phase ชัด ให้มุ่งไปที่สถาปัตยกรรมเป้าหมาย ไม่ต้องรักษาสถานะระหว่างทางให้ราบรื่นด้วยโค้ดชั่วคราว

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังย้าย storage layer ในสามขั้นและไม่ควรเขียน adapter ที่จะลบทิ้งในขั้นถัดไป

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก migrate-callers-then-delete-legacy-apis ที่เป็นกฎของ API ภายในหนึ่งตัวและ caller เก่า

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply outcome oriented execution" หรือโหลดตรงด้วย `/pstack:principle-outcome-oriented-execution`

</div>
