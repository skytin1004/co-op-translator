# Co-op Translator

_輕鬆自動化並維護您的教育 GitHub 內容多語言翻譯，隨著您的專案演進。_

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

#### 支援由 [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯文](../ar/README.md) | [孟加拉文](../bn/README.md) | [保加利亞文](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文 (簡體)](../zh-CN/README.md) | [中文 (繁體, 香港)](./README.md) | [中文 (繁體, 澳門)](../zh-MO/README.md) | [中文 (繁體, 台灣)](../zh-TW/README.md) | [克羅地亞文](../hr/README.md) | [捷克文](../cs/README.md) | [丹麥文](../da/README.md) | [荷蘭文](../nl/README.md) | [愛沙尼亞文](../et/README.md) | [芬蘭文](../fi/README.md) | [法文](../fr/README.md) | [德文](../de/README.md) | [希臘文](../el/README.md) | [希伯來文](../he/README.md) | [印地文](../hi/README.md) | [匈牙利文](../hu/README.md) | [印尼文](../id/README.md) | [義大利文](../it/README.md) | [日文](../ja/README.md) | [坎納達文](../kn/README.md) | [高棉語](../km/README.md) | [韓文](../ko/README.md) | [立陶宛文](../lt/README.md) | [馬來文](../ms/README.md) | [馬拉雅拉姆文](../ml/README.md) | [馬拉地文](../mr/README.md) | [尼泊爾文](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威文](../no/README.md) | [波斯文 (Farsi)](../fa/README.md) | [波蘭文](../pl/README.md) | [葡萄牙文 (巴西)](../pt-BR/README.md) | [葡萄牙文 (葡萄牙)](../pt-PT/README.md) | [旁遮普文 (Gurmukhi)](../pa/README.md) | [羅馬尼亞文](../ro/README.md) | [俄文](../ru/README.md) | [塞爾維亞文 (西里爾字母)](../sr/README.md) | [斯洛伐克文](../sk/README.md) | [斯洛文尼亞文](../sl/README.md) | [西班牙文](../es/README.md) | [斯瓦希里文](../sw/README.md) | [瑞典文](../sv/README.md) | [他加祿文 (菲律賓語)](../tl/README.md) | [泰米爾文](../ta/README.md) | [泰盧固文](../te/README.md) | [泰文](../th/README.md) | [土耳其文](../tr/README.md) | [烏克蘭文](../uk/README.md) | [烏爾都文](../ur/README.md) | [越南文](../vi/README.md)

> **想本地克隆？**
>
> 此儲存庫包含 50 多種語言的翻譯，會大幅增加下載體積。若要不下載翻譯，請使用稀疏結帳 (sparse checkout)：
>
> **Bash / macOS / Linux：**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows)：**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 這樣能讓您以更快速度下載並完成課程。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概覽

**Co-op Translator** 幫助您輕鬆將教育 GitHub 內容本地化為多種語言。  
當您更新 Markdown 文件、圖片或筆記本時，翻譯將自動同步，確保您的內容對全球學習者保持準確和最新。

以下為翻譯內容組織示例：

![Example](../../translated_images/zh-HK/translation-ex.0c8aa6a7ee0aad2b.webp)

## 如何管理翻譯狀態

Co-op Translator 以<strong>版本化軟體產物</strong>方式管理翻譯內容，  
而非靜態檔案。

該工具透過<strong>語言範圍的元資料</strong>來追蹤已翻譯的 Markdown、圖片和筆記本狀態。

這種設計使 Co-op Translator 能夠：

- 可靠地偵測過期翻譯
- 一致處理 Markdown、圖片和筆記本
- 安全擴展於大型、快速更新、多語言的儲存庫

透過將翻譯視為受管理的產物，  
翻譯工作流程自然符合現代軟體的相依與產物管理實務。

→ [如何管理翻譯狀態](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速開始

```bash
# 建立並啟動虛擬環境（建議）
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 安裝套件
pip install co-op-translator
# 翻譯
translate -l "ko ja fr" -md
```

Docker：

```bash
# 從 GHCR 拉取公開映像
docker pull ghcr.io/azure/co-op-translator:latest
# 以掛載當前資料夾及提供 .env 環境變數的方式執行（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最簡設置

1. 確認您使用的 Python 版本符合支援（目前 3.10-3.12），poetry (pyproject.toml) 會自動處理。
2. 使用範本 [.env.template](../../.env.template) 建立 `.env` 檔案
3. 設定一個大型語言模型提供者（Azure OpenAI 或 OpenAI）
4. (選用) 圖片翻譯 (`-img`)，配置 Azure AI Vision
5. (選用) 可複製變數並加上後綴如 `_1`, `_2` 等，配置多組憑證。每組中所有變數需相同後綴。
6. (建議) 清理舊有翻譯避免衝突（如 `translations/`）
7. (建議) 依據 [README 語言範本](./getting_started/README_languages_template.md) 加入翻譯區塊到您的 README
8. 請參考：[設定 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

翻譯所有支援類型：

```bash
translate -l "ko ja"
```

僅翻譯 Markdown：

```bash
translate -l "de" -md
```

Markdown + 圖片：

```bash
translate -l "pt" -md -img
```

僅翻譯筆記本：

```bash
translate -l "zh" -nb
```

更多參數選項：[指令參考](./getting_started/command-reference.md)

## 功能

- 自動翻譯 Markdown、筆記本及圖片
- 保持翻譯與原始檔同步
- 支援本地（CLI）或 CI（GitHub Actions）操作
- 使用 Azure OpenAI 或 OpenAI；圖片支持可選 Azure AI Vision
- 保留 Markdown 格式與結構

## 文件

- [指令列指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公開儲存庫與標準祕密）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（Microsoft 組織儲存庫與組織層級設置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 語言範本](./getting_started/README_languages_template.md)
- [支援語言](./getting_started/supported-languages.md)
- [貢獻指南](./CONTRIBUTING.md)
- [疑難排解](./getting_started/troubleshooting.md)

### Microsoft 專用指南
> [!NOTE]
> 僅供 Microsoft “初學者” 儲存庫維護者參考。

- [更新“其他課程”列表（僅針對 Microsoft 初學者儲存庫）](./getting_started/update-other-courses.md)

## 支援我們，促進全球學習

加入我們，一起改變教育內容的全球分享方式！在 GitHub 為 [Co-op Translator](https://github.com/azure/co-op-translator) 點 ⭐，支持我們打破語言障礙，推動學習與技術的普及。您的支持與貢獻對我們意義重大！歡迎提出程式碼貢獻及功能建議。

### 探索您的語言版本 Microsoft 教育內容

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [使用 .NET 的生成式 AI 初學者](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [生成式 AI 初學者](https://github.com/microsoft/generative-ai-for-beginners)
- [使用 Java 的生成式 AI 初學者](https://github.com/microsoft/generative-ai-for-beginners-java)
- [機器學習初學者](https://aka.ms/ml-beginners)
- [資料科學初學者](https://aka.ms/datascience-beginners)
- [AI 初學者](https://aka.ms/ai-beginners)
- [資安初學者](https://github.com/microsoft/Security-101)
- [網頁開發初學者](https://aka.ms/webdev-beginners)
- [物聯網初學者](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 視頻簡報

👉 點擊下方圖片前往 YouTube 觀看。

- **Open at Microsoft**：18 分鐘簡短介紹與快速上手指南，教您如何使用 Co-op Translator。

  [![Open at Microsoft](../../translated_images/zh-HK/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢獻

本專案歡迎您的貢獻與建議。想為 Azure Co-op Translator 貢獻嗎？請參閱我們的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何幫助使 Co-op Translator 更加普及與易用。

## 貢獻者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行為守則

本專案已採用 [Microsoft 開放原始碼行為守則](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請參閱 [行為守則常見問題](https://opensource.microsoft.com/codeofconduct/faq/) 或
聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 以提出其他問題或意見。

## 負責任的 AI

Microsoft 致力協助我們的客戶負責任地使用我們的 AI 產品，分享我們的經驗，並透過 Transparency Notes 及 Impact Assessments 等工具建立以信任為基礎的合作夥伴關係。許多這些資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 對負責任 AI 的方法以我們的 AI 原則為基礎，包括公平性、可靠性與安全性、隱私與安全、包容性、透明度以及問責制。

大型自然語言、影像及語音模型——如本範例中使用的模型——可能會出現不公平、不可靠或冒犯性的行為，並因此造成傷害。請參閱 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)，了解相關風險與限制。

建議採取的風險緩解方法是在系統架構中包含可偵測及防止有害行為的安全系統。[Azure AI 內容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能在應用程式和服務中偵測有害的使用者及 AI 產生內容。Azure AI 內容安全包含文字及影像 API，讓您能偵測有害素材。我們也有互動式的內容安全工作室，允許您檢視、探索並試用可偵測不同媒介有害內容的示範程式碼。以下的[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)會引導您向服務發出請求。

另一個需要考量的是整體應用程式效能。針對多媒體及多模型應用程式，我們認為效能是指系統依您和您的用戶所期望運作，包括不產生有害輸出。評估整體應用程式效能時，請使用[生成品質以及風險與安全度指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

您可以使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 在開發環境中評估您的 AI 應用程式。無論是測試資料集或目標，您的生成式 AI 應用程式輸出皆會透過內建評估器或您自訂的評估器進行量化評測。若要開始使用 prompt flow sdk 評估您的系統，請參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。完成評估執行後，您可於[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) 內視覺化結果。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。微軟商標或標誌的授權使用必須遵循並受限於 [Microsoft 的商標及品牌指引](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在修改版本的本專案中使用 Microsoft 商標或標誌，不得引起混淆或暗示微軟贊助。
任何第三方商標或標誌的使用均受該第三方政策的約束。

## 尋求協助

如果遇到困難或對於建置 AI 應用程式有任何疑問，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如需產品回饋或編輯過程中遇到錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->