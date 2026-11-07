---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:recall

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เข้าใจโค้ด&quot;, &quot;link&quot;: &quot;/situations/understand-code&quot;}, {&quot;title&quot;: &quot;เริ่มงาน/ตั้งค่า&quot;, &quot;link&quot;: &quot;/situations/start-setup&quot;}]" />

<PromptBlock text="/pstack:recall งานของฉันเรื่อง export pipeline เมื่อสัปดาห์ที่แล้ว แล้วอ่าน open issue เรื่องแถวซ้ำ" />

<div class="spec-row">

## ใช้ทำอะไร

สร้าง context งานล่าสุดใหม่จากประวัติแชตของตัวเอง สถานะจริงใน git/gh และ "shared record" (user report, fix ที่ถูก revert, incident) แล้วคืน capsule สั้นๆ ว่าตอนนี้อยู่ตรงไหนและควรทำอะไรต่อ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อเปิดแชตใหม่เพื่อทำต่อจากงานสัปดาห์ก่อนและ agent ใหม่ไม่รู้อะไรเลย

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

recall สร้าง context ข้ามหลายแชตล่าสุด (ค่าเริ่มต้นย้อนหลัง 7 วัน ใน workspace ปัจจุบัน) ส่วน ketchup ครอบคลุมเฉพาะแชตนี้ตั้งแต่ข้อความล่าสุด การกลับไปทำต่อแชตเดียวเฉพาะคือ playbook Session pickup

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:recall`

</div>
