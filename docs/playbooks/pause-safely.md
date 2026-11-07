---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Pause safely"
---

# Pause safely

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode pause safely ช่วยหยุดงานให้ปลอดภัยก่อนเลิกทำ</code></p>

<PromptBlock text="/pstack:poteto-mode pause safely commit สิ่งที่มีเป็น wip commit และเขียน resume note" />

<div class="spec-row">

## ใช้ทำอะไร

หยุดงานที่ค้างอยู่อย่างสะอาดเพื่อให้กลับมาต่อได้: หยุดที่ขอบที่ปลอดภัย, commit เป็น `wip:` เดียว และเขียน resume note ที่ agent ที่เริ่มใหม่อ่านต่อได้

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังจะ offline หรือ context ใกล้ถูก compact และอยากให้งานต่อได้

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้เมื่อสั่งหยุดชัดเจนเท่านั้น ถ้าพูดว่า "keep going" หรือ "going to bed, keep going" จะไม่หยุด ไม่ push หรือเปิด PR ใหม่เพื่อหยุด เป็นคู่กับ Session pickup

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode pause safely ช่วยหยุดงานให้ปลอดภัยก่อนเลิกทำ`

</div>
