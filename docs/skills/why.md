# /pstack:why

<small>ประเภท: **Workflow skill** · สถานการณ์: `เข้าใจโค้ด` `เจอ bug`</small>

## ใช้ทำอะไร

สืบเหตุผลและเจตนาเบื้องหลังโค้ด: ค้นหลายแหล่งขนาน (source control, issue tracker, docs, chat, observability ฯลฯ ตาม MCP ที่มี) แล้วสรุปพร้อมอ้างอิงและบอกระดับความมั่นใจ

## ใช้เมื่อ

เช่นเมื่อสงสัยว่าทำไม threshold ถึงเป็น 30 วินาที หรือทำไมโค้ดส่วนนี้เพิ่งพังหลัง release ล่าสุด

## ต่างจาก / ข้อควรรู้

why ตอบว่าทำไม ส่วน how ตอบว่าทำงานอย่างไร ความครอบคลุมของคำตอบขึ้นกับ MCP ที่ติดตั้ง และรายงานจะบอกว่าค้นแหล่งไหนบ้าง

## วิธีเรียก

`/pstack:why`

## ตัวอย่าง prompt

```text
/pstack:why does the export retry use a 30 second timeout? check the history and any incidents.
```
