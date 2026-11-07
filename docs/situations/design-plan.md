# ออกแบบ/วางแผน

ใช้เมื่อยังไม่ควรลงมือเขียน เช่นยังเลือก design ไม่ได้ หรือต้องวางแผนหลาย PR

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Prototype**](/playbooks/prototype) — ทำต้นแบบทิ้งขว้างหลายแบบหลัง switcher แล้วเลือกจากสิ่งที่รันได้.

   <PromptBlock compact text="/pstack:poteto-mode ทำ prototype layout ของหน้า settings สองสามแบบ ใส่ไว้หลัง switcher แล้วส่ง screenshot ของแต่ละแบบมาให้" />
2. [**/pstack:architect**](/skills/architect) — ร่าง type และ module boundary ก่อน พิมพ์ "with checkpoint" ถ้าอยากตรวจก่อนเขียนโค้ด.

   <PromptBlock compact text="/pstack:architect with checkpoint ช่วยร่าง type และ module boundary ของ retry queue ใน src/jobs/ แล้วให้ดู design ก่อนค่อย implement" />
3. [**/pstack:arena**](/skills/arena) — ขอความเห็นที่สองเรื่อง design จากหลาย candidate.

   <PromptBlock compact text="/pstack:arena ขอความเห็นที่สองเรื่อง design ของ thread นี้ ให้ candidate หลายตัวทำจาก brief เดียวกัน แล้วให้ judge ต่าง model เลือกแนวทางที่ดีที่สุดพร้อมเก็บส่วนดีของตัวอื่นมารวม" />
4. [**Playbook: Multi-phase or multi-PR plan**](/playbooks/multi-phase-or-multi-pr-plan) — เมื่อ design นิ่งแล้ว ให้เขียนแผนเป็น PR เล็กที่ตรวจได้ แผนคือ deliverable และไม่ implement.

   <PromptBlock compact text="/pstack:poteto-mode เปลี่ยน design นี้เป็น plan แบ่งเป็น PR เล็กๆ ที่ verify ได้ แต่ละอันมีขั้นตอน verification ของตัวเอง" />
5. [**/pstack:figure-it-out**](/skills/figure-it-out) — เมื่อไม่มี playbook ไหนพอดี เช่น migration ใหญ่ข้ามหลายจุด.

   <PromptBlock compact text="/pstack:figure-it-out migrate ทุก caller ของ logger API เก่าไปใช้ API ใหม่ done คือ API เก่าถูกลบแล้วและ test suite ทั้งหมดผ่าน" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
