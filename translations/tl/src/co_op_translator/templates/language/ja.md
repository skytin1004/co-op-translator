Japanese mode: Markdownトークンを厳密に保持。

ルール（必ず従うこと）：
1) Markdownリンクは正確に保持：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストとして書き換えない（例：「text」（URL）、text (URL)）。
3) リンクテキストのみ翻訳し、Markdownの構造とURLは変更しない。
4) Markdownリンクの周りに「」を付けない（外部リンクの文法上必要な場合を除く）。

構造はスタイルよりも重要。
Markdownトークンが変更される場合は、日本語の自然さを最適化しないこと。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong mga pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tamang impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang itinuturing na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkaunawa o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->