# Command reference

The **Co-op Translator** CLI get plenty options to customize how you go take do translation:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | E go translate your project enter the languages wey you specify. Example: translate -l "es fr de" go translate go Spanish, French, and German. Use translate -l "all" to translate enter all the languages wey dem dey support.
translate -l "language_codes" -u              | E go update translations by deleting the ones wey dey first and then e go create dem again. Warning: This one mean say e go delete all the translations wey dey for the languages wey you select.
translate -l "language_codes" -img            | E go translate only the image files.
translate -l "language_codes" -md             | E go translate only the Markdown files.
translate -l "language_codes" -nb             | E go translate only the Jupyter notebook files (.ipynb).
translate -l "language_codes" --fix           | E go re-translate the files wey get low confidence score based on how e be before.
translate -l "language_codes" -d              | E go enable debug mode to show detailed logs.
translate -l "language_codes" --save-logs, -s | E go save DEBUG-level logs for files under <root_dir>/logs/ (console still dey control by -d)
translate -l "language_codes" -r "root_dir"   | E go specify the root directory of the project
translate -l "language_codes" -f              | E go use fast mode for image translation (fit plot sharp sharp times 3 but e fit affect quality and how e dey align small).
translate -l "language_codes" -y              | E go automatically confirm all prompts (good for CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Enable or disable to add machine translation disclaimer section to translated markdown and notebooks (default be say e dey enabled).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | E go personalize the README languages section advisory (sparse checkout) with your repository URL.
translate -l "language_codes" --help          | Help details inside the CLI wey show available commands
evaluate -l "language_code"                  | E go evaluate translation quality for one language and give confidence scores
evaluate -l "language_code" -c 0.8           | E go evaluate translations with custom confidence threshold
evaluate -l "language_code" -f               | Fast evaluation mode (na rule-based only, no LLM)
evaluate -l "language_code" -D               | Deep evaluation mode (na LLM-based only, e deep but e slow)
evaluate -l "language_code" --save-logs, -s  | E go save DEBUG-level logs for files under <root_dir>/logs/
migrate-links -l "language_codes"             | E go reprocess translated Markdown files to update links to notebooks (.ipynb). E prefer translated notebooks if e dey; if no, e fit use original notebooks.
migrate-links -l "language_codes" -r          | E go specify the project root directory (default na current directory).
migrate-links -l "language_codes" --dry-run   | E go show which files go change but no write any change.
migrate-links -l "language_codes" --no-fallback-to-original | No go rewrite links go original notebooks when translated counterparts no dey (e go update only if the translated one dey).
migrate-links -l "language_codes" -d          | E go enable debug mode for detailed logging.
migrate-links -l "language_codes" --save-logs, -s | E go save DEBUG-level logs for files under <root_dir>/logs/
migrate-links -l "all" -y                      | E go process all languages and auto-confirm the warning prompt.

## Usage examples

  1. Default behaviour (add new translations no delete the ones wey already dey):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Add only new Korean image translations (no delete any translation wey dey):    translate -l "ko" -img

  3. Update all Korean translations (Warning: This one go delete all the current Korean translations before e go re-translate):    translate -l "ko" -u

  4. Update only Korean images (Warning: This one go delete all current Korean images before e go re-translate):    translate -l "ko" -img -u

  5. Add new markdown translations for Korean without touching other translations:    translate -l "ko" -md

  6. Fix translations wey get low confidence based on the last evaluation results: translate -l "ko" --fix

  7. Fix translations with low confidence for specific files only (markdown): translate -l "ko" --fix -md

  8. Fix translations with low confidence for specific files only (images): translate -l "ko" --fix -img

  9. Use fast mode for image translation:    translate -l "ko" -img -f

  10. Fix low confidence translations with your own confidence threshold: translate -l "ko" --fix -c 0.8

  11. Debug mode example: - translate -l "ko" -d: E go enable debug logging.
  12. Save logs to files: translate -l "ko" -s
  13. Console DEBUG and file DEBUG: translate -l "ko" -d -s
  14. Translate without adding machine translation disclaimers: translate -l "ko" --no-disclaimer

  15. Migrate notebook links for Korean translations (update links to translated notebooks if e dey):    migrate-links -l "ko"

  15. Migrate links with dry-run (no file writes):    migrate-links -l "ko" --dry-run

  16. Only update links if translated notebooks dey (no fallback to originals):    migrate-links -l "ko" --no-fallback-to-original

  17. Process all languages with confirmation prompt:    migrate-links -l "all"

  18. Process all languages and auto-confirm:    migrate-links -l "all" -y
  19. Save logs to files for migrate-links:    migrate-links -l "ko ja" -s

  20. Personalize README languages advisory with your repo URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: The evaluation functionality still dey beta. This feature na to evaluate translated documents, and the way e take work plus all the details still dey develop and fit change later.

  1. Evaluate Korean translations: evaluate -l "ko"

  2. Evaluate with custom confidence threshold: evaluate -l "ko" -c 0.8

  3. Fast evaluation (na rule-based only): evaluate -l "ko" -f

  4. Deep evaluation (LLM-based only): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make e correct, abeg sabi say automated translations fit get some errors or wahala. Di original document for dia own language na di correct one wey you suppose trust. If na serious matter, e good make professional human translation do am. We no go responsible for any misunderstanding or wrong meaning wey fit come from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->