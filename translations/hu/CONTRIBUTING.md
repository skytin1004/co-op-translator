<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:03:05+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Közreműködés a Co-op Translator projekthez

Ez a projekt örömmel fogadja a hozzájárulásokat és javaslatokat. A legtöbb hozzájárulás esetén szükséges, hogy elfogadd a Contributor License Agreementet (CLA), amelyben kijelented, hogy jogodban áll, és ténylegesen megadod nekünk a jogokat a hozzájárulásod felhasználására. Részletekért látogass el a https://cla.opensource.microsoft.com oldalra.

Amikor benyújtasz egy pull requestet, egy CLA bot automatikusan ellenőrzi, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően jelöli a PR-t (pl. státusz ellenőrzés, komment). Egyszerűen kövesd a bot által adott utasításokat. Ezt csak egyszer kell megtenned minden olyan repónál, amely a mi CLA-nkat használja.

## Fejlesztői környezet beállítása

A fejlesztői környezethez ajánljuk a Poetry használatát a függőségek kezelésére. A projekt függőségeit a `pyproject.toml` fájlban kezeljük, ezért a telepítéshez is a Poetry-t használd.

### Virtuális környezet létrehozása

#### pip használatával

```bash
python -m venv .venv
```

#### Poetry használatával

```bash
poetry init
```

### Virtuális környezet aktiválása

#### pip és Poetry esetén is

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry használatával

```bash
poetry shell
```

### A csomag és szükséges függőségek telepítése

#### Poetry használatával (pyproject.toml alapján)

```bash
poetry install
```

### Manuális tesztelés

PR beküldése előtt fontos, hogy teszteld a fordítási funkciót valódi dokumentációval:

1. Hozz létre egy teszt könyvtárat a gyökérkönyvtárban:
    ```bash
    mkdir test_docs
    ```

2. Másolj néhány markdown dokumentációt és képet, amit le szeretnél fordítani, a teszt könyvtárba. Például:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Telepítsd a csomagot helyben:
    ```bash
    pip install -e .
    ```

4. Futtasd a Co-op Translator-t a teszt dokumentumokon:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Ellenőrizd a lefordított fájlokat a `test_docs/translations` és `test_docs/translated_images` mappákban, hogy megbizonyosodj róla:
   - A fordítás minősége megfelelő
   - A metaadat kommentek helyesek
   - Az eredeti markdown szerkezet megmaradt
   - A linkek és képek megfelelően működnek

Ez a manuális tesztelés segít abban, hogy a módosításaid valóban jól működjenek éles helyzetekben.

### Környezeti változók

1. Hozz létre egy `.env` fájlt a gyökérkönyvtárban a mellékelt `.env.template` fájl másolásával.
1. Töltsd ki a környezeti változókat az útmutató szerint.

> [!TIP]
>
> ### További fejlesztői környezet lehetőségek
>
> A projektet helyben futtatás mellett használhatod GitHub Codespaces-t vagy VS Code Dev Containers-t is alternatív fejlesztői környezetként.
>
> #### GitHub Codespaces
>
> A mintákat virtuálisan is futtathatod GitHub Codespaces segítségével, további beállítás nélkül.
>
> A gomb megnyitja a böngésződben egy webes VS Code példányt:
>
> 1. Nyisd meg a sablont (ez néhány percet igénybe vehet):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Helyi futtatás VS Code Dev Containers használatával
>
> ⚠️ Ez az opció csak akkor működik, ha a Docker Desktop legalább 16 GB RAM-ot kap. Ha kevesebb RAM-od van, próbáld ki a [GitHub Codespaces opciót](../..) vagy [állítsd be helyben](../..).
>
> Egy kapcsolódó lehetőség a VS Code Dev Containers, amely megnyitja a projektet a helyi VS Code-ban a [Dev Containers bővítmény](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) segítségével:
>
> 1. Indítsd el a Docker Desktopot (ha még nincs telepítve, telepítsd)
> 2. Nyisd meg a projektet:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Kódstílus

A [Black](https://github.com/psf/black) formázót használjuk Python kódhoz, hogy egységes kódstílust tartsunk fenn a projektben. A Black egy kompromisszummentes kódformázó, amely automatikusan átalakítja a Python kódot a Black stílusának megfelelően.

#### Konfiguráció

A Black konfigurációját a `pyproject.toml` fájlban adjuk meg:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black telepítése

A Black-et Poetry-vel (ajánlott) vagy pip-pel is telepítheted:

##### Poetry használatával

A Black automatikusan települ a fejlesztői környezet beállításakor:
```bash
poetry install
```

##### pip használatával

Ha pip-et használsz, közvetlenül telepítheted a Black-et:
```bash
pip install black
```

#### Black használata

##### Poetry-vel

1. Formázd az összes Python fájlt a projektben:
    ```bash
    poetry run black .
    ```

2. Formázz egy adott fájlt vagy könyvtárat:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip-pel

1. Formázd az összes Python fájlt a projektben:
    ```bash
    black .
    ```

2. Formázz egy adott fájlt vagy könyvtárat:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Javasoljuk, hogy állítsd be a szerkesztődet úgy, hogy mentéskor automatikusan formázza a kódot Black-kel. A legtöbb modern szerkesztő támogatja ezt bővítményekkel vagy pluginekkel.

## Co-op Translator futtatása

A Co-op Translator futtatásához Poetry használatával kövesd az alábbi lépéseket:

1. Navigálj abba a könyvtárba, ahol a fordítási teszteket szeretnéd elvégezni, vagy hozz létre egy ideiglenes mappát teszteléshez.

2. Futtasd az alábbi parancsot. Cseréld le a `-l ko` részt arra a nyelvkódra, amelyre fordítani szeretnél. A `-d` kapcsoló a debug módot jelzi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Győződj meg róla, hogy a Poetry környezeted aktív (poetry shell), mielőtt futtatod a parancsot.

## Új nyelv hozzáadása

Szívesen fogadunk új nyelvek támogatását. PR megnyitása előtt végezd el az alábbi lépéseket a gördülékeny átnézés érdekében.

1. Add hozzá a nyelvet a font mappinghoz
   - Szerkeszd a `src/co_op_translator/fonts/font_language_mappings.yml` fájlt
   - Adj hozzá egy bejegyzést:
     - `code`: ISO-szerű nyelvkód (pl. `vi`)
     - `name`: Emberbarát megjelenítési név
     - `font`: Olyan font, amely a `src/co_op_translator/fonts/` mappában megtalálható és támogatja a karakterkészletet
     - `rtl`: `true`, ha jobbról balra íródik, egyébként `false`

2. Szükséges fontfájlok hozzáadása (ha kell)
   - Ha új font szükséges, ellenőrizd, hogy a licenc kompatibilis-e a nyílt forráskódú terjesztéssel
   - Add hozzá a fontfájlt a `src/co_op_translator/fonts/` mappához

3. Helyi ellenőrzés
   - Futtass fordítást egy kis mintán (Markdown, képek, notebookok, ha releváns)
   - Ellenőrizd, hogy a kimenet helyesen jelenik-e meg, beleértve a fontokat és az esetleges RTL elrendezést

4. Dokumentáció frissítése
   - Győződj meg róla, hogy a nyelv szerepel a `getting_started/supported-languages.md` fájlban
   - A `README_languages_template.md`-hez nem kell módosítás; ez automatikusan generálódik a támogatott listából

5. PR megnyitása
   - Írd le, milyen nyelvet adtál hozzá, és milyen font/licenc szempontokat vettél figyelembe
   - Csatolj képernyőképeket a megjelenített eredményekről, ha lehetséges

Példa YAML bejegyzés:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Az új nyelv tesztelése

Az új nyelvet az alábbi parancs futtatásával tesztelheted:

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

## Karbantartók

### Commit üzenet és összevonási stratégia

A projekt commit történetének egységessége és átláthatósága érdekében egy meghatározott commit üzenet formátumot követünk **a végső commit üzenethez**, amikor a **Squash and Merge** stratégiát alkalmazzuk.

Amikor egy pull requestet (PR) összevonunk, az egyes commitok egyetlen commitba lesznek összegyúrva. A végső commit üzenetnek az alábbi formátumot kell követnie, hogy tiszta és egységes történetet kapjunk.

#### Commit üzenet formátum (squash and merge esetén)

Az alábbi formátumot használjuk commit üzenetekhez:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Meghatározza a commit kategóriáját. Az alábbi típusokat használjuk:
  - `Docs`: Dokumentációs frissítésekhez.
  - `Build`: Build rendszerhez vagy függőségekhez kapcsolódó változásokhoz, beleértve a konfigurációs fájlokat, CI workflowkat vagy a Dockerfile-t.
  - `Core`: A projekt alapvető funkcióihoz vagy jellemzőihez kapcsolódó módosításokhoz, különösen a `src/co_op_translator/core` könyvtárban lévő fájlok esetén.

- **description**: Rövid összefoglaló a változásról.
- **PR number**: A commithez tartozó pull request száma.

**Példák**:

- `Docs: Telepítési útmutató frissítése érthetőség miatt (#50)`
- `Core: Képfordítás kezelésének javítása (#60)`

> [!NOTE]
> Jelenleg a **`Docs`**, **`Core`** és **`Build`** előtagokat automatikusan hozzáadjuk a PR címéhez a módosított forráskódhoz rendelt címkék alapján. Ha a megfelelő címke van beállítva, általában nem kell manuálisan módosítanod a PR címét. Csak ellenőrizd, hogy minden helyes, és az előtag megfelelően generálódott.

#### Összevonási stratégia

A **Squash and Merge** az alapértelmezett stratégia a pull requestekhez. Ez biztosítja, hogy a commit üzenetek megfeleljenek a formátumnak, még akkor is, ha az egyes commitok nem.

**Indokok**:

- Tiszta, lineáris projekt történet.
- Egységes commit üzenetek.
- Kevesebb "zaj" az apró commitok miatt (pl. "fix typo").

Összevonáskor ügyelj rá, hogy a végső commit üzenet megfeleljen a fent leírt formátumnak.

**Squash and Merge példa**
Ha egy PR az alábbi commitokat tartalmazza:

- `fix typo`
- `update README`
- `adjust formatting`

Ezeket össze kell vonni egybe:
`Docs: Dokumentáció érthetőségének és formázásának javítása (#65)`

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.