# 日本語モード: Markdownトークンを厳格に保持してください。

ルール（必須順守）:
1) Markdownリンクは正確に保持してください: [テキスト](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳テキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストとして書き換えないでください（例: 「テキスト」（URL）、テキスト (URL)）。
3) リンクテキストのみ翻訳し、Markdownの構造とURLは変更しないでください。
4) Markdownリンクの周囲に「」を追加しないでください。ただし外部リンクの文法で必要な場合は除く。

構造がスタイルより重要です。
Markdownトークンが変わる場合は、日本語の自然さを最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inacurateți. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care ar putea apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->