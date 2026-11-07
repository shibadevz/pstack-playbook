---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:teach

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เข้าใจโค้ด&quot;, &quot;link&quot;: &quot;/situations/understand-code&quot;}]" />

<PromptBlock text="/pstack:teach ช่วยอธิบายว่าทำไมคุณ implement แบบนี้ ไม่ใช้ queue แลกอะไรไปบ้าง" />

<div class="spec-row">

## ใช้ทำอะไร

อธิบายงานก้อนหนึ่ง (subsystem หรือ change) ให้ผู้ใช้เข้าใจจริง โดยรัน how และ why แล้วถักเป็นคำอธิบายเดียวที่เริ่มจากนิยามง่ายๆ แล้วต่อด้วยวาดภาพทีละขั้น

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่ออยากเข้าใจว่าทำไม agent เลือก implement แบบนี้ และแลกอะไรไป

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

how อธิบายสิ่งที่โค้ดทำ, why อธิบายเหตุผล, teach รันหนึ่งหรือทั้งสองแล้วอธิบายผลอย่างเข้าใจง่าย เป้าหมายคือให้เข้าใจ ไม่ได้แก้โค้ด

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:teach`

</div>
