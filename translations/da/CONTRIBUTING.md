<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:52:00+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "da"
}
-->
# Bidrag til Co-op Translator

Dette projekt byder bidrag og forslag velkommen. De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), hvor du erklærer, at du har ret til, og faktisk giver os, rettighederne til at bruge dit bidrag. For flere detaljer, besøg https://cla.opensource.microsoft.com.

Når du indsender et pull request, vil en CLA-bot automatisk afgøre, om du skal udfylde en CLA og markere PR'en derefter (f.eks. statuscheck, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repos, der bruger vores CLA.

## Opsætning af udviklingsmiljø

For at sætte udviklingsmiljøet op til dette projekt anbefaler vi at bruge Poetry til at håndtere afhængigheder. Vi bruger `pyproject.toml` til at styre projektets afhængigheder, så du bør bruge Poetry til at installere dem.

### Opret et virtuelt miljø

#### Brug af pip

```bash
python -m venv .venv
```

#### Brug af Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljø

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Brug af Poetry

```bash
poetry shell
```

### Installation af pakken og nødvendige pakker

#### Brug af Poetry (fra pyproject.toml)

```bash
poetry install
```

### Manuel test

Før du indsender et PR, er det vigtigt at teste oversættelsesfunktionen med rigtig dokumentation:

1. Opret en testmappe i roden af projektet:
    ```bash
    mkdir test_docs
    ```

2. Kopiér noget markdown-dokumentation og billeder, du vil oversætte, ind i testmappen. For eksempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installer pakken lokalt:
    ```bash
    pip install -e .
    ```

4. Kør Co-op Translator på dine testdokumenter:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Tjek de oversatte filer i `test_docs/translations` og `test_docs/translated_images` for at sikre:
   - At oversættelseskvaliteten er god
   - At metadata-kommentarerne er korrekte
   - At den oprindelige markdown-struktur er bevaret
   - At links og billeder fungerer korrekt

Denne manuelle test hjælper med at sikre, at dine ændringer fungerer godt i praksis.

### Miljøvariabler

1. Opret en `.env`-fil i roden af projektet ved at kopiere den medfølgende `.env.template`-fil.
1. Udfyld miljøvariablerne som angivet.

> [!TIP]
>
> ### Yderligere muligheder for udviklingsmiljø
>
> Ud over at køre projektet lokalt kan du også bruge GitHub Codespaces eller VS Code Dev Containers som alternative udviklingsmiljøer.
>
> #### GitHub Codespaces
>
> Du kan køre disse eksempler virtuelt ved at bruge GitHub Codespaces, uden yderligere opsætning.
>
> Knappen åbner en webbaseret VS Code-instans i din browser:
>
> 1. Åbn skabelonen (dette kan tage flere minutter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kør lokalt med VS Code Dev Containers
>
> ⚠️ Denne mulighed virker kun, hvis din Docker Desktop har mindst 16 GB RAM til rådighed. Hvis du har mindre end 16 GB RAM, kan du prøve [GitHub Codespaces-muligheden](../..) eller [sætte det op lokalt](../..).
>
> En relateret mulighed er VS Code Dev Containers, som åbner projektet i din lokale VS Code ved hjælp af [Dev Containers-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det, hvis det ikke allerede er installeret)
> 2. Åbn projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodestil

Vi bruger [Black](https://github.com/psf/black) som vores formatteringsværktøj til Python-kode for at sikre en ensartet kodestil i hele projektet. Black er en kompromisløs formatter, der automatisk omformaterer Python-kode, så den følger Blacks kodestil.

#### Konfiguration

Black-konfigurationen er angivet i vores `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installation af Black

Du kan installere Black med enten Poetry (anbefalet) eller pip:

##### Brug af Poetry

Black installeres automatisk, når du sætter udviklingsmiljøet op:
```bash
poetry install
```

##### Brug af pip

Hvis du bruger pip, kan du installere Black direkte:
```bash
pip install black
```

#### Brug af Black

##### Med Poetry

1. Formater alle Python-filer i projektet:
    ```bash
    poetry run black .
    ```

2. Formater en specifik fil eller mappe:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formater alle Python-filer i projektet:
    ```bash
    black .
    ```

2. Formater en specifik fil eller mappe:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi anbefaler at sætte din editor op til automatisk at formatere kode med Black, når du gemmer. De fleste moderne editorer understøtter dette via udvidelser eller plugins.

## Kørsel af Co-op Translator

For at køre Co-op Translator med Poetry i dit miljø, følg disse trin:

1. Gå til den mappe, hvor du vil udføre oversættelsestests, eller opret en midlertidig mappe til testformål.

2. Kør følgende kommando. Erstat `-l ko` med den sprogkode, du ønsker at oversætte til. Flaget `-d` angiver debug-tilstand.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for, at dit Poetry-miljø er aktiveret (poetry shell), før du kører kommandoen.

## Bidrag med et nyt sprog

Vi byder bidrag, der tilføjer understøttelse af nye sprog, velkommen. Før du åbner et PR, skal du gennemføre nedenstående trin for at sikre en smidig gennemgang.

1. Tilføj sproget til font-mappingen
   - Redigér `src/co_op_translator/fonts/font_language_mappings.yml`
   - Tilføj en post med:
     - `code`: ISO-lignende sprogkode (f.eks. `vi`)
     - `name`: Brugervenligt navn
     - `font`: En font, der findes i `src/co_op_translator/fonts/`, og som understøtter skriftsystemet
     - `rtl`: `true` hvis højre-til-venstre, ellers `false`

2. Inkludér nødvendige fontfiler (hvis nødvendigt)
   - Hvis en ny font er nødvendig, skal du sikre, at licensen er kompatibel med open source-distribution
   - Tilføj fontfilen til `src/co_op_translator/fonts/`

3. Lokal verifikation
   - Kør oversættelser på et lille eksempel (Markdown, billeder og notebooks efter behov)
   - Tjek at output vises korrekt, inkl. fonte og evt. RTL-layout

4. Opdatér dokumentation
   - Sørg for, at sproget fremgår af `getting_started/supported-languages.md`
   - Ingen ændringer i `README_languages_template.md` er nødvendige; den genereres ud fra listen over understøttede sprog

5. Opret et PR
   - Beskriv det tilføjede sprog og eventuelle font-/licensovervejelser
   - Vedhæft skærmbilleder af det viste output, hvis muligt

Eksempel på YAML-post:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Test det nye sprog

Du kan teste det nye sprog ved at køre følgende kommando:

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

## Vedligeholdere

### Commit-besked og fusionsstrategi

For at sikre konsistens og klarhed i projektets commit-historik følger vi et specifikt format for commit-beskeder **til den endelige commit-besked**, når vi bruger **Squash and Merge**-strategien.

Når et pull request (PR) flettes, bliver de enkelte commits samlet til én. Den endelige commit-besked skal følge formatet nedenfor for at bevare en ren og ensartet historik.

#### Format for commit-besked (ved squash and merge)

Vi bruger følgende format til commit-beskeder:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Angiver kategorien for committet. Vi bruger følgende typer:
  - `Docs`: Til opdateringer af dokumentation.
  - `Build`: Til ændringer relateret til build-systemet eller afhængigheder, inkl. opdateringer af konfigurationsfiler, CI-workflows eller Dockerfile.
  - `Core`: Til ændringer i projektets kernefunktionalitet eller funktioner, især dem der involverer filer i `src/co_op_translator/core`-mappen.

- **description**: En kortfattet beskrivelse af ændringen.
- **PR number**: Nummeret på det pull request, der er knyttet til committet.

**Eksempler**:

- `Docs: Opdater installationsvejledning for klarhed (#50)`
- `Core: Forbedret håndtering af billedoversættelse (#60)`

> [!NOTE]
> Lige nu tilføjes **`Docs`**, **`Core`** og **`Build`**-præfikserne automatisk til PR-titler baseret på de labels, der er sat på den ændrede kildekode. Så længe det korrekte label er sat, behøver du normalt ikke manuelt at opdatere PR-titlen. Du skal blot sikre, at alt er korrekt, og at præfikset er genereret rigtigt.

#### Fusionsstrategi

Vi bruger **Squash and Merge** som standardstrategi for pull requests. Denne strategi sikrer, at commit-beskeder følger vores format, selvom de enkelte commits ikke gør.

**Årsager**:

- En ren, lineær projekthistorik.
- Ensartede commit-beskeder.
- Mindre støj fra små commits (f.eks. "fix typo").

Når du fletter, skal du sikre, at den endelige commit-besked følger formatet beskrevet ovenfor.

**Eksempel på Squash and Merge**
Hvis et PR indeholder følgende commits:

- `fix typo`
- `update README`
- `adjust formatting`

Skal de samles til:
`Docs: Forbedret dokumentationsklarhed og formatering (#65)`

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.