# อัปเดตส่วน "หลักสูตรอื่นๆ" (Microsoft Beginners repos)

คู่มือนี้อธิบายวิธีการทำให้ส่วน "หลักสูตรอื่นๆ" ซิงโครไนซ์อัตโนมัติด้วย Co‑op Translator และวิธีการอัปเดตเท็มเพลตทั่วโลกสำหรับทุกรีโพ

- ใช้กับ: รีโพ Microsoft Beginners เท่านั้น
- ทำงานกับ: Co‑op Translator CLI และ GitHub Actions
- แหล่งที่มาของเท็มเพลต: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## เริ่มต้นอย่างรวดเร็ว: เปิดใช้งานการซิงค์อัตโนมัติในรีโพของคุณ

เพิ่มตัวบ่งชี้ต่อไปนี้รอบๆ ส่วน "หลักสูตรอื่นๆ" ใน README ของคุณ Co‑op Translator จะทำการแทนที่ทุกอย่างระหว่างตัวบ่งชี้เหล่านี้ในแต่ละครั้งที่ทำงาน

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ทุกครั้งที่ Co‑op Translator ทำงาน — ผ่าน CLI (เช่น `translate -l "<language codes>"`) หรือ GitHub Actions — จะอัปเดตส่วน "หลักสูตรอื่นๆ" ที่อยู่ระหว่างตัวบ่งชี้เหล่านี้โดยอัตโนมัติ

> [!NOTE]
> หากคุณมีรายชื่อที่มีอยู่แล้ว ให้ห่อหุ้มด้วยตัวบ่งชี้เดียวกัน การทำงานครั้งถัดไปจะแทนที่ด้วยเนื้อหามาตรฐานล่าสุด

---

## วิธีเปลี่ยนเนื้อหาระดับโลก

หากคุณต้องการอัปเดตเนื้อหามาตรฐานที่ปรากฏในรีโพ Beginners ทั้งหมด:

1. แก้ไขเท็มเพลต: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. เปิด pull request ไปยังรีโพ Co-op Translator พร้อมกับการเปลี่ยนแปลงของคุณ
3. หลังจาก PR ถูกรวมแล้ว เวอร์ชันของ Co‑op Translator จะถูกอัปเดต
4. ครั้งถัดไปที่ Co‑op Translator ทำงาน (CLI หรือ GitHub Action) ในรีโพเป้าหมาย จะซิงค์ส่วนที่อัปเดตโดยอัตโนมัติ

วิธีนี้ช่วยให้มีแหล่งข้อมูลที่ถูกต้องเดียวสำหรับเนื้อหา "หลักสูตรอื่นๆ" ในรีโพ Beginners ทั้งหมด

## ขนาดของรีโพ

รีโพสามารถมีขนาดใหญ่ขึ้นเนื่องจากจำนวนภาษาที่แปล เพื่อช่วยให้ผู้ใช้ปลายทางมีคำแนะนำเกี่ยวกับการใช้ clone - sparse เพื่อโคลนเฉพาะภาษาที่จำเป็นเท่านั้น ไม่ต้องโคลนรีโพทั้งหมด

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่เป็นทางการ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญภาษามนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->