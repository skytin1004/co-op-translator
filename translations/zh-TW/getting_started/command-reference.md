# Command reference

The **Co-op Translator** CLI 提供多種選項以自訂翻譯流程：

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將您的專案翻譯成指定語言。例如：translate -l "es fr de" 會翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援的語言。
translate -l "language_codes" -u              | 更新翻譯，會刪除現有翻譯並重新建立。警告：此操作會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 僅翻譯圖片檔案。
translate -l "language_codes" -md             | 僅翻譯 Markdown 檔案。
translate -l "language_codes" -nb             | 僅翻譯 Jupyter 筆記本檔案 (.ipynb)。
translate -l "language_codes" --fix           | 根據先前評估結果，重新翻譯置信度較低的檔案。
translate -l "language_codes" -d              | 啟用除錯模式，提供詳細日誌。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別的日誌保存到 <root_dir>/logs/ 目錄下（終端機輸出由 -d 控制）。
translate -l "language_codes" -r "root_dir"   | 指定專案根目錄。
translate -l "language_codes" -f              | 對圖片翻譯使用快速模式（繪圖速度快 3 倍左右，但會略微犧牲品質與對齊）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 流程）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 啟用或停用在翻譯的 Markdown 和筆記本中加入機器翻譯免責聲明段落（預設：啟用）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | 個人化 README 中語言區段的建議（稀疏檢出）並加入您的倉庫 URL。
translate -l "language_codes" --help          | CLI 內顯示可用指令的說明。
evaluate -l "language_code"                  | 評估特定語言的翻譯品質並提供置信度分數。
evaluate -l "language_code" -c 0.8           | 以自訂置信度門檻評估翻譯。
evaluate -l "language_code" -f               | 快速評估模式（僅基於規則，不使用大型語言模型）。
evaluate -l "language_code" -D               | 深度評估模式（僅基於大型語言模型，較詳盡但較慢）。
evaluate -l "language_code" --save-logs, -s  | 將 DEBUG 級別日誌保存到 <root_dir>/logs/。
migrate-links -l "language_codes"             | 重新處理翻譯後的 Markdown 檔案以更新指向筆記本 (.ipynb) 的連結。優先使用翻譯後的筆記本，否則可轉回使用原始筆記本。
migrate-links -l "language_codes" -r          | 指定專案根目錄（預設為當前目錄）。
migrate-links -l "language_codes" --dry-run   | 顯示將會變更的檔案，但不進行寫入。
migrate-links -l "language_codes" --no-fallback-to-original | 在翻譯筆記本不存在時，不改寫連結至原始筆記本（只有在翻譯筆記本存在時才更新）。
migrate-links -l "language_codes" -d          | 啟用除錯模式，提供詳細日誌。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌保存到 <root_dir>/logs/。
migrate-links -l "all" -y                      | 處理所有語言並自動確認警告提示。

## 使用範例

  1. 預設行為（新增翻譯，無刪除既有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 僅新增韓文圖片翻譯（不刪除既有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：此操作會刪除所有現有韓文翻譯後再翻譯）：    translate -l "ko" -u

  4. 僅更新韓文圖片翻譯（警告：此操作會刪除所有現有韓文圖片後再翻譯）：    translate -l "ko" -img -u

  5. 新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正置信度低的翻譯： translate -l "ko" --fix

  7. 僅修正置信度低的特定檔案（Markdown）： translate -l "ko" --fix -md

  8. 僅修正置信度低的特定檔案（圖片）： translate -l "ko" --fix -img

  9. 圖片翻譯使用快速模式：    translate -l "ko" -img -f

  10. 以自訂門檻修正置信度低的翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 將日誌保存至檔案： translate -l "ko" -s
  13. 終端機 DEBUG 與檔案 DEBUG： translate -l "ko" -d -s
  14. 翻譯時不加入機器翻譯免責聲明： translate -l "ko" --no-disclaimer

  15. 更新韓文翻譯的筆記本連結（有翻譯筆記本時更新連結）：    migrate-links -l "ko"

  15. 使用 dry-run 模式遷移連結（不寫入檔案）：    migrate-links -l "ko" --dry-run

  16. 只有在存在翻譯筆記本時更新連結（不轉回原始筆記本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 執行所有語言並顯示確認提示：    migrate-links -l "all"

  18. 執行所有語言並自動確認：    migrate-links -l "all" -y
  19. migrate-links 保存日誌至檔案：    migrate-links -l "ko ja" -s

  20. 使用您的倉庫 URL 個人化 README 語言建議：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 評估範例

> [!WARNING]  
> **Beta 功能**：評估功能目前為測試版。此功能是針對翻譯文件做評估，評估方法與詳細實作仍在開發中，且可能會有所變更。

  1. 評估韓文翻譯： evaluate -l "ko"

  2. 以自訂置信度門檻評估： evaluate -l "ko" -c 0.8

  3. 快速評估（僅規則法）： evaluate -l "ko" -f

  4. 深度評估（僅大型語言模型）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。請以原始文件的母語版本為權威依據。針對重要資訊，建議使用專業人工翻譯。本公司對於因使用本翻譯而產生的任何誤解或誤譯不負任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->