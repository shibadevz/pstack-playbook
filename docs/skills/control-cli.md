# /pstack:control-cli

<small>ประเภท: **Workflow skill** · สถานการณ์: `Verify/เทส` `เจอ bug`</small>

## ใช้ทำอะไร

สร้างหรือปรับ harness ในเครื่อง (tmux หรือ PTY script) เพื่อขับ ตรวจ และ profile CLI/TUI แบบ interactive โดยไม่ต้องใช้ service ภายนอก

## ใช้เมื่อ

เช่นเมื่อ bug อยู่ใน prompt flow ของ CLI ที่ต้องกด arrow key และ Ctrl-C หรืออยากวัด startup time

## ต่างจาก / ข้อควรรู้

ใช้ harness ที่ repo มีอยู่ก่อน ถ้าไม่มีค่อยประกอบจากเครื่องมือมาตรฐาน poteto-mode ใช้ skill นี้เป็น control skill ของ surface แบบ CLI/TUI ส่วน UI บน browser ใช้ control-ui

## วิธีเรียก

`/pstack:control-cli`

## ตัวอย่าง prompt

```text
/pstack:control-cli drive the interactive prompt flow of ./bin/mycli, save the transcript, and measure startup time.
```
