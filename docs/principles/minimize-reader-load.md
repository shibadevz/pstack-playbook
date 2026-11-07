---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-minimize-reader-load"
---

# minimize-reader-load

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}, {&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-minimize-reader-load</code></p>

<PromptBlock text="/pstack:poteto-mode review src/billing/ หาโค้ดที่ trace ยาก apply minimize reader load และยุบ wrapper ที่มี caller เดียว" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อรีวิวหรือปรับโค้ดที่ตามยาก ให้นับ layer ระหว่างคำถามกับคำตอบและ hidden state ในหัวผู้อ่าน แล้วยุบ wrapper ที่มี caller เดียวและลด scope ของ mutable state

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องเปิด 5 ไฟล์เพื่อตามว่าค่า timeout มาจากไหน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใน playbook Refactoring ตัวชี้วัดความสำเร็จคือ reader load ลดลง ถ้าไม่ลดให้ revert

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply minimize reader load" หรือโหลดตรงด้วย `/pstack:principle-minimize-reader-load`

</div>
