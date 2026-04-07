# Използване на Co-op Translator GitHub Action (Публична настройка)

**Целева аудитория:** Това ръководство е предназначено за потребители в повечето публични или частни хранилища, където стандартните разрешения на GitHub Actions са достатъчни. Използва вградения `GITHUB_TOKEN`.

Автоматизирайте превода на документацията във вашето хранилище лесно с Co-op Translator GitHub Action. Това ръководство ви показва как да настроите действието така, че автоматично да създава pull request-и с обновени преводи всеки път, когато изходните Markdown файлове или изображения се променят.

> [!IMPORTANT]
>
> **Избор на правилното ръководство:**
>
> Това ръководство описва **по-опростената настройка със стандартния `GITHUB_TOKEN`**. Това е препоръчителният метод за повечето потребители, тъй като не изисква управление на чувствителни GitHub App Private Keys.
>

## Предварителни условия

Преди да конфигурирате GitHub Action, уверете се, че разполагате с необходимите идентификационни данни за AI услугата.

**1. Задължително: Идентификационни данни за AI езиков модел**
Трябва да имате идентификационни данни за поне един поддържан езиков модел:

- **Azure OpenAI**: Изисква Endpoint, API Key, имена на модел/деплоймънт, версия на API.
- **OpenAI**: Изисква API Key, (по желание: Org ID, Base URL, Model ID).
- Вижте [Поддържани модели и услуги](../../../../README.md) за подробности.

**2. По желание: Идентификационни данни за AI Vision (за превод на изображения)**

- Необходими само ако искате да превеждате текст в изображения.
- **Azure AI Vision**: Изисква Endpoint и Subscription Key.
- Ако не са предоставени, действието работи в [режим само за Markdown](../markdown-only-mode.md).

## Настройка и конфигуриране

Следвайте тези стъпки, за да конфигурирате Co-op Translator GitHub Action във вашето хранилище със стандартния `GITHUB_TOKEN`.

### Стъпка 1: Разберете удостоверяването (Използване на `GITHUB_TOKEN`)

Този workflow използва вградения `GITHUB_TOKEN`, предоставен от GitHub Actions. Този токен автоматично дава разрешения на workflow-а да взаимодейства с вашето хранилище според настройките, конфигурирани в **Стъпка 3**.

### Стъпка 2: Конфигурирайте секретите на хранилището

Трябва само да добавите **идентификационните данни за AI услугата** като криптирани секрети в настройките на вашето хранилище.

1.  Отидете във вашето GitHub хранилище.
2.  Изберете **Settings** > **Secrets and variables** > **Actions**.
3.  Под **Repository secrets** натиснете **New repository secret** за всеки необходим AI секрет, изброен по-долу.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.bg.png" alt="Select setting action"> *(Референция на изображението: Показва къде да добавите секрети)*

**Задължителни AI секрети (Добавете ВСИЧКИ, които са приложими според вашите предварителни условия):**

| Secret Name                         | Описание                                   | Източник на стойността             |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Ключ за Azure AI Service (Computer Vision)  | Вашият Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint за Azure AI Service (Computer Vision) | Вашият Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Ключ за Azure OpenAI service              | Вашият Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint за Azure OpenAI service          | Вашият Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Име на вашия Azure OpenAI модел           | Вашият Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Име на вашия Azure OpenAI Deployment      | Вашият Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Версия на API за Azure OpenAI             | Вашият Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key за OpenAI                         | Вашата OpenAI платформа               |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (по желание)       | Вашата OpenAI платформа               |
| `OPENAI_CHAT_MODEL_ID`              | Конкретен OpenAI model ID (по желание)    | Вашата OpenAI платформа               |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL (по желание)   | Вашата OpenAI платформа               |

### Стъпка 3: Конфигурирайте разрешенията на workflow-а

GitHub Action се нуждае от разрешения чрез `GITHUB_TOKEN`, за да чете кода и да създава pull request-и.

1.  В хранилището си отидете на **Settings** > **Actions** > **General**.
2.  Превъртете до секцията **Workflow permissions**.
3.  Изберете **Read and write permissions**. Това дава на `GITHUB_TOKEN` необходимите `contents: write` и `pull-requests: write` разрешения за този workflow.
4.  Уверете се, че отметката за **Allow GitHub Actions to create and approve pull requests** е **отбелязана**.
5.  Натиснете **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.bg.png" alt="Permission setting">

### Стъпка 4: Създайте workflow файла

Накрая създайте YAML файла, който дефинира автоматизирания workflow с `GITHUB_TOKEN`.

1.  В основната директория на вашето хранилище създайте `.github/workflows/` директория, ако не съществува.
2.  Вътре в `.github/workflows/` създайте файл с име `co-op-translator.yml`.
3.  Поставете следното съдържание в `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Персонализирайте workflow-а:**
  - **[!IMPORTANT] Целеви езици:** В стъпката `Run Co-op Translator` **ЗАДЪЛЖИТЕЛНО прегледайте и коригирайте списъка с езикови кодове** в командата `translate -l "..." -y`, за да отговаря на нуждите на вашия проект. Примерният списък (`ar de es...`) трябва да бъде заменен или коригиран.
  - **Тригер (`on:`):** Настоящият тригер се изпълнява при всяко push-ване към `main`. За големи хранилища обмислете добавяне на `paths:` филтър (вижте коментирания пример в YAML), за да се изпълнява workflow-ът само при промяна на релевантни файлове (напр. изходна документация), което спестява runner минути.
  - **Детайли за PR:** Персонализирайте `commit-message`, `title`, `body`, името на `branch` и `labels` в стъпката `Create Pull Request`, ако е необходимо.

## Изпълнение на workflow-а

> [!WARNING]  
> **Лимит на времето за GitHub-hosted Runner:**  
> GitHub-hosted runner-и като `ubuntu-latest` имат **максимален лимит за изпълнение от 6 часа**.  
> За големи хранилища с документация, ако процесът на превод надвиши 6 часа, workflow-ът ще бъде автоматично прекратен.  
> За да предотвратите това, обмислете:  
> - Използване на **self-hosted runner** (без лимит на времето)  
> - Намаляване на броя целеви езици за всяко изпълнение

След като файлът `co-op-translator.yml` бъде слят в основния ви branch (или branch-а, посочен в тригера `on:`), workflow-ът ще се изпълнява автоматично всеки път, когато има промени, които се push-ват към този branch (и съвпадат с филтъра `paths`, ако е конфигуриран).

---

**Отказ от отговорност**:
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали в резултат на използването на този превод.