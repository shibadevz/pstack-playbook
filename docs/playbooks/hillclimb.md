---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Hillclimb"
---

# Hillclimb

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}, {&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยปรับ &lt;metric&gt; ไปเรื่อย ๆ จนถึง &lt;เป้าหมาย&gt;</code></p>

<PromptBlock text="/pstack:poteto-mode ช่วยปรับ cold start time ต่อไปจนต่ำกว่า 1.5 วินาทีบน benchmark fixture เก็บ decision log และทำหนึ่ง commit ต่อหนึ่งการปรับที่รับไว้" />

<div class="spec-row">

## ใช้ทำอะไร

ปรับปรุง metric เดียวอย่างต่อเนื่องและเป็นวิทยาศาสตร์จนถึงเป้า: วน loop สมมติฐานทีละอัน วัดก่อน-หลังด้วย harness ที่ freeze แล้ว บันทึก `decision.tsv` และ commit ต่อหนึ่ง win ที่ยอมรับ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องการลดเวลา cold start จาก 3.2 วินาทีให้ต่ำกว่า 1.5 วินาที และไม่ใช่การแก้ครั้งเดียว

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Perf issue ที่เป็นการแก้ครั้งเดียว Hillclimb คือ loop หนึ่งการเปลี่ยน หนึ่งการวัด เก็บหรือ revert และถ้าไม่มี case ที่ repro อาการได้ ให้แก้ repro ก่อน

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยปรับ <metric> ไปเรื่อย ๆ จนถึง <เป้าหมาย>`

</div>
