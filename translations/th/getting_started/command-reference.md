# Command reference

The **Co-op Translator** CLI มีตัวเลือกหลายอย่างเพื่อปรับแต่งกระบวนการแปล:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | แปลโปรเจกต์ของคุณเป็นภาษาที่ระบุ ตัวอย่าง: translate -l "es fr de" แปลเป็นภาษาสเปน ฝรั่งเศส และเยอรมัน ใช้ translate -l "all" เพื่อแปลเป็นทุกภาษาที่รองรับ
translate -l "language_codes" -u              | อัปเดตการแปลโดยลบการแปลที่มีอยู่และสร้างใหม่ คำเตือน: สิ่งนี้จะลบการแปลทั้งหมดในปัจจุบันสำหรับภาษาที่ระบุ
translate -l "language_codes" -img            | แปลเฉพาะไฟล์ภาพ
translate -l "language_codes" -md             | แปลเฉพาะไฟล์ Markdown
translate -l "language_codes" -nb             | แปลเฉพาะไฟล์ Jupyter notebook (.ipynb)
translate -l "language_codes" --fix           | แปลซ้ำไฟล์ที่มีคะแนนความมั่นใจต่ำตามผลการประเมินก่อนหน้า
translate -l "language_codes" -d              | เปิดโหมดดีบักเพื่อบันทึกรายละเอียด
translate -l "language_codes" --save-logs, -s | บันทึกบันทึก DEBUG ระดับไว้ในไฟล์ภายใต้ <root_dir>/logs/ (คอนโซลยังคงควบคุมโดย -d)
translate -l "language_codes" -r "root_dir"   | ระบุไดเรกทอรีรูทของโปรเจกต์
translate -l "language_codes" -f              | ใช้โหมดเร็วสำหรับการแปลภาพ (เร็วขึ้นถึง 3 เท่าโดยมีค่าใช้จ่ายเล็กน้อยในคุณภาพและการจัดแนว)
translate -l "language_codes" -y              | ยืนยันอัตโนมัติสำหรับทุกพรอมต์ (เหมาะสำหรับ CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | เปิดหรือปิดการเพิ่มส่วนคำชี้แจงการแปลเครื่องใน markdown และโน้ตบุ๊กที่แปลแล้ว (ค่าเริ่มต้น: เปิด)
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | ปรับแต่งส่วนภาษา README ด้วย URL ที่เก็บของคุณ (sparse checkout)
translate -l "language_codes" --help          | รายละเอียดช่วยเหลือภายใน CLI แสดงคำสั่งที่มี
evaluate -l "language_code"                  | ประเมินคุณภาพการแปลสำหรับภาษาหนึ่งและให้คะแนนความมั่นใจ
evaluate -l "language_code" -c 0.8           | ประเมินการแปลด้วยเกณฑ์ความมั่นใจที่กำหนดเอง
evaluate -l "language_code" -f               | โหมดประเมินแบบเร็ว (ใช้กฎเท่านั้น ไม่มี LLM)
evaluate -l "language_code" -D               | โหมดประเมินลึก (ใช้ LLM เท่านั้น ละเอียดกว่าแต่ช้ากว่า)
evaluate -l "language_code" --save-logs, -s  | บันทึกบันทึก DEBUG ระดับไว้ในไฟล์ภายใต้ <root_dir>/logs/
migrate-links -l "language_codes"             | ประมวลผลไฟล์ Markdown ที่แปลเพื่ออัปเดตลิงก์ไปยังโน้ตบุ๊ก (.ipynb) โดยเลือกโน้ตบุ๊กแปลหากมี มิฉะนั้นจะใช้โน้ตบุ๊กต้นฉบับแทน
migrate-links -l "language_codes" -r          | ระบุไดเรกทอรีรูทของโปรเจกต์ (ค่าเริ่มต้น: ไดเรกทอรีปัจจุบัน)
migrate-links -l "language_codes" --dry-run   | แสดงว่าไฟล์ใดจะเปลี่ยนโดยไม่เขียนทับไฟล์
migrate-links -l "language_codes" --no-fallback-to-original | ไม่เขียนลิงก์กลับไปยังโน้ตบุ๊กต้นฉบับเมื่อไม่มีโน้ตบุ๊กที่แปล (อัปเดตเฉพาะเมื่อมีโน้ตบุ๊กแปล)
migrate-links -l "language_codes" -d          | เปิดโหมดดีบักเพื่อบันทึกรายละเอียด
migrate-links -l "language_codes" --save-logs, -s | บันทึกบันทึก DEBUG ระดับไว้ในไฟล์ภายใต้ <root_dir>/logs/
migrate-links -l "all" -y                      | ประมวลผลทุกภาษาและยืนยันอัตโนมัติสำหรับพรอมต์คำเตือน

## Usage examples

  1. พฤติกรรมเริ่มต้น (เพิ่มการแปลใหม่โดยไม่ลบการแปลที่มี):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. เพิ่มการแปลภาพภาษาเกาหลีใหม่เท่านั้น (ไม่ลบการแปลที่มีอยู่):    translate -l "ko" -img

  3. อัปเดตการแปลภาษาเกาหลีทั้งหมด (คำเตือน: สิ่งนี้จะลบการแปลภาษาเกาหลีทั้งหมดก่อนแปลใหม่):    translate -l "ko" -u

  4. อัปเดตเฉพาะภาพภาษาเกาหลี (คำเตือน: สิ่งนี้จะลบภาพภาษาเกาหลีทั้งหมดก่อนแปลใหม่):    translate -l "ko" -img -u

  5. เพิ่มการแปล markdown ใหม่สำหรับภาษาเกาหลีโดยไม่กระทบการแปลอื่น:    translate -l "ko" -md

  6. แก้ไขการแปลที่มีความมั่นใจต่ำตามผลการประเมินก่อนหน้า: translate -l "ko" --fix

  7. แก้ไขการแปลที่มีความมั่นใจต่ำสำหรับไฟล์เฉพาะ (markdown): translate -l "ko" --fix -md

  8. แก้ไขการแปลที่มีความมั่นใจต่ำสำหรับไฟล์เฉพาะ (ภาพ): translate -l "ko" --fix -img

  9. ใช้โหมดเร็วสำหรับการแปลภาพ:    translate -l "ko" -img -f

  10. แก้ไขการแปลที่มีความมั่นใจต่ำด้วยเกณฑ์กำหนดเอง: translate -l "ko" --fix -c 0.8

  11. ตัวอย่างโหมดดีบัก: - translate -l "ko" -d: เปิดบันทึกดีบัก
  12. บันทึกบันทึกลงไฟล์: translate -l "ko" -s
  13. DEBUG ในคอนโซลและไฟล์: translate -l "ko" -d -s
  14. แปลโดยไม่เพิ่มคำชี้แจงการแปลเครื่องในผลลัพธ์: translate -l "ko" --no-disclaimer

  15. ย้ายลิงก์โน้ตบุ๊กสำหรับการแปลภาษาเกาหลี (อัปเดตลิงก์ไปยังโน้ตบุ๊กแปลเมื่อมี):    migrate-links -l "ko"

  15. ย้ายลิงก์ด้วย dry-run (ไม่เขียนไฟล์):    migrate-links -l "ko" --dry-run

  16. อัปเดตลิงก์เฉพาะเมื่อมีโน้ตบุ๊กแปล (ไม่ย้อนกลับไปต้นฉบับ):    migrate-links -l "ko" --no-fallback-to-original

  17. ประมวลผลทุกภาษาพร้อมพรอมต์ยืนยัน:    migrate-links -l "all"

  18. ประมวลผลทุกภาษาและยืนยันอัตโนมัติ:    migrate-links -l "all" -y
  19. บันทึกบันทึกไฟล์สำหรับ migrate-links:    migrate-links -l "ko ja" -s

  20. ปรับแต่งคำแนะนำส่วนภาษา README ด้วย URL repo ของคุณ:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: ฟีเจอร์การประเมินยังอยู่ในสถานะเบต้า ฟีเจอร์นี้ถูกปล่อยออกมาเพื่อประเมินเอกสารที่แปลแล้ว และวิธีการประเมินรวมถึงการดำเนินการโดยละเอียดยังอยู่ในระหว่างการพัฒนาและอาจมีการเปลี่ยนแปลงได้

  1. ประเมินการแปลภาษาเกาหลี: evaluate -l "ko"

  2. ประเมินด้วยเกณฑ์ความมั่นใจที่กำหนดเอง: evaluate -l "ko" -c 0.8

  3. ประเมินแบบเร็ว (ใช้กฎเท่านั้น): evaluate -l "ko" -f

  4. ประเมินแบบลึก (ใช้ LLM เท่านั้น): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้บริการแปลภาษาจากมนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->