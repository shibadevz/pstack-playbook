---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Babysit"
---

# Babysit

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode babysit this pr ช่วยดูแลจนผ่าน CI ทั้งหมด</code></p>

<PromptBlock text="/pstack:poteto-mode babysit this pr ให้ CI เขียว" />

<div class="spec-row">

## ใช้ทำอะไร

ขับ PR หรือ stack ไปจนถึง merge-ready: ประกาศโหมด (drive, background, threads-only, check), เคลียร์ทีละ PR จากล่างสุด โดยเรียงลำดับ conflict, review thread, CI และหยุดตรงที่เป็นการตัดสินใจของมนุษย์

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ stack สร้างเสร็จแล้วและ CI แดง หรือมี review comment ค้าง

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ไม่ merge เว้นแต่ผู้ใช้ขอ merge, land หรือ ship ซึ่งเป็น Shipping ถ้าไม่ใช้ผ่าน poteto-mode วลีอย่าง "babysit this pr" อาจไปเรียก skill อื่นที่ติดตั้งไว้แทน Opening a PR ไม่เริ่ม babysit ให้เอง

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode babysit this pr ช่วยดูแลจนผ่าน CI ทั้งหมด`

</div>
