---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-fix-root-causes"
---

# fix-root-causes

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-fix-root-causes</code></p>

<PromptBlock text="/pstack:poteto-mode หน้า profile crash เมื่อไม่มี avatar apply fix root causes อย่าแค่เติม null check" />

<div class="spec-row">

## ใช้ทำอะไร

เวลา debug ให้ไล่แต่ละอาการไปถึง root cause แล้วแก้ที่นั่น: repro ก่อน ถาม why จนถึงต้นทาง และต้านการใส่ nil-check ที่แค่ปิดเสียง crash

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ app crash ด้วย null pointer และมีคนเสนอให้ใส่ `if (x)` ครอบแล้วจบ

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ถ้า fix ซ้ำล้มเหลวบน premise เดียวกันให้ใช้ attack-the-premise

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply fix root causes" หรือโหลดตรงด้วย `/pstack:principle-fix-root-causes`

</div>
