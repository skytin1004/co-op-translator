<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-22T11:14:52+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pcm"
}
-->
# How to Contribute for Co-op Translator

Dis project dey open for anybody wey wan contribute or suggest beta idea. Most times, if you wan contribute, you go need sign one Contributor License Agreement (CLA) wey go show say you get right to give us permission to use wetin you contribute. If you wan sabi more, go https://cla.opensource.microsoft.com.

If you submit pull request, CLA bot go check whether you need to sign CLA, e go mark your PR well (like status check, comment). Just follow wetin the bot talk. You go only do am once for all repo wey dey use our CLA.

## How to Set Up Development Environment

To set up your environment for this project, na Poetry we dey recommend to manage dependencies. We dey use `pyproject.toml` to manage project dependencies, so to install dependencies, use Poetry.

### How to Create Virtual Environment

#### If na pip you wan use

```bash
python -m venv .venv
```

#### If na Poetry you wan use

```bash
poetry init
```

### How to Activate Virtual Environment

#### For both pip and Poetry

- For Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- For Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### If na Poetry you wan use

```bash
poetry shell
```

### How to Install Package and Other Packages Weh You Need

#### If na Poetry (from pyproject.toml)

```bash
poetry install
```

### How to Test Manually

Before you submit PR, abeg test the translation work with real documentation:

1. Create one test folder for the main directory:
    ```bash
    mkdir test_docs
    ```

2. Copy some markdown documentation and images wey you wan translate enter the test folder. Example:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Install the package for your computer:
    ```bash
    pip install -e .
    ```

4. Run Co-op Translator for your test documents:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Check the translated files for `test_docs/translations` and `test_docs/translated_images` to confirm say:
   - The translation beta
   - The metadata comments correct
   - The original markdown style still dey
   - Links and images dey work well

This manual test go help make sure say your change dey work for real life.

### Environment Variables

1. Create `.env` file for the main directory by copying the `.env.template` file wey dem give.
1. Fill the environment variables as dem take guide you.

> [!TIP]
>
> ### Other Ways to Set Up Development Environment
>
> Apart from running the project for your computer, you fit use GitHub Codespaces or VS Code Dev Containers as another way to set up your environment.
>
> #### GitHub Codespaces
>
> You fit run this sample for GitHub Codespaces, you no need do any extra setup.
>
> The button go open VS Code for your browser:
>
> 1. Open the template (fit take some minutes):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### How to Run for Your Computer with VS Code Dev Containers
>
> ⚠️ This option go work only if your Docker Desktop get at least 16 GB RAM. If your RAM no reach, try the [GitHub Codespaces option](../..) or [set am for your computer](../..).
>
> Another way na VS Code Dev Containers, e go open the project for your VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install am if you never get am)
> 2. Open the project:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Code Style

We dey use [Black](https://github.com/psf/black) as our Python code formatter so that code style go dey the same everywhere for the project. Black no dey compromise, e go reformat Python code make e follow Black style.

#### Configuration

The Black configuration dey inside our `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### How to Install Black

You fit install Black with Poetry (na the one we recommend) or pip:

##### If na Poetry

Black go install by itself when you set up your environment:
```bash
poetry install
```

##### If na pip

If na pip you dey use, install Black like this:
```bash
pip install black
```

#### How to Use Black

##### With Poetry

1. Format all Python files for the project:
    ```bash
    poetry run black .
    ```

2. Format one file or folder:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. Format all Python files for the project:
    ```bash
    black .
    ```

2. Format one file or folder:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> E good make you set your editor to dey format code with Black anytime you save. Most editors fit do am with extension or plugin.

## How to Run Co-op Translator

To run Co-op Translator with Poetry for your environment, do like this:

1. Go the folder wey you wan use test translation or create one temporary folder for test.

2. Run this command. Change `-l ko` to the language code wey you wan translate to. The `-d` flag mean debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Make sure say your Poetry environment don activate (poetry shell) before you run the command.

## How to Add New Language

We dey happy if you fit add new language. Before you open PR, abeg do these steps so review go easy.

1. Add the language for font mapping
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Add entry wey get:
     - `code`: ISO-like language code (like `vi`)
     - `name`: The name wey people fit read
     - `font`: Font wey dey inside `src/co_op_translator/fonts/` wey fit support the language
     - `rtl`: `true` if na right-to-left, if no be, put `false`

2. Add font files wey you need
   - If you need new font, check say the license fit open source
   - Put the font file for `src/co_op_translator/fonts/`

3. Test for your computer
   - Run translation for small sample (Markdown, images, notebooks if e dey)
   - Check say output dey render well, font and RTL layout if e apply

4. Update documentation
   - Make sure say the language dey inside `getting_started/supported-languages.md`
   - No need change `README_languages_template.md`; e dey generate from the supported list

5. Open PR
   - Talk about the language wey you add and any font/license matter
   - If you fit, add screenshot of how the output look

Example YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainers

### How to Write Commit Message and Merge

To make our commit history dey clear and correct, we dey follow one style for commit message **for the final commit message** when we dey use **Squash and Merge**.

When PR merge, all the commits go join as one commit. The final commit message suppose follow the style below so history go clean.

#### Commit Message Style (for squash and merge)

We dey use this style for commit message:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Na the category of the commit. We dey use:
  - `Docs`: For documentation update.
  - `Build`: For anything wey concern build system or dependencies, like config files, CI workflow, or Dockerfile.
  - `Core`: For change wey affect the main project work or features, especially files inside `src/co_op_translator/core`.

- **description**: Small summary of wetin change.
- **PR number**: The pull request number wey join with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> For now, the **`Docs`**, **`Core`**, and **`Build`** prefix dey add to PR title automatically based on the label wey you put for the source code. If you put the correct label, you no need change PR title by yourself. Just check say everything correct and the prefix dey as e suppose.

#### Merge Style

We dey use **Squash and Merge** as our normal way to merge PR. This way make sure say commit message follow our style, even if the small commits no follow.

**Why we dey do am**:

- Project history go dey straight and clean.
- Commit message go dey the same style.
- E go remove small small commit wey no too matter (like "fix typo").

When you wan merge, make sure say the final commit message follow the style we talk above.

**Example of Squash and Merge**
If PR get these commits:

- `fix typo`
- `update README`
- `adjust formatting`

Dem go join as one:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate dis document. Even though we try make e correct, abeg make you sabi say AI fit make mistake or no too accurate. Na the original document for the main language be the correct one wey you suppose follow. If the info dey important, abeg use professional human translation. We no go fit hold any responsibility for wahala wey fit happen because of how you take use this translation.