---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:figure-it-out

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<PromptBlock text="/pstack:figure-it-out migrate ทุก caller ของ logger API เก่าไปใช้ API ใหม่ done คือ API เก่าถูกลบแล้วและ test suite ทั้งหมดผ่าน" />

<div class="spec-row">

## ใช้ทำอะไร

ออกแบบ playbook เฉพาะงานเมื่อไม่มี playbook ไหนพอดี: Frame, ออกแบบ workflow, วน loop แบบสมมติฐาน-วัด-เก็บหรือ revert และจดการตัดสินใจไว้ให้คนตรวจทีหลัง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้อง migrate ทุก caller ของ API เก่าข้ามหลายจุด หรือเป็นงานที่คนจะมารีวิวหลังเดินไปไหนแล้ว

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

figure-it-out ออกแบบ run หนึ่งครั้งที่เข้มงวด ส่วน playbook Orchestrate รันทั้ง program ที่กินหลายวันและหลาย PR และ playbook Autonomous run ขับ task เดียวไปจนถึงเงื่อนไขที่ตรวจได้

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:figure-it-out`

</div>
