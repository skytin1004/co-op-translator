<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-22T11:15:53+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pcm"
}
-->
# Command reference

**Co-op Translator** CLI get plenti option wey fit make you run translation anyhow wey you want:

Command                                       | Wetin e mean
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | E go translate your project go the language wey you choose. Example: translate -l "es fr de" go translate am to Spanish, French, and German. If you use translate -l "all", e go translate to all language wey dem support.
translate -l "language_codes" -u              | E go update translation by comot the one wey dey before, then do am again. Warning: E go wipe all the translation wey dey for the language wey you choose.
translate -l "language_codes" -img            | E go translate only image files.
translate -l "language_codes" -md             | E go translate only Markdown files.
translate -l "language_codes" -nb             | E go translate only Jupyter notebook files (.ipynb).
translate -l "language_codes" --fix           | E go re-translate files wey get low confidence score based on the last evaluation.
translate -l "language_codes" -d              | E go open debug mode so you fit see beta log.
translate -l "language_codes" --save-logs, -s | E go save DEBUG log for file inside <root_dir>/logs/ (console still dey control with -d)
translate -l "language_codes" -r "root_dir"   | E go tell am where your project root directory dey
translate -l "language_codes" -f              | E go use fast mode for image translation (fit run 3x faster but small quality and alignment fit loss).
translate -l "language_codes" -y              | E go confirm all prompt by itself (good for CI/CD pipeline)
translate -l "language_codes" --help          | E go show help for CLI, show all command wey dey
evaluate -l "language_code"                  | E go check how beta translation dey for one language, show confidence score
evaluate -l "language_code" -c 0.8           | E go check translation with your own confidence threshold
evaluate -l "language_code" -f               | Fast evaluation mode (na only rule-based, no LLM)
evaluate -l "language_code" -D               | Deep evaluation mode (na only LLM, e dey thorough but e slow)
evaluate -l "language_code" --save-logs, -s  | E go save DEBUG log for file inside <root_dir>/logs/
migrate-links -l "language_codes"             | E go reprocess translated Markdown files to update link to notebook (.ipynb). If translated notebook dey, e go use am; if e no dey, e fit use original notebook.
migrate-links -l "language_codes" -r          | E go tell am where your project root directory dey (default na current directory).
migrate-links -l "language_codes" --dry-run   | E go show you the files wey go change but e no go write am.
migrate-links -l "language_codes" --no-fallback-to-original | E no go change link to original notebook if translated one no dey (e go only update if translated dey).
migrate-links -l "language_codes" -d          | E go open debug mode so you fit see beta log.
migrate-links -l "language_codes" --save-logs, -s | E go save DEBUG log for file inside <root_dir>/logs/
migrate-links -l "all" -y                      | E go process all language and confirm warning prompt by itself.

## Usage examples

  1. Default way (e go add new translation, e no go comot the one wey dey before):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Add only new Korean image translation (e no go comot the one wey dey before):    translate -l "ko" -img

  3. Update all Korean translation (Warning: E go comot all Korean translation before e do am again):    translate -l "ko" -u

  4. Update only Korean images (Warning: E go comot all Korean image before e do am again):    translate -l "ko" -img -u

  5. Add new markdown translation for Korean, e no go touch other translation:    translate -l "ko" -md

  6. Fix translation wey get low confidence based on last evaluation: translate -l "ko" --fix

  7. Fix low confidence translation for only some files (markdown): translate -l "ko" --fix -md

  8. Fix low confidence translation for only some files (images): translate -l "ko" --fix -img

  9. Use fast mode for image translation:    translate -l "ko" -img -f

  10. Fix low confidence translation with your own threshold: translate -l "ko" --fix -c 0.8

  11. Debug mode example: - translate -l "ko" -d: E go open debug logging.
  12. Save log for file: translate -l "ko" -s
  13. Console DEBUG and file DEBUG: translate -l "ko" -d -s

  14. Migrate notebook link for Korean translation (e go update link to translated notebook if e dey):    migrate-links -l "ko"

  15. Migrate link with dry-run (e no go write file):    migrate-links -l "ko" --dry-run

  16. Only update link if translated notebook dey (e no go fallback to original):    migrate-links -l "ko" --no-fallback-to-original

  17. Process all language with confirmation prompt:    migrate-links -l "all"

  18. Process all language and confirm by itself:    migrate-links -l "all" -y
  19. Save log for file for migrate-links:    migrate-links -l "ko ja" -s

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: The evaluation feature still dey beta. Dem release am so people fit check translated document, but the way e dey work and how dem do am still dey change.

  1. Check Korean translation: evaluate -l "ko"

  2. Check with your own confidence threshold: evaluate -l "ko" -c 0.8

  3. Fast evaluation (na only rule-based): evaluate -l "ko" -f

  4. Deep evaluation (na only LLM): evaluate -l "ko" -D

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate this document. Even though we try make the translation correct, abeg make you sabi say machine translation fit get mistake or no too dey accurate. Na the original document for the main language be the correct one wey you suppose follow. If the information dey very important, abeg use professional human translation. We no go fit hold any responsibility for wahala or wrong understanding wey fit happen because of this translation.