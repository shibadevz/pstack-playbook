---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:control-ui

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}]" />

<PromptBlock text="/pstack:control-ui เปิดหน้า settings ในเครื่อง repro focus bug ที่เกิดหลังกด Tab และถ่าย screenshot ก่อนกับหลังแก้" />

<div class="spec-row">

## ใช้ทำอะไร

สร้างหรือปรับ harness แบบ browser/CDP ในเครื่องเพื่อขับและตรวจ UI ของ web, IDE หรือ Electron พร้อม screenshot, accessibility snapshot, profile และ visual diff

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ bug เกิดเฉพาะตอน focus หรือ keyboard จริงใน browser และต้องการ screenshot ก่อนและหลังแก้

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้ harness ที่ repo มีอยู่ก่อน (Playwright, Cypress, Electron script) poteto-mode ใช้ skill นี้เป็น control skill ของ surface แบบ browser/Electron/web ส่วน CLI/TUI ใช้ control-cli

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:control-ui`

</div>
