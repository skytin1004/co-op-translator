# 更新「其他課程」部分（Microsoft 初學者存放庫）

本指南說明如何使用 Co-op Translator 使「其他課程」部分自動同步，以及如何更新所有存放庫的全域範本。

- 適用範圍：僅限 Microsoft 初學者存放庫
- 適用工具：Co-op Translator CLI 與 GitHub Actions
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在您的存放庫中啟用自動同步

在您的 README 中「其他課程」部分周圍加入以下標記。Co-op Translator 將在每次執行時替換這些標記之間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 執行時 — 透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions — 都會自動更新由這些標記包圍的「其他課程」部分。

> [!NOTE]
> 如果您已經有現有清單，只要用相同的標記包覆即可。下一次執行時，將會替換成最新的標準化內容。

---

## 如何更改全域內容

如果您想更新出現在所有初學者存放庫中的標準化內容：

1. 編輯範本：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 提交包含您變更的 pull request 至 Co-op Translator 存放庫
3. PR 合併後，Co-op Translator 版本會更新
4. 下一次 Co-op Translator 在目標存放庫中執行（無論是 CLI 或 GitHub Action），都會自動同步更新的部分

這確保「其他課程」內容在所有初學者存放庫中擁有唯一可信來源。


## 存放庫大小

由於翻譯語言數量眾多，存放庫可能會變得很大，為幫助最終使用者，建議使用 clone - sparse 來只克隆必要語言，而非整個存放庫。

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
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯所引起的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->