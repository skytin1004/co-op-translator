---
title: "Localizeflowを使ったPR（プルリクエスト）の自動翻訳"
description: "GitHub App「Localizeflow」によるPR自動翻訳の仕組みを説明しています。"
---

# Localizeflowを使ったPR（プルリクエスト）の自動翻訳

LocalizeflowはGitHub Appとして実装されており、以下のような流れでPRの翻訳を自動化しています。

## ワークフロー

1. PRで変更が加えられると、Localizeflowは自動的にトリガーされます。
2. 対象ファイルの更新を検知し、変更内容を抽出します。
3. 抽出したテキストを翻訳APIに送信して翻訳を取得します。
4. 翻訳結果を元に翻訳ファイルを更新します。
5. 翻訳結果を反映したPRコメントまたは別PRとして自動的に提案します。

## 使い方

1. GitHubリポジトリにLocalizeflowをインストールします。
2. `localizeflow.config.json` で翻訳対象と言語を設定します。
3. 翻訳したいテキストを含むPRを作成します。
4. Localizeflowが自動的に翻訳結果をPRに反映します。

> 詳細は[Localizeflowの公式ドキュメント](https://github.com/Azure/localizeflow)をご参照ください。

## メリット

- 手動の翻訳作業が不要になり、開発効率が向上します。
- プルリクエストのレビュー時間が短縮され、品質が向上します。
- 翻訳の一貫性が保たれやすくなります。

## 注意点

- 翻訳結果は機械翻訳のため、必ずネイティブチェックを行ってください。
- 特殊な用語はカスタム辞書での管理を推奨します。

以上のように、Localizeflowを活用することで、GitHub上での国際化対応が効率的に行えます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vrijwaring**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onjuistheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->