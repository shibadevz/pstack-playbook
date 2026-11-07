---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-attack-the-premise"
---

# attack-the-premise

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}, {&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-attack-the-premise</code></p>

<PromptBlock text="/pstack:poteto-mode flaky sync test ยัง fail อยู่หลังแก้ไปสองรอบ ซึ่งทั้งสองรอบสมมติว่า cache เป็นสาเหตุ ช่วย apply attack the premise" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อ fix สองอันขึ้นไปที่อยู่บน premise เดียวกันไม่ผ่าน gate เดิม ให้สำรวจก่อนว่า actor ไหนถือความไม่สมดุลอยู่ แล้วตั้งคำถามกับ premise แทนการเขียน fix ที่สามบน premise เดิม

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อแก้ race ด้วย lock สองรอบแล้ว test ยังพังที่เดิม และควรถามว่า lock คือคำตอบจริงหรือเปล่า

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้เฉพาะตอน fix ซ้ำล้มเหลว ถ้าเพิ่งเริ่มแก้ให้ใช้ fix-root-causes

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply attack the premise" หรือโหลดตรงด้วย `/pstack:principle-attack-the-premise`

</div>
