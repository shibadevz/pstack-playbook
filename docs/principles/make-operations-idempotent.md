---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-make-operations-idempotent"
---

# make-operations-idempotent

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-make-operations-idempotent</code></p>

<PromptBlock text="/pstack:poteto-mode ทำให้ nightly import รันซ้ำได้อย่างปลอดภัยหลัง crash apply make operations idempotent รันรอบสองต้องได้แถวเหมือนเดิม" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อออกแบบ command, lifecycle step หรือ loop ที่ทำงานท่ามกลาง crash, restart และ retry ให้บรรจบที่ end state เดียวกันไม่ว่าจะเคยรันค้างไว้แค่ไหน

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ job import รันครึ่งทางแล้ว process ตาย แล้ว retry ต้องไม่ทำให้แถวซ้ำ

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply make operations idempotent" หรือโหลดตรงด้วย `/pstack:principle-make-operations-idempotent`

</div>
