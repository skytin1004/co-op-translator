# 指令參考

**Co-op Translator** CLI 提供多種選項來自訂翻譯流程：

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將您的專案翻譯成指定語言。範例：translate -l "es fr de" 將翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援語言。
translate -l "language_codes" -u              | 更新翻譯，將刪除現有翻譯並重新建立。警告：這會刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 只翻譯圖片檔案。
translate -l "language_codes" -md             | 只翻譯 Markdown 檔案。
translate -l "language_codes" -nb             | 只翻譯 Jupyter 筆記本檔案（.ipynb）。
translate -l "language_codes" --fix           | 根據先前評估結果，重新翻譯低信心分數的檔案。
translate -l "language_codes" -d              | 啟用除錯模式以獲得詳細日誌。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別的日誌保存到 <root_dir>/logs/ 目錄下的檔案（控制台輸出由 -d 控制）
translate -l "language_codes" -r "root_dir"   | 指定專案根目錄
translate -l "language_codes" -f              | 使用快速模式進行圖片翻譯（繪製速度最高提升 3 倍，質量和對齊會略有影響）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 流程）
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 啟用或停用在翻譯的 Markdown 和筆記本中加入機器翻譯免責聲明區塊（預設啟用）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | 以您的倉庫 URL 個人化 README 語言區段通知（稀疏簽出）。
translate -l "language_codes" --help          | 查看 CLI 中的可用指令說明
evaluate -l "language_code"                  | 評估特定語言的翻譯品質並給出信心分數
evaluate -l "language_code" -c 0.8           | 使用自訂信心閾值評估翻譯
evaluate -l "language_code" -f               | 快速評估模式（僅規則基礎，無 LLM）
evaluate -l "language_code" -D               | 深度評估模式（僅 LLM，較詳盡但較慢）
evaluate -l "language_code" --save-logs, -s  | 將 DEBUG 級別的日誌保存到 <root_dir>/logs/ 目錄下的檔案
migrate-links -l "language_codes"             | 重新處理已翻譯的 Markdown 檔案，更新指向 Jupyter 筆記本 (.ipynb) 的連結。優先使用翻譯後的筆記本，如無則可回退至原始筆記本。
migrate-links -l "language_codes" -r          | 指定專案根目錄（預設為當前目錄）。
migrate-links -l "language_codes" --dry-run   | 顯示哪些檔案將被更改，但不寫入變更。
migrate-links -l "language_codes" --no-fallback-to-original | 翻譯的筆記本不存在時，不將連結改寫指向原始筆記本（僅當有翻譯時才更新）。
migrate-links -l "language_codes" -d          | 啟用除錯模式以獲得詳細日誌。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別的日誌保存到 <root_dir>/logs/ 目錄下的檔案
migrate-links -l "all" -y                      | 處理所有語言並自動確認警告提示。

## 使用範例

  1. 預設行為（新增翻譯，不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 僅新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：這會刪除所有現有韓文翻譯再重新翻譯）：    translate -l "ko" -u

  4. 只更新韓文圖片（警告：這會刪除所有現有韓文圖片再重新翻譯）：    translate -l "ko" -img -u

  5. 新增韓文 Markdown 翻譯而不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正低信心翻譯： translate -l "ko" --fix

  7. 只修正特定檔案的低信心翻譯（Markdown）： translate -l "ko" --fix -md

  8. 只修正特定檔案的低信心翻譯（圖片）： translate -l "ko" --fix -img

  9. 使用快速模式進行圖片翻譯：    translate -l "ko" -img -f

  10. 以自訂門檻修正低信心翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 將日誌保存至檔案： translate -l "ko" -s
  13. 同時啟用主控台與檔案的 DEBUG： translate -l "ko" -d -s
  14. 翻譯時不在輸出中加入機器翻譯免責聲明： translate -l "ko" --no-disclaimer

  15. 針對韓文翻譯遷移筆記本連結（有翻譯時更新連結）：    migrate-links -l "ko"

  15. 模擬執行連結遷移（不寫入檔案變更）：    migrate-links -l "ko" --dry-run

  16. 僅當有翻譯筆記本時更新連結（不回退至原始筆記本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 處理所有語言並顯示確認提示：    migrate-links -l "all"

  18. 處理所有語言並自動確認：    migrate-links -l "all" -y
  19. 將遷移連結日誌保存至檔案：    migrate-links -l "ko ja" -s

  20. 以您的倉庫 URL 個人化 README 語言通知區塊：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 評估範例

> [!WARNING]  
> **Beta 功能**：評估功能目前為 Beta 版本。此功能用於評估翻譯文件，評估方法和詳細實作尚在開發中，且可能改變。

  1. 評估韓文翻譯： evaluate -l "ko"

  2. 使用自訂信心門檻評估： evaluate -l "ko" -c 0.8

  3. 快速評估（僅規則基礎）： evaluate -l "ko" -f

  4. 深度評估（僅 LLM）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖我們致力於確保翻譯準確，但請注意，自動翻譯可能存在錯誤或不準確之處。原文文件以其原始語言版本為權威依據。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->