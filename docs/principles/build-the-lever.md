---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-build-the-lever"
---

# build-the-lever

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}, {&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-build-the-lever</code></p>

<PromptBlock text="/pstack:poteto-mode เปลี่ยนชื่อ getUser เป็น fetchUser ทั้ง repo apply build the lever ขอ codemod ที่ฉันรันซ้ำได้" />

<div class="spec-row">

## ใช้ทำอะไร

กับงาน non-trivial ทุกชนิด ให้สร้างเครื่องมือที่ทำหรือพิสูจน์งาน (codemod, script, generator หรือ skill ที่ subagent ทำตาม) แทนการทำมือ เครื่องมือคือ artifact ที่ผู้รีวิวรันซ้ำได้

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องเปลี่ยนชื่อ API ใน 200 ไฟล์ และควรเขียน codemod แทนแก้ทีละไฟล์

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply build the lever" หรือโหลดตรงด้วย `/pstack:principle-build-the-lever`

</div>
