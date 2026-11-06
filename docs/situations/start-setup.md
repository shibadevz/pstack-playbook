# เริ่มงาน/ตั้งค่า

ใช้เมื่อเพิ่งติดตั้ง PStack หรือกำลังจะเริ่มงานแรกในแชตใหม่

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**/pstack:setup-pstack**](/skills/setup-pstack.md) — เลือก model ต่อ role และ reasoning budget ครั้งเดียว ถ้าไม่รัน ทุก role จะใช้ model ของ session. วิธีเรียก: พิมพ์ `/pstack:setup-pstack`
2. [**/pstack:poteto-mode**](/skills/poteto-mode.md) — เริ่มงานจริงด้วย goal และ done check ที่ตรวจได้ แล้วให้ playbook ที่ตรงกับงานเลือกขั้นตอนเอง. วิธีเรียก: พิมพ์ `/pstack:poteto-mode <goal และ done check>`
3. [**/pstack:in-your-own-words**](/skills/in-your-own-words.md) — ให้ agent เล่าความเข้าใจก่อนลงมือ ถ้าคำขอยาวหรือรก จะเห็นว่าอ่านผิดตรงไหนก่อนมีโค้ด. วิธีเรียก: พิมพ์ `/pstack:in-your-own-words`
4. [**/pstack:create-verification-skill**](/skills/create-verification-skill.md) — ถ้า project ยังไม่มีวิธี script ไว้ขับ app จริง skill นี้สร้างให้ เพื่อให้ agent ตรวจงานตัวเองได้. วิธีเรียก: พิมพ์ `/pstack:create-verification-skill`
5. [**/pstack:poteto-help**](/skills/poteto-help.md) — ไม่แน่ใจว่าจะใช้ skill ไหน ถามได้โดยไม่เริ่มงาน. วิธีเรียก: พิมพ์ `/pstack:poteto-help <คำถาม>`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode add a --json flag to the export command. text output stays byte-identical. verify both.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
