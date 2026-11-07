---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:maintain-verification-skill

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;ปรับแต่ง PStack&quot;, &quot;link&quot;: &quot;/situations/customize-pstack&quot;}]" />

<PromptBlock text="/pstack:maintain-verification-skill ช่วย audit verify skill เทียบกับ app ปัจจุบัน" />

<div class="spec-row">

## ใช้ทำอะไร

รอบดูแลที่ทำให้ verification skill และ feature map ตรงกับ app: source reader ขนานต่อ feature, หนึ่ง session ขับทุก feature และส่ง PR แก้ที่พิสูจน์แล้วไม่เกินหนึ่งอัน ผลเป็น clean, changed หรือ blocked

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ app เปลี่ยนไปหลาย release แล้วสงสัยว่า verify skill ที่สร้างไว้เริ่มล้าสมัย

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต้องมี verification skill อยู่แล้ว (ปกติ `.claude/skills/verify-*/`) ถ้าไม่มีจะหยุดและชี้ไปที่ create-verification-skill ผลรันนี้แก้เฉพาะโฟลเดอร์ของ verification skill ไม่แก้ product code

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:maintain-verification-skill`

</div>
