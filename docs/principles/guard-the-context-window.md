# /pstack:principle-guard-the-context-window

<small>ประเภท: **Principle** · สถานการณ์: `เข้าใจโค้ด` `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

เมื่อ context กำลังเต็ม (output ใหญ่ ไฟล์ยาว อ่านซ้ำ วางแผน fan-out) ให้ส่งงานก้อนใหญ่ให้ subagent และเก็บแค่สรุปใน main thread ไม่ใช่ payload ดิบ

## ใช้เมื่อ

เช่นเมื่อต้องอ่าน trace ขนาด 50 MB และไม่อยากให้ main thread เต็มด้วย dump

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply guard the context window" หรือโหลดตรงด้วย /pstack:principle-guard-the-context-window`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode go through these 40 crash logs. apply guard the context window. subagents read the logs, you keep only the summary.
```
