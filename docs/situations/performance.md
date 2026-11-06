# Performance

ใช้เมื่อมีความช้าหรือตัวเลขที่ต้องวัด แก้ และเชื่อถือได้

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Perf issue**](/playbooks/perf-issue.md) — จับ baseline, ไล่ลองหลัก performance mantra, แก้ตามที่วัดได้ และอ้างตัวเลขใน PR. วิธีเรียก: พิมพ์ `/pstack:poteto-mode <operation> takes <time> on <fixture>. trace it, fix the measured cause.`
2. [**/pstack:benchmark-checklist**](/skills/benchmark-checklist.md) — ตรวจตัวเลขด้วยคำถาม 7 ข้อก่อนรายงาน เช่นเช็กว่า cache อุ่นอยู่หรือไม่. วิธีเรียก: พิมพ์ `/pstack:benchmark-checklist`
3. [**Playbook: Hillclimb**](/playbooks/hillclimb.md) — ถ้าต้องการปรับ metric ต่อเนื่องจนถึงเป้า ไม่ใช่แก้ครั้งเดียว. วิธีเรียก: พิมพ์ `/pstack:poteto-mode keep improving <metric> until it reaches <target>.`
4. [**Playbook: Runtime forensics**](/playbooks/runtime-forensics.md) — ถ้าต้องวินิจฉัย process ที่ยังรันอยู่ เช่น CPU spin หรือ leak. วิธีเรียก: พิมพ์ `/pstack:poteto-mode diagnose why the process spins at idle. profile the live process, no fix yet.`
5. [**Playbook: Trace forensics**](/playbooks/trace-forensics.md) — ถ้ามีไฟล์ trace หรือ profile ที่จับไว้แล้วและต้องการหาเส้นทางร้อน. วิธีเรียก: พิมพ์ `/pstack:poteto-mode diagnose this trace file. no fix yet.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode exporting the 60k-row fixture takes 40s. trace it, fix the measured cause, and show me before and after.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
