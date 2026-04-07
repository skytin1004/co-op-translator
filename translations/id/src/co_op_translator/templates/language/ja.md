Japanese mode: Markdownトークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクは正確に保持する：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) 絶対にリンクをプレーンテキストに書き直さない（例：「text」（URL）、text (URL)）。
3) リンクテキストのみ翻訳し、Markdown構造とURLは変更しない。
4) Markdownリンクの周囲に「」を付けない。ただし、外側の文法で必要な場合は除く。

スタイルより構造を優先する。
Markdownトークンが変更される場合は、日本語の自然さを最適化しない。

例
原文：This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解：本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り：本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->