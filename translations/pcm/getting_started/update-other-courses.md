# Update di "Other Courses" section (Microsoft Beginners repos)

Dis guide dey explain how to make di "Other Courses" section auto‑synchronize using Co‑op Translator, and how to update di global template for all repos.

- Applies to: Microsoft Beginners repositories only
- Works with: Co‑op Translator CLI and GitHub Actions
- Template source: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Quick start: Enable auto‑sync for your repo

Add di following markers round di "Other Courses" section for your README. Co‑op Translator go replace everything wey dey between these markers on every run.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Every time Co‑op Translator run—via CLI (like `translate -l "<language codes>"`) or GitHub Actions—it go automatically update di "Other Courses" section wey dey wrapped by these markers.

> [!NOTE]
> If you get list wey don dey before, just wrap am with di same markers. Di next run go replace am with di latest standardized content.

---

## How to change di global content

If you want update di standardized content wey dey appear for all Beginners repos:

1. Edit di template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open one pull request to di Co-op Translator repo with your changes
3. After di PR merge, di Co‑op Translator version go update
4. Di next time Co‑op Translator run (CLI or GitHub Action) for one target repo, e go automatically sync di updated section

Dis one make sure say na one single source of truth dey for di "Other Courses" content across all Beginners repositories.


## Repo Sizes 

Di repos fit become big because of di amount of languages wey dem translate to help end users get guidance on how to use clone - sparse to only clone di necessary languages and no di whole repo 

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
Dis document don translated wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make una sabi say automated translations fit get errors or mistakes. Di original document for im own language na di correct source. For important matters, better make person wey sabi do human translation help. We no go carry mind any misunderstanding or wrong meaning wey fit arise from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->