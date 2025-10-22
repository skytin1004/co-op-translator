<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:45:45+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pl"
}
-->
# Współtworzenie Co-op Translator

Ten projekt zachęca do współtworzenia i zgłaszania sugestii. Większość kontrybucji wymaga zaakceptowania
Umowy Licencyjnej Współtwórcy (CLA), w której oświadczasz, że masz prawo i faktycznie udzielasz nam
prawa do korzystania z Twojego wkładu. Szczegóły znajdziesz na https://cla.opensource.microsoft.com.

Gdy zgłaszasz pull request, bot CLA automatycznie sprawdzi, czy musisz zaakceptować CLA i odpowiednio oznaczy PR (np. status, komentarz). Po prostu postępuj zgodnie z instrukcjami bota. Wystarczy zrobić to raz dla wszystkich repozytoriów korzystających z naszej CLA.

## Konfiguracja środowiska deweloperskiego

Do zarządzania zależnościami w tym projekcie zalecamy użycie Poetry. Używamy `pyproject.toml` do zarządzania zależnościami, więc do ich instalacji powinieneś używać Poetry.

### Tworzenie środowiska wirtualnego

#### Za pomocą pip

```bash
python -m venv .venv
```

#### Za pomocą Poetry

```bash
poetry init
```

### Aktywacja środowiska wirtualnego

#### Dla pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Za pomocą Poetry

```bash
poetry shell
```

### Instalacja pakietu i wymaganych zależności

#### Za pomocą Poetry (z pyproject.toml)

```bash
poetry install
```

### Testowanie manualne

Przed zgłoszeniem PR warto przetestować funkcjonalność tłumaczenia na prawdziwej dokumentacji:

1. Utwórz katalog testowy w katalogu głównym:
    ```bash
    mkdir test_docs
    ```

2. Skopiuj wybraną dokumentację markdown oraz obrazy do katalogu testowego. Przykład:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Zainstaluj pakiet lokalnie:
    ```bash
    pip install -e .
    ```

4. Uruchom Co-op Translator na swoich testowych dokumentach:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Sprawdź przetłumaczone pliki w `test_docs/translations` oraz `test_docs/translated_images`, aby zweryfikować:
   - Jakość tłumaczenia
   - Poprawność komentarzy z metadanymi
   - Zachowanie oryginalnej struktury markdown
   - Poprawność linków i obrazów

Takie testowanie pozwala upewnić się, że Twoje zmiany działają poprawnie w praktyce.

### Zmienne środowiskowe

1. Utwórz plik `.env` w katalogu głównym, kopiując dostarczony plik `.env.template`.
1. Uzupełnij zmienne środowiskowe zgodnie z instrukcją.

> [!TIP]
>
> ### Dodatkowe opcje środowiska deweloperskiego
>
> Oprócz lokalnego uruchamiania projektu możesz skorzystać z GitHub Codespaces lub VS Code Dev Containers jako alternatywnego środowiska.
>
> #### GitHub Codespaces
>
> Możesz uruchomić przykłady wirtualnie za pomocą GitHub Codespaces bez dodatkowej konfiguracji.
>
> Przycisk otworzy instancję VS Code w przeglądarce:
>
> 1. Otwórz szablon (może to potrwać kilka minut):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Lokalnie przez VS Code Dev Containers
>
> ⚠️ Ta opcja działa tylko, jeśli Twój Docker Desktop ma przydzielone co najmniej 16 GB RAM. Jeśli masz mniej, spróbuj [GitHub Codespaces](../..) lub [skonfiguruj lokalnie](../..).
>
> Alternatywą są VS Code Dev Containers, które otworzą projekt w lokalnym VS Code z rozszerzeniem [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Uruchom Docker Desktop (zainstaluj, jeśli nie masz)
> 2. Otwórz projekt:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Styl kodu

Używamy [Black](https://github.com/psf/black) jako formatera kodu Python, aby zachować spójny styl w projekcie. Black automatycznie formatuje kod zgodnie ze swoim standardem.

#### Konfiguracja

Konfiguracja Black znajduje się w naszym pliku `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacja Black

Możesz zainstalować Black przez Poetry (zalecane) lub pip:

##### Przez Poetry

Black instaluje się automatycznie podczas konfiguracji środowiska:
```bash
poetry install
```

##### Przez pip

Jeśli używasz pip, zainstaluj Black bezpośrednio:
```bash
pip install black
```

#### Użycie Black

##### Z Poetry

1. Sformatuj wszystkie pliki Python w projekcie:
    ```bash
    poetry run black .
    ```

2. Sformatuj wybrany plik lub katalog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Z pip

1. Sformatuj wszystkie pliki Python w projekcie:
    ```bash
    black .
    ```

2. Sformatuj wybrany plik lub katalog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Zalecamy skonfigurowanie edytora, aby automatycznie formatował kod Black przy zapisie. Większość nowoczesnych edytorów obsługuje to przez rozszerzenia lub wtyczki.

## Uruchamianie Co-op Translator

Aby uruchomić Co-op Translator przez Poetry w swoim środowisku, wykonaj następujące kroki:

1. Przejdź do katalogu, w którym chcesz wykonać testy tłumaczenia lub utwórz tymczasowy folder do testów.

2. Wykonaj poniższe polecenie. Zmień `-l ko` na kod języka, na który chcesz tłumaczyć. Flaga `-d` uruchamia tryb debugowania.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Upewnij się, że środowisko Poetry jest aktywne (poetry shell) przed uruchomieniem polecenia.

## Dodanie nowego języka

Chętnie przyjmujemy kontrybucje dodające obsługę nowych języków. Przed zgłoszeniem PR wykonaj poniższe kroki, aby ułatwić przegląd.

1. Dodaj język do mapowania czcionek
   - Edytuj `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodaj wpis z:
     - `code`: kod języka w stylu ISO (np. `vi`)
     - `name`: przyjazna nazwa wyświetlana
     - `font`: czcionka dostępna w `src/co_op_translator/fonts/`, obsługująca dany alfabet
     - `rtl`: `true` jeśli język jest pisany od prawej do lewej, w przeciwnym razie `false`

2. Dodaj wymagane pliki czcionek (jeśli potrzeba)
   - Jeśli wymagana jest nowa czcionka, sprawdź zgodność licencji z dystrybucją open source
   - Dodaj plik czcionki do `src/co_op_translator/fonts/`

3. Weryfikacja lokalna
   - Przetłumacz próbkę (Markdown, obrazy, notatniki jeśli trzeba)
   - Sprawdź, czy wynik wyświetla się poprawnie, w tym czcionki i ewentualny układ RTL

4. Aktualizacja dokumentacji
   - Upewnij się, że język pojawia się w `getting_started/supported-languages.md`
   - Nie trzeba zmieniać `README_languages_template.md`; generuje się z listy obsługiwanych języków

5. Zgłoś PR
   - Opisz dodany język oraz kwestie czcionek/licencji
   - Dołącz zrzuty ekranu z renderowania, jeśli to możliwe

Przykładowy wpis YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testowanie nowego języka

Możesz przetestować nowy język, uruchamiając polecenie:

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

## Utrzymujący

### Format wiadomości commit i strategia scalania

Aby zachować spójność i przejrzystość historii commitów, stosujemy określony format wiadomości **dla finalnego commita** przy strategii **Squash and Merge**.

Gdy pull request (PR) zostaje scalony, poszczególne commity są łączone w jeden. Finalna wiadomość powinna mieć poniższy format, by zachować czystą historię.

#### Format wiadomości commit (dla squash and merge)

Stosujemy następujący format:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Kategoria commita. Używamy:
  - `Docs`: Aktualizacje dokumentacji.
  - `Build`: Zmiany związane z systemem budowania lub zależnościami, w tym konfiguracje, workflow CI, Dockerfile.
  - `Core`: Modyfikacje kluczowych funkcji projektu, szczególnie plików w `src/co_op_translator/core`.

- **description**: Krótkie podsumowanie zmiany.
- **PR number**: Numer pull requestu powiązanego z commitem.

**Przykłady**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Obecnie prefiksy **`Docs`**, **`Core`** i **`Build`** są automatycznie dodawane do tytułów PR na podstawie etykiet przypisanych do zmienionego kodu. Jeśli etykieta jest poprawna, zwykle nie musisz ręcznie zmieniać tytułu PR. Wystarczy sprawdzić, czy wszystko jest poprawne i prefiks został wygenerowany prawidłowo.

#### Strategia scalania

Domyślnie stosujemy **Squash and Merge** dla pull requestów. Ta strategia zapewnia, że wiadomości commitów mają nasz format, nawet jeśli poszczególne commity go nie mają.

**Powody**:

- Czysta, liniowa historia projektu.
- Spójność wiadomości commitów.
- Mniej "szumu" od drobnych commitów (np. "fix typo").

Przy scalaniu upewnij się, że finalna wiadomość commit ma opisany wyżej format.

**Przykład Squash and Merge**
Jeśli PR zawiera commity:

- `fix typo`
- `update README`
- `adjust formatting`

Powinny zostać połączone w:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za autorytatyczne źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnych usług tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.