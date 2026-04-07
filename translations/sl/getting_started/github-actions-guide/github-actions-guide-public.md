# Uporaba Co-op Translator GitHub Action (Javna nastavitev)

**Ciljna skupina:** Ta vodič je namenjen uporabnikom v večini javnih ali zasebnih repozitorijev, kjer so standardna dovoljenja GitHub Actions zadostna. Uporablja vgrajeni `GITHUB_TOKEN`.

Avtomatizirajte prevajanje dokumentacije vašega repozitorija brez napora z uporabo Co-op Translator GitHub Action. Ta vodič vas vodi skozi postopek nastavitve akcije, ki samodejno ustvari pull requeste s posodobljenimi prevodi, kadar koli se spremenijo vaši izvorni Markdown dokumenti ali slike.

> [!IMPORTANT]
>
> **Izbira pravega vodiča:**
>
> Ta vodič opisuje **enostavnejšo nastavitev z uporabo standardnega `GITHUB_TOKEN`**. To je priporočena metoda za večino uporabnikov, saj ni potrebno upravljati občutljivih zasebnih ključev GitHub App.
>

## Predpogoji

Preden nastavite GitHub Action, poskrbite, da imate pripravljene potrebne podatke za AI storitve.

**1. Obvezno: Poverilnice za jezikovni model AI**
Potrebujete podatke za vsaj en podprt jezikovni model:

- **Azure OpenAI**: Potrebujete Endpoint, API ključ, imena modelov/deploymentov, verzijo API.
- **OpenAI**: Potrebujete API ključ, (neobvezno: Org ID, Base URL, Model ID).
- Glejte [Podprti modeli in storitve](../../../../README.md) za podrobnosti.

**2. Neobvezno: Poverilnice za AI Vision (za prevajanje slik)**

- Potrebno le, če želite prevajati besedilo na slikah.
- **Azure AI Vision**: Potrebujete Endpoint in Subscription Key.
- Če tega ne navedete, bo akcija privzeto delovala v [načinu samo za Markdown](../markdown-only-mode.md).

## Nastavitev in konfiguracija

Sledite tem korakom za nastavitev Co-op Translator GitHub Action v vašem repozitoriju z uporabo standardnega `GITHUB_TOKEN`.

### 1. korak: Razumevanje avtentikacije (Uporaba `GITHUB_TOKEN`)

Ta potek dela uporablja vgrajeni `GITHUB_TOKEN`, ki ga zagotavlja GitHub Actions. Ta žeton samodejno omogoča dovoljenja za potek dela za interakcijo z vašim repozitorijem glede na nastavitve, določene v **3. koraku**.

### 2. korak: Nastavite skrivnosti repozitorija

Dodati morate le **podatke za AI storitve** kot šifrirane skrivnosti v nastavitvah vašega repozitorija.

1.  Odprite ciljni GitHub repozitorij.
2.  Pojdite na **Settings** > **Secrets and variables** > **Actions**.
3.  Pod **Repository secrets** kliknite **New repository secret** za vsako zahtevano skrivnost AI storitve, navedeno spodaj.

    ![Izbira nastavitve action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.sl.png) *(Referenca slike: prikazuje, kje dodati skrivnosti)*

**Zahtevane skrivnosti za AI storitve (dodajte VSE, ki jih potrebujete glede na predpogoje):**

| Ime skrivnosti                      | Opis                                      | Vir vrednosti                    |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Ključ za Azure AI Service (Computer Vision)  | Vaš Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint za Azure AI Service (Computer Vision) | Vaš Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Ključ za Azure OpenAI storitev            | Vaš Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint za Azure OpenAI storitev         | Vaš Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Ime vašega Azure OpenAI modela            | Vaš Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Ime vašega Azure OpenAI deploymenta       | Vaš Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Verzija API za Azure OpenAI               | Vaš Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API ključ za OpenAI                       | Vaša OpenAI platforma              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (neobvezno)        | Vaša OpenAI platforma              |
| `OPENAI_CHAT_MODEL_ID`              | ID določenega OpenAI modela (neobvezno)   | Vaša OpenAI platforma              |
| `OPENAI_BASE_URL`                   | Osnovni URL za OpenAI API (neobvezno)     | Vaša OpenAI platforma              |

### 3. korak: Nastavite dovoljenja za potek dela

GitHub Action potrebuje dovoljenja, ki jih omogoča `GITHUB_TOKEN`, za prenos kode in ustvarjanje pull requestov.

1.  V repozitoriju pojdite na **Settings** > **Actions** > **General**.
2.  Pomaknite se do razdelka **Workflow permissions**.
3.  Izberite **Read and write permissions**. S tem omogočite `GITHUB_TOKEN` potrebna dovoljenja `contents: write` in `pull-requests: write` za ta potek dela.
4.  Prepričajte se, da je potrjeno polje **Allow GitHub Actions to create and approve pull requests**.
5.  Kliknite **Save**.

![Nastavitev dovoljenj](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.sl.png)

### 4. korak: Ustvarite datoteko poteka dela

Na koncu ustvarite YAML datoteko, ki definira avtomatiziran potek dela z uporabo `GITHUB_TOKEN`.

1.  V korenskem imeniku repozitorija ustvarite mapo `.github/workflows/`, če še ne obstaja.
2.  V mapi `.github/workflows/` ustvarite datoteko z imenom `co-op-translator.yml`.
3.  V datoteko `co-op-translator.yml` prilepite naslednjo vsebino.

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
4.  **Prilagodite potek dela:**
  - **[!IMPORTANT] Ciljni jeziki:** V koraku `Run Co-op Translator` **MORATE pregledati in po potrebi spremeniti seznam jezikovnih kod** v ukazu `translate -l "..." -y`, da ustreza potrebam vašega projekta. Primer seznama (`ar de es...`) je treba zamenjati ali prilagoditi.
  - **Sprožilec (`on:`):** Trenutni sprožilec se zažene ob vsakem pushu na `main`. Za večje repozitorije razmislite o dodajanju filtra `paths:` (glejte komentiran primer v YAML), da se potek dela zažene le ob spremembah relevantnih datotek (npr. izvorne dokumentacije) in tako prihranite minute izvajanja.
  - **Podrobnosti PR:** Po potrebi prilagodite `commit-message`, `title`, `body`, ime `branch` in `labels` v koraku `Create Pull Request`.

## Zagon poteka dela

> [!WARNING]  
> **Časovna omejitev za GitHub-hosted runnerje:**  
> GitHub-hosted runnerji, kot je `ubuntu-latest`, imajo **najdaljši čas izvajanja 6 ur**.  
> Če prevajanje v velikih repozitorijih preseže 6 ur, bo potek dela samodejno prekinjen.  
> Da to preprečite, razmislite o:  
> - Uporabi **self-hosted runnerja** (brez časovne omejitve)  
> - Zmanjšanju števila ciljnih jezikov na posamezen zagon

Ko je datoteka `co-op-translator.yml` združena v vašo glavno vejo (ali vejo, določeno v sprožilcu `on:`), se bo potek dela samodejno zagnal ob vsaki spremembi, potisnjeni v to vejo (in če ustreza filtru `paths`, če je nastavljen).

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.