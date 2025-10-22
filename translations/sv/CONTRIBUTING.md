<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:50:58+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sv"
}
-->
# Bidra till Co-op Translator

Det här projektet välkomnar bidrag och förslag. De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att, och faktiskt gör, ge oss rättigheter att använda ditt bidrag. För mer information, besök https://cla.opensource.microsoft.com.

När du skickar in en pull request kommer en CLA-bot automatiskt att avgöra om du behöver godkänna ett CLA och märka PR:n därefter (t.ex. statuskontroll, kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vårt CLA.

## Sätta upp utvecklingsmiljön

För att sätta upp utvecklingsmiljön för det här projektet rekommenderar vi att du använder Poetry för att hantera beroenden. Vi använder `pyproject.toml` för att hantera projektberoenden, så för att installera beroenden bör du använda Poetry.

### Skapa en virtuell miljö

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktivera den virtuella miljön

#### För både pip och Poetry

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

### Installera paketet och nödvändiga paket

#### Med Poetry (från pyproject.toml)

```bash
poetry install
```

### Manuell testning

Innan du skickar in en PR är det viktigt att testa översättningsfunktionen med riktig dokumentation:

1. Skapa en testmapp i rotkatalogen:
    ```bash
    mkdir test_docs
    ```

2. Kopiera några markdown-dokument och bilder du vill översätta till testmappen. Till exempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installera paketet lokalt:
    ```bash
    pip install -e .
    ```

4. Kör Co-op Translator på dina testdokument:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kontrollera de översatta filerna i `test_docs/translations` och `test_docs/translated_images` för att verifiera:
   - Översättningskvaliteten
   - Att metadata-kommentarerna är korrekta
   - Att den ursprungliga markdown-strukturen är bevarad
   - Att länkar och bilder fungerar som de ska

Den här manuella testningen hjälper till att säkerställa att dina ändringar fungerar bra i verkliga scenarier.

### Miljövariabler

1. Skapa en `.env`-fil i rotkatalogen genom att kopiera den medföljande `.env.template`-filen.
1. Fyll i miljövariablerna enligt instruktionerna.

> [!TIP]
>
> ### Ytterligare alternativ för utvecklingsmiljö
>
> Förutom att köra projektet lokalt kan du även använda GitHub Codespaces eller VS Code Dev Containers som alternativa sätt att sätta upp utvecklingsmiljön.
>
> #### GitHub Codespaces
>
> Du kan köra dessa exempel virtuellt med GitHub Codespaces utan extra inställningar eller konfiguration.
>
> Knappen öppnar en webbaserad VS Code-instans i din webbläsare:
>
> 1. Öppna mallen (detta kan ta några minuter):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Köra lokalt med VS Code Dev Containers
>
> ⚠️ Det här alternativet fungerar bara om din Docker Desktop har minst 16 GB RAM tilldelat. Om du har mindre än 16 GB RAM kan du prova [GitHub Codespaces-alternativet](../..) eller [sätta upp det lokalt](../..).
>
> Ett relaterat alternativ är VS Code Dev Containers, som öppnar projektet i din lokala VS Code med [Dev Containers-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Starta Docker Desktop (installera om det inte redan är installerat)
> 2. Öppna projektet:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Kodstil

Vi använder [Black](https://github.com/psf/black) som formatterare för Python-kod för att hålla en enhetlig kodstil i projektet. Black är en kompromisslös formatterare som automatiskt formaterar Python-kod enligt Blacks kodstil.

#### Konfiguration

Black-konfigurationen anges i vår `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installera Black

Du kan installera Black med antingen Poetry (rekommenderas) eller pip:

##### Med Poetry

Black installeras automatiskt när du sätter upp utvecklingsmiljön:
```bash
poetry install
```

##### Med pip

Om du använder pip kan du installera Black direkt:
```bash
pip install black
```

#### Använda Black

##### Med Poetry

1. Formatera alla Python-filer i projektet:
    ```bash
    poetry run black .
    ```

2. Formatera en specifik fil eller mapp:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formatera alla Python-filer i projektet:
    ```bash
    black .
    ```

2. Formatera en specifik fil eller mapp:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi rekommenderar att du ställer in din editor så att koden automatiskt formateras med Black vid varje sparning. De flesta moderna editorer har stöd för detta via tillägg eller plugins.

## Köra Co-op Translator

För att köra Co-op Translator med Poetry i din miljö, följ dessa steg:

1. Navigera till den katalog där du vill utföra översättningstester eller skapa en temporär mapp för teständamål.

2. Kör följande kommando. Byt ut `-l ko` mot den språkkod du vill översätta till. Flaggan `-d` aktiverar debug-läge.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Se till att din Poetry-miljö är aktiverad (poetry shell) innan du kör kommandot.

## Bidra med ett nytt språk

Vi välkomnar bidrag som lägger till stöd för nya språk. Innan du öppnar en PR, följ stegen nedan för att underlätta granskningen.

1. Lägg till språket i font-mappningen
   - Redigera `src/co_op_translator/fonts/font_language_mappings.yml`
   - Lägg till en post med:
     - `code`: ISO-liknande språkkod (t.ex. `vi`)
     - `name`: Namn som visas för användaren
     - `font`: Ett typsnitt som finns i `src/co_op_translator/fonts/` och stöder skriftspråket
     - `rtl`: `true` om höger-till-vänster, annars `false`

2. Inkludera nödvändiga fontfiler (om det behövs)
   - Om ett nytt typsnitt krävs, kontrollera att licensen tillåter öppen källkodsdistribution
   - Lägg till fontfilen i `src/co_op_translator/fonts/`

3. Lokal verifiering
   - Kör översättningar på ett litet exempel (Markdown, bilder och notebooks vid behov)
   - Kontrollera att resultatet visas korrekt, inklusive typsnitt och eventuell RTL-layout

4. Uppdatera dokumentationen
   - Se till att språket finns med i `getting_started/supported-languages.md`
   - Ingen ändring av `README_languages_template.md` behövs; den genereras från listan över stödda språk

5. Skicka in en PR
   - Beskriv vilket språk som lagts till och eventuella font-/licensfrågor
   - Bifoga gärna skärmdumpar av renderade resultat om möjligt

Exempel på YAML-post:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testa det nya språket

Du kan testa det nya språket genom att köra följande kommando:

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

## Underhållare

### Commit-meddelande och sammanslagningsstrategi

För att säkerställa konsekvens och tydlighet i projektets commit-historik följer vi ett specifikt format för commit-meddelanden **för det slutgiltiga commit-meddelandet** när vi använder strategin **Squash and Merge**.

När en pull request (PR) slås ihop kommer de enskilda commitarna att slås samman till en enda commit. Det slutgiltiga commit-meddelandet ska följa formatet nedan för att hålla historiken ren och konsekvent.

#### Format för commit-meddelande (för squash and merge)

Vi använder följande format för commit-meddelanden:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Anger kategorin för commiten. Vi använder följande typer:
  - `Docs`: För uppdateringar av dokumentation.
  - `Build`: För ändringar relaterade till byggsystemet eller beroenden, inklusive uppdateringar av konfigurationsfiler, CI-workflows eller Dockerfile.
  - `Core`: För ändringar av projektets kärnfunktionalitet eller funktioner, särskilt de som rör filer i `src/co_op_translator/core`-katalogen.

- **description**: En kort sammanfattning av ändringen.
- **PR number**: Numret på pull requesten som är kopplad till commiten.

**Exempel**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> För närvarande läggs prefixen **`Docs`**, **`Core`** och **`Build`** automatiskt till PR-titlar baserat på de etiketter som används på ändrad källkod. Så länge rätt etikett används behöver du vanligtvis inte ändra PR-titeln manuellt. Du behöver bara kontrollera att allt är korrekt och att prefixet har genererats som det ska.

#### Sammanslagningsstrategi

Vi använder **Squash and Merge** som standardstrategi för pull requests. Denna strategi säkerställer att commit-meddelanden följer vårt format, även om enskilda commitar inte gör det.

**Anledningar**:

- En ren, linjär projekthistorik.
- Konsekvens i commit-meddelanden.
- Mindre brus från små commitar (t.ex. "fix typo").

När du slår ihop, se till att det slutgiltiga commit-meddelandet följer formatet ovan.

**Exempel på Squash and Merge**
Om en PR innehåller följande commitar:

- `fix typo`
- `update README`
- `adjust formatting`

Ska de slås ihop till:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.