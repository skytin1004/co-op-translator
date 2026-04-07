# Co-op Translator

_輕鬆自動化並維護您的教育 GitHub 內容在多語言間的翻譯，隨著專案演進。_

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
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文（簡體）](../zh-CN/README.md) | [中文（繁體，香港）](../zh-HK/README.md) | [中文（繁體，澳門）](../zh-MO/README.md) | [中文（繁體，臺灣）](./README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (Farsi)](../fa/README.md) | [波蘭語](../pl/README.md) | [巴西葡萄牙語](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [旁遮普語 (Gurmukhi)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾字母)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛維尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **偏好本機克隆？**
>
> 本儲存庫包含 50+ 語言翻譯，會顯著增加下載大小。若想不包含翻譯地克隆，請使用稀疏簽出：
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
> 此方式提供您完成課程所需的全部內容，且下載速度更快。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概覽

**Co-op Translator** 幫助您輕鬆將教育 GitHub 內容本地化成多種語言。  
當您更新 Markdown 檔案、影像或筆記本時，翻譯會自動同步，確保您的內容對全球學習者保持正確且最新。

翻譯內容組織範例如下：

![Example](../../imgs/translation-ex.png)

## 如何管理翻譯狀態

Co-op Translator 將翻譯內容視為 <strong>版本化軟體產物</strong>，  
而非靜態檔案。

此工具透過 <strong>語言範圍的元資料</strong>，追蹤翻譯的 Markdown、影像及筆記本狀態。

此設計讓 Co-op Translator 能夠：

- 可靠偵測過期翻譯
- 對 Markdown、影像與筆記本採取一致處理
- 安全地擴展用於大型、快速變動、多語言的儲存庫

透過將翻譯建模為管理中的產物，  
翻譯工作流程自然符合現代軟體的依賴性與產物管理實務。

→ [如何管理翻譯狀態](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速開始

```bash
# 建立並啟動虛擬環境（建議）
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
# 從 GHCR 拉取公共映像檔
docker pull ghcr.io/azure/co-op-translator:latest
# 以當前資料夾掛載並提供 .env 運行（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小設定

1. 確認您使用的是受支援的 Python 版本（目前是 3.10-3.12）。在 poetry (pyproject.toml) 中會自動處理。
2. 使用範本 [.env.template](../../.env.template) 建立 `.env` 檔案
3. 配置一組 LLM 提供者（Azure OpenAI 或 OpenAI）
4. （選擇性）對於影像翻譯 (`-img`)，配置 Azure AI Vision
5. （選擇性）您可以透過添加變數後綴如 `_1`、`_2` 等複製多組認證。每組變數必須擁有相同後綴。
6. （建議）清除先前翻譯結果以避免衝突（例如 `translations/`）
7. （建議）使用 [README 語言範本](./getting_started/README_languages_template.md) 在您的 README 新增翻譯區塊
8. 參考：[設置 Azure AI](./getting_started/set-up-azure-ai.md)

## 用法

翻譯所有支援的類型：

```bash
translate -l "ko ja"
```

僅翻譯 Markdown：

```bash
translate -l "de" -md
```

Markdown + 影像：

```bash
translate -l "pt" -md -img
```

僅翻譯筆記本：

```bash
translate -l "zh" -nb
```

更多參數說明：[指令參考](./getting_started/command-reference.md)

## 功能

- 自動翻譯 Markdown、筆記本和影像
- 保持翻譯與來源變動同步
- 可在本機 (CLI) 或 CI (GitHub Actions) 執行
- 使用 Azure OpenAI 或 OpenAI；影像翻譯可選用 Azure AI Vision
- 保留 Markdown 格式與結構

## 文件

- [指令列使用指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開儲存庫及標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織儲存庫與組織層設定）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 語言範本](./getting_started/README_languages_template.md)
- [支援語言](./getting_started/supported-languages.md)
- [貢獻指南](./CONTRIBUTING.md)
- [疑難排解](./getting_started/troubleshooting.md)

### Microsoft 專屬指南
> [!NOTE]
> 僅供 Microsoft “For Beginners” 儲存庫管理者使用。

- [更新「其他課程」清單（僅限 Microsoft 初學者儲存庫）](./getting_started/update-other-courses.md)

## 支持我們，促進全球學習

加入我們，一同革新教育內容在全球的分享方式！  
在 GitHub 上為 [Co-op Translator](https://github.com/azure/co-op-translator) 點讚並支持我們打破學習與科技語言障礙的使命。  
您的關注與貢獻將帶來重大影響！歡迎程式碼貢獻與功能建議。

### 以您的語言探索 Microsoft 教育內容

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

## 影音簡介

👉 點擊下方圖片於 YouTube 收看。

- **Open at Microsoft**：簡短18分鐘介紹與快速指南，教您如何使用 Co-op Translator。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

本專案歡迎貢獻與建議。有興趣為 Azure Co-op Translator 貢獻者，請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md) 指南，了解如何協助讓 Co-op Translator 更加普及。

## 貢獻者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案已採用 [Microsoft 開放原始碼行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請參閱 [行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/)，或聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出任何其他問題或意見。

## 負責任的 AI

微軟致力協助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並通過 Transparency Notes 和 Impact Assessments 等工具建立基於信任的合作夥伴關係。許多此類資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
微軟的負責任 AI 方針基於我們的 AI 原則：公平性、可靠性與安全性、隱私與安全性、包容性、透明性及問責制。

大型自然語言、影像及語音模型——如本範例中所使用的——可能會出現不公平、不可靠或冒犯性的行為，進而造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相關風險與限制。

建議緩解此類風險的方法是在架構中加入安全系統，偵測及防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供一層獨立防護，能夠在應用程式與服務中偵測有害的使用者生成及 AI 生成內容。Azure AI Content Safety 包括文字與影像 API，讓您能偵測有害內容。我們還有一個互動式 Content Safety Studio，可讓您檢視、探索並試用偵測不同樣態有害內容的範例程式碼。以下[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)將指引您如何向服務發送請求。

另一個需要考慮的面向是整體應用程式效能。對於多模態與多模型應用程式，我們視效能為系統按您與使用者預期運作，包含不產生有害輸出。使用[產生品質以及風險安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)對您的整體應用進行評估，十分重要。

您可使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 在開發環境中評估您的 AI 應用。無論是測試資料集或目標，生成的 AI 結果皆可用內建評估器或自訂評估器進行量化衡量。若要開始使用 prompt flow sdk 評估系統，請參閱[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在[Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。授權使用微軟商標或標誌需遵守並遵循[微軟商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在修改本專案版本中使用微軟商標或標誌，必須避免造成混淆或暗示微軟贊助。
任何第三方商標或標誌的使用，皆須遵守該第三方的政策。

## 尋求協助

如果遇到困難或對於建立 AI 應用有任何疑問，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

若您有產品回饋或在建置過程中發現錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所導致的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->