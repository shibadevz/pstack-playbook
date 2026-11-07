---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:automate-me

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}]" />

<PromptBlock text="/pstack:automate-me ช่วยอัปเดต mode skill ของฉันจากแชต 3 สัปดาห์ล่าสุดใน workspace นี้" />

<div class="spec-row">

## ใช้ทำอะไร

ร่างหรืออัปเดต personal `-mode` skill จากนิสัยการทำงานของผู้ใช้ โดยขุดประวัติแชตล่าสุด ถามเพิ่ม แล้วเขียนผ่าน pstack-create-skill และ unslop

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องพิมพ์ "ใช้ worktree แยก PR เล็ก" ซ้ำทุกแชตและอยากให้ agent ทำตามเองโดยไม่ต้องบอก

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

reflect เปลี่ยนบทเรียนของงานหนึ่งงานเป็นการแก้ skill ที่มีอยู่ ส่วน automate-me สร้าง skill ส่วนตัวจากนิสัยโดยรวม การขุดประวัติอ่านเฉพาะ transcript ของ workspace ปัจจุบัน

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:automate-me`

</div>
