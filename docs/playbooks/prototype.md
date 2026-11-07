---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Prototype"
---

# Prototype

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ออกแบบ/วางแผน&quot;, &quot;link&quot;: &quot;/situations/design-plan&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยทำ prototype หลายทางเลือกให้ &lt;ฟีเจอร์&gt;</code></p>

<PromptBlock text="/pstack:poteto-mode ทำ prototype layout ของหน้า settings สองสามแบบ ใส่ไว้หลัง switcher แล้วส่ง screenshot ของแต่ละแบบมาให้" />

<div class="spec-row">

## ใช้ทำอะไร

ร่างต้นแบบทิ้งขว้างเพื่อตัดสินใจ design หรือ behavior อย่างถูก: สร้างใน scratch dir แยก, เทียบหลายแบบหลัง switcher เดียว, ถ่าย screenshot แล้วสรุปตัวเลือก tradeoff และคำแนะนำ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อต้องเลือก layout ของหน้า settings และอยากเลือกจากสิ่งที่รันได้ ไม่ใช่คำบรรยาย

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ผลคือการตัดสินใจกับ artifact ทิ้งขว้าง ไม่ใช่โค้ดที่ ship ได้ การสร้างจริงตามหลังด้วย Feature ถ้าไม่มี decision ให้ตัดสินใจก็ไม่ต้อง prototype

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยทำ prototype หลายทางเลือกให้ <ฟีเจอร์>`

</div>
