<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:18:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "et"
}
-->
# Kaasalöömine Co-op Translatorisse

Selles projektis on teretulnud nii panused kui ka ettepanekud. Enamik panuseid nõuab, et nõustuksid Contributor License Agreementiga (CLA), millega kinnitad, et sul on õigus anda meile õigused oma panuse kasutamiseks. Täpsemalt loe https://cla.opensource.microsoft.com.

Kui esitad pull requesti, kontrollib CLA bot automaatselt, kas pead CLA täitma, ja märgistab PR-i vastavalt (nt staatuse kontroll, kommentaar). Järgi lihtsalt boti juhiseid. Seda pead tegema vaid korra kõigi meie CLA-d kasutavate repo-de puhul.

## Arenduskeskkonna seadistamine

Selle projekti arenduskeskkonna seadistamiseks soovitame kasutada Poetry't sõltuvuste haldamiseks. Kasutame projekti sõltuvuste haldamiseks faili `pyproject.toml`, seega sõltuvuste paigaldamiseks kasuta Poetry't.

### Virtuaalkeskkonna loomine

#### pip-iga

```bash
python -m venv .venv
```

#### Poetry-ga

```bash
poetry init
```

### Virtuaalkeskkonna aktiveerimine

#### pip-i ja Poetry jaoks

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry-ga

```bash
poetry shell
```

### Paketi ja vajalike pakettide paigaldamine

#### Poetry-ga (pyproject.toml põhjal)

```bash
poetry install
```

### Käsitsi testimine

Enne PR-i esitamist on oluline testida tõlke funktsionaalsust päris dokumentatsiooniga:

1. Loo juurkausta testkataloog:
    ```bash
    mkdir test_docs
    ```

2. Kopeeri mõned markdown-dokumendid ja pildid, mida soovid tõlkida, testkataloogi. Näiteks:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Paigalda pakett lokaalselt:
    ```bash
    pip install -e .
    ```

4. Käivita Co-op Translator oma testdokumentide peal:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kontrolli tõlgitud faile kataloogides `test_docs/translations` ja `test_docs/translated_images`, et veenduda:
   - Tõlke kvaliteet on hea
   - Metaandmete kommentaarid on õiged
   - Algne markdown struktuur on säilinud
   - Lingid ja pildid töötavad korrektselt

See käsitsi testimine aitab tagada, et sinu muudatused toimivad ka päris olukordades.

### Keskkonnamuutujad

1. Loo juurkausta `.env` fail, kopeerides olemasoleva `.env.template` faili.
1. Täida keskkonnamuutujad vastavalt juhistele.

> [!TIP]
>
> ### Täiendavad arenduskeskkonna valikud
>
> Lisaks lokaalsele käivitamisele saad kasutada ka GitHub Codespaces'i või VS Code Dev Containers'it alternatiivse arenduskeskkonna seadistamiseks.
>
> #### GitHub Codespaces
>
> Saad neid näiteid käivitada virtuaalselt GitHub Codespaces'is ilma täiendavate seadistusteta.
>
> Nupp avab veebipõhise VS Code'i sinu brauseris:
>
> 1. Ava mall (see võib võtta mitu minutit):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Kohalik käivitamine VS Code Dev Containers'iga
>
> ⚠️ See valik töötab ainult siis, kui sinu Docker Desktopile on eraldatud vähemalt 16 GB RAM-i. Kui sul on vähem kui 16 GB RAM-i, proovi [GitHub Codespaces'i valikut](../..) või [seadista lokaalselt](../..).
>
> Seotud valik on VS Code Dev Containers, mis avab projekti sinu kohalikus VS Code'is kasutades [Dev Containers extension'i](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Käivita Docker Desktop (paigalda, kui pole veel paigaldatud)
> 2. Ava projekt:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Koodistiil

Kasutame [Black](https://github.com/psf/black) Python koodi vormindajat, et hoida projektis ühtlast koodistiili. Black on kompromissitu vormindaja, mis muudab Python koodi automaatselt Blacki stiilile vastavaks.

#### Seadistamine

Blacki seadistus on määratud meie `pyproject.toml` failis:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blacki paigaldamine

Blacki saab paigaldada kas Poetry (soovitatav) või pip-iga:

##### Poetry-ga

Black paigaldatakse automaatselt arenduskeskkonna seadistamisel:
```bash
poetry install
```

##### pip-iga

Kui kasutad pip-i, saad Blacki paigaldada otse:
```bash
pip install black
```

#### Blacki kasutamine

##### Poetry-ga

1. Vorminda kõik projekti Python failid:
    ```bash
    poetry run black .
    ```

2. Vorminda konkreetne fail või kataloog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip-iga

1. Vorminda kõik projekti Python failid:
    ```bash
    black .
    ```

2. Vorminda konkreetne fail või kataloog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Soovitame seadistada oma koodiredaktori nii, et Black vormindaks koodi automaatselt salvestamisel. Enamik kaasaegseid redaktoreid toetab seda laienduste või pluginatega.

## Co-op Translatori käivitamine

Co-op Translatori käivitamiseks Poetry abil oma keskkonnas järgi neid samme:

1. Liigu kataloogi, kus soovid teha tõlketeste, või loo ajutine kaust testimiseks.

2. Käivita järgmine käsk. Asenda `-l ko` selle keele koodiga, millesse soovid tõlkida. `-d` lipp tähendab debug-režiimi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Veendu, et Poetry keskkond on aktiveeritud (poetry shell) enne käsu käivitamist.

## Uue keele lisamine

Ootame panuseid, mis lisavad uute keelte toe. Enne PR-i avamist tee allolevad sammud, et ülevaatus sujuks.

1. Lisa keel fontide kaardistusse
   - Muuda faili `src/co_op_translator/fonts/font_language_mappings.yml`
   - Lisa kirje:
     - `code`: ISO-laadne keelekood (nt `vi`)
     - `name`: Inimsõbralik nimi
     - `font`: Font, mis on olemas `src/co_op_translator/fonts/` kaustas ja toetab seda kirjasüsteemi
     - `rtl`: `true`, kui paremalt vasakule, muidu `false`

2. Lisa vajalikud fondifailid (vajadusel)
   - Kui on vaja uut fonti, kontrolli, et selle litsents lubab avatud lähtekoodiga levitamist
   - Lisa fondifail `src/co_op_translator/fonts/` kausta

3. Kohalik kontroll
   - Käivita tõlge väikese näidisega (Markdown, pildid ja märkmikud vastavalt vajadusele)
   - Veendu, et väljund kuvatakse õigesti, sh fondid ja RTL paigutus, kui asjakohane

4. Uuenda dokumentatsiooni
   - Veendu, et keel on kirjas failis `getting_started/supported-languages.md`
   - Faili `README_languages_template.md` muuta pole vaja; see genereeritakse toetatud nimekirja põhjal

5. Ava PR
   - Kirjelda lisatud keelt ja fonti/litsentsi puudutavaid asjaolusid
   - Lisa võimalusel ekraanipildid väljunditest

Näide YAML kirjest:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Uue keele testimine

Uut keelt saad testida järgmise käsuga:

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

## Hooldajad

### Commiti sõnum ja liitmisstrateegia

Et hoida projekti commitide ajalugu ühtlasena ja selgena, järgime kindlat commit-sõnumi formaati **lõpliku commit-sõnumi jaoks** kui kasutame **Squash and Merge** strateegiat.

Kui pull request (PR) liidetakse, surutakse üksikud commitid üheks commitiks. Lõplik commit-sõnum peab järgima allolevat formaati, et ajalugu oleks puhas ja ühtlane.

#### Commiti sõnumi formaat (squash and merge jaoks)

Kasutame commit-sõnumite jaoks järgmist formaati:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Määrab commit'i kategooria. Kasutame järgmisi tüüpe:
  - `Docs`: Dokumentatsiooni uuendused.
  - `Build`: Muudatused ehitussüsteemis või sõltuvustes, sh konfiguratsioonifailid, CI töövood või Dockerfile.
  - `Core`: Projekti põhifunktsionaalsuse või funktsioonide muudatused, eriti failides `src/co_op_translator/core` kataloogis.

- **description**: Lühike kokkuvõte muudatusest.
- **PR number**: Commitiga seotud pull requesti number.

**Näited**:

- `Docs: Täpsusta paigaldusjuhiseid (#50)`
- `Core: Paranda pilditõlke käsitlemist (#60)`

> [!NOTE]
> Praegu lisatakse **`Docs`**, **`Core`** ja **`Build`** prefiksid PR-i pealkirjale automaatselt vastavalt sellele, millised sildid on muudetud lähtekoodile rakendatud. Kui õige silt on lisatud, ei pea tavaliselt PR-i pealkirja käsitsi muutma. Pead vaid kontrollima, et kõik on õige ja prefiks on korrektselt genereeritud.

#### Liitmisstrateegia

Kasutame **Squash and Merge** kui vaikimisi PR-ide liitmisstrateegiat. See tagab, et commit-sõnumid järgivad meie formaati, isegi kui üksikud commitid seda ei tee.

**Põhjused**:

- Puhas, lineaarne projekti ajalugu.
- Ühtlus commit-sõnumites.
- Vähem müra väikestest commitidest (nt "fix typo").

Liitmisel veendu, et lõplik commit-sõnum järgib ülaltoodud formaati.

**Squash and Merge näide**
Kui PR sisaldab järgmisi committe:

- `fix typo`
- `update README`
- `adjust formatting`

Need tuleks suruda üheks:
`Docs: Täpsusta dokumentatsiooni ja vormindust (#65)`

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algses keeles on autoriteetne allikas. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamiste eest.