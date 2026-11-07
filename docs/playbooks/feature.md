---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Feature"
---

# Feature

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;สร้างฟีเจอร์&quot;, &quot;link&quot;: &quot;/situations/build-feature&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode เพิ่ม &lt;พฤติกรรม&gt; โดย &lt;output ปัจจุบัน&gt; ต้องเหมือนเดิมทุก byte ช่วย verify ทั้งสองอย่าง</code></p>

<PromptBlock text="/pstack:poteto-mode เพิ่ม flag --json ให้คำสั่ง export ผลลัพธ์แบบ text ต้องเหมือนเดิมแบบ byte-identical และ verify ทั้งสองแบบ" />

<div class="spec-row">

## ใช้ทำอะไร

สร้างหรือเปลี่ยน behavior จากรูปข้อมูลที่ตั้งชื่อ: ใช้ how กับ subsystem, architect, เขียน throughput checkpoint, delegate โค้ดให้ subagent, ตรวจบน surface ที่ตรงกัน และ rebase เป็น commit เล็กเรียงลำดับ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องเพิ่ม flag `--json` ให้ command และผลแบบ text ต้องไม่เปลี่ยนแม้แต่ byte เดียว

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ถ้า implementation มีหลายรูปแบบที่ใช้ได้ จะ delegate ผ่าน arena ถ้า design ยังถูกโต้แย้งให้รัน interrogate ก่อน ship งานที่ใหญ่ข้ามหลายจุดหรือต้องไปตรวจทีหลัง ให้ใช้ figure-it-out

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode เพิ่ม <พฤติกรรม> โดย <output ปัจจุบัน> ต้องเหมือนเดิมทุก byte ช่วย verify ทั้งสองอย่าง`

</div>
