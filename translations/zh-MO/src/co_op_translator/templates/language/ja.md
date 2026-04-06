Japanese mode：Markdownトークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクは正確に維持すること：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたtext](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えないこと（例：「text」（URL）、text (URL)など）。
3) リンクテキストのみを翻訳し、Markdownの構造とURLはそのまま保持すること。
4) Markdownリンクの外側の文法が必要としない限り、「」をリンクの周りに追加しないこと。

構造はスタイルより重要です。Markdownトークンが変更される場合は、日本語の自然さを最適化しないでください。

例
原文：This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正しい：本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り：本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於提供準確的翻譯，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯所產生的任何誤解或誤釋不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->