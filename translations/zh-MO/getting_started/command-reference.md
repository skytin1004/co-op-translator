# Command reference

The **Co-op Translator** CLI 提供多種選項以自訂翻譯過程：

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將您的項目翻譯成指定語言。例如：translate -l "es fr de" 會翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援的語言。
translate -l "language_codes" -u              | 更新翻譯，會刪除現有翻譯並重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 僅翻譯圖片檔案。
translate -l "language_codes" -md             | 僅翻譯 Markdown 檔案。
translate -l "language_codes" -nb             | 僅翻譯 Jupyter 筆記本檔案 (.ipynb)。
translate -l "language_codes" --fix           | 根據先前評估結果，重新翻譯置信度較低的檔案。
translate -l "language_codes" -d              | 開啟除錯模式以獲得詳細日志。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別日志保存至 <root_dir>/logs/ 下的檔案（控制台日志受 -d 控制）。
translate -l "language_codes" -r "root_dir"   | 指定專案的根目錄。
translate -l "language_codes" -f              | 使用圖片翻譯的快速模式（繪圖速度可提升至 3 倍，但會稍微犧牲品質和對齊）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 流程）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 啟用或停用在翻譯的 Markdown 和筆記本中新增機器翻譯免責聲明區塊（預設：啟用）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | 使用您的倉庫 URL 個人化 README 語言區段建議（稀疏結帳）。
translate -l "language_codes" --help          | CLI 內部的幫助詳情，顯示可用命令。
evaluate -l "language_code"                  | 評估特定語言的翻譯品質並提供置信度分數。
evaluate -l "language_code" -c 0.8           | 使用自訂置信度門檻評估翻譯。
evaluate -l "language_code" -f               | 快速評估模式（僅基於規則，無大型語言模型）。
evaluate -l "language_code" -D               | 深度評估模式（僅基於大型語言模型，更詳細但較慢）。
evaluate -l "language_code" --save-logs, -s  | 將 DEBUG 級別日志保存至 <root_dir>/logs/ 下的檔案。
migrate-links -l "language_codes"             | 重新處理已翻譯的 Markdown 檔案以更新指向筆記本 (.ipynb) 的連結。若有翻譯筆記本優先使用，否則可回退至原始筆記本。
migrate-links -l "language_codes" -r          | 指定專案根目錄（預設為當前目錄）。
migrate-links -l "language_codes" --dry-run   | 顯示會更改哪些檔案，但不寫入變更。
migrate-links -l "language_codes" --no-fallback-to-original | 在找不到翻譯筆記本時，不回退重寫為原始筆記本連結（僅在有翻譯筆記本時才更新）。
migrate-links -l "language_codes" -d          | 啟用除錯模式以獲得詳細日志。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別日志保存至 <root_dir>/logs/。
migrate-links -l "all" -y                      | 處理所有語言並自動確認警告提示。

## Usage examples

  1. 預設行為（新增翻譯而不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 只新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：這會刪除所有現有韓文翻譯後再重新翻譯）：    translate -l "ko" -u

  4. 只更新韓文圖片（警告：這會刪除所有現有韓文圖片後再重新翻譯）：    translate -l "ko" -img -u

  5. 新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正低置信度翻譯： translate -l "ko" --fix

  7. 僅修正特定檔案（Markdown）的低置信度翻譯： translate -l "ko" --fix -md

  8. 僅修正特定檔案（圖片）的低置信度翻譯： translate -l "ko" --fix -img

  9. 使用圖片翻譯快速模式：    translate -l "ko" -img -f

  10. 使用自訂門檻修正低置信度翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 保存日誌至檔案： translate -l "ko" -s
  13. 控制台 DEBUG 和檔案 DEBUG ： translate -l "ko" -d -s
  14. 翻譯時不加入機器翻譯免責聲明： translate -l "ko" --no-disclaimer

  15. 路徑轉移筆記本連結（更新指向已翻譯筆記本的連結，如有）：    migrate-links -l "ko"

  15. 以 dry-run 模式轉移連結（不寫入檔案）：    migrate-links -l "ko" --dry-run

  16. 僅當翻譯筆記本存在時更新連結（不回退至原始筆記本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 處理所有語言並提示確認：    migrate-links -l "all"

  18. 處理所有語言並自動確認：    migrate-links -l "all" -y
  19. 保存 migrate-links 日誌至檔案：    migrate-links -l "ko ja" -s

  20. 使用您的倉庫 URL 個人化 README 語言建議：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta 功能**：評估功能目前屬於 Beta 版本。該功能為評估已翻譯文件而釋出，評估方法與詳細實作仍在開發中，可能會有變動。

  1. 評估韓文翻譯： evaluate -l "ko"

  2. 使用自訂置信度門檻評估： evaluate -l "ko" -c 0.8

  3. 快速評估（僅基於規則）： evaluate -l "ko" -f

  4. 深度評估（僅基於大型語言模型）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤譯，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->