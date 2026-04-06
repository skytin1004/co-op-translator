# Co-op Translator

_Легко автоматизируйте и поддерживайте переводы вашего образовательного контента на GitHub на нескольких языках по мере развития вашего проекта._

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

### 🌐 Поддержка нескольких языков

#### Поддерживается [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](./README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Предпочитаете клонировать локально?**
>
> Этот репозиторий включает более 50 языков переводов, что значительно увеличивает размер загрузки. Чтобы клонировать без переводов, используйте sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Это даст вам всё необходимое для завершения курса с гораздо более быстрой загрузкой.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Обзор

**Co-op Translator** помогает вам легко локализовать ваш образовательный контент на GitHub на несколько языков.
Когда вы обновляете файлы Markdown, изображения или ноутбуки, переводы автоматически синхронизируются, гарантируя, что ваш контент остаётся точным и актуальным для обучающихся по всему миру.

Пример организации переведённого контента:

![Example](../../translated_images/ru/translation-ex.0c8aa6a7ee0aad2b.webp)

## Как управляется состояние перевода

Co-op Translator управляет переведённым контентом как **версионируемыми программными артефактами**,  
а не как статическими файлами.

Инструмент отслеживает состояние переведённых Markdown, изображений и ноутбуков,
используя **метаданные с областью действия по языку**.

Этот подход позволяет Co-op Translator:

- Надёжно обнаруживать устаревшие переводы
- Обрабатывать Markdown, изображения и ноутбуки единообразно
- Безопасно масштабироваться в крупных, быстро развивающихся многоязычных репозиториях

Моделируя переводы как управляемые артефакты,
рабочие процессы перевода естественным образом соответствуют современным
практикам управления зависимостями и артефактами программного обеспечения.

→ [Как управляется состояние перевода](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Быстрый старт

```bash
# Создайте и активируйте виртуальное окружение (рекомендуется)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Установите пакет
pip install co-op-translator
# Перевести
translate -l "ko ja fr" -md
```

Docker:

```bash
# Загрузите публичный образ из GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Запустите с подключенной текущей папкой и предоставленным .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Минимальная настройка

1. Убедитесь, что у вас установлена поддерживаемая версия Python (в настоящее время 3.10-3.12). В poetry (pyproject.toml) это обрабатывается автоматически.
2. Создайте файл `.env`, используя шаблон: [.env.template](../../.env.template)
3. Настройте одного провайдера LLM (Azure OpenAI или OpenAI)
4. (Опционально) Для перевода изображений (`-img`) настройте Azure AI Vision
5. (Опционально) Вы можете настроить несколько наборов учётных данных, продублировав переменные с суффиксами, например `_1`, `_2` и т.д. Все переменные в наборе должны иметь одинаковый суффикс.
6. (Рекомендуется) Удалите предыдущие переводы, чтобы избежать конфликтов (например, `translations/`)
7. (Рекомендуется) Добавьте раздел перевода в ваш README, используя [шаблон языков для README](./getting_started/README_languages_template.md)
8. См.: [Настройка Azure AI](./getting_started/set-up-azure-ai.md)

## Использование

Перевод всех поддерживаемых типов:

```bash
translate -l "ko ja"
```

Только Markdown:

```bash
translate -l "de" -md
```

Markdown + изображения:

```bash
translate -l "pt" -md -img
```

Только ноутбуки:

```bash
translate -l "zh" -nb
```

Больше флагов: [Справочник команд](./getting_started/command-reference.md)

## Возможности

- Автоматизированный перевод для Markdown, ноутбуков и изображений
- Поддерживает синхронизацию переводов с изменениями в исходниках
- Работает локально (CLI) или в CI (GitHub Actions)
- Использует Azure OpenAI или OpenAI; опционально Azure AI Vision для изображений
- Сохраняет форматирование и структуру Markdown

## Документация

- [Руководство по командной строке](./getting_started/command-line-guide/command-line-guide.md)
- [Руководство по GitHub Actions (публичные репозитории и стандартные секреты)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Руководство по GitHub Actions (репозитории организации Microsoft и организационные настройки)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Шаблон языков для README](./getting_started/README_languages_template.md)
- [Поддерживаемые языки](./getting_started/supported-languages.md)
- [Участие в проекте](./CONTRIBUTING.md)
- [Устранение неполадок](./getting_started/troubleshooting.md)

### Руководство для Microsoft
> [!NOTE]
> Только для сопровождающих репозитории Microsoft “Для начинающих”.

- [Обновление списка «других курсов» (только для репозиториев MS Beginners)](./getting_started/update-other-courses.md)

## Поддержите нас и способствуйте глобальному обучению

Присоединяйтесь к нам в революционизации обмена образовательным контентом по всему миру! Поставьте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub и поддержите нашу миссию по устранению языковых барьеров в обучении и технологиях. Ваш интерес и вклад имеют большое значение! Мы всегда рады вашим кода и предложениям по функциям.

### Изучайте образовательный контент Microsoft на вашем языке

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

## Видео презентации

👉 Нажмите на изображение ниже, чтобы посмотреть на YouTube.

- **Open at Microsoft**: Краткое 18-минутное введение и быстрое руководство по использованию Co-op Translator.

  [![Open at Microsoft](../../translated_images/ru/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Участие в проекте

Этот проект приветствует ваш вклад и предложения. Хотите внести свой вклад в Azure Co-op Translator? Пожалуйста, ознакомьтесь с нашими [CONTRIBUTING.md](./CONTRIBUTING.md) для инструкций о том, как вы можете помочь сделать Co-op Translator более доступным.

## Участники проекта
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведения

Этот проект принял [Кодекс поведения с открытым исходным кодом Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Для получения дополнительной информации см. [Часто задаваемые вопросы о Кодексе поведения](https://opensource.microsoft.com/codeofconduct/faq/) или свяжитесь с [opencode@microsoft.com](mailto:opencode@microsoft.com) для любых дополнительных вопросов или комментариев.

## Ответственный ИИ

Microsoft стремится помочь нашим клиентам ответственно использовать наши продукты ИИ, делиться нашими знаниями и строить партнерские отношения, основанные на доверии, с помощью таких инструментов, как Заметки о прозрачности и Оценки воздействия. Многие из этих ресурсов можно найти по адресу [https://aka.ms/RAI](https://aka.ms/RAI).  
Подход Microsoft к ответственному ИИ основан на наших принципах ИИ: справедливости, надежности и безопасности, конфиденциальности и безопасности, инклюзивности, прозрачности и подотчетности.

Крупномасштабные модели естественного языка, изображения и речи — такие, как в этом примере — потенциально могут вести себя несправедливо, ненадежно или оскорбительно, что может привести к ущербу. Пожалуйста, ознакомьтесь с [Заметкой о прозрачности сервиса Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы быть в курсе рисков и ограничений.

Рекомендуемый подход к снижению этих рисков — включить в архитектуру систему безопасности, которая может обнаруживать и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, способный обнаруживать вредоносный контент, созданный пользователями и ИИ, в приложениях и службах. Azure AI Content Safety включает API для текста и изображений, которые позволяют обнаруживать вредоносный материал. Также у нас есть интерактивная Студия Безопасности Контента, которая позволяет просматривать, исследовать и пробовать примеры кода для обнаружения вредоносного контента в разных модальностях. Следующая [документация быстрого старта](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) проведет вас через процесс выполнения запросов к сервису.

Еще одним аспектом, который следует учитывать, является общая производительность приложения. В многомодальных и многомодельных приложениях под производительностью понимается, что система работает так, как ожидают вы и ваши пользователи, включая отсутствие генерации вредоносных результатов. Важно оценивать производительность вашего приложения в целом, используя [метрики качества генерации, риска и безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Вы можете оценить свое ИИ-приложение в среде разработки, используя [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Имея тестовый набор данных или цель, результаты генерации вашего генеративного ИИ приложения количественно измеряются встроенными или пользовательскими оценщиками. Чтобы начать использовать prompt flow sdk для оценки вашей системы, вы можете следовать [руководству быстрого старта](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После выполнения оценки вы можете [визуализировать результаты в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торговые марки

Этот проект может содержать торговые марки или логотипы проектов, продуктов или услуг. Разрешенное использование торговых марок или логотипов Microsoft регулируется и должно соответствовать [Руководству Microsoft по торговым маркам и бренду](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Использование торговых марок или логотипов Microsoft в изменённых версиях этого проекта не должно вводить в заблуждение или подразумевать спонсорство Microsoft.  
Любое использование торговых марок или логотипов третьих сторон подчиняется политике этих третьих сторон.

## Получение помощи

Если у вас возникли трудности или есть вопросы по созданию ИИ-приложений, присоединяйтесь к:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Если у вас есть отзывы о продукте или сообщения об ошибках при разработке, посетите:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие при использовании данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->