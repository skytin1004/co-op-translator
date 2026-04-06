# อัปเดตส่วน "หลักสูตรอื่นๆ" (Microsoft Beginners repos)

คำแนะนำนี้อธิบายวิธีการทำให้ส่วน "หลักสูตรอื่นๆ" ซิงโครไนซ์อัตโนมัติด้วย Co‑op Translator และวิธีอัปเดตแม่แบบทั่วโลกสำหรับทุก repos

- ใช้กับ: Microsoft Beginners repositories เท่านั้น
- ทำงานร่วมกับ: Co‑op Translator CLI และ GitHub Actions
- แหล่งที่มาของแม่แบบ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## เริ่มต้นอย่างรวดเร็ว: เปิดใช้งานการซิงค์อัตโนมัติใน repo ของคุณ

เพิ่มเครื่องหมายต่อไปนี้รอบส่วน "หลักสูตรอื่นๆ" ใน README ของคุณ Co‑op Translator จะทำการแทนที่ทุกอย่างระหว่างเครื่องหมายเหล่านี้ในทุกครั้งที่รัน

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ทุกครั้งที่ Co‑op Translator ทำงาน—ผ่าน CLI (เช่น `translate -l "<language codes>"`) หรือ GitHub Actions—จะอัปเดตส่วน "หลักสูตรอื่นๆ" ที่ถูกครอบด้วยเครื่องหมายเหล่านี้โดยอัตโนมัติ

> [!NOTE]
> หากคุณมีรายการที่มีอยู่แล้ว เพียงแค่ครอบด้วยเครื่องหมายเดียวกัน การรันครั้งถัดไปจะแทนที่ด้วยเนื้อหามาตรฐานล่าสุด

---

## วิธีเปลี่ยนเนื้อหาระดับโลก

หากคุณต้องการอัปเดตเนื้อหามาตรฐานที่ปรากฏในทุก Beginners repos:

1. แก้ไขแม่แบบ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. เปิด pull request ไปยัง repo ของ Co-op Translator พร้อมกับการเปลี่ยนแปลงของคุณ
3. หลังจาก PR ถูกรวม Co‑op Translator เวอร์ชันจะได้รับการอัปเดต
4. ครั้งต่อไปที่ Co‑op Translator รัน (CLI หรือ GitHub Action) ใน repo เป้าหมาย มันจะซิงค์ส่วนที่อัปเดตโดยอัตโนมัติ

วิธีนี้จะรับประกันแหล่งความจริงเดียวสำหรับเนื้อหา "หลักสูตรอื่นๆ" ในทุก Beginners repositories

## ขนาดของ Repo

repo อาจมีขนาดใหญ่เนื่องจากจำนวนภาษาที่แปล เพื่อช่วยผู้ใช้ปลายทางในการแนะนำวิธีการใช้ clone - sparse เพื่อโคลนเฉพาะภาษาที่จำเป็นเท่านั้น ไม่ใช่โคลน repo ทั้งหมด

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
เอกสารนี้ได้ถูกแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามรักษาความถูกต้องให้มากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->