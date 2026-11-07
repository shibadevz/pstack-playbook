---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Eval"
---

# Eval

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode run the eval playbook กับ &lt;การเปลี่ยนแปลง&gt;</code></p>

<PromptBlock text="/pstack:poteto-mode run the eval playbook กับ change ของฉันใน babysit skill เทียบกับเวอร์ชันปัจจุบันแบบ blind" />

<div class="spec-row">

## ใช้ทำอะไร

ทดสอบว่าการเปลี่ยน skill, โครงสร้าง หรือ prompt ส่งผลต่อพฤติกรรม agent อย่างไรก่อนนำไปใช้ โดยทดลองแบบ blind: หลาย candidate บน prompt เดียวกัน, judge แบบ blind และตรวจ chain จาก transcript

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อแก้ skill แล้วอยากรู้ว่า agent ทำตามจริงหรือไม่ก่อนรวมเข้า main

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

candidate ต้องไม่เห็นคำว่า eval, test, judge, rubric หรือ arena และ prompt ต้องเหมือนคำขอปกติของผู้ใช้ judge เห็นผลลัพธ์ตาม label ที่ปิดชื่อ model

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode run the eval playbook กับ <การเปลี่ยนแปลง>`

</div>
