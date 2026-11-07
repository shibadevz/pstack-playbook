---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Orchestrate"
---

# Orchestrate

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}, {&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยดูแลโปรเจกต์นี้ทั้งหมด และรับผิดชอบ &lt;migration&gt; นี้จนกว่าจะ land</code></p>

<PromptBlock text="/pstack:poteto-mode ดูแล migration นี้จนกว่าจะ land ทำทั้งโปรเจกต์ผ่าน stacked PR มา check in กับฉันวันละสองครั้ง" />

<div class="spec-row">

## ใช้ทำอะไร

ให้ coordinator แชตเดียวเป็นเจ้าของ program ใหญ่ (หลายวัน, PR ซ้อนกันมาก, subagent หลายสิบถึงร้อย): เขียน brief, ระบายคิว, รักษา frontier ให้เขียว และไม่เขียนโค้ดเอง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมอบทั้ง migration ที่ต้อง land หลายสิบ PR ให้ coordinator ดูแลจนจบ

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Autonomous run ที่ขับ task เดียวถึง predicate และต่างจาก figure-it-out ที่ออกแบบ run เดียว ถ้างานที่ agent ตัวเดียวทำจบในงบของ session ได้ จะไม่ route มาที่นี่ pstack ไม่มี skill `/orchestrate` ถ้าเมนู slash แสดงว่าเป็นของ plugin อื่น

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยดูแลโปรเจกต์นี้ทั้งหมด และรับผิดชอบ <migration> นี้จนกว่าจะ land`

</div>
