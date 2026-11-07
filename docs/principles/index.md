---
pageClass: overview overview-cmd
---

# Principles

| คำสั่ง | ใช้ทำอะไร |
|---|---|
| [attack-the-premise](/principles/attack-the-premise) | เมื่อ fix สองอันขึ้นไปที่อยู่บน premise เดียวกันไม่ผ่าน gate เดิม ให้สำรวจก่อนว่า actor ไหนถือความไม่สมดุลอยู่ แล้วตั้งคำถามกับ premise แทนการเขียน fix ที่สามบน premise เดิม |
| [boundary-discipline](/principles/boundary-discipline) | วาง validation และ error handling ที่ขอบระบบ (CLI, config, network, external API) แล้วเชื่อ internal type และให้ business logic เป็น pure function |
| [build-the-lever](/principles/build-the-lever) | กับงาน non-trivial ทุกชนิด ให้สร้างเครื่องมือที่ทำหรือพิสูจน์งาน (codemod, script, generator หรือ skill ที่ subagent ทำตาม) แทนการทำมือ เครื่องมือคือ artifact ที่ผู้รีวิวรันซ้ำได้ |
| [encode-lessons-in-structure](/principles/encode-lessons-in-structure) | เมื่อเขียนคำสั่งเดิมซ้ำเป็นครั้งที่สอง หรือเห็นการแก้ที่เกิดซ้ำ ให้เข้ารหัสกฎเป็น lint, metadata flag, runtime check หรือ script แทนการเพิ่มข้อความ |
| [exhaust-the-design-space](/principles/exhaust-the-design-space) | เมื่อเจอ interaction ใหม่หรือการตัดสินใจเชิงสถาปัตยกรรมที่ไม่มีแบบอย่างใน codebase ให้ build prototype 2-3 แบบที่แข่งกันแล้วเทียบข้างกันก่อนตัดสินใจ |
| [experience-first](/principles/experience-first) | เมื่อต้องแลก product, UX หรือขอบเขตฟีเจอร์ ให้เลือกความพอใจของผู้ใช้เหนือความสะดวกของ implementation และส่งฟีเจอร์น้อยแต่เนี้ยบ ดีกว่ามากแต่หยาบ |
| [explain-the-number](/principles/explain-the-number) | ก่อนเชื่อ รายงาน หรือลงมือตามตัวเลขที่วัดมา (speedup, regression, throughput, latency, eval result) ให้หาสิ่งที่จำกัดตัวเลข และตัดความเป็นไปได้ว่าวัดสิ่งอื่นที่ไม่ใช่งานจริง |
| [fix-root-causes](/principles/fix-root-causes) | เวลา debug ให้ไล่แต่ละอาการไปถึง root cause แล้วแก้ที่นั่น: repro ก่อน ถาม why จนถึงต้นทาง และต้านการใส่ nil-check ที่แค่ปิดเสียง crash |
| [foundational-thinking](/principles/foundational-thinking) | ก่อนเขียน logic ให้เลือกชนิดข้อมูลและโครงข้อมูลหลัก ลำดับงานระหว่าง scaffold กับ feature และถามว่า actor พร้อมกันใช้อะไรร่วมกัน เพื่อให้โค้ดที่ตามมาชัดเจนเอง |
| [guard-the-context-window](/principles/guard-the-context-window) | เมื่อ context กำลังเต็ม (output ใหญ่ ไฟล์ยาว อ่านซ้ำ วางแผน fan-out) ให้ส่งงานก้อนใหญ่ให้ subagent และเก็บแค่สรุปใน main thread ไม่ใช่ payload ดิบ |
| [laziness-protocol](/principles/laziness-protocol) | เมื่อ refactor, ประเมินขนาด diff หรืออยากเพิ่ม abstraction, layer: เอนไปทางการลบและการเปลี่ยนที่เล็กที่สุดที่แก้ปัญหาได้ ตัดสินใจเรื่องเดียวกันที่เดียว |
| [make-operations-idempotent](/principles/make-operations-idempotent) | เมื่อออกแบบ command, lifecycle step หรือ loop ที่ทำงานท่ามกลาง crash, restart และ retry ให้บรรจบที่ end state เดียวกันไม่ว่าจะเคยรันค้างไว้แค่ไหน |
| [migrate-callers-then-delete-legacy-apis](/principles/migrate-callers-then-delete-legacy-apis) | เมื่อเพิ่ม internal API ใหม่แต่ยังมี caller เก่า ให้ย้าย caller และลบ API เก่าใน wave เดียวกัน แทนการเก็บ compatibility layer |
| [minimize-reader-load](/principles/minimize-reader-load) | เมื่อรีวิวหรือปรับโค้ดที่ตามยาก ให้นับ layer ระหว่างคำถามกับคำตอบและ hidden state ในหัวผู้อ่าน แล้วยุบ wrapper ที่มี caller เดียวและลด scope ของ mutable state |
| [model-the-domain](/principles/model-the-domain) | เมื่อเขียน logic ที่มี state หรือโค้ดแตกแขนงมากและซ้ำการสมมติรูปข้อมูลหลายไฟล์ ให้ใส่ domain ลงโครงสร้าง (state machine, typed model, table/registry) แทนเงื่อนไขกระจัดกระจาย |
| [never-block-on-the-human](/principles/never-block-on-the-human) | เมื่ออยากถามว่า "ทำ X ดีไหม" กับงานที่ย้อนกลับได้ ให้ทำไปแล้วอธิบายเหตุผล ให้มนุษย์แก้ทางทีหลัง ส่วนงานย้อนกลับไม่ได้ (force-push, ลบ data จริง, ส่งข้อความออกนอก) ยังต้องขออนุญาต |
| [outcome-oriented-execution](/principles/outcome-oriented-execution) | ใน rewrite หรือ migration ที่วางแผนไว้มี phase ชัด ให้มุ่งไปที่สถาปัตยกรรมเป้าหมาย ไม่ต้องรักษาสถานะระหว่างทางให้ราบรื่นด้วยโค้ดชั่วคราว |
| [prove-it-works](/principles/prove-it-works) | หลังงานเสร็จและก่อนประกาศว่าเสร็จ ให้ตรวจกับของจริง (รัน feature, อ่านค่าที่เก็บจริง, ดู diff) ไม่ใช่ proxy, self-report หรือ "compile ผ่าน" |
| [redesign-from-first-principles](/principles/redesign-from-first-principles) | เมื่อใส่ requirement ใหม่ลงใน design เดิม ให้ออกแบบใหม่เหมือน requirement นั้นเป็นข้อสมมติฐานตั้งแต่วันแรก ส่งผลไปทุกจุดที่อ้างถึง (type, docs, ตัวอย่าง) และคิดทั้ง redesign แล้วส่งมอบทีละส่วน |
| [separate-before-serializing-shared-state](/principles/separate-before-serializing-shared-state) | เมื่อ actor พร้อมกันอาจเขียนไฟล์, branch, key หรือ state object เดียวกัน ให้กำจัดการแชร์ก่อน และใช้ serialize ก็ต่อเมื่อ writer เดียวร่วมเป็น invariant จริง |
| [sequence-verifiable-units](/principles/sequence-verifiable-units) | กับงานหลายขั้น (sweep, migration, edit ซ้ำๆ) และการ stack commit/PR ให้แตกเป็นหน่วยเล็กที่จบด้วยสถานะที่ตรวจได้ ตรวจแต่ละหน่วยก่อนไปหน่วยถัดไป และเรียงการส่งมอบให้ลำดับพิสูจน์ตัวเองให้ผู้รีวิวเห็น |
| [subtract-before-you-add](/principles/subtract-before-you-add) | เมื่อจะเพิ่ม, refactor หรือ rewrite ให้ลบก่อน (dead code, validator ซ้ำซ้อน, stub ที่ไม่มีเนื้อหา) แล้วค่อยสร้างบนฐานที่ง่ายกว่า |
| [test-behavior-not-implementation](/principles/test-behavior-not-implementation) | เมื่อเขียน แก้ หรือคง test ให้เรียกโค้ดแบบที่ผู้ใช้เรียกและ assert ผลที่ผู้ใช้เห็นจริง และเขียนใหม่หรือลบ test ที่ยังผ่านแม้ทุก function ที่ import คืน undefined |
| [type-system-discipline](/principles/type-system-discipline) | เมื่อออกแบบ type หรือ signature ในภาษา static type ให้ทำให้ state ที่เป็นไปไม่ได้แสดงไม่ได้ brand primitive ที่มีความหมาย parse ข้อมูลภายนอกที่ขอบ ไม่โกหก compiler และ exhaust ทุก variant |
