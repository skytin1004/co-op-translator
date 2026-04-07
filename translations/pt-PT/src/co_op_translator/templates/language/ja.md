日本語モード: Markdownトークンを厳密に保持してください。

ルール（必ず従うこと）:
1) Markdownリンクを正確に保持すること: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えないこと（例：「text」（URL）、text（URL））。
3) リンクのテキストのみ翻訳し、Markdown構造とURLは変更しないこと。
4) 外部リンクの文法が必要な場合を除き、Markdownリンクの周りに「」を付けないこと。

構造はスタイルよりも重要です。
Markdownトークンが変わる場合、日本語の自然さを最適化しないでください。

例
ソース: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正しい: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->