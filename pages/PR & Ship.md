# PR & Ship

ใช้เมื่อโค้ดเสร็จและต้องเปิด PR ดูให้เขียว และ land หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. **Playbook: Opening a PR** — ขั้นตอนมาตรฐานของ commit เล็กเรียงลำดับ และ PR description ที่อ่านจบในหนึ่งนาที. วิธีเรียก: พิมพ์ `/pstack:poteto-mode open the pr.`
2. **Playbook: Babysit** — ขับ PR หรือ stack ไปจน merge-ready: เคลียร์ conflict, review thread แล้ว CI และไม่ merge เอง. วิธีเรียก: พิมพ์ `/pstack:poteto-mode babysit this pr. get it green.`
3. **Playbook: Shipping** — land เฉพาะช่วง PR ที่ verified แล้วต่อเนื่องจากล่างสุด ใช้เมื่อสั่งให้ land หรือ ship. วิธีเรียก: พิมพ์ `/pstack:poteto-mode land the stack.`
4. **/pstack:technical-writing** — ใช้เขียน PR title, description และ commit body. วิธีเรียก: พิมพ์ `/pstack:technical-writing`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode เปิด PR commit เล็กๆ เรียงลำดับ ใส่หลักฐานใน description
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
