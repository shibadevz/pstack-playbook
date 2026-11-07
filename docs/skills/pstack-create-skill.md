---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:pstack-create-skill

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}]" />

<PromptBlock text="/pstack:pstack-create-skill สร้าง project skill ที่รัน release checklist ของเรา และปิดท้ายด้วย check ที่ตัดสินได้ว่าผ่านหรือไม่ผ่าน" />

<div class="spec-row">

## ใช้ทำอะไร

เขียน project skill ที่ `.claude/skills/<name>/SKILL.md` พร้อม frontmatter (`name`, `description`), ลำดับขั้น, กรณี error และเงื่อนไขเสร็จที่ตรวจได้ แล้วลองเรียกใช้จริงกับงานเล็กหนึ่งครั้ง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมี workflow ที่ทำซ้ำบ่อย เช่น release checklist และอยากให้เป็น skill

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

เป็นตัวแทน skill authoring แบบ native ใน port นี้ playbook Authoring or modifying a skill เรียกใช้ตัวนี้ จึงควรเขียน SKILL.md ผ่าน playbook ไม่ใช่เขียนเอง

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:pstack-create-skill`

</div>
