---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Shipping"
---

# Shipping

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode land the stack ช่วย ship ทุก PR ใน stack ให้ครบ</code></p>

<PromptBlock text="/pstack:poteto-mode ช่วย land the stack ให้หน่อย" />

<div class="spec-row">

## ใช้ทำอะไร

ครึ่งหลังของ Babysit: ตรวจ PR ที่เขียวแต่ละอันแยกอิสระ แล้ว land เฉพาะช่วงที่ verified ต่อเนื่องจากล่างสุดขึ้นไป ทีละ PR ผ่าน `gh` (หรือ `origin` ถ้ามี) แล้วหยุดที่ ceiling

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ stack เขียวและผู้ใช้สั่งให้ land

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

เขียวไม่เท่ากับปลอดภัย: ต้องมี verdict อิสระต่อ PR ก่อน และไม่แตะ stack ระหว่าง land ยกเว้นย้าย PR ถัดไปหลัง merge ถ้ามี verdict ไม่ครบ จะหยุดที่ PR ล่างสุดที่ยังไม่ผ่าน

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode land the stack ช่วย ship ทุก PR ใน stack ให้ครบ`

</div>
