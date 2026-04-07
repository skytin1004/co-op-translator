# Co-op Translator

_轻松自动化并维护您的教育类 GitHub 内容在多个语言中的翻译，随着项目的发展同步更新。_

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 多语言支持

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 支持

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语 (Myanmar)](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../zh-HK/README.md) | [中文（繁体，澳门）](../zh-MO/README.md) | [中文（繁体，台湾）](../zh-TW/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [爱沙尼亚语](../et/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印度尼西亚语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [卡纳达语](../kn/README.md) | [高棉语](../km/README.md) | [韩语](../ko/README.md) | [立陶宛语](../lt/README.md) | [马来语](../ms/README.md) | [马拉雅拉姆语](../ml/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [尼日利亚皮钦语](../pcm/README.md) | [挪威语](../no/README.md) | [波斯语 (Farsi)](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../pt-BR/README.md) | [葡萄牙语（葡萄牙）](../pt-PT/README.md) | [旁遮普语（古鲁穆奇）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔字母）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰米尔语](../ta/README.md) | [泰卢固语](../te/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)

> **更愿意本地克隆？**
>
> 本仓库包含50多个语言的翻译，下载体积较大。若想不包含翻译进行克隆，可使用稀疏检出：
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 这样您能快速获得完成课程所需的所有内容，下载速度更快。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概述

**Co-op Translator** 帮助您轻松将教育类 GitHub 内容本地化为多种语言。
当您更新 Markdown 文件、图片或笔记本时，翻译会自动同步，确保您的内容始终准确且保持最新，为全球学习者提供支持。

翻译内容的组织示例：

![示例](../../imgs/translation-ex.png)

## 翻译状态如何管理

Co-op Translator 将翻译内容作为 <strong>有版本的软件工件</strong> 管理，  
而非静态文件。

该工具使用 <strong>语言范围的元数据</strong> 跟踪翻译的 Markdown、图片和笔记本的状态。

此设计使 Co-op Translator 能够：

- 可靠地检测过期的翻译
- 一致地处理 Markdown、图片和笔记本
- 安全地扩展到大型、快速变化、多语言的仓库

通过将翻译建模为受控工件，
翻译流程自然契合现代
软件依赖和工件管理实践。

→ [如何管理翻译状态](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 快速开始

```bash
# 创建并激活虚拟环境（推荐）
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 安装软件包
pip install co-op-translator
# 翻译
translate -l "ko ja fr" -md
```

Docker:

```bash
# 从 GHCR 拉取公共镜像
docker pull ghcr.io/azure/co-op-translator:latest
# 运行时挂载当前文件夹并提供 .env（Bash/Zsh）
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最小配置

1. 确认您使用支持的 Python 版本（当前支持 3.10-3.12）。在 poetry（pyproject.toml）中会自动处理。
2. 使用模板创建 `.env` 文件: [.env.template](../../.env.template)
3. 配置一个 LLM 提供商（Azure OpenAI 或 OpenAI）
4. （可选）配置 Azure AI Vision，用于图片翻译（`-img`）
5. （可选）可以通过添加变量后缀，如 `_1`, `_2` 等，配置多个凭据集。每个集内的变量须共享相同后缀。
6. （推荐）清理之前的翻译内容，避免冲突（如 `translations/`）
7. （推荐）在 README 添加翻译部分，使用 [README languages 模板](./getting_started/README_languages_template.md)
8. 查看：[设置 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

翻译所有支持类型：

```bash
translate -l "ko ja"
```

仅 Markdown：

```bash
translate -l "de" -md
```

Markdown + 图片：

```bash
translate -l "pt" -md -img
```

仅笔记本：

```bash
translate -l "zh" -nb
```

更多参数选项：[命令参考](./getting_started/command-reference.md)

## 功能

- 自动翻译 Markdown、笔记本及图片
- 保持翻译与源内容同步
- 本地（CLI）或 CI（GitHub Actions）均可使用
- 使用 Azure OpenAI 或 OpenAI；图片支持 Azure AI Vision（可选）
- 保留 Markdown 格式及结构

## 文档

- [命令行指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公共仓库与标准密钥）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（微软组织仓库及组织级设置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 语言模板](./getting_started/README_languages_template.md)
- [支持的语言](./getting_started/supported-languages.md)
- [贡献指南](./CONTRIBUTING.md)
- [疑难解答](./getting_started/troubleshooting.md)

### 微软专用指南
> [!NOTE]
> 仅针对微软“初学者”仓库的维护者。

- [更新“其他课程”列表（仅限 MS 初学者仓库）](./getting_started/update-other-courses.md)

## 支持我们并推动全球学习

加入我们，革新教育内容的全球共享方式！请在 GitHub 上给 [Co-op Translator](https://github.com/azure/co-op-translator) 点⭐，支持我们打破语言障碍、促进学习和技术传播的使命。您的关注和贡献意义重大！欢迎代码贡献和功能建议。

### 探索微软教育内容的您的语言版本

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 视频演示

👉 点击下方图片，在 YouTube 上观看。

- **Open at Microsoft**：一段简短的18分钟介绍及快速指南，教您如何使用 Co-op Translator。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 贡献

欢迎对本项目进行贡献和提出建议。想为 Azure Co-op Translator 贡献力量？请查看我们的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何帮助 Co-op Translator 更易于访问。

## 贡献者
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行为准则

本项目已采用 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。  
有关更多信息，请参阅 [行为准则常见问题](https://opensource.microsoft.com/codeofconduct/faq/) 或  
通过 [opencode@microsoft.com](mailto:opencode@microsoft.com) 联系我们，提出任何额外的问题或意见。

## 负责任的 AI

微软致力于帮助客户负责任地使用我们的 AI 产品，分享我们的经验教训，通过 Transparency Notes 和 Impact Assessments 等工具建立基于信任的合作伙伴关系。许多这些资源可以在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。  
微软的负责任 AI 方法基于我们的 AI 原则：公平、可靠与安全、隐私与安全性、包容性、透明度和问责制。

大规模自然语言、图像和语音模型——如本示例中使用的模型——可能会表现出不公平、不可靠或冒犯性的行为，从而导致伤害。请查阅 [Azure OpenAI 服务透明度说明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)，了解风险和限制。

减轻这些风险的推荐方法是在您的架构中包含一个安全系统，可以检测和防止有害行为。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供独立的保护层，能够检测应用和服务中的有害用户生成和 AI 生成内容。Azure AI Content Safety 包括文本和图像 API，可帮助您检测有害材料。此外，我们还提供了一个互动式内容安全工作室，允许您查看、探索并尝试用于检测不同模态有害内容的示例代码。以下 [快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 将指导您如何向服务发出请求。

另一个需要考虑的方面是整体应用性能。对于多模态和多模型应用，我们认为性能意味着系统按您和您的用户预期执行，包括不生成有害输出。使用 [生成质量和风险及安全指标](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) 评估整体应用性能非常重要。

您可以使用 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 在开发环境中评估您的 AI 应用。无论是测试数据集还是目标，您的生成式 AI 产出都可以通过内置评估器或您自定义的评估器进行定量衡量。要开始使用 prompt flow sdk 评估系统，您可以参阅 [快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估运行后，您可以[在 Azure AI Studio 中可视化结果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商标

本项目可能包含项目、产品或服务的商标或徽标。微软商标或徽标的授权使用须遵循并符合  
[微软商标和品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。  
在本项目的修改版本中使用微软商标或徽标不得引起混淆或暗示微软赞助。  
任何第三方商标或徽标的使用均需遵守该第三方的政策。

## 获取帮助

如果您遇到困难或有任何有关构建 AI 应用的问题，请加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在构建过程中有产品反馈或错误报告，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力追求准确性，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误用，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->