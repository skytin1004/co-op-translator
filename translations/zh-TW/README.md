# Co-op Translator

_輕鬆自動化並維護您教育性 GitHub 內容的多語言翻譯，隨著專案演進同步更新。_

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

### 🌐 多語言支援

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 提供支援

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文（簡體）](../zh-CN/README.md) | [中文（繁體，香港）](../zh-HK/README.md) | [中文（繁體，澳門）](../zh-MO/README.md) | [中文（繁體，台灣）](./README.md) | [克羅埃西亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (法爾西語)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../pt-BR/README.md) | [葡萄牙語（葡萄牙）](../pt-PT/README.md) | [旁遮普語（古圖赫文）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語（菲律賓語）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **想要本地複製嗎？**
>
> 此儲存庫包含 50 多種語言的翻譯，會大幅增加下載大小。若想不含翻譯進行複製，請使用稀疏檢出：
>
> **Bash / macOS / Linux：**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD（Windows）：**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 這樣您可以快速下載並取得完成課程所需的所有內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概述

**Co-op Translator** 幫助您輕鬆將教育性 GitHub 內容本地化為多種語言。  
當您更新 Markdown 檔案、圖片或筆記本時，翻譯會自動同步，確保您的內容對全球學習者始終準確且最新。

翻譯內容如何組織示例：

![Example](../../translated_images/zh-TW/translation-ex.0c8aa6a7ee0aad2b.webp)

## 翻譯狀態管理方式

Co-op Translator 將翻譯內容視為<strong>版本化的軟體工件</strong>，  
而非靜態檔案。

此工具透過<strong>語言範圍的元資料</strong>來追蹤翻譯的 Markdown、圖片與筆記本檔案狀態。

此設計讓 Co-op Translator 可：

- 可靠地偵測過時翻譯
- 一致地處理 Markdown、圖片與筆記本檔案
- 在大型、快速變動且多語言的儲存庫中安全擴展

透過把翻譯建模為受控工件，  
翻譯工作流程自然符合現代軟體依賴及工件管理實務。

→ [翻譯狀態管理詳情](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速入門

```bash
# 建立並啟用虛擬環境（建議）
python -m venv .venv
# Windows 作業系統
.venv\Scripts\activate
# macOS/Linux 作業系統
source .venv/bin/activate
# 安裝套件
pip install co-op-translator
# 翻譯
translate -l "ko ja fr" -md
```

Docker:

```bash
# 從 GHCR 拉取公開映像檔
docker pull ghcr.io/azure/co-op-translator:latest
# 以當前資料夾掛載並提供 .env 執行（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最簡配置

1. 確認您擁有支援的 Python 版本（目前支持 3.10-3.12）。在 poetry (pyproject.toml) 會自動處理。
2. 使用範本創建 `.env` 檔案：[.env.template](../../.env.template)
3. 配置一個 LLM 供應商（Azure OpenAI 或 OpenAI）
4. （選用）若需圖片翻譯（`-img`），配置 Azure AI Vision
5. （選用）您可以通過複製變數並加上後綴如 `_1`、`_2` 等來配置多組認證。每組變數須共用相同後綴。
6. （推薦）清理之前翻譯以避免衝突（例如 `translations/`）
7. （推薦）使用 [README 語言範本](./getting_started/README_languages_template.md) 為 README 新增翻譯區段
8. 參見：[設定 Azure AI](./getting_started/set-up-azure-ai.md)

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

更多參數：請參考 [指令參考](./getting_started/command-reference.md)

## 功能特色

- 自動翻譯 Markdown、筆記本與圖片
- 隨原始內容變動同步翻譯
- 可本地使用（CLI）或持續整合（GitHub Actions）
- 支援 Azure OpenAI、OpenAI；圖片選用 Azure AI Vision
- 保留 Markdown 格式與結構

## 文件

- [命令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公共儲存庫與標準祕密）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（微軟組織儲存庫與組織層級設置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 語言範本](./getting_started/README_languages_template.md)
- [支援語言](./getting_started/supported-languages.md)
- [貢獻指南](./CONTRIBUTING.md)
- [疑難排解](./getting_started/troubleshooting.md)

### 微軟專屬指南
> [!NOTE]
> 僅供微軟 “For Beginners” 儲存庫的維護者參考。

- [更新“其他課程”清單（僅限 MS Beginners 儲存庫）](./getting_started/update-other-courses.md)

## 支持我們，促進全球學習

加入我們，改變全球教育內容的分享方式！請在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 送出 ⭐，支持我們打破學習與科技的語言障礙使命。您的關注與貢獻將帶來巨大影響！歡迎提供程式碼貢獻與功能建議。

### 以您的語言探索微軟教育內容

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

## 影片簡報

👉 點擊下方圖片於 YouTube 觀看。

- **Open at Microsoft**：18 分鐘簡短介紹與 Co-op Translator 使用快速指南。

  [![Open at Microsoft](../../translated_images/zh-TW/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

歡迎提出貢獻與建議。想為 Azure Co-op Translator 貢獻？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md) 指引，了解如何協助讓 Co-op Translator 更容易被更多人使用。

## 貢獻者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請參閱 [行為準則常見問答](https://opensource.microsoft.com/codeofconduct/faq/) 或
聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出其他問題或意見。

## 負責任的 AI

Microsoft 致力於協助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並透過透明度說明與影響評估等工具建立基於信任的合作關係。許多相關資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 的負責任 AI 方法建基於我們的 AI 原則：公平性、可靠與安全、隱私與安全性、包容性、透明度及問責制。

大型自然語言、圖像及語音模型——如本範例中使用的模型——可能會有不公平、不可靠或冒犯性的行為，進而造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 了解風險與局限。

建議的風險減緩方法是在架構中包含安全系統，能偵測並阻止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立防護層，能偵測應用程式與服務中的用戶生成及 AI 生成有害內容。Azure AI Content Safety 包含文字與影像 API，協助偵測有害素材。我們也提供互動式 Content Safety Studio，讓您檢視、探索並試用偵測不同模態有害內容的範例程式碼。以下的 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 將引導您如何向服務發出請求。

另一個需注意的面向是整體應用程式效能。對於多模態及多模型應用程式，我們認為效能意指系統的表現符合您和使用者的預期，包括不產生有害輸出。評估整體應用效能時，請使用 [生成品質與風險安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以在開發環境使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 評估您的 AI 應用。不論是測試資料集或目標，生成式 AI 應用的結果都可用內建或自訂評估器進行量化評測。要開始使用 prompt flow sdk 評估系統，請參照 [快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在 [Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。經授權使用 Microsoft
商標或標誌需依照並遵守
[Microsoft 商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在修改版本中使用 Microsoft 商標或標誌時，不能造成混淆或暗示 Microsoft 的贊助。
任何第三方商標或標誌的使用，皆須遵守該第三方的政策。

## 尋求協助

如果您遇到困難或對建置 AI 應用有任何疑問，請加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在建置過程中有產品反饋或錯誤回報，請前往：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於保持準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言版本文件應視為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用本翻譯內容而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->