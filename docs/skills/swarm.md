# /pstack:swarm

<small>ประเภท: **Workflow skill** · สถานการณ์: `Verify/เทส` `Review` `ปล่อยรันเอง/ข้ามคืน`</small>

## ใช้ทำอะไร

กระจาย worker N ตัวที่แยกกัน (ตามชิ้นงาน, แข่ง brief เดียวกัน หรือผสม) รอให้ครบแล้วรวมเป็นรายงานเดียวที่ใช้ `PASS`, `ISSUES` หรือ `BLOCKED` พร้อมหลักฐาน

## ใช้เมื่อ

เช่นเมื่อต้องเช็กทุก package ใต้ `packages/` กับ script ตรวจของแต่ละอัน

## ต่างจาก / ข้อควรรู้

swarm แบ่งงานเป็น slice หรือแข่งแล้วรายงานเดียว ส่วน arena ให้ทุก worker ทำ brief เดียวกันแล้วรวมส่วนดี worker ที่เขียนไฟล์ต้องมี worktree หรือ output directory ของตัวเอง

## วิธีเรียก

`/pstack:swarm`

## ตัวอย่าง prompt

```text
/pstack:swarm check every package under packages/ against its check script. one worker per package. one report.
```
