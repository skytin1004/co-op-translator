# 日本語モード: Markdownトークンを厳密に保持する.

ルール（必ず守ること）:  
1) Markdownリンクはそのまま保持: [テキスト](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳テキスト](../../../../../../src/co_op_translator/templates/language/同じURL)  
2) 絶対にリンクをプレーンテキスト化しない（例: 「テキスト」（URL）やテキスト (URL))  
3) リンクテキストのみ翻訳し、Markdownの構造やURLは変更しない  
4) Markdownリンクのまわりに「」を付けない（文法上必要な場合を除く）  

構造優先で自然さを犠牲にしてもOK。Markdownトークンの変更はしないこと。  

例  
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).  
正: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。  
誤: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->