# ปรับแต่ง PStack

ใช้เมื่ออยากให้ PStack เข้ากับวิธีทำงานของตัวเองหรือทีม

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:setup-pstack**](/skills/setup-pstack.md) — เปลี่ยน model ต่อ role และ reasoning budget ที่ใช้ มีผลตั้งแต่ dispatch ถัดไป. วิธีเรียก: พิมพ์ `/pstack:setup-pstack`
2. [**/pstack:automate-me**](/skills/automate-me.md) — สร้าง personal `-mode` skill จากนิสัยการทำงานของตัวเอง. วิธีเรียก: พิมพ์ `/pstack:automate-me`
3. [**/pstack:reflect**](/skills/reflect.md) — หลังจบงาน เปลี่ยนบทเรียนเป็นการแก้ skill ที่มีอยู่ซึ่งคุณอนุมัติ. วิธีเรียก: พิมพ์ `/pstack:reflect`
4. [**/pstack:correct**](/skills/correct.md) — แก้ที่ repo ไม่ให้ agent ทำผิดแบบเดิมซ้ำ. วิธีเรียก: พิมพ์ `/pstack:correct`
5. [**Playbook: Authoring or modifying a skill**](/playbooks/authoring-or-modifying-a-skill.md) — เขียนหรือแก้ SKILL.md ผ่าน playbook เพื่อให้มี validate และรีวิว. วิธีเรียก: พิมพ์ `/pstack:poteto-mode write a skill for <workflow>.`

## ตัวอย่าง prompt

```text
/pstack:reflect capture what we learned so the next run doesn't repeat it.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
