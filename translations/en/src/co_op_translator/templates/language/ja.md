English mode: preserve Markdown tokens strictly.

Rules (must follow):
1) Keep Markdown links exactly: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [translated text](../../../../../../src/co_op_translator/templates/language/same URL).
2) NEVER rewrite links as plain text (e.g., “text” (URL), text (URL)).
3) Translate only link text; keep Markdown structure and URL unchanged.
4) Do not add quotation marks around a Markdown link unless outside-link grammar requires it.

STRUCTURE IS MORE IMPORTANT THAN STYLE.
Do not optimize English naturalness if Markdown tokens would change.

Example
Source: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Correct: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Incorrect: This document uses “Co-op Translator” (https://github.com/Azure/co-op-translator).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->