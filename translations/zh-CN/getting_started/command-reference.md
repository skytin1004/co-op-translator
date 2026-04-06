# 命令参考

**Co-op Translator** CLI 提供了多种选项来自定义翻译过程：

命令                                           | 描述
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 将您的项目翻译成指定语言。例如：translate -l "es fr de" 翻译成西班牙语、法语和德语。使用 translate -l "all" 翻译成所有支持的语言。
translate -l "language_codes" -u              | 通过删除现有翻译重新创建它们以更新翻译。警告：这将删除指定语言的所有当前翻译。
translate -l "language_codes" -img            | 仅翻译图像文件。
translate -l "language_codes" -md             | 仅翻译 Markdown 文件。
translate -l "language_codes" -nb             | 仅翻译 Jupyter notebook 文件（.ipynb）。
translate -l "language_codes" --fix           | 根据之前评估结果重新翻译低置信度文件。
translate -l "language_codes" -d              | 启用调试模式以获得详细日志。
translate -l "language_codes" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/ 下的文件（控制台日志仍受 -d 控制）。
translate -l "language_codes" -r "root_dir"   | 指定项目根目录。
translate -l "language_codes" -f              | 使用快速模式翻译图像（绘图速度提升最多3倍，质量和布局略有损失）。
translate -l "language_codes" -y              | 自动确认所有提示（适用于 CI/CD 流水线）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 启用或禁用向翻译后的 Markdown 和笔记本中添加机器翻译免责声明部分（默认启用）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | 使用您的仓库 URL 个性化 README 语言部分提示（稀疏检出）。
translate -l "language_codes" --help          | CLI 内显示可用命令的帮助详情。
evaluate -l "language_code"                  | 评估特定语言的翻译质量并提供置信度评分。
evaluate -l "language_code" -c 0.8           | 使用自定义置信度阈值评估翻译。
evaluate -l "language_code" -f               | 快速评估模式（仅基于规则，不使用大模型）。
evaluate -l "language_code" -D               | 深度评估模式（仅基于大模型，更彻底但更慢）。
evaluate -l "language_code" --save-logs, -s  | 将 DEBUG 级别日志保存到 <root_dir>/logs/ 下的文件。
migrate-links -l "language_codes"             | 重新处理翻译后的 Markdown 文件，更新指向笔记本（.ipynb）的链接。优先使用翻译的笔记本；如无，可回退到原始笔记本。
migrate-links -l "language_codes" -r          | 指定项目根目录（默认：当前目录）。
migrate-links -l "language_codes" --dry-run   | 显示哪些文件会被更改，但不写入更改。
migrate-links -l "language_codes" --no-fallback-to-original | 翻译笔记本缺失时不重写链接为原始笔记本（仅当翻译存在时更新）。
migrate-links -l "language_codes" -d          | 启用调试模式以获得详细日志。
migrate-links -l "language_codes" --save-logs, -s | 将 DEBUG 级别日志保存到 <root_dir>/logs/ 下的文件。
migrate-links -l "all" -y                      | 处理所有语言并自动确认警告提示。

## 使用示例

  1. 默认行为（添加新翻译，不删除现有翻译）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 仅添加新的韩文图像翻译（不删除现有翻译）：    translate -l "ko" -img

  3. 更新所有韩文翻译（警告：此操作会删除所有现有韩文翻译后重新翻译）：    translate -l "ko" -u

  4. 仅更新韩文图像（警告：此操作会删除所有现有韩文图像后重新翻译）：    translate -l "ko" -img -u

  5. 为韩文添加新的 Markdown 翻译而不影响其他翻译：    translate -l "ko" -md

  6. 根据之前的评估结果修复低置信度翻译： translate -l "ko" --fix

  7. 仅修复特定文件的低置信度翻译（Markdown）： translate -l "ko" --fix -md

  8. 仅修复特定文件的低置信度翻译（图像）： translate -l "ko" --fix -img

  9. 使用快速模式翻译图像：    translate -l "ko" -img -f

  10. 以自定义阈值修复低置信度翻译： translate -l "ko" --fix -c 0.8

  11. 调试模式示例： - translate -l "ko" -d：启用调试日志。
  12. 将日志保存到文件： translate -l "ko" -s
  13. 控制台 DEBUG 和文件 DEBUG： translate -l "ko" -d -s
  14. 翻译时不添加机器翻译免责声明： translate -l "ko" --no-disclaimer

  15. 迁移韩文翻译笔记本链接（有翻译笔记本时更新链接）：    migrate-links -l "ko"

  15. 以 dry-run 模式迁移链接（不写文件）：    migrate-links -l "ko" --dry-run

  16. 仅当翻译笔记本存在时更新链接（不回退到原始笔记本）：    migrate-links -l "ko" --no-fallback-to-original

  17. 处理所有语言并提示确认：    migrate-links -l "all"

  18. 处理所有语言并自动确认：    migrate-links -l "all" -y
  19. 为 migrate-links 保存日志到文件：    migrate-links -l "ko ja" -s

  20. 用您的仓库 URL 个性化 README 语言部分提示：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 评估示例

> [!WARNING]  
> <strong>测试版功能</strong>：评估功能目前处于测试阶段。该功能用于评估翻译文档，评估方法及其详细实现仍在开发中，可能会有变动。

  1. 评估韩文翻译： evaluate -l "ko"

  2. 以自定义置信度阈值进行评估： evaluate -l "ko" -c 0.8

  3. 快速评估（仅基于规则）： evaluate -l "ko" -f

  4. 深度评估（仅基于大模型）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译生成。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或错误解读，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->