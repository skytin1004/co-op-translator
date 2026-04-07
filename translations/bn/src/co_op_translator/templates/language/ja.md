Japanese mode: マークダウンのトークンを厳密に保持します。

ルール（必ず従ってください）：
1) マークダウンリンクは正確に保持します：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えないでください（例：「text」（URL）、text (URL)など）。
3) リンクのテキスト部分のみ翻訳し、マークダウンの構造とURLは変更しないでください。
4) マークダウンリンクに「」をつけないでください。ただし、リンク外の文法上必要な場合は除く。

構造はスタイルよりも重要です。
マークダウントークンが変わる場合は日本語の自然な表現の最適化を行わないでください。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正しい例: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤った例: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই ডকুমেন্টটি AI অনুবাদ সার্ভিস [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকা সম্ভব। মূল ডকুমেন্টটি তার নিজস্ব ভাষায় অগ্রহণযোগ্য উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারের কারণে কোনও ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->