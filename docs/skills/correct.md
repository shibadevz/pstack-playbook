---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:correct

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<PromptBlock text="/pstack:correct agent ชอบเพิ่ม config flag ใหม่โดยไม่ลงทะเบียนใน schema" />

<div class="spec-row">

## ใช้ทำอะไร

หาความผิดพลาดที่ agent ทำซ้ำใน repo แล้วทำให้เป็นไปไม่ได้ โดยลองระดับสูงสุดที่ใช้ได้ก่อน: architecture, type, lint ที่ error บอกวิธีแก้, test และเขียน docs เป็นอย่างสุดท้าย พร้อมพิสูจน์ว่า check ใหม่ fail กับความผิดพลาดจริงในอดีต

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องแก้ agent เรื่องเดิมซ้ำๆ เช่นเพิ่ม config flag แล้วไม่ลงทะเบียนใน schema

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

การแก้ในแชตช่วยได้แค่ run เดียว ส่วน /pstack:correct แก้ที่ repo เพื่อให้ run ถัดไปทำผิดไม่ได้ class ของความผิดพลาดต้องเกิดอย่างน้อยสองครั้งจึงนับ

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:correct`

</div>
