---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Session pickup"
---

# Session pickup

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}, {&quot;title&quot;: &quot;เริ่มงาน/ตั้งค่า&quot;, &quot;link&quot;: &quot;/situations/start-setup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode take over this branch ช่วยรับช่วงงานต่อจาก &lt;branch&gt; นี้</code></p>

<PromptBlock text="/pstack:poteto-mode take over this branch อ่าน decision log หาว่าอะไรเสร็จแล้ว และทำต่อ อย่าทำงานที่เสร็จแล้วซ้ำ" />

<div class="spec-row">

## ใช้ทำอะไร

รับช่วงงานของ agent ก่อนหน้าจาก transcript, URL ของ cloud agent หรือ branch ที่ push แล้ว: อ่าน trail, สร้างสถานะใหม่, เทียบ done กับ pending และเริ่มจาก resume point โดยไม่ทำงานที่เสร็จซ้ำ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมี branch ที่ agent อีกแชตทำค้างไว้ และต้องรับต่อโดยไม่รื้อของเดิม

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก recall ที่สร้าง context ข้ามหลายแชต Session pickup กลับไปทำต่องานหนึ่งแชตหรือ branch ที่เจาะจง เป็นคู่กับ Pause safely และ trail ของงานก่อนหน้าถือเป็นข้อมูลที่เชื่อได้

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode take over this branch ช่วยรับช่วงงานต่อจาก <branch> นี้`

</div>
