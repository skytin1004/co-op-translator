Japanese mode: Markdownトークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクをそのまま保持する：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキスト（例：「text」（URL）、text (URL)）に書き換えない。
3) リンクテキストのみを翻訳し、Markdown構造とURLは変更しない。
4) 外部リンクの文法上の必要がない限り、Markdownリンクの周りに「」を追加しない。

構造はスタイルより重要です。
Markdownトークンが変わるような日本語の自然な最適化はしないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogiškas vertimas. Mes neatsakom už jokius nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->