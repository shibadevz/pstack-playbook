---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-never-block-on-the-human"
---

# never-block-on-the-human

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-never-block-on-the-human</code></p>

<PromptBlock text="/pstack:poteto-mode ฉันจะไปพักก่อน ทำ migration ต่อไปเลย apply never block on the human หยุดถามเฉพาะ action ที่ย้อนกลับไม่ได้" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่ออยากถามว่า "ทำ X ดีไหม" กับงานที่ย้อนกลับได้ ให้ทำไปแล้วอธิบายเหตุผล ให้มนุษย์แก้ทางทีหลัง ส่วนงานย้อนกลับไม่ได้ (force-push, ลบ data จริง, ส่งข้อความออกนอก) ยังต้องขออนุญาต

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะถามว่า "ตั้งชื่อ branch แบบนี้ได้ไหม" ทั้งที่เปลี่ยนทีหลังได้

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply never block on the human" หรือโหลดตรงด้วย `/pstack:principle-never-block-on-the-human`

</div>
