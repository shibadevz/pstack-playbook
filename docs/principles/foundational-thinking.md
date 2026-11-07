---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-foundational-thinking"
---

# foundational-thinking

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-foundational-thinking</code></p>

<PromptBlock text="/pstack:poteto-mode เพิ่ม job queue apply foundational thinking ให้ตกลง job state และ data shape ให้เสร็จก่อนเขียน logic ใดๆ" />

<div class="spec-row">

## ใช้ทำอะไร

ก่อนเขียน logic ให้เลือกชนิดข้อมูลและโครงข้อมูลหลัก ลำดับงานระหว่าง scaffold กับ feature และถามว่า actor พร้อมกันใช้อะไรร่วมกัน เพื่อให้โค้ดที่ตามมาชัดเจนเอง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะเขียนระบบ job queue และยังไม่ได้กำหนดว่า job หนึ่งมี state อะไรบ้าง

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply foundational thinking" หรือโหลดตรงด้วย `/pstack:principle-foundational-thinking`

</div>
