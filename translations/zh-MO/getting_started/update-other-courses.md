# 更新「其他課程」部分（Microsoft Beginners 倉庫）

本指南說明如何使用 Co-op Translator 讓「其他課程」部分自動同步，以及如何更新所有倉庫的全局模板。

- 適用於：僅限 Microsoft Beginners 倉庫
- 搭配使用：Co-op Translator CLI 及 GitHub Actions
- 模板來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在你的倉庫啟用自動同步

在你的 README 中「其他課程」部分周圍加入以下標記。Co-op Translator 將在每次執行時替換這些標記之間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
每次 Co-op Translator 執行—透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions—都會自動更新由這些標記包裹的「其他課程」部分。

> [!NOTE]  
> 如果你已有現存清單，只需用相同標記包裹。下一次執行時將以最新標準化內容取代。

---

## 如何更改全局內容

如果你想更新所有 Beginners 倉庫中顯示的標準化內容：

1. 編輯模板：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. 提出包含你更改的 pull request 至 Co-op Translator 倉庫  
3. PR 合併後，Co-op Translator 的版本將更新  
4. 下一次 Co-op Translator 執行（CLI 或 GitHub Action）於目標倉庫時，會自動同步更新的部分

這確保「其他課程」內容在所有 Beginners 倉庫中有單一的真實來源。

## 倉庫大小

由於翻譯成多種語言，倉庫可能變得龐大。為協助終端用戶指導如何使用 clone - sparse 僅克隆必要語言，而非整個倉庫，

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
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。文件原文之母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我哋對因使用本翻譯而引起嘅任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->