# Використання GitHub Action Co-op Translator (Інструкція для організацій)

**Цільова аудиторія:** Ця інструкція призначена для **внутрішніх користувачів Microsoft** або **команд, які мають доступ до необхідних облікових даних для попередньо створеного Co-op Translator GitHub App** або можуть створити власний GitHub App.

Автоматизуйте переклад документації вашого репозиторію за допомогою Co-op Translator GitHub Action. Ця інструкція допоможе налаштувати дію так, щоб автоматично створювались pull request із оновленими перекладами щоразу, коли змінюються вихідні Markdown-файли або зображення.

> [!IMPORTANT]
> 
> **Вибір правильної інструкції:**
>
> Тут описано налаштування через **GitHub App ID та Private Key**. Зазвичай вам потрібен саме цей "Організаційний спосіб", якщо: **`GITHUB_TOKEN` має обмежені права:** Ваша організація або налаштування репозиторію обмежують стандартні права, які надає `GITHUB_TOKEN`. Зокрема, якщо `GITHUB_TOKEN` не має необхідних прав `write` (наприклад, `contents: write` або `pull-requests: write`), робочий процес із [Публічної інструкції](./github-actions-guide-public.md) не спрацює через недостатні права. Використання окремого GitHub App із явно наданими правами обходить це обмеження.
>
> **Якщо це не про вас:**
>
> Якщо стандартний `GITHUB_TOKEN` має достатньо прав у вашому репозиторії (тобто немає організаційних обмежень), скористайтеся **[Публічною інструкцією з використанням GITHUB_TOKEN](./github-actions-guide-public.md)**. Публічна інструкція не потребує отримання чи зберігання App ID або Private Key і використовує лише стандартний `GITHUB_TOKEN` та права репозиторію.

## Необхідне

Перед налаштуванням GitHub Action переконайтеся, що у вас є потрібні облікові дані AI-сервісу.

**1. Обов’язково: Облікові дані AI Language Model**
Потрібні облікові дані для хоча б однієї з підтримуваних мовних моделей:

- **Azure OpenAI**: Потрібен Endpoint, API Key, назви моделі/деплойменту, версія API.
- **OpenAI**: Потрібен API Key, (опціонально: Org ID, Base URL, Model ID).
- Деталі дивіться у [Підтримувані моделі та сервіси](../../../../README.md).
- Інструкція: [Налаштування Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Опціонально: Облікові дані Computer Vision (для перекладу тексту на зображеннях)**

- Потрібно лише, якщо треба перекладати текст на зображеннях.
- **Azure Computer Vision**: Потрібен Endpoint та Subscription Key.
- Якщо не вказано, дія працює у [режимі лише Markdown](../markdown-only-mode.md).
- Інструкція: [Налаштування Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Налаштування та конфігурація

Виконайте ці кроки для налаштування Co-op Translator GitHub Action у вашому репозиторії:

### Крок 1: Встановіть і налаштуйте автентифікацію GitHub App

Робочий процес використовує автентифікацію через GitHub App для безпечної взаємодії з вашим репозиторієм (наприклад, створення pull request) від вашого імені. Виберіть один із варіантів:

#### **Варіант A: Встановити попередньо створений Co-op Translator GitHub App (для внутрішнього використання Microsoft)**

1. Перейдіть на сторінку [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Натисніть **Install** і виберіть акаунт або організацію, де знаходиться ваш цільовий репозиторій.

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.uk.png)

1. Виберіть **Only select repositories** і оберіть ваш цільовий репозиторій (наприклад, `PhiCookBook`). Натисніть **Install**. Може знадобитися автентифікація.

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.uk.png)

1. **Отримайте облікові дані App (потрібна внутрішня процедура):** Щоб робочий процес міг автентифікуватися як додаток, вам потрібно отримати два параметри від команди Co-op Translator:
  - **App ID:** Унікальний ідентифікатор Co-op Translator app. App ID: `1164076`.
  - **Private Key:** Потрібно отримати **повний вміст** файлу приватного ключа `.pem` у відповідальної особи. **Зберігайте цей ключ як пароль і не розголошуйте.**

1. Перейдіть до Кроку 2.

#### **Варіант B: Використати власний GitHub App**

- За бажанням, можете створити і налаштувати власний GitHub App. Переконайтеся, що він має права Read & write до Contents і Pull requests. Вам знадобиться його App ID і згенерований Private Key.

### Крок 2: Налаштуйте секрети репозиторію

Потрібно додати облікові дані GitHub App і AI-сервісу як зашифровані секрети у налаштуваннях репозиторію.

1. Перейдіть у ваш цільовий GitHub репозиторій (наприклад, `PhiCookBook`).

1. Відкрийте **Settings** > **Secrets and variables** > **Actions**.

1. У розділі **Repository secrets** натисніть **New repository secret** для кожного секрету зі списку нижче.

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.uk.png)

**Обов’язкові секрети (для автентифікації GitHub App):**

| Назва секрету        | Опис                                            | Джерело значення                                 |
| :------------------- | :---------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | App ID GitHub App (з Кроку 1)                   | Налаштування GitHub App                          |
| `GH_APP_PRIVATE_KEY` | **Повний вміст** завантаженого `.pem` файлу     | `.pem` файл (з Кроку 1)                          |

**Секрети AI-сервісу (Додайте ВСІ, які потрібні згідно з вашими вимогами):**

| Назва секрету                         | Опис                                         | Джерело значення                 |
| :------------------------------------ | :-------------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Ключ для Azure AI Service (Computer Vision)   | Azure AI Foundry                 |
| `AZURE_AI_SERVICE_ENDPOINT`           | Endpoint для Azure AI Service (Computer Vision) | Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`                | Ключ для Azure OpenAI service                 | Azure AI Foundry                 |
| `AZURE_OPENAI_ENDPOINT`               | Endpoint для Azure OpenAI service             | Azure AI Foundry                 |
| `AZURE_OPENAI_MODEL_NAME`             | Назва вашої моделі Azure OpenAI               | Azure AI Foundry                 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`   | Назва деплойменту Azure OpenAI                | Azure AI Foundry                 |
| `AZURE_OPENAI_API_VERSION`            | Версія API для Azure OpenAI                   | Azure AI Foundry                 |
| `OPENAI_API_KEY`                      | API Key для OpenAI                            | OpenAI Platform                  |
| `OPENAI_ORG_ID`                       | OpenAI Organization ID                        | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`                | ID конкретної моделі OpenAI                   | OpenAI Platform                  |
| `OPENAI_BASE_URL`                     | Кастомний базовий URL OpenAI API              | OpenAI Platform                  |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.uk.png)

### Крок 3: Створіть файл workflow

Останній крок — створити YAML-файл, який описує автоматизований робочий процес.

1. У корені вашого репозиторію створіть директорію `.github/workflows/`, якщо її ще немає.

1. Всередині `.github/workflows/` створіть файл з назвою `co-op-translator.yml`.

1. Вставте наступний вміст у co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **Налаштуйте workflow:**
  - **[!IMPORTANT] Цільові мови:** У кроці `Run Co-op Translator` **ОБОВ’ЯЗКОВО перегляньте і змініть список мовних кодів** у команді `translate -l "..." -y` відповідно до потреб вашого проекту. Прикладовий список (`ar de es...`) потрібно замінити або скоригувати.
  - **Тригер (`on:`):** Зараз workflow запускається при кожному push у `main`. Для великих репозиторіїв рекомендується додати фільтр `paths:` (див. закоментований приклад у YAML), щоб workflow запускався лише при зміні релевантних файлів (наприклад, документації), що дозволить зекономити час runner.
  - **Деталі PR:** За потреби змініть `commit-message`, `title`, `body`, назву `branch` та `labels` у кроці `Create Pull Request`.

## Управління обліковими даними та їх оновлення

- **Безпека:** Завжди зберігайте чутливі облікові дані (API ключі, приватні ключі) як секрети GitHub Actions. Ніколи не розміщуйте їх у workflow-файлі чи коді репозиторію.
- **[!IMPORTANT] Оновлення ключів (для внутрішніх користувачів Microsoft):** Зверніть увагу, що ключ Azure OpenAI, який використовується всередині Microsoft, може мати політику обов’язкового оновлення (наприклад, кожні 5 місяців). Оновлюйте відповідні секрети GitHub (`AZURE_OPENAI_...` ключі) **до закінчення терміну дії**, щоб уникнути збоїв workflow.

## Запуск workflow

> [!WARNING]  
> **Ліміт часу для GitHub-hosted runner:**  
> GitHub-hosted runner, такі як `ubuntu-latest`, мають **максимальний ліміт виконання 6 годин**.  
> Для великих репозиторіїв документації, якщо процес перекладу перевищить 6 годин, workflow буде автоматично завершено.  
> Щоб уникнути цього, розгляньте:  
> - Використання **self-hosted runner** (без ліміту часу)  
> - Зменшення кількості цільових мов за один запуск

Після того, як файл `co-op-translator.yml` буде додано у вашу основну гілку (або гілку, вказану у тригері `on:`), workflow автоматично запускатиметься при кожному push у цю гілку (і при збігу з фільтром `paths`, якщо налаштовано).

Якщо будуть створені або оновлені переклади, дія автоматично створить Pull Request із цими змінами, готовий до вашого перегляду та злиття.

---

**Застереження**:
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.