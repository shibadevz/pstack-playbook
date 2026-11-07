---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Trace forensics"
---

# Trace forensics

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}, {&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยวินิจฉัยไฟล์ trace นี้ ยังไม่ต้อง fix</code></p>

<PromptBlock text="/pstack:poteto-mode ช่วยวินิจฉัยว่าทำไม app ค้าง โดยใช้ startup.cpuprofile ที่แนบมา โหลดเข้า sqlite หา hot path และ map กลับไปที่ source ยังไม่ต้อง fix" />

<div class="spec-row">

## ใช้ทำอะไร

วินิจฉัยจาก artifact ที่จับมาแล้ว (cpuprofile, trace, spindump, heap snapshot) โดย dump ลง sqlite เพื่อ query หาเส้นทางร้อนหรือ retainer chain แล้วอ้างถึง source

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมีคนส่งไฟล์ .cpuprofile มาให้ว่าแอปค้าง และไม่มี process ให้ไปจับเพิ่ม

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Runtime forensics ตรงที่ artifact เป็นชุดข้อมูลคงที่ ให้อ่านไม่ใช่รันซ้ำ ถ้าไม่มีคู่ before/after จะรายงานเป็นสมมติฐานที่แข็งที่สุด ไม่ใช่สาเหตุที่ยืนยันแล้ว

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยวินิจฉัยไฟล์ trace นี้ ยังไม่ต้อง fix`

</div>
