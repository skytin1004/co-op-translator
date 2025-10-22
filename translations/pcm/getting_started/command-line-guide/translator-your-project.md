<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-22T11:17:28+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "pcm"
}
-->
# How you go take translate your project with Co-op Translator

**Co-op Translator** na command-line tool wey go help you translate markdown and image files for your project to plenty languages. This section go show you how you fit use the tool, talk about the different CLI options wey dey, and give you example for different ways wey you fit use am.

> [!NOTE]
> If you wan see all the commands and wetin dem mean, check the [Command reference](./command-reference.md).

---

## Example Ways and Commands

See some common ways wey people dey use **Co-op Translator**, plus the correct command wey you go run.

### 1. Basic Translation (One Language)

If you wan translate your whole project (markdown files and images) to one language, like Korean, run this command:

```bash
translate -l "ko"
```

This command go translate all your markdown and image files to Korean, e go add new translation but e no go delete any one wey dey before.

> [!TIP]
>
> You wan know the language codes wey **Co-op Translator** dey support? Go the [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) section for the repo to see more.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, na this method I use take add Korean translation for the markdown files and images wey dey.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Translation for Plenty Languages

If you wan translate your project to plenty languages (like Spanish, French, and German), use this command:

```bash
translate -l "es fr de"
```

This command go translate your project to Spanish, French, and German, e go add new translation but e no go touch the ones wey dey before.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, after I pull the latest changes to get the newest commits, na this method I use take translate the new markdown files and images wey I add.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Normally, e better make you translate one language at a time, but if na special change you wan add, to translate plenty languages once fit make sense.

### 3. Update Translation (E go Delete Old Ones)

If you wan update translation (like delete the old translation and put new one), use the `-u` option. E go delete all the translation for the language wey you choose and do fresh translation.

```bash
translate -l "ko" -u
```

Warning: This command go ask you make you confirm before e go delete the old translation.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, na this method I use take update all the Spanish translated files. I dey recommend this method if the original content change well well for plenty markdown documents. But if na only small translated markdown files you wan update, e better make you delete those files by hand and use the `-a` method to add the new translation.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Translate Only Images

If na only image files you wan translate for your project, use the `-img` option:

```bash
translate -l "ko" -img
```

This command go translate only the images to Korean, e no go touch any markdown file.

### 6. Translate Only Markdown Files

If na only markdown files you wan translate for your project, use the `-md` option:

```bash
translate -l "ko" -md
```

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, na this method I use take check for translation error for the Korean files and e go try translate again for any file wey get wahala.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

This option dey check for translation error. For now, if the line break difference between the original and translated file pass six, e go mark am as translation error. I dey plan to make this check better for future.

For example, this method dey useful to find missing part or translation wey spoil, and e go try translate those files again by itself.

But if you already sabi the files wey get problem, e better make you delete those files by hand and use the `-a` option to translate them again.

### 8. Debug Mode

If you wan see plenty log for troubleshooting, use the `-d` option:

```bash
translate -l "ko" -d
```

This command go run the translation for debug mode, e go show you extra log wey fit help you find problem for the translation process.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, I see one wahala wey translation with plenty links for markdown files dey cause formatting error, like translation wey break and line break wey e no gree do. To check wetin dey happen, I use the `-d` option to see how the translation dey work.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Translate All Languages

If you wan translate your project to all the languages wey the tool support, use the all keyword.

> [!WARNING]
> To translate all languages once fit take plenty time, depend on how big your project be. For example, to translate **Phi-3 CookBook** to Spanish take about 2 hours. If the work big, e no make sense for one person to do 20 languages. E better make you share the work for plenty people, each person go handle one or two languages, and update translation small small.

```bash
translate -l "all"
```

This command go translate your project to all the languages wey dey. If you run am, just know say e fit take plenty time, depend on how big your project be.

> [!TIP]
>
> ### How to Delete Translated Files by Hand (Optional)
> Translated files now dey auto detect and clean when you update the source file.
>
> But if you wan update translation by hand - like you wan redo one file or override the system - you fit use this command to delete all version of the file for all language folders.
>
> ### For Windows:
> 1. **Use Command Prompt**:
>    - Open Command Prompt.
>    - Use `cd` to enter the folder wey get the files.
>    - Use this command to delete files:
>      ```
>      del /s *filename*
>      ```
>      Change `filename` to the part of the file name wey you dey find. `/s` go search inside subfolders too.
>
> 2. **Use PowerShell**:
>    - Open PowerShell.
>    - Run this command:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Change `"C:\YourPath"` to your folder path and `filename` to the name wey you dey find.
>
> ### For macOS/Linux:
> 1. **Use Terminal**:
>   - Open Terminal.
>   - Use `cd` to enter the folder.
>   - Use the `find` command:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Change `filename` to the name wey you dey find.
>
> Always check the files well before you delete, make you no go delete wetin you no suppose.
>
> After you delete the files wey you wan replace, just run your `translate -l` command again to update the files with the latest change.

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate dis document. Even though we try make e correct, abeg make you sabi say machine translation fit get mistake or wahala. Na the original document for the main language be the correct one wey you suppose trust. If the info dey important, abeg use professional human translation. We no go fit hold any responsibility for any wahala or misunderstanding wey fit happen because you use this translation.