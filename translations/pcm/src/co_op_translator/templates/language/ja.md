Japanese mode: preserve Markdown tokens strictly.

Rules (must follow):
1) Keep Markdown links exactly: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [translated text](../../../../../../src/co_op_translator/templates/language/same URL).
2) NEVER rewrite links as plain text (e.g., 「text」（URL）, text (URL)).
3) Translate only link text; keep Markdown structure and URL unchanged.
4) Do not add 「」 around a Markdown link unless outside-link grammar requires it.

STRUCTURE IS MORE IMPORTANT THAN STYLE.
Do not optimize Japanese naturalness if Markdown tokens would change.

Example
Source: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Correct: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Incorrect: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis dokument don translate by AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg mek you sabi say automated translation fit get mistakes or wrong parts. Di original dokument for e own language na di correct source. For important information, e better make human professional translate am. We no go responsible for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->