<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T14:15:00+00:00",
  "source_file": "README.md",
  "language_code": "uk"
}
-->
# Co-op Translator

_Автоматизуйте переклад вашого освітнього контенту на GitHub на різні мови, щоб охопити світову аудиторію._

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

### 🌐 Підтримка багатьох мов

#### Підтримується [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](./README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Огляд

**Co-op Translator** дозволяє швидко перекладати ваш освітній контент на GitHub на різні мови, щоб легко охопити світову аудиторію. Коли ви оновлюєте свої Markdown-файли, зображення чи Jupyter-ноутбуки, переклади автоматично синхронізуються, щоб ваш освітній контент на GitHub залишався актуальним для міжнародних користувачів.

Ось як Co-op Translator організовує перекладений освітній контент на GitHub:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.uk.png)

## Швидкий старт

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

## Мінімальне налаштування

- Створіть `.env` за шаблоном: [.env.template](../../.env.template)
- Налаштуйте одного постачальника LLM (Azure OpenAI або OpenAI)
- Для перекладу зображень (`-img`) також налаштуйте Azure AI Vision
- Рекомендовано: Якщо у вас вже є переклади, створені іншими інструментами, спочатку видаліть їх, щоб уникнути конфліктів (наприклад: `translations/`).
- Рекомендовано: Додайте розділ перекладів у ваш README, використовуючи [README languages template](./README_languages_template.md)
- Дивіться: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

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

Тільки ноутбуки:

```bash
translate -l "zh" -nb
```

Більше прапорців: [Command reference](./getting_started/command-reference.md)

## Можливості

- Автоматичний переклад Markdown, ноутбуків та зображень
- Синхронізація перекладів при зміні джерела
- Працює локально (CLI) або в CI (GitHub Actions)
- Використовує Azure OpenAI або OpenAI; опціонально Azure AI Vision для зображень
- Зберігає форматування та структуру Markdown

## Документація

- [Посібник з командного рядка](./getting_started/command-line-guide/command-line-guide.md)
- [Посібник з GitHub Actions (публічні репозиторії та стандартні секрети)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Посібник з GitHub Actions (репозиторії організації Microsoft та організаційні налаштування)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Підтримувані мови](./getting_started/supported-languages.md)
- [Вирішення проблем](./getting_started/troubleshooting.md)

## Підтримайте нас і сприяйте глобальному навчанню

Долучайтеся до революції у поширенні освітнього контенту по всьому світу! Поставте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub і підтримайте нашу місію — подолати мовні бар’єри у навчанні та технологіях. Ваш інтерес і внески мають велике значення! Ми завжди відкриті до пропозицій та внесків у код.

### Досліджуйте освітній контент Microsoft вашою мовою

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

Дізнайтеся більше про Co-op Translator з наших презентацій _(Натисніть на зображення нижче, щоб переглянути на YouTube.)_:

- **Open at Microsoft**: Коротке 18-хвилинне ознайомлення та швидкий гайд по використанню Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.uk.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Внесок

Проєкт відкритий для внесків та пропозицій. Хочете долучитися до Azure Co-op Translator? Ознайомтеся з [CONTRIBUTING.md](./CONTRIBUTING.md) для рекомендацій, як зробити Co-op Translator ще доступнішим.

## Учасники

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведінки

У цьому проєкті діє [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Детальніше дивіться [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) або
звертайтеся на [opencode@microsoft.com](mailto:opencode@microsoft.com) з додатковими питаннями чи коментарями.

## Відповідальний AI

Microsoft прагне допомагати клієнтам відповідально використовувати наші AI-продукти, ділитися досвідом і будувати партнерські відносини на основі довіри через такі інструменти, як Transparency Notes та Impact Assessments. Багато з цих ресурсів доступні за адресою [https://aka.ms/RAI](https://aka.ms/RAI).
Підхід Microsoft до відповідального AI базується на принципах справедливості, надійності та безпеки, конфіденційності та захисту, інклюзивності, прозорості та відповідальності.

Великі моделі для обробки природної мови, зображень і голосу — як ті, що використовуються у цьому прикладі — можуть поводитися несправедливо, ненадійно чи образливо, що може призвести до шкоди. Ознайомтеся з [Transparency note для Azure OpenAI service](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб знати про ризики та обмеження.

Рекомендований спосіб зменшення ризиків — включити систему безпеки у вашу архітектуру, яка може виявляти та запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами чи AI, у додатках та сервісах. Azure AI Content Safety містить API для тексту та зображень, які дозволяють виявляти шкідливі матеріали. Також є інтерактивна Content Safety Studio, де можна переглядати, досліджувати та тестувати приклади коду для виявлення шкідливого контенту у різних форматах. Ось [документація для швидкого старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest), яка допоможе зробити запити до сервісу.


Ще один аспект, який варто враховувати, — це загальна продуктивність застосунку. У багатомодальних і багатомодельних застосунках продуктивність означає, що система працює так, як очікуєте ви та ваші користувачі, зокрема не генерує шкідливих результатів. Важливо оцінювати продуктивність вашого застосунку за допомогою [метрик якості генерації, ризиків і безпеки](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Ви можете оцінити ваш AI-застосунок у середовищі розробки за допомогою [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Маючи тестовий набір даних або ціль, генерації вашого генеративного AI-застосунку кількісно вимірюються вбудованими або власними оцінювачами на ваш вибір. Щоб почати використовувати prompt flow sdk для оцінки вашої системи, скористайтеся [інструкцією для швидкого старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після запуску оцінювання ви можете [переглянути результати в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торговельні марки

Цей проєкт може містити торговельні марки або логотипи проєктів, продуктів чи сервісів. Дозволене використання торговельних марок або логотипів Microsoft регулюється та має відповідати
[Вказівкам щодо торговельних марок і бренду Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Використання торговельних марок або логотипів Microsoft у змінених версіях цього проєкту не повинно вводити в оману або створювати враження, що Microsoft підтримує цей проєкт.
Будь-яке використання торговельних марок або логотипів третіх сторін регулюється політикою відповідних третіх сторін.

## Допомога

Якщо у вас виникли труднощі або питання щодо створення AI-застосунків, приєднуйтесь до:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Якщо у вас є відгуки щодо продукту або виникають помилки під час розробки, відвідайте:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Застереження**:
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.