---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Autopilot-stack"
---

# Autopilot-stack

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode stack them, don&#x27;t ship ช่วย stack ไว้ก่อน ยังไม่ต้อง ship</code></p>

<PromptBlock text="/pstack:poteto-mode autopilot การเปลี่ยนแปลงเหล่านี้ แต่ stack them, don&#x27;t ship ฉันจะ land stack เอง" />

<div class="spec-row">

## ใช้ทำอะไร

สร้างและตรวจคิวของการเปลี่ยนแปลงด้วย autonomy เต็ม แล้วส่งมอบเป็น stack เส้นตรงของ PR ที่ chain ด้วย base branch ให้ผู้ใช้รีวิวและ land เอง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่ออยากให้ agent สร้าง stack ให้ครบแต่ยังไม่ merge อะไรเอง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Autopilot-full ตรงที่ owner รายงาน STACK-READY แทน merge-ready และไม่ retarget, rebase หรือ merge เอง มีแค่ root ที่แตะ topology และผู้ใช้เป็นคน land

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode stack them, don't ship ช่วย stack ไว้ก่อน ยังไม่ต้อง ship`

</div>
