# Review

ใช้เมื่อ diff หรือ branch ใกล้เสร็จและอยากให้มีคนลองพังก่อนส่งต่อ

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:interrogate**](/skills/interrogate) — reviewer หลายตัวรีวิวแบบ adversarial แล้วสรุปเป็น act-on กับ dismissed โดยไม่แก้โค้ดเอง.

   <PromptBlock compact text="/pstack:interrogate ทั้ง branch แบบสงสัยไว้ก่อน ยังไม่ต้องแก้อะไร ไม่ต้องจุกจิกเว้นแต่เป็น bug หรือ regression จริง" />
2. [**/pstack:blast-radius**](/skills/blast-radius) — หาสิ่งที่พังนอก diff และพิสูจน์ fact เดียวที่ทำให้ปลอดภัย เหมาะกับ diff เล็กที่ไม่น่าไว้ใจ.

   <PromptBlock compact text="/pstack:blast-radius ของการลบ cache reset ใน src/session.ts พิสูจน์ข้อเท็จจริงข้อเดียวที่ทำให้มันปลอดภัยด้วยการรันโค้ดจริง ถ้าพิสูจน์ไม่ได้ให้ mark ว่า unproven" />
3. [**/pstack:no-comments**](/skills/no-comments) — ล้าง comment และ workaround ก่อนส่งรีวิว.

   <PromptBlock compact text="/pstack:no-comments review diff เทียบกับ main" />
4. [**/pstack:swarm**](/skills/swarm) — ตรวจหลาย package หรือหลาย slice ขนานแล้วรับรายงานเดียว.

   <PromptBlock compact text="/pstack:swarm ตรวจทุก package ใต้ packages/ ด้วย check script ของแต่ละตัว หนึ่ง worker ต่อหนึ่ง package แล้วรวมเป็น report เดียว" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
