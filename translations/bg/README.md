# Co-op Translator

_Лесно автоматизирайте и поддържайте преводите на вашето образователно съдържание в GitHub на множество езици, докато вашият проект се развива._

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

### 🌐 Многоезична поддръжка

#### Поддържано от [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабски](../ar/README.md) | [Бенгалски](../bn/README.md) | [Български](./README.md) | [Бирмански (Мианмар)](../my/README.md) | [Китайски (опростен)](../zh-CN/README.md) | [Китайски (традиционен, Хонг Конг)](../zh-HK/README.md) | [Китайски (традиционен, Макао)](../zh-MO/README.md) | [Китайски (традиционен, Тайван)](../zh-TW/README.md) | [Хърватски](../hr/README.md) | [Чешки](../cs/README.md) | [Датски](../da/README.md) | [Нидерландски](../nl/README.md) | [Естонски](../et/README.md) | [Фински](../fi/README.md) | [Френски](../fr/README.md) | [Немски](../de/README.md) | [Гръцки](../el/README.md) | [Иврит](../he/README.md) | [Хинди](../hi/README.md) | [Унгарски](../hu/README.md) | [Индонезийски](../id/README.md) | [Италиански](../it/README.md) | [Японски](../ja/README.md) | [Каннада](../kn/README.md) | [Кхмер](../km/README.md) | [Корейски](../ko/README.md) | [Литовски](../lt/README.md) | [Малайски](../ms/README.md) | [Малаялам](../ml/README.md) | [Марати](../mr/README.md) | [Непалски](../ne/README.md) | [Нигерийски Пиджин](../pcm/README.md) | [Норвежки](../no/README.md) | [Персийски (Фарси)](../fa/README.md) | [Полски](../pl/README.md) | [Португалски (Бразилия)](../pt-BR/README.md) | [Португалски (Португалия)](../pt-PT/README.md) | [Пенджабски (Гурмуки)](../pa/README.md) | [Румънски](../ro/README.md) | [Руски](../ru/README.md) | [Сръбски (кирилица)](../sr/README.md) | [Словашки](../sk/README.md) | [Словенски](../sl/README.md) | [Испански](../es/README.md) | [Суахили](../sw/README.md) | [Шведски](../sv/README.md) | [Тагалог (Филипински)](../tl/README.md) | [Тамилски](../ta/README.md) | [Телугу](../te/README.md) | [Тайски](../th/README.md) | [Турски](../tr/README.md) | [Украински](../uk/README.md) | [Урду](../ur/README.md) | [Виетнамски](../vi/README.md)

> **Предпочитате да клонирате локално?**
>
> Това хранилище включва преводи на над 50 езика, което значително увеличава размера на изтегляне. За да клонирате без преводи, използвайте рядък чек-аут:
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
> Това ви дава всичко необходимо за завършване на курса с много по-бързо изтегляне.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Преглед

**Co-op Translator** ви помага лесно да локализирате вашето образователно съдържание в GitHub на множество езици.  
Когато обновявате Markdown файлове, изображения или тетрадки, преводите се синхронизират автоматично, като гарантират, че вашето съдържание остава точно и актуално за учащите по целия свят.

Пример как е организирано преведеното съдържание:

![Example](../../translated_images/bg/translation-ex.0c8aa6a7ee0aad2b.webp)

## Как се управлява състоянието на превода

Co-op Translator управлява преведеното съдържание като **версионирани софтуерни артефакти**,  
а не като статични файлове.

Инструментът следи състоянието на преведените Markdown файлове, изображения и тетрадки  
чрез **метаданни със специфичен езиков обхват**.

Този дизайн позволява на Co-op Translator да:

- Надеждно открива остарели преводи
- Третира Markdown, изображения и тетрадки по еднакъв начин
- Масшабира безопасно в големи, бързо променящи се, многоезични хранилища

Чрез моделиране на преводите като управлявани артефакти,  
работните процеси за превод естествено се подравняват със съвременните практики  
за управление на зависимости и артефакти в софтуера.

→ [Как се управлява състоянието на превода](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Бърз старт

```bash
# Създайте и активирайте виртуална среда (препоръчително)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Инсталирайте пакета
pip install co-op-translator
# Преведете
translate -l "ko ja fr" -md
```

Docker:

```bash
# Изтеглете публичното изображение от GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Стартирайте с монтирано текущо съдържание и предоставен .env файл (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Минимална конфигурация

1. Уверете се, че имате поддържана версия на Python (в момента 3.10-3.12). В poetry (pyproject.toml) това се обработва автоматично.
2. Създайте файл `.env` по шаблона: [.env.template](../../.env.template)
3. Конфигурирайте един LLM доставчик (Azure OpenAI или OpenAI)
4. (По избор) За превод на изображения (`-img`), конфигурирайте Azure AI Vision
5. (По избор) Можете да конфигурирате множество набори от идентификационни данни, като дублирате променливи с суфикси като `_1`, `_2` и т.н. Всички променливи в един набор трябва да споделят един и същ суфикс.
6. (Препоръчително) Изчистете всякакви предишни преводи, за да избегнете конфликти (например в `translations/`)
7. (Препоръчително) Добавете секция за преводи към вашето README, като използвате [шаблона за езици в README](./getting_started/README_languages_template.md)
8. Вижте: [Конфигуриране на Azure AI](./getting_started/set-up-azure-ai.md)

## Използване

Превежда всички поддържани типове:

```bash
translate -l "ko ja"
```

Само Markdown:

```bash
translate -l "de" -md
```

Markdown + изображения:

```bash
translate -l "pt" -md -img
```

Само тетрадки:

```bash
translate -l "zh" -nb
```

Още флагове: [Референция за командите](./getting_started/command-reference.md)

## Характеристики

- Автоматизиран превод на Markdown, тетрадки и изображения
- Поддържа преводите синхронизирани с промените в източника
- Работи локално (CLI) или в CI (GitHub Actions)
- Използва Azure OpenAI или OpenAI; по избор Azure AI Vision за изображения
- Запазва форматирането и структурата на Markdown

## Документация

- [Ръководство за командния ред](./getting_started/command-line-guide/command-line-guide.md)
- [Ръководство за GitHub Actions (публични хранилища и стандартни тайни)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Ръководство за GitHub Actions (хранилища на Microsoft организацията и настройки на ниво организация)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Шаблон за езици в README](./getting_started/README_languages_template.md)
- [Поддържани езици](./getting_started/supported-languages.md)
- [Принос](./CONTRIBUTING.md)
- [Отстраняване на проблеми](./getting_started/troubleshooting.md)

### Ръководство специфично за Microsoft
> [!NOTE]
> Само за поддръжници на Microsoft хранилищата „За начинаещи“.

- [Обновяване на списъка с „други курсове“ (само за хранилища на Microsoft За начинаещи)](./getting_started/update-other-courses.md)

## Подкрепете ни и насърчете глобалното обучение

Присъединете се към нас в революционизирането на начина, по който образователното съдържание се споделя глобално! Дайте ⭐ на [Co-op Translator](https://github.com/azure/co-op-translator) в GitHub и подкрепете нашата мисия да премахнем езиковите бариери в ученето и технологиите. Вашият интерес и принос имат голямо значение! Приносите с код и предложенията за функционалности са винаги добре дошли.

### Разгледайте образователното съдържание на Microsoft на вашия език

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

👉 Кликнете върху изображението по-долу, за да гледате в YouTube.

- **Open at Microsoft**: Кратко 18-минутно въведение и бързо ръководство как да използвате Co-op Translator.

  [![Open at Microsoft](../../translated_images/bg/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Принос

Този проект приветства приноси и предложения. Интересувате се да допринесете за Azure Co-op Translator? Моля, вижте нашия [CONTRIBUTING.md](./CONTRIBUTING.md) за насоки как можете да помогнете да направим Co-op Translator по-достъпен.

## Съединители
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс на поведение

Този проект е приел [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
За повече информация вижте [Често задавани въпроси за Кодекса на поведение](https://opensource.microsoft.com/codeofconduct/faq/) или
свържете се с [opencode@microsoft.com](mailto:opencode@microsoft.com) за допълнителни въпроси или коментари.

## Отговорен AI

Microsoft е ангажирана да помага на клиентите си да използват нашите AI продукти отговорно, да споделя наученото и да изгражда партньорства, базирани на доверие, чрез инструменти като Transparency Notes и Impact Assessments. Много от тези ресурси могат да бъдат намерени на [https://aka.ms/RAI](https://aka.ms/RAI).
Подходът на Microsoft към отговорния AI е основан на нашите AI принципи за справедливост, надеждност и безопасност, поверителност и сигурност, приобщаване, прозрачност и отчетност.

Големи модели за естествен език, изображения и реч - като тези, използвани в този пример - могат потенциално да се държат по начини, които са несправедливи, ненадеждни или обидни, което може да причини вреди. Моля, консултирайте се с [бележката за прозрачност на Azure OpenAI услугата](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), за да сте информирани за рисковете и ограниченията.

Препоръчителният подход за намаляване на тези рискове е да включите система за безопасност във вашата архитектура, която може да открива и предотвратява вредно поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставя независим слой защита, способен да открива вредно съдържание, генерирано от потребители и AI, в приложения и услуги. Azure AI Content Safety включва текстови и изображенски API, които ви позволяват да откривате материал, който е вреден. Имаме също така интерактивно Content Safety Studio, което ви позволява да разглеждате, изследвате и изпробвате примерен код за откриване на вредно съдържание в различни модалности. Следната [документация за бързо стартиране](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ви води през правенето на заявки към услугата.

Друг аспект, който трябва да се вземе предвид, е общото представяне на приложението. При мултимодални и мултимоделни приложения, представянето означава, че системата функционира така, както вие и вашите потребители очакват, включително и да не генерира вредни резултати. Важно е да оцените представянето на вашето цялостно приложение, използвайки [метрики за качество на генериране и риск и безопасност](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Можете да оцените вашето AI приложение в средата за разработка, използвайки [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Като имате тестов набор от данни или цел, вашите генерирани резултати от generative AI приложението се измерват количествено с вградени оценители или персонализирани оценители по ваш избор. За да започнете с prompt flow sdk за оценка на вашата система, може да следвате [ръководството за бързо стартиране](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). След като изпълните оценъчно стартиране, можете да [визуализирате резултатите в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Търговски марки

Този проект може да съдържа търговски марки или лога на проекти, продукти или услуги. Разрешената употреба на търговски марки или лога на Microsoft подлежи и трябва да следва
[Марковите и бранд насоки на Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Използването на търговски марки или лога на Microsoft в модифицирани версии на този проект не трябва да причинява объркване или да предполага спонсорство от Microsoft.
Всяка употреба на търговски марки или лога на трети страни подлежи на политиките на тези трети страни.

## Получаване на помощ

Ако се затрудните или имате въпроси за изграждането на AI приложения, присъединете се към:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ако имате обратна връзка за продукта или грешки по време на разработката, посетете:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->