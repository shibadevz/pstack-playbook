---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:reflect

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}]" />

<PromptBlock text="/pstack:reflect ช่วยจดสิ่งที่เราเรียนรู้ไว้ เพื่อให้รอบหน้าไม่พลาดซ้ำ" />

<div class="spec-row">

## ใช้ทำอะไร

spawn reviewer สามตัวพร้อมกัน (judgment, tooling, divergent) ไล่ดู transcript ของแชตปัจจุบัน แล้วส่งบทเรียนแต่ละข้อไปเป็นการแก้ skill ที่มีอยู่

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อจบงานที่มี agent ทำผิดซ้ำแล้วอยากให้บทเรียนไม่หายไป

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ข้ามถ้าแชตไม่มีสาระหรือบทเรียนมีใน skill อยู่แล้ว (เรื่องที่เกิดครั้งเดียวไม่ใช่บทเรียน) อนุมัติเฉพาะการแก้ที่เปลี่ยนการตัดสินใจครั้งต่อไป ต่างจาก automate-me ที่สร้าง skill ส่วนตัวจากนิสัยโดยรวม

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:reflect`

</div>
