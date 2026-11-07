---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Authoring or modifying a skill"
---

# Authoring or modifying a skill

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยเขียน skill สำหรับ &lt;workflow&gt;</code></p>

<PromptBlock text="/pstack:poteto-mode เขียน skill สำหรับ release checklist ของเรา validate frontmatter และ link แล้วเปิด PR" />

<div class="spec-row">

## ใช้ทำอะไร

เขียนหรือแก้ SKILL.md ผ่าน pstack-create-skill, validate frontmatter และ link อ้างอิง, ทำ test ถ้าเป็นโครงสร้าง และเปิด PR

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่ออยากเพิ่ม skill สำหรับ release checklist หรือแก้ skill ที่ agent ตีความผิด

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

อย่าเขียน SKILL.md เองโดยไม่ผ่าน playbook และแก้ skill ที่มีปัญหาใน PR ของมันเอง ไม่ใช่ปนไปกับงาน feature ที่เจอปัญหา

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยเขียน skill สำหรับ <workflow>`

</div>
