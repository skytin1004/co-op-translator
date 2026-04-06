# Command reference

The **Co-op Translator** CLI มีตัวเลือกหลายอย่างให้ปรับแต่งกระบวนการแปล:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | แปลโปรเจกต์ของคุณเป็นภาษาที่ระบุ ตัวอย่าง: translate -l "es fr de" แปลเป็นภาษาสเปน ฝรั่งเศส และเยอรมัน ใช้ translate -l "all" เพื่อแปลเป็นทุกภาษาที่รองรับ
translate -l "language_codes" -u              | อัปเดตการแปลโดยลบการแปลที่มีอยู่และสร้างใหม่ หมายเหตุ: การดำเนินการนี้จะลบการแปลปัจจุบันทั้งหมดสำหรับภาษาที่ระบุ
translate -l "language_codes" -img            | แปลเฉพาะไฟล์รูปภาพ
translate -l "language_codes" -md             | แปลเฉพาะไฟล์ Markdown
translate -l "language_codes" -nb             | แปลเฉพาะไฟล์สมุดบันทึก Jupyter (.ipynb)
translate -l "language_codes" --fix           | แปลซ้ำไฟล์ที่ได้คะแนนความมั่นใจต่ำตามผลการประเมินก่อนหน้า
translate -l "language_codes" -d              | เปิดโหมดดีบักสำหรับบันทึกรายละเอียด
translate -l "language_codes" --save-logs, -s | บันทึกบันทึกในระดับ DEBUG ลงในไฟล์ภายใต้ <root_dir>/logs/ (คอนโซลยังคงควบคุมด้วย -d)
translate -l "language_codes" -r "root_dir"   | กำหนดไดเรกทอรีรูทของโปรเจกต์
translate -l "language_codes" -f              | ใช้โหมดเร็วสำหรับการแปลรูปภาพ (เร็วขึ้นสูงสุด 3 เท่าที่มีผลกระทบเล็กน้อยต่อคุณภาพและการจัดตำแหน่ง)
translate -l "language_codes" -y              | ยืนยันคำสั่งทั้งหมดโดยอัตโนมัติ (มีประโยชน์สำหรับ pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | เปิดหรือปิดการเพิ่มส่วนปฏิเสธความรับผิดชอบการแปลเครื่องในไฟล์ markdown และสมุดบันทึกที่แปลแล้ว (ค่าเริ่มต้น: เปิดใช้งาน)
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | ปรับแต่งส่วนคำแนะนำภาษาใน README (sparse checkout) ด้วย URL ของรีโปของคุณ
translate -l "language_codes" --help          | รายละเอียดคำสั่งช่วยเหลือใน CLI แสดงคำสั่งที่ใช้ได้
evaluate -l "language_code"                  | ประเมินคุณภาพการแปลสำหรับภาษาที่ระบุและให้คะแนนความมั่นใจ
evaluate -l "language_code" -c 0.8           | ประเมินการแปลด้วยเกณฑ์ความมั่นใจที่กำหนดเอง
evaluate -l "language_code" -f               | โหมดประเมินเร็ว (เฉพาะกฎ ไม่มี LLM)
evaluate -l "language_code" -D               | โหมดประเมินลึก (เฉพาะ LLM ละเอียดแต่ช้ากว่า)
evaluate -l "language_code" --save-logs, -s  | บันทึกบันทึกระดับ DEBUG ลงในไฟล์ภายใต้ <root_dir>/logs/
migrate-links -l "language_codes"             | ประมวลผลไฟล์ Markdown ที่แปลแล้วเพื่ออัปเดตลิงก์ไปยังสมุดบันทึก (.ipynb) โดยเลือกสมุดบันทึกที่แปลแล้วเมื่อตัวเลือกมี; หากไม่มีจะกลับไปใช้สมุดบันทึกต้นฉบับ
migrate-links -l "language_codes" -r          | กำหนดไดเรกทอรีรูทของโปรเจกต์ (ค่าเริ่มต้น: ไดเรกทอรีปัจจุบัน)
migrate-links -l "language_codes" --dry-run   | แสดงไฟล์ที่จะเปลี่ยนโดยไม่เขียนการเปลี่ยนแปลง
migrate-links -l "language_codes" --no-fallback-to-original | ไม่เขียนลิงก์ไปยังสมุดบันทึกต้นฉบับเมื่อไม่มีสมุดบันทึกแปล (อัปเดตเฉพาะเมื่อมีการแปล)
migrate-links -l "language_codes" -d          | เปิดโหมดดีบักสำหรับบันทึกรายละเอียด
migrate-links -l "language_codes" --save-logs, -s | บันทึกบันทึกระดับ DEBUG ลงในไฟล์ภายใต้ <root_dir>/logs/
migrate-links -l "all" -y                      | ประมวลผลทุกภาษาและยืนยันคำเตือนโดยอัตโนมัติ

## Usage examples

  1. พฤติกรรมเริ่มต้น (เพิ่มการแปลใหม่โดยไม่ลบแปลที่มี):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. เพิ่มเฉพาะการแปลภาพเกาหลีใหม่ (ไม่ลบการแปลที่มีอยู่):    translate -l "ko" -img

  3. อัปเดตการแปลเกาหลีทั้งหมด (คำเตือน: จะลบการแปลเกาหลีทั้งหมดก่อนแปลใหม่):    translate -l "ko" -u

  4. อัปเดตเฉพาะภาพเกาหลี (คำเตือน: จะลบภาพเกาหลีทั้งหมดก่อนแปลใหม่):    translate -l "ko" -img -u

  5. เพิ่มการแปล markdown เกาหลีใหม่โดยไม่กระทบการแปลอื่น:    translate -l "ko" -md

  6. แก้ไขการแปลความมั่นใจต่ำตามผลประเมินก่อนหน้า: translate -l "ko" --fix

  7. แก้ไขการแปลความมั่นใจต่ำเฉพาะไฟล์บางประเภท (markdown): translate -l "ko" --fix -md

  8. แก้ไขการแปลความมั่นใจต่ำเฉพาะไฟล์บางประเภท (รูปภาพ): translate -l "ko" --fix -img

  9. ใช้โหมดเร็วสำหรับแปลภาพ:    translate -l "ko" -img -f

  10. แก้ไขการแปลความมั่นใจต่ำด้วยเกณฑ์กำหนดเอง: translate -l "ko" --fix -c 0.8

  11. ตัวอย่างโหมดดีบัก: - translate -l "ko" -d: เปิดบันทึกดีบัก
  12. บันทึกบันทึกลงไฟล์: translate -l "ko" -s
  13. DEBUG บนคอนโซลและไฟล์: translate -l "ko" -d -s
  14. แปลโดยไม่เพิ่มปฏิเสธความรับผิดชอบการแปลเครื่องในผลลัพธ์: translate -l "ko" --no-disclaimer

  15. โยกย้ายลิงก์สมุดบันทึกสำหรับการแปลเกาหลี (อัปเดตลิงก์ไปยังสมุดบันทึกที่แปลแล้วเมื่อมี):    migrate-links -l "ko"

  15. โยกย้ายลิงก์ด้วย dry-run (ไม่เขียนไฟล์):    migrate-links -l "ko" --dry-run

  16. อัปเดตลิงก์เฉพาะเมื่อมีสมุดบันทึกแปล (ไม่ใช้ลิงก์ต้นฉบับ):    migrate-links -l "ko" --no-fallback-to-original

  17. ประมวลผลทุกภาษาพร้อมคำยืนยัน:    migrate-links -l "all"

  18. ประมวลผลทุกภาษาและยืนยันโดยอัตโนมัติ:    migrate-links -l "all" -y
  19. บันทึกบันทึกลงไฟล์สำหรับ migrate-links:    migrate-links -l "ko ja" -s

  20. ปรับแต่งคำแนะนำส่วนภาษา README ด้วย URL รีโปของคุณ:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **ฟีเจอร์เบต้า**: ฟังก์ชันการประเมินยังอยู่ในสถานะเบต้า ฟีเจอร์นี้เปิดตัวเพื่อประเมินเอกสารแปล และวิธีการประเมินรวมถึงการดำเนินการโดยละเอียดยังอยู่ระหว่างพัฒนาและอาจมีการเปลี่ยนแปลงในอนาคต

  1. ประเมินการแปลภาษาเกาหลี: evaluate -l "ko"

  2. ประเมินด้วยเกณฑ์ความมั่นใจที่กำหนดเอง: evaluate -l "ko" -c 0.8

  3. ประเมินเร็ว (เฉพาะกฎ): evaluate -l "ko" -f

  4. ประเมินลึก (เฉพาะ LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้การแปลโดยนักแปลมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->