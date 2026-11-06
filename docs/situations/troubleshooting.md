# ปัญหาที่เจอบ่อย

ตารางนี้ใช้เมื่อ run ไปผิดทาง แต่ละแถวบอกอาการ วิธีแก้ และตัวอย่าง

| อาการ | วิธีแก้ | ตัวอย่าง |
|---|---|---|
| โหมดหยุดทำงานหลังผ่านไปไม่กี่ turn | เปิดโหมดโดยไม่ได้ขึ้นต้นข้อความด้วย `/pstack:poteto-mode` หรือ hook ไม่ได้ทำงาน ให้ขึ้นต้นข้อความด้วย `/pstack:poteto-mode` | พิมพ์ `/pstack:poteto-mode continue with the export fix` แทนการเขียนว่า "ใช้ poteto-mode ต่อ" กลางประโยค |
| คำถามถูกมองเป็นขั้นต่อของงานก่อนหน้า | พูดว่า "new task" หรือบอกว่า turn นี้ไม่ต้องใช้โหมด | "new task. how does the scheduler pick the next job?" |
| เลือก model ใหม่แล้วไม่มีผล | `models.json` จาก `/pstack:setup-pstack` ถูกอ่านใหม่ทุก dispatch จึงไม่ต้องเปิดแชตใหม่ ให้เช็กว่า `.pstack/claude/models.json` ของ project ไม่ได้ override ไฟล์ระดับผู้ใช้ | เพิ่งตั้ง review panel เป็นสาม model แต่ project มีไฟล์เก่าอยู่ ให้แก้หรือลบไฟล์ของ project |
| ค่าใช้จ่ายสูงกว่าคาด | รัน `/pstack:setup-pstack` ซ้ำเพื่อเลือก budget เล็กลงหรือ model ถูกลง ตั้ง role เป็น `auto` หรือ `inherit-parent` เพื่อใช้ model ของแชต ย่อ panel ให้สั้นลง และใช้ `/pstack:poteto-mode` กับงานที่ต้องการความเข้มงวดเท่านั้น | แก้ typo หนึ่งบรรทัดไม่ต้องใช้ `/pstack:poteto-mode` |
| skill ไม่โหลดเอง | มีแค่ `/pstack:setup-pstack` ที่โหลดจากคำพูดของผู้ใช้ ตัวอื่นโหลดเมื่อพิมพ์เรียกหรือเมื่อ `/pstack:poteto-mode` เรียกใช้ และ `/pstack:poteto-mode` ไม่ได้เรียกทุก skill | พิมพ์ `/pstack:interrogate the whole branch` เองแทนการหวังว่าจะถูกเรียก |
| agent หลายตัวเขียนทับกัน | ให้แต่ละ agent มี worktree ของตัวเอง หรือใช้ remote runner ที่ยืนยันแล้ว | เติม "own worktree per attempt" ใน prompt |
| run ข้ามคืนขยับแต่ไม่เสร็จอะไร | กลไกปลุกต้องมี check ที่ผ่านหรือไม่ผ่านได้ ไม่ใช่ระยะเวลา (ดูเรื่อง overnight ใน guide หน้า 7 ของ repo) | เปลี่ยนจาก "keep going for 8 hours" เป็น "done means all parser fixtures pass" |
| reply บอกว่าสำเร็จเพราะ build เขียว | ขอคำสั่งจริง, flow จริง, ค่าที่เก็บจริง หรือ profile ซึ่งคือ principle prove-it-works | "apply prove it works. show me the real output, not the build log." |

ถ้า run ลอยไปเรื่อยๆ ใช้ prompt บรรทัดเดียวบังคับทางได้ เช่น "i said the goal is to repro. i did not ask for a fix yet."
