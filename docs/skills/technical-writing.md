---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:technical-writing

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;เขียนเอกสาร/สื่อสาร&quot;, &quot;link&quot;: &quot;/situations/docs-communication&quot;}, {&quot;title&quot;: &quot;PR &amp; Ship&quot;, &quot;link&quot;: &quot;/situations/pr-ship&quot;}]" />

<PromptBlock text="/pstack:technical-writing เขียน PR description สำหรับ branch นี้ ให้มี why, what changed, scope, blast radius และ verification" />

<div class="spec-row">

## ใช้ทำอะไร

มาตรฐานงานเขียนเทคนิคแบบหลายชั้น (Diátaxis, Google developer style, STE, Global English) สำหรับ docs, RFC, README, PR description และ commit message

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อกำลังเขียน PR description ที่ผู้รีวิวต้องอ่านครั้งเดียวแล้วเข้าใจ

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

playbook Opening a PR ใช้ skill นี้กับ PR title, description และ commit body แล้วตามด้วย unslop ใช้ชื่อ symbol, file, flag จริงของ codebase แทนคำอธิบายอ้อมๆ

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:technical-writing`

</div>
