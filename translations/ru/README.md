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
> В этом репозитории есть более 50 переводов на различные языки, что значительно увеличивает размер загрузки. Чтобы клонировать без переводов, используйте sparse checkout:
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
> Это даст вам всё необходимое для прохождения курса с гораздо более быстрой загрузкой.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Обзор

**Co-op Translator** помогает вам без труда локализовать ваш образовательный контент на GitHub на несколько языков.  
Когда вы обновляете свои Markdown файлы, изображения или ноутбуки, переводы автоматически синхронизируются, гарантируя актуальность и точность контента для учащихся по всему миру.

Пример организации переведённого контента:

![Example](../../imgs/translation-ex.png)

## Как управляется состояние перевода

Co-op Translator управляет переведённым контентом как **версионированными артефактами программного обеспечения**,  
а не как статическими файлами.

Инструмент отслеживает состояние переведённых Markdown, изображений и ноутбуков  
с помощью **метаданных, заданных для каждого языка**.

Этот подход позволяет Co-op Translator:

- Надёжно обнаруживать устаревшие переводы
- Обрабатывать Markdown, изображения и ноутбуки последовательно
- Безопасно масштабироваться в крупных, быстро меняющихся мульти-язычных репозиториях

Моделируя переводы как управляемые артефакты,  
рабочие процессы перевода естественно согласуются с современными  
практиками управления зависимостями и артефактами программного обеспечения.

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
# Загрузить публичный образ из GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Запустить с текущей папкой в качестве монтирования и предоставленным .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Минимальная настройка

1. Убедитесь, что у вас установлена поддерживаемая версия Python (в настоящее время 3.10-3.12). В poetry (pyproject.toml) это происходит автоматически.
2. Создайте файл `.env` на основе шаблона: [.env.template](../../.env.template)
3. Настройте одного провайдера LLM (Azure OpenAI или OpenAI)
4. (Опционально) Для перевода изображений (`-img`) настройте Azure AI Vision
5. (Опционально) Вы можете настроить несколько наборов учетных данных, продублировав переменные с суффиксами `_1`, `_2` и т.д. Все переменные в наборе должны иметь одинаковый суффикс.
6. (Рекомендуется) Очистите предыдущие переводы, чтобы избежать конфликтов (например, `translations/`)
7. (Рекомендуется) Добавьте раздел перевода в README, используя шаблон [README languages template](./getting_started/README_languages_template.md)
8. Смотрите: [Настройка Azure AI](./getting_started/set-up-azure-ai.md)

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

Дополнительные флаги: [Справочник команд](./getting_started/command-reference.md)

## Возможности

- Автоматический перевод Markdown, ноутбуков и изображений
- Поддержание синхронизации переводов с изменениями исходников
- Работа локально (CLI) или в CI (GitHub Actions)
- Использование Azure OpenAI или OpenAI; опционально Azure AI Vision для изображений
- Сохраняет форматирование и структуру Markdown

## Документация

- [Руководство по командной строке](./getting_started/command-line-guide/command-line-guide.md)
- [Руководство по GitHub Actions (публичные репозитории и стандартные секреты)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Руководство по GitHub Actions (репозитории организации Microsoft и настройки на уровне организации)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Шаблон языков в README](./getting_started/README_languages_template.md)
- [Поддерживаемые языки](./getting_started/supported-languages.md)
- [Как внести вклад](./CONTRIBUTING.md)
- [Поиск и устранение неполадок](./getting_started/troubleshooting.md)

### Руководство для Microsoft
> [!NOTE]
> Только для поддерживающих репозитории Microsoft “For Beginners”.

- [Обновление списка «других курсов» (только для репозиториев MS Beginners)](./getting_started/update-other-courses.md)

## Поддержите нас и способствуйте глобальному обучению

Присоединяйтесь к революции в распространении образовательного контента по всему миру! Поставьте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub и поддержите нашу миссию по устранению языковых барьеров в обучении и технологиях. Ваш интерес и вклад имеют важное значение! Приглашаем кода и предложения по функционалу.

### Исследуйте образовательный контент Microsoft на вашем языке

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD для начинающих](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI для начинающих](https://github.com/microsoft/edgeai-for-beginners)
- [Протокол контекста модели (MCP) для начинающих](https://github.com/microsoft/mcp-for-beginners)
- [AI агенты для начинающих](https://github.com/microsoft/ai-agents-for-beginners)
- [Генеративный AI для начинающих на .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Генеративный AI для начинающих](https://github.com/microsoft/generative-ai-for-beginners)
- [Генеративный AI для начинающих на Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML для начинающих](https://aka.ms/ml-beginners)
- [Data Science для начинающих](https://aka.ms/datascience-beginners)
- [AI для начинающих](https://aka.ms/ai-beginners)
- [Кибербезопасность для начинающих](https://github.com/microsoft/Security-101)
- [Веб-разработка для начинающих](https://aka.ms/webdev-beginners)
- [IoT для начинающих](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Видео презентации

👉 Нажмите на изображение ниже, чтобы посмотреть на YouTube.

- **Open at Microsoft**: Краткое 18-минутное введение и быстрое руководство по использованию Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Внесение вклада

Этот проект приветствует вклады и предложения. Хотите помочь развитию Azure Co-op Translator? Пожалуйста, ознакомьтесь с [CONTRIBUTING.md](./CONTRIBUTING.md) для инструкций о том, как сделать Co-op Translator более доступным.

## Участники проекта
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведения

Этот проект принял [Кодекс поведения с открытым исходным кодом Microsoft](https://opensource.microsoft.com/codeofconduct/).
Для получения дополнительной информации смотрите [Часто задаваемые вопросы о Кодексе поведения](https://opensource.microsoft.com/codeofconduct/faq/) или
свяжитесь с [opencode@microsoft.com](mailto:opencode@microsoft.com) по любым дополнительным вопросам или комментариям.

## Ответственный ИИ

Microsoft стремится помочь нашим клиентам ответственно использовать наши продукты ИИ, делиться нашим опытом и строить партнёрства на основе доверия с помощью таких инструментов, как Transparency Notes и Impact Assessments. Многие из этих ресурсов можно найти по адресу [https://aka.ms/RAI](https://aka.ms/RAI).
Подход Microsoft к ответственному ИИ основан на наших принципах ИИ: справедливость, надежность и безопасность, конфиденциальность и безопасность, инклюзивность, прозрачность и подотчетность.

Крупномасштабные модели естественного языка, изображений и речи — такие, как использованные в этом примере — потенциально могут вести себя несправедливо, ненадежно или оскорбительно, что, в свою очередь, может причинять вред. Пожалуйста, ознакомьтесь с [Прозрачностью сервиса Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы быть проинформированными о рисках и ограничениях.

Рекомендуемый подход к снижению этих рисков — включить в архитектуру систему безопасности, способную обнаруживать и предотвращать вредное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, способный обнаруживать вредоносный пользовательский и сгенерированный ИИ контент в приложениях и сервисах. Azure AI Content Safety включает текстовые и графические API, которые позволяют обнаруживать вредоносные материалы. У нас также есть интерактивная Content Safety Studio, которая позволяет просматривать, изучать и пробовать пример кода для обнаружения вредоносного контента в разных форматах. Следующая [документация быстрого начала](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) поможет вам сделать запросы к сервису.

Еще один аспект, который нужно учитывать — общая производительность приложения. В приложениях с мультимодальными и мультимодельными функциями мы считаем производительность способностью системы работать так, как вы и ваши пользователи ожидаете, включая недопущение генерации вредного вывода. Важно оценивать производительность вашего приложения с использованием [метрик качества генерации и рисков безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Вы можете оценить свое AI-приложение в вашей среде разработки с помощью [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Имея тестовый набор данных или цель, генерации вашего генеративного AI приложения количественно измеряются встроенными или пользовательскими оценщиками по вашему выбору. Чтобы начать работу с prompt flow sdk для оценки вашей системы, вы можете следовать [руководству быстрого старта](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После завершения оценки, вы можете [визуализировать результаты в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торговые марки

В этом проекте могут содержаться торговые марки или логотипы проектов, продуктов или сервисов. Авторизованное использование торговых марок или логотипов Microsoft регулируется и должно соответствовать
[Руководству Microsoft по торговым маркам и брендам](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Использование торговых марок или логотипов Microsoft в изменённых версиях этого проекта не должно вызывать путаницу или подразумевать спонсорство Microsoft.
Любое использование торговых марок или логотипов третьих сторон подчиняется правилам этих сторон.

## Получение помощи

Если вы застряли или у вас есть вопросы по созданию AI-приложений, присоединяйтесь:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Если у вас есть отзывы о продукте или ошибки при создании, посетите:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->