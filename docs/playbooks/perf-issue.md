---
pageClass: entity-page entity-playbooks
outline: false
title: "Playbook: Perf issue"
---

# Perf issue

<EntityMeta type="playbooks" label="Playbook" :sits="[{&quot;title&quot;: &quot;Performance&quot;, &quot;link&quot;: &quot;/situations/performance&quot;}]" />

<p class="typeline"><span class="typeline-label">พิมพ์</span><code>/pstack:poteto-mode &lt;operation&gt; ใช้เวลา &lt;เวลา&gt; บน &lt;fixture&gt; ช่วย trace แล้ว fix ที่สาเหตุซึ่งวัดได้</code></p>

<PromptBlock text="/pstack:poteto-mode export fixture 60k แถวใช้เวลา 40 วินาที ช่วย trace หา fix สาเหตุที่วัดได้ และให้ดูก่อนกับหลัง" />

<div class="spec-row">

## ใช้ทำอะไร

แก้ความช้าที่วัดได้: จับ baseline trace, ตรวจ baseline ด้วย benchmark-checklist, ไล่ลองหลัก performance mantra เรียงจากถูกสุด, วัดหลังแก้ แล้วอ้างตัวเลขใน PR

</div>

<div class="spec-row">

## ใช้เมื่อ

เช่นเมื่อ export ไฟล์ 60k แถวใช้เวลา 40 วินาทีและอยากรู้ว่าเวลาหายไปที่ไหน

</div>

<div class="spec-row">

## ต่างจาก / ข้อควรรู้

ใช้สำหรับการแก้ครั้งเดียว ถ้าต้องการปรับปรุง metric ต่อเนื่องจนถึงเป้า ให้ใช้ Hillclimb

</div>

<div class="spec-row">

## วิธีเรียก

`/pstack:poteto-mode <operation> ใช้เวลา <เวลา> บน <fixture> ช่วย trace แล้ว fix ที่สาเหตุซึ่งวัดได้`

</div>
