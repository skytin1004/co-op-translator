# Command reference

The **Co-op Translator** CLI 提供多個選項來自訂翻譯流程：

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 將您的專案翻譯成指定語言。範例：translate -l "es fr de" 將翻譯成西班牙語、法語和德語。使用 translate -l "all" 可翻譯成所有支援的語言。
translate -l "language_codes" -u              | 更新翻譯，會刪除現有翻譯並重新建立。警告：這將刪除指定語言的所有現有翻譯。
translate -l "language_codes" -img            | 僅翻譯圖片檔案。
translate -l "language_codes" -md             | 僅翻譯 Markdown 檔案。
translate -l "language_codes" -nb             | 僅翻譯 Jupyter notebook 檔案 (.ipynb)。
translate -l "language_codes" --fix           | 根據之前的評估結果，重新翻譯低信心分數的檔案。
translate -l "language_codes" -d              | 啟用除錯模式以獲得詳細日誌。
translate -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌保存至 <root_dir>/logs/ 目錄下的檔案（控制台仍由 -d 控制）。
translate -l "language_codes" -r "root_dir"   | 指定專案的根目錄。
translate -l "language_codes" -f              | 對圖片翻譯使用快速模式（繪圖速度最高可提升 3 倍，品質和對齊略有損失）。
translate -l "language_codes" -y              | 自動確認所有提示（適用於 CI/CD 流程）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 啟用或禁用在翻譯的 markdown 和 notebook 中新增機器翻譯免責聲明段落（預設啟用）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | 使用您的倉庫 URL 個人化 README 的語言部分建議（稀疏檢出）。
translate -l "language_codes" --help          | CLI 內顯示可用命令的幫助詳細資訊。
evaluate -l "language_code"                  | 評估特定語言翻譯品質並提供信心分數。
evaluate -l "language_code" -c 0.8           | 使用自訂信心閾值評估翻譯。
evaluate -l "language_code" -f               | 快速評估模式（僅基於規則，無 LLM）。
evaluate -l "language_code" -D               | 深度評估模式（僅基於 LLM，較為全面但較慢）。
evaluate -l "language_code" --save-logs, -s  | 將 DEBUG 級別日誌保存至 <root_dir>/logs/ 目錄下。
migrate-links -l "language_codes"             | 重新處理已翻譯的 Markdown 檔案，更新指向 notebook (.ipynb) 的連結。優先使用翻譯後的 notebook，若無則可回退到原始 notebook。
migrate-links -l "language_codes" -r          | 指定專案根目錄（預設為當前目錄）。
migrate-links -l "language_codes" --dry-run   | 顯示將變更的檔案但不寫入變更。
migrate-links -l "language_codes" --no-fallback-to-original | 未找到翻譯的 notebook 時，不重寫指向原始 notebook 的連結（僅在翻譯存在時更新連結）。
migrate-links -l "language_codes" -d          | 啟用除錯模式以獲得詳細日誌。
migrate-links -l "language_codes" --save-logs, -s | 將 DEBUG 級別日誌保存至 <root_dir>/logs/ 目錄下。
migrate-links -l "all" -y                      | 處理所有語言並自動確認警告提示。

## Usage examples

  1. 預設行為（新增新翻譯，不刪除現有翻譯）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 僅新增韓文圖片翻譯（不刪除現有翻譯）：    translate -l "ko" -img

  3. 更新所有韓文翻譯（警告：這會在重新翻譯前刪除所有現有韓文翻譯）：    translate -l "ko" -u

  4. 只更新韓文圖片（警告：這會在重新翻譯前刪除所有現有韓文圖片）：    translate -l "ko" -img -u

  5. 新增韓文 Markdown 翻譯，不影響其他翻譯：    translate -l "ko" -md

  6. 根據先前評估結果修正低信心翻譯： translate -l "ko" --fix

  7. 僅修正特定檔案低信心翻譯（Markdown）： translate -l "ko" --fix -md

  8. 僅修正特定檔案低信心翻譯（圖片）： translate -l "ko" --fix -img

  9. 使用快速模式翻譯圖片：    translate -l "ko" -img -f

  10. 使用自訂閾值修正低信心翻譯： translate -l "ko" --fix -c 0.8

  11. 除錯模式範例： - translate -l "ko" -d：啟用除錯日誌。
  12. 將日誌保存至檔案： translate -l "ko" -s
  13. 併用控制台 DEBUG 和文件 DEBUG： translate -l "ko" -d -s
  14. 翻譯時不添加機器翻譯免責聲明： translate -l "ko" --no-disclaimer

  15. 韓文翻譯的 notebook 連結遷移（有翻譯時更新連結）：    migrate-links -l "ko"

  15. 連結遷移的 dry-run（不寫檔）：    migrate-links -l "ko" --dry-run

  16. 僅在有翻譯 notebook 時更新連結（不回退到原始檔）：    migrate-links -l "ko" --no-fallback-to-original

  17. 處理所有語言並顯示確認提示：    migrate-links -l "all"

  18. 處理所有語言並自動確認：    migrate-links -l "all" -y
  19. 保存 migrate-links 的日誌至檔案：    migrate-links -l "ko ja" -s

  20. 個人化 README 語言建議，使用您的倉庫 URL：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**：評估功能目前處於 Beta 階段。此功能用於評估翻譯文件，評估方法及詳細實作仍在開發中，可能會變更。

  1. 評估韓文翻譯品質： evaluate -l "ko"

  2. 使用自訂信心閾值評估： evaluate -l "ko" -c 0.8

  3. 快速評估（僅規則基礎）： evaluate -l "ko" -f

  4. 深度評估（僅 LLM 基礎）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。本公司不對因使用此翻譯而引起的任何誤解或誤讀承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->