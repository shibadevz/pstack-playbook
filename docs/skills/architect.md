---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:architect

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<PromptBlock text="/pstack:architect with checkpoint ช่วยร่าง type และ module boundary ของ retry queue ใน src/jobs/ แล้วให้ดู design ก่อนค่อย implement" />

<div class="spec-row">

## ใช้ทำอะไร

ร่าง type, signature และโครง module โดยให้ body เป็น `not implemented` ก่อน ให้หลาย candidate ออกแบบผ่าน arena แล้ว implement ตาม sketch ที่เลือก

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังเพิ่ม module ใหม่ที่หลายส่วนต้องเรียกข้าม function boundary และกลัวว่าการเขียนโค้ดทันทีจะล็อกรูปแบบผิด

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ค่าเริ่มต้นคือ implement ต่อทันทีหลังเลือก design ถ้าอยากตรวจก่อนให้เติม "with checkpoint" ถ้า implementation ชนกับ sketch ซ้ำๆ skill นี้ให้ทิ้ง sketch แล้วออกแบบใหม่

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:architect`

</div>
