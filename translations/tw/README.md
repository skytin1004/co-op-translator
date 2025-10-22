<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:31:02+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# Co-op Translator

_輕鬆自動化翻譯你的教育 GitHub 內容到多種語言，讓全球用戶都能輕鬆接觸。_

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

### 🌐 多語言支援

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 提供

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](./README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 簡介

**Co-op Translator** 讓你能夠快速將教育性 GitHub 內容翻譯成多種語言，輕鬆觸及全球用戶。當你更新 Markdown 檔案、圖片或 Jupyter 筆記本時，翻譯會自動同步，確保你的教育內容始終新穎且適合國際使用者。

看看 Co-op Translator 如何組織翻譯後的教育 GitHub 內容：

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.tw.png)

## 快速開始

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

Docker：

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最簡設置

- 使用範本建立 `.env`： [.env.template](../../.env.template)
- 設定一個 LLM 供應商（Azure OpenAI 或 OpenAI）
- 若要翻譯圖片（`-img`），也要設定 Azure AI Vision
- 建議：如果你有其他工具產生的翻譯，先清理它們以避免衝突（例如：`translations/`）。
- 建議：在你的 README 加入翻譯語言區塊，參考 [README 語言範本](./README_languages_template.md)
- 參考：[設定 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方式

翻譯所有支援類型：

```bash
translate -l "ko ja"
```

只翻譯 Markdown：

```bash
translate -l "de" -md
```

Markdown + 圖片：

```bash
translate -l "pt" -md -img
```

只翻譯筆記本：

```bash
translate -l "zh" -nb
```

更多參數：[指令參考](./getting_started/command-reference.md)

## 功能特色

- 自動翻譯 Markdown、筆記本和圖片
- 翻譯內容會隨原始檔案變動自動同步
- 可在本地（CLI）或 CI（GitHub Actions）執行
- 支援 Azure OpenAI 或 OpenAI；圖片可選用 Azure AI Vision
- 保留 Markdown 格式與結構

## 文件

- [命令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開倉庫與標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織倉庫與組織層級設置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [支援語言列表](./getting_started/supported-languages.md)
- [疑難排解](./getting_started/troubleshooting.md)

## 支持我們，推動全球學習

邀請你一起改變教育內容的全球分享方式！歡迎在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點個 ⭐，支持我們打破學習與科技的語言障礙。你的關注與貢獻都很重要！歡迎提供程式碼貢獻與功能建議。

### 探索你語言的 Microsoft 教育內容

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

## 影片簡報

想更了解 Co-op Translator？歡迎觀看我們的簡報影片（點擊下方圖片可在 YouTube 觀看）：

- **Open at Microsoft**：18 分鐘簡介，快速教你如何使用 Co-op Translator。

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.tw.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻方式

本專案歡迎各種貢獻與建議。想參與 Azure Co-op Translator 的開發嗎？請參考 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何協助我們讓 Co-op Translator 更易用。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
更多資訊請參考 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
有任何問題與意見請聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 負責任的 AI

Microsoft 致力於協助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並透過透明說明與影響評估等工具建立信任。相關資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 的負責任 AI 原則包括公平性、可靠與安全、隱私與安全、包容性、透明度與問責。

大規模自然語言、影像與語音模型（如本範例所用）有可能出現不公平、不可靠或冒犯性行為，可能造成傷害。請參考 [Azure OpenAI 服務透明說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相關風險與限制。

建議的風險緩解方式是，在你的架構中加入安全系統，偵測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能偵測應用程式與服務中的有害用戶或 AI 產生內容。Azure AI Content Safety 包含文字與圖片 API，可偵測有害內容。我們也有互動式 Content Safety Studio，讓你可以瀏覽、探索並試用偵測各種型態有害內容的範例程式碼。以下 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 可協助你開始使用該服務。
另一個需要考慮的面向是整體應用程式效能。對於多模態和多模型的應用程式來說，效能指的是系統能夠如你和你的使用者所預期地運作，包括不產生有害的輸出。評估整體應用程式的效能時，建議參考[生成品質以及風險與安全性指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

你可以在開發環境中利用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 來評估你的 AI 應用程式。無論是使用測試資料集或目標，你的生成式 AI 應用程式都能透過內建或自訂的評估器進行量化評量。若要開始使用 prompt flow sdk 來評估你的系統，可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，你可以[在 Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。經授權使用 Microsoft
商標或標誌時，必須遵守
[Microsoft 商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本專案的修改版本中使用 Microsoft 商標或標誌時，不得造成混淆或暗示 Microsoft 贊助。
任何第三方商標或標誌的使用，則需遵循該第三方的相關政策。

## 尋求協助

如果你在開發 AI 應用程式時遇到困難或有任何問題，歡迎加入：

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

如果你有產品回饋或在開發過程中遇到錯誤，請前往：

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。