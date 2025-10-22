<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T11:56:11+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Co-op Translator

_教育用のGitHubコンテンツを自動で多言語に翻訳し、世界中のユーザーに届けることができます。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 多言語対応

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) がサポートする言語

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](./README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概要

**Co-op Translator** を使えば、教育用のGitHubコンテンツを素早く多言語に翻訳し、世界中のユーザーに簡単に届けることができます。Markdownファイルや画像、Jupyterノートブックを更新すると、翻訳も自動で同期されるので、国際的なユーザー向けに常に最新のコンテンツを提供できます。

Co-op Translatorがどのように翻訳コンテンツを整理するかはこちら：

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ja.png)

## クイックスタート

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Dockerの場合:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小限のセットアップ

- テンプレート [.env.template](../../.env.template) を使って `.env` を作成
- LLMプロバイダー（Azure OpenAI または OpenAI）を1つ設定
- 画像翻訳（`-img`）を使う場合は Azure AI Vision も設定
- 推奨: 他のツールで生成した翻訳がある場合は、競合を避けるために事前に整理してください（例: `translations/`）。
- 推奨: READMEに [README languages template](./README_languages_template.md) を使って翻訳セクションを追加
- 詳細: [Azure AI のセットアップ](./getting_started/set-up-azure-ai.md)

## 使い方

すべての対応タイプを翻訳:

```bash
translate -l "ko ja"
```

Markdownのみ:

```bash
translate -l "de" -md
```

Markdown＋画像:

```bash
translate -l "pt" -md -img
```

ノートブックのみ:

```bash
translate -l "zh" -nb
```

その他のフラグ: [コマンドリファレンス](./getting_started/command-reference.md)

## 特長

- Markdown、ノートブック、画像の自動翻訳
- ソースの変更に合わせて翻訳を自動で同期
- ローカル（CLI）でもCI（GitHub Actions）でも利用可能
- Azure OpenAIまたはOpenAIを使用、画像にはオプションでAzure AI Vision
- Markdownの書式や構造を維持

## ドキュメント

- [コマンドラインガイド](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actionsガイド（パブリックリポジトリ＆標準シークレット）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actionsガイド（Microsoft組織リポジトリ＆組織レベル設定）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [対応言語一覧](./getting_started/supported-languages.md)
- [トラブルシューティング](./getting_started/troubleshooting.md)

## サポートとグローバル学習の推進

教育コンテンツのグローバルな共有を一緒に進めましょう！ [Co-op Translator](https://github.com/azure/co-op-translator) にGitHubで⭐をつけて、学習や技術の言語の壁をなくす活動を応援してください。皆さんの関心や貢献が大きな力になります。コードの貢献や機能提案も大歓迎です。

### Microsoftの教育コンテンツをあなたの言語で

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 動画プレゼンテーション

Co-op Translatorについて、プレゼン動画で詳しく学べます _(下の画像をクリックするとYouTubeで視聴できます)_:

- **Open at Microsoft**: Co-op Translatorの概要と使い方を18分で紹介しています。

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ja.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## コントリビューション

このプロジェクトは貢献や提案を歓迎しています。Azure Co-op Translatorへの貢献に興味がある方は、[CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。より多くの人が使いやすくなるよう、ぜひご協力ください。

## コントリビューター

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行動規範

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) を採用しています。
詳細は [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) をご覧いただくか、
ご質問やご意見は [opencode@microsoft.com](mailto:opencode@microsoft.com) までご連絡ください。

## 責任あるAI

Microsoftは、お客様がAI製品を責任を持って利用できるよう支援し、学びを共有し、透明性のあるパートナーシップを築くことに取り組んでいます。Transparency NotesやImpact Assessmentsなどのツールを通じて、これらのリソースの多くは [https://aka.ms/RAI](https://aka.ms/RAI) でご覧いただけます。
Microsoftの責任あるAIへの取り組みは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任というAI原則に基づいています。

このサンプルで使われているような大規模な自然言語・画像・音声モデルは、不公平・信頼性の欠如・不快な挙動を示す可能性があり、結果として有害な影響を及ぼすことがあります。リスクや制限については [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) をご確認ください。

これらのリスクを軽減するためには、有害な挙動を検知・防止できる安全システムをアーキテクチャに組み込むことが推奨されます。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) は、ユーザー生成・AI生成コンテンツの有害性を検知できる独立した保護レイヤーを提供します。Azure AI Content Safetyには、テキストと画像のAPIがあり、有害なコンテンツを検知できます。また、Content Safety Studioでは、さまざまなモダリティで有害コンテンツ検知のサンプルコードを試すことができます。サービスへのリクエスト方法は、[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) をご参照ください。
もう一つ考慮すべき点は、アプリケーション全体のパフォーマンスです。マルチモーダルやマルチモデルのアプリケーションでは、パフォーマンスとは、システムがあなたやユーザーの期待通りに動作し、有害な出力を生成しないことも含まれます。アプリケーション全体のパフォーマンスは、[生成品質やリスク・安全性の指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使って評価することが重要です。

AIアプリケーションは、開発環境で[Prompt Flow SDK](https://microsoft.github.io/promptflow/index.html)を使って評価できます。テストデータセットやターゲットを指定すると、生成AIアプリケーションの出力は、組み込みの評価ツールや独自の評価ツールで定量的に測定されます。Prompt Flow SDKを使ってシステム評価を始めるには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)を参考にしてください。評価を実行した後は、[Azure AI Studioで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)できます。

## 商標について

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの正規の使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。
このプロジェクトの改変版でMicrosoftの商標やロゴを使用する場合、混乱を招いたり、Microsoftが後援していると誤解されるような使い方はしないでください。
第三者の商標やロゴの使用については、それぞれの第三者のポリシーに従ってください。

## ヘルプを得るには

AIアプリの開発で困ったことや質問がある場合は、以下に参加してください：

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

製品に関するフィードバックや、開発中にエラーが発生した場合は、以下をご利用ください：

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。