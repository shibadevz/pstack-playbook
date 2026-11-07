---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:interrogate

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Review&quot;, &quot;link&quot;: &quot;/situations/review&quot;}]" />

<PromptBlock text="/pstack:interrogate ทั้ง branch แบบสงสัยไว้ก่อน ยังไม่ต้องแก้อะไร ไม่ต้องจุกจิกเว้นแต่เป็น bug หรือ regression จริง" />

<div class="spec-row">

## ใช้ทำอะไร

ให้ reviewer หลายตัว (หนึ่งตัวต่อ model ที่ตั้งค่าไว้) รีวิวการเปลี่ยนแปลงแบบ adversarial จากมุมอิสระ แล้วสรุป verdict ที่แยกเป็นหมวด act-on และ dismissed โดยไม่แก้โค้ดเอง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ branch ใกล้เสร็จและอยากให้ต่างคนต่างโมเดลลองพังก่อนเปิด PR

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

interrogate รีวิวตัว diff ส่วน blast-radius หาสิ่งที่พังนอก diff panel มาจาก role `interrogate reviewers` ใน models.json ถ้าไม่ได้ตั้งค่า seat จะ inherit model ของแชต ซึ่งไม่ใช่ความหลากหลายของ model-family

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:interrogate`

</div>
