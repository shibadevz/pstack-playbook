---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Bug fix"
---

# Bug fix

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode &lt;อาการ&gt; ช่วย repro ก่อน แล้วค่อย fix และ verify</code></p>

<PromptBlock text="/pstack:poteto-mode ตอน retry แล้ว export สร้างแถวซ้ำ ช่วย repro ให้เห็นก่อน แล้วค่อย fix และ verify" />

<div class="spec-row">

## ใช้ทำอะไร

แก้ defect ที่รายงานมา: repro เองบน surface ที่ตรงกัน, ไล่หา cause แบบ binary search ด้วยหลักฐานตอนรัน, วางแผนและ delegate fix, ตรวจบน surface เดิมและ stage commit ให้ failing repro อยู่ก่อน fix

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อมีรายงานว่า export สร้างแถวซ้ำตอน retry

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ทุกบรรทัดที่ ship ต้องสืบกลับไปถึงหลักฐานตอนรัน การแก้แบบ "อาจช่วย" ไม่ถูก ship ถ้ามี test path ที่ถูกให้ใช้ tdd ถ้ายังไม่รู้สาเหตุและต้องการแค่วินิจฉัย ใช้ Runtime forensics

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode <อาการ> ช่วย repro ก่อน แล้วค่อย fix และ verify`

</div>
