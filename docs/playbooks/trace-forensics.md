# Playbook: Trace forensics

<small>ประเภท: **Playbook** · สถานการณ์: `เจอ bug` `Performance`</small>

## ใช้ทำอะไร

วินิจฉัยจาก artifact ที่จับมาแล้ว (cpuprofile, trace, spindump, heap snapshot) โดย dump ลง sqlite เพื่อ query หาเส้นทางร้อนหรือ retainer chain แล้วอ้างถึง source

## ใช้เมื่อ

เช่นเมื่อมีคนส่งไฟล์ .cpuprofile มาให้ว่าแอปค้าง และไม่มี process ให้ไปจับเพิ่ม

## ต่างจาก / ข้อควรรู้

ต่างจาก Runtime forensics ตรงที่ artifact เป็นชุดข้อมูลคงที่ ให้อ่านไม่ใช่รันซ้ำ ถ้าไม่มีคู่ before/after จะรายงานเป็นสมมติฐานที่แข็งที่สุด ไม่ใช่สาเหตุที่ยืนยันแล้ว

## วิธีเรียก

`/pstack:poteto-mode diagnose this trace file. no fix yet.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode diagnose why the app hangs, using the attached startup.cpuprofile. load it into sqlite, find the hot path, and map it to source. no fix yet.
```
