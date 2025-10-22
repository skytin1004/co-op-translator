<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:08:05+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "bg"
}
-->
# Принос към Co-op Translator

Този проект приветства приноси и предложения. Повечето приноси изискват да се съгласите с Contributor License Agreement (CLA), с което декларирате, че имате право да предоставите и действително предоставяте правата за използване на вашия принос. За подробности посетете https://cla.opensource.microsoft.com.

Когато изпратите pull request, CLA ботът автоматично ще определи дали трябва да предоставите CLA и ще отбележи PR-а съответно (например със статус чек, коментар). Просто следвайте инструкциите, които ботът предоставя. Това се прави само веднъж за всички репозитории, които използват нашия CLA.

## Настройка на среда за разработка

За настройка на средата за разработка препоръчваме да използвате Poetry за управление на зависимостите. Използваме `pyproject.toml` за управление на зависимостите на проекта, затова за инсталиране на зависимостите трябва да използвате Poetry.

### Създаване на виртуална среда

#### С pip

```bash
python -m venv .venv
```

#### С Poetry

```bash
poetry init
```

### Активиране на виртуалната среда

#### За pip и Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### С Poetry

```bash
poetry shell
```

### Инсталиране на пакета и нужните пакети

#### С Poetry (от pyproject.toml)

```bash
poetry install
```

### Ръчно тестване

Преди да изпратите PR, е важно да тествате функционалността за превод с реална документация:

1. Създайте тестова директория в основната директория:
    ```bash
    mkdir test_docs
    ```

2. Копирайте някаква markdown документация и изображения, които искате да преведете, в тестовата директория. Например:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Инсталирайте пакета локално:
    ```bash
    pip install -e .
    ```

4. Стартирайте Co-op Translator върху вашите тестови документи:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Проверете преведените файлове в `test_docs/translations` и `test_docs/translated_images`, за да се уверите:
   - В качеството на превода
   - Че метаданните в коментарите са коректни
   - Че оригиналната markdown структура е запазена
   - Че връзките и изображенията работят правилно

Това ръчно тестване помага да се гарантира, че вашите промени работят добре в реални ситуации.

### Променливи на средата

1. Създайте `.env` файл в основната директория, като копирате предоставения `.env.template` файл.
1. Попълнете променливите на средата според указанията.

> [!TIP]
>
> ### Допълнителни опции за среда за разработка
>
> Освен локално стартиране на проекта, можете да използвате и GitHub Codespaces или VS Code Dev Containers като алтернативна среда за разработка.
>
> #### GitHub Codespaces
>
> Можете да стартирате тези примери виртуално чрез GitHub Codespaces без допълнителни настройки.
>
> Бутонът ще отвори VS Code в браузъра ви:
>
> 1. Отворете шаблона (може да отнеме няколко минути):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Локално стартиране с VS Code Dev Containers
>
> ⚠️ Тази опция работи само ако Docker Desktop има поне 16 GB RAM. Ако имате по-малко, опитайте [GitHub Codespaces](../..) или [локална настройка](../..).
>
> Свързана опция е VS Code Dev Containers, която отваря проекта във вашия локален VS Code чрез [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Стартирайте Docker Desktop (инсталирайте го, ако не е инсталиран)
> 2. Отворете проекта:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Стил на кода

Използваме [Black](https://github.com/psf/black) като форматер за Python код, за да поддържаме последователен стил в целия проект. Black автоматично форматира Python кода според стандарта на Black.

#### Конфигурация

Конфигурацията на Black е зададена в нашия `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Инсталиране на Black

Можете да инсталирате Black с Poetry (препоръчително) или pip:

##### С Poetry

Black се инсталира автоматично при настройка на средата за разработка:
```bash
poetry install
```

##### С pip

Ако използвате pip, можете да инсталирате Black директно:
```bash
pip install black
```

#### Използване на Black

##### С Poetry

1. Форматирайте всички Python файлове в проекта:
    ```bash
    poetry run black .
    ```

2. Форматирайте конкретен файл или директория:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### С pip

1. Форматирайте всички Python файлове в проекта:
    ```bash
    black .
    ```

2. Форматирайте конкретен файл или директория:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Препоръчваме да настроите редактора си да форматира автоматично с Black при запис. Повечето съвременни редактори го поддържат чрез разширения или плъгини.

## Стартиране на Co-op Translator

За да стартирате Co-op Translator с Poetry във вашата среда, следвайте тези стъпки:

1. Отидете в директорията, където искате да тествате преводи, или създайте временна папка за тестове.

2. Изпълнете следната команда. Заменете `-l ko` с кода на езика, на който искате да превеждате. Флагът `-d` активира debug режим.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Уверете се, че средата на Poetry е активирана (poetry shell) преди да изпълните командата.

## Добавяне на нов език

Приемаме приноси за добавяне на нови езици. Преди да отворите PR, изпълнете стъпките по-долу за по-лесен преглед.

1. Добавете езика към font mapping
   - Редактирайте `src/co_op_translator/fonts/font_language_mappings.yml`
   - Добавете запис с:
     - `code`: ISO-подобен код на езика (например `vi`)
     - `name`: Човеко-четимо име
     - `font`: Шрифт от `src/co_op_translator/fonts/`, който поддържа скрипта
     - `rtl`: `true` ако е отдясно-наляво, иначе `false`

2. Добавете нужните файлове с шрифт (ако е необходимо)
   - Ако е нужен нов шрифт, проверете лиценза за open source разпространение
   - Добавете файла с шрифта в `src/co_op_translator/fonts/`

3. Локална проверка
   - Стартирайте преводи на малък пример (Markdown, изображения и notebooks, ако е приложимо)
   - Проверете дали изходът се визуализира коректно, включително шрифтове и RTL оформление, ако е приложимо

4. Обновете документацията
   - Уверете се, че езикът е добавен в `getting_started/supported-languages.md`
   - Не са нужни промени в `README_languages_template.md`; той се генерира от списъка с поддържани езици

5. Отворете PR
   - Описвайте добавения език и лицензионни съображения за шрифта
   - Прикачете скрийншоти на визуализирания изход, ако е възможно

Примерен YAML запис:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Тест на новия език

Можете да тествате новия език с командата:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## Поддръжка

### Формат на commit съобщенията и стратегия за сливане

За да поддържаме последователност и яснота в историята на commit-ите, следваме специфичен формат **за финалното commit съобщение** при използване на **Squash and Merge** стратегията.

Когато pull request (PR) се слее, отделните commit-и се обединяват в един. Финалното commit съобщение трябва да следва формата по-долу за чиста и последователна история.

#### Формат на commit съобщенията (за squash and merge)

Използваме следния формат за commit съобщения:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Категория на commit-а. Използваме:
  - `Docs`: За промени в документацията.
  - `Build`: За промени, свързани със системата за билд или зависимости, включително конфигурационни файлове, CI workflows или Dockerfile.
  - `Core`: За промени в основната функционалност или функции на проекта, особено файлове в `src/co_op_translator/core`.

- **description**: Кратко описание на промяната.
- **PR number**: Номерът на pull request-а, свързан с commit-а.

**Примери**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> В момента префиксите **`Docs`**, **`Core`** и **`Build`** се добавят автоматично към заглавията на PR според етикетите на променения изходен код. Ако е приложен правилният етикет, обикновено не е нужно да редактирате заглавието на PR. Просто проверете дали всичко е коректно и префиксът е генериран правилно.

#### Стратегия за сливане

Използваме **Squash and Merge** като стандартна стратегия за pull request-и. Тази стратегия гарантира, че commit съобщенията следват нашия формат, дори ако отделните commit-и не го правят.

**Причини**:

- Чиста, линейна история на проекта.
- Последователност в commit съобщенията.
- По-малко шум от дребни commit-и (например "fix typo").

При сливане се уверете, че финалното commit съобщение следва описания формат.

**Пример за Squash and Merge**
Ако PR съдържа следните commit-и:

- `fix typo`
- `update README`
- `adjust formatting`

Те трябва да се обединят в:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Отказ от отговорност**:
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали в резултат на използването на този превод.