<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-22T11:16:34+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pcm"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide

## Overview
Microsoft Co-Op Translator na strong tool wey dey help you translate Markdown documents sharp sharp. Dis guide go show you how you fit solve wahala wey fit show when you dey use am.

## Common Issues and Solutions

### 1. Markdown Tag Wahala
**Wahala:** The translated Markdown document get one `markdown` tag for the top, e dey cause wahala for how e dey show.

**How to Solve Am:** Just comot the `markdown` tag wey dey the top of the file. Once you do am, the Markdown file go dey show well.

**Steps:**
1. Open the translated Markdown (`.md`) file.
2. Find the `markdown` tag for the top of the document.
3. Delete the `markdown` tag.
4. Save the file.
5. Open the file again make sure say e dey show well.

### 2. Embedded Images URL Wahala
**Wahala:** The URL for the images wey dem embed no match the language locale, so images no dey show or e dey show wrong one.

**How to Solve Am:** Check the URL for the images, make sure say the language locale for the image file name match the document language. All images dey inside `translated_images` folder and each image get language locale for the name.

**Steps:**
1. Open the translated Markdown document.
2. Find the images wey dem embed and check their URLs.
3. Make sure say the language locale for the image file name match the document language.
4. Change the URLs if e no correct.
5. Save the file and open am again to confirm say images dey show well.

### 3. Translation No Pure
**Wahala:** The translation no too correct or e need small touch.

**How to Solve Am:** Read the translated document well, make the changes wey go make am better and easy to understand.

**Steps:**
1. Open the translated document.
2. Read the content well.
3. Make the changes wey go make the translation correct.
4. Save the file.

## 4. Permission Error Redacted or 404

If images or text no dey translate to the correct language and when you run am for -d debug mode you see 401 error, na authentication wahala be that—maybe the key no correct, e don expire, or e no dey linked to the endpoint region.

Run co-op translator with the [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) to see wetin dey cause the wahala.

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Wetin fit cause am**:
  - Subscription key wey you use no correct or e don redacted for the request.
  - AI Services Key or Subscription Key fit dey another Azure resource (like Translator or OpenAI) instead of **Azure AI Vision** resource.

 **Resource Type**
  - Go [Azure Portal](https://portal.azure.com) or [Azure AI Foundry](https://ai.azure.com) make sure say the resource na `Azure AI services` → `Vision`.
  - Check the keys, make sure say na the correct one you dey use.

## 5. Configuration Errors (New Error Handling)

With the new selective translation system, Co-op Translator go show you clear error message if you never configure the services wey e need.

### 5.1. Azure AI Service No Set for Image Translation

**Wahala:** You request image translation (`-img` flag) but Azure AI Service never set well.

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**How to Solve Am:**
1. **Option 1**: Set Azure AI Service
   - Add `AZURE_AI_SERVICE_API_KEY` for your `.env` file
   - Add `AZURE_AI_SERVICE_ENDPOINT` for your `.env` file
   - Make sure say the service dey work

2. **Option 2**: No request image translation again
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Missing Required Configuration

**Wahala:** The main LLM configuration no dey.

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**How to Solve Am:**
1. Check your `.env` file, make sure say at least one of these LLM configs dey:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   You need only Azure OpenAI OR OpenAI, no need to set both.

### 5.3. Selective Translation Confusion

**Wahala:** No file translate even though the command run finish.

**Wetin fit cause am:**
- You use wrong file type flags (`-md`, `-img`, `-nb`)
- No matching files dey for the project
- Directory structure no correct

**How to Solve Am:**
1. **Use debug mode** to see wetin dey happen:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Check file types** for your project:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Check flag combinations**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migration from Old System

### 6.1. Markdown-Only Mode No Dey Again

**Wahala:** Commands wey before dey fallback to markdown-only no dey work as before.

**Old Behavior:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**New Behavior:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**How to Solve Am:**
- **Talk am clear** wetin you wan translate:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Link Dey Go Wrong Place

**Wahala:** Links for translated files dey point go where you no expect.

**Cause:** How link dey work fit change based on the file types wey you select.

**How to Solve Am:**
1. **Understand how link dey work now**:
   - If you add `-nb`: Notebook links go point to translated versions
   - If you no add `-nb`: Notebook links go point to original files
   - If you add `-img`: Image links go point to translated versions
   - If you no add `-img`: Image links go point to original files

2. **Choose the correct combination** for wetin you wan do:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action run but no Pull Request (PR) show

**Wetin you go see:** The workflow logs for `peter-evans/create-pull-request` go talk:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Wetin fit cause am:**
- **No changes:** The translation step no make any difference (repo already dey up to date).
- **Ignored outputs:** `.gitignore` dey block files wey you wan commit (like `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths no match:** The paths wey you give the action no match where the output dey.
- **Workflow logic/conditions:** The translation step stop early or e write files for wrong place.

**How to fix / check:**
1. **Check if outputs dey:** After translation, check say new or changed files dey for `translations/` and/or `translated_images/`.
   - If you dey translate notebooks, make sure say `.ipynb` files dey under `translations/<lang>/...`.
2. **Check `.gitignore`:** No ignore the files wey the tool generate. Make sure say you NO dey ignore:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (if you dey translate notebooks)
3. **Make sure add-paths match outputs:** Use multiline value, add both folders if you need:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Force PR for debugging:** For now, allow empty commits to check if everything dey work:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Run with debug:** Add `-d` for the translate command to see which files e find and write.
6. **Permissions (GITHUB_TOKEN):** Make sure say the workflow get write permission to create commits and PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Quick Debugging Checklist

If you dey try solve translation wahala:

1. **Use debug mode**: Add `-d` flag to see better logs
2. **Check your flags**: Make sure say `-md`, `-img`, `-nb` match wetin you wan do
3. **Check configuration**: Your `.env` file suppose get the correct keys
4. **Test small small**: Start with `-md` only, then add other types join
5. **Check file structure**: Make sure say the source files dey and you fit reach am

If you wan know more about the commands and flags wey dey, check the [Command Reference](./command-reference.md).

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate this document. Even though we try make the translation correct, abeg make you sabi say AI fit make mistake or no translate am well. Na the original document for the main language be the correct one wey you suppose follow. If the information dey important, abeg use professional human translator. We no go fit hold any responsibility for wahala wey fit happen because of how this translation take be.