# /pstack:make-bot-ui

<small>ประเภท: **Workflow skill** · สถานการณ์: `สร้างฟีเจอร์`</small>

## ใช้ทำอะไร

สร้างหน้า UI (page, dashboard, ปุ่ม) ที่เมื่อกดแล้ว server ในเครื่อง POST JSON ไปปลุก Grok Bot ผ่าน webhook โดยเก็บ sender key ไว้ฝั่ง server เท่านั้น

## ใช้เมื่อ

เช่นเมื่ออยากทำหน้าที่มีปุ่ม "Run report" ซึ่งกดแล้วสั่งบอทให้ทำงาน

## ต่างจาก / ข้อควรรู้

ต้องมี bot runner ที่รองรับ webhook ที่ตั้งค่าไว้แล้ว ตัว skill อ้างอิง routine API ของ Cursor (`update_state` และอื่นๆ) ซึ่งใช้ได้เมื่อมีของเทียบเท่าที่ใช้งานได้จริงเท่านั้น ถ้าไม่มีให้หยุดที่ร่างและรายงานว่าขาดอะไร

## วิธีเรียก

`/pstack:make-bot-ui`

## ตัวอย่าง prompt

```text
/pstack:make-bot-ui build a page with a Run report button that wakes my bot over a webhook. draft only if no webhook-capable bot runner is configured.
```
