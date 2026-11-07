# Verify/เทส

ใช้เมื่อต้องพิสูจน์ว่างานใช้ได้จริงกับของจริง ไม่ใช่แค่ build ผ่าน

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:create-verification-skill**](/skills/create-verification-skill) — สร้าง verify skill ที่ขับ app จริงเหมือนผู้ใช้ เป็นของที่คุ้มที่สุดถ้า project ยังไม่มี.

   <PromptBlock compact text="/pstack:create-verification-skill ช่วยสร้าง verify skill สำหรับ web app ของ repo นี้ และพิสูจน์ว่าใช้งานได้จริงหนึ่งรอบก่อนส่งมอบ" />
2. [**/pstack:control-ui**](/skills/control-ui) — ขับและ screenshot UI บน browser, Electron หรือ web.

   <PromptBlock compact text="/pstack:control-ui เปิดหน้า settings ในเครื่อง repro focus bug ที่เกิดหลังกด Tab และถ่าย screenshot ก่อนกับหลังแก้" />
3. [**/pstack:control-cli**](/skills/control-cli) — ขับและบันทึก transcript ของ CLI/TUI.

   <PromptBlock compact text="/pstack:control-cli ช่วย drive interactive prompt flow ของ ./bin/mycli เก็บ transcript ไว้ และวัด startup time" />
4. [**/pstack:principle-prove-it-works**](/principles/prove-it-works) — สั่งให้ agent ตรวจกับ artifact จริงก่อนประกาศว่าเสร็จ.

   <PromptBlock compact text="/pstack:poteto-mode แก้ปุ่ม export apply prove it works ให้ดู output จริง ไม่ใช่ build log" />
5. [**/pstack:swarm**](/skills/swarm) — ตรวจหลายชิ้นขนานแล้วรับรายงานเดียวเป็น PASS, ISSUES หรือ BLOCKED.

   <PromptBlock compact text="/pstack:swarm ตรวจทุก package ใต้ packages/ ด้วย check script ของแต่ละตัว หนึ่ง worker ต่อหนึ่ง package แล้วรวมเป็น report เดียว" />

## ตัวอย่าง prompt รวม

<PromptBlock text="/pstack:poteto-mode แก้ปุ่ม export apply prove it works ให้ดู output จริงของ export ไม่ใช่ build log" />

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
