# Co-op Translator

_輕鬆自動化並維護您的教育性 GitHub 內容在多種語言中的翻譯，隨著您的專案持續發展。_

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

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 支援

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (緬甸)](../my/README.md) | [中文 (簡體)](../zh-CN/README.md) | [中文 (繁體，香港)](./README.md) | [中文 (繁體，澳門)](../zh-MO/README.md) | [中文 (繁體，台灣)](../zh-TW/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (法爾西語)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語 (巴西)](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [旁遮普語 (固魯米奇文)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾字母)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛維尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **想本機複製嗎？**
>
> 此儲存庫包含超過 50 種語言的翻譯，因此顯著增加下載大小。 若要在不包含翻譯的情況下複製，請使用稀疏檢出：
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
> 這讓您能以更快的速度下載所需的全部內容，完成課程。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概覽

**Co-op Translator** 幫助您輕鬆將教育性 GitHub 內容本地化至多種語言。  
當您更新 Markdown 檔案、圖片或筆記本時，翻譯會自動保持同步，確保您的內容對全球學習者保持準確及最新。

翻譯內容組織範例：

![Example](../../imgs/translation-ex.png)

## 翻譯狀態管理方式

Co-op Translator 將翻譯內容管理為 <strong>有版本的軟體工件</strong>，  
而非靜態檔案。

該工具使用 <strong>語言範圍的元資料</strong> 追蹤翻譯 Markdown、圖片和筆記本的狀態。

這種設計讓 Co-op Translator 能：

- 可靠地偵測過期翻譯
- 一致性地處理 Markdown、圖片與筆記本
- 安全地擴展至大型快速變動的多語言儲存庫

透過將翻譯建模為受管理的工件，  
翻譯工作流程可更自然地與現代的軟體依賴及工件管理實踐相結合。

→ [翻譯狀態管理方式介紹](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速開始

```bash
# 建立並啟動虛擬環境（建議使用）
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
# 從 GHCR 拉取公共映像
docker pull ghcr.io/azure/co-op-translator:latest
# 以掛載當前資料夾並提供 .env 方式運行（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小設定

1. 確認您擁有受支援的 Python 版本（目前是 3.10-3.12）。在 poetry（pyproject.toml）中會自動處理。
2. 使用範本建立 `.env` 檔案： [.env.template](../../.env.template)
3. 配置一個 LLM 供應商（Azure OpenAI 或 OpenAI）
4. （選用）針對圖片翻譯 (`-img`)，設定 Azure AI Vision
5. （選用）您可以透過副本變數並加上 `_1`、`_2` 等後綴來配置多組認證集合。集合中的所有變數必須使用相同的後綴。
6. （建議）清理之前的所有翻譯以避免衝突（例如 `translations/`）
7. （建議）使用 [README 語言範本](./getting_started/README_languages_template.md) 在您的 README 中新增翻譯區塊
8. 參考： [設定 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方式

翻譯所有支援的檔案類型：

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

更多指令參數： [指令參考](./getting_started/command-reference.md)

## 特色

- 自動翻譯 Markdown、筆記本與圖片
- 翻譯與原始內容變更自動同步
- 可本機執行（CLI）或於 CI (GitHub Actions) 中運行
- 支援 Azure OpenAI 或 OpenAI；可選用 Azure AI Vision 處理圖片
- 保留 Markdown 格式及結構

## 文件

- [指令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開儲存庫與標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織儲存庫與組織級設定）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 語言範本](./getting_started/README_languages_template.md)
- [支援的語言](./getting_started/supported-languages.md)
- [貢獻指南](./CONTRIBUTING.md)
- [疑難排解](./getting_started/troubleshooting.md)

### Microsoft 專屬指南
> [!NOTE]
> 僅供維護 Microsoft “For Beginners” 系列儲存庫者使用。

- [更新 “其他課程” 清單（僅限 MS Beginners 系列儲存庫）](./getting_started/update-other-courses.md)

## 支持我們，共促全球學習

加入我們，一起革新教育內容的全球分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點讚⭐，支持我們打破學習與科技領域的語言障礙使命。您的關注和貢獻帶來重大影響！歡迎您提供程式碼貢獻與功能建議。

### 探索 Microsoft 教育內容的多種語言版本

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

👉 點擊下方圖片於 YouTube 觀賞。

- **Open at Microsoft：** 18 分鐘簡介影片，快速指南如何使用 Co-op Translator。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

本專案歡迎所有貢獻與意見。想要參與 Azure Co-op Translator 的開發嗎？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何協助讓 Co-op Translator 更易取得。

## 貢獻者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

此專案已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請參閱 [行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/) 或
聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 以獲得更多問題或意見。

## 負責任的 AI

Microsoft 致力協助我們的客戶負責任地使用 AI 產品，分享我們的經驗，並透過 Transparency Notes 和 Impact Assessments 等工具建立基於信任的合作夥伴關係。許多這些資源皆可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 負責任的 AI 方法以我們的 AI 原則為基礎，包括公平性、可靠性與安全性、隱私和安全性、包容性、透明性與問責性。

大型自然語言、影像與語音模型——如本示例中使用的模型——可能會表現出不公平、不可靠或冒犯的行為，從而造成傷害。請查閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解風險與限制。

緩解這些風險的建議方法是將安全系統納入架構中，以便偵測和防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能在應用程式和服務中偵測有害的使用者產生及 AI 產生內容。Azure AI Content Safety 包含文本和影像 API，可讓您偵測有害內容。我們還有一個互動式的 Content Safety Studio，允許您查看、探索並嘗試跨多模態偵測有害內容的範例程式碼。以下的 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 導引您如何向服務發送請求。

另一個需考量的面向是整體應用程式的效能。對於多模態和多模型應用，我們認為效能是指系統達到您和使用者的預期表現，包括不產生有害輸出。評估您整體應用的效能時，非常重要的是使用 [生成品質與風險和安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以透過 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 在開發環境中評估您的 AI 應用。無論是測試資料集或目標，您的生成式 AI 應用產出都會透過內建或您選擇的自訂評估器進行定量衡量。若要開始使用 prompt flow sdk 評估系統，請參考 [快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可在 [Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含項目、產品或服務的商標或標誌。授權使用 Microsoft
商標或標誌需遵守並遵循
[Microsoft 的商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
修改版本專案中使用 Microsoft 商標或標誌不得引起混淆或暗示 Microsoft 贊助。
任何第三方商標或標誌的使用皆須遵守相關第三方政策。

## 尋求協助

如果您遇到困難或對建立 AI 應用有任何疑問，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

若您在建立過程中有產品反饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 自動翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->