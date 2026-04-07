# 更新「其他課程」區段（Microsoft Beginners 倉庫）

本指南說明如何使用 Co‑op Translator，使「其他課程」區段自動同步，以及如何更新所有倉庫的全局範本。

- 適用於：僅限 Microsoft Beginners 倉庫
- 配合使用：Co‑op Translator CLI 和 GitHub Actions
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在你的倉庫啟用自動同步

在你的 README 中，於「其他課程」區段周圍新增以下標記。Co‑op Translator 每次執行時都會取代這些標記之間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co‑op Translator 執行時──無論是透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions──都會自動更新這些標記包圍的「其他課程」區段。

> [!NOTE]
> 如果你已有現有清單，只需用相同標記包起來。下一次執行時，它將以最新的標準化內容取代。

---

## 如何更改全局內容

如果你想更新出現在所有 Beginners 倉庫裡的標準化內容：

1. 編輯範本：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 於 Co-op Translator 倉庫開啟拉取請求（pull request）提交你的變更
3. PR 合併後，Co‑op Translator 版本將會更新
4. 下一次 Co‑op Translator 在目標倉庫中執行（CLI 或 GitHub Action）時，會自動同步更新後的區段

這確保「其他課程」內容於所有 Beginners 倉庫中有單一正確來源。

## 倉庫大小

由於翻譯成多種語言，倉庫可能會變大，為協助最終用戶提供如何使用 clone - sparse 只克隆必要語言而非整個倉庫的指導，

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
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。儘管我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。應以原始文件的母語版本為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->