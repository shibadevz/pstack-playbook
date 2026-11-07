# ปรับแต่ง PStack

ใช้เมื่ออยากให้ PStack เข้ากับวิธีทำงานของตัวเองหรือทีม หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- **/pstack:setup-pstack** — เปลี่ยน model ต่อ role และ reasoning budget ที่ใช้ มีผลตั้งแต่ dispatch ถัดไป. วิธีเรียก: พิมพ์ `/pstack:setup-pstack`
- **/pstack:automate-me** — สร้าง personal `-mode` skill จากนิสัยการทำงานของตัวเอง. วิธีเรียก: พิมพ์ `/pstack:automate-me`
- **/pstack:reflect** — หลังจบงาน เปลี่ยนบทเรียนเป็นการแก้ skill ที่มีอยู่ซึ่งคุณอนุมัติ. วิธีเรียก: พิมพ์ `/pstack:reflect`
- **/pstack:correct** — แก้ที่ repo ไม่ให้ agent ทำผิดแบบเดิมซ้ำ. วิธีเรียก: พิมพ์ `/pstack:correct`
- **Playbook: Authoring or modifying a skill** — เขียนหรือแก้ SKILL.md ผ่าน playbook เพื่อให้มี validate และรีวิว. วิธีเรียก: พิมพ์ `/pstack:poteto-mode write a skill for <workflow>.`

## ตัวอย่าง prompt

```text
/pstack:reflect ช่วยจดสิ่งที่เราเรียนรู้ไว้ เพื่อให้รอบหน้าไม่พลาดซ้ำ
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
