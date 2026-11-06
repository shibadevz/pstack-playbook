# Verify/เทส

ใช้เมื่อต้องพิสูจน์ว่างานใช้ได้จริงกับของจริง ไม่ใช่แค่ build ผ่าน หน้านี้อ่านได้โดยไม่ต้องใช้ database

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. **/pstack:create-verification-skill** — สร้าง verify skill ที่ขับ app จริงเหมือนผู้ใช้ เป็นของที่คุ้มที่สุดถ้า project ยังไม่มี. วิธีเรียก: พิมพ์ `/pstack:create-verification-skill`
2. **/pstack:control-ui** — ขับและ screenshot UI บน browser, Electron หรือ web. วิธีเรียก: พิมพ์ `/pstack:control-ui`
3. **/pstack:control-cli** — ขับและบันทึก transcript ของ CLI/TUI. วิธีเรียก: พิมพ์ `/pstack:control-cli`
4. **/pstack:principle-prove-it-works** — สั่งให้ agent ตรวจกับ artifact จริงก่อนประกาศว่าเสร็จ. วิธีเรียก: สั่งด้วยชื่อใน poteto-mode เช่น "apply prove it works" หรือพิมพ์ `/pstack:principle-prove-it-works`
5. **/pstack:swarm** — ตรวจหลายชิ้นขนานแล้วรับรายงานเดียวเป็น PASS, ISSUES หรือ BLOCKED. วิธีเรียก: พิมพ์ `/pstack:swarm`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode fix the export button. apply prove it works. show me the real output of the export, not the build log.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
