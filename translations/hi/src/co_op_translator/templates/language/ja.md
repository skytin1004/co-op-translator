Japanese mode: Markdown トークンを厳密に保持します。

ルール（必ず守ること）：
1) Markdownリンクは正確に保持すること：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストとして書き換えないこと（例：「text」（URL）、text (URL)）。
3) リンクテキストのみを翻訳し、Markdown構造やURLは変更しないこと。
4) 外部リンクの文法上必要な場合を除き、Markdownリンクの周囲に「」を付けないこと。

構造はスタイルよりも重要です。
Markdownトークンが変わる場合は日本語の自然さを最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
不正解: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या असंगतताएं हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। हम इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या अन्य व्याख्याओं के लिए जवाबदेह नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->