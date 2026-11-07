---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:how

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เข้าใจโค้ด&quot;, &quot;link&quot;: &quot;/situations/understand-code&quot;}]" />

<PromptBlock text="/pstack:how อธิบายว่า job scheduler ใน src/scheduler/ ทำงานอย่างไร ตั้งแต่ flow หลัก ไฟล์ที่เกี่ยวข้อง ไปจนถึง gotcha ที่ควรระวัง ก่อนที่ฉันจะแก้ แล้วใช้ /pstack:why หาว่าทำไมมันพังเมื่อไม่นานมานี้" />

<div class="spec-row">

## ใช้ทำอะไร

อธิบายว่าโค้ดทำงานอย่างไรในระดับ senior engineer ที่ onboard subsystem (Overview, Key Concepts, How It Works, Where Things Live, Gotchas) และตอบคำถามว่าโค้ดใหม่ควรอยู่ที่ไหนหรือ package ไหนเป็นเจ้าของ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องแก้ระบบ scheduler ที่ไม่เคยแตะและอยากรู้ flow ก่อนลงมือ

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

how ตอบว่าตอนนี้ทำงานอย่างไร, why ตอบว่าทำไมเป็นแบบนี้, teach เรียกทั้งสองแล้วอธิบายให้เข้าใจ งานเล็ก (module เดียว) ใช้ explainer ตัวเดียว งานใหญ่แตกเป็น explorer หลายมุม

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:how`

</div>
