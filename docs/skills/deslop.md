---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:deslop

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}, {&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}]" />

<PromptBlock text="/pstack:deslop ช่วยล้าง AI slop ใน branch นี้เทียบกับ main" />

<div class="spec-row">

## ใช้ทำอะไร

ลบ AI slop ที่เพิ่มใน branch เทียบกับ main เช่น comment เกินจำเป็น, defensive check ที่ผิดปกติ, การ cast เป็น `any` และ nesting ที่ลึกเกิน โดยรักษา behavior เดิม

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะ commit แล้วเห็นว่า diff มี try/catch และ comment ที่ไม่ตรงกับสไตล์ของไฟล์

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

bundled ใน port นี้ และ playbook Opening a PR ให้รันก่อน commit no-comments ใช้ reviewer แยกเพื่อตรวจ comment และ workaround ส่วน unslop ใช้กับข้อความ ไม่ใช่โค้ด

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:deslop`

</div>
