---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:poteto-mode

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เริ่มงาน/ตั้งค่า&quot;, &quot;link&quot;: &quot;/situations/start-setup&quot;}, {&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}, {&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}, {&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<PromptBlock text="/pstack:poteto-mode แก้ export ซ้ำตอน retry ช่วย repro ก่อน แล้วค่อย fix และ verify บน user path จริง" />

<div class="spec-row">

## ใช้ทำอะไร

จับคู่งานกับ playbook, คัดลอกขั้นตอนของ playbook เข้า todo list แล้วเรียก skill อื่นตามที่ขั้นตอนต้องการ ขั้นที่ข้ามจะค้างใน list เป็น `skip: <reason>`

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมีงาน non-trivial ที่อยากให้ทำอย่างเข้มงวด เช่น "fix the duplicate export on retry"

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ถ้าขึ้นต้นข้อความด้วย `/pstack:poteto-mode` hook จะบันทึกโหมดและเปิดต่อทุก turn จนกว่าจะส่ง `/pstack:poteto-mode off` การพิมพ์ชื่อกลางประโยคหรือใน code block ไม่เปิดโหมด ใช้ subagent `pstack:poteto-agent` ตอนทำ step ของ playbook และจะแปลงเป็นงานใหม่เมื่อพิมพ์ "new task"

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode <goal และ done check>`

</div>
