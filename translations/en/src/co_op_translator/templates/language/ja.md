---
title: Localizeflow を使用した Azure アプリの翻訳と公開
description: GitHub App 形式の Localizeflow を使った Azure アプリの翻訳プロセスの紹介
---

# Localizeflow を使用した Azure アプリの翻訳と公開

このドキュメントでは、GitHub 上の Azure アプリに対して [Localizeflow] という GitHub App を使って翻訳を自動化し、翻訳された内容をどのように公開するかを説明します。

## 前提

- アプリは GitHub リポジトリにあります
- Localizeflow GitHub App がリポジトリにインストールされています
- 翻訳は PR を通じて管理されます

## 流れ

1. 原文の更新や新機能の追加に伴い、source ファイルをリポジトリにコミット
2. Localizeflow が自動的にそれを検知し、翻訳 PR を作成
3. 翻訳者やレビュワーが PR を確認・編集
4. PR がマージされると翻訳済みのコンテンツが本番に反映

## メリット

- 翻訳と開発のサイクルがシームレス
- Azure アプリの公開内容が常に最新の状態に保たれる
- 翻訳の管理が GitHub 上で完結し利便性が高い

## 参考リンク

- [Localizeflow GitHub App](https://github.com/marketplace/localizeflow)
- [Azure アプリ開発ドキュメント](https://docs.microsoft.com/azure/app-service/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->