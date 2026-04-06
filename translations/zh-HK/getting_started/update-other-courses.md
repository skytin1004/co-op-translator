# 更新「其他課程」部分 (Microsoft Beginners 儲存庫)

本指南說明如何使用 Co-op Translator 使「其他課程」部分自動同步，以及如何更新所有儲存庫的全局範本。

- 適用於：僅 Microsoft Beginners 儲存庫  
- 適用工具：Co-op Translator CLI 和 GitHub Actions  
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  

---

## 快速開始：在您的儲存庫啟用自動同步

在 README 中的「其他課程」部分周圍添加以下標記。Co-op Translator 會在每次執行時替換這些標記之間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
每次 Co-op Translator 執行時—無論是透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions—都會自動更新這些標記所包圍的「其他課程」部分。

> [!NOTE]  
> 如果您已有現成清單，只需用相同的標記包裹它。下一次執行時會用最新標準化內容取代。

---

## 如何更改全局內容

如果您想更新所有 Beginners 儲存庫中出現的標準化內容：

1. 編輯範本：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. 開啟針對 Co-op Translator 儲存庫的 pull request，提交您的更改  
3. PR 合併後，Co-op Translator 版本將更新  
4. 下一次 Co-op Translator 在目標儲存庫（CLI 或 GitHub Action）執行時，會自動同步更新的部分  

此操作確保所有 Beginners 儲存庫中「其他課程」內容有唯一真實來源。

## 儲存庫大小

由於翻譯成的語言數量眾多，儲存庫可能會變得很大，這是為了協助終端用戶提供如何使用 clone - sparse 只克隆必要語言而非整個儲存庫的指導。

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
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對使用此翻譯所引起的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->