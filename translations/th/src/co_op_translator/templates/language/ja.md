Japanese mode: マークダウンのトークンを厳密に保持してください。

ルール（必ず守ってください）：
1) マークダウンのリンクを正確に保持する：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) 絶対にリンクをプレーンテキストとして書き換えない（例：「text」（URL）、text (URL)）。
3) リンクテキストのみを翻訳し、マークダウンの構造とURLは変更しない。
4) マークダウンのリンクの周りに「」を追加しない。ただし、外部リンクの文法上必要な場合は除く。

構造はスタイルより重要です。
マークダウンのトークンが変わる場合は、日本語の自然さを最適化しないでください。

例
元文：This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解：本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
不正解：本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->