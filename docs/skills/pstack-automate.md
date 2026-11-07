---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:pstack-automate

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<PromptBlock text="/pstack:pstack-automate ตั้งค่า Benny automation pack ให้ repo นี้ โดยใช้ scheduler ที่ฉันอนุญาตไว้แล้ว" />

<div class="spec-row">

## ใช้ทำอะไร

ตั้งค่า automation source pack แบบ dormant (Benny) ไว้ใน `.pstack/automations/benny/` ผ่าน scheduler ที่ผู้ใช้อนุญาต แล้วรัน test report หนึ่งครั้งเพื่อพิสูจน์

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมี scheduler ที่ใช้งานได้และอยากให้ทีมมี automation triage รายงานเข้า thread เดิม

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต้องมี scheduler หรือ automation tool ที่เปิดใช้จริงและผู้ใช้อนุญาตให้ตั้งค่า port นี้ไม่มี daemon, bot token หรือ cloud account มาให้ ขั้นตอนนี้ใช้สร้างใหม่เท่านั้น (ถ้ามีอยู่แล้วให้ validate และทำ checklist) skill นี้ไม่อยู่ในตารางเลือก skill ของ poteto-help ควรอ่านไฟล์ SKILL.md ก่อนใช้

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:pstack-automate`

</div>
