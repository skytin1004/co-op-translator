<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:55:35+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "nl"
}
-->
# Bijdragen aan Co-op Translator

Dit project staat open voor bijdragen en suggesties. Voor de meeste bijdragen moet je akkoord gaan met een Contributor License Agreement (CLA), waarmee je verklaart dat je het recht hebt om je bijdrage te leveren en ons de rechten geeft om deze te gebruiken. Meer informatie vind je op https://cla.opensource.microsoft.com.

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet ondertekenen en het PR van de juiste status voorzien (bijvoorbeeld statuscontrole, opmerking). Volg gewoon de instructies van de bot. Je hoeft dit maar één keer te doen voor alle repositories die onze CLA gebruiken.

## Ontwikkelomgeving instellen

Voor het instellen van de ontwikkelomgeving raden we aan om Poetry te gebruiken voor het beheren van afhankelijkheden. We gebruiken `pyproject.toml` om de afhankelijkheden van het project te beheren, dus je dient Poetry te gebruiken om deze te installeren.

### Maak een virtuele omgeving aan

#### Met pip

```bash
python -m venv .venv
```

#### Met Poetry

```bash
poetry init
```

### Activeer de virtuele omgeving

#### Voor zowel pip als Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Met Poetry

```bash
poetry shell
```

### Installeren van het pakket en benodigde pakketten

#### Met Poetry (uit pyproject.toml)

```bash
poetry install
```

### Handmatig testen

Voordat je een PR indient, is het belangrijk om de vertaalfunctionaliteit te testen met echte documentatie:

1. Maak een testmap aan in de hoofdmap:
    ```bash
    mkdir test_docs
    ```

2. Kopieer wat markdown-documentatie en afbeeldingen die je wilt vertalen naar de testmap. Bijvoorbeeld:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installeer het pakket lokaal:
    ```bash
    pip install -e .
    ```

4. Voer Co-op Translator uit op je testdocumenten:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Controleer de vertaalde bestanden in `test_docs/translations` en `test_docs/translated_images` om te verifiëren:
   - De kwaliteit van de vertaling
   - Of de metadata-opmerkingen kloppen
   - Of de originele markdownstructuur behouden is
   - Of links en afbeeldingen goed werken

Deze handmatige test helpt om te zorgen dat je wijzigingen goed werken in praktijksituaties.

### Omgevingsvariabelen

1. Maak een `.env`-bestand aan in de hoofdmap door het meegeleverde `.env.template`-bestand te kopiëren.
1. Vul de omgevingsvariabelen in zoals aangegeven.

> [!TIP]
>
> ### Extra opties voor de ontwikkelomgeving
>
> Naast lokaal werken kun je ook GitHub Codespaces of VS Code Dev Containers gebruiken als alternatieve ontwikkelomgeving.
>
> #### GitHub Codespaces
>
> Je kunt deze voorbeelden virtueel uitvoeren via GitHub Codespaces, zonder extra instellingen of installatie.
>
> De knop opent een webgebaseerde VS Code in je browser:
>
> 1. Open de template (dit kan enkele minuten duren):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Lokaal uitvoeren met VS Code Dev Containers
>
> ⚠️ Deze optie werkt alleen als je Docker Desktop minimaal 16 GB RAM heeft. Heb je minder dan 16 GB RAM, probeer dan de [GitHub Codespaces-optie](../..) of [stel het lokaal in](../..).
>
> Een andere optie is VS Code Dev Containers, waarmee je het project opent in je lokale VS Code via de [Dev Containers-extensie](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installeer indien nodig)
> 2. Open het project:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### Code-stijl

We gebruiken [Black](https://github.com/psf/black) als formatter voor onze Python-code om een consistente stijl in het project te behouden. Black is een compromisloze formatter die Python-code automatisch herschrijft volgens de Black-stijl.

#### Configuratie

De Black-configuratie staat in onze `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black installeren

Je kunt Black installeren met Poetry (aanbevolen) of pip:

##### Met Poetry

Black wordt automatisch geïnstalleerd bij het instellen van de ontwikkelomgeving:
```bash
poetry install
```

##### Met pip

Als je pip gebruikt, kun je Black direct installeren:
```bash
pip install black
```

#### Black gebruiken

##### Met Poetry

1. Formatteer alle Python-bestanden in het project:
    ```bash
    poetry run black .
    ```

2. Formatteer een specifiek bestand of map:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Met pip

1. Formatteer alle Python-bestanden in het project:
    ```bash
    black .
    ```

2. Formatteer een specifiek bestand of map:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> We raden aan om je editor zo in te stellen dat code automatisch met Black wordt geformatteerd bij het opslaan. De meeste moderne editors ondersteunen dit via extensies of plugins.

## Co-op Translator uitvoeren

Om Co-op Translator met Poetry in je omgeving te draaien, volg je deze stappen:

1. Navigeer naar de map waar je vertaaltests wilt uitvoeren of maak een tijdelijke map aan voor testdoeleinden.

2. Voer het volgende commando uit. Vervang `-l ko` door de taalcode waarin je wilt vertalen. De `-d`-vlag zet de debugmodus aan.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Zorg dat je Poetry-omgeving is geactiveerd (poetry shell) voordat je het commando uitvoert.

## Een nieuwe taal toevoegen

We verwelkomen bijdragen die ondersteuning voor nieuwe talen toevoegen. Voltooi de onderstaande stappen voordat je een PR opent, zodat de review soepel verloopt.

1. Voeg de taal toe aan de font-mapping
   - Bewerk `src/co_op_translator/fonts/font_language_mappings.yml`
   - Voeg een item toe met:
     - `code`: ISO-achtige taalcode (bijv. `vi`)
     - `name`: Mensvriendelijke naam
     - `font`: Een font uit `src/co_op_translator/fonts/` die het schrift ondersteunt
     - `rtl`: `true` als het rechts-naar-links is, anders `false`

2. Voeg benodigde fontbestanden toe (indien nodig)
   - Als een nieuw font nodig is, controleer dan of de licentie geschikt is voor open source distributie
   - Voeg het fontbestand toe aan `src/co_op_translator/fonts/`

3. Lokale verificatie
   - Voer vertalingen uit voor een kleine sample (Markdown, afbeeldingen en notebooks indien van toepassing)
   - Controleer of de output correct wordt weergegeven, inclusief fonts en eventuele RTL-layout

4. Documentatie bijwerken
   - Zorg dat de taal vermeld staat in `getting_started/supported-languages.md`
   - Je hoeft `README_languages_template.md` niet aan te passen; deze wordt gegenereerd uit de ondersteunde lijst

5. Open een PR
   - Beschrijf de toegevoegde taal en eventuele font/licentie-overwegingen
   - Voeg indien mogelijk screenshots toe van de weergegeven output

Voorbeeld YAML-item:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Test de nieuwe taal

Je kunt de nieuwe taal testen met het volgende commando:

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

## Beheerders

### Commitbericht en merge-strategie

Om consistentie en duidelijkheid in de commitgeschiedenis van ons project te waarborgen, hanteren we een specifiek format voor commitberichten **voor het definitieve commitbericht** bij gebruik van de **Squash and Merge**-strategie.

Wanneer een pull request (PR) wordt samengevoegd, worden de individuele commits samengevoegd tot één commit. Het definitieve commitbericht moet het onderstaande format volgen om een nette en consistente geschiedenis te behouden.

#### Format commitbericht (voor squash and merge)

We gebruiken het volgende format voor commitberichten:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Geeft de categorie van de commit aan. We gebruiken de volgende types:
  - `Docs`: Voor updates aan de documentatie.
  - `Build`: Voor wijzigingen aan het build-systeem of afhankelijkheden, inclusief updates aan configuratiebestanden, CI-workflows of de Dockerfile.
  - `Core`: Voor aanpassingen aan de kernfunctionaliteit of features van het project, vooral in bestanden in de map `src/co_op_translator/core`.

- **description**: Een korte samenvatting van de wijziging.
- **PR number**: Het nummer van de pull request die bij de commit hoort.

**Voorbeelden**:

- `Docs: Installatie-instructies verduidelijkt (#50)`
- `Core: Verbeterde verwerking van afbeeldingvertaling (#60)`

> [!NOTE]
> Momenteel worden de **`Docs`**, **`Core`** en **`Build`**-prefixen automatisch toegevoegd aan PR-titels op basis van de labels die zijn toegepast op de gewijzigde broncode. Zolang het juiste label is toegepast, hoef je meestal de PR-titel niet handmatig aan te passen. Je hoeft alleen te controleren of alles klopt en de prefix correct is gegenereerd.

#### Merge-strategie

We gebruiken **Squash and Merge** als standaardstrategie voor pull requests. Deze strategie zorgt ervoor dat commitberichten ons format volgen, zelfs als individuele commits dat niet doen.

**Redenen**:

- Een schone, lineaire projectgeschiedenis.
- Consistentie in commitberichten.
- Minder ruis door kleine commits (zoals "fix typo").

Zorg bij het samenvoegen dat het definitieve commitbericht het hierboven beschreven format volgt.

**Voorbeeld van Squash and Merge**
Als een PR de volgende commits bevat:

- `fix typo`
- `update README`
- `adjust formatting`

Moeten ze worden samengevoegd tot:
`Docs: Documentatie verduidelijkt en opmaak verbeterd (#65)`

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.