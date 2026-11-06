# ออกแบบ/วางแผน

ใช้เมื่อยังไม่ควรลงมือเขียน เช่นยังเลือก design ไม่ได้ หรือต้องวางแผนหลาย PR

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Prototype**](/playbooks/prototype.md) — ทำต้นแบบทิ้งขว้างหลายแบบหลัง switcher แล้วเลือกจากสิ่งที่รันได้. วิธีเรียก: พิมพ์ `/pstack:poteto-mode prototype a few options for <feature>.`
2. [**/pstack:architect**](/skills/architect.md) — ร่าง type และ module boundary ก่อน พิมพ์ "with checkpoint" ถ้าอยากตรวจก่อนเขียนโค้ด. วิธีเรียก: พิมพ์ `/pstack:architect`
3. [**/pstack:arena**](/skills/arena.md) — ขอความเห็นที่สองเรื่อง design จากหลาย candidate. วิธีเรียก: พิมพ์ `/pstack:arena`
4. [**Playbook: Multi-phase or multi-PR plan**](/playbooks/multi-phase-or-multi-pr-plan.md) — เมื่อ design นิ่งแล้ว ให้เขียนแผนเป็น PR เล็กที่ตรวจได้ แผนคือ deliverable และไม่ implement. วิธีเรียก: พิมพ์ `/pstack:poteto-mode turn this design into a plan.`
5. [**/pstack:figure-it-out**](/skills/figure-it-out.md) — เมื่อไม่มี playbook ไหนพอดี เช่น migration ใหญ่ข้ามหลายจุด. วิธีเรียก: พิมพ์ `/pstack:figure-it-out`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
