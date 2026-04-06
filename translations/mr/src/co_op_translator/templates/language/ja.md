Japanese mode: Markdown トークンを厳密に保持してください。

ルール（必ず守ること）：
1) Markdownリンクを正確に保持してください：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えてはいけません（例：「text」（URL）, text (URL)）。
3) リンクテキストのみを翻訳し、Markdownの構造とURLは変更しないでください。
4) Markdownリンクの周りに「」を付けてはいけません。ただし外部リンクの文法上必要な場合を除きます。

構造はスタイルよりも重要です。
Markdownトークンが変わる場合は日本語の自然さを最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
不正解: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**तपशील**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असताना, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा असमर्थता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती साठी व्यावसायिक मानवी भाषांतर शिफारस केली जाते. या भाषांतराच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थाच्या दायित्व आम्ही घेत नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->