# /pstack:principle-explain-the-number

<small>ประเภท: **Principle** · สถานการณ์: `Performance` `Verify/เทส`</small>

## ใช้ทำอะไร

ก่อนเชื่อ รายงาน หรือลงมือตามตัวเลขที่วัดมา (speedup, regression, throughput, latency, eval result) ให้หาสิ่งที่จำกัดตัวเลข และตัดความเป็นไปได้ว่าวัดสิ่งอื่นที่ไม่ใช่งานจริง

## ใช้เมื่อ

เช่นเมื่อได้ผล "เร็วขึ้น 2 เท่า" แต่ยังตอบไม่ได้ว่าทำไมไม่ใช่ 4 เท่า

## ต่างจาก / ข้อควรรู้

ต่างจาก prove-it-works ที่เช็กว่า output จริงหรือไม่ ส่วนนี้เช็กว่าตัวเลขวัดอะไรอยู่ ถ้าเป็นตัวเลข perf ให้รันขั้นตอนเต็มด้วย benchmark-checklist

## วิธีเรียก

`ส่วนใหญ่สั่งด้วยชื่อใน poteto-mode เช่น "apply explain the number" หรือโหลดตรงด้วย /pstack:principle-explain-the-number`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode the new parser benchmark shows 2x. apply explain the number before we put it in the PR.
```
