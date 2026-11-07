---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:make-bot-ui

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<PromptBlock text="/pstack:make-bot-ui สร้างหน้าที่มีปุ่ม Run report เพื่อปลุก bot ของฉันผ่าน webhook ถ้ายังไม่ได้ตั้งค่า bot runner ที่รองรับ webhook ให้ทำเป็น draft เท่านั้น" />

<div class="spec-row">

## ใช้ทำอะไร

สร้างหน้า UI (page, dashboard, ปุ่ม) ที่เมื่อกดแล้ว server ในเครื่อง POST JSON ไปปลุก Grok Bot ผ่าน webhook โดยเก็บ sender key ไว้ฝั่ง server เท่านั้น

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่ออยากทำหน้าที่มีปุ่ม "Run report" ซึ่งกดแล้วสั่งบอทให้ทำงาน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต้องมี bot runner ที่รองรับ webhook ที่ตั้งค่าไว้แล้ว ตัว skill อ้างอิง routine API ของ Cursor (`update_state` และอื่นๆ) ซึ่งใช้ได้เมื่อมีของเทียบเท่าที่ใช้งานได้จริงเท่านั้น ถ้าไม่มีให้หยุดที่ร่างและรายงานว่าขาดอะไร

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:make-bot-ui`

</div>
