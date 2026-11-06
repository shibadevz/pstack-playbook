# ปล่อยรันเอง/ข้ามคืน

ใช้เมื่อจะเดินไปไหนแล้วให้ agent ทำต่อเองจนเสร็จ และกลับมาตรวจทีหลัง

## เริ่มจากสิ่งเหล่านี้ (เรียงตามลำดับ)

1. [**Playbook: Autonomous run**](/playbooks/autonomous-run.md) — ตั้ง done เป็น check ที่ผ่านหรือไม่ผ่านได้ แล้วขับจนถึงเงื่อนไขนั้นโดยไม่หยุด. วิธีเรียก: พิมพ์ `/pstack:poteto-mode im going to bed. <goal>. done means <checks>.`
2. [**/pstack:show-me-your-work**](/skills/show-me-your-work.md) — เก็บ decision log เป็น TSV ให้ตรวจตอนเช้า เริ่มจากหัวข้อ Attention ท้าย reply. วิธีเรียก: พิมพ์ `/pstack:show-me-your-work`
3. [**/pstack:ketchup**](/skills/ketchup.md) — กลับมาแล้วอยากรู้สั้นๆ ว่าอะไรเปลี่ยนและอะไรรอให้ตัดสินใจ. วิธีเรียก: พิมพ์ `/pstack:ketchup`
4. [**Playbook: Pause safely**](/playbooks/pause-safely.md) — ต้องหยุดชั่วคราว (offline หรือ context ใกล้ compact) โดยให้งานต่อได้. วิธีเรียก: พิมพ์ `/pstack:poteto-mode pause safely.`
5. [**Playbook: Session pickup**](/playbooks/session-pickup.md) — รับช่วงงานที่ agent อีกแชตทำค้างไว้จาก transcript หรือ branch. วิธีเรียก: พิมพ์ `/pstack:poteto-mode take over this branch.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode im going to bed. migrate every caller to the new parser in a fresh worktree off main. done means zero old callers, all parser fixtures pass, old api deleted. keep a decision log. don't ask me before committing. if you're truly stuck after a few hours, stop and write up why.
```

เขียน prompt โดยบอก goal และ done check ที่ตรวจได้ ไม่ต้องไล่ชื่อ skill เอง ให้ `/pstack:poteto-mode` เลือกขั้นตอน
