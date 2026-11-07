---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:ketchup

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เขียนเอกสาร/สื่อสาร&quot;, &quot;link&quot;: &quot;/situations/docs-communication&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<PromptBlock text="/pstack:ketchup ช่วยตามให้ทันว่าในแชตนี้มีอะไรเปลี่ยนไปบ้าง" />

<div class="spec-row">

## ใช้ทำอะไร

ตามผู้ใช้ให้ทันสิ่งที่เปลี่ยนในแชตนี้ตั้งแต่ข้อความล่าสุดของเขา ด้วยประโยคสั้นๆ และ visual เล็กๆ พร้อมบริบทพอให้ตัดสินใจแต่ละ action item (reply ยาวไม่เกินประมาณ 150 คำ)

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกลับมาจากพักแล้วมี subagent รายงานเข้ามาหลายอัน และไม่รู้ว่าอะไรต้องให้ตัวเองตัดสินใจ

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ketchup ครอบคลุมเฉพาะแชตนี้ตั้งแต่ข้อความล่าสุด ส่วน recall สร้าง context ข้ามหลายแชตล่าสุด ถ้าจะกลับไปทำต่อแชตหรือ branch เฉพาะอันให้ใช้ playbook Session pickup

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:ketchup`

</div>
