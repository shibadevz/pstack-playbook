---
pageClass: entity-page entity-principles
outline: false
title: "/pstack:principle-encode-lessons-in-structure"
---

# encode-lessons-in-structure

<EntityMeta type="principles" label="Principle" :sits="[{&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}, {&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:principle-encode-lessons-in-structure</code></p>

<PromptBlock text="/pstack:poteto-mode นี่เป็นครั้งที่สามแล้วที่ agent ลืมลงทะเบียน flag ใน schema apply encode lessons in structure" />

<div class="spec-row">

## ใช้ทำอะไร

เมื่อเขียนคำสั่งเดิมซ้ำเป็นครั้งที่สอง หรือเห็นการแก้ที่เกิดซ้ำ ให้เข้ารหัสกฎเป็น lint, metadata flag, runtime check หรือ script แทนการเพิ่มข้อความ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องบอก agent "อย่าลืม register flag ใน schema" เป็นครั้งที่สามแล้ว

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ถ้ากฎต้องใช้ดุลยพินิจและเข้ารหัสไม่ได้ ให้ทำคำสั่งเด่นขึ้นและเพิ่มตัวอย่างความผิดพลาด ส่วน /pstack:correct เป็น skill เต็มที่ใช้หลักนี้ทั่ว repo

</div>

<div class="spec-row">

## วิธีเรียก

ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply encode lessons in structure" หรือโหลดตรงด้วย `/pstack:principle-encode-lessons-in-structure`

</div>
