# /pstack:control-ui

<small>ประเภท: **Workflow skill** · สถานการณ์: `Verify/เทส` `เจอ bug`</small>

## ใช้ทำอะไร

สร้างหรือปรับ harness แบบ browser/CDP ในเครื่องเพื่อขับและตรวจ UI ของ web, IDE หรือ Electron พร้อม screenshot, accessibility snapshot, profile และ visual diff

## ใช้เมื่อ

เช่นเมื่อ bug เกิดเฉพาะตอน focus หรือ keyboard จริงใน browser และต้องการ screenshot ก่อนและหลังแก้

## ต่างจาก / ข้อควรรู้

ใช้ harness ที่ repo มีอยู่ก่อน (Playwright, Cypress, Electron script) poteto-mode ใช้ skill นี้เป็น control skill ของ surface แบบ browser/Electron/web ส่วน CLI/TUI ใช้ control-cli

## วิธีเรียก

`/pstack:control-ui`

## ตัวอย่าง prompt

```text
/pstack:control-ui open the settings page locally, reproduce the focus bug after pressing Tab, and take before and after screenshots.
```
