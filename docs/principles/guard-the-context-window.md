---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-guard-the-context-window"
---

# guard-the-context-window

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;เข้าใจโค้ด&quot;, &quot;link&quot;: &quot;/situations/understand-code&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-guard-the-context-window</code></p>

<PromptBlock text="/pstack:poteto-mode ไล่ดู crash log 40 ไฟล์นี้ apply guard the context window ให้ subagent อ่าน log แล้วคุณเก็บแค่ summary" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อ context กำลังเต็ม (output ใหญ่ ไฟล์ยาว อ่านซ้ำ วางแผน fan-out) ให้ส่งงานก้อนใหญ่ให้ subagent และเก็บแค่สรุปใน main thread ไม่ใช่ payload ดิบ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องอ่าน trace ขนาด 50 MB และไม่อยากให้ main thread เต็มด้วย dump

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply guard the context window" หรือโหลดตรงด้วย `/pstack:principle-guard-the-context-window`

</div>
