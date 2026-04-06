Japanese mode: Markdownトークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクを正確に保持：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたtext](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えない（例：「text」（URL）、text（URL））。
3) リンクのテキストだけを翻訳し、Markdownの構造とURLは変えない。
4) リンクの外側の文法的に必要な場合を除き、「」はつけない。

構造がスタイルより重要です。
Markdownトークンが変わる場合は日本語としての自然さの最適化を行わない。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正しい: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) használatával készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén ajánlott professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->