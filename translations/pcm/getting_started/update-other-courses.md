# Update di "Other Courses" section (Microsoft Beginners repos)

Dis guide dey explain how to make di "Other Courses" section auto‑synchronize using Co‑op Translator, an how to update di global template for all repos.

- Ede to: Microsoft Beginners repositories only
- E dey work wit: Co‑op Translator CLI and GitHub Actions
- Template source: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Quick start: Enable auto‑sync for your repo

Add di following markers round di "Other Courses" section for your README. Co‑op Translator go replace everytin between these markers anytime e run.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Every time Co‑op Translator run—via CLI (for example, `translate -l "<language codes>"`) or GitHub Actions—e go automatically update di "Other Courses" section wey di markers dey wrap.

> [!NOTE]
> If you get already existing list, just wrap am wit di same markers. Di next run go replace am wit di latest standard content.

---

## How to change di global content

If you want update di standard content wey dey appear for all Beginners repos:

1. Edit di template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open pull request for Co-op Translator repo wit your changes
3. After PR don merge, Co‑op Translator version go update
4. Next time wey Co‑op Translator run (CLI or GitHub Action) for di target repo, e go automatically sync di updated section

Dis one dey make sure say only one source of truth dey for di "Other Courses" content for all Beginners repositories.

## Repo Sizes 

Di repos fit become big because of di number of languages wey dem translate to, to help end users sabi how to use clone - sparse to only clone di necessary languages and no di whole repo 

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am correct, abeg sabi say automated translations fit get errors or mistakes. Di original dokument for im own language na di main correct source. If na serious info, better make person wey sabi do professional human translation do am. We no responsible for any misunderstandings or wrong meaning wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->