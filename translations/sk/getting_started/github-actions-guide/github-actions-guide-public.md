# Použitie Co-op Translator GitHub Action (Verejné nastavenie)

**Cieľová skupina:** Táto príručka je určená pre používateľov vo väčšine verejných alebo súkromných repozitárov, kde sú štandardné oprávnenia GitHub Actions postačujúce. Využíva zabudovaný `GITHUB_TOKEN`.

Automatizujte preklad dokumentácie vášho repozitára jednoducho pomocou Co-op Translator GitHub Action. Táto príručka vás prevedie nastavením akcie tak, aby automaticky vytvárala pull requesty s aktualizovanými prekladmi vždy, keď sa zmenia vaše zdrojové Markdown súbory alebo obrázky.

> [!IMPORTANT]
>
> **Výber správnej príručky:**
>
> Táto príručka popisuje **jednoduchšie nastavenie pomocou štandardného `GITHUB_TOKEN`**. Toto je odporúčaný spôsob pre väčšinu používateľov, pretože nevyžaduje spravovanie citlivých súkromných kľúčov GitHub App.
>

## Predpoklady

Pred konfiguráciou GitHub Action si pripravte potrebné prihlasovacie údaje k AI službe.

**1. Povinné: Prihlasovacie údaje k AI jazykovému modelu**
Potrebujete údaje aspoň k jednému podporovanému jazykovému modelu:

- **Azure OpenAI**: Vyžaduje Endpoint, API kľúč, názvy modelov/deploymentov, verziu API.
- **OpenAI**: Vyžaduje API kľúč, (voliteľne: Org ID, Base URL, Model ID).
- Podrobnosti nájdete v [Podporované modely a služby](../../../../README.md).

**2. Voliteľné: Prihlasovacie údaje k AI Vision (pre preklad textu v obrázkoch)**

- Potrebné len v prípade, že chcete prekladať text v obrázkoch.
- **Azure AI Vision**: Vyžaduje Endpoint a Subscription Key.
- Ak nie sú zadané, akcia sa prepne do [režimu len pre Markdown](../markdown-only-mode.md).

## Nastavenie a konfigurácia

Postupujte podľa týchto krokov na nastavenie Co-op Translator GitHub Action vo vašom repozitári pomocou štandardného `GITHUB_TOKEN`.

### Krok 1: Pochopenie autentifikácie (Použitie `GITHUB_TOKEN`)

Tento workflow používa zabudovaný `GITHUB_TOKEN`, ktorý poskytuje GitHub Actions. Tento token automaticky udeľuje workflowu oprávnenia na interakciu s vaším repozitárom podľa nastavení z **Kroku 3**.

### Krok 2: Nastavenie tajomstiev repozitára

Stačí pridať **prihlasovacie údaje k AI službe** ako šifrované tajomstvá v nastaveniach vášho repozitára.

1.  Prejdite do cieľového GitHub repozitára.
2.  Choďte na **Settings** > **Secrets and variables** > **Actions**.
3.  V sekcii **Repository secrets** kliknite na **New repository secret** pre každé potrebné tajomstvo AI služby uvedené nižšie.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.sk.png) *(Referenčný obrázok: Ukazuje, kde pridať tajomstvá)*

**Povinné tajomstvá AI služby (Pridajte VŠETKY, ktoré sa vás týkajú podľa predpokladov):**

| Názov tajomstva                      | Popis                                      | Zdroj hodnoty                  |
| :----------------------------------- | :------------------------------------------ | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`           | Kľúč pre Azure AI Service (Computer Vision) | Vaša Azure AI Foundry          |
| `AZURE_AI_SERVICE_ENDPOINT`          | Endpoint pre Azure AI Service (Computer Vision) | Vaša Azure AI Foundry      |
| `AZURE_OPENAI_API_KEY`               | Kľúč pre Azure OpenAI službu                | Vaša Azure AI Foundry          |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint pre Azure OpenAI službu            | Vaša Azure AI Foundry          |
| `AZURE_OPENAI_MODEL_NAME`            | Názov vášho Azure OpenAI modelu             | Vaša Azure AI Foundry          |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Názov vášho Azure OpenAI deploymentu        | Vaša Azure AI Foundry          |
| `AZURE_OPENAI_API_VERSION`           | Verzia API pre Azure OpenAI                 | Vaša Azure AI Foundry          |
| `OPENAI_API_KEY`                     | API kľúč pre OpenAI                         | Vaša OpenAI Platform           |
| `OPENAI_ORG_ID`                      | OpenAI Organization ID (voliteľné)          | Vaša OpenAI Platform           |
| `OPENAI_CHAT_MODEL_ID`               | Konkrétne OpenAI model ID (voliteľné)       | Vaša OpenAI Platform           |
| `OPENAI_BASE_URL`                    | Vlastné OpenAI API Base URL (voliteľné)     | Vaša OpenAI Platform           |

### Krok 3: Nastavenie oprávnení workflowu

GitHub Action potrebuje oprávnenia udelené cez `GITHUB_TOKEN` na checkout kódu a vytváranie pull requestov.

1.  Vo vašom repozitári choďte na **Settings** > **Actions** > **General**.
2.  Posuňte sa dole do sekcie **Workflow permissions**.
3.  Vyberte **Read and write permissions**. Tým udelíte `GITHUB_TOKEN` potrebné oprávnenia `contents: write` a `pull-requests: write` pre tento workflow.
4.  Uistite sa, že je zaškrtnuté políčko **Allow GitHub Actions to create and approve pull requests**.
5.  Kliknite na **Save**.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.sk.png)

### Krok 4: Vytvorenie workflow súboru

Nakoniec vytvorte YAML súbor, ktorý definuje automatizovaný workflow s použitím `GITHUB_TOKEN`.

1.  V koreňovom adresári vášho repozitára vytvorte adresár `.github/workflows/`, ak ešte neexistuje.
2.  Vnútri `.github/workflows/` vytvorte súbor s názvom `co-op-translator.yml`.
3.  Skopírujte nasledujúci obsah do `co-op-translator.yml`.

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
4.  **Prispôsobenie workflowu:**
  - **[!IMPORTANT] Cieľové jazyky:** V kroku `Run Co-op Translator` **MUSÍTE skontrolovať a upraviť zoznam jazykových kódov** v príkaze `translate -l "..." -y` podľa potrieb vášho projektu. Ukážkový zoznam (`ar de es...`) je potrebné nahradiť alebo upraviť.
  - **Spúšťač (`on:`):** Aktuálny spúšťač beží pri každom pushi na `main`. Pri veľkých repozitároch zvážte pridanie filtra `paths:` (pozrite komentovaný príklad v YAML), aby workflow bežal len pri zmene relevantných súborov (napr. zdrojová dokumentácia), čím ušetríte minúty runnera.
  - **Detaily PR:** Prispôsobte `commit-message`, `title`, `body`, názov `branch` a `labels` v kroku `Create Pull Request` podľa potreby.

## Spustenie workflowu

> [!WARNING]  
> **Časový limit GitHub-hosted runnera:**  
> GitHub-hosted runneri ako `ubuntu-latest` majú **maximálny čas vykonávania 6 hodín**.  
> Pri veľkých repozitároch s dokumentáciou, ak prekladový proces presiahne 6 hodín, workflow bude automaticky ukončený.  
> Aby ste tomu predišli, zvážte:  
> - Použitie **self-hosted runnera** (bez časového limitu)  
> - Zníženie počtu cieľových jazykov na jeden beh

Keď bude súbor `co-op-translator.yml` zlúčený do vašej hlavnej vetvy (alebo vetvy určenej v spúšťači `on:`), workflow sa automaticky spustí vždy, keď sa do tejto vetvy pushnú zmeny (a zodpovedajú filtru `paths`, ak je nastavený).

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.