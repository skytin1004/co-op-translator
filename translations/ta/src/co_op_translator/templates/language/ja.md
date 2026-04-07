Japanese mode: Markdown トークンを厳密に保持してください。

ルール（必ず守ること）:
1) Markdown リンクはそのまま保持すること: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じ URL)。
2) リンクをプレーンテキストとして書き換えないこと（例：「text」（URL）、text (URL)）。
3) リンクテキストのみを翻訳し、Markdown の構造と URL は変更しないこと。
4) Markdown リンクの周りに「」を付けないこと。外部リンクの文法が必要とする場合を除く。

構造はスタイルよりも重要です。
Markdown トークンが変わる場合は、日本語の自然さを最適化しないこと。

例
元の文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**வெறுப்புமInd தடையான்**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழி பெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டது. நமக்கு துல்லியம் முக்கியமானது என்றாலும், தன்னிச்சையான மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதைக் கவனத்தில் கொள்ளவும். உள்ளூர் மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கின்றோம். இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதில் ஏற்படும் எந்த தவறான புரிதல்களுக்கோ அல்லது தவறான பொருளடக்கங்களுக்கோ நாங்கள் பொறுப்பு இல்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->