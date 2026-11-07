# เริ่มงาน/ตั้งค่า

ใช้เมื่อเพิ่งติดตั้ง PStack หรือกำลังจะเริ่มงานแรกในแชตใหม่

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:setup-pstack**](/skills/setup-pstack) — เลือก model ต่อ role และ reasoning budget ครั้งเดียว ถ้าไม่รัน ทุก role จะใช้ model ของ session.

   <PromptBlock compact text="/pstack:setup-pstack ช่วยตั้งค่า model และ reasoning budget ของ pstack" />
2. [**/pstack:poteto-mode**](/skills/poteto-mode) — เริ่มงานจริงด้วย goal และ done check ที่ตรวจได้ แล้วให้ playbook ที่ตรงกับงานเลือกขั้นตอนเอง.

   <PromptBlock compact text="/pstack:poteto-mode แก้ export ซ้ำตอน retry ช่วย repro ก่อน แล้วค่อย fix และ verify บน user path จริง" />
3. [**/pstack:in-your-own-words**](/skills/in-your-own-words) — ให้ agent เล่าความเข้าใจก่อนลงมือ ถ้าคำขอยาวหรือรก จะเห็นว่าอ่านผิดตรงไหนก่อนมีโค้ด.

   <PromptBlock compact text="/pstack:in-your-own-words &lt;วางคำสั่งที่ยาวหรือยุ่งเหยิงตรงนี้&gt;" />
4. [**/pstack:create-verification-skill**](/skills/create-verification-skill) — ถ้า project ยังไม่มีวิธี script ไว้ขับ app จริง skill นี้สร้างให้ เพื่อให้ agent ตรวจงานตัวเองได้.

   <PromptBlock compact text="/pstack:create-verification-skill ช่วยสร้าง verify skill สำหรับ web app ของ repo นี้ และพิสูจน์ว่าใช้งานได้จริงหนึ่งรอบก่อนส่งมอบ" />
5. [**/pstack:poteto-help**](/skills/poteto-help) — ไม่แน่ใจว่าจะใช้ skill ไหน ถามได้โดยไม่เริ่มงาน.

   <PromptBlock compact text="/pstack:poteto-help ทำยังไงให้ poteto-mode เปิดอยู่ทุก turn" />

## วิธีเขียน prompt

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
