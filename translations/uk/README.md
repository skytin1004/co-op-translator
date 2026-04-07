# Co-op Translator

_Легко автоматизуйте та підтримуйте переклади вашого освітнього контенту на GitHub кількома мовами у міру розвитку вашого проєкту._

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

### 🌐 Підтримка багатомовності

#### Підтримується [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](./README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Віддаєте перевагу клонувати локально?**
>
> Цей репозиторій містить понад 50 мовних перекладів, що значно збільшує обсяг завантаження. Щоб клонувати без перекладів, використовуйте sparse checkout:
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
> Це дає вам усе, що потрібно для проходження курсу, із набагато швидшим завантаженням.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Огляд

**Co-op Translator** допомагає легко локалізувати ваш освітній контент на GitHub кількома мовами.
Коли ви оновлюєте файли Markdown, зображення чи ноутбуки, переклади автоматично синхронізуються, забезпечуючи точність і актуальність контенту для навчальних по всьому світу.

Приклад організації перекладеного контенту:

![Example](../../imgs/translation-ex.png)

## Як керується стан перекладу

Co-op Translator управляє перекладеним контентом як **версійними програмними артефактами**,  
а не як статичними файлами.

Інструмент відслідковує стан перекладених Markdown, зображень та ноутбуків
з використанням **метаданих з урахуванням мови**.

Такий підхід дозволяє Co-op Translator:

- Надійно виявляти застарілі переклади
- Однорідно працювати з Markdown, зображеннями та ноутбуками
- Безпечно масштабуватися на великих, швидкозмінних багатомовних репозиторіях

Моделюючи переклади як керовані артефакти,
робочі процеси перекладу природньо узгоджуються з сучасними
практиками управління залежностями та артефактами в розробці ПЗ.

→ [Як керується стан перекладу](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Швидкий старт

```bash
# Створіть і активуйте віртуальне оточення (рекомендовано)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Встановіть пакет
pip install co-op-translator
# Перекласти
translate -l "ko ja fr" -md
```

Docker:

```bash
# Завантажте публічне зображення з GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Запустіть з підключеною поточною папкою та наданим файлом .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Мінімальна настройка

1. Переконайтесь, що у вас встановлена підтримувана версія Python (зараз 3.10-3.12). У poetry (pyproject.toml) це налаштовується автоматично.
2. Створіть файл `.env` за шаблоном: [.env.template](../../.env.template)
3. Налаштуйте одного провайдера LLM (Azure OpenAI або OpenAI)
4. (Опціонально) Для перекладу зображень (`-img`) налаштуйте Azure AI Vision
5. (Опціонально) Ви можете налаштувати кілька наборів облікових даних, дублюючи змінні з суфіксами на кшталт `_1`, `_2` тощо. Усі змінні в наборі мають однаковий суфікс.
6. (Рекомендовано) Очистіть будь-які попередні переклади, щоб уникнути конфліктів (наприклад, `translations/`)
7. (Рекомендовано) Додайте розділ про переклад у ваш README, використовуючи [шаблон мов для README](./getting_started/README_languages_template.md)
8. Див. також: [Налаштування Azure AI](./getting_started/set-up-azure-ai.md)

## Використання

Перекладайте всі підтримувані типи:

```bash
translate -l "ko ja"
```

Лише Markdown:

```bash
translate -l "de" -md
```

Markdown + зображення:

```bash
translate -l "pt" -md -img
```

Лише ноутбуки:

```bash
translate -l "zh" -nb
```

Більше прапорців: [Довідник команд](./getting_started/command-reference.md)

## Можливості

- Автоматичний переклад Markdown, ноутбуків та зображень
- Синхронізація перекладів зі змінами в джерелі
- Працює локально (CLI) або в CI (GitHub Actions)
- Використовує Azure OpenAI або OpenAI; опційно Azure AI Vision для зображень
- Зберігає форматування та структуру Markdown

## Документація

- [Посібник командного рядка](./getting_started/command-line-guide/command-line-guide.md)
- [Посібник GitHub Actions (публічні репозиторії та стандартні секрети)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Посібник GitHub Actions (репозиторії організації Microsoft та налаштування на рівні організації)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Шаблон мов для README](./getting_started/README_languages_template.md)
- [Підтримувані мови](./getting_started/supported-languages.md)
- [Як внести свій внесок](./CONTRIBUTING.md)
- [Усунення неполадок](./getting_started/troubleshooting.md)

### Специфічний посібник Microsoft
> [!NOTE]
> Для підтримувачів репозиторіїв Microsoft «Для початківців» лише.

- [Оновлення списку «інші курси» (лише для репозиторіїв MS Beginners)](./getting_started/update-other-courses.md)

## Підтримайте нас і сприяйте глобальному навчанню

Приєднуйтеся до нас у революції обміну освітнім контентом у світі! Подаруйте [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ на GitHub і підтримайте нашу місію подолання мовних бар’єрів у навчанні та технологіях. Ваша зацікавленість і внесок мають значний вплив! Внески коду та пропозиції щодо функцій завжди вітаються.

### Досліджуйте освітній контент Microsoft вашою мовою

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

## Відео презентації

👉 Натисніть на зображення нижче, щоб подивитися на YouTube.

- **Open at Microsoft**: Коротке 18-хвилинне введення та швидкий посібник із використання Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Внесок

Цей проєкт вітає внески та пропозиції. Бажаєте сприяти розвитку Azure Co-op Translator? Будь ласка, ознайомтеся з нашим [CONTRIBUTING.md](./CONTRIBUTING.md), щоб дізнатися, як допомогти зробити Co-op Translator більш доступним.

## Учасники

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведінки

Цей проєкт прийняв [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Для отримання додаткової інформації див. [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) або звертайтеся за адресою [opencode@microsoft.com](mailto:opencode@microsoft.com) з будь-якими додатковими питаннями чи коментарями.

## Відповідальний Штучний Інтелект

Microsoft прагне допомагати нашим клієнтам відповідально використовувати наші продукти ШІ, ділитися нашими знаннями та будувати партнерства, засновані на довірі, за допомогою таких інструментів, як Примітки прозорості та Оцінки впливу. Багато цих ресурсів можна знайти за адресою [https://aka.ms/RAI](https://aka.ms/RAI).  
Підхід Microsoft до відповідального ШІ базується на наших принципах ШІ: справедливість, надійність і безпека, конфіденційність і безпека, інклюзивність, прозорість і підзвітність.

Великі моделі природної мови, зображень і мовлення - як, наприклад, ті, що використовуються в цьому прикладі - можуть потенційно діяти несправедливо, ненадійно або образливо, що може викликати шкоду. Будь ласка, ознайомтеся з [Приміткою прозорості служби Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб дізнатися про ризики та обмеження.

Рекомендований підхід до зменшення цих ризиків — включити у вашу архітектуру систему безпеки, яка може виявляти та запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами або ШІ, у застосунках та службах. Azure AI Content Safety включає API для тексту та зображень, які дозволяють виявляти шкідливі матеріали. Ми також маємо інтерактивний Content Safety Studio, який дозволяє переглядати, досліджувати та випробовувати приклади коду для виявлення шкідливого контенту в різних модальностях. Наступна [документація швидкого початку](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) допоможе вам здійснювати запити до служби.

Ще одним аспектом є загальна продуктивність застосунку. У мультимодальних і мультимодельних застосунках ми розглядаємо продуктивність як відповідність системи вашим і користувацьким очікуванням, у тому числі недопущення генерації шкідливих результатів. Важливо оцінити продуктивність вашого загального застосунку, використовуючи [метрики якості генерації, ризиків і безпеки](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Ви можете оцінити свій ШІ-застосунок у середовищі розробки, використовуючи [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Використовуючи тестовий набір даних або ціль, генерації вашого генеративного застосунку ШІ кількісно оцінюють за допомогою вбудованих або власних оцінювачів за вашим вибором. Щоб розпочати роботу з prompt flow sdk для оцінки вашої системи, ви можете слідувати [керівництву швидкого початку](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після запуску оцінки ви можете [візуалізувати результати в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торгові марки

У цьому проєкті можуть міститися торгові марки або логотипи проєктів, продуктів чи послуг. Авторизоване використання торгових марок або логотипів Microsoft підпорядковується та має відповідати [Правилам використання торгових марок та брендів Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Використання торгових марок або логотипів Microsoft у змінених версіях цього проєкту не повинно викликати плутанину або створювати враження спонсорства Microsoft.  
Використання торгових марок або логотипів третіх сторін підпорядковується політикам цих третіх сторін.

## Отримання допомоги

Якщо у вас виникли труднощі або питання щодо створення AI-застосунків, приєднуйтеся до:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Якщо у вас є відгуки про продукт чи помилки при створенні, відвідайте:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо враховувати, що автоматичні переклади можуть містити помилки чи неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильне тлумачення, що можуть виникнути внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->