# 「Other Courses」セクションの更新（Microsoft Beginnersリポジトリ）

このガイドでは、Co‑op Translatorを使用して「Other Courses」セクションを自動同期する方法と、すべてのリポジトリに対するグローバルテンプレートの更新方法を説明します。

- 適用対象：Microsoft Beginnersリポジトリのみ
- 対応ツール：Co‑op Translator CLIおよびGitHub Actions
- テンプレートのソース：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## クイックスタート：リポジトリでの自動同期を有効にする

READMEの「Other Courses」セクションの周りに以下のマーカーを追加してください。Co‑op Translatorはこれらのマーカー間のすべてを毎回の実行時に置き換えます。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op TranslatorはCLI（例：`translate -l "<language codes>"`）またはGitHub Actions経由で実行されるたびに、これらのマーカーで囲まれた「Other Courses」セクションを自動的に更新します。

> [!NOTE]
> すでにリストがある場合は、同じマーカーで囲むだけです。次回の実行時に最新の標準化された内容に置き換えられます。

---

## グローバルコンテンツの変更方法

すべてのBeginnersリポジトリに表示される標準化コンテンツを更新したい場合は：

1. テンプレートを編集：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 変更を含むプルリクエストをCo-op Translatorリポジトリに送る
3. PRがマージされるとCo‑op Translatorのバージョンが更新される
4. 変更後、ターゲットリポジトリでCo‑op Translator（CLIまたはGitHub Action）が次回実行されると、更新済みのセクションが自動で同期される

これにより、すべてのBeginnersリポジトリにおける「Other Courses」コンテンツの単一の信頼できる情報源が確保されます。


## リポジトリサイズ

翻訳対象の言語数によりリポジトリが大きくなる可能性があります。エンドユーザーが必要な言語のみをクローンできるように、`clone - sparse` の使用ガイダンスを提供しています。

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されました。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文の母国語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳については責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->