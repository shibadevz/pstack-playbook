# /pstack:automate-me

<small>ประเภท: **Workflow skill** · สถานการณ์: `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

ร่างหรืออัปเดต personal `-mode` skill จากนิสัยการทำงานของผู้ใช้ โดยขุดประวัติแชตล่าสุด ถามเพิ่ม แล้วเขียนผ่าน pstack-create-skill และ unslop

## ใช้เมื่อ

เช่นเมื่อต้องพิมพ์ "ใช้ worktree แยก PR เล็ก" ซ้ำทุกแชตและอยากให้ agent ทำตามเองโดยไม่ต้องบอก

## ต่างจาก / ข้อควรรู้

reflect เปลี่ยนบทเรียนของงานหนึ่งงานเป็นการแก้ skill ที่มีอยู่ ส่วน automate-me สร้าง skill ส่วนตัวจากนิสัยโดยรวม การขุดประวัติอ่านเฉพาะ transcript ของ workspace ปัจจุบัน

## วิธีเรียก

`/pstack:automate-me`

## ตัวอย่าง prompt

```text
/pstack:automate-me update my mode skill from the last 3 weeks of chats in this workspace.
```
