<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:09:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sr"
}
-->
# Допринос Co-op Translator-у

Овај пројекат је отворен за доприносе и предлоге. Већина доприноса захтева да прихватите
Contributor License Agreement (CLA), којим потврђујете да имате право да нам уступите
права на коришћење вашег доприноса. Више информација можете наћи на https://cla.opensource.microsoft.com.

Када пошаљете pull request, CLA бот ће аутоматски проверити да ли треба да прихватите CLA и обележити PR (нпр. статусна провера, коментар). Само следите упутства која вам бот даје. Ово је потребно да урадите само једном за све репозиторијуме који користе наш CLA.

## Подешавање развојног окружења

За подешавање развојног окружења за овај пројекат препоручујемо да користите Poetry за управљање зависностима. Користимо `pyproject.toml` за управљање зависностима, па је за инсталацију потребно користити Poetry.

### Креирање виртуелног окружења

#### Коришћење pip-а

```bash
python -m venv .venv
```

#### Коришћење Poetry-а

```bash
poetry init
```

### Активирање виртуелног окружења

#### За pip и Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Коришћење Poetry-а

```bash
poetry shell
```

### Инсталација пакета и потребних зависности

#### Коришћење Poetry-а (из pyproject.toml)

```bash
poetry install
```

### Ручно тестирање

Пре слања PR-а, важно је да тестирате функционалност превођења на стварној документацији:

1. Креирајте тест директоријум у корену пројекта:
    ```bash
    mkdir test_docs
    ```

2. Копирајте неку markdown документацију и слике које желите да преведете у тест директоријум. На пример:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Инсталирајте пакет локално:
    ```bash
    pip install -e .
    ```

4. Покрените Co-op Translator на вашим тест документима:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Проверите преведене фајлове у `test_docs/translations` и `test_docs/translated_images` да бисте се уверили:
   - Да је квалитет превода добар
   - Да су мета-коментари исправни
   - Да је оригинална markdown структура очувана
   - Да линкови и слике раде како треба

Ово ручно тестирање помаже да се уверите да ваше измене добро функционишу у пракси.

### Енвиронмент променљиве

1. Креирајте `.env` фајл у корену пројекта копирањем датог `.env.template` фајла.
1. Попуните променљиве у складу са упутствима.

> [!TIP]
>
> ### Додатне опције за развојно окружење
>
> Поред локалног покретања пројекта, можете користити и GitHub Codespaces или VS Code Dev Containers као алтернативу за развојно окружење.
>
> #### GitHub Codespaces
>
> Овај пример можете покренути виртуелно преко GitHub Codespaces без додатних подешавања.
>
> Дугме ће отворити VS Code у вашем претраживачу:
>
> 1. Отворите шаблон (може потрајати неколико минута):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Локално покретање преко VS Code Dev Containers
>
> ⚠️ Ова опција ради само ако је вашем Docker Desktop-у додељено најмање 16 GB RAM-а. Ако имате мање од 16 GB, пробајте [GitHub Codespaces опцију](../..) или [локално подешавање](../..).
>
> Слична опција је VS Code Dev Containers, који ће отворити пројекат у вашем локалном VS Code-у преко [Dev Containers екстензије](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Покрените Docker Desktop (инсталирајте ако већ није инсталиран)
> 2. Отворите пројекат:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Стил кода

Користимо [Black](https://github.com/psf/black) као форматер Python кода ради доследног стила кроз цео пројекат. Black је алат који аутоматски форматира Python код по својим правилима.

#### Конфигурација

Black конфигурација је дефинисана у нашем `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Инсталација Black-а

Black можете инсталирати преко Poetry-а (препоручено) или pip-а:

##### Преко Poetry-а

Black се аутоматски инсталира када подесите развојно окружење:
```bash
poetry install
```

##### Преко pip-а

Ако користите pip, можете инсталирати Black директно:
```bash
pip install black
```

#### Коришћење Black-а

##### Са Poetry-ем

1. Форматирајте све Python фајлове у пројекту:
    ```bash
    poetry run black .
    ```

2. Форматирајте одређени фајл или директоријум:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Са pip-ом

1. Форматирајте све Python фајлове у пројекту:
    ```bash
    black .
    ```

2. Форматирајте одређени фајл или директоријум:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Препоручујемо да подесите ваш едитор да аутоматски форматира код са Black-ом при сваком чувању. Већина модерних едитора то подржава преко екстензија или додатака.

## Покретање Co-op Translator-а

Да бисте покренули Co-op Translator преко Poetry-а у вашем окружењу, следите ове кораке:

1. Идите у директоријум где желите да тестирате превођење или направите привремени фолдер за тестирање.

2. Покрените следећу команду. Замените `-l ko` са кодом језика на који желите да преведете. Опција `-d` укључује debug режим.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Проверите да ли је ваше Poetry окружење активно (poetry shell) пре покретања команде.

## Додавање новог језика

Радо прихватамо доприносе који додају подршку за нове језике. Пре отварања PR-а, завршите следеће кораке ради лакше ревизије.

1. Додајте језик у мапирање фонтова
   - Измените `src/co_op_translator/fonts/font_language_mappings.yml`
   - Додајте унос са:
     - `code`: ISO-код језика (нпр. `vi`)
     - `name`: Назив језика за приказ
     - `font`: Фонт који се налази у `src/co_op_translator/fonts/` и подржава писмо
     - `rtl`: `true` ако је писмо здесна налево, иначе `false`

2. Додајте потребне фајлове са фонтовима (ако је потребно)
   - Ако је потребан нови фонт, проверите да ли је лиценца компатибилна са open source дистрибуцијом
   - Додајте фонт у `src/co_op_translator/fonts/`

3. Локална провера
   - Покрените превод за мали узорак (Markdown, слике и бележнице по потреби)
   - Проверите да ли се излаз исправно приказује, укључујући фонтове и RTL распоред ако је применљиво

4. Ажурирајте документацију
   - Проверите да ли се језик појављује у `getting_started/supported-languages.md`
   - Не мењајте `README_languages_template.md`; он се генерише са листе подржаних језика

5. Отворите PR
   - Описати додати језик и све фонт/лиценцне детаље
   - Додајте снимке екрана приказаног излаза ако је могуће

Пример YAML уноса:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Тестирање новог језика

Нови језик можете тестирати покретањем следеће команде:

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

## Одржаваоци

### Формат commit поруке и стратегија спајања

Ради доследности и прегледности историје commit-а, користимо одређени формат commit поруке **за финалну commit поруку** када користимо **Squash and Merge** стратегију.

Када се pull request (PR) споји, појединачни commit-и се спајају у један commit. Финална commit порука треба да прати формат испод ради чисте и доследне историје.

#### Формат commit поруке (за squash and merge)

Користимо следећи формат commit порука:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Категорија commit-а. Користимо следеће типове:
  - `Docs`: За измене документације.
  - `Build`: За измене у build систему или зависностима, укључујући конфигурационе фајлове, CI workflow-ове или Dockerfile.
  - `Core`: За измене у основној функционалности пројекта, посебно у фајловима у `src/co_op_translator/core` директоријуму.

- **description**: Кратак опис измене.
- **PR number**: Број pull request-а који је повезан са commit-ом.

**Примери**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Тренутно се **`Docs`**, **`Core`** и **`Build`** префикси аутоматски додају на PR наслове на основу label-а који су додељени измењеном изворном коду. Ако је исправан label додељен, обично не морате ручно да мењате наслов PR-а. Само проверите да је све исправно и да је префикс генерисан како треба.

#### Стратегија спајања

Користимо **Squash and Merge** као подразумевану стратегију за pull request-ове. Ова стратегија обезбеђује да commit поруке прате наш формат, чак и ако појединачни commit-и то не чине.

**Разлози**:

- Чиста, линеарна историја пројекта.
- Доследност commit порука.
- Мање "шумова" од ситних commit-а (нпр. "fix typo").

При спајању, проверите да финална commit порука прати горе описани формат.

**Пример Squash and Merge-а**
Ако PR садржи следеће commit-е:

- `fix typo`
- `update README`
- `adjust formatting`

Треба да буду спојени у:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.