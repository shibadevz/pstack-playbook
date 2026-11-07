---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Opening a PR"
---

# Opening a PR

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยเปิด PR ให้หน่อย</code></p>

<PromptBlock text="/pstack:poteto-mode เปิด PR commit เล็กๆ เรียงลำดับ ใส่หลักฐานใน description" />

<div class="spec-row">

## ใช้ทำอะไร

ขั้นตอนเปิด PR ที่ใช้ปิดท้ายทุก playbook อื่น: ทำงานจาก worktree แยก, commit เล็กเรียงลำดับ, deslop และ no-comments ก่อนรีวิว, เขียน title แบบ Conventional Commits และ description 6 หัวข้อ (Why, What changed, Scope, Tradeoffs, Blast Radius, Verification)

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อแก้เสร็จแล้วและต้องเปิด PR ที่ผู้รีวิวอ่านจบในหนึ่งนาที

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

เปิด PR เป็น ready เสมอ ไม่ใช่ draft และการเปิด PR ไม่เริ่ม babysit ให้เอง ต้องขอ babysit แยกเมื่อ stack ครบ ใช้ `gh` เป็นค่าเริ่มต้น และใช้ `origin` ถ้ามี

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยเปิด PR ให้หน่อย`

</div>
