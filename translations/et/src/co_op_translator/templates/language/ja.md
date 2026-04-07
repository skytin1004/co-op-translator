---
title: "Azure Kubernetes Service のセキュリティのベストプラクティス"
description: Azure Kubernetes Service クラスターを作成および保護するための推奨方法の概要。
ms.date: 07/01/2023
ms.topic: article
ms.custom: best-practice
---

# Azure Kubernetes Service のセキュリティのベストプラクティス

このドキュメントでは、Azure Kubernetes Service (AKS) クラスターを作成および保護するための推奨されるベストプラクティスの概要を説明します。

## ネットワーキング

- **ネットワークポリシーを有効にする**: ネットワークポリシーを使用して、Pod 間の通信を制限し、最小特権の原則をサポートします。
- **Azure CNI を使用する**: Azure CNI は、VNet 内のリソース間で IP アドレスを共有し、ネットワーク分離とセキュリティを改善します。
- **ネットワーク セキュリティ グループ (NSG) と Azure Firewall を使う**: トラフィックを制御し、悪意あるアクセスを防ぎます。

## セキュリティ構成

- **Azure Active Directory (AAD) 統合**: クラスターアクセス時のユーザー認証と権限管理を強化します。
- **Azure RBAC を使用する**: Kubernetes RBAC と組み合わせて、アクセス制御を細かく管理します。
- **Pod セキュリティ ポリシーの適用**: システムの安全性を維持するため、Pod が実行できる操作を制限します。

## ノードのセキュリティ

- **マネージド ノード プールの使用**: AKS のマネージド ノードプールによって、ノードのアップデートとパッチ管理を容易にします。
- **最小限の特権を持つコンテナの実行**: コンテナを root ユーザーで実行しないようにし、セキュリティリスクを軽減します。
- **ノードの自動アップグレードと自動スケールを有効にする**: 最新のセキュリティ更新を確実に適用します。

## 監視とロギング

- **Azure Monitor と Azure Log Analytics を活用**: クラスターの診断とセキュリティツールの統合によって、異常検出とトラブルシューティング効率を向上させます。
- **監査ログの有効化**: Kubernetes API サーバーの監査ログを有効にし、セキュリティインシデントを追跡します。

## セキュリティ更新とパッチ管理

- **定期的なクラスターのアップグレード**: AKS の最新バージョンに更新を行い、既知の脆弱性を防ぎます。
- **イメージのスキャンと管理**: コンテナイメージの脆弱性スキャンを行い、信頼できるイメージソースのみを使用します。

詳細については、[Azure Kubernetes Service セキュリティのベストプラクティス](https://learn.microsoft.com/azure/aks/operator-best-practices-security) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellekti tõlke teenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüdleme täpsuse poole, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->