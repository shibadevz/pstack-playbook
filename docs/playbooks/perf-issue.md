# Playbook: Perf issue

<small>ประเภท: **Playbook** · สถานการณ์: `Performance`</small>

## ใช้ทำอะไร

แก้ความช้าที่วัดได้: จับ baseline trace, ตรวจ baseline ด้วย benchmark-checklist, ไล่ลองหลัก performance mantra เรียงจากถูกสุด, วัดหลังแก้ แล้วอ้างตัวเลขใน PR

## ใช้เมื่อ

เช่นเมื่อ export ไฟล์ 60k แถวใช้เวลา 40 วินาทีและอยากรู้ว่าเวลาหายไปที่ไหน

## ต่างจาก / ข้อควรรู้

ใช้สำหรับการแก้ครั้งเดียว ถ้าต้องการปรับปรุง metric ต่อเนื่องจนถึงเป้า ให้ใช้ Hillclimb

## วิธีเรียก

`/pstack:poteto-mode <operation> takes <time> on <fixture>. trace it, fix the measured cause.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode exporting the 60k-row fixture takes 40s. trace it, fix the measured cause, and show me before and after.
```
