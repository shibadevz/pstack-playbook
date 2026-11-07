---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Worktree and simulator cleanup"
---

# Worktree and simulator cleanup

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;Refactor/เก็บกวาด&quot;, &quot;link&quot;: &quot;/situations/refactor-cleanup&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode ช่วยเก็บกวาด worktree และคืนพื้นที่ดิสก์</code></p>

<PromptBlock text="/pstack:poteto-mode อะไรกิน disk ฉันอยู่ ช่วยล้าง worktree ที่ merge แล้วหรือถูกทิ้ง และลบ simulator เก่า ให้ดูก่อนว่าอะไร prune ได้อย่างปลอดภัยก่อนลบ" />

<div class="spec-row">

## ใช้ทำอะไร

เคลียร์พื้นที่ดิสก์ด้วยการ prune git worktree ที่ merge แล้วหรือถูกทิ้ง และ iOS simulator เก่า โดยตรวจการใช้งานก่อนลบ

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อดิสก์เต็มและสงสัยว่า worktree เก่าและ simulator กินพื้นที่

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ลบ state ของผู้ใช้โดยไม่มี code review มาคอยจับ จึงใช้ gate เป็นตัวรีวิว: bucket เป็นคำแนะนำ ไม่ใช่สิทธิ์ และ worktree ที่มี uncommitted work (`wip:N`) จะหยุดถามก่อน ขั้น simulator ใช้ `xcrun simctl` ซึ่งใช้ได้เฉพาะเครื่องที่มี Xcode

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode ช่วยเก็บกวาด worktree และคืนพื้นที่ดิสก์`

</div>
