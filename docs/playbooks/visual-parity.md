---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Visual parity"
---

# Visual parity

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วย migrate &lt;components&gt; ให้หน้าตาตรงกับของเดิมระดับ pixel</code></p>

<PromptBlock text="/pstack:poteto-mode migrate component Button และ Card ไปใช้ styling system ใหม่ โดย pixel-exact parity จับ baseline screenshot ก่อน แล้ว verify ด้วย image diff" />

<div class="spec-row">

## ใช้ทำอะไร

ทำให้ UI เหมือนกันแบบ pixel-exact ระหว่างสอง implementation หรือเมื่อย้ายระบบ styling: สร้าง baseline ด้วย visual regression harness ก่อน แล้วย้ายทีละ component และตรวจด้วย image diff จนเป็นศูนย์

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังย้าย styling ของปุ่มและ card ไประบบใหม่และผลต้องตรงเดิมทุกพิกเซล

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

baseline คือ spec ห้ามแก้ harness, ห้ามแตะ baseline และห้ามปรับโครงสร้าง component เพื่อให้ diff ผ่าน diff ที่ไม่ใช่ศูนย์คือ fail ถ้าไม่มี baseline จะไม่รับรอง parity

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วย migrate <components> ให้หน้าตาตรงกับของเดิมระดับ pixel`

</div>
