---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:tdd

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}, {&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}]" />

<PromptBlock text="/pstack:tdd เขียน regression test ที่ fail ก่อน สำหรับ bug ที่ export เขียนแถวซ้ำตอน retry แล้วค่อย fix ให้ test ผ่าน และ rerun เพื่อยืนยัน" />

<div class="spec-row">

## ใช้ทำอะไร

แก้ bug แบบ test-first: เขียน regression test ที่ fail ด้วยเหตุผลที่ถูกต้องก่อน แล้วแก้ production code ให้ผ่าน และถ้า test ไม่คุ้มก็ใช้ check ที่ใกล้เคียงที่สุดแทน

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ bug มี test target ในเครื่องที่ถูกและชัด เช่น function เดียวที่คืนค่าผิดเมื่อ input ซ้ำ

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้เมื่อผู้ใช้ขอ TDD หรือ test ที่ fail เอง หรือเมื่อ test path ถูกและชัดเท่านั้น ถ้าต้องตั้ง harness ใหญ่ ใช้ mock เปราะ หรือ repro ไม่ชัด ให้ข้ามการเพิ่ม test (no new test ดีกว่า test ที่แย่)

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:tdd`

</div>
