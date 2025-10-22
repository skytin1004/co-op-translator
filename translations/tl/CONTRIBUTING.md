<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:00:58+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tl"
}
-->
# Pag-aambag sa Co-op Translator

Malugod naming tinatanggap ang mga ambag at suhestiyon sa proyektong ito. Karamihan sa mga ambag ay nangangailangan na sumang-ayon ka sa isang Contributor License Agreement (CLA) na nagsasaad na may karapatan kang ibigay at aktwal mong ibinibigay sa amin ang mga karapatan na gamitin ang iyong ambag. Para sa detalye, bisitahin ang https://cla.opensource.microsoft.com.

Kapag nagsumite ka ng pull request, awtomatikong tutukuyin ng isang CLA bot kung kailangan mong magbigay ng CLA at lalagyan ng tamang palatandaan ang PR (hal. status check, komento). Sundin lamang ang mga tagubilin ng bot. Kailangan mo lang gawin ito nang isang beses para sa lahat ng repo na gumagamit ng aming CLA.

## Pag-setup ng Development Environment

Para i-setup ang development environment ng proyektong ito, inirerekomenda naming gamitin ang Poetry para sa pamamahala ng dependencies. Ginagamit namin ang `pyproject.toml` para sa pamamahala ng dependencies ng proyekto, kaya para mag-install ng dependencies, dapat mong gamitin ang Poetry.

### Gumawa ng Virtual Environment

#### Gamit ang pip

```bash
python -m venv .venv
```

#### Gamit ang Poetry

```bash
poetry init
```

### I-activate ang Virtual Environment

#### Para sa pip at Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Gamit ang Poetry

```bash
poetry shell
```

### Pag-install ng Package at mga Kailangan na Package

#### Gamit ang Poetry (mula sa pyproject.toml)

```bash
poetry install
```

### Manwal na Pagsusuri

Bago magsumite ng PR, mahalagang subukan ang functionality ng pagsasalin gamit ang totoong dokumentasyon:

1. Gumawa ng test directory sa root directory:
    ```bash
    mkdir test_docs
    ```

2. Kopyahin ang ilang markdown documentation at mga larawan na gusto mong isalin papunta sa test directory. Halimbawa:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. I-install ang package nang lokal:
    ```bash
    pip install -e .
    ```

4. Patakbuhin ang Co-op Translator sa iyong mga test document:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Suriin ang mga isinaling file sa `test_docs/translations` at `test_docs/translated_images` para tiyakin na:
   - Maganda ang kalidad ng pagsasalin
   - Tama ang metadata comments
   - Napanatili ang orihinal na markdown structure
   - Maayos ang mga link at larawan

Nakakatulong ang manwal na pagsusuri na ito para matiyak na gumagana nang maayos ang iyong mga pagbabago sa totoong sitwasyon.

### Environment Variables

1. Gumawa ng `.env` file sa root directory sa pamamagitan ng pagkopya ng ibinigay na `.env.template` file.
1. Punan ang mga environment variable ayon sa gabay.

> [!TIP]
>
> ### Karagdagang Opsyon para sa Development Environment
>
> Bukod sa pagpapatakbo ng proyekto nang lokal, maaari mo ring gamitin ang GitHub Codespaces o VS Code Dev Containers bilang alternatibong paraan ng pag-setup ng development environment.
>
> #### GitHub Codespaces
>
> Maaari mong patakbuhin ang mga sample na ito online gamit ang GitHub Codespaces at hindi na kailangan ng karagdagang setup.
>
> Bubuksan ng button ang isang web-based na VS Code instance sa iyong browser:
>
> 1. Buksan ang template (maaaring tumagal ito ng ilang minuto):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Pagpapatakbo nang Lokal gamit ang VS Code Dev Containers
>
> ⚠️ Gagana lang ang opsyong ito kung ang iyong Docker Desktop ay may hindi bababa sa 16 GB na RAM. Kung mas mababa sa 16 GB ang RAM mo, subukan ang [GitHub Codespaces option](../..) o [i-setup ito nang lokal](../..).
>
> Isa pang opsyon ay ang VS Code Dev Containers, na magbubukas ng proyekto sa iyong lokal na VS Code gamit ang [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. I-start ang Docker Desktop (i-install kung wala pa)
> 2. Buksan ang proyekto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

Gumagamit kami ng [Black](https://github.com/psf/black) bilang Python code formatter para mapanatili ang pare-parehong istilo ng code sa buong proyekto. Ang Black ay isang code formatter na awtomatikong nire-reformat ang Python code para sumunod sa Black code style.

#### Configuration

Ang configuration ng Black ay nakasaad sa aming `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Pag-install ng Black

Maaari mong i-install ang Black gamit ang Poetry (inirerekomenda) o pip:

##### Gamit ang Poetry

Awtomatikong na-i-install ang Black kapag in-setup mo ang development environment:
```bash
poetry install
```

##### Gamit ang pip

Kung pip ang gamit mo, puwede mong i-install ang Black nang direkta:
```bash
pip install black
```

#### Paggamit ng Black

##### Gamit ang Poetry

1. I-format ang lahat ng Python file sa proyekto:
    ```bash
    poetry run black .
    ```

2. I-format ang isang partikular na file o directory:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Gamit ang pip

1. I-format ang lahat ng Python file sa proyekto:
    ```bash
    black .
    ```

2. I-format ang isang partikular na file o directory:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Inirerekomenda naming i-setup ang iyong editor para awtomatikong mag-format ng code gamit ang Black tuwing magse-save. Karamihan sa mga modernong editor ay may suporta para dito sa pamamagitan ng mga extension o plugin.

## Pagpapatakbo ng Co-op Translator

Para patakbuhin ang Co-op Translator gamit ang Poetry sa iyong environment, sundin ang mga hakbang na ito:

1. Pumunta sa directory kung saan mo gustong magsagawa ng translation tests o gumawa ng temporary folder para sa testing.

2. I-execute ang sumusunod na command. Palitan ang `-l ko` ng language code na gusto mong pagsalinan. Ang `-d` flag ay nangangahulugang debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Tiyaking naka-activate ang iyong Poetry environment (poetry shell) bago patakbuhin ang command.

## Mag-ambag ng Bagong Wika

Malugod naming tinatanggap ang mga ambag na magdadagdag ng suporta para sa mga bagong wika. Bago magbukas ng PR, kumpletuhin muna ang mga hakbang sa ibaba para maging maayos ang review.

1. Idagdag ang wika sa font mapping
   - I-edit ang `src/co_op_translator/fonts/font_language_mappings.yml`
   - Magdagdag ng entry na may:
     - `code`: ISO-like language code (hal. `vi`)
     - `name`: Pangalan ng wika na madaling maintindihan
     - `font`: Font na kasama sa `src/co_op_translator/fonts/` na sumusuporta sa script
     - `rtl`: `true` kung right-to-left, kung hindi ay `false`

2. Isama ang kinakailangang font files (kung kailangan)
   - Kung kailangan ng bagong font, tiyakin ang lisensya ay compatible para sa open source distribution
   - Idagdag ang font file sa `src/co_op_translator/fonts/`

3. Lokal na beripikasyon
   - Patakbuhin ang pagsasalin para sa maliit na sample (Markdown, images, at notebooks kung naaangkop)
   - Tiyaking tama ang output, kasama ang font at anumang RTL layout kung kailangan

4. I-update ang dokumentasyon
   - Tiyaking lumalabas ang wika sa `getting_started/supported-languages.md`
   - Walang kailangang baguhin sa `README_languages_template.md`; awtomatiko itong nabubuo mula sa supported list

5. Magbukas ng PR
   - Ilarawan ang wikang idinagdag at anumang font/licensing considerations
   - Mag-attach ng screenshot ng rendered outputs kung maaari

Halimbawa ng YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Subukan ang Bagong Wika

Maaari mong subukan ang bagong wika sa pamamagitan ng pagpapatakbo ng sumusunod na command:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## Mga Tagapangalaga

### Commit Message at Merge Strategy

Para mapanatili ang consistency at kalinawan sa commit history ng aming proyekto, sinusunod namin ang isang partikular na format ng commit message **para sa final commit message** kapag ginagamit ang **Squash and Merge** strategy.

Kapag na-merge ang isang pull request (PR), pagsasamahin ang mga indibidwal na commit sa isang commit. Dapat sundin ng final commit message ang format sa ibaba para mapanatili ang malinis at consistent na history.

#### Commit Message Format (para sa squash and merge)

Gamit namin ang sumusunod na format para sa commit messages:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Tinutukoy ang kategorya ng commit. Ginagamit namin ang mga sumusunod na type:
  - `Docs`: Para sa mga update sa dokumentasyon.
  - `Build`: Para sa mga pagbabago na may kinalaman sa build system o dependencies, kabilang ang updates sa configuration files, CI workflows, o Dockerfile.
  - `Core`: Para sa mga pagbabago sa pangunahing functionality o features ng proyekto, lalo na sa mga file sa `src/co_op_translator/core` directory.

- **description**: Maikling buod ng pagbabago.
- **PR number**: Ang numero ng pull request na kaugnay ng commit.

**Mga Halimbawa**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Sa kasalukuyan, ang **`Docs`**, **`Core`**, at **`Build`** na prefix ay awtomatikong idinadagdag sa PR titles base sa labels na inilagay sa binagong source code. Hangga't tama ang label, kadalasan ay hindi mo na kailangang baguhin ang PR title. Kailangan mo lang tiyakin na tama ang lahat at tama ang na-generate na prefix.

#### Merge Strategy

Gamit namin ang **Squash and Merge** bilang default na strategy para sa pull requests. Tinitiyak ng strategy na ito na sumusunod ang commit messages sa aming format, kahit hindi pa ito nasunod sa mga indibidwal na commit.

**Mga Dahilan**:

- Malinis at tuwid na project history.
- Consistent na commit messages.
- Mas kaunting ingay mula sa maliliit na commit (hal. "fix typo").

Kapag nagme-merge, tiyaking sumusunod ang final commit message sa commit message format na nakasaad sa itaas.

**Halimbawa ng Squash and Merge**
Kung ang isang PR ay may mga sumusunod na commit:

- `fix typo`
- `update README`
- `adjust formatting`

Dapat silang pagsamahin bilang:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.