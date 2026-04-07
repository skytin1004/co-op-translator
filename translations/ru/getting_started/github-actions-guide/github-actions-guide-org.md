# Использование GitHub Action Co-op Translator (Руководство для организаций)

**Целевая аудитория:** Это руководство предназначено для **внутренних пользователей Microsoft** или **команд, имеющих доступ к необходимым учетным данным для предустановленного приложения Co-op Translator GitHub App**, либо способных создать собственное приложение GitHub App.

Автоматизируйте перевод документации вашего репозитория с помощью GitHub Action Co-op Translator. В этом руководстве описан процесс настройки действия, чтобы автоматически создавать pull-запросы с обновленными переводами при изменении исходных Markdown-файлов или изображений.

> [!IMPORTANT]
> 
> **Выбор подходящего руководства:**
>
> В этом руководстве описана настройка с использованием **GitHub App ID и приватного ключа**. Обычно вам нужен этот способ ("Руководство для организаций"), если: **`GITHUB_TOKEN` имеет ограниченные права:** В вашей организации или репозитории права стандартного `GITHUB_TOKEN` ограничены. В частности, если `GITHUB_TOKEN` не имеет необходимых прав `write` (например, `contents: write` или `pull-requests: write`), то рабочий процесс из [Публичного руководства](./github-actions-guide-public.md) завершится ошибкой из-за недостаточных прав. Использование отдельного GitHub App с явно заданными правами позволяет обойти это ограничение.
>
> **Если вышеуказанное к вам не относится:**
>
> Если стандартный `GITHUB_TOKEN` имеет достаточные права в вашем репозитории (то есть нет ограничений со стороны организации), используйте **[Публичное руководство по настройке с GITHUB_TOKEN](./github-actions-guide-public.md)**. Публичное руководство не требует получения или управления App ID и приватными ключами, а использует только стандартный `GITHUB_TOKEN` и права репозитория.

## Предварительные требования

Перед настройкой GitHub Action убедитесь, что у вас есть необходимые учетные данные для AI-сервиса.

**1. Обязательно: Учетные данные языковой модели AI**
Вам нужны учетные данные хотя бы для одной поддерживаемой языковой модели:

- **Azure OpenAI**: Требуются Endpoint, API Key, имена модели/деплоймента, версия API.
- **OpenAI**: Требуется API Key, (опционально: Org ID, Base URL, Model ID).
- Подробнее см. [Поддерживаемые модели и сервисы](../../../../README.md).
- Руководство по настройке: [Настройка Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Необязательно: Учетные данные Computer Vision (для перевода текста на изображениях)**

- Требуется только если нужно переводить текст на изображениях.
- **Azure Computer Vision**: Требуются Endpoint и Subscription Key.
- Если не указано, действие работает в [режиме только Markdown](../markdown-only-mode.md).
- Руководство по настройке: [Настройка Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Настройка и конфигурация

Выполните следующие шаги для настройки GitHub Action Co-op Translator в вашем репозитории:

### Шаг 1: Установка и настройка аутентификации через GitHub App

Рабочий процесс использует аутентификацию через GitHub App для безопасного взаимодействия с вашим репозиторием (например, создания pull-запросов) от вашего имени. Выберите один из вариантов:

#### **Вариант A: Установка предустановленного приложения Co-op Translator GitHub App (для внутреннего использования Microsoft)**

1. Перейдите на страницу [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Нажмите **Install** и выберите аккаунт или организацию, где находится ваш целевой репозиторий.

    ![Установка приложения](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ru.png)

1. Выберите **Only select repositories** и укажите ваш репозиторий (например, `PhiCookBook`). Нажмите **Install**. Возможно, потребуется пройти аутентификацию.

    ![Установка авторизации](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ru.png)

1. **Получение учетных данных приложения (требуется внутренний процесс):** Чтобы рабочий процесс мог аутентифицироваться как приложение, вам нужны две информации, предоставляемые командой Co-op Translator:
  - **App ID:** Уникальный идентификатор приложения Co-op Translator. App ID: `1164076`.
  - **Private Key:** Необходимо получить **полное содержимое** файла приватного ключа `.pem` у контактного лица-администратора. **Относитесь к этому ключу как к паролю и храните его в безопасности.**

1. Перейдите к шагу 2.

#### **Вариант B: Использование собственного приложения GitHub App**

- При желании вы можете создать и настроить собственное приложение GitHub App. Убедитесь, что у него есть права Read & write на Contents и Pull requests. Вам понадобятся его App ID и сгенерированный приватный ключ.

### Шаг 2: Настройка секретов репозитория

Добавьте учетные данные GitHub App и вашего AI-сервиса как зашифрованные секреты в настройках репозитория.

1. Перейдите в ваш целевой репозиторий на GitHub (например, `PhiCookBook`).

1. Откройте **Settings** > **Secrets and variables** > **Actions**.

1. В разделе **Repository secrets** нажмите **New repository secret** для каждого секрета из списка ниже.

   ![Выбор настроек actions](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ru.png)

**Обязательные секреты (для аутентификации через GitHub App):**

| Имя секрета          | Описание                                      | Источник значения                                     |
| :------------------- | :-------------------------------------------- | :---------------------------------------------------- |
| `GH_APP_ID`          | App ID приложения GitHub (из шага 1).         | Настройки GitHub App                                  |
| `GH_APP_PRIVATE_KEY` | **Полное содержимое** скачанного файла `.pem`. | Файл `.pem` (из шага 1)                               |

**Секреты AI-сервиса (добавьте ВСЕ, которые применимы согласно вашим требованиям):**

| Имя секрета                         | Описание                               | Источник значения                     |
| :---------------------------------- | :------------------------------------- | :------------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Ключ для Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint для Azure AI Service (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Ключ для Azure OpenAI                  | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint для Azure OpenAI              | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Имя вашей модели Azure OpenAI          | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Имя деплоймента Azure OpenAI           | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Версия API для Azure OpenAI            | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API Key для OpenAI                     | OpenAI Platform                      |
| `OPENAI_ORG_ID`                     | ID организации OpenAI                  | OpenAI Platform                      |
| `OPENAI_CHAT_MODEL_ID`              | ID конкретной модели OpenAI            | OpenAI Platform                      |
| `OPENAI_BASE_URL`                   | Пользовательский Base URL для OpenAI API| OpenAI Platform                      |

![Ввод имени переменной среды](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ru.png)

### Шаг 3: Создание файла рабочего процесса

Теперь создайте YAML-файл, определяющий автоматизированный рабочий процесс.

1. В корневой директории вашего репозитория создайте папку `.github/workflows/`, если она отсутствует.

1. Внутри `.github/workflows/` создайте файл с именем `co-op-translator.yml`.

1. Вставьте следующий контент в co-op-translator.yml.

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

4.  **Настройте рабочий процесс:**
  - **[!IMPORTANT] Целевые языки:** В шаге `Run Co-op Translator` **ОБЯЗАТЕЛЬНО проверьте и измените список языковых кодов** в команде `translate -l "..." -y` согласно требованиям вашего проекта. Пример списка (`ar de es...`) нужно заменить или скорректировать.
  - **Триггер (`on:`):** Сейчас триггер срабатывает при каждом push в `main`. Для больших репозиториев рекомендуется добавить фильтр `paths:` (см. пример в комментарии в YAML), чтобы запускать рабочий процесс только при изменении релевантных файлов (например, исходной документации), экономя минуты runner.
  - **Детали PR:** При необходимости настройте `commit-message`, `title`, `body`, имя ветки и `labels` в шаге `Create Pull Request`.

## Управление учетными данными и их обновление

- **Безопасность:** Всегда храните чувствительные данные (API-ключи, приватные ключи) как секреты GitHub Actions. Никогда не размещайте их в файле рабочего процесса или коде репозитория.
- **[!IMPORTANT] Обновление ключей (для внутренних пользователей Microsoft):** Обратите внимание, что ключ Azure OpenAI, используемый внутри Microsoft, может требовать обязательного обновления (например, каждые 5 месяцев). Обновляйте соответствующие секреты GitHub (`AZURE_OPENAI_...`) **до истечения срока действия**, чтобы избежать сбоев рабочего процесса.

## Запуск рабочего процесса

> [!WARNING]  
> **Ограничение времени выполнения GitHub-hosted runner:**  
> GitHub-hosted runner, такие как `ubuntu-latest`, имеют **максимальное ограничение времени выполнения — 6 часов**.  
> Для больших репозиториев с документацией, если процесс перевода займет больше 6 часов, рабочий процесс будет автоматически завершен.  
> Чтобы избежать этого, рассмотрите варианты:  
> - Использование **self-hosted runner** (без ограничения времени)  
> - Сокращение количества целевых языков за один запуск

После того как файл `co-op-translator.yml` будет добавлен в вашу основную ветку (или ветку, указанную в триггере `on:`), рабочий процесс будет автоматически запускаться при каждом пуше в эту ветку (и при совпадении с фильтром `paths`, если он настроен).

Если переводы будут созданы или обновлены, действие автоматически создаст Pull Request с изменениями, готовыми к вашему рассмотрению и слиянию.

---

**Отказ от ответственности**:
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.