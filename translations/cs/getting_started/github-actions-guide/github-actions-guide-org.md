# Použití Co-op Translator GitHub Action (Organizační příručka)

**Cílová skupina:** Tato příručka je určena pro **interní uživatele Microsoftu** nebo **týmy, které mají přístup k potřebným přihlašovacím údajům pro předpřipravenou Co-op Translator GitHub App** nebo si mohou vytvořit vlastní GitHub App.

Automatizujte překlad dokumentace vašeho repozitáře snadno pomocí Co-op Translator GitHub Action. Tato příručka vás provede nastavením akce, která automaticky vytváří pull requesty s aktualizovanými překlady pokaždé, když se změní vaše zdrojové Markdown soubory nebo obrázky.

> [!IMPORTANT]
> 
> **Výběr správné příručky:**
>
> Tato příručka popisuje nastavení pomocí **GitHub App ID a Private Key**. Tento "Organizační" způsob obvykle potřebujete, pokud: **`GITHUB_TOKEN` má omezená oprávnění:** Nastavení vaší organizace nebo repozitáře omezuje výchozí oprávnění, která standardnímu `GITHUB_TOKEN` uděluje GitHub. Konkrétně pokud `GITHUB_TOKEN` nemá potřebná oprávnění pro zápis (například `contents: write` nebo `pull-requests: write`), workflow z [Veřejné příručky](./github-actions-guide-public.md) selže kvůli nedostatečným oprávněním. Použití dedikované GitHub App s explicitně udělenými oprávněními tento problém obchází.
>
> **Pokud se vás výše uvedené netýká:**
>
> Pokud má standardní `GITHUB_TOKEN` ve vašem repozitáři dostatečná oprávnění (tj. nejste omezeni organizačními restrikcemi), použijte **[Veřejnou příručku s GITHUB_TOKEN](./github-actions-guide-public.md)**. Veřejná příručka nevyžaduje získání ani správu App ID nebo Private Key a spoléhá pouze na standardní `GITHUB_TOKEN` a oprávnění repozitáře.

## Předpoklady

Než nastavíte GitHub Action, ujistěte se, že máte připravené potřebné přihlašovací údaje k AI službě.

**1. Povinné: Přihlašovací údaje k AI jazykovému modelu**
Potřebujete přihlašovací údaje alespoň k jednomu podporovanému jazykovému modelu:

- **Azure OpenAI**: Vyžaduje Endpoint, API Key, názvy modelu/deploymentu, verzi API.
- **OpenAI**: Vyžaduje API Key, (volitelně: Org ID, Base URL, Model ID).
- Podrobnosti viz [Podporované modely a služby](../../../../README.md).
- Příručka k nastavení: [Nastavení Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Volitelné: Přihlašovací údaje ke Computer Vision (pro překlad textu v obrázcích)**

- Potřebné pouze pokud chcete překládat text v obrázcích.
- **Azure Computer Vision**: Vyžaduje Endpoint a Subscription Key.
- Pokud není zadáno, akce se spustí v [režimu pouze pro Markdown](../markdown-only-mode.md).
- Příručka k nastavení: [Nastavení Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Nastavení a konfigurace

Postupujte podle těchto kroků pro nastavení Co-op Translator GitHub Action ve vašem repozitáři:

### Krok 1: Instalace a konfigurace GitHub App autentizace

Workflow používá autentizaci přes GitHub App pro bezpečnou interakci s vaším repozitářem (např. vytváření pull requestů) vaším jménem. Vyberte jednu možnost:

#### **Možnost A: Instalace předpřipravené Co-op Translator GitHub App (pro interní použití Microsoftu)**

1. Přejděte na stránku [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Zvolte **Install** a vyberte účet nebo organizaci, kde se nachází váš cílový repozitář.

    ![Instalace aplikace](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.cs.png)

1. Zvolte **Only select repositories** a vyberte svůj cílový repozitář (např. `PhiCookBook`). Klikněte na **Install**. Můžete být požádáni o ověření.

    ![Instalace autorizace](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.cs.png)

1. **Získání přihlašovacích údajů aplikace (vyžadován interní proces):** Aby workflow mohl autentizovat jako aplikace, potřebujete dvě informace od týmu Co-op Translator:
  - **App ID:** Jedinečný identifikátor Co-op Translator aplikace. App ID je: `1164076`.
  - **Private Key:** Musíte získat **celý obsah** souboru `.pem` s privátním klíčem od kontaktní osoby správce. **S tímto klíčem zacházejte jako s heslem a uchovávejte jej v bezpečí.**

1. Pokračujte na krok 2.

#### **Možnost B: Použití vlastní GitHub App**

- Pokud chcete, můžete si vytvořit a nakonfigurovat vlastní GitHub App. Ujistěte se, že má Read & write přístup k obsahu a pull requestům. Budete potřebovat její App ID a vygenerovaný Private Key.

### Krok 2: Nastavení tajných údajů repozitáře

Musíte přidat přihlašovací údaje GitHub App a vaše AI služby jako šifrovaná tajemství v nastavení repozitáře.

1. Přejděte do cílového GitHub repozitáře (např. `PhiCookBook`).

1. Otevřete **Settings** > **Secrets and variables** > **Actions**.

1. V sekci **Repository secrets** klikněte na **New repository secret** pro každé tajemství uvedené níže.

   ![Výběr nastavení akce](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.cs.png)

**Povinná tajemství (pro GitHub App autentizaci):**

| Název tajemství      | Popis                                             | Zdroj hodnoty                                   |
| :------------------- | :------------------------------------------------ | :----------------------------------------------- |
| `GH_APP_ID`          | App ID GitHub App (z kroku 1).                    | Nastavení GitHub App                            |
| `GH_APP_PRIVATE_KEY` | **Celý obsah** staženého souboru `.pem`.          | Soubor `.pem` (z kroku 1)                       |

**Tajemství AI služby (Přidejte VŠECHNA, která odpovídají vašim předpokladům):**

| Název tajemství                      | Popis                                         | Zdroj hodnoty                  |
| :----------------------------------- | :--------------------------------------------- | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`           | Klíč pro Azure AI Service (Computer Vision)    | Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`          | Endpoint pro Azure AI Service (Computer Vision)| Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`               | Klíč pro Azure OpenAI službu                   | Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint pro Azure OpenAI službu               | Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`            | Název vašeho Azure OpenAI modelu               | Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Název vašeho Azure OpenAI deploymentu          | Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`           | Verze API pro Azure OpenAI                     | Azure AI Foundry               |
| `OPENAI_API_KEY`                     | API klíč pro OpenAI                            | OpenAI Platform                |
| `OPENAI_ORG_ID`                      | OpenAI Organization ID                         | OpenAI Platform                |
| `OPENAI_CHAT_MODEL_ID`               | Konkrétní OpenAI model ID                      | OpenAI Platform                |
| `OPENAI_BASE_URL`                    | Vlastní OpenAI API Base URL                    | OpenAI Platform                |

![Zadání názvu proměnné prostředí](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.cs.png)

### Krok 3: Vytvoření workflow souboru

Nakonec vytvořte YAML soubor, který definuje automatizovaný workflow.

1. V kořenovém adresáři vašeho repozitáře vytvořte složku `.github/workflows/`, pokud neexistuje.

1. Uvnitř `.github/workflows/` vytvořte soubor s názvem `co-op-translator.yml`.

1. Vložte následující obsah do souboru co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **Přizpůsobení workflow:**
  - **[!IMPORTANT] Cílové jazyky:** Ve kroku `Run Co-op Translator` **MUSÍTE zkontrolovat a upravit seznam jazykových kódů** v příkazu `translate -l "..." -y` podle potřeb vašeho projektu. Ukázkový seznam (`ar de es...`) je třeba nahradit nebo upravit.
  - **Trigger (`on:`):** Aktuální trigger spouští workflow při každém pushi na `main`. U velkých repozitářů zvažte přidání filtru `paths:` (viz komentovaný příklad v YAML), aby se workflow spouštěl pouze při změně relevantních souborů (např. zdrojové dokumentace), což šetří čas běhu runneru.
  - **Detaily PR:** Přizpůsobte `commit-message`, `title`, `body`, název `branch` a `labels` ve kroku `Create Pull Request` podle potřeby.

## Správa a obnova přihlašovacích údajů

- **Bezpečnost:** Vždy ukládejte citlivé přihlašovací údaje (API klíče, privátní klíče) jako GitHub Actions secrets. Nikdy je nezveřejňujte v souboru workflow ani v kódu repozitáře.
- **[!IMPORTANT] Obnova klíčů (interní uživatelé Microsoftu):** Uvědomte si, že Azure OpenAI klíč používaný v rámci Microsoftu může mít povinnou politiku obnovy (např. každých 5 měsíců). Ujistěte se, že odpovídající GitHub secrets (`AZURE_OPENAI_...` klíče) **aktualizujete před jejich expirací**, abyste předešli selhání workflow.

## Spuštění workflow

> [!WARNING]  
> **Časový limit pro GitHub-hosted runner:**  
> GitHub-hosted runnery jako `ubuntu-latest` mají **maximální čas běhu 6 hodin**.  
> U velkých repozitářů s dokumentací, pokud překladový proces přesáhne 6 hodin, workflow bude automaticky ukončen.  
> Abyste tomu předešli, zvažte:  
> - Použití **self-hosted runneru** (bez časového limitu)  
> - Snížení počtu cílových jazyků na jeden běh

Jakmile je soubor `co-op-translator.yml` sloučen do vaší hlavní větve (nebo větve uvedené v triggeru `on:`), workflow se automaticky spustí pokaždé, když do této větve provedete změny (a odpovídají filtru `paths`, pokud je nastaven).

Pokud jsou překlady vygenerovány nebo aktualizovány, akce automaticky vytvoří Pull Request s těmito změnami, připravený k vaší kontrole a sloučení.

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neneseme odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.