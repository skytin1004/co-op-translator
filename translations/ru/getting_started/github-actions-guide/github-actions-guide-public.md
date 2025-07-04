<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:21:46+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ru"
}
-->
# Использование Co-op Translator GitHub Action (Публичная настройка)

**Целевая аудитория:** Это руководство предназначено для пользователей большинства публичных и приватных репозиториев, где достаточно стандартных прав GitHub Actions. Для работы используется встроенный `GITHUB_TOKEN`.

Автоматизируйте перевод документации вашего репозитория с помощью Co-op Translator GitHub Action. В этом руководстве показано, как настроить действие для автоматического создания pull request с обновлёнными переводами при изменении исходных Markdown-файлов или изображений.

> [!IMPORTANT]
>
> **Выбор подходящего руководства:**
>
> В этом руководстве описана **более простая настройка с использованием стандартного `GITHUB_TOKEN`**. Это рекомендуемый способ для большинства пользователей, так как не требует управления конфиденциальными приватными ключами GitHub App.
>

## Требования

Перед настройкой GitHub Action убедитесь, что у вас есть необходимые учётные данные для AI-сервисов.

**1. Обязательно: учётные данные для языковой модели AI**  
Вам нужны данные как минимум для одной из поддерживаемых языковых моделей:

- **Azure OpenAI**: необходимы Endpoint, API Key, имена моделей/деплойментов, версия API.  
- **OpenAI**: необходим API Key, (необязательно: Org ID, базовый URL, ID модели).  
- Подробнее см. в разделе [Supported Models and Services](../../../../README.md).

**2. Необязательно: учётные данные AI Vision (для перевода изображений)**

- Требуются только если нужно переводить текст на изображениях.  
- **Azure AI Vision**: необходимы Endpoint и Subscription Key.  
- Если не указаны, действие работает в [режиме только с Markdown](../markdown-only-mode.md).

## Настройка и конфигурация

Следуйте этим шагам, чтобы настроить Co-op Translator GitHub Action в вашем репозитории с использованием стандартного `GITHUB_TOKEN`.

### Шаг 1: Понимание аутентификации (с использованием `GITHUB_TOKEN`)

Этот workflow использует встроенный `GITHUB_TOKEN`, предоставляемый GitHub Actions. Этот токен автоматически даёт права workflow на взаимодействие с вашим репозиторием в соответствии с настройками из **Шага 3**.

### Шаг 2: Настройка секретов репозитория

Вам нужно добавить только **учётные данные AI-сервисов** в виде зашифрованных секретов в настройках репозитория.

1.  Перейдите в нужный репозиторий на GitHub.  
2.  Откройте **Settings** > **Secrets and variables** > **Actions**.  
3.  В разделе **Repository secrets** нажмите **New repository secret** для каждого требуемого секрета AI-сервиса из списка ниже.

    ![Выбор действия настройки](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.ru.png) *(Изображение для ориентира: где добавлять секреты)*

**Обязательные секреты AI-сервисов (добавьте ВСЕ, которые соответствуют вашим требованиям):**

| Название секрета                    | Описание                                   | Источник значения                 |
| :---------------------------------- | :----------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Ключ для Azure AI Service (Компьютерное зрение) | Ваш Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint для Azure AI Service (Компьютерное зрение) | Ваш Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Ключ для Azure OpenAI сервиса              | Ваш Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint для Azure OpenAI сервиса           | Ваш Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Имя вашей модели Azure OpenAI               | Ваш Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Имя вашего деплоймента Azure OpenAI          | Ваш Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Версия API для Azure OpenAI                  | Ваш Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key для OpenAI                          | Ваша платформа OpenAI             |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (необязательно)       | Ваша платформа OpenAI             |
| `OPENAI_CHAT_MODEL_ID`              | Конкретный ID модели OpenAI (необязательно) | Ваша платформа OpenAI             |
| `OPENAI_BASE_URL`                   | Кастомный базовый URL OpenAI API (необязательно) | Ваша платформа OpenAI             |

### Шаг 3: Настройка прав workflow

GitHub Action требует прав, предоставляемых через `GITHUB_TOKEN`, для проверки кода и создания pull request.

1.  В репозитории откройте **Settings** > **Actions** > **General**.  
2.  Пролистайте до раздела **Workflow permissions**.  
3.  Выберите **Read and write permissions**. Это даст `GITHUB_TOKEN` необходимые права `contents: write` и `pull-requests: write` для этого workflow.  
4.  Убедитесь, что включена опция **Allow GitHub Actions to create and approve pull requests**.  
5.  Нажмите **Save**.

![Настройка прав](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.ru.png)

### Шаг 4: Создание файла workflow

Наконец, создайте YAML-файл, который определяет автоматический workflow с использованием `GITHUB_TOKEN`.

1.  В корневой папке вашего репозитория создайте каталог `.github/workflows/`, если он ещё не существует.  
2.  Внутри `.github/workflows/` создайте файл с именем `co-op-translator.yml`.  
3.  Вставьте следующий контент в `co-op-translator.yml`.

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
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
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
4.  **Настройка workflow:**  
  - **[!IMPORTANT] Целевые языки:** при необходимости измените параметр в шаге `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request`.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие в результате использования данного перевода.