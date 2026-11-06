# Playbook: Prototype

<small>ประเภท: **Playbook** · สถานการณ์: `ออกแบบ/วางแผน`</small>

## ใช้ทำอะไร

ร่างต้นแบบทิ้งขว้างเพื่อตัดสินใจ design หรือ behavior อย่างถูก: สร้างใน scratch dir แยก, เทียบหลายแบบหลัง switcher เดียว, ถ่าย screenshot แล้วสรุปตัวเลือก tradeoff และคำแนะนำ

## ใช้เมื่อ

เช่นเมื่อต้องเลือก layout ของหน้า settings และอยากเลือกจากสิ่งที่รันได้ ไม่ใช่คำบรรยาย

## ต่างจาก / ข้อควรรู้

ผลคือการตัดสินใจกับ artifact ทิ้งขว้าง ไม่ใช่โค้ดที่ ship ได้ การสร้างจริงตามหลังด้วย Feature ถ้าไม่มี decision ให้ตัดสินใจก็ไม่ต้อง prototype

## วิธีเรียก

`/pstack:poteto-mode prototype a few options for <feature>.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.
```
