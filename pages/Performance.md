# Performance

ใช้เมื่อมีความช้าหรือตัวเลขที่ต้องวัด แก้ และเชื่อถือได้ หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- **Playbook: Perf issue** — จับ baseline, ไล่ลองหลัก performance mantra, แก้ตามที่วัดได้ และอ้างตัวเลขใน PR. วิธีเรียก: พิมพ์ `/pstack:poteto-mode <operation> takes <time> on <fixture>. trace it, fix the measured cause.`
- **/pstack:benchmark-checklist** — ตรวจตัวเลขด้วยคำถาม 7 ข้อก่อนรายงาน เช่นเช็กว่า cache อุ่นอยู่หรือไม่. วิธีเรียก: พิมพ์ `/pstack:benchmark-checklist`
- **Playbook: Hillclimb** — ถ้าต้องการปรับ metric ต่อเนื่องจนถึงเป้า ไม่ใช่แก้ครั้งเดียว. วิธีเรียก: พิมพ์ `/pstack:poteto-mode keep improving <metric> until it reaches <target>.`
- **Playbook: Runtime forensics** — ถ้าต้องวินิจฉัย process ที่ยังรันอยู่ เช่น CPU spin หรือ leak. วิธีเรียก: พิมพ์ `/pstack:poteto-mode diagnose why the process spins at idle. profile the live process, no fix yet.`
- **Playbook: Trace forensics** — ถ้ามีไฟล์ trace หรือ profile ที่จับไว้แล้วและต้องการหาเส้นทางร้อน. วิธีเรียก: พิมพ์ `/pstack:poteto-mode diagnose this trace file. no fix yet.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode export fixture 60k แถวใช้เวลา 40 วินาที ช่วย trace หา fix สาเหตุที่วัดได้ และให้ดูก่อนกับหลัง
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
