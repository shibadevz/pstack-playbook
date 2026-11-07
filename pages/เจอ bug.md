# เจอ bug

ใช้เมื่อมี defect ที่รายงานมาและต้องการ repro, หา root cause และ fix ด้วยหลักฐาน หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. **Playbook: Bug fix** — ค่าเริ่มต้นสำหรับ bug: repro เอง, ไล่หา cause, fix และตรวจบน surface เดิม ให้ failing repro อยู่ก่อน fix ใน git history. วิธีเรียก: พิมพ์ `/pstack:poteto-mode <symptom>. repro first, then fix and verify.`
2. **/pstack:tdd** — ถ้า bug มี test path ในเครื่องที่ถูกและชัด ให้เขียน test ที่ fail ก่อนแก้ ถ้าไม่ชัดให้ข้าม. วิธีเรียก: พิมพ์ `/pstack:tdd`
3. **/pstack:why** — ถ้า bug เพิ่งเกิดหลัง release ให้ดูประวัติการเปลี่ยนที่เกี่ยวข้อง. วิธีเรียก: พิมพ์ `/pstack:why`
4. **/pstack:control-ui** — ใช้ repro bug ที่ต้องมี browser, focus หรือ rendering จริง (ส่วน CLI ใช้ control-cli). วิธีเรียก: พิมพ์ `/pstack:control-ui`
5. **/pstack:principle-fix-root-causes** — กัน agent จากการใส่ null check ที่ปิดเสียง crash โดยไม่แก้ต้นเหตุ. วิธีเรียก: สั่งด้วยชื่อใน poteto-mode เช่น "apply fix root causes" หรือพิมพ์ `/pstack:principle-fix-root-causes`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode ตอน retry แล้ว export สร้างแถวซ้ำ ช่วย repro ก่อน ถ้ามีทางเขียน test ที่ถูกให้ /pstack:tdd แล้วค่อย fix และ rerun
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
