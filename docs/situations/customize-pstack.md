# ปรับแต่ง PStack

ใช้เมื่ออยากให้ PStack เข้ากับวิธีทำงานของตัวเองหรือทีม

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:setup-pstack**](/skills/setup-pstack) — เปลี่ยน model ต่อ role และ reasoning budget ที่ใช้ มีผลตั้งแต่ dispatch ถัดไป.

   <PromptBlock compact text="/pstack:setup-pstack ช่วยตั้งค่า model และ reasoning budget ของ pstack" />
2. [**/pstack:automate-me**](/skills/automate-me) — สร้าง personal `-mode` skill จากนิสัยการทำงานของตัวเอง.

   <PromptBlock compact text="/pstack:automate-me ช่วยอัปเดต mode skill ของฉันจากแชต 3 สัปดาห์ล่าสุดใน workspace นี้" />
3. [**/pstack:reflect**](/skills/reflect) — หลังจบงาน เปลี่ยนบทเรียนเป็นการแก้ skill ที่มีอยู่ซึ่งคุณอนุมัติ.

   <PromptBlock compact text="/pstack:reflect ช่วยจดสิ่งที่เราเรียนรู้ไว้ เพื่อให้รอบหน้าไม่พลาดซ้ำ" />
4. [**/pstack:correct**](/skills/correct) — แก้ที่ repo ไม่ให้ agent ทำผิดแบบเดิมซ้ำ.

   <PromptBlock compact text="/pstack:correct agent ชอบเพิ่ม config flag ใหม่โดยไม่ลงทะเบียนใน schema" />
5. [**Playbook: Authoring or modifying a skill**](/playbooks/authoring-or-modifying-a-skill) — เขียนหรือแก้ SKILL.md ผ่าน playbook เพื่อให้มี validate และรีวิว.

   <PromptBlock compact text="/pstack:poteto-mode เขียน skill สำหรับ release checklist ของเรา validate frontmatter และ link แล้วเปิด PR" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
