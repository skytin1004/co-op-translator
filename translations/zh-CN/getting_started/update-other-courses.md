# 更新“其他课程”部分（Microsoft Beginners 仓库）

本指南解释了如何使用 Co‑op Translator 使“其他课程”部分自动同步，以及如何更新所有仓库的全局模板。

- 适用范围：仅限 Microsoft Beginners 仓库
- 适用工具：Co‑op Translator CLI 和 GitHub Actions
- 模板来源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速开始：在你的仓库中启用自动同步

在 README 中的“其他课程”部分周围添加以下标记。Co‑op Translator 会在每次运行时替换这些标记之间的所有内容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co‑op Translator 运行时——无论是通过 CLI（例如，`translate -l "<language codes>"`）还是 GitHub Actions——都会自动更新这些标记包裹的“其他课程”部分。

> [!NOTE]
> 如果你已经有现成的列表，只需用相同的标记包裹它。下一次运行时将用最新的标准内容替换它。

---

## 如何更改全局内容

如果你想更新所有 Beginners 仓库中出现的标准化内容：

1. 编辑模板：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 提交包含你的更改的 pull request 到 Co-op Translator 仓库
3. PR 合并后，Co‑op Translator 版本会被更新
4. 下一次 Co‑op Translator 在目标仓库中运行（无论 CLI 还是 GitHub Action），都会自动同步更新的部分

这确保了“其他课程”内容在所有 Beginners 仓库中的单一可信源。

## 仓库大小

仓库可能因为支持多语言翻译而变得庞大，方便最终用户使用 clone - sparse 仅克隆必要的语言，而不是整个仓库。

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
**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力追求准确性，但请注意自动翻译可能包含错误或不准确之处。原始文档的本地语言版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用此翻译而产生的任何误解或误释，概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->