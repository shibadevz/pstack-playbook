---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:poteto-help

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เริ่มงาน/ตั้งค่า&quot;, &quot;link&quot;: &quot;/situations/start-setup&quot;}]" />

<PromptBlock text="/pstack:poteto-help ทำยังไงให้ poteto-mode เปิดอยู่ทุก turn" />

<div class="spec-row">

## ใช้ทำอะไร

ตอบคำถามเรื่อง setup, `/pstack:poteto-mode` และการเลือก skill, playbook หรือ principle พร้อมให้ prompt ที่ส่งต่อได้และลิงก์ไปไฟล์ต้นทาง โดยไม่เริ่มงานจริง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อไม่แน่ใจว่าควรใช้ skill ไหนกับงานตรงหน้า

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

เป็นคำถามเรื่องวิธีใช้เท่านั้น ถ้าพิมพ์เป็นคำสั่งให้ทำงาน (เช่น "use pstack to fix this bug") จะทำงานภายใต้ poteto-mode แทน

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-help <คำถาม>`

</div>
