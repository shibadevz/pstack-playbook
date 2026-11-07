---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-type-system-discipline"
---

# type-system-discipline

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-type-system-discipline</code></p>

<PromptBlock text="/pstack:poteto-mode id ทั้งหมดใน src/ เป็น string ธรรมดา apply type system discipline และทำ brand ให้ userId กับ orderId" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อออกแบบ type หรือ signature ในภาษา static type ให้ทำให้ state ที่เป็นไปไม่ได้แสดงไม่ได้ brand primitive ที่มีความหมาย parse ข้อมูลภายนอกที่ขอบ ไม่โกหก compiler และ exhaust ทุก variant

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ `userId` และ `orderId` เป็น string ทั้งคู่ และเคยสลับกันจน bug หลุด

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใน TypeScript ให้ใช้คู่กับ typescript-best-practices

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply type system discipline" หรือโหลดตรงด้วย `/pstack:principle-type-system-discipline`

</div>
