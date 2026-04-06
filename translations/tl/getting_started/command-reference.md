# Command reference

The **Co-op Translator** CLI offers several options to customize the translation process:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Isinasalin ang iyong proyekto sa mga tinukoy na wika. Halimbawa: translate -l "es fr de" ay nagsasalin sa Español, Pranses, at Aleman. Gamitin ang translate -l "all" para isalin sa lahat ng suportadong wika.
translate -l "language_codes" -u              | Ina-update ang mga pagsasalin sa pamamagitan ng pagtanggal ng mga umiiral at muling paglikha ng mga ito. Babala: Tatanggalin nito ang lahat ng kasalukuyang pagsasalin para sa tinukoy na mga wika.
translate -l "language_codes" -img            | Isinasalin lamang ang mga image file.
translate -l "language_codes" -md             | Isinasalin lamang ang mga Markdown file.
translate -l "language_codes" -nb             | Isinasalin lamang ang mga Jupyter notebook file (.ipynb).
translate -l "language_codes" --fix           | Muling isinasalin ang mga file na may mababang confidence score base sa mga naunang resulta ng pagsusuri.
translate -l "language_codes" -d              | Pinapagana ang debug mode para sa detalyadong logging.
translate -l "language_codes" --save-logs, -s | Ina-save ang DEBUG-level logs sa mga file sa ilalim ng <root_dir>/logs/ (ang console ay nananatiling kontrolado ng -d)
translate -l "language_codes" -r "root_dir"   | Tinukoy ang root directory ng proyekto
translate -l "language_codes" -f              | Ginagamit ang fast mode para sa pagsasalin ng imahe (hanggang 3x na mas mabilis ang plotting na may bahagyang pagsasakripisyo sa kalidad at alignment).
translate -l "language_codes" -y              | Awtomatikong kinukumpirma ang lahat ng prompt (kapaki-pakinabang para sa CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Pinapagana o pinapahinto ang paglalagay ng machine translation disclaimer section sa mga isinalin na markdown at notebook (default: pinapagana).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Pinapasadyang advisory sa bahagi ng README languages section (sparse checkout) gamit ang iyong repository URL.
translate -l "language_codes" --help          | detalyadong tulong sa loob ng CLI na nagpapakita ng mga magagamit na command
evaluate -l "language_code"                  | Sinusuri ang kalidad ng pagsasalin para sa isang partikular na wika at nagbibigay ng confidence score
evaluate -l "language_code" -c 0.8           | Sinusuri ang mga pagsasalin gamit ang custom confidence threshold
evaluate -l "language_code" -f               | Mabilis na mode ng pagsusuri (rule-based lamang, walang LLM)
evaluate -l "language_code" -D               | Malalim na mode ng pagsusuri (LLM-based lamang, mas masusi ngunit mas mabagal)
evaluate -l "language_code" --save-logs, -s  | Ina-save ang DEBUG-level logs sa mga file sa ilalim ng <root_dir>/logs/
migrate-links -l "language_codes"             | Muling pinoproseso ang mga isinaling Markdown file para i-update ang mga link sa mga notebook (.ipynb). Mas pinipili ang mga isinaling notebook kung available; kung hindi ay maaaring bumalik sa orihinal na mga notebook.
migrate-links -l "language_codes" -r          | Itinatalaga ang root directory ng proyekto (default: kasalukuyang direktoryo).
migrate-links -l "language_codes" --dry-run   | Ipinapakita kung aling mga file ang magbabago nang hindi sinusulat ang mga pagbabago.
migrate-links -l "language_codes" --no-fallback-to-original | Hindi nire-rewrite ang mga link sa orihinal na mga notebook kapag wala ang isinaling kapareha (i-update lamang kapag may isinalin).
migrate-links -l "language_codes" -d          | Pinapagana ang debug mode para sa detalyadong logging.
migrate-links -l "language_codes" --save-logs, -s | Ina-save ang DEBUG-level logs sa mga file sa ilalim ng <root_dir>/logs/
migrate-links -l "all" -y                      | Pinoproseso lahat ng wika at awtomatikong kinukumpirma ang warning prompt.

## Usage examples

  1. Default na pag-uugali (magdagdag ng bagong pagsasalin nang hindi tinatanggal ang mga umiiral):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Magdagdag lamang ng bagong pagsasalin ng Korean na mga imahe (hindi tinatanggal ang mga umiiral na pagsasalin):    translate -l "ko" -img

  3. I-update ang lahat ng pagsasalin ng Korean (Babala: Tatanggalin nito ang lahat ng umiiral na pagsasalin ng Korean bago muling isalin):    translate -l "ko" -u

  4. I-update lamang ang mga imahe ng Korean (Babala: Tatanggalin nito ang lahat ng umiiral na mga imahe ng Korean bago muling isalin):    translate -l "ko" -img -u

  5. Magdagdag ng bagong pagsasalin ng markdown para sa Korean nang hindi naaapektuhan ang ibang pagsasalin:    translate -l "ko" -md

  6. Ayusin ang mga pagsasalin na may mababang confidence base sa naunang mga resulta ng pagsusuri: translate -l "ko" --fix

  7. Ayusin ang mga pagsasalin na may mababang confidence para sa mga partikular na file lamang (markdown): translate -l "ko" --fix -md

  8. Ayusin ang mga pagsasalin na may mababang confidence para sa mga partikular na file lamang (imahe): translate -l "ko" --fix -img

  9. Gamitin ang fast mode para sa pagsasalin ng imahe:    translate -l "ko" -img -f

  10. Ayusin ang mga pagsasalin na may mababang confidence gamit ang custom threshold: translate -l "ko" --fix -c 0.8

  11. Halimbawa ng debug mode: - translate -l "ko" -d: Pinapagana ang debug logging.
  12. I-save ang logs sa mga file: translate -l "ko" -s
  13. Console DEBUG at file DEBUG: translate -l "ko" -d -s
  14. Isalin nang hindi naglalagay ng machine translation disclaimers sa mga output: translate -l "ko" --no-disclaimer

  15. I-migrate ang mga link ng notebook para sa mga pagsasalin ng Korean (i-update ang mga link sa isinaling mga notebook kapag available):    migrate-links -l "ko"

  15. I-migrate ang mga link gamit ang dry-run (hindi nagsusulat ng file):    migrate-links -l "ko" --dry-run

  16. I-update lamang ang mga link kapag mayroon nang isinaling notebook (huwag bumalik sa orihinal):    migrate-links -l "ko" --no-fallback-to-original

  17. Iproseso lahat ng wika na may kumpirmasyon na prompt:    migrate-links -l "all"

  18. Iproseso lahat ng wika at awtomatikong kumpirmahin:    migrate-links -l "all" -y
  19. I-save ang logs sa mga file para sa migrate-links:    migrate-links -l "ko ja" -s

  20. Pasadyang advisory sa README languages gamit ang iyong URL ng repo:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: Ang functionality ng pagsusuri ay kasalukuyang nasa beta. Ang tampok na ito ay inilabas upang suriin ang mga isinaling dokumento, at ang mga pamamaraan ng pagsusuri at detalyadong implementasyon ay patuloy pang dine-develop at maaaring magbago.

  1. Suriin ang mga pagsasalin sa Korean: evaluate -l "ko"

  2. Suriin gamit ang custom confidence threshold: evaluate -l "ko" -c 0.8

  3. Mabilis na pagsusuri (rule-based lamang): evaluate -l "ko" -f

  4. Malalim na pagsusuri (LLM-based lamang): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang aming pinagsusumikapang maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring may mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->