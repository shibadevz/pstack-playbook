# Playbook: Autonomous run

<small>ประเภท: **Playbook** · สถานการณ์: `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

ขับงานยาวงานเดียวจนถึงเงื่อนไขที่ตรวจได้โดยไม่หยุด: ตั้ง predicate, เลือกกลไกปลุก (scheduler หรือ watcher), ทำการเปลี่ยนเล็กที่สุดต่อ iteration และ checkpoint ลง log

## ใช้เมื่อ

เช่นเมื่อจะนอนและอยากให้ agent ทำต่อจน fixture ทุกอันผ่าน

## ต่างจาก / ข้อควรรู้

ต่างจาก Orchestrate ที่เป็น program หลายวันหลาย PR plateau ไม่ใช่เหตุให้หยุด ให้เปลี่ยนวิธี และห้ามผ่อน predicate เพื่อประกาศชนะ ต้องมี check ที่ผ่านหรือไม่ผ่านได้ ไม่ใช่ระยะเวลา และกลไกปลุกอาจรายงาน capability gap ตาม runtime contract

## วิธีเรียก

`/pstack:poteto-mode im going to bed. <goal>. done means <checks>.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode im going to bed. migrate every caller to the new parser in a fresh worktree off main. done means zero old callers, all parser fixtures pass, old api deleted. keep a decision log. don't ask me before committing.
```
