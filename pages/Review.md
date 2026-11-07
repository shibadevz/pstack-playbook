# Review

ใช้เมื่อ diff หรือ branch ใกล้เสร็จและอยากให้มีคนลองพังก่อนส่งต่อ หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. **/pstack:interrogate** — reviewer หลายตัวรีวิวแบบ adversarial แล้วสรุปเป็น act-on กับ dismissed โดยไม่แก้โค้ดเอง. วิธีเรียก: พิมพ์ `/pstack:interrogate`
2. **/pstack:blast-radius** — หาสิ่งที่พังนอก diff และพิสูจน์ fact เดียวที่ทำให้ปลอดภัย เหมาะกับ diff เล็กที่ไม่น่าไว้ใจ. วิธีเรียก: พิมพ์ `/pstack:blast-radius`
3. **/pstack:no-comments** — ล้าง comment และ workaround ก่อนส่งรีวิว. วิธีเรียก: พิมพ์ `/pstack:no-comments`
4. **/pstack:swarm** — ตรวจหลาย package หรือหลาย slice ขนานแล้วรับรายงานเดียว. วิธีเรียก: พิมพ์ `/pstack:swarm`

## ตัวอย่าง prompt

```text
/pstack:interrogate ทั้ง branch แบบสงสัยไว้ก่อน ยังไม่ต้องแก้อะไร ไม่ต้องจุกจิกเว้นแต่เป็น bug หรือ regression จริง
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
