---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:create-verification-skill

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;เริ่มงาน/ตั้งค่า&quot;, &quot;link&quot;: &quot;/situations/start-setup&quot;}]" />

<PromptBlock text="/pstack:create-verification-skill ช่วยสร้าง verify skill สำหรับ web app ของ repo นี้ และพิสูจน์ว่าใช้งานได้จริงหนึ่งรอบก่อนส่งมอบ" />

<div class="spec-row">

## ใช้ทำอะไร

สร้าง project-local skill ที่ `.claude/skills/verify-<app>/` ซึ่งสอน agent ขับ app จริงเหมือนผู้ใช้ (Launch, Doctor, Drive, Evidence, Cleanup) พร้อม feature map และพิสูจน์ว่าใช้ได้หนึ่งรอบก่อนส่งมอบ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อโปรเจกต์ไม่มีวิธี script ไว้พิสูจน์พฤติกรรมของ UI, CLI หรือ service

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

`/pstack:setup-pstack` จะเสนอสร้างให้ตอนท้ายถ้าไม่พบ verify-* skill หรือ harness ใน project ถ้าสร้างแล้วต้องการดูแลให้ตรงกับ app ใช้ maintain-verification-skill

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:create-verification-skill`

</div>
