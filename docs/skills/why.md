---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:why

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เข้าใจโค้ด&quot;, &quot;link&quot;: &quot;/situations/understand-code&quot;}, {&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}]" />

<PromptBlock text="/pstack:why ทำไม export retry ถึงใช้ timeout 30 วินาที ช่วยดูประวัติและ incident ที่เกี่ยวข้อง" />

<div class="spec-row">

## ใช้ทำอะไร

สืบเหตุผลและเจตนาเบื้องหลังโค้ด: ค้นหลายแหล่งขนาน (source control, issue tracker, docs, chat, observability ฯลฯ ตาม MCP ที่มี) แล้วสรุปพร้อมอ้างอิงและบอกระดับความมั่นใจ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อสงสัยว่าทำไม threshold ถึงเป็น 30 วินาที หรือทำไมโค้ดส่วนนี้เพิ่งพังหลัง release ล่าสุด

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

why ตอบว่าทำไม ส่วน how ตอบว่าทำงานอย่างไร ความครอบคลุมของคำตอบขึ้นกับ MCP ที่ติดตั้ง และรายงานจะบอกว่าค้นแหล่งไหนบ้าง

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:why`

</div>
