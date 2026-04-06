# 「Other Courses」セクションの更新（Microsoft Beginnersリポジトリ）

このガイドは、Co‑op Translatorを使って「Other Courses」セクションを自動同期する方法と、全リポジトリに対するグローバルテンプレートの更新方法を説明します。

- 適用対象: Microsoft Beginnersリポジトリのみ
- 動作環境: Co‑op Translator CLIおよびGitHub Actions
- テンプレートソース: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## クイックスタート: リポジトリでの自動同期を有効にする

READMEの「Other Courses」セクションの周りに以下のマーカーを追加してください。Co‑op Translatorはこれらのマーカー間のすべてを毎回の実行時に置き換えます。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op TranslatorがCLI（例: `translate -l "<language codes>"`）やGitHub Actionsから実行されるたびに、このマーカーで囲まれた「Other Courses」セクションを自動的に更新します。

> [!NOTE]
> 既存のリストがある場合は、同じマーカーで囲むだけでかまいません。次回の実行時に最新の標準化された内容に置き換えられます。

---

## グローバルコンテンツの変更方法

すべてのBeginnersリポジトリに表示される標準化された内容を更新したい場合は、以下の手順に従ってください。

1. テンプレートを編集: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 変更内容をCo-op Translatorリポジトリにプルリクエストとして提出する
3. PRがマージされると、Co‑op Translatorのバージョンが更新される
4. 対象のリポジトリでCo‑op Translatorが次回（CLIまたはGitHub Action経由で）実行されると、更新されたセクションが自動的に同期される

これにより、「Other Courses」コンテンツがすべてのBeginnersリポジトリで一元管理されます。


## リポジトリのサイズ

翻訳対象の言語数が多いため、リポジトリサイズが大きくなることがあります。エンドユーザーが必要な言語のみをクローンするために、clone - sparseの使い方に関するガイダンスを提供しています。

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
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を利用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用によって生じたいかなる誤解や誤訳についても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->