# /pstack:deslop

<small>ประเภท: **Workflow skill** · สถานการณ์: `PR & Ship` `Refactor/เก็บกวาด` `Review`</small>

## ใช้ทำอะไร

ลบ AI slop ที่เพิ่มใน branch เทียบกับ main เช่น comment เกินจำเป็น, defensive check ที่ผิดปกติ, การ cast เป็น `any` และ nesting ที่ลึกเกิน โดยรักษา behavior เดิม

## ใช้เมื่อ

เช่นเมื่อกำลังจะ commit แล้วเห็นว่า diff มี try/catch และ comment ที่ไม่ตรงกับสไตล์ของไฟล์

## ต่างจาก / ข้อควรรู้

bundled ใน port นี้ และ playbook Opening a PR ให้รันก่อน commit no-comments ใช้ reviewer แยกเพื่อตรวจ comment และ workaround ส่วน unslop ใช้กับข้อความ ไม่ใช่โค้ด

## วิธีเรียก

`/pstack:deslop`

## ตัวอย่าง prompt

```text
/pstack:deslop
```
