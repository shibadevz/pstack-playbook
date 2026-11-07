---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-prove-it-works"
---

# prove-it-works

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-prove-it-works</code></p>

<PromptBlock text="/pstack:poteto-mode แก้ปุ่ม export apply prove it works ให้ดู output จริง ไม่ใช่ build log" />

<div class="spec-row">

## ใช้ทำอะไร

หลังงานเสร็จและก่อนประกาศว่าเสร็จ ให้ตรวจกับของจริง (รัน feature, อ่านค่าที่เก็บจริง, ดู diff) ไม่ใช่ proxy, self-report หรือ "compile ผ่าน"

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ build เขียว แต่ยังไม่มีใครกดปุ่ม export จริง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

เป็น principle ที่ใช้บ่อยสุดสำหรับแก้ run ที่รายงานสำเร็จจาก build เขียว ส่วน explain-the-number ตรวจว่าตัวเลขวัดอะไรอยู่

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply prove it works" หรือโหลดตรงด้วย `/pstack:principle-prove-it-works`

</div>
