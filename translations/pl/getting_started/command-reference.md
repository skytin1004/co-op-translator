# Odwołanie do poleceń

CLI **Co-op Translator** oferuje kilka opcji umożliwiających dostosowanie procesu tłumaczenia:

Command                                       | Opis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Tłumaczy Twój projekt na określone języki. Przykład: translate -l "es fr de" tłumaczy na hiszpański, francuski i niemiecki. Użyj translate -l "all", aby przetłumaczyć na wszystkie obsługiwane języki.
translate -l "language_codes" -u              | Aktualizuje tłumaczenia poprzez usunięcie istniejących i ponowne ich utworzenie. Uwaga: Spowoduje to usunięcie wszystkich obecnych tłumaczeń dla określonych języków.
translate -l "language_codes" -img            | Tłumaczy tylko pliki obrazów.
translate -l "language_codes" -md             | Tłumaczy tylko pliki Markdown.
translate -l "language_codes" -nb             | Tłumaczy tylko pliki Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Ponownie tłumaczy pliki o niskim poziomie zaufania na podstawie wyników poprzedniej oceny.
translate -l "language_codes" -d              | Włącza tryb debugowania dla szczegółowego logowania.
translate -l "language_codes" --save-logs, -s | Zapisuje logi poziomu DEBUG do plików w <root_dir>/logs/ (konsola pozostaje kontrolowana przez -d)
translate -l "language_codes" -r "root_dir"   | Określa katalog główny projektu
translate -l "language_codes" -f              | Używa trybu szybkiego dla tłumaczenia obrazów (do 3x szybsze generowanie kosztem nieznacznej jakości i wyrównania).
translate -l "language_codes" -y              | Automatycznie potwierdza wszystkie monity (przydatne dla CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Włącza lub wyłącza dodawanie sekcji z zastrzeżeniem dotyczącym tłumaczeń maszynowych w tłumaczonych plikach markdown i notebookach (domyślnie: włączone).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizuje ostrzeżenie sekcji języków w README (sparse checkout) za pomocą adresu URL Twojego repozytorium.
translate -l "language_codes" --help          | szczegóły pomocy dostępne w CLI pokazujące dostępne polecenia
evaluate -l "language_code"                  | Ocena jakości tłumaczenia dla określonego języka i podanie wyników zaufania
evaluate -l "language_code" -c 0.8           | Ocena tłumaczeń z niestandardowym progiem zaufania
evaluate -l "language_code" -f               | Szybki tryb oceny (tylko oparte na regułach, bez LLM)
evaluate -l "language_code" -D               | Głęboka ocena (tylko LLM, bardziej szczegółowa, ale wolniejsza)
evaluate -l "language_code" --save-logs, -s  | Zapisuje logi poziomu DEBUG do plików w <root_dir>/logs/
migrate-links -l "language_codes"             | Ponowne przetworzenie przetłumaczonych plików Markdown w celu aktualizacji linków do notebooków (.ipynb). Preferuje przetłumaczone notebooki, gdy są dostępne; w przeciwnym razie może użyć oryginalnych notebooków.
migrate-links -l "language_codes" -r          | Określenie katalogu głównego projektu (domyślnie: bieżący katalog).
migrate-links -l "language_codes" --dry-run   | Pokazuje, które pliki uległyby zmianie bez zapisywania zmian.
migrate-links -l "language_codes" --no-fallback-to-original | Nie przepisywać linków do oryginalnych notebooków, gdy brakuje przetłumaczonych odpowiedników (aktualizuj tylko gdy istnieją tłumaczenia).
migrate-links -l "language_codes" -d          | Włącza tryb debugowania dla szczegółowego logowania.
migrate-links -l "language_codes" --save-logs, -s | Zapisuje logi poziomu DEBUG do plików w <root_dir>/logs/
migrate-links -l "all" -y                      | Przetwarza wszystkie języki i automatycznie potwierdza ostrzeżenie.

## Przykłady użycia

  1. Domyślne zachowanie (dodaje nowe tłumaczenia bez usuwania istniejących):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj tylko nowe korejskie tłumaczenia obrazów (nie są usuwane istniejące tłumaczenia):    translate -l "ko" -img

  3. Aktualizuj wszystkie koreańskie tłumaczenia (Uwaga: usuwa wszystkie istniejące koreańskie tłumaczenia przed ponownym tłumaczeniem):    translate -l "ko" -u

  4. Aktualizuj tylko koreańskie obrazy (Uwaga: usuwa wszystkie istniejące koreańskie obrazy przed ponownym tłumaczeniem):    translate -l "ko" -img -u

  5. Dodaj nowe tłumaczenia markdown dla koreańskiego bez wpływu na inne tłumaczenia:    translate -l "ko" -md

  6. Popraw tłumaczenia o niskim poziomie zaufania na podstawie poprzednich wyników oceny: translate -l "ko" --fix

  7. Popraw tłumaczenia o niskim poziomie zaufania dla określonych plików (markdown): translate -l "ko" --fix -md

  8. Popraw tłumaczenia o niskim poziomie zaufania dla określonych plików (obrazy): translate -l "ko" --fix -img

  9. Użyj szybkiego trybu dla tłumaczenia obrazów:    translate -l "ko" -img -f

  10. Popraw tłumaczenia o niskim poziomie zaufania z niestandardowym progiem: translate -l "ko" --fix -c 0.8

  11. Przykład trybu debugowania: - translate -l "ko" -d: Włącz logowanie debugowania.
  12. Zapisz logi do plików: translate -l "ko" -s
  13. DEBUG w konsoli i w pliku: translate -l "ko" -d -s
  14. Tłumacz bez dodawania zastrzeżeń tłumaczenia maszynowego do wyników: translate -l "ko" --no-disclaimer

  15. Migracja linków do notebooków dla koreańskich tłumaczeń (aktualizacja linków do przetłumaczonych notebooków, gdy dostępne):    migrate-links -l "ko"

  15. Migracja linków z dry-run (bez zapisu plików):    migrate-links -l "ko" --dry-run

  16. Aktualizuj linki tylko gdy istnieją przetłumaczone notebooki (nie cofaj do oryginałów):    migrate-links -l "ko" --no-fallback-to-original

  17. Przetwórz wszystkie języki z potwierdzeniem:    migrate-links -l "all"

  18. Przetwórz wszystkie języki i automatycznie potwierdź:    migrate-links -l "all" -y
  19. Zapisz logi do plików dla migrate-links:    migrate-links -l "ko ja" -s

  20. Spersonalizuj ostrzeżenie sekcji języków w README adresem URL swojego repozytorium:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Przykłady oceny

> [!WARNING]  
> **Funkcja Beta**: Funkcjonalność oceny jest obecnie w wersji beta. Ta funkcja została udostępniona do oceny przetłumaczonych dokumentów, a metody oceny oraz szczegółowa implementacja są w trakcie rozwoju i mogą ulec zmianie.

  1. Oceń koreańskie tłumaczenia: evaluate -l "ko"

  2. Oceń z niestandardowym progiem zaufania: evaluate -l "ko" -c 0.8

  3. Szybka ocena (tylko na podstawie reguł): evaluate -l "ko" -f

  4. Głęboka ocena (tylko LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonywanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->