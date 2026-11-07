---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-test-behavior-not-implementation"
---

# test-behavior-not-implementation

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-test-behavior-not-implementation</code></p>

<PromptBlock text="/pstack:poteto-mode review test ใน tests/export/ apply test behavior not implementation เขียนใหม่หรือลบ test ที่ยังผ่านแม้ทุก function จะ return undefined" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อเขียน แก้ หรือคง test ให้เรียกโค้ดแบบที่ผู้ใช้เรียกและ assert ผลที่ผู้ใช้เห็นจริง และเขียนใหม่หรือลบ test ที่ยังผ่านแม้ทุก function ที่ import คืน undefined

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อเจอ test ที่ mock ทุกอย่างจนไม่มีโค้ดจริงถูกรัน

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply test behavior not implementation" หรือโหลดตรงด้วย `/pstack:principle-test-behavior-not-implementation`

</div>
