---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:show-me-your-work

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<PromptBlock text="/pstack:show-me-your-work ช่วยตามให้ทันว่าเมื่อคืนคุณทำอะไรไปบ้าง" />

<div class="spec-row">

## ใช้ทำอะไร

เก็บ decision trail เป็นไฟล์ TSV หนึ่งแถวต่อหนึ่งการตัดสินใจ (ts, phase, decision, why, evidence, result) และจบ reply ด้วยหัวข้อ Attention ที่ชี้ flag ตามแถวหรือจังหวะที่เกิด

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อสั่งงานยาวให้ทำข้ามคืนแล้วตอนเช้าอยากตรวจว่าตัดสินใจอะไรไปบ้าง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

เก็บเป็น local โดยค่าเริ่มต้น และ commit เมื่อผู้รีวิวต้องใช้ trail เพื่อเชื่อผล evidence ต้องเป็น pointer (SHA, PR, `file:line`, path) ไม่ใช่ย่อหน้า

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:show-me-your-work`

</div>
