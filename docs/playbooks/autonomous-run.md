---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Autonomous run"
---

# Autonomous run

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;ปล่อยรันเอง/ข้ามคืน&quot;, &quot;link&quot;: &quot;/situations/autonomous-overnight&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ฉันจะไปนอนแล้วนะ &lt;เป้าหมาย&gt; ถือว่าเสร็จเมื่อ &lt;เกณฑ์ตรวจ&gt; ผ่านครบ</code></p>

<PromptBlock text="/pstack:poteto-mode ฉันจะไปนอนแล้ว migrate ทุก caller ไปใช้ parser ใหม่ ใน worktree ใหม่ที่แตกจาก main done คือไม่เหลือ caller เก่า parser fixture ผ่านทั้งหมด และ API เก่าถูกลบ เก็บ decision log ไม่ต้องถามก่อน commit" />

<div class="spec-row">

## ใช้ทำอะไร

ขับงานยาวงานเดียวจนถึงเงื่อนไขที่ตรวจได้โดยไม่หยุด: ตั้ง predicate, เลือกกลไกปลุก (scheduler หรือ watcher), ทำการเปลี่ยนเล็กที่สุดต่อ iteration และ checkpoint ลง log

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อจะนอนและอยากให้ agent ทำต่อจน fixture ทุกอันผ่าน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ต่างจาก Orchestrate ที่เป็น program หลายวันหลาย PR plateau ไม่ใช่เหตุให้หยุด ให้เปลี่ยนวิธี และห้ามผ่อน predicate เพื่อประกาศชนะ ต้องมี check ที่ผ่านหรือไม่ผ่านได้ ไม่ใช่ระยะเวลา และกลไกปลุกอาจรายงาน capability gap ตาม runtime contract

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ฉันจะไปนอนแล้วนะ <เป้าหมาย> ถือว่าเสร็จเมื่อ <เกณฑ์ตรวจ> ผ่านครบ`

</div>
