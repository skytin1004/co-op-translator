<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:27:46+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# Co-op Translator

_轻松自动化翻译你的教育类 GitHub 内容，覆盖全球用户。_

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

#### 由 [Co-op Translator](https://github.com/Azure/Co-op-Translator) 提供支持

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，台湾）](../tw/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [爱沙尼亚语](../et/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印尼语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) | [立陶宛语](../lt/README.md) | [马来语](../ms/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [尼日利亚皮钦语](../pcm/README.md) | [挪威语](../no/README.md) | [波斯语](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../br/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [旁遮普语（古尔穆奇文）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰米尔语](../ta/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 项目简介

**Co-op Translator** 可以帮你快速将教育类 GitHub 内容翻译成多种语言，让全球用户都能轻松访问。当你更新 Markdown 文件、图片或 Jupyter 笔记本时，翻译内容会自动同步，确保你的教育内容始终新鲜、适合国际用户。

看看 Co-op Translator 如何组织翻译后的教育内容：

![示例](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.zh.png)

## 快速开始

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 最简配置

- 使用模板创建 `.env` 文件：[.env.template](../../.env.template)
- 配置一个 LLM 提供商（Azure OpenAI 或 OpenAI）
- 如果需要图片翻译（`-img`），还需设置 Azure AI Vision
- 推荐：如果你有其他工具生成的翻译，建议先清理（比如：`translations/`），避免冲突
- 推荐：在 README 中添加翻译语言区块，参考 [README 语言模板](./README_languages_template.md)
- 参考：[设置 Azure AI](./getting_started/set-up-azure-ai.md)

## 使用方法

翻译所有支持的类型：

```bash
translate -l "ko ja"
```

只翻译 Markdown：

```bash
translate -l "de" -md
```

Markdown + 图片：

```bash
translate -l "pt" -md -img
```

只翻译笔记本：

```bash
translate -l "zh" -nb
```

更多参数见：[命令参考](./getting_started/command-reference.md)

## 功能亮点

- 自动翻译 Markdown、笔记本和图片
- 翻译内容与源文件变动自动同步
- 支持本地（CLI）和 CI（GitHub Actions）运行
- 支持 Azure OpenAI 或 OpenAI，可选 Azure AI Vision 处理图片
- 保持 Markdown 格式和结构不变

## 文档

- [命令行指南](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 指南（公开仓库 & 标准密钥）](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 指南（微软组织仓库 & 组织级配置）](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [支持的语言](./getting_started/supported-languages.md)
- [故障排查](./getting_started/troubleshooting.md)

## 支持我们，助力全球学习

欢迎加入我们，一起推动教育内容全球共享！在 GitHub 上为 [Co-op Translator](https://github.com/azure/co-op-translator) 点个 ⭐，支持我们打破学习和技术的语言壁垒。你的关注和贡献非常重要！欢迎代码贡献和功能建议。

### 用你的语言探索微软教育内容

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

## 视频介绍

通过我们的演示视频进一步了解 Co-op Translator _(点击下方图片跳转 YouTube)_：

- **Open at Microsoft**：18 分钟简要介绍及快速上手指南

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.zh.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 贡献指南

欢迎大家贡献和提出建议。想参与 Azure Co-op Translator 项目？请查阅我们的 [CONTRIBUTING.md](./CONTRIBUTING.md)，了解如何让 Co-op Translator 更易用。

## 贡献者

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行为准则

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。
更多信息请参阅 [行为准则 FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
如有疑问请联系 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 负责任的 AI

微软致力于帮助客户负责任地使用我们的 AI 产品，分享我们的经验，并通过透明说明和影响评估等工具建立信任。相关资源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 查阅。
微软的负责任 AI 方法基于公平、可靠与安全、隐私与安全、包容性、透明度和问责制等原则。

大规模自然语言、图像和语音模型（如本项目使用的模型）有可能出现不公平、不可靠或令人反感的行为，可能带来伤害。请查阅 [Azure OpenAI 服务透明说明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)，了解相关风险和限制。

建议的风险缓解方法是在你的架构中加入安全系统，检测并阻止有害行为。[Azure AI 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供了独立的保护层，能检测应用和服务中的有害用户生成内容和 AI 生成内容。Azure AI 内容安全包括文本和图片 API，可检测有害信息。我们还提供了交互式内容安全工作室，方便你查看、探索和试用不同模态下的有害内容检测代码。以下 [快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 可指导你如何调用服务。
另一个需要考虑的方面是整体应用性能。对于多模态和多模型应用，我们认为性能是指系统能够按照你和用户的预期运行，包括不会生成有害内容。评估你的整体应用性能时，建议参考[生成质量以及风险和安全指标](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。

你可以在开发环境中使用[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)来评估你的 AI 应用。无论是测试数据集还是目标，生成式 AI 应用的输出都可以通过内置评估器或你自定义的评估器进行量化评估。要开始使用 prompt flow sdk 评估你的系统，可以参考[快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估后，你可以在[Azure AI Studio 中可视化结果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商标

本项目可能包含项目、产品或服务的商标或标志。微软商标或标志的授权使用需遵守
[微软商标与品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本项目的修改版本中使用微软商标或标志时，不得造成混淆或暗示微软赞助。
任何第三方商标或标志的使用需遵守相关第三方政策。

## 获取帮助

如果你在构建 AI 应用时遇到问题或有疑问，欢迎加入：

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

如果你有产品反馈或在构建过程中遇到错误，请访问：

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。