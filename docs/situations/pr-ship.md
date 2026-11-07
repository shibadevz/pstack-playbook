# PR & Ship

ใช้เมื่อโค้ดเสร็จและต้องเปิด PR ดูให้เขียว และ land

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Opening a PR**](/playbooks/opening-a-pr) — ขั้นตอนมาตรฐานของ commit เล็กเรียงลำดับ และ PR description ที่อ่านจบในหนึ่งนาที.

   <PromptBlock compact text="/pstack:poteto-mode เปิด PR commit เล็กๆ เรียงลำดับ ใส่หลักฐานใน description" />
2. [**Playbook: Babysit**](/playbooks/babysit) — ขับ PR หรือ stack ไปจน merge-ready: เคลียร์ conflict, review thread แล้ว CI และไม่ merge เอง.

   <PromptBlock compact text="/pstack:poteto-mode babysit this pr ให้ CI เขียว" />
3. [**Playbook: Shipping**](/playbooks/shipping) — land เฉพาะช่วง PR ที่ verified แล้วต่อเนื่องจากล่างสุด ใช้เมื่อสั่งให้ land หรือ ship.

   <PromptBlock compact text="/pstack:poteto-mode ช่วย land the stack ให้หน่อย" />
4. [**/pstack:technical-writing**](/skills/technical-writing) — ใช้เขียน PR title, description และ commit body.

   <PromptBlock compact text="/pstack:technical-writing เขียน PR description สำหรับ branch นี้ ให้มี why, what changed, scope, blast radius และ verification" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
