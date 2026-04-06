# Co-op Translator

_Легко автоматизуйте та підтримуйте переклади вашого освітнього GitHub-контенту кількома мовами в міру розвитку вашого проєкту._

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

### 🌐 Підтримка кількох мов

#### Підтримується [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабська](../ar/README.md) | [Бенгальська](../bn/README.md) | [Болгарська](../bg/README.md) | [Бірманська (М’янма)](../my/README.md) | [Китайська (спрощена)](../zh-CN/README.md) | [Китайська (традиційна, Гонконг)](../zh-HK/README.md) | [Китайська (традиційна, Макао)](../zh-MO/README.md) | [Китайська (традиційна, Тайвань)](../zh-TW/README.md) | [Хорватська](../hr/README.md) | [Чеська](../cs/README.md) | [Данська](../da/README.md) | [Нідерландська](../nl/README.md) | [Естонська](../et/README.md) | [Фінська](../fi/README.md) | [Французька](../fr/README.md) | [Німецька](../de/README.md) | [Грецька](../el/README.md) | [Іврит](../he/README.md) | [Гінді](../hi/README.md) | [Угорська](../hu/README.md) | [Індонезійська](../id/README.md) | [Італійська](../it/README.md) | [Японська](../ja/README.md) | [Каннада](../kn/README.md) | [Кхмер](../km/README.md) | [Корейська](../ko/README.md) | [Литовська](../lt/README.md) | [Малайська](../ms/README.md) | [Малаялам](../ml/README.md) | [Маратхі](../mr/README.md) | [Непальська](../ne/README.md) | [Нігерійський піджин](../pcm/README.md) | [Норвезька](../no/README.md) | [Перська (фарсі)](../fa/README.md) | [Польська](../pl/README.md) | [Португальська (Бразилія)](../pt-BR/README.md) | [Португальська (Португалія)](../pt-PT/README.md) | [Пенджабі (Гурмухі)](../pa/README.md) | [Румунська](../ro/README.md) | [Російська](../ru/README.md) | [Сербська (кирилиця)](../sr/README.md) | [Словацька](../sk/README.md) | [Словенська](../sl/README.md) | [Іспанська](../es/README.md) | [Свахілі](../sw/README.md) | [Шведська](../sv/README.md) | [Тагалог (філіппінська)](../tl/README.md) | [Тамільська](../ta/README.md) | [Телугу](../te/README.md) | [Тайська](../th/README.md) | [Турецька](../tr/README.md) | [Українська](./README.md) | [Урду](../ur/README.md) | [В’єтнамська](../vi/README.md)

> **Віддаєте перевагу клонувати локально?**
>
> Цей репозиторій містить понад 50 мовних перекладів, що значно збільшує розмір завантаження. Щоб клонувати без перекладів, скористайтеся розрідженим checkout:
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
> Це дасть вам усе необхідне для завершення курсу з набагато швидшим завантаженням.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Огляд

**Co-op Translator** допомагає легко локалізувати ваш освітній GitHub-контент кількома мовами.
Коли ви оновлюєте Markdown-файли, зображення або нотатники, переклади автоматично синхронізуються, забезпечуючи точність і актуальність контенту для учнів у всьому світі.

Приклад організації перекладеного контенту:

![Example](../../translated_images/uk/translation-ex.0c8aa6a7ee0aad2b.webp)

## Як управляється стан перекладу

Co-op Translator управляє перекладеним контентом як **версійованими програмними артефактами**,  
а не статичними файлами.

Інструмент відстежує стан перекладеного Markdown, зображень і нотатників
за допомогою **метаданих, обмежених мовою**.

Таке рішення дозволяє Co-op Translator:

- Надійно виявляти застарілі переклади
- Послідовно обробляти Markdown, зображення та нотатники
- Безпечно масштабуватися у великих, швидкозмінних багатомовних репозиторіях

Завдяки моделюванню перекладів як керованих артефактів,
робочі процеси перекладу природно узгоджуються з сучасними
практиками управління залежностями та артефактами в програмному забезпеченні.

→ [Як управляється стан перекладу](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Швидкий старт

```bash
# Створіть та активуйте віртуальне середовище (рекомендується)
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
# Завантажити публічний образ з GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Запустити з примонтованою поточною папкою і наданим файлом .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Мінімальне налаштування

1. Переконайтесь, що у вас встановлена підтримувана версія Python (наразі 3.10-3.12). У poetry (pyproject.toml) це налаштовується автоматично.
2. Створіть файл `.env` за шаблоном: [.env.template](../../.env.template)
3. Налаштуйте одного провайдера LLM (Azure OpenAI або OpenAI)
4. (За бажанням) Для перекладу зображень (`-img`) налаштуйте Azure AI Vision
5. (За бажанням) Ви можете налаштувати кілька наборів даних для аутентифікації, дублюючи змінні з суфіксами на кшталт `_1`, `_2` тощо. Всі змінні в наборі мають мати однаковий суфікс.
6. (Рекомендується) Очистіть попередні переклади, щоб уникнути конфліктів (наприклад, `translations/`)
7. (Рекомендується) Додайте розділ «Переклади» у ваш README, використовуючи [шаблон мов для README](./getting_started/README_languages_template.md)
8. Дивіться: [Налаштування Azure AI](./getting_started/set-up-azure-ai.md)

## Використання

Перекласти всі підтримувані типи:

```bash
translate -l "ko ja"
```

Тільки Markdown:

```bash
translate -l "de" -md
```

Markdown + зображення:

```bash
translate -l "pt" -md -img
```

Тільки нотатники:

```bash
translate -l "zh" -nb
```

Більше опцій: [Довідник команд](./getting_started/command-reference.md)

## Особливості

- Автоматичний переклад Markdown, нотатників і зображень
- Підтримує синхронізацію перекладів з вихідними змінами
- Працює локально (CLI) або в CI (GitHub Actions)
- Використовує Azure OpenAI або OpenAI; опційно Azure AI Vision для зображень
- Зберігає форматування та структуру Markdown

## Документація

- [Посібник з командного рядка](./getting_started/command-line-guide/command-line-guide.md)
- [Посібник GitHub Actions (публічні репозиторії і стандартні секрети)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Посібник GitHub Actions (репозиторії організації Microsoft та організаційні налаштування)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Шаблон мов README](./getting_started/README_languages_template.md)
- [Підтримувані мови](./getting_started/supported-languages.md)
- [Співпраця](./CONTRIBUTING.md)
- [Усунення несправностей](./getting_started/troubleshooting.md)

### Специфічний посібник для Microsoft
> [!NOTE]
> Лише для підтримувачів репозиторіїв Microsoft “For Beginners”.

- [Оновлення списку «інших курсів» (лише для репозиторіїв MS Beginners)](./getting_started/update-other-courses.md)

## Підтримайте нас і сприяйте глобальному навчанню

Приєднуйтесь до нас у революції поширення освітнього контенту по всьому світу! Поставте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub та підтримайте нашу місію зруйнувати мовні бар’єри у навчанні та технологіях. Ваша зацікавленість і внески мають значний вплив! Внески у код та пропозиції щодо функцій завжди вітаються.

### Ознайомтеся з освітнім контентом Microsoft вашою мовою

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

## Відеопрезентації

👉 Натисніть на зображення нижче, щоб переглянути на YouTube.

- **Open at Microsoft**: Коротке 18-хвилинне введення та швидкий посібник з використання Co-op Translator.

  [![Open at Microsoft](../../translated_images/uk/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Співпраця

Цей проєкт вітає внески та пропозиції. Зацікавлені зробити внесок у Azure Co-op Translator? Будь ласка, ознайомтеся з нашим [CONTRIBUTING.md](./CONTRIBUTING.md) для інструкцій, як ви можете допомогти зробити Co-op Translator більш доступним.

## Учасники проекту
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведінки

Цей проєкт прийняв [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Для отримання додаткової інформації див. [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) або  
зв’яжіться за адресою [opencode@microsoft.com](mailto:opencode@microsoft.com) з будь-якими додатковими питаннями чи коментарями.

## Відповідальний ШІ

Microsoft прагне допомогти своїм клієнтам відповідально використовувати наші продукти ШІ, ділитися нашими знаннями та будувати партнерства на основі довіри за допомогою таких інструментів, як Transparency Notes та Impact Assessments. Багато з цих ресурсів можна знайти за адресою [https://aka.ms/RAI](https://aka.ms/RAI).  
Підхід Microsoft до відповідального ШІ ґрунтується на наших принципах ШІ: справедливість, надійність і безпека, конфіденційність і безпека, інклюзивність, прозорість і підзвітність.

Великомасштабні моделі природної мови, зображень і мови — як ті, що використовуються в цьому прикладі — потенційно можуть поводитися несправедливо, ненадійно або образливо, що може спричинити шкоду. Будь ласка, ознайомтеся з [Transparency note служби Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб бути поінформованими про ризики та обмеження.

Рекомендований підхід до пом'якшення цих ризиків полягає в тому, щоб включити в архітектуру систему безпеки, яка може виявляти та запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами та ШІ в додатках і службах. Azure AI Content Safety включає текстові та графічні API, які дозволяють визначати шкідливі матеріали. У нас також є інтерактивна Content Safety Studio, яка дозволяє переглядати, досліджувати та випробовувати приклади коду для виявлення шкідливого контенту в різних модальностях. Наступна [документація для швидкого старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) проведе вас через виконання запитів до служби.

Ще одним аспектом, який слід врахувати, є загальна продуктивність додатка. У багатомодальних і багатомодельних додатках продуктивність означає, що система працює так, як ви та ваші користувачі очікують, включаючи відсутність генерації шкідливих результатів. Важливо оцінити продуктивність вашого загального додатка за допомогою [метрик якості генерації, ризиків і безпеки](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Ви можете оцінити свій додаток ШІ у середовищі розробки за допомогою [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Задано тестовий набір даних або ціль, генерації вашого генеративного додатка ШІ кількісно оцінюються за допомогою вбудованих або обраних власних оцінювачів. Щоб розпочати роботу з prompt flow sdk для оцінки вашої системи, ви можете слідувати [інструкції для швидкого старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після виконання оцінювання ви можете [візуалізувати результати в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торгові марки

Цей проєкт може містити торгові марки або логотипи проєктів, продуктів чи послуг. Авторизоване використання торгових марок або логотипів Microsoft підпорядковується та повинне відповідати [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Використання торгових марок або логотипів Microsoft у модифікованих версіях цього проєкту не повинно спричиняти плутанину або створювати враження спонсорства Microsoft.  
Використання торгових марок або логотипів третіх сторін підпорядковується політикам цих третіх сторін.

## Отримання допомоги

Якщо ви застрягли або маєте питання щодо створення додатків ШІ, приєднуйтеся до:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Якщо у вас є відгуки про продукт або помилки під час розробки, відвідайте:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->