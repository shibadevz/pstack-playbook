# Performance

ใช้เมื่อมีความช้าหรือตัวเลขที่ต้องวัด แก้ และเชื่อถือได้

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- [**Playbook: Perf issue**](/playbooks/perf-issue) — จับ baseline, ไล่ลองหลัก performance mantra, แก้ตามที่วัดได้ และอ้างตัวเลขใน PR

   <PromptBlock compact text="/pstack:poteto-mode export fixture 60k แถวใช้เวลา 40 วินาที ช่วย trace หา fix สาเหตุที่วัดได้ และให้ดูก่อนกับหลัง" />
- [**/pstack:benchmark-checklist**](/skills/benchmark-checklist) — ตรวจตัวเลขด้วยคำถาม 7 ข้อก่อนรายงาน เช่นเช็กว่า cache อุ่นอยู่หรือไม่

   <PromptBlock compact text="/pstack:benchmark-checklist ช่วยตรวจ speedup 40% นี้ให้ดีก่อนใส่ใน PR description" />
- [**Playbook: Hillclimb**](/playbooks/hillclimb) — ถ้าต้องการปรับ metric ต่อเนื่องจนถึงเป้า ไม่ใช่แก้ครั้งเดียว

   <PromptBlock compact text="/pstack:poteto-mode ช่วยปรับ cold start time ต่อไปจนต่ำกว่า 1.5 วินาทีบน benchmark fixture เก็บ decision log และทำหนึ่ง commit ต่อหนึ่งการปรับที่รับไว้" />
- [**Playbook: Runtime forensics**](/playbooks/runtime-forensics) — ถ้าต้องวินิจฉัย process ที่ยังรันอยู่ เช่น CPU spin หรือ leak

   <PromptBlock compact text="/pstack:poteto-mode desktop app ใช้ CPU 80% ตอน idle ช่วยจับ CPU profile จาก process ที่กำลังรันและวินิจฉัยสาเหตุ ยังไม่ต้อง fix" />
- [**Playbook: Trace forensics**](/playbooks/trace-forensics) — ถ้ามีไฟล์ trace หรือ profile ที่จับไว้แล้วและต้องการหาเส้นทางร้อน

   <PromptBlock compact text="/pstack:poteto-mode ช่วยวินิจฉัยว่าทำไม app ค้าง โดยใช้ startup.cpuprofile ที่แนบมา โหลดเข้า sqlite หา hot path และ map กลับไปที่ source ยังไม่ต้อง fix" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
