<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:53:10+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "no"
}
-->
# Bidra til Co-op Translator

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rett til, og faktisk gir oss, rettighetene til å bruke ditt bidrag. For mer informasjon, se https://cla.opensource.microsoft.com.

Når du sender inn en pull request, vil en CLA-bot automatisk sjekke om du må godta en CLA og merke PR-en deretter (f.eks. status-sjekk, kommentar). Følg bare instruksjonene fra boten. Du trenger kun å gjøre dette én gang for alle repos som bruker vår CLA.

## Sette opp utviklingsmiljø

For å sette opp utviklingsmiljøet for dette prosjektet anbefaler vi å bruke Poetry for å håndtere avhengigheter. Vi bruker `pyproject.toml` til å administrere prosjektavhengigheter, så du bør bruke Poetry for å installere dem.

### Opprett et virtuelt miljø

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljøet

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Med Poetry

```bash
poetry shell
```

### Installere pakken og nødvendige avhengigheter

#### Med Poetry (fra pyproject.toml)

```bash
poetry install
```

### Manuell testing

Før du sender inn en PR, er det viktig å teste oversettelsesfunksjonen med ekte dokumentasjon:

1. Lag en testmappe i rotmappen:
    ```bash
    mkdir test_docs
    ```

2. Kopier noen markdown-dokumenter og bilder du vil oversette inn i testmappen. For eksempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installer pakken lokalt:
    ```bash
    pip install -e .
    ```

4. Kjør Co-op Translator på testdokumentene dine:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Sjekk de oversatte filene i `test_docs/translations` og `test_docs/translated_images` for å verifisere:
   - Kvaliteten på oversettelsen
   - At metadata-kommentarene er riktige
   - At den originale markdown-strukturen er bevart
   - At lenker og bilder fungerer som de skal

Denne manuelle testingen hjelper deg å sikre at endringene dine fungerer godt i praksis.

### Miljøvariabler

1. Lag en `.env`-fil i rotmappen ved å kopiere den medfølgende `.env.template`-filen.
1. Fyll inn miljøvariablene som beskrevet.

> [!TIP]
>
> ### Flere alternativer for utviklingsmiljø
>
> I tillegg til å kjøre prosjektet lokalt, kan du også bruke GitHub Codespaces eller VS Code Dev Containers som alternative utviklingsmiljøer.
>
> #### GitHub Codespaces
>
> Du kan kjøre disse eksemplene virtuelt med GitHub Codespaces uten ekstra oppsett.
>
> Knappen åpner en nettbasert VS Code-instans i nettleseren din:
>
> 1. Åpne malen (dette kan ta noen minutter):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Kjøre lokalt med VS Code Dev Containers
>
> ⚠️ Dette alternativet fungerer kun hvis Docker Desktop har minst 16 GB RAM tilgjengelig. Har du mindre enn 16 GB RAM, kan du prøve [GitHub Codespaces-alternativet](../..) eller [sette opp lokalt](../..).
>
> Et annet alternativ er VS Code Dev Containers, som åpner prosjektet i din lokale VS Code med [Dev Containers-utvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det hvis du ikke har det)
> 2. Åpne prosjektet:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### Kodestil

Vi bruker [Black](https://github.com/psf/black) som formatter for Python-kode for å holde enhetlig stil i prosjektet. Black er kompromissløs og formaterer automatisk Python-koden til sin egen stil.

#### Konfigurasjon

Black-konfigurasjonen er spesifisert i vår `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installere Black

Du kan installere Black med enten Poetry (anbefalt) eller pip:

##### Med Poetry

Black installeres automatisk når du setter opp utviklingsmiljøet:
```bash
poetry install
```

##### Med pip

Hvis du bruker pip, kan du installere Black direkte:
```bash
pip install black
```

#### Bruke Black

##### Med Poetry

1. Formater alle Python-filer i prosjektet:
    ```bash
    poetry run black .
    ```

2. Formater en spesifikk fil eller mappe:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formater alle Python-filer i prosjektet:
    ```bash
    black .
    ```

2. Formater en spesifikk fil eller mappe:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi anbefaler å sette opp editoren din til å automatisk formatere kode med Black ved lagring. De fleste moderne editorer støtter dette via utvidelser eller plugins.

## Kjøre Co-op Translator

For å kjøre Co-op Translator med Poetry i ditt miljø, følg disse stegene:

1. Gå til mappen der du vil teste oversettelser, eller lag en midlertidig mappe for testing.

2. Kjør følgende kommando. Bytt ut `-l ko` med språkkoden du vil oversette til. Flagget `-d` aktiverer debug-modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for at Poetry-miljøet ditt er aktivert (poetry shell) før du kjører kommandoen.

## Bidra med et nytt språk

Vi ønsker bidrag som legger til støtte for nye språk. Før du åpner en PR, følg stegene under for å gjøre gjennomgangen enklere.

1. Legg til språket i font-mappingen
   - Rediger `src/co_op_translator/fonts/font_language_mappings.yml`
   - Legg til en oppføring med:
     - `code`: ISO-lignende språkkode (f.eks. `vi`)
     - `name`: Brukervennlig visningsnavn
     - `font`: En font som ligger i `src/co_op_translator/fonts/` og støtter skriftsystemet
     - `rtl`: `true` hvis høyre-til-venstre, ellers `false`

2. Legg til nødvendige fontfiler (om nødvendig)
   - Hvis en ny font trengs, sjekk at lisensen tillater åpen kildekode-distribusjon
   - Legg fontfilen til `src/co_op_translator/fonts/`

3. Lokal verifisering
   - Kjør oversettelser for et lite eksempel (Markdown, bilder og notatbøker etter behov)
   - Sjekk at utdata vises riktig, inkludert fonter og eventuell RTL-layout

4. Oppdater dokumentasjonen
   - Sørg for at språket vises i `getting_started/supported-languages.md`
   - Ingen endringer i `README_languages_template.md` er nødvendig; den genereres fra listen over støttede språk

5. Åpne en PR
   - Beskriv språket du har lagt til og eventuelle font-/lisenshensyn
   - Legg ved skjermbilder av utdata om mulig

Eksempel på YAML-oppføring:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Test det nye språket

Du kan teste det nye språket ved å kjøre følgende kommando:

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

## Vedlikeholdere

### Commit-melding og flettestrategi

For å sikre konsistens og tydelighet i prosjektets commit-historikk, følger vi et bestemt format **for den endelige commit-meldingen** når vi bruker **Squash and Merge**-strategien.

Når en pull request (PR) flettes, blir de individuelle commitene slått sammen til én commit. Den endelige commit-meldingen skal følge formatet under for å holde historikken ryddig og konsistent.

#### Commit-meldingsformat (for squash and merge)

Vi bruker følgende format for commit-meldinger:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Angir kategorien for commiten. Vi bruker følgende typer:
  - `Docs`: For oppdateringer i dokumentasjonen.
  - `Build`: For endringer relatert til byggesystemet eller avhengigheter, inkludert oppdateringer av konfigurasjonsfiler, CI-workflows eller Dockerfile.
  - `Core`: For endringer i prosjektets kjernefunksjonalitet eller funksjoner, spesielt de som involverer filer i `src/co_op_translator/core`-mappen.

- **description**: En kort oppsummering av endringen.
- **PR number**: Nummeret på pull requesten som commiten gjelder.

**Eksempler**:

- `Docs: Oppdater installasjonsinstruksjoner for klarhet (#50)`
- `Core: Forbedre håndtering av bildeoversettelse (#60)`

> [!NOTE]
> For øyeblikket blir **`Docs`**, **`Core`** og **`Build`**-prefiksene automatisk lagt til PR-titler basert på etikettene som brukes på endret kildekode. Så lenge riktig etikett er brukt, trenger du vanligvis ikke å oppdatere PR-tittelen manuelt. Du må bare sjekke at alt er riktig og at prefikset er generert som det skal.

#### Flettestrategi

Vi bruker **Squash and Merge** som standard strategi for pull requests. Denne strategien sikrer at commit-meldinger følger vårt format, selv om de individuelle commitene ikke gjør det.

**Grunner**:

- En ryddig, lineær prosjekt-historikk.
- Konsistens i commit-meldinger.
- Mindre støy fra små commits (f.eks. "fikset skrivefeil").

Når du fletter, sørg for at den endelige commit-meldingen følger formatet beskrevet over.

**Eksempel på Squash and Merge**
Hvis en PR inneholder følgende commits:

- `fikset skrivefeil`
- `oppdatert README`
- `justert formatering`

Skal de slås sammen til:
`Docs: Forbedre dokumentasjonsklarhet og formatering (#65)`

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.