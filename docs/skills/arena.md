---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:arena

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}, {&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<PromptBlock text="/pstack:arena ขอความเห็นที่สองเรื่อง design ของ thread นี้ ให้ candidate หลายตัวทำจาก brief เดียวกัน แล้วให้ judge ต่าง model เลือกแนวทางที่ดีที่สุดพร้อมเก็บส่วนดีของตัวอื่นมารวม" />

<div class="spec-row">

## ใช้ทำอะไร

ให้ candidate N ตัวทำ brief เดียวกัน ให้ judge ข้าม model ตัดสิน เลือก base แล้วเก็บส่วนที่ดีที่สุดของตัวอื่นมาต่อเข้าไป

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ artifact ที่ไม่ง่ายถ้าลองแค่ครั้งเดียวอาจล็อกรูปผิด หรืออยากได้ความเห็นที่สองเรื่อง design

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

arena ให้ทุก worker ทำ brief เดียวกันแล้วรวมส่วนดี ส่วน swarm แบ่งงานเป็น slice หรือแข่งกันแล้วรายงานเดียว อย่าใช้ arena เพื่อ coverage ถ้า model-family diversity ยังยืนยันไม่ได้ ตาม runtime contract ของ port จะรายงานข้อจำกัดนี้

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:arena`

</div>
