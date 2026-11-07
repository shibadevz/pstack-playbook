---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-sequence-verifiable-units"
---

# sequence-verifiable-units

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-sequence-verifiable-units</code></p>

<PromptBlock text="/pstack:poteto-mode อัปเดต call site ทั้ง 40 จุดให้ใช้ signature ใหม่ apply sequence verifiable units หนึ่ง commit ที่ verify แล้วต่อหนึ่งกลุ่ม" />

<div class="spec-row">

## ใช้ทำอะไร

กับงานหลายขั้น (sweep, migration, edit ซ้ำๆ) และการ stack commit/PR ให้แตกเป็นหน่วยเล็กที่จบด้วยสถานะที่ตรวจได้ ตรวจแต่ละหน่วยก่อนไปหน่วยถัดไป และเรียงการส่งมอบให้ลำดับพิสูจน์ตัวเองให้ผู้รีวิวเห็น

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องแก้ 40 ไฟล์ และควรตรวจทีละกลุ่มแทนรวมตรวจตอนท้าย

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

playbook Bug fix ใช้หลักนี้โดยให้ failing repro อยู่ก่อน fix ใน git history

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply sequence verifiable units" หรือโหลดตรงด้วย `/pstack:principle-sequence-verifiable-units`

</div>
