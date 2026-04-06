Japanese mode: Markdownトークンを厳密に保持します。

ルール（必ず守ってください）：
1) Markdownリンクは完全に同じに保持してください：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えないでください（例：「text」（URL）, text (URL)など）。
3) リンクテキストのみ翻訳し、Markdownの構造とURLは変更しないでください。
4) Markdownリンクの周りに「」を付けないでください。ただし、外部リンクの文法上必要な場合を除きます。

構造はスタイルよりも重要です。
Markdownトークンが変わる場合は日本語の自然さを最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilmekle birlikte, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu olmadığımızı belirtiriz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->