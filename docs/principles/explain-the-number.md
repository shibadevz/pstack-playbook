---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-explain-the-number"
---

# explain-the-number

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}, {&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-explain-the-number</code></p>

<PromptBlock text="/pstack:poteto-mode benchmark ของ parser ใหม่ออกมา 2x apply explain the number ก่อนเราใส่ใน PR" />

<div class="spec-row">

## ใช้ทำอะไร

ก่อนเชื่อ รายงาน หรือลงมือตามตัวเลขที่วัดมา (speedup, regression, throughput, latency, eval result) ให้หาสิ่งที่จำกัดตัวเลข และตัดความเป็นไปได้ว่าวัดสิ่งอื่นที่ไม่ใช่งานจริง

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อได้ผล "เร็วขึ้น 2 เท่า" แต่ยังตอบไม่ได้ว่าทำไมไม่ใช่ 4 เท่า

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก prove-it-works ที่เช็กว่า output จริงหรือไม่ ส่วนนี้เช็กว่าตัวเลขวัดอะไรอยู่ ถ้าเป็นตัวเลข perf ให้รันขั้นตอนเต็มด้วย benchmark-checklist

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply explain the number" หรือโหลดตรงด้วย `/pstack:principle-explain-the-number`

</div>
