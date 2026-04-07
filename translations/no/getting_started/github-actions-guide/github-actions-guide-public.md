# Bruke Co-op Translator GitHub Action (Offentlig Oppsett)

**Målgruppe:** Denne veiledningen er for brukere i de fleste offentlige eller private repositorier hvor standard GitHub Actions-tillatelser er tilstrekkelige. Den bruker den innebygde `GITHUB_TOKEN`.

Automatiser oversettelsen av dokumentasjonen i ditt repository enkelt med Co-op Translator GitHub Action. Denne veiledningen viser deg hvordan du setter opp actionen slik at den automatisk oppretter pull requests med oppdaterte oversettelser hver gang kilde-Markdown-filer eller bilder endres.

> [!IMPORTANT]
>
> **Velg riktig veiledning:**
>
> Denne veiledningen beskriver **det enklere oppsettet med standard `GITHUB_TOKEN`**. Dette er anbefalt metode for de fleste brukere, siden du slipper å håndtere sensitive GitHub App Private Keys.
>

## Forutsetninger

Før du konfigurerer GitHub Action, må du ha nødvendige AI-tjenestelegitimasjoner klare.

**1. Påkrevd: AI Language Model-legitimasjon**
Du trenger legitimasjon for minst én støttet Language Model:

- **Azure OpenAI**: Krever Endpoint, API-nøkkel, Modell-/Deploymentsnavn, API-versjon.
- **OpenAI**: Krever API-nøkkel, (Valgfritt: Org ID, Base URL, Modell-ID).
- Se [Støttede modeller og tjenester](../../../../README.md) for detaljer.

**2. Valgfritt: AI Vision-legitimasjon (for bildeoversettelse)**

- Kun nødvendig hvis du skal oversette tekst i bilder.
- **Azure AI Vision**: Krever Endpoint og Subscription Key.
- Hvis dette ikke oppgis, vil actionen bruke [Kun Markdown-modus](../markdown-only-mode.md) som standard.

## Oppsett og Konfigurasjon

Følg disse stegene for å konfigurere Co-op Translator GitHub Action i ditt repository med standard `GITHUB_TOKEN`.

### Steg 1: Forstå autentisering (bruk av `GITHUB_TOKEN`)

Denne workflowen bruker den innebygde `GITHUB_TOKEN` som tilbys av GitHub Actions. Denne tokenen gir automatisk nødvendige tillatelser til workflowen for å samhandle med repositoryet ditt, basert på innstillingene du konfigurerer i **Steg 3**.

### Steg 2: Konfigurer Repository Secrets

Du trenger kun å legge til **AI-tjenestelegitimasjonen** din som krypterte secrets i repository-innstillingene.

1.  Gå til ditt aktuelle GitHub-repository.
2.  Gå til **Settings** > **Secrets and variables** > **Actions**.
3.  Under **Repository secrets**, klikk **New repository secret** for hver nødvendige AI-tjeneste secret som er listet under.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.no.png" alt="Velg innstilling action"> *(Bildehenvisning: Viser hvor du legger til secrets)*

**Nødvendige AI-tjeneste secrets (Legg til ALLE som gjelder ut fra dine forutsetninger):**

| Secret Name                         | Beskrivelse                               | Kilde til verdi                  |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Nøkkel for Azure AI Service (Computer Vision)  | Din Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint for Azure AI Service (Computer Vision) | Din Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Nøkkel for Azure OpenAI-tjeneste              | Din Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint for Azure OpenAI-tjeneste         | Din Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Ditt Azure OpenAI-modellnavn              | Din Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Ditt Azure OpenAI Deployment-navn         | Din Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | API-versjon for Azure OpenAI              | Din Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API-nøkkel for OpenAI                        | Din OpenAI Platform              |
| `OPENAI_ORG_ID`                     | OpenAI Organisasjons-ID (valgfritt)         | Din OpenAI Platform              |
| `OPENAI_CHAT_MODEL_ID`              | Spesifikk OpenAI-modell-ID (valgfritt)       | Din OpenAI Platform              |
| `OPENAI_BASE_URL`                   | Egendefinert OpenAI API Base URL (valgfritt) | Din OpenAI Platform              |

### Steg 3: Konfigurer Workflow-tillatelser

GitHub Action trenger tillatelser via `GITHUB_TOKEN` for å sjekke ut kode og opprette pull requests.

1.  I repositoryet ditt, gå til **Settings** > **Actions** > **General**.
2.  Bla ned til seksjonen **Workflow permissions**.
3.  Velg **Read and write permissions**. Dette gir `GITHUB_TOKEN` nødvendige `contents: write` og `pull-requests: write` tillatelser for denne workflowen.
4.  Sørg for at boksen for **Allow GitHub Actions to create and approve pull requests** er **huk av**.
5.  Klikk **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.no.png" alt="Tillatelsesinnstilling">

### Steg 4: Opprett workflow-filen

Til slutt, opprett YAML-filen som definerer den automatiserte workflowen med `GITHUB_TOKEN`.

1.  I rotmappen til repositoryet ditt, opprett `.github/workflows/`-mappen hvis den ikke finnes fra før.
2.  Inne i `.github/workflows/`, opprett en fil som heter `co-op-translator.yml`.
3.  Lim inn følgende innhold i `co-op-translator.yml`.

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
4.  **Tilpass workflowen:**
  - **[!IMPORTANT] Mål-språk:** I steget `Run Co-op Translator` må du **GÅ GJENNOM og endre listen over språkkoder** i kommandoen `translate -l "..." -y` slik at den passer til prosjektet ditt. Eksempellisten (`ar de es...`) må byttes ut eller justeres.
  - **Trigger (`on:`):** Nåværende trigger kjører på hver push til `main`. For store repositories, vurder å legge til en `paths:`-filter (se kommentert eksempel i YAML) slik at workflowen kun kjøres når relevante filer (f.eks. kilde-dokumentasjon) endres, for å spare runner-minutter.
  - **PR-detaljer:** Tilpass `commit-message`, `title`, `body`, `branch`-navn og `labels` i steget `Create Pull Request` om nødvendig.

## Kjøre workflowen

> [!WARNING]  
> **Tidsbegrensning for GitHub-hostede runners:**  
> GitHub-hostede runners som `ubuntu-latest` har en **maksimal kjøretid på 6 timer**.  
> For store dokumentasjonsprosjekter, hvis oversettelsesprosessen tar mer enn 6 timer, vil workflowen automatisk bli avbrutt.  
> For å unngå dette, vurder:  
> - Å bruke en **self-hosted runner** (ingen tidsbegrensning)  
> - Å redusere antall målspråk per kjøring

Når `co-op-translator.yml`-filen er merget inn i din main branch (eller den grenen som er spesifisert i `on:`-triggeren), vil workflowen automatisk kjøres hver gang det pushes endringer til den grenen (og matcher `paths`-filteret, hvis konfigurert).

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.