---
title: Localizeflow を使い始める
description: Azure Localizeflow を使い始める方法のガイド
---

# Localizeflow を使い始める

Azure Localizeflow は、国際化とローカリゼーションのワークフローを合理化するために設計されたツールです。このガイドでは、基本的な設定方法と最初の PR（プルリクエスト）を作成する方法について説明します。

## 必要条件

- GitHub アカウント
- Azure DevOps アカウント (オプション)
- レポジトリへの書き込み権限

## セットアップ手順

1. レポジトリに [Localizeflow](https://github.com/Azure/localizeflow) GitHub App をインストールします。
2. `.github` フォルダーに `localizeflow.yml` 設定ファイルを作成し、プロジェクトのローカリゼーション設定を定義します。
3. 翻訳対象のファイルを指定し、サポートする言語をリストアップします。
4. 翻訳者とレビューアーを管理するための役割を割り当てます。

## 最初の PR の作成

1. 翻訳したいファイルを変更します。
2. 変更をコミットして、新しいブランチを作成します。
3. プルリクエストを作成すると、[Localizeflow](https://github.com/Azure/localizeflow) により自動的に翻訳レビューが開始されます。
4. レビュー完了後、PR をマージしてください。

詳細は [Localizeflow ドキュメント](https://aka.ms/localizeflow) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件採用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。對於因使用此翻譯而引起的任何誤解或誤譯，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->