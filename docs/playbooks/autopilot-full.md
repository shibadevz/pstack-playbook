---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Autopilot-full"
---

# Autopilot-full

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode full autopilot กับ queue นี้ แต่ละรายการเป็นอิสระจากกัน</code></p>

<PromptBlock text="/pstack:poteto-mode full autopilot กับ queue นี้ แต่ละรายการเป็นอิสระต่อกัน" />

<div class="spec-row">

## ใช้ทำอะไร

ผลักคิวของ PR อิสระจนถึง merged ด้วย autonomy เต็ม: หนึ่ง owner ต่อ PR ตั้งแต่ build ถึง merge และ root ใช้ swarm ที่ไม่เคยเขียนโค้ดตรวจก่อน owner merge

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมีรายการ PR สิบอัน แต่ละอันเป็นอิสระ และผู้ใช้ให้สิทธิ์ land เอง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้เมื่อ PR อิสระต่อกันและให้สิทธิ์ land แล้ว ถ้าต้องการรีวิวก่อน land หรืองานต่อเนื่องกัน ใช้ Autopilot-stack รายการที่ผู้ใช้ระบุว่าเป็นของตัวเองจะหยุดที่ merge-ready

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode full autopilot กับ queue นี้ แต่ละรายการเป็นอิสระจากกัน`

</div>
