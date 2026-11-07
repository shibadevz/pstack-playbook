---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Multi-phase or multi-PR plan"
---

# Multi-phase or multi-PR plan

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยแปลง design นี้ให้เป็นแผนงาน</code></p>

<PromptBlock text="/pstack:poteto-mode เปลี่ยน design นี้เป็น plan แบ่งเป็น PR เล็กๆ ที่ verify ได้ แต่ละอันมีขั้นตอน verification ของตัวเอง" />

<div class="spec-row">

## ใช้ทำอะไร

เขียนแผนสำหรับงานที่ข้ามหลาย phase หรือ PR ซ้อนกัน ให้เป็น checklist ที่ owner รันทีละช่องและผู้ใช้ตรวจจากหลักฐาน แผนคือ deliverable และไม่ implement

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ design นิ่งแล้วและต้องการแผน migration เป็น PR เล็กที่ตรวจได้ทีละอัน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ถ้างานแค่หนึ่งสองไฟล์และวิธีชัดเจนจะข้ามแผน pstack ไม่มี planning skill ให้ใช้ plan mode ของ runtime ควบคู่ถ้ามี แผนรันสคริปต์ตรวจ `check-plan.mjs` และเริ่มทำเมื่อผู้ใช้สั่ง go เท่านั้น

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยแปลง design นี้ให้เป็นแผนงาน`

</div>
