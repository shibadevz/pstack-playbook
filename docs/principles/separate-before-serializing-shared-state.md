---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-separate-before-serializing-shared-state"
---

# separate-before-serializing-shared-state

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-separate-before-serializing-shared-state</code></p>

<PromptBlock text="/pstack:poteto-mode migrate component 12 ตัวนี้แบบขนาน apply separate before serializing shared state หนึ่ง worktree ต่อหนึ่งเจ้าของ" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อ actor พร้อมกันอาจเขียนไฟล์, branch, key หรือ state object เดียวกัน ให้กำจัดการแชร์ก่อน และใช้ serialize ก็ต่อเมื่อ writer เดียวร่วมเป็น invariant จริง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมี subagent สามตัวจะแก้ไฟล์ config เดียวกันพร้อมกัน และควรแยกไฟล์หรือ worktree ให้ก่อน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจากการใช้ lock หลังเกิดปัญหา เพราะหลักการนี้ให้แยกตั้งแต่ต้น playbook Feature และ Visual parity อ้างหลักการนี้

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply separate before serializing shared state" หรือโหลดตรงด้วย `/pstack:principle-separate-before-serializing-shared-state`

</div>
