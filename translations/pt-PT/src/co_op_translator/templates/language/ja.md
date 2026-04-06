Japanese mode: Markdownトークンを厳密に保持します。

ルール（必ず守ること）：
1) Markdownリンクは正確に保持すること：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳済みtext](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) 決してリンクをプレーンテキストに書き換えないこと（例：「text」（URL）、text (URL)）。
3) リンクテキストのみ翻訳すること；Markdownの構造とURLは変更しないこと。
4) Markdownリンクの周りに「」を追加しないこと（リンク外の文法による場合を除く）。

構造の方がスタイルより重要。
Markdownトークンが変わる場合は日本語の自然さを最適化しないこと。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正しい例: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
間違い例: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, é recomendada a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->