---
title: Localizeflow を使用して GitHub のプルリクエストを自動的にローカライズする
description: Azure Pipelines ではなく GitHub App を使用して GitHub のプルリクエスト（PR）を自動的にローカライズする方法に関するガイドです。
---

# Localizeflow を使用して GitHub のプルリクエストを自動的にローカライズする

このドキュメントでは、デフォルトの Azure Pipelines ではなく [Localizeflow GitHub App](https://github.com/marketplace/localizeflow) を使用して GitHub リポジトリ内でプルリクエスト（PR）をローカライズする方法について説明します。

## 概要

- [Localizeflow GitHub App](https://github.com/marketplace/localizeflow) を GitHub リポジトリにインストールします。
- App は PR イベントをトリガーとして検出します。
- App は PR で変更されたファイルから翻訳されていないリソース文字列を抽出します。
- App は翻訳プロバイダーを呼び出して翻訳を取得します。
- App は翻訳された文字列で新しいコミットを PR に追加します。

## インストール

1. [Localizeflow GitHub App ページ](https://github.com/marketplace/localizeflow) にアクセスします。
2. 「インストール」をクリックし、ローカライズしたいリポジトリを選択します。
3. インストールを完了します。

## 設定

- App は `localizeflow.yaml` 設定ファイルを必要とします。リポジトリのルートに配置してください。
- 設定ファイルには以下を含めます:
  - 翻訳対象ファイルのパターン
  - ターゲット言語
  - 使用する翻訳プロバイダーの設定

例:

```yaml
sources:
  - path: "resources/*.resx"
    languages: [ "ja", "fr", "de" ]

providers:
  azure:
    apiKey: ${{ secrets.AZURE_TRANSLATOR_KEY }}
```

## 使い方

- PR を作成または更新すると、Localizeflow が自動的に実行され、ローカライズされていない文字列を検出および翻訳します。
- 翻訳結果は同じ PR に新しいコミットとして追加されます。

## メリット

- Azure Pipelines を使わずに GitHub のみで完結します。
- PR ごとに最新の変更を自動的にローカライズ。
- 翻訳ワークフローが簡素化されます。

詳細は [Localizeflow ドキュメント](https://localizeflow.com/docs) をご覧ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->