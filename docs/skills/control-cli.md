---
pageClass: entity-page entity-skills
outline: false
---

# /pstack:control-cli

<EntityMeta type="skills" label="Workflow skill" :sits="[{&quot;title&quot;: &quot;Verify/เทส&quot;, &quot;link&quot;: &quot;/situations/verify-test&quot;}, {&quot;title&quot;: &quot;เจอ bug&quot;, &quot;link&quot;: &quot;/situations/found-bug&quot;}]" />

<PromptBlock text="/pstack:control-cli ช่วย drive interactive prompt flow ของ ./bin/mycli เก็บ transcript ไว้ และวัด startup time" />

<div class="spec-row">

## ใช้ทำอะไร

สร้างหรือปรับ harness ในเครื่อง (tmux หรือ PTY script) เพื่อขับ ตรวจ และ profile CLI/TUI แบบ interactive โดยไม่ต้องใช้ service ภายนอก

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ bug อยู่ใน prompt flow ของ CLI ที่ต้องกด arrow key และ Ctrl-C หรืออยากวัด startup time

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้ harness ที่ repo มีอยู่ก่อน ถ้าไม่มีค่อยประกอบจากเครื่องมือมาตรฐาน poteto-mode ใช้ skill นี้เป็น control skill ของ surface แบบ CLI/TUI ส่วน UI บน browser ใช้ control-ui

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:control-cli`

</div>
