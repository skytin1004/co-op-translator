# 更新「其他課程」部分（Microsoft 初學者倉庫）

本指南說明如何使用 Co‑op Translator 使「其他課程」部分自動同步，以及如何更新所有倉庫的全局範本。

- 適用對象：僅限 Microsoft 初學者倉庫
- 適用工具：Co‑op Translator CLI 及 GitHub Actions
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在你的倉庫啟用自動同步

在你的 README 中，於「其他課程」部分加上以下標記。Co‑op Translator 會在每次執行時替換這些標記之間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co‑op Translator 執行時 — 無論是透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions — 都會自動更新被這些標記包圍的「其他課程」部分。

> [!NOTE]
> 如果你已有現成列表，只需用相同標記包起來。下一次執行時，內容會被最新標準化內容取代。

---

## 如何更改全局內容

若你想更新出現在所有初學者倉庫中的標準化內容：

1. 編輯範本：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 開啟一個 pull request 至 Co-op Translator 倉庫提交變更
3. PR 合併後，Co‑op Translator 版本會更新
4. 下一次 Co‑op Translator（CLI 或 GitHub Action）在目標倉庫執行時，會自動同步更新的部分

這樣可確保所有初學者倉庫「其他課程」內容的單一真實來源。

## 倉庫大小

由於支持多語言翻譯，倉庫可能變得龐大，方便終端用戶提供如何使用 clone - sparse 僅克隆所需語言而非整個倉庫的指引。

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
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應視為權威資料。對於重要資訊，建議尋求專業人工翻譯。我們不對使用此翻譯所引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->