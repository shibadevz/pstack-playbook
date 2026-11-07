---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:benchmark-checklist

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}, {&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}]" />

<PromptBlock text="/pstack:benchmark-checklist ช่วยตรวจ speedup 40% นี้ให้ดีก่อนใส่ใน PR description" />

<div class="spec-row">

## ใช้ทำอะไร

ตรวจตัวเลข performance ด้วยคำถาม 7 ข้อ (limiter, tuning, เกิน limit, error, ทำซ้ำได้, สำคัญจริงไหม, งานเกิดขึ้นจริงไหม) ก่อนรายงานหรือนำไปใช้ ผลคือ faster, slower, no measurable difference หรือ inconclusive

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะเขียนใน PR ว่า "export เร็วขึ้น 40%" และยังไม่รู้ว่า cache อุ่นอยู่หรือเปล่า

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

principle-explain-the-number เป็นกฎสั้น ส่วน skill นี้คือขั้นตอนเต็มสำหรับตัวเลข perf ถ้าแค่ขอ ballpark ครั้งเดียวก็พอ แต่ยังต้องเช็กข้อ 4 (error) และข้อ 7 (งานเกิดขึ้นจริง)

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:benchmark-checklist`

</div>
