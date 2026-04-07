# Command reference

The **Co-op Translator** CLI offers several options to customize the translation process:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Isinalin ang iyong proyekto sa mga tinukoy na wika. Halimbawa: translate -l "es fr de" ay nagsasalin sa Spanish, French, at German. Gamitin ang translate -l "all" upang isalin sa lahat ng suportadong wika.
translate -l "language_codes" -u              | Ina-update ang mga pagsasalin sa pamamagitan ng pagtanggal ng mga umiiral at muling paggawa ng mga ito. Babala: Tatanggalin nito lahat ng kasalukuyang pagsasalin para sa mga tinukoy na wika.
translate -l "language_codes" -img            | Isinasalin lamang ang mga file ng larawan.
translate -l "language_codes" -md             | Isinasalin lamang ang mga Markdown file.
translate -l "language_codes" -nb             | Isinasalin lamang ang mga Jupyter notebook file (.ipynb).
translate -l "language_codes" --fix           | Muling isinasalin ang mga file na may mababang kumpiyansa base sa mga naunang resulta ng pagsusuri.
translate -l "language_codes" -d              | Pinapagana ang debug mode para sa detalyadong pag-log.
translate -l "language_codes" --save-logs, -s | I-save ang DEBUG-level na mga log sa mga file sa ilalim ng <root_dir>/logs/ (ang console ay nananatiling kontrolado ng -d)
translate -l "language_codes" -r "root_dir"   | Tinukoy ang root directory ng proyekto
translate -l "language_codes" -f              | Gumagamit ng fast mode para sa pagsasalin ng mga larawan (hanggang 3x na mas mabilis na paggawa ng guhit sa kaunting kawalan sa kalidad at pagkaka-align).
translate -l "language_codes" -y              | Awtomatikong kinukumpirma lahat ng mga prompt (kapaki-pakinabang para sa CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Pinapagana o hindi pinapagana ang pagdaragdag ng bahagi ng disclaimer ng machine translation sa mga isinaling markdown at notebook (default: naka-enable).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Pinapasadya ang seksyon ng mga wika sa README advisory (sparse checkout) gamit ang URL ng iyong repository.
translate -l "language_codes" --help          | mga detalye ng tulong sa loob ng CLI na nagpapakita ng mga magagamit na utos
evaluate -l "language_code"                  | Sinusuri ang kalidad ng pagsasalin para sa isang partikular na wika at nagbibigay ng mga confidence score
evaluate -l "language_code" -c 0.8           | Sinusuri ang mga pagsasalin na may pasadyang threshold ng kumpiyansa
evaluate -l "language_code" -f               | Mabilis na mode ng pagsusuri (base lamang sa patakaran, walang LLM)
evaluate -l "language_code" -D               | Malalim na mode ng pagsusuri (base lamang sa LLM, mas masinsin ngunit mas mabagal)
evaluate -l "language_code" --save-logs, -s  | I-save ang DEBUG-level na mga log sa mga file sa ilalim ng <root_dir>/logs/
migrate-links -l "language_codes"             | Muling pinoproseso ang mga isinaling Markdown file para i-update ang mga link sa mga notebook (.ipynb). Pinipili ang mga isinaling notebook kapag magagamit; kung hindi, maaari bumalik sa orihinal.
migrate-links -l "language_codes" -r          | Tukuyin ang root directory ng proyekto (default: kasalukuyang directory).
migrate-links -l "language_codes" --dry-run   | Ipakita kung alin ang mga file na magbabago nang hindi nagsusulat ng mga pagbabago.
migrate-links -l "language_codes" --no-fallback-to-original | Huwag i-rewrite ang mga link sa mga orihinal na notebook kapag nawawala ang mga isinaling katapat (nag-a-update lamang kapag may isinalin).
migrate-links -l "language_codes" -d          | Pinapagana ang debug mode para sa detalyadong pag-log.
migrate-links -l "language_codes" --save-logs, -s | I-save ang DEBUG-level na mga log sa mga file sa ilalim ng <root_dir>/logs/
migrate-links -l "all" -y                      | Pinoproseso ang lahat ng wika at awtomatikong kinukumpirma ang babalang prompt.

## Usage examples

  1. Default behavior (magdagdag ng bagong mga pagsasalin nang hindi tinatanggal ang mga kasalukuyan):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Magdagdag lamang ng mga bagong pagsasalin ng imahe sa Korean (hindi tinatanggal ang mga kasalukuyang pagsasalin):    translate -l "ko" -img

  3. I-update lahat ng pagsasalin sa Korean (Babala: Tatanggalin nito lahat ng umiiral na pagsasalin sa Korean bago muling isalin):    translate -l "ko" -u

  4. I-update lamang ang mga larawan sa Korean (Babala: Tatanggalin nito lahat ng umiiral na mga larawan sa Korean bago muling isalin):    translate -l "ko" -img -u

  5. Magdagdag ng bagong mga pagsasalin ng markdown para sa Korean nang hindi naaapektuhan ang ibang mga pagsasalin:    translate -l "ko" -md

  6. Ayusin ang mga pagsasalin na may mababang kumpiyansa base sa naunang mga resulta ng pagsusuri: translate -l "ko" --fix

  7. Ayusin ang mga mababang kumpiyansang pagsasalin para sa mga partikular na file lamang (markdown): translate -l "ko" --fix -md

  8. Ayusin ang mga mababang kumpiyansang pagsasalin para sa mga partikular na file lamang (mga larawan): translate -l "ko" --fix -img

  9. Gumamit ng mabilis na mode para sa pagsasalin ng larawan:    translate -l "ko" -img -f

  10. Ayusin ang mga mababang kumpiyansang pagsasalin gamit ang pasadyang threshold: translate -l "ko" --fix -c 0.8

  11. Halimbawa ng debug mode: - translate -l "ko" -d: I-enable ang debug logging.
  12. I-save ang mga log sa mga file: translate -l "ko" -s
  13. Console DEBUG at file DEBUG: translate -l "ko" -d -s
  14. Isalin nang hindi nagdaragdag ng mga disclaimer ng machine translation sa mga output: translate -l "ko" --no-disclaimer

  15. I-migrate ang mga link ng notebook para sa mga pagsasalin sa Korean (i-update ang mga link sa isinaling mga notebook kapag magagamit):    migrate-links -l "ko"

  15. I-migrate ang mga link gamit ang dry-run (hindi nagsusulat sa file):    migrate-links -l "ko" --dry-run

  16. I-update lamang ang mga link kapag may mga isinaling notebook (huwag bumalik sa orihinal):    migrate-links -l "ko" --no-fallback-to-original

  17. Iproseso ang lahat ng wika na may prompt ng kumpirmasyon:    migrate-links -l "all"

  18. Iproseso ang lahat ng wika at awtomatikong kumpirmahin:    migrate-links -l "all" -y
  19. I-save ang mga log sa mga file para sa migrate-links:    migrate-links -l "ko ja" -s

  20. Pasadyang advisory ng README na seksyon ng mga wika gamit ang iyong URL ng repo:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: Ang functionality ng pagsusuri ay kasalukuyang nasa beta. Ang tampok na ito ay inilabas upang suriin ang mga isinaling dokumento, at ang mga paraan ng pagsusuri at detalyadong implementasyon ay nasa ilalim pa ng pagbuo at maaaring magbago.

  1. Suriin ang mga pagsasalin sa Korean: evaluate -l "ko"

  2. Suriin gamit ang pasadyang threshold ng kumpiyansa: evaluate -l "ko" -c 0.8

  3. Mabilis na pagsusuri (base lamang sa patakaran): evaluate -l "ko" -f

  4. Malalim na pagsusuri (base lamang sa LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagsisiwalat**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa kawastuhan, pakatandaan na ang mga automated na pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring mabuo mula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->