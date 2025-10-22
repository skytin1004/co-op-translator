<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-22T11:17:17+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "pcm"
}
-->
# How to Install Co-op translator package

**Co-op Translator** na command-line tool wey go help you translate all di markdown files plus images wey dey your project to plenti languages. Dis tutorial go show you how you go fit set up di translator and run am for different ways.

### How to create virtual environment

You fit create virtual environment with `pip` or `Poetry`. Just run any of dis commands for your terminal.

#### If na pip you wan use

```bash
python -m venv .venv
```

#### If na Poetry you wan use

```bash
poetry init
```

### How to activate di virtual environment

After you don create di virtual environment, you go need activate am. How you go do am depend on your operating system. Run dis command for your terminal.

#### For both pip and Poetry

- For Windows:

    ```bash
    .venv\Scripts\activate
    ```

- For Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### If na Poetry you use

1. If na Poetry you take create di environment, run dis command for your terminal to activate am.

    ```bash
    poetry shell
    ```

### How to Install di Package plus wetin e need

After you don set up and activate your virtual environment, next step na to install all di things wey di package need.

### Quick install

To install Co-Op Translator with pip

```
pip install co-op-translator
```
Or

To install with poetry
```
poetry add co-op-translator
```

#### If you wan use pip (from requirements.txt) after you don clone dis repo

> [!NOTE]
> Abeg no do dis one if you don already install co-op translator with quick install.

1. If na pip you dey use, just run dis command for your terminal. E go help you install all di packages wey dey inside `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

#### If na Poetry you wan use (from pyproject.toml)

1. If na Poetry you dey use, just run dis command for your terminal. E go help you install all di packages wey dey inside `pyproject.toml` file:

    ```bash
    poetry install
    ```

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate dis document. Even though we try make e correct, abeg make you sabi say AI fit make mistake or get wahala for the translation. Na the original document for the main language be the correct one wey you suppose follow. If the info dey important, abeg use professional human translation. We no go fit hold any responsibility for any wahala or misunderstanding wey fit happen because of this translation.