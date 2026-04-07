# Co-op Translator

_輕鬆自動化並維護您的教育 GitHub 內容在多語言間的翻譯，隨著您的專案演進。_

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
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](./README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **偏好本機 Clone？**
>
> 此儲存庫包含超過 50 種語言的翻譯資料，會大幅增加下載大小。若要不帶翻譯克隆，請使用稀疏檢出：
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
> 這樣您可以更快速地下載完成課程所需的全部內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概觀

**Co-op Translator** 幫助您輕鬆將教育 GitHub 內容本地化成多種語言。  
當您更新 Markdown 檔案、圖片或筆記本時，翻譯將自動保持同步，確保您的內容對全球學習者都保持準確且最新。

翻譯內容組織範例：

![Example](../../imgs/translation-ex.png)

## 如何管理翻譯狀態

Co-op Translator 將翻譯過的內容當作 <strong>版本化軟體成果物</strong> 管理，  
而非靜態檔案。

此工具使用 <strong>語言範圍的元資料</strong> 追蹤翻譯的 Markdown、圖片和筆記本的狀態。

此設計讓 Co-op Translator 可以：

- 可靠地偵測過時的翻譯
- 一致地對待 Markdown、圖片和筆記本
- 安全地擴展至大型快速變動的多語言儲存庫

透過將翻譯建模為受控的成果物，  
翻譯工作流程自然與現代軟體依賴及成果物管理實務相符。

→ [如何管理翻譯狀態](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速開始

```bash
# 建立及啟動虛擬環境（建議使用）
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
# 以掛載當前資料夾及提供 .env 的方式運行（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小設置

1. 確認您擁有支援的 Python 版本（目前為 3.10-3.12）。在 poetry（pyproject.toml）中會自動處理。
2. 使用範本建立 `.env` 檔案： [.env.template](../../.env.template)
3. 配置一個 LLM 提供者（Azure OpenAI 或 OpenAI）
4. （可選）若要進行圖片翻譯（`-img`），配置 Azure AI Vision
5. （可選）您可以透過複製變數並加上後綴（如 `_1`、`_2` 等）配置多組憑證。每組變數必須使用相同後綴。
6. （建議）清理先前的翻譯以避免衝突（例如 `translations/`）
7. （建議）使用 [README 語言範本](./getting_started/README_languages_template.md) 將翻譯區塊新增到您的 README
8. 參見：[設定 Azure AI](./getting_started/set-up-azure-ai.md)

## 用法

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

## 功能

- 自動翻譯 Markdown、筆記本和圖片
- 保持翻譯與來源變更同步
- 可本機使用（CLI）或自動化流程中（GitHub Actions）
- 使用 Azure OpenAI 或 OpenAI；圖片可選用 Azure AI Vision
- 保留 Markdown 格式與結構

## 文件

- [指令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開儲存庫 & 標準密鑰）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（微軟組織儲存庫 & 組織級別設定）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 語言範本](./getting_started/README_languages_template.md)
- [支援語言](./getting_started/supported-languages.md)
- [貢獻指南](./CONTRIBUTING.md)
- [疑難排解](./getting_started/troubleshooting.md)

### Microsoft 專屬指南
> [!NOTE]
> 僅限 Microsoft 「For Beginners」儲存庫維護者。

- [更新「其他課程」清單（僅限 MS Beginners 儲存庫）](./getting_started/update-other-courses.md)

## 支援我們並促進全球學習

與我們一起革命化教育內容的全球分享方式！請在 GitHub 上為 [Co-op Translator](https://github.com/azure/co-op-translator) 點 ⭐，支持我們推動打破語言障礙的學習與科技使命。您的關注與貢獻將產生重大影響！歡迎貢獻程式碼與功能建議。

### 用您的語言探索 Microsoft 教育內容

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

## 影音簡報

👉 點擊下方圖片於 YouTube 觀看。

- **Open at Microsoft**：18 分鐘簡短介紹與快速教學，示範如何使用 Co-op Translator。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

此專案歡迎貢獻與建議。想參與 Azure Co-op Translator 的開發嗎？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md) 指引，了解如何協助讓 Co-op Translator 更加容易使用。

## 貢獻者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

本專案已採用[Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲瞭解更多資訊，請參閱[行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/)，或聯絡[opencode@microsoft.com](mailto:opencode@microsoft.com)提出任何額外的問題或意見。

## 負責任的 AI

Microsoft 致力於協助客戶負責任地使用我們的 AI 產品，分享我們的學習成果，並透過像是透明度說明與影響評估等工具建立基於信任的夥伴關係。許多相關資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 取得。
Microsoft 負責任 AI 的方法基於我們的 AI 原則：公平性、可靠性與安全性、隱私與安全、包容性、透明度及問責制。

大型的自然語言、影像與語音模型——如本範例中所使用者——可能會展現不公平、不可靠或冒犯性的行為，進而造成傷害。請參考[Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)以了解風險與限制。

建議採用的風險緩解方法是在您的架構中包含安全系統，能夠偵測並防止有害行為。[Azure AI 內容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能夠偵測應用程式和服務中的有害使用者產生及 AI 產生內容。Azure AI 內容安全包含文字和影像 API，可讓您偵測有害素材。我們也有提供互動式的內容安全工作室，讓您檢視、探索並試用針對不同模式偵測有害內容的範例程式碼。以下[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)將指導您如何向服務發出請求。

另一個要考慮的層面是整體應用程式的效能。對於多模態和多模型應用程式，我們認為效能是指系統如您及您的使用者所預期般執行，包括不產生有害輸出。評估整體應用效能時，重要的是使用[產生品質與風險及安全指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)在開發環境中評估您的 AI 應用程式。無論是測試資料集或目標，您的生成式 AI 應用的結果都可以用內建評估器或您選擇的自訂評估器量化。要開始使用 prompt flow SDK 評估您的系統，您可以參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。一旦執行評估流程，您可以在[Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。授權使用 Microsoft
商標或標誌必須遵循
[Microsoft 的商標與品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本專案修改版本中使用 Microsoft 商標或標誌不得造成混淆或暗示 Microsoft 贊助。
任何第三方商標或標誌的使用均須遵守該第三方的政策。

## 獲得協助

若您遇到困難或有任何有關建立 AI 應用的問題，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

若您在開發過程中有產品回饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。對因使用本翻譯而產生之任何誤解或誤釋，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->