---
title: "GitHub App での Localizeflow プルリクエストのレビュー流れ"
description: "GitHub App でのプルリクエストレビューとローカライズフローの統合方法について説明します。"
---

# GitHub App での Localizeflow プルリクエストのレビュー流れ

このドキュメントでは、GitHub App を使って Localizeflow のプルリクエスト（PR）を効率的にレビューする流れを説明します。

## 目的

- プルリクエストのレビューをレビューアーにとってわかりやすくする
- どのコメントや修正が Locaizeflow 由来かどうかを識別しやすくする
- レビュー作業の効率化

## 流れ概要

1. PR が作成されると、GitHub App が自動的に Localizeflow チェックを実行します。
2. チェック結果が PR にコメントとして表示されます。
3. レビュアーはコメントを確認し、必要に応じて修正コメントを返信します。
4. 修正が完了すると、再度チェックが走り結果が更新されます。

## 詳細

### チェックコメントの内容

- どのファイルのどの行に翻訳やローカライズの問題があるか
- 提案されている修正案
- [Co-op Translator](https://github.com/Azure/co-op-translator) を使った翻訳支援ツールのリンク

### コメントの区別

- Localizeflow が自動投稿したコメントは「ラベル」をつけて区別されています。
- レビュアーのコメントや議論とは混同されないようにするためです。

### 修正作業

- 修正は PR のブランチ上で行います。
- 修正後にコミット・プッシュすると、自動的にチェックが再実行されます。

## まとめ

GitHub App と Localizeflow の統合によって、レビュー作業がスムーズになり、翻訳品質の向上が期待できます。

不明点や要望があれば、[Co-op Translator](https://github.com/Azure/co-op-translator) の Issue またはリポジトリの連絡先までご連絡ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Hati ya kutamatisha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asilia katika lugha yake ya kale inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutoajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->