# 更新「其他課程」區段（Microsoft Beginners 倉庫）

本指南說明如何使用 Co‑op Translator 讓「其他課程」區段自動同步，以及如何更新所有倉庫的全域範本。

- 適用對象：僅限 Microsoft Beginners 倉庫
- 適用工具：Co‑op Translator CLI 與 GitHub Actions
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在你的倉庫啟用自動同步

在你的 README 中「其他課程」區段周圍加入以下標記。Co‑op Translator 會在每次執行時替換這些標記間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co‑op Translator 執行時——無論是透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions——都會自動更新由這些標記包覆的「其他課程」區段。

> [!NOTE]
> 如果你已有現成列表，只需用相同標記包裹起來，下一次執行時將會用最新的標準內容取代它。

---

## 如何變更全域內容

如果你想更新出現在所有 Beginners 倉庫的標準化內容：

1. 編輯範本：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 提交拉取請求（PR）到 Co-op Translator 倉庫，包含你的更改
3. PR 合併後，Co‑op Translator 版本會被更新
4. 下次 Co‑op Translator 執行（CLI 或 GitHub Action）於目標倉庫時，將自動同步更新後的區段

這可確保所有 Beginners 倉庫中「其他課程」內容的唯一真實來源。

## 倉庫大小

由於翻譯成多國語言，倉庫可能變得龐大，幫助終端用戶提供如何使用 clone - sparse 僅克隆必要語言，而非整個倉庫的指引

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應視為權威資料來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->