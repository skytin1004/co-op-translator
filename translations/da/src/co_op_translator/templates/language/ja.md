Japanese mode: Markdown トークンを厳密に保持してください。

ルール（必ず守ること）:
1) Markdownリンクは正確に保持すること: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキスト（例：「text」（URL）、text (URL)）に書き換えないこと。
3) 翻訳するのはリンクテキストのみ。Markdownの構造とURLは変更しないこと。
4) Markdownリンクの周りに「」を付けないこと。ただし、リンク外の文法上必要な場合は除く。

構造はスタイルより重要です。
Markdownトークンが変わる場合、日本語の自然さは最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->