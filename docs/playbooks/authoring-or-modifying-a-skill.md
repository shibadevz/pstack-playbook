# Playbook: Authoring or modifying a skill

<small>ประเภท: **Playbook** · สถานการณ์: `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

เขียนหรือแก้ SKILL.md ผ่าน pstack-create-skill, validate frontmatter และ link อ้างอิง, ทำ test ถ้าเป็นโครงสร้าง และเปิด PR

## ใช้เมื่อ

เช่นเมื่ออยากเพิ่ม skill สำหรับ release checklist หรือแก้ skill ที่ agent ตีความผิด

## ต่างจาก / ข้อควรรู้

อย่าเขียน SKILL.md เองโดยไม่ผ่าน playbook และแก้ skill ที่มีปัญหาใน PR ของมันเอง ไม่ใช่ปนไปกับงาน feature ที่เจอปัญหา

## วิธีเรียก

`/pstack:poteto-mode write a skill for <workflow>.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode write a skill for our release checklist. validate the frontmatter and links, then open a PR.
```
