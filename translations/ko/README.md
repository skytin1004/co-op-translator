# Co-op Translator

_프로젝트가 진화함에 따라 교육용 GitHub 콘텐츠를 여러 언어로 쉽고 자동화하여 유지 관리하세요._

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

### 🌐 다국어 지원

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator)에서 지원

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](./README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **로컬 복제를 선호하시나요?**
>
> 이 저장소는 50개 이상의 언어 번역본을 포함하여 다운로드 크기가 크게 증가합니다. 번역본 없이 클론하려면 sparse checkout을 사용하세요:
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
> 이렇게 하면 더 빠른 다운로드로 코스를 완료하는 데 필요한 모든 것을 얻을 수 있습니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 개요

<strong>Co-op Translator</strong>는 교육용 GitHub 콘텐츠를 여러 언어로 손쉽게 현지화할 수 있도록 도와줍니다.  
Markdown 파일, 이미지 또는 노트북을 업데이트할 때, 번역본은 자동으로 동기화되어 전 세계 학습자들에게 정확하고 최신 상태의 콘텐츠를 제공합니다.

번역된 콘텐츠가 구성되는 예시:

![Example](../../translated_images/ko/translation-ex.0c8aa6a7ee0aad2b.webp)

## 번역 상태 관리 방식

Co-op Translator는 번역된 콘텐츠를 <strong>버전 관리되는 소프트웨어 아티팩트</strong>로 관리하며,  
정적인 파일로 관리하지 않습니다.

이 도구는 <strong>언어별 메타데이터</strong>를 사용해 번역된 Markdown, 이미지, 노트북 상태를 추적합니다.

이 설계 덕분에 Co-op Translator는 다음을 가능하게 합니다:

- 오래된 번역본을 신뢰성 있게 감지
- Markdown, 이미지, 노트북을 일관되게 처리
- 크고 빠르게 변화하는 다국어 저장소에 안전하게 확장

번역을 관리된 아티팩트로 모델링함으로써,  
번역 워크플로가 최신 소프트웨어 종속성 및 아티팩트 관리 관행과 자연스럽게 맞닿습니다.

→ [번역 상태 관리 방식 자세히 보기](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## 빠른 시작

```bash
# 가상 환경 생성 및 활성화 (권장)
python -m venv .venv
# 윈도우
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 패키지 설치
pip install co-op-translator
# 번역하기
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR에서 공개 이미지를 가져옵니다
docker pull ghcr.io/azure/co-op-translator:latest
# 현재 폴더를 마운트하고 .env를 제공하여 실행합니다 (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## 최소 설정

1. 지원되는 Python 버전(현재 3.10-3.12)을 확인하세요. poetry(pyproject.toml)에서는 자동으로 처리됩니다.
2. 템플릿을 사용하여 `.env` 파일을 만드세요: [.env.template](../../.env.template)
3. LLM 공급자 한 곳(Azure OpenAI 또는 OpenAI)을 설정하세요
4. (선택사항) 이미지 번역(`-img`)용 Azure AI Vision을 구성하세요
5. (선택사항) 접미사로 `_1`, `_2` 등 여러 자격 증명 세트를 복제하여 구성할 수 있습니다. 세트 내 모든 변수는 같은 접미사를 가져야 합니다.
6. (권장) 충돌을 방지하기 위해 이전 번역본을 정리하세요 (예: `translations/`)
7. (권장) [README 언어 템플릿](./getting_started/README_languages_template.md)을 사용해 README에 번역 섹션을 추가하세요
8. 참조: [Azure AI 설정](./getting_started/set-up-azure-ai.md)

## 사용법

지원되는 모든 유형 번역:

```bash
translate -l "ko ja"
```

Markdown만 번역:

```bash
translate -l "de" -md
```

Markdown + 이미지:

```bash
translate -l "pt" -md -img
```

노트북만 번역:

```bash
translate -l "zh" -nb
```

추가 플래그: [명령어 참고](./getting_started/command-reference.md)

## 기능

- Markdown, 노트북, 이미지 자동 번역
- 원본 변경에 따라 번역 자동 동기화 유지
- 로컬(CLI) 또는 CI(GitHub Actions)에서 사용 가능
- Azure OpenAI 또는 OpenAI 사용; 이미지에는 선택적 Azure AI Vision 사용
- Markdown 형식 및 구조 보존

## 문서

- [명령줄 가이드](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions 가이드 (공개 저장소 및 표준 시크릿)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions 가이드 (Microsoft 조직 저장소 및 조직 레벨 설정)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README 언어 템플릿](./getting_started/README_languages_template.md)
- [지원 언어](./getting_started/supported-languages.md)
- [기여하기](./CONTRIBUTING.md)
- [문제 해결](./getting_started/troubleshooting.md)

### Microsoft 전용 가이드
> [!NOTE]
> Microsoft “For Beginners” 저장소 관리자만 해당합니다.

- [“other courses” 목록 업데이트 (MS Beginners 저장소 전용)](./getting_started/update-other-courses.md)

## 저희를 지원하고 글로벌 학습을 촉진하세요

교육 콘텐츠가 전 세계적으로 공유되는 방식을 혁신하는 데 동참하세요!  
[Co-op Translator](https://github.com/azure/co-op-translator)에 GitHub에서 ⭐를 주시고, 학습과 기술의 언어 장벽을 허무는 사명을 응원해 주세요. 여러분의 관심과 기여가 큰 임팩트를 만듭니다! 코드 기여와 기능 제안도 언제나 환영합니다.

### 여러분의 언어로 된 Microsoft 교육 콘텐츠 탐색

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

## 비디오 발표

👉 아래 이미지를 클릭해 YouTube에서 시청하세요.

- **Open at Microsoft**: Co-op Translator 사용법을 간단히 소개하는 18분 분량 안내 영상입니다.

  [![Open at Microsoft](../../translated_images/ko/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 기여하기

이 프로젝트는 기여 및 제안을 환영합니다. Azure Co-op Translator에 기여하고 싶으시다면,  
[CONTRIBUTING.md](./CONTRIBUTING.md)에서 기여 지침을 확인해 주세요.

## 기여자들
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 행동 강령

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다.
자세한 내용은 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하거나,
추가 질문이나 의견이 있는 경우 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 연락해 주세요.

## 책임 있는 AI

Microsoft는 고객이 AI 제품을 책임감 있게 사용할 수 있도록 지원하고, 학습 내용을 공유하며, Transparency Notes 및 Impact Assessments와 같은 도구를 통해 신뢰 기반의 파트너십을 구축하는 데 전념하고 있습니다. 이러한 리소스 중 많은 부분은 [https://aka.ms/RAI](https://aka.ms/RAI)에서 찾아볼 수 있습니다.
Microsoft의 책임 있는 AI 접근 방식은 공정성, 신뢰성 및 안전성, 프라이버시 및 보안, 포용성, 투명성, 책임성이라는 AI 원칙에 기초하고 있습니다.

이 샘플에 사용된 것과 같은 대규모 자연어, 이미지, 음성 모델은 불공정하거나 신뢰할 수 없거나 공격적으로 행동할 가능성이 있으며, 이는 해를 초래할 수 있습니다. 위험과 한계에 대해 알기 위해 [Azure OpenAI 서비스 Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참고해 주세요.

이러한 위험을 완화하는 권장 방법은 유해한 행동을 감지하고 방지할 수 있는 안전 시스템을 아키텍처에 포함하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 애플리케이션과 서비스 내에서 사용자 생성 및 AI 생성의 유해 콘텐츠를 감지할 수 있는 독립적인 보호 계층을 제공합니다. Azure AI Content Safety에는 유해한 자료를 감지할 수 있는 텍스트 및 이미지 API가 포함되어 있습니다. 또한 다양한 모달리티에서 유해 콘텐츠를 감지하는 샘플 코드를 보고 탐색하며 사용해 볼 수 있는 대화형 Content Safety Studio도 갖추고 있습니다. 다음의 [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)는 서비스에 요청을 하는 절차를 안내합니다.

또 다른 고려 사항은 전체 애플리케이션 성능입니다. 다중 모달 및 다중 모델 애플리케이션의 경우, 성능이란 시스템이 사용자와 귀하가 기대하는 대로 작동하는 것을 의미하며, 여기에는 유해한 결과를 생성하지 않는 것도 포함됩니다. 전체 애플리케이션의 성능을 평가할 때는 [생성 품질 및 위험 및 안전 지표](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)를 사용하는 것이 중요합니다.

개발 환경에서 AI 애플리케이션을 평가하려면 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html)를 사용할 수 있습니다. 테스트 데이터셋이나 목표가 주어지면, 귀하의 생성형 AI 애플리케이션 결과는 내장 평가자 또는 선택한 맞춤 평가자를 사용해 정량적으로 측정됩니다. prompt flow sdk를 사용하여 시스템을 평가하는 방법에 관해 시작하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 참고하세요. 평가 실행을 완료하면 [Azure AI Studio에서 결과를 시각화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)할 수 있습니다.

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함되어 있을 수 있습니다. Microsoft 상표 또는 로고의 정식 사용은 [Microsoft 상표 및 브랜드 가이드라인](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)을 준수해야 합니다.
변경된 버전의 프로젝트에서 Microsoft 상표 또는 로고를 사용하는 경우 혼동을 초래하거나 Microsoft의 후원을 암시하지 않아야 합니다.
서드파티 상표 또는 로고의 사용은 해당 서드파티 정책의 적용을 받습니다.

## 도움 받기

AI 앱 개발에 어려움을 겪거나 질문이 있을 경우 다음에 참여하세요:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

제품 피드백이나 빌드 중 오류가 발생한 경우 다음을 방문하세요:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문가에 의한 인간 번역을 권장합니다. 본 번역의 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->