# 指令參考

**Co-op Translator** CLI 提供多個選項以自訂翻譯流程：

指令                                         | 說明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將您的專案翻譯成指定語言。例如：translate -l "es fr de" 將翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯所有支援的語言。
translate -l "language_codes" -u              | 更新翻譯，會刪除現有翻譯後重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 只翻譯圖片檔案。
translate -l "language_codes" -md             | 只翻譯 Markdown 檔案。
translate -l "language_codes" -nb             | 只翻譯 Jupyter 筆記本檔案 (.ipynb)。
translate -l "language_codes" --fix           | 根據先前評估結果對置信度低的檔案重新翻譯。
translate -l "language_codes" -d              | 啟用除錯模式以獲取詳細日誌。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌儲存在 <root_dir>/logs/ 底下（主控台顯示仍由 -d 控制）
translate -l "language_codes" -r "root_dir"   | 指定專案根目錄
translate -l "language_codes" -f              | 使用快速模式翻譯圖片（繪圖速度最多快 3 倍，品質及對齊稍有犧牲）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 管線）
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 啟用或停用在翻譯的 Markdown 和筆記本中加入機器翻譯免責聲明段落（預設：啟用）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | 使用您的儲存庫 URL 個人化 README 語言區段建議（稀疏結帳）。
translate -l "language_codes" --help          | CLI 內的幫助詳情，顯示可用指令
evaluate -l "language_code"                  | 評估特定語言的翻譯品質並提供置信度分數
evaluate -l "language_code" -c 0.8           | 以自訂置信度門檻評估翻譯
evaluate -l "language_code" -f               | 快速評估模式（只有規則基礎，無 LLM）
evaluate -l "language_code" -D               | 深度評估模式（只有 LLM，較全面但較慢）
evaluate -l "language_code" --save-logs, -s  | 將 DEBUG 級別日誌儲存在 <root_dir>/logs/ 底下
migrate-links -l "language_codes"             | 重新處理翻譯過的 Markdown 檔案，更新連結至筆記本 (.ipynb)。優先使用翻譯後的筆記本，如無則可回退至原始筆記本。
migrate-links -l "language_codes" -r          | 指定專案根目錄（預設：當前目錄）。
migrate-links -l "language_codes" --dry-run   | 顯示會變更哪些檔案，但不寫入變更。
migrate-links -l "language_codes" --no-fallback-to-original | 當翻譯筆記本不存在時，不重寫連結至原始筆記本（只有翻譯存在時更新連結）。
migrate-links -l "language_codes" -d          | 啟用除錯模式以獲取詳細日誌。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌儲存在 <root_dir>/logs/ 底下
migrate-links -l "all" -y                      | 處理所有語言並自動確認警告提示。

## 使用範例

  1. 預設行為（新增新翻譯而不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 只新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：刪除所有現有韓文翻譯後重新翻譯）：    translate -l "ko" -u

  4. 只更新韓文圖片（警告：刪除所有現有韓文圖片後重新翻譯）：    translate -l "ko" -img -u

  5. 只新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正置信度低的翻譯： translate -l "ko" --fix

  7. 只修正特定檔案置信度低的翻譯（Markdown）： translate -l "ko" --fix -md

  8. 只修正特定檔案置信度低的翻譯（圖片）： translate -l "ko" --fix -img

  9. 使用快速模式翻譯圖片：    translate -l "ko" -img -f

  10. 以自訂門檻修正置信度低的翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 將日誌儲存到檔案： translate -l "ko" -s
  13. 主控台 DEBUG 及檔案 DEBUG： translate -l "ko" -d -s
  14. 翻譯時不要在輸出加入機器翻譯免責聲明： translate -l "ko" --no-disclaimer

  15. 移轉韓文筆記本連結（當翻譯筆記本存在時更新連結）：    migrate-links -l "ko"

  15. 執行移轉並以 dry-run 模式預覽（不寫檔）：    migrate-links -l "ko" --dry-run

  16. 僅當存在翻譯筆記本時更新連結（不回退至原始筆記本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 處理所有語言並有確認提示：    migrate-links -l "all"

  18. 處理所有語言並自動確認：    migrate-links -l "all" -y
  19. 為 migrate-links 儲存日誌檔案：    migrate-links -l "ko ja" -s

  20. 使用您的儲存庫 URL 個人化 README 語言建議：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 評估範例

> [!WARNING]  
> **Beta 功能**：評估功能目前仍處於 Beta 階段。此功能用來評估翻譯過的文件，其評估方法及詳細實作仍在開發中，未來或會有所變更。

  1. 評估韓文翻譯： evaluate -l "ko"

  2. 以自訂置信度門檻評估： evaluate -l "ko" -c 0.8

  3. 快速評估（只有規則基礎）： evaluate -l "ko" -f

  4. 深度評估（只有 LLM）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文檔是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯的。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議由專業人工翻譯處理。對於因使用本翻譯而引起的任何誤解或錯誤詮釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->