<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:29:54+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# Co-op Translator

_輕鬆自動化翻譯你的教育 GitHub 內容至多種語言，助你觸及全球用戶。_

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

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 支援

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯文](../ar/README.md) | [孟加拉文](../bn/README.md) | [保加利亞文](../bg/README.md) | [緬甸文](../my/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，香港）](./README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，台灣）](../tw/README.md) | [克羅地亞文](../hr/README.md) | [捷克文](../cs/README.md) | [丹麥文](../da/README.md) | [荷蘭文](../nl/README.md) | [愛沙尼亞文](../et/README.md) | [芬蘭文](../fi/README.md) | [法文](../fr/README.md) | [德文](../de/README.md) | [希臘文](../el/README.md) | [希伯來文](../he/README.md) | [印地文](../hi/README.md) | [匈牙利文](../hu/README.md) | [印尼文](../id/README.md) | [意大利文](../it/README.md) | [日文](../ja/README.md) | [韓文](../ko/README.md) | [立陶宛文](../lt/README.md) | [馬來文](../ms/README.md) | [馬拉地文](../mr/README.md) | [尼泊爾文](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威文](../no/README.md) | [波斯文](../fa/README.md) | [波蘭文](../pl/README.md) | [葡萄牙文（巴西）](../br/README.md) | [葡萄牙文（葡萄牙）](../pt/README.md) | [旁遮普文（果魯穆奇）](../pa/README.md) | [羅馬尼亞文](../ro/README.md) | [俄文](../ru/README.md) | [塞爾維亞文（西里爾字母）](../sr/README.md) | [斯洛伐克文](../sk/README.md) | [斯洛文尼亞文](../sl/README.md) | [西班牙文](../es/README.md) | [斯瓦希里文](../sw/README.md) | [瑞典文](../sv/README.md) | [他加祿語（菲律賓語）](../tl/README.md) | [泰米爾文](../ta/README.md) | [泰文](../th/README.md) | [土耳其文](../tr/README.md) | [烏克蘭文](../uk/README.md) | [烏爾都文](../ur/README.md) | [越南文](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 簡介

**Co-op Translator** 讓你可以快速將教育 GitHub 內容翻譯成多種語言，輕鬆觸及全球用戶。當你更新 Markdown 檔案、圖片或 Jupyter 筆記本時，翻譯會自動同步，確保你的教育內容對國際用戶保持新鮮和相關。

看看 Co-op Translator 如何組織翻譯後的教育 GitHub 內容：

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hk.png)

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

- 用範本建立 `.env`： [.env.template](../../.env.template)
- 設定一個 LLM 供應商（Azure OpenAI 或 OpenAI）
- 如需圖片翻譯（`-img`），同時設定 Azure AI Vision
- 建議：如果你有其他工具產生的翻譯，先清理（例如：`translations/`），避免衝突。
- 建議：在 README 加入翻譯語言區段，參考 [README 語言範本](./README_languages_template.md)
- 詳情請參考：[設置 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

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

更多參數： [指令參考](./getting_started/command-reference.md)

## 功能特色

- 自動翻譯 Markdown、筆記本及圖片
- 翻譯內容與原文變更保持同步
- 可本地（CLI）或 CI（GitHub Actions）運行
- 支援 Azure OpenAI 或 OpenAI；圖片可選用 Azure AI Vision
- 保持 Markdown 格式及結構

## 文件

- [命令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開倉庫及標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織倉庫及組織級設置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [支援語言列表](./getting_started/supported-languages.md)
- [疑難排解](./getting_started/troubleshooting.md)

## 支持我們，推動全球學習

一起推動教育內容全球分享的革新！歡迎到 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點個 ⭐，支持我們打破學習和科技的語言障礙。你的關注和貢獻非常重要！歡迎提交程式碼和功能建議。

### 探索 Microsoft 教育內容（多語言）

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

## 影片簡介

想了解 Co-op Translator？歡迎觀看我們的簡報影片 _(點擊下圖可在 YouTube 收看)_：

- **Open at Microsoft**：18 分鐘簡介及快速教學，帶你認識 Co-op Translator。

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hk.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻方式

本項目歡迎各方貢獻及建議。有興趣參與 Azure Co-op Translator？請參閱 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何協助我們令 Co-op Translator 更易用。

## 貢獻者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為守則

本項目採用 [Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/)。
詳情請參閱 [行為守則 FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
如有疑問或意見，請電郵 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 負責任的 AI

Microsoft 致力協助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並透過透明度說明及影響評估等工具建立信任。相關資源可於 [https://aka.ms/RAI](https://aka.ms/RAI) 查閱。
Microsoft 的負責任 AI 原則包括公平、可靠與安全、私隱與保安、包容、透明及問責。

大規模自然語言、圖像及語音模型（如本範例所用）有機會出現不公平、不可靠或冒犯行為，可能造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 了解相關風險及限制。

建議的風險緩解方法是於你的架構中加入安全系統，偵測及防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立保護層，可偵測應用程式及服務中的有害用戶或 AI 內容。Azure AI Content Safety 包括文字及圖像 API，助你偵測有害資料。我們亦有互動式 Content Safety Studio，讓你試用偵測不同類型有害內容的範例程式碼。以下 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 可指導你如何向服務發送請求。
另一個需要考慮的層面是整體應用程式的效能。對於多模態和多模型的應用程式來說，效能指的是系統能夠如你和用戶所期望般運作，包括不產生有害的輸出。評估整體應用程式的效能時，建議使用[生成品質及風險與安全性指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

你可以在開發環境中利用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)來評估你的 AI 應用程式。無論是測試數據集或目標，你的生成式 AI 應用程式的輸出都可以透過內建或自訂的評估器進行量化評分。想要開始使用 prompt flow sdk 來評估你的系統，可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，你可以[在 Azure AI Studio 視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本項目可能包含某些項目、產品或服務的商標或標誌。使用 Microsoft 商標或標誌必須遵守
[Microsoft 的商標及品牌指引](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本項目的修改版本中使用 Microsoft 商標或標誌時，不得造成混淆或暗示 Microsoft 的贊助。
任何第三方商標或標誌的使用，則需遵守該第三方的相關政策。

## 尋求協助

如果你在開發 AI 應用程式時遇到困難或有疑問，歡迎加入：

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

如果你有產品意見或在開發過程中遇到錯誤，請前往：

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始語言版本應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。因使用本翻譯而引起的任何誤解或錯誤，我們概不負責。