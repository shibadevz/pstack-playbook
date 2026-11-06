# Playbook: Worktree and simulator cleanup

<small>ประเภท: **Playbook** · สถานการณ์: `Refactor/เก็บกวาด`</small>

## ใช้ทำอะไร

เคลียร์พื้นที่ดิสก์ด้วยการ prune git worktree ที่ merge แล้วหรือถูกทิ้ง และ iOS simulator เก่า โดยตรวจการใช้งานก่อนลบ

## ใช้เมื่อ

เช่นเมื่อดิสก์เต็มและสงสัยว่า worktree เก่าและ simulator กินพื้นที่

## ต่างจาก / ข้อควรรู้

ลบ state ของผู้ใช้โดยไม่มี code review มาคอยจับ จึงใช้ gate เป็นตัวรีวิว: bucket เป็นคำแนะนำ ไม่ใช่สิทธิ์ และ worktree ที่มี uncommitted work (`wip:N`) จะหยุดถามก่อน ขั้น simulator ใช้ `xcrun simctl` ซึ่งใช้ได้เฉพาะเครื่องที่มี Xcode

## วิธีเรียก

`/pstack:poteto-mode clean up worktrees. free up space.`

## ตัวอย่าง prompt

```text
/pstack:poteto-mode what's using my disk? clean up worktrees that are merged or abandoned and delete old simulators. show me what's safe to prune before you delete.
```
