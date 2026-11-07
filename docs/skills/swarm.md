---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:swarm

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<PromptBlock text="/pstack:swarm ตรวจทุก package ใต้ packages/ ด้วย check script ของแต่ละตัว หนึ่ง worker ต่อหนึ่ง package แล้วรวมเป็น report เดียว" />

<div class="spec-row">

## ใช้ทำอะไร

กระจาย worker N ตัวที่แยกกัน (ตามชิ้นงาน, แข่ง brief เดียวกัน หรือผสม) รอให้ครบแล้วรวมเป็นรายงานเดียวที่ใช้ `PASS`, `ISSUES` หรือ `BLOCKED` พร้อมหลักฐาน

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องเช็กทุก package ใต้ `packages/` กับ script ตรวจของแต่ละอัน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

swarm แบ่งงานเป็น slice หรือแข่งแล้วรายงานเดียว ส่วน arena ให้ทุก worker ทำ brief เดียวกันแล้วรวมส่วนดี worker ที่เขียนไฟล์ต้องมี worktree หรือ output directory ของตัวเอง

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:swarm`

</div>
