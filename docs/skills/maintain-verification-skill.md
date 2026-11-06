# /pstack:maintain-verification-skill

<small>ประเภท: **Workflow skill** · สถานการณ์: `Verify/เทส` `ปรับแต่ง PStack`</small>

## ใช้ทำอะไร

รอบดูแลที่ทำให้ verification skill และ feature map ตรงกับ app: source reader ขนานต่อ feature, หนึ่ง session ขับทุก feature และส่ง PR แก้ที่พิสูจน์แล้วไม่เกินหนึ่งอัน ผลเป็น clean, changed หรือ blocked

## ใช้เมื่อ

เช่นเมื่อ app เปลี่ยนไปหลาย release แล้วสงสัยว่า verify skill ที่สร้างไว้เริ่มล้าสมัย

## ต่างจาก / ข้อควรรู้

ต้องมี verification skill อยู่แล้ว (ปกติ `.claude/skills/verify-*/`) ถ้าไม่มีจะหยุดและชี้ไปที่ create-verification-skill ผลรันนี้แก้เฉพาะโฟลเดอร์ของ verification skill ไม่แก้ product code

## วิธีเรียก

`/pstack:maintain-verification-skill`

## ตัวอย่าง prompt

```text
/pstack:maintain-verification-skill audit the verify skill against the current app.
```
