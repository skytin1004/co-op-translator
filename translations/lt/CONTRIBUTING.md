<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:15:48+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "lt"
}
-->
# Prisidėjimas prie Co-op Translator

Šis projektas kviečia prisidėti ir teikti pasiūlymus. Dauguma indėlių reikalauja, kad sutiktumėte su Contributor License Agreement (CLA), patvirtinančiu, kad turite teisę ir iš tikrųjų suteikiate mums teises naudoti jūsų indėlį. Daugiau informacijos rasite https://cla.opensource.microsoft.com.

Kai pateikiate pull request, CLA bot automatiškai nustatys, ar reikia pateikti CLA, ir atitinkamai pažymės PR (pvz., statuso patikrinimas, komentaras). Tiesiog sekite boto pateiktas instrukcijas. Tai reikės padaryti tik vieną kartą visiems repo, naudojantiems mūsų CLA.

## Aplinkos paruošimas vystymui

Norint paruošti vystymo aplinką šiam projektui, rekomenduojame naudoti Poetry priklausomybių valdymui. Priklausomybės tvarkomos per `pyproject.toml`, todėl jas diegti reikėtų su Poetry.

### Sukurkite virtualią aplinką

#### Naudojant pip

```bash
python -m venv .venv
```

#### Naudojant Poetry

```bash
poetry init
```

### Aktyvuokite virtualią aplinką

#### Tiek pip, tiek Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Naudojant Poetry

```bash
poetry shell
```

### Paketo ir reikalingų paketų diegimas

#### Naudojant Poetry (iš pyproject.toml)

```bash
poetry install
```

### Rankinis testavimas

Prieš pateikiant PR, svarbu išbandyti vertimo funkcionalumą su tikra dokumentacija:

1. Sukurkite testavimo katalogą pagrindiniame kataloge:
    ```bash
    mkdir test_docs
    ```

2. Nukopijuokite norimą išversti markdown dokumentaciją ir paveikslėlius į testavimo katalogą. Pavyzdžiui:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Įdiekite paketą lokaliai:
    ```bash
    pip install -e .
    ```

4. Paleiskite Co-op Translator savo testavimo dokumentuose:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Patikrinkite išverstus failus `test_docs/translations` ir `test_docs/translated_images`, kad įsitikintumėte:
   - Vertimo kokybe
   - Ar metaduomenų komentarai teisingi
   - Ar išlaikyta originali markdown struktūra
   - Ar nuorodos ir paveikslėliai veikia tinkamai

Šis rankinis testavimas padeda užtikrinti, kad jūsų pakeitimai veikia realiose situacijose.

### Aplinkos kintamieji

1. Sukurkite `.env` failą pagrindiniame kataloge, nukopijavę pateiktą `.env.template` failą.
1. Užpildykite aplinkos kintamuosius pagal instrukcijas.

> [!TIP]
>
> ### Papildomos vystymo aplinkos galimybės
>
> Be vietinio projekto paleidimo, galite naudoti GitHub Codespaces arba VS Code Dev Containers kaip alternatyvų vystymo aplinkos paruošimą.
>
> #### GitHub Codespaces
>
> Galite paleisti šiuos pavyzdžius virtualiai naudodami GitHub Codespaces, nereikia papildomų nustatymų ar diegimo.
>
> Mygtukas atidarys naršyklėje VS Code internetinę versiją:
>
> 1. Atidarykite šabloną (tai gali užtrukti kelias minutes):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Paleidimas vietoje naudojant VS Code Dev Containers
>
> ⚠️ Ši galimybė veiks tik jei jūsų Docker Desktop paskirta bent 16 GB RAM. Jei turite mažiau nei 16 GB RAM, galite išbandyti [GitHub Codespaces galimybę](../..) arba [paruošti vietinę aplinką](../..).
>
> Susijusi galimybė – VS Code Dev Containers, kuri atidarys projektą jūsų vietiniame VS Code naudojant [Dev Containers plėtinį](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Paleiskite Docker Desktop (įdiekite, jei dar neįdiegta)
> 2. Atidarykite projektą:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Kodo stilius

Naudojame [Black](https://github.com/psf/black) kaip Python kodo formatuotoją, kad palaikytume vienodą kodo stilių visame projekte. Black automatiškai performatuoja Python kodą pagal Black stilių.

#### Konfigūracija

Black konfigūracija nurodyta mūsų `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black diegimas

Galite įdiegti Black naudodami Poetry (rekomenduojama) arba pip:

##### Naudojant Poetry

Black automatiškai įdiegiama, kai paruošiate vystymo aplinką:
```bash
poetry install
```

##### Naudojant pip

Jei naudojate pip, Black galite įdiegti tiesiogiai:
```bash
pip install black
```

#### Black naudojimas

##### Su Poetry

1. Suformatuokite visus Python failus projekte:
    ```bash
    poetry run black .
    ```

2. Suformatuokite konkretų failą ar katalogą:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Su pip

1. Suformatuokite visus Python failus projekte:
    ```bash
    black .
    ```

2. Suformatuokite konkretų failą ar katalogą:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Rekomenduojame nustatyti redaktorių, kad kodas būtų automatiškai formatuojamas su Black išsaugojant. Dauguma šiuolaikinių redaktorių tai palaiko per plėtinius ar papildinius.

## Co-op Translator paleidimas

Norėdami paleisti Co-op Translator su Poetry savo aplinkoje, atlikite šiuos veiksmus:

1. Pereikite į katalogą, kuriame norite atlikti vertimo testus, arba sukurkite laikiną katalogą testavimui.

2. Vykdykite šią komandą. Pakeiskite `-l ko` į norimos kalbos kodą. `-d` žymi debug režimą.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Įsitikinkite, kad jūsų Poetry aplinka aktyvuota (poetry shell) prieš paleidžiant komandą.

## Naujos kalbos pridėjimas

Kviečiame prisidėti, pridedant naujų kalbų palaikymą. Prieš atidarant PR, atlikite žemiau nurodytus veiksmus, kad peržiūra vyktų sklandžiai.

1. Pridėkite kalbą į šriftų susiejimą
   - Redaguokite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Pridėkite įrašą su:
     - `code`: ISO tipo kalbos kodas (pvz., `vi`)
     - `name`: Draugiškas kalbos pavadinimas
     - `font`: Šriftas, esantis `src/co_op_translator/fonts/`, palaikantis rašmenį
     - `rtl`: `true`, jei rašoma iš dešinės į kairę, kitaip `false`

2. Pridėkite reikalingus šriftų failus (jei reikia)
   - Jei reikia naujo šrifto, patikrinkite licencijos suderinamumą su atviro kodo platinimu
   - Pridėkite šrifto failą į `src/co_op_translator/fonts/`

3. Vietinis patikrinimas
   - Paleiskite vertimus su nedideliu pavyzdžiu (Markdown, paveikslėliai, ir prireikus užrašų knygelės)
   - Patikrinkite, ar rezultatas tinkamai atvaizduojamas, įskaitant šriftus ir RTL išdėstymą, jei taikoma

4. Atnaujinkite dokumentaciją
   - Įsitikinkite, kad kalba yra `getting_started/supported-languages.md`
   - `README_languages_template.md` keisti nereikia; jis generuojamas iš palaikomų kalbų sąrašo

5. Atidarykite PR
   - Aprašykite pridėtą kalbą ir šrifto/licencijos aspektus
   - Pridėkite atvaizduotų rezultatų ekrano nuotraukas, jei įmanoma

Pavyzdinis YAML įrašas:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Naujos kalbos testavimas

Naują kalbą galite išbandyti paleisdami šią komandą:

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

## Prižiūrėtojai

### Commit žinutės ir sujungimo strategija

Kad projektas būtų aiškus ir nuoseklus, laikomės tam tikro commit žinutės formato **galutinei commit žinutei** naudojant **Squash and Merge** strategiją.

Kai pull request (PR) sujungiamas, atskiri commit bus sujungti į vieną. Galutinė commit žinutė turi atitikti žemiau pateiktą formatą, kad istorija būtų tvarkinga ir nuosekli.

#### Commit žinutės formatas (squash and merge)

Naudojame šį commit žinutės formatą:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Nurodo commit kategoriją. Naudojame šiuos tipus:
  - `Docs`: Dokumentacijos atnaujinimai.
  - `Build`: Pakeitimai, susiję su build sistema ar priklausomybėmis, įskaitant konfigūracijos failus, CI workflows ar Dockerfile.
  - `Core`: Projekto pagrindinės funkcijos ar savybių pakeitimai, ypač failuose `src/co_op_translator/core` kataloge.

- **description**: Trumpas pakeitimo aprašymas.
- **PR number**: Pull request numeris, susijęs su commit.

**Pavyzdžiai**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Šiuo metu **`Docs`**, **`Core`** ir **`Build`** priešdėliai automatiškai pridedami prie PR pavadinimų pagal priskirtas etiketes modifikuotam šaltinio kodui. Jei teisinga etiketė priskirta, paprastai nereikia rankiniu būdu keisti PR pavadinimo. Tiesiog patikrinkite, ar viskas teisinga ir priešdėlis sugeneruotas tinkamai.

#### Sujungimo strategija

Naudojame **Squash and Merge** kaip numatytą strategiją pull requestams. Ši strategija užtikrina, kad commit žinutės atitiktų mūsų formatą, net jei atskiri commit to nedaro.

**Privalumai**:

- Tvarkinga, linijinė projekto istorija.
- Nuoseklumas commit žinutėse.
- Mažiau triukšmo nuo smulkių commit (pvz., "fix typo").

Sujungiant, įsitikinkite, kad galutinė commit žinutė atitinka aukščiau aprašytą formatą.

**Squash and Merge pavyzdys**
Jei PR sudaro šie commit:

- `fix typo`
- `update README`
- `adjust formatting`

Jie turi būti sujungti į:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.