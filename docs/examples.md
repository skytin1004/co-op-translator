# Examples

These examples use the real CLI and Python API entry points from this repository.

## Translate Markdown with the CLI

```bash
translate -l "ko ja fr" -md
```

This translates Markdown files only and writes output under:

```text
translations/ko/
translations/ja/
translations/fr/
```

## Translate notebooks only

```bash
translate -l "zh-CN" -nb
```

Notebook links can later be normalized with:

```bash
migrate-links -l "zh-CN"
```

## Translate images only

```bash
translate -l "pt-BR" -img
```

Image translation requires both an LLM provider and Azure AI Vision.

## Preview without writing files

```bash
translate -l "de es" -md --dry-run
```

Dry runs are useful when checking token estimates, migration plans, or CI wiring.

## Repair low-confidence translations

First evaluate translations:

```bash
evaluate -l "ko" -c 0.8
```

Then retranslate Markdown files below the threshold:

```bash
translate -l "ko" --fix -c 0.8 -md
```

## Run from Python

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

## Translate multiple roots from Python

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

## Use explicit output groups

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

## Preserve glossary terms

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

Glossary terms are scoped to the API call and restored afterward.

## CI-friendly translation command

```bash
translate -l "ko ja" -md -y -s
```

This auto-confirms prompts and saves DEBUG-level logs under `logs/`.
