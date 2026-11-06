# /pstack:setup-pstack

<small>ประเภท: **Workflow skill** · สถานการณ์: `เริ่มงาน/ตั้งค่า` `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

ตั้งค่าว่า pstack ใช้ model ไหนในแต่ละ role (17 role) และ reasoning budget ระดับไหน โดยตรวจ model ที่ launch ได้จริงแล้วเขียน `.pstack/claude/models.json`

## ใช้เมื่อ

เช่นเมื่อติดตั้ง plugin เสร็จ หรือเมื่อค่าใช้จ่ายสูงเกินคาดและอยากลด budget

## ต่างจาก / ข้อควรรู้

เป็น skill เดียวที่โหลดจากคำพูดของผู้ใช้ได้เอง ถ้าไม่เคยรันทุก role จะ inherit model ของ session `auto` และ `inherit-parent` ไม่ใช่ slug ของ model แต่แปลว่าไม่ส่ง field model ให้ subagent ไฟล์ project (`.pstack/claude/models.json`) ถูกอ่านก่อนไฟล์ผู้ใช้ (`~/.config/pstack/claude/models.json`) และไม่ต้องเปิดแชตใหม่หลังแก้

## วิธีเรียก

`/pstack:setup-pstack`

## ตัวอย่าง prompt

```text
/pstack:setup-pstack
```
