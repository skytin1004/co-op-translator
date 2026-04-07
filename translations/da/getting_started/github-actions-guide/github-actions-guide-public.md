# Brug af Co-op Translator GitHub Action (Offentlig Opsætning)

**Målgruppe:** Denne vejledning er til brugere i de fleste offentlige eller private repositories, hvor standard GitHub Actions-tilladelser er tilstrækkelige. Den bruger den indbyggede `GITHUB_TOKEN`.

Automatiser oversættelsen af dit repositories dokumentation nemt med Co-op Translator GitHub Action. Denne vejledning guider dig igennem opsætningen af actionen, så der automatisk oprettes pull requests med opdaterede oversættelser, hver gang dine kilde-Markdown-filer eller billeder ændres.

> [!IMPORTANT]
>
> **Vælg den rigtige vejledning:**
>
> Denne vejledning beskriver **den enklere opsætning med standard `GITHUB_TOKEN`**. Dette er den anbefalede metode for de fleste brugere, da du ikke skal håndtere følsomme GitHub App Private Keys.
>

## Forudsætninger

Før du konfigurerer GitHub Action, skal du have de nødvendige AI-tjenesteoplysninger klar.

**1. Krævet: AI Language Model-oplysninger**
Du skal have oplysninger til mindst én understøttet Language Model:

- **Azure OpenAI**: Kræver Endpoint, API Key, Model/Deployment-navne, API Version.
- **OpenAI**: Kræver API Key, (Valgfrit: Org ID, Base URL, Model ID).
- Se [Understøttede modeller og tjenester](../../../../README.md) for detaljer.

**2. Valgfrit: AI Vision-oplysninger (til billedoversættelse)**

- Kun nødvendigt, hvis du skal oversætte tekst i billeder.
- **Azure AI Vision**: Kræver Endpoint og Subscription Key.
- Hvis ikke angivet, kører actionen i [Markdown-only mode](../markdown-only-mode.md).

## Opsætning og Konfiguration

Følg disse trin for at konfigurere Co-op Translator GitHub Action i dit repository med standard `GITHUB_TOKEN`.

### Trin 1: Forstå godkendelse (Brug af `GITHUB_TOKEN`)

Denne workflow bruger den indbyggede `GITHUB_TOKEN`, som GitHub Actions stiller til rådighed. Tokenet giver automatisk workflowen de nødvendige tilladelser til at interagere med dit repository, baseret på indstillingerne i **Trin 3**.

### Trin 2: Konfigurer Repository Secrets

Du skal kun tilføje dine **AI-tjenesteoplysninger** som krypterede secrets i repository-indstillingerne.

1.  Gå til dit ønskede GitHub repository.
2.  Gå til **Settings** > **Secrets and variables** > **Actions**.
3.  Under **Repository secrets**, klik på **New repository secret** for hver nødvendig AI-tjeneste secret, der er listet nedenfor.

    ![Vælg indstilling action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.da.png) *(Billedreference: Viser hvor du tilføjer secrets)*

**Nødvendige AI-tjeneste secrets (Tilføj ALLE der er relevante ud fra dine forudsætninger):**

| Secret Name                         | Beskrivelse                               | Værdi-kilde                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Nøgle til Azure AI Service (Computer Vision)  | Din Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint til Azure AI Service (Computer Vision) | Din Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Nøgle til Azure OpenAI service              | Din Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint til Azure OpenAI service         | Din Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Dit Azure OpenAI Model Name               | Din Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Dit Azure OpenAI Deployment Name          | Din Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | API Version til Azure OpenAI              | Din Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key til OpenAI                        | Din OpenAI Platform                |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Valgfrit)         | Din OpenAI Platform                |
| `OPENAI_CHAT_MODEL_ID`              | Specifikt OpenAI model ID (Valgfrit)      | Din OpenAI Platform                |
| `OPENAI_BASE_URL`                   | Tilpasset OpenAI API Base URL (Valgfrit)  | Din OpenAI Platform                |

### Trin 3: Konfigurer Workflow-tilladelser

GitHub Action skal have tilladelser via `GITHUB_TOKEN` til at tjekke kode ud og oprette pull requests.

1.  I dit repository, gå til **Settings** > **Actions** > **General**.
2.  Rul ned til sektionen **Workflow permissions**.
3.  Vælg **Read and write permissions**. Dette giver `GITHUB_TOKEN` de nødvendige `contents: write` og `pull-requests: write` tilladelser til denne workflow.
4.  Sørg for at afkrydsningsfeltet **Allow GitHub Actions to create and approve pull requests** er **markeret**.
5.  Klik på **Save**.

![Tilladelsesindstilling](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.da.png)

### Trin 4: Opret workflow-filen

Til sidst skal du oprette YAML-filen, der definerer den automatiserede workflow med `GITHUB_TOKEN`.

1.  I roden af dit repository, opret mappen `.github/workflows/` hvis den ikke allerede findes.
2.  Inde i `.github/workflows/`, opret en fil med navnet `co-op-translator.yml`.
3.  Indsæt følgende indhold i `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Tilpas workflowen:**
  - **[!IMPORTANT] Mål-sprog:** I `Run Co-op Translator`-trinnet skal du **gennemgå og tilpasse listen af sprogkoder** i kommandoen `translate -l "..." -y`, så den passer til dit projekt. Eksempellisten (`ar de es...`) skal udskiftes eller justeres.
  - **Trigger (`on:`):** Den nuværende trigger kører ved hvert push til `main`. For store repositories kan du overveje at tilføje et `paths:` filter (se kommenteret eksempel i YAML) for kun at køre workflowen, når relevante filer (f.eks. kilde-dokumentation) ændres, så du sparer runner-minutter.
  - **PR-detaljer:** Tilpas `commit-message`, `title`, `body`, `branch` navn og `labels` i `Create Pull Request`-trinnet efter behov.

## Kørsel af workflowen

> [!WARNING]  
> **Tidsbegrænsning for GitHub-hostede runners:**  
> GitHub-hostede runners som `ubuntu-latest` har en **maksimal køretid på 6 timer**.  
> For store dokumentationsrepositories, hvis oversættelsesprocessen overstiger 6 timer, vil workflowen automatisk blive afbrudt.  
> For at undgå dette kan du:  
> - Bruge en **self-hosted runner** (ingen tidsbegrænsning)  
> - Reducere antallet af mål-sprog pr. kørsel

Når `co-op-translator.yml`-filen er flettet ind i din main branch (eller den branch, der er angivet i `on:` triggeren), vil workflowen automatisk køre, hver gang der pushes ændringer til den branch (og matcher `paths` filteret, hvis det er konfigureret).

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.