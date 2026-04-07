# Co-op Translator

_教育用のGitHubコンテンツの翻訳を、プロジェクトの進化に合わせて複数言語で簡単に自動化・維持できます。_

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

> **ローカルでクローンすることを希望されますか？**
>
> このリポジトリには50以上の言語の翻訳が含まれており、ダウンロードサイズが大幅に増加します。翻訳なしでクローンするにはスパースチェックアウトを使用してください：
>
> **Bash/macOS/Linux:**
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
> これにより、コースを完了するために必要なすべてのものをより速いダウンロードで入手できます。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概要

**Co-op Translator** は、教育用GitHubコンテンツを複数の言語に簡単にローカライズするためのツールです。  
Markdownファイル、画像、ノートブックを更新すると、翻訳が自動的に同期され、世界中の学習者に向けて正確かつ最新のコンテンツを提供できます。

翻訳されたコンテンツの整理例:

![Example](../../imgs/translation-ex.png)

## 翻訳状態の管理方法

Co-op Translatorは翻訳されたコンテンツを<strong>バージョン管理されたソフトウェアアーティファクト</strong>として管理し、  
静的ファイルとして扱いません。

ツールは翻訳済みMarkdown、画像、ノートブックの状態を  
<strong>言語スコープのメタデータ</strong>で追跡します。

この設計によりCo-op Translatorは以下を実現します：

- 古くなった翻訳の確実な検出
- Markdown、画像、ノートブックを一貫して扱う
- 大規模かつ高速で多言語に対応するリポジトリで安全にスケール

翻訳を管理されたアーティファクトとしてモデル化することで、  
翻訳ワークフローは最新のソフトウェア依存関係およびアーティファクト管理のプラクティスと自然に整合します。

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
# GHCRから公開イメージをプルする
docker pull ghcr.io/azure/co-op-translator:latest
# 現在のフォルダをマウントし、.envを提供して実行する（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小構成

1. サポートされているPythonバージョン（現在3.10-3.12）があることを確認してください。poetry（pyproject.toml）では自動的に処理されます。
2. テンプレートを使って `.env` ファイルを作成します: [.env.template](../../.env.template)
3. 1つのLLMプロバイダー（Azure OpenAIまたはOpenAI）を設定します
4. （オプション）画像翻訳 (`-img`) の場合はAzure AI Visionを設定します
5. （オプション）複数の認証情報セットを設定したい場合は、変数に `_1`、`_2` などのサフィックスを付けて複製します。セット内のすべての変数は同じサフィックスである必要があります。
6. （推奨）競合を避けるために以前の翻訳をクリーンアップします（例: `translations/`）
7. （推奨）READMEに翻訳セクションを追加します。テンプレートは [README languages template](./getting_started/README_languages_template.md) を参照してください
8. 参照： [Azure AIの設定](./getting_started/set-up-azure-ai.md)

## 使い方

対応するすべてのタイプを翻訳:

```bash
translate -l "ko ja"
```

Markdownのみ:

```bash
translate -l "de" -md
```

Markdown+画像:

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
- ソースの変更に合わせて翻訳を同期
- ローカル(CLI)またはCI(GitHub Actions)で動作
- Azure OpenAIまたはOpenAIを使用。画像にはオプションでAzure AI Visionを使用
- Markdownのフォーマットと構造を保持

## ドキュメント

- [コマンドラインガイド](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actionsガイド（公開リポジトリと標準シークレット）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actionsガイド（Microsoft組織リポジトリと組織レベルのセットアップ）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README言語テンプレート](./getting_started/README_languages_template.md)
- [対応言語一覧](./getting_started/supported-languages.md)
- [コントリビューション](./CONTRIBUTING.md)
- [トラブルシューティング](./getting_started/troubleshooting.md)

### Microsoft向けガイド
> [!NOTE]
> Microsoft「For Beginners」リポジトリのメンテナ向けのみ。

- [“他のコース”リストの更新方法（MS Beginnersリポジトリ専用）](./getting_started/update-other-courses.md)

## 私たちを支援し、グローバルな学習を促進しましょう

教育コンテンツのグローバル共有の革新にぜひご参加ください！[Co-op Translator](https://github.com/azure/co-op-translator) にGitHubで⭐をつけて、学習やテクノロジーの言語の壁を打ち破るミッションを応援してください。皆さんの関心と貢献が大きな影響をもたらします！コードの貢献や機能提案も大歓迎です。

### Microsoft教育コンテンツをあなたの言語で探検

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
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

## ビデオプレゼンテーション

👉 下の画像をクリックしてYouTubeで視聴してください。

- **Open at Microsoft**：Co-op Translatorの使い方を簡単に紹介する18分間のビデオ。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## コントリビューション

このプロジェクトは貢献や提案を歓迎します。Azure Co-op Translatorへの貢献に興味がある方は、ガイドラインについて [CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。Co-op Translatorをよりアクセスしやすいものにするための方法が記載されています。

## コントリビューター
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行動規範

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) を採用しています。
詳細については [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) を参照するか、追加の質問やコメントについては [opencode@microsoft.com](mailto:opencode@microsoft.com) にお問い合わせください。

## Responsible AI

Microsoft は、お客様が AI 製品を責任を持って使用できるよう支援し、知見を共有し、Transparency Notes や Impact Assessments などのツールを通じて信頼に基づくパートナーシップを構築することにコミットしています。これらの多くのリソースは [https://aka.ms/RAI](https://aka.ms/RAI) で確認できます。
Microsoft の Responsible AI への取り組みは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、および説明責任という AI 原則に基づいています。

このサンプルで使用されているような大規模な自然言語、画像、音声モデルは、不公平、信頼性に欠ける、または不快な振る舞いをする可能性があり、それが害をもたらすことがあります。リスクや制限については、[Azure OpenAI サービス Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) をご確認ください。

これらのリスクを軽減するために推奨されるアプローチは、害を及ぼす行動を検出し防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) は、アプリケーションやサービス内で有害なユーザー生成および AI 生成コンテンツを検出できる独立した保護層を提供します。Azure AI Content Safety は、テキストと画像の API を含み、有害な内容の検出を可能にします。さらに、異なるモダリティの有害コンテンツ検出のサンプルコードを閲覧、探索、試用できるインタラクティブな Content Safety Studio も提供しています。以下の [クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) では、サービスへのリクエスト方法を案内しています。

考慮すべきもう一つの側面は、全体的なアプリケーションのパフォーマンスです。マルチモーダルおよびマルチモデルのアプリケーションでは、パフォーマンスとは、システムがユーザーの期待どおりに動作し、有害な出力を生成しないことを意味すると考えています。アプリケーション全体のパフォーマンスを [生成品質およびリスク・安全性メトリクス](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) を使って評価することが重要です。

開発環境で AI アプリケーションを評価するには、[prompt flow SDK](https://microsoft.github.io/promptflow/index.html) を使用できます。テストデータセットやターゲットを用いて、生成型 AI アプリケーションの生成結果が組み込み評価器や任意のカスタム評価器で定量的に測定されます。prompt flow sdk を使ったシステム評価の開始には、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) を参照してください。評価の実行後は、[Azure AI Studio で結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) することができます。

## 商標

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoft の商標やロゴの許可された使用は [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。
このプロジェクトの修正版で Microsoft の商標やロゴを使用する場合、混乱を生じさせたり Microsoft の後援を示唆したりしてはなりません。
第三者の商標やロゴの使用については、それら第三者の規約が適用されます。

## ヘルプを得る

AI アプリの構築でつまずいたり質問がある場合は、以下に参加してください：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

製品フィードバックや開発中のエラーについては以下を訪問してください：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文のネイティブ言語での文書が正式な情報源とみなされます。重要な情報については専門の人間翻訳をご利用いただくことを推奨します。本翻訳の利用によるいかなる誤解や解釈違いについても当方は一切責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->