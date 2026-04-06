# Command reference

Di **Co-op Translator** CLI get plenty options wey fit customize di translation process:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | E go translate your project into di languages wey you specify. Example: translate -l "es fr de" go translate am go Spanish, French, and German. Use translate -l "all" to translate am go all di languages wey dem support.
translate -l "language_codes" -u              | E go update di translations by deleting di ones wey don already dey and create dem again. Warning: Dis one go delete all di current translations for di languages wey you specify.
translate -l "language_codes" -img            | E go translate only image files dem.
translate -l "language_codes" -md             | E go translate only Markdown files.
translate -l "language_codes" -nb             | E go translate only Jupyter notebook files (.ipynb).
translate -l "language_codes" --fix           | E go retranslate files wey get low confidence scores based on di previous evaluation results.
translate -l "language_codes" -d              | E go enable debug mode for detailed logging.
translate -l "language_codes" --save-logs, -s | E go save DEBUG-level logs go files inside <root_dir>/logs/ (console still dey controlled by -d)
translate -l "language_codes" -r "root_dir"   | E go specify di root directory of di project
translate -l "language_codes" -f              | E go use fast mode for image translation (e fit plot 3x faster but di quality and alignment fit reduce small).
translate -l "language_codes" -y              | E go automatically confirm all prompts (good for CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | E go enable or disable adding machine translation disclaimer section for translated markdown and notebooks (default na enabled).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | E go personalize di README languages section advisory (sparse checkout) with your repo URL.
translate -l "language_codes" --help          | Help details inside di CLI wey dey show di available commands
evaluate -l "language_code"                  | E evaluate di translation quality for one particular language and give confidence scores
evaluate -l "language_code" -c 0.8           | E evaluate translations with custom confidence threshold
evaluate -l "language_code" -f               | Fast evaluation mode (rule-based only, no LLM)
evaluate -l "language_code" -D               | Deep evaluation mode (LLM-based only, more thorough but slower)
evaluate -l "language_code" --save-logs, -s  | E save DEBUG-level logs go files inside <root_dir>/logs/
migrate-links -l "language_codes"             | E go reprocess translated Markdown files to update links to notebooks (.ipynb). E prefer with translated notebooks when dem dey; if no translate, e fit fallback to original notebooks.
migrate-links -l "language_codes" -r          | E specify di root directory of di project (default na current directory).
migrate-links -l "language_codes" --dry-run   | Show which files go change without writing di changes.
migrate-links -l "language_codes" --no-fallback-to-original | No go rewrite di links go original notebooks if translated ones no dey (go update links only when translated versions dey).
migrate-links -l "language_codes" -d          | Enable debug mode for detailed logging.
migrate-links -l "language_codes" --save-logs, -s | Save DEBUG-level logs go files inside <root_dir>/logs/
migrate-links -l "all" -y                      | Process all languages and auto-confirm di warning prompt.

## Usage examples

  1. Default behavior (add new translations without deleting existing ones):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Add only new Korean image translations (no existing translations dey deleted):    translate -l "ko" -img

  3. Update all Korean translations (Warning: Dis one dey delete all existing Korean translations before e translate again):    translate -l "ko" -u

  4. Update only Korean images (Warning: Dis one dey delete all existing Korean images before e translate again):    translate -l "ko" -img -u

  5. Add new markdown translations for Korean without affecting other translations:    translate -l "ko" -md

  6. Fix low confidence translations based on previous evaluation results: translate -l "ko" --fix

  7. Fix low confidence translations for specific files only (markdown): translate -l "ko" --fix -md

  8. Fix low confidence translations for specific files only (images): translate -l "ko" --fix -img

  9. Use fast mode for image translation:    translate -l "ko" -img -f

  10. Fix low confidence translations with custom threshold: translate -l "ko" --fix -c 0.8

  11. Debug mode example: - translate -l "ko" -d: Enable debug logging.
  12. Save logs go files: translate -l "ko" -s
  13. Console DEBUG and file DEBUG: translate -l "ko" -d -s
  14. Translate without adding machine translation disclaimers go outputs: translate -l "ko" --no-disclaimer

  15. Migrate notebook links for Korean translations (update links to translated notebooks when dem dey):    migrate-links -l "ko"

  15. Migrate links with dry-run (no file writes):    migrate-links -l "ko" --dry-run

  16. Only update links when translated notebooks dey (no fallback go original ones):    migrate-links -l "ko" --no-fallback-to-original

  17. Process all languages with confirmation prompt:    migrate-links -l "all"

  18. Process all languages and auto-confirm:    migrate-links -l "all" -y
  19. Save logs go files for migrate-links:    migrate-links -l "ko ja" -s

  20. Personalize README languages advisory with your repo URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: Di evaluation functionality still dey beta. Dis feature na beta release to evaluate translated documents, and di evaluation methods and detailed implementation still dey for development and fit change.

  1. Evaluate Korean translations: evaluate -l "ko"

  2. Evaluate with custom confidence threshold: evaluate -l "ko" -c 0.8

  3. Fast evaluation (rule-based only): evaluate -l "ko" -f

  4. Deep evaluation (LLM-based only): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document na im we use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate am. Even though we dey try make am correct, abeg make una sabi say automated translations fit get errors or mistakes. The original document for im native language na im be the main correct source. For important information, make you use professional human translation. We no go responsible for any misunderstanding or wrong meaning wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->