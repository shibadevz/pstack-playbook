---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Investigation"
---

# Investigation

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;เข้าใจโค้ด&quot;, &quot;link&quot;: &quot;/situations/understand-code&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยสืบว่าทำไม &lt;อาการ&gt; เกิดขึ้น ยังไม่ต้องแก้โค้ดนะ</code></p>

<PromptBlock text="/pstack:poteto-mode ช่วยสืบว่าทำไม export retry สามครั้งก่อน fail บอกว่าเรารู้อะไรบ้าง ใช้ data อะไร และ hypothesis ที่ดีที่สุดคืออะไร ยังไม่ต้องแก้โค้ด" />

<div class="spec-row">

## ใช้ทำอะไร

คำถามแบบอ่านอย่างเดียว (X ทำงานอย่างไร, ทำไม Y ถูกสร้างแบบนี้, แน่ใจไหมว่า Z, ควรทำ X หรือ Y) ได้คำอธิบายพร้อมอ้างอิงหรือคำแนะนำพร้อมตาราง tradeoff โดยไม่แก้โค้ด

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อถามว่า "retry ทำงานอย่างไรและทำไมถึงใช้ 30 วินาที" และยังไม่ต้องการแก้อะไร

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ไม่ต้องมี PR ถ้าสืบเพื่อเตรียมแก้โค้ด จะส่งกลับให้ผู้ใช้แล้ว route ไปที่ Bug fix หรือ Feature ใช้ how (และ why สำหรับเรื่องเหตุผล)

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยสืบว่าทำไม <อาการ> เกิดขึ้น ยังไม่ต้องแก้โค้ดนะ`

</div>
