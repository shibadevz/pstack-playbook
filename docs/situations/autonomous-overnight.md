# ปล่อยรันเอง/ข้ามคืน

ใช้เมื่อจะเดินไปไหนแล้วให้ agent ทำต่อเองจนเสร็จ และกลับมาตรวจทีหลัง

## เลือกใช้ตามสถานการณ์

ไม่ต้องใช้ครบทุกตัว เลือกตัวที่ตรงกับงานตอนนั้น ถ้าไม่แน่ใจให้เริ่มจากตัวแรก

- [**Playbook: Autonomous run**](/playbooks/autonomous-run) — ตั้ง done เป็น check ที่ผ่านหรือไม่ผ่านได้ แล้วขับจนถึงเงื่อนไขนั้นโดยไม่หยุด

   <PromptBlock compact text="/pstack:poteto-mode ฉันจะไปนอนแล้ว migrate ทุก caller ไปใช้ parser ใหม่ ใน worktree ใหม่ที่แตกจาก main done คือไม่เหลือ caller เก่า parser fixture ผ่านทั้งหมด และ API เก่าถูกลบ เก็บ decision log ไม่ต้องถามก่อน commit" />
- [**/pstack:show-me-your-work**](/skills/show-me-your-work) — เก็บ decision log เป็น TSV ให้ตรวจตอนเช้า เริ่มจากหัวข้อ Attention ท้าย reply

   <PromptBlock compact text="/pstack:show-me-your-work ช่วยตามให้ทันว่าเมื่อคืนคุณทำอะไรไปบ้าง" />
- [**/pstack:ketchup**](/skills/ketchup) — กลับมาแล้วอยากรู้สั้นๆ ว่าอะไรเปลี่ยนและอะไรรอให้ตัดสินใจ

   <PromptBlock compact text="/pstack:ketchup ช่วยตามให้ทันว่าในแชตนี้มีอะไรเปลี่ยนไปบ้าง" />
- [**Playbook: Pause safely**](/playbooks/pause-safely) — ต้องหยุดชั่วคราว (offline หรือ context ใกล้ compact) โดยให้งานต่อได้

   <PromptBlock compact text="/pstack:poteto-mode pause safely commit สิ่งที่มีเป็น wip commit และเขียน resume note" />
- [**Playbook: Session pickup**](/playbooks/session-pickup) — รับช่วงงานที่ agent อีกแชตทำค้างไว้จาก transcript หรือ branch

   <PromptBlock compact text="/pstack:poteto-mode take over this branch อ่าน decision log หาว่าอะไรเสร็จแล้ว และทำต่อ อย่าทำงานที่เสร็จแล้วซ้ำ" />

## ตัวอย่าง prompt รวม

<PromptBlock text="/pstack:poteto-mode ฉันจะไปนอนแล้ว migrate ทุก caller ไปใช้ parser ใหม่ ใน worktree ใหม่ที่แตกจาก main done คือไม่เหลือ caller เก่า parser fixture ผ่านทั้งหมด และ API เก่าถูกลบ เก็บ decision log ไม่ต้องถามก่อน commit ถ้าติดจริงๆ หลังผ่านไปหลายชั่วโมง ให้หยุดแล้วเขียนสรุปว่าทำไม" />

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
