---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-laziness-protocol"
---

# laziness-protocol

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}, {&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-laziness-protocol</code></p>

<PromptBlock text="/pstack:poteto-mode เพิ่ม flag --json apply laziness protocol เอา diff ที่เล็กที่สุดที่ใช้ได้" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อ refactor, ประเมินขนาด diff หรืออยากเพิ่ม abstraction, layer: เอนไปทางการลบและการเปลี่ยนที่เล็กที่สุดที่แก้ปัญหาได้ ตัดสินใจเรื่องเดียวกันที่เดียว

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อแค่เพิ่ม flag เดียวแต่ draft แรกสร้าง factory กับ config object ขึ้นมา

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

การใช้ arena กับ implementation ที่มีหลายรูปแบบใน playbook Feature ยังต้องทำแม้ protocol นี้ เพราะผลคือการแยกผู้รีวิว ไม่ได้ลดจำนวนบรรทัด

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply laziness protocol" หรือโหลดตรงด้วย `/pstack:principle-laziness-protocol`

</div>
