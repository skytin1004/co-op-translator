# 更新“其他课程”部分（Microsoft Beginners 仓库）

本指南说明如何使用 Co‑op Translator 自动同步“其他课程”部分，以及如何更新所有仓库的全局模板。

- 适用范围：仅限 Microsoft Beginners 仓库
- 适用工具：Co‑op Translator CLI 和 GitHub Actions
- 模板来源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速开始：在你的仓库中启用自动同步

在你的 README 中“其他课程”部分周围添加以下标记。Co‑op Translator 会在每次运行时替换这些标记之间的所有内容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co‑op Translator 运行时——无论是通过 CLI（例如，`translate -l "<language codes>"`）还是 GitHub Actions——都会自动更新被这些标记包裹的“其他课程”部分。

> [!NOTE]
> 如果你已有现成列表，只需用相同标记包裹即可。下一次运行时，它将用最新的标准化内容替换。

---

## 如何更改全局内容

如果你想更新出现在所有 Beginners 仓库中的标准化内容：

1. 编辑模板：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 提交一个包含你更改的 pull request 到 Co-op Translator 仓库
3. PR 合并后，Co‑op Translator 版本将更新
4. 下一次 Co‑op Translator 在目标仓库中运行（无论 CLI 还是 GitHub Action）时，会自动同步更新后的部分

这样可以确保所有 Beginners 仓库中的“其他课程”内容有唯一的权威来源。

## 仓库大小

由于翻译成多种语言，仓库可能变得很大，旨在帮助终端用户指导如何使用 clone - sparse 只克隆必要的语言，而非整个仓库

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
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但自动翻译可能包含错误或不准确之处。请以原始语言的文档为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->