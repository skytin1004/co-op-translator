---
title: "GitHub Actions で Localizeflow を統合する"
description: "GitHub Actions を使用して Localizeflow プロジェクトを CI/CD ワークフローに統合する方法のガイド。"
---

# GitHub Actions で Localizeflow を統合する

Localizeflow は、GitHub Actions と統合して翻訳プロセスを自動化し、継続的に更新された翻訳ファイルを保つことをサポートします。このガイドでは、Localizeflow を使って GitHub リポジトリの CI/CD パイプラインに翻訳管理を組み込む基本的なステップを説明します。

## 前提条件

- GitHub と連携している Localizeflow アカウント
- 翻訳管理を組み込みたい GitHub リポジトリ
- ローカル環境に GitHub CLI が設定されていることが望ましい

## ワークフローの設定

1. `.github/workflows` フォルダに `localizeflow.yml` というファイルを作成します。

2. 以下は基本的な例です。必要に応じてステップや環境変数を調整してください。

```yaml
name: Localizeflow Translation Sync

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  sync-translations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16'

      - name: Install dependencies
        run: npm install

      - name: Sync translations with Localizeflow
        env:
          LOCALIZEFLOW_API_KEY: ${{ secrets.LOCALIZEFLOW_API_KEY }}
        run: npx localizeflow sync
```

## 重要ポイント

- `LOCALIZEFLOW_API_KEY` は GitHub シークレットとして設定してください。
- `npx localizeflow sync` コマンドは Localizeflow CLI で翻訳を同期します。

## 追加のカスタマイズ

- PR 作成時やマージ後に特定のスクリプトを実行することができます。
- ワークフローに通知やレビューリクエストの追加も可能です。

詳細については、Localizeflow の公式ドキュメントや GitHub Actions のドキュメントを参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feilfortolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->