# /pstack:principle-build-the-lever

<small>ประเภท: **Principle** · สถานการณ์: `Refactor/เก็บกวาด` `สร้างฟีเจอร์`</small>

## ใช้ทำอะไร

กับงาน non-trivial ทุกชนิด ให้สร้างเครื่องมือที่ทำหรือพิสูจน์งาน (codemod, script, generator หรือ skill ที่ subagent ทำตาม) แทนการทำมือ เครื่องมือคือ artifact ที่ผู้รีวิวรันซ้ำได้

## ใช้เมื่อ

เช่นเมื่อต้องเปลี่ยนชื่อ API ใน 200 ไฟล์ และควรเขียน codemod แทนแก้ทีละไฟล์

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply build the lever" หรือโหลดตรงด้วย /pstack:principle-build-the-lever`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode rename getUser to fetchUser across the repo. apply build the lever. give me a codemod I can rerun.
```
