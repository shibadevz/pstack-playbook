---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Refactoring"
---

# Refactoring

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ย้าย &lt;โค้ด&gt; ไปรวมไว้ใน module เดียว โดย behavior ต้องไม่เปลี่ยนเลย ช่วยบันทึก output ปัจจุบันไว้ก่อน</code></p>

<PromptBlock text="/pstack:poteto-mode ย้ายโค้ด pricing จากสามไฟล์เข้า src/pricing/ โดย behavior ต้องไม่เปลี่ยนเลย บันทึก output ปัจจุบันก่อน แล้วพิสูจน์ว่าไม่เปลี่ยนหลังย้าย" />

<div class="spec-row">

## ใช้ทำอะไร

เปลี่ยนโครงสร้างโดยไม่เปลี่ยน behavior (rename, extract, inline, dedupe, move): ตรึง behavior ด้วย characterization test ก่อน แล้วลบ ย้ายเป็นก้าวเล็ก และพิสูจน์ว่า behavior เดิมกับของจริง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องย้ายโค้ดกระจายสามไฟล์มารวม module เดียวโดยผลลัพธ์ต้องเหมือนเดิมทุกอย่าง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Feature ที่เพิ่ม behavior และ Bug fix ที่แก้ behavior ถ้าเจอ bug จริงระหว่างทางให้แยกออกและ ship โครงสร้างก่อน งานโครงสร้างที่ใหญ่ข้ามหลายจุดให้ใช้ figure-it-out

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ย้าย <โค้ด> ไปรวมไว้ใน module เดียว โดย behavior ต้องไม่เปลี่ยนเลย ช่วยบันทึก output ปัจจุบันไว้ก่อน`

</div>
