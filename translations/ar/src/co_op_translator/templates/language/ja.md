```markdown
日本語モード: Markdownトークンを厳密に保持します。

ルール（必須遵守）：
1) Markdownリンクはそのまま維持：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクを通常の文章表記に書き換えない（例: 「text」（URL）, text (URL)）。
3) リンクテキストのみ翻訳し、Markdownの構造とURLは変更しない。
4) 外部リンク文法が不要の場合、Markdownリンクの周りに「」を付けない。

構造は自然な表現より重要です。
Markdownトークンが変更される場合は日本語の自然さを最適化しないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة أو المهمة، يوصى بالاعتماد على الترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->