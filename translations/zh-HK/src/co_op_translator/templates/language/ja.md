Japanese mode: Markdownトークンを厳密に保持します。

ルール（必ず守ること）：
1) Markdownリンクは正確に保持すること：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [translated text](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) 絶対にリンクをプレーンテキストに書き換えないこと（例：「text」（URL）、text (URL) は不可）。
3) 翻訳するのはリンクテキスト部分のみで、Markdownの構造やURLは変更しないこと。
4) Markdownリンクの周囲に「」を追加しないこと。ただし、リンク外の文法上必要な場合を除く。

構造がスタイルより重要です。
Markdownトークンが変わってしまう場合は日本語の自然さを最適化しないこと。

例
原文：This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解：本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り：本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。如因使用此翻譯而產生任何誤解或誤釋，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->