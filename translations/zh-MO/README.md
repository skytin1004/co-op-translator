# Co-op Translator

_輕鬆自動化並維護您在教育 GitHub 內容的多語言翻譯，隨著您的專案發展保持最新。_

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
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [簡體中文](../zh-CN/README.md) | [繁體中文 (香港)](../zh-HK/README.md) | [繁體中文 (澳門)](./README.md) | [繁體中文 (臺灣)](../zh-TW/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (Farsi)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語 (巴西)](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [潘加比語 (Gurmukhi)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾文)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語 (菲律賓語)](../tl/README.md) | [坦米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **想要優先本地複製？**
>
> 本倉庫包含超過 50 種語言的翻譯，會大幅增加下載大小。若要複製不帶翻譯的版本，請使用稀疏簽出：
>
> **Bash / macOS / Linux：**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows)：**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 這樣您就能以更快的速度下載，獲得完成課程所需的所有內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概覽

**Co-op Translator** 幫助您輕鬆地將教育 GitHub 內容本地化成多種語言。  
當您更新 Markdown 文件、圖片或筆記本時，翻譯內容會自動同步，確保您的內容對全球學習者保持準確且最新。

翻譯內容組織示例：

![Example](../../translated_images/zh-MO/translation-ex.0c8aa6a7ee0aad2b.webp)

## 如何管理翻譯狀態

Co-op Translator 將翻譯內容視為具有版本控制的<strong>軟體組件</strong>，  
而非靜態檔案。

此工具使用<strong>語言範圍的元資料</strong>追蹤翻譯 Markdown、圖片和筆記本的狀態。

此設計使 Co-op Translator 能夠：

- 穩健偵測過時的翻譯
- 統一處理 Markdown、圖片與筆記本
- 安全擴展到大型快速變動且多語言的資訊庫

透過將翻譯模擬為受管控的組件，  
翻譯工作流程自然與現代軟體依賴和組件管理方法對齊。

→ [如何管理翻譯狀態](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速開始

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
# 從 GHCR 拉取公共映像檔
docker pull ghcr.io/azure/co-op-translator:latest
# 掛載當前資料夾並提供 .env 執行（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小設定

1. 確認您擁有受支援的 Python 版本（目前為 3.10-3.12）。在 poetry (pyproject.toml) 中會自動處理。
2. 使用範本建立 `.env` 文件： [.env.template](../../.env.template)
3. 配置一個 LLM 供應者（Azure OpenAI 或 OpenAI）
4. （選擇性）針對圖片翻譯（`-img`）配置 Azure AI Vision
5. （選擇性）可透過後綴如 `_1`、`_2` 複製變數組來配置多組憑證。每組變數必須共享相同後綴。
6. （建議）清理先前翻譯以避免衝突（例如 `translations/`）
7. （建議）在您的 README 中新增翻譯區段，使用 [README languages template](./getting_started/README_languages_template.md)
8. 參考：[設定 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

翻譯所有支援類型：

```bash
translate -l "ko ja"
```

僅 Markdown：

```bash
translate -l "de" -md
```

Markdown + 圖片：

```bash
translate -l "pt" -md -img
```

僅筆記本：

```bash
translate -l "zh" -nb
```

更多參數：[指令參考](./getting_started/command-reference.md)

## 功能特色

- 自動翻譯 Markdown、筆記本及圖片
- 讓翻譯與原始內容變更保持同步
- 可本地使用（CLI）或在 CI（GitHub Actions）中執行
- 使用 Azure OpenAI 或 OpenAI；圖片可選用 Azure AI Vision
- 保留 Markdown 格式與結構

## 文件

- [命令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開專案與標準機密）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織專案與組織級設定）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 語言模板](./getting_started/README_languages_template.md)
- [支援語言](./getting_started/supported-languages.md)
- [貢獻指南](./CONTRIBUTING.md)
- [疑難排解](./getting_started/troubleshooting.md)

### 微軟專屬指南
> [!NOTE]
> 僅適用於 Microsoft “初學者”系列專案的維護者。

- [更新「其他課程」清單（僅限 MS 初學者專案）](./getting_started/update-other-courses.md)

## 支持我們，共促全球學習

加入我們，革新全球教育內容分享方式！給予 [Co-op Translator](https://github.com/azure/co-op-translator) GitHub 一顆 ⭐，支持我們打破學習與科技的語言障礙。您的關注與貢獻將帶來深遠影響！歡迎代碼貢獻與功能建議。

### 探索不同語言的微軟教育內容

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

## 影片簡介

👉 點擊下方圖片於 YouTube 觀看。

- **Open at Microsoft** ：18 分鐘簡短介紹及快速指南，教您如何使用 Co-op Translator。

  [![Open at Microsoft](../../translated_images/zh-MO/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

本專案歡迎貢獻與建議。想要為 Azure Co-op Translator 貢獻嗎？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md) 以瞭解如何協助讓 Co-op Translator 更易於使用。

## 貢獻者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為準則

此項目已採用 [Microsoft 開放原始碼行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲知更多資訊，請參閱 [行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/) 或
聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出其他問題或意見。

## 負責任的 AI

微軟致力於協助我們的客戶負責任地使用 AI 產品，分享我們的學習，並透過 Transparancy Notes 和 Impact Assessments 等工具建立基於信任的夥伴關係。許多此類資源可於 [https://aka.ms/RAI](https://aka.ms/RAI) 取得。
微軟對負責任 AI 的方法基於我們的 AI 原則，包括公平性、可靠性與安全性、隱私與安全性、包容性、透明度以及問責制。

大型自然語言、影像和語音模型（如本範例中使用的模型）可能會以不公平、不可靠或冒犯性的方式表現，從而造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ，了解風險和限制。

建議採取的風險緩解方法是在您的架構中包含一個安全系統，能夠檢測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能偵測應用程式和服務中用戶生成及 AI 生成的有害內容。Azure AI Content Safety 包含文字及影像 API，允許您偵測有害素材。我們同時提供互動式 Content Safety Studio，可讓您檢視、探索並試用跨不同模態偵測有害內容的範例程式碼。下列 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 導引您如何向服務發送請求。

另一個需要考慮的面向是整體應用程式效能。對於多模態和多模型的應用程式，我們認為效能代表系統按您和使用者的期望運作，包括不產生有害輸出。評估整體應用程式效能時，請參考 [生成質量以及風險與安全度量](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以在開發環境中使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 評估 AI 應用程式。無論是測試資料集或目標，您的生成式 AI 應用程式輸出均可透過內建評估器或您自訂的評估器量化衡量。若要開始使用 prompt flow sdk 來評估您的系統，您可以參考 [快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在 [Azure AI Studio 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。授權使用微軟商標或標誌須遵守
[微軟商標及品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
對本專案修改版中使用微軟商標或標誌，不得引起混淆或暗示微軟贊助。
任何第三方商標或標誌的使用均須遵守該第三方的政策。

## 獲取協助

如遇困難或有關於建置 AI 應用程式的任何問題，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如在建置過程中有產品反饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯所得。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。對於因使用此翻譯所引起的任何誤解或誤釋，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->