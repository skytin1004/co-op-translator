Japanese mode: Markdownトークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクをそのまま保持：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳済みtext](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに変換しない（例：「text」（URL）、text (URL)）。
3) リンクのテキストのみ翻訳し、Markdownの構造とURLは変更しない。
4) Markdownリンクの周囲に「」を付けない。ただし、リンク外の文法上必要な場合を除く。

構造はスタイルより優先されます。  
Markdownトークンが変わる場合は、日本語の自然な表現を最適化しないでください。

例  
元文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).  
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。  
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->