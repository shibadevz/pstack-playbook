# PR & Ship

ใช้เมื่อโค้ดเสร็จและต้องเปิด PR ดูให้เขียว และ land

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Opening a PR**](/playbooks/opening-a-pr.md) — ขั้นตอนมาตรฐานของ commit เล็กเรียงลำดับ และ PR description ที่อ่านจบในหนึ่งนาที. วิธีเรียก: พิมพ์ `/pstack:poteto-mode open the pr.`
2. [**Playbook: Babysit**](/playbooks/babysit.md) — ขับ PR หรือ stack ไปจน merge-ready: เคลียร์ conflict, review thread แล้ว CI และไม่ merge เอง. วิธีเรียก: พิมพ์ `/pstack:poteto-mode babysit this pr. get it green.`
3. [**Playbook: Shipping**](/playbooks/shipping.md) — land เฉพาะช่วง PR ที่ verified แล้วต่อเนื่องจากล่างสุด ใช้เมื่อสั่งให้ land หรือ ship. วิธีเรียก: พิมพ์ `/pstack:poteto-mode land the stack.`
4. [**/pstack:technical-writing**](/skills/technical-writing.md) — ใช้เขียน PR title, description และ commit body. วิธีเรียก: พิมพ์ `/pstack:technical-writing`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode open the pr. small ordered commits, evidence in the description.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
