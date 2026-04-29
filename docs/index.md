# Co-op Translator Documentation

<section class="cot-hero tw-relative tw-isolate tw-mb-10 tw-overflow-hidden tw-rounded-3xl tw-border tw-border-sky-100 tw-bg-white tw-p-6 tw-shadow-coop dark:tw-border-slate-700 dark:tw-bg-slate-900 md:tw-grid md:tw-grid-cols-[1.2fr_0.8fr] md:tw-gap-8 md:tw-p-10">
  <div class="tw-pointer-events-none tw-absolute tw-inset-0 tw--z-10 tw-bg-[radial-gradient(circle_at_20%_10%,rgba(37,99,235,0.18),transparent_28%),linear-gradient(135deg,rgba(240,249,255,0.96),rgba(236,253,245,0.8))] dark:tw-bg-[radial-gradient(circle_at_20%_10%,rgba(37,99,235,0.32),transparent_28%),linear-gradient(135deg,rgba(15,23,42,0.98),rgba(12,74,110,0.58))]"></div>
  <div class="tw-flex tw-flex-col tw-justify-center">
    <p class="tw-m-0 tw-text-xs tw-font-extrabold tw-uppercase tw-tracking-[0.18em] tw-text-coop-cyan">API and CLI reference</p>
    <h1 class="tw-my-4 tw-max-w-3xl tw-font-display tw-text-4xl tw-font-black tw-leading-tight tw-tracking-normal tw-text-coop-ink dark:tw-text-white md:tw-text-6xl">Co-op Translator Documentation</h1>
    <p class="tw-mb-6 tw-max-w-2xl tw-text-lg tw-leading-8 tw-text-slate-600 dark:tw-text-slate-300">
      Translate Markdown, notebooks, and image text into language-scoped outputs,
      then keep those translations synchronized as your project changes.
    </p>
    <div class="tw-flex tw-flex-wrap tw-gap-3">
      <a class="tw-inline-flex tw-items-center tw-rounded-full tw-bg-coop-blue tw-px-5 tw-py-3 tw-text-sm tw-font-bold tw-text-white tw-shadow-lg tw-shadow-blue-500/20 tw-transition hover:tw-bg-blue-700" href="api/">Python API</a>
      <a class="tw-inline-flex tw-items-center tw-rounded-full tw-border tw-border-slate-300 tw-bg-white/75 tw-px-5 tw-py-3 tw-text-sm tw-font-bold tw-text-slate-800 tw-transition hover:tw-border-coop-blue hover:tw-text-coop-blue dark:tw-border-slate-600 dark:tw-bg-slate-900/70 dark:tw-text-slate-100" href="cli/">CLI Reference</a>
    </div>
  </div>
  <div class="tw-mt-8 tw-flex tw-min-w-0 tw-flex-col tw-justify-center md:tw-mt-0">
    <div class="tw-overflow-hidden tw-rounded-2xl tw-border tw-border-slate-200 tw-bg-slate-950 tw-shadow-2xl">
      <div class="tw-flex tw-items-center tw-gap-2 tw-border-b tw-border-white/10 tw-px-4 tw-py-3">
        <span class="tw-h-3 tw-w-3 tw-rounded-full tw-bg-red-400"></span>
        <span class="tw-h-3 tw-w-3 tw-rounded-full tw-bg-amber-300"></span>
        <span class="tw-h-3 tw-w-3 tw-rounded-full tw-bg-emerald-400"></span>
        <span class="tw-ml-3 tw-text-xs tw-font-bold tw-uppercase tw-tracking-[0.14em] tw-text-slate-400">Command surface</span>
      </div>
      <pre class="tw-m-0 tw-overflow-x-auto tw-p-5"><code class="tw-text-sm tw-leading-7 tw-text-slate-100">translate -l "ko ja" -md
evaluate -l "ko"
migrate-links -l "ko ja"</code></pre>
    </div>
  </div>
</section>

Co-op Translator is a Python command-line tool and automation library for translating project documentation into multiple languages. It translates Markdown, Jupyter notebooks, and image text, then stores output under language-scoped folders such as `translations/<lang>/` and `translated_images/<lang>/`.

This documentation focuses on the two supported integration surfaces in this repository:

- **Python API**: the package-level programmatic entry point exported from `co_op_translator.api`.
- **CLI**: the installed commands `translate`, `evaluate`, and `migrate-links`.

## Start here

Use these pages depending on what you are trying to do:

<div class="tw-grid tw-gap-4 md:tw-grid-cols-2" markdown>

<a class="tw-block tw-rounded-2xl tw-border tw-border-slate-200 tw-bg-white tw-p-5 tw-no-underline tw-shadow-sm tw-transition hover:tw--translate-y-0.5 hover:tw-border-coop-blue hover:tw-shadow-lg dark:tw-border-slate-700 dark:tw-bg-slate-900/60" href="configuration/">
  <span class="tw-text-sm tw-font-extrabold tw-uppercase tw-tracking-[0.14em] tw-text-coop-cyan">Configure</span>
  <strong class="tw-mt-2 tw-block tw-text-xl tw-text-coop-ink dark:tw-text-white">Configuration</strong>
  <span class="tw-mt-2 tw-block tw-text-slate-600 dark:tw-text-slate-300">Configure Azure OpenAI, OpenAI, Azure AI Vision, fallback credential sets, and output directories.</span>
</a>

<a class="tw-block tw-rounded-2xl tw-border tw-border-slate-200 tw-bg-white tw-p-5 tw-no-underline tw-shadow-sm tw-transition hover:tw--translate-y-0.5 hover:tw-border-coop-blue hover:tw-shadow-lg dark:tw-border-slate-700 dark:tw-bg-slate-900/60" href="examples/">
  <span class="tw-text-sm tw-font-extrabold tw-uppercase tw-tracking-[0.14em] tw-text-coop-cyan">Run</span>
  <strong class="tw-mt-2 tw-block tw-text-xl tw-text-coop-ink dark:tw-text-white">Examples</strong>
  <span class="tw-mt-2 tw-block tw-text-slate-600 dark:tw-text-slate-300">Use practical CLI and Python snippets for translation, evaluation, and repair workflows.</span>
</a>

<a class="tw-block tw-rounded-2xl tw-border tw-border-slate-200 tw-bg-white tw-p-5 tw-no-underline tw-shadow-sm tw-transition hover:tw--translate-y-0.5 hover:tw-border-coop-blue hover:tw-shadow-lg dark:tw-border-slate-700 dark:tw-bg-slate-900/60" href="api/">
  <span class="tw-text-sm tw-font-extrabold tw-uppercase tw-tracking-[0.14em] tw-text-coop-cyan">Integrate</span>
  <strong class="tw-mt-2 tw-block tw-text-xl tw-text-coop-ink dark:tw-text-white">Python API</strong>
  <span class="tw-mt-2 tw-block tw-text-slate-600 dark:tw-text-slate-300">Call the stable package API from scripts, automations, or larger Python applications.</span>
</a>

<a class="tw-block tw-rounded-2xl tw-border tw-border-slate-200 tw-bg-white tw-p-5 tw-no-underline tw-shadow-sm tw-transition hover:tw--translate-y-0.5 hover:tw-border-coop-blue hover:tw-shadow-lg dark:tw-border-slate-700 dark:tw-bg-slate-900/60" href="cli/">
  <span class="tw-text-sm tw-font-extrabold tw-uppercase tw-tracking-[0.14em] tw-text-coop-cyan">Operate</span>
  <strong class="tw-mt-2 tw-block tw-text-xl tw-text-coop-ink dark:tw-text-white">CLI Reference</strong>
  <span class="tw-mt-2 tw-block tw-text-slate-600 dark:tw-text-slate-300">Review every installed command and option: <code>translate</code>, <code>evaluate</code>, and <code>migrate-links</code>.</span>
</a>

<a class="tw-block tw-rounded-2xl tw-border tw-border-slate-200 tw-bg-white tw-p-5 tw-no-underline tw-shadow-sm tw-transition hover:tw--translate-y-0.5 hover:tw-border-coop-blue hover:tw-shadow-lg dark:tw-border-slate-700 dark:tw-bg-slate-900/60 md:tw-col-span-2" href="maintainer-guide/">
  <span class="tw-text-sm tw-font-extrabold tw-uppercase tw-tracking-[0.14em] tw-text-coop-cyan">Maintain</span>
  <strong class="tw-mt-2 tw-block tw-text-xl tw-text-coop-ink dark:tw-text-white">Maintainer Guide</strong>
  <span class="tw-mt-2 tw-block tw-text-slate-600 dark:tw-text-slate-300">Understand the public API boundary, CLI dispatch, docs workflow, and implementation flow.</span>
</a>

</div>

## Command surface

The installed commands are:

```bash
translate -l "ko ja" -md
evaluate -l "ko"
migrate-links -l "ko ja"
```

The Python API exports:

```python
from co_op_translator.api import run_translation
```

## Install the package

```bash
pip install co-op-translator
```

For repository development:

```bash
pip install -r requirements.txt
pip install -e .
```

## Build this documentation locally

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Then open `http://127.0.0.1:8000`.

To produce the static site:

```bash
mkdocs build --strict
```

The generated files are written to `site/`.
