Japanese mode: Markdownトークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクは完全にそのまま保持してください：[text](../../../../../../src/co_op_translator/templates/language/URL) → [翻訳されたtext](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えないこと（例：「text」（URL）、text (URL)など）。
3) リンクテキストのみ翻訳し、Markdownの構造とURLはそのままに。
4) 外部リンクの文法上必要な場合を除き、Markdownリンクの周りに「」を付けない。

構造は様式より重要です。
Markdownトークンが変わる場合は、自然な日本語を優先して最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正しい訳例: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤った訳例: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->