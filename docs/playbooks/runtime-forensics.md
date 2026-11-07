---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Runtime forensics"
---

# Runtime forensics

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}, {&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยวินิจฉัยว่าทำไม process วนใช้ CPU ตอน idle ให้ profile process ที่กำลังรันอยู่ ยังไม่ต้อง fix</code></p>

<PromptBlock text="/pstack:poteto-mode desktop app ใช้ CPU 80% ตอน idle ช่วยจับ CPU profile จาก process ที่กำลังรันและวินิจฉัยสาเหตุ ยังไม่ต้อง fix" />

<div class="spec-row">

## ใช้ทำอะไร

วินิจฉัยอาการตอนรัน (leak, idle-CPU spin, glitch) จาก instrumentation ของ process จริง ผลคือคำวินิจฉัยที่อ้างอิงได้ ไม่ใช่ fix

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ process กิน CPU ตอนไม่มีใครใช้ และอยากรู้ว่า function ไหนวนอยู่

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Trace forensics ที่ artifact จับไว้แล้ว (ที่นี่จับสัญญาณจาก process ที่ยังรันอยู่) เมื่อรู้สาเหตุแล้วให้ส่งต่อไป Bug fix หรือ Perf issue

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยวินิจฉัยว่าทำไม process วนใช้ CPU ตอน idle ให้ profile process ที่กำลังรันอยู่ ยังไม่ต้อง fix`

</div>
