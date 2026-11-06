# /pstack:pstack-create-skill

<small>ประเภท: **Workflow skill** · สถานการณ์: `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

เขียน project skill ที่ `.claude/skills/<name>/SKILL.md` พร้อม frontmatter (`name`, `description`), ลำดับขั้น, กรณี error และเงื่อนไขเสร็จที่ตรวจได้ แล้วลองเรียกใช้จริงกับงานเล็กหนึ่งครั้ง

## ใช้เมื่อ

เช่นเมื่อมี workflow ที่ทำซ้ำบ่อย เช่น release checklist และอยากให้เป็น skill

## ต่างจาก / ข้อควรรู้

เป็นตัวแทน skill authoring แบบ native ใน port นี้ playbook Authoring or modifying a skill เรียกใช้ตัวนี้ จึงควรเขียน SKILL.md ผ่าน playbook ไม่ใช่เขียนเอง

## วิธีเรียก

`/pstack:pstack-create-skill`

## ตัวอย่าง prompt

```text
/pstack:pstack-create-skill create a project skill that runs our release checklist and ends with a check that can pass or fail.
```
