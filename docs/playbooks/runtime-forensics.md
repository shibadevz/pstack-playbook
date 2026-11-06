# Playbook: Runtime forensics

<small>ประเภท: **Playbook** · สถานการณ์: `เจอ bug` `Performance`</small>

## ใช้ทำอะไร

วินิจฉัยอาการตอนรัน (leak, idle-CPU spin, glitch) จาก instrumentation ของ process จริง ผลคือคำวินิจฉัยที่อ้างอิงได้ ไม่ใช่ fix

## ใช้เมื่อ

เช่นเมื่อ process กิน CPU ตอนไม่มีใครใช้ และอยากรู้ว่า function ไหนวนอยู่

## ต่างจาก / ข้อควรรู้

ต่างจาก Trace forensics ที่ artifact จับไว้แล้ว (ที่นี่จับสัญญาณจาก process ที่ยังรันอยู่) เมื่อรู้สาเหตุแล้วให้ส่งต่อไป Bug fix หรือ Perf issue

## วิธีเรียก

`/pstack:poteto-mode diagnose why the process spins at idle. profile the live process, no fix yet.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode the desktop app uses 80% CPU while idle. capture a CPU profile from the running process and diagnose the cause. no fix yet.
```
