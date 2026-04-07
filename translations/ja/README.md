# Co-op Translator

_教育用GitHubコンテンツの多言語翻訳を、プロジェクトの進展に合わせて簡単に自動化・維持できます。_

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
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

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) によるサポート

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](./README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ローカルでクローンしたいですか？**
>
> このリポジトリには50以上の言語翻訳が含まれており、ダウンロードサイズが大幅に増加します。翻訳を含めずにクローンするには、スパースチェックアウトを使用してください:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> これにより、より高速なダウンロードでコース完了に必要なすべてが手に入ります。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概要

**Co-op Translator** は、教育用GitHubコンテンツを多言語に簡単にローカライズする手助けをします。  
Markdownファイル、画像、ノートブックを更新すると、翻訳も自動的に同期され、世界中の学習者に正確で最新のコンテンツを提供します。

翻訳済みコンテンツの例の構成:

![Example](../../translated_images/ja/translation-ex.0c8aa6a7ee0aad2b.webp)

## 翻訳状態の管理方法

Co-op Translatorは翻訳済みコンテンツを<strong>バージョン管理されたソフトウェアアーティファクト</strong>として管理し、  
静的なファイルとしてではありません。

このツールは<strong>言語ごとのメタデータ</strong>を用いて、翻訳されたMarkdown、画像、ノートブックの状態を追跡します。

この設計によりCo-op Translatorは以下を可能にします：

- 古くなった翻訳の確実な検出
- Markdown、画像、ノートブックを一貫して扱う
- 大規模で迅速に動く多言語リポジトリに安全にスケール

翻訳を管理されたアーティファクトとしてモデル化することで、  
翻訳ワークフローは最新のソフトウェアの依存関係管理やアーティファクト管理のプラクティスに自然に合致します。

→ [翻訳状態の管理方法](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## クイックスタート

```bash
# 仮想環境を作成して有効化する（推奨）
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# パッケージをインストールする
pip install co-op-translator
# 翻訳する
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCRからパブリックイメージを取得する
docker pull ghcr.io/azure/co-op-translator:latest
# カレントフォルダをマウントし、.envを提供して実行する（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小セットアップ

1. 対応しているPythonのバージョン（現在は3.10-3.12）を確認します。poetry (pyproject.toml) では自動的に対応します。
2. テンプレート [.env.template](../../.env.template) を使用して `.env` ファイルを作成します。
3. LLMプロバイダー（Azure OpenAIまたはOpenAI）を1つ設定します。
4. （オプション）画像翻訳（`-img`）の場合はAzure AI Visionを設定します。
5. （オプション）複数の資格情報セットを設定したい場合は、`_1`、`_2`などのサフィックスを付けて変数を複製します。セット内のすべての変数は同じサフィックスを共有する必要があります。
6. （推奨）競合を防ぐために前回の翻訳（例：`translations/`）をクリーンアップします。
7. （推奨）READMEに翻訳セクションを追加するために [README languages template](./getting_started/README_languages_template.md) を使用します。
8. 詳細は: [Azure AIのセットアップ](./getting_started/set-up-azure-ai.md)

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

詳細なフラグ: [コマンド参照](./getting_started/command-reference.md)

## 特徴

- Markdown、ノートブック、画像の自動翻訳
- ソースの変更に同期して翻訳を維持
- ローカル (CLI) およびCI (GitHub Actions)で動作
- Azure OpenAIやOpenAIを使用、画像にはオプションでAzure AI Vision
- Markdownの書式と構造を保持

## ドキュメント

- [コマンドラインガイド](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions ガイド（公開リポジトリ＆標準シークレット）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions ガイド（Microsoft組織リポジトリ＆組織レベルセットアップ）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README言語テンプレート](./getting_started/README_languages_template.md)
- [対応言語一覧](./getting_started/supported-languages.md)
- [貢献について](./CONTRIBUTING.md)
- [トラブルシューティング](./getting_started/troubleshooting.md)

### Microsoft専用ガイド
> [!NOTE]
> Microsoft「初心者向け」リポジトリのメンテナー向け。

- [「その他のコース」一覧の更新（MS初心者リポジトリ専用）](./getting_started/update-other-courses.md)

## 私たちをサポートし、グローバル学習を促進しましょう

教育コンテンツの世界的な共有方法を変革する私たちに参加しませんか？  
[Co-op Translator](https://github.com/azure/co-op-translator) にGitHubで⭐を付けて、学習と技術の言語の壁を打ち破る私たちのミッションを支援してください。皆さんの関心と貢献が大きな力になります！コードの貢献や機能提案もいつでも歓迎です。

### Microsoftの教育コンテンツをあなたの言語で探索

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [.NETで学ぶ生成AI 初心者向け](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Javaで学ぶ生成AI 初心者向け](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ビデオプレゼンテーション

👉 以下の画像をクリックするとYouTubeで視聴できます。

- **Open at Microsoft**: Co-op Translatorの簡単な18分間の紹介とクイックガイド。

  [![Open at Microsoft](../../translated_images/ja/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢献について

このプロジェクトでは貢献や提案を歓迎しています。Azure Co-op Translatorに貢献したい方は、[CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。Co-op Translator をより使いやすくするためにあなたも手助けできます。

## 貢献者一覧
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行動規範

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) を採用しています。
詳細については [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) をご覧いただくか、
ご質問やご意見がある場合は [opencode@microsoft.com](mailto:opencode@microsoft.com) までご連絡ください。

## 責任あるAI

Microsoftは、お客様が当社のAI製品を責任を持って使用できるよう支援し、学びを共有し、Transparency NotesやImpact Assessmentsなどのツールを通じて信頼に基づくパートナーシップを構築することに取り組んでいます。これらの多くのリソースは [https://aka.ms/RAI](https://aka.ms/RAI) にてご覧いただけます。  
Microsoftの責任あるAIへのアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任というAIの原則に根ざしています。

このサンプルで使用されているような大規模な自然言語、画像、音声モデルは、不公平、不確実、または不快な動作を示す可能性があり、結果として害を及ぼすことがあります。リスクや制限については、[Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) をご参照ください。

これらのリスクを軽減する推奨される方法は、害を及ぼす行動を検出・防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) は、アプリケーションやサービス内のユーザー生成コンテンツやAI生成コンテンツの害を検出できる独立した保護レイヤーを提供します。Azure AI Content Safetyはテキストおよび画像APIを含み、有害な素材を検出することができます。また、異なるモダリティにわたる有害コンテンツの検出サンプルコードを表示、探索、試すことができるインタラクティブなContent Safety Studioも提供しています。以下の [クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) では、サービスへのリクエストの方法を案内しています。

別の考慮すべき点として、アプリケーション全体のパフォーマンスがあります。マルチモーダルかつマルチモデルのアプリケーションでは、パフォーマンスとは、システムがあなたやユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。[生成品質およびリスクと安全性の指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) を使用して、全体のアプリケーションのパフォーマンスを評価することが重要です。

開発環境でAIアプリケーションを評価するには、[prompt flow SDK](https://microsoft.github.io/promptflow/index.html) を使うことができます。テストデータセットまたは目標を指定すると、生成型AIアプリケーションの生成物は組み込み評価器または任意のカスタム評価器で定量的に測定されます。prompt flow sdkでシステム評価を開始するには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) に従ってください。評価実行を完了すると、[Azure AI Studioで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) できます。

## 商標

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。  
Microsoftの商標やロゴの使用は [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。  
本プロジェクトの変更版においてMicrosoftの商標やロゴを使用する場合、混同やMicrosoftのスポンサーシップを示唆しないようにしてください。  
第三者の商標やロゴの使用は、それら第三者のポリシーに従う必要があります。

## ヘルプを得るには

もし行き詰まったり、AIアプリ構築の質問がある場合は、以下に参加してください：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

製品のフィードバックや構築中のエラーがある場合は、こちらをご利用ください：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれている可能性があります。原文の言語で記載された元の文書が正式な情報源とみなされるべきです。重要な情報については、専門の人翻訳を推奨します。本翻訳の使用に起因するいかなる誤解や誤訳についても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->