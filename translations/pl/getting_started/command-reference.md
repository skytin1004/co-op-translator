# Command reference

The **Co-op Translator** CLI oferuje kilka opcji dostosowania procesu tłumaczenia:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Tłumaczy Twój projekt na określone języki. Przykład: translate -l "es fr de" tłumaczy na hiszpański, francuski i niemiecki. Użyj translate -l "all", aby przetłumaczyć na wszystkie obsługiwane języki.
translate -l "language_codes" -u              | Aktualizuje tłumaczenia, usuwając istniejące i tworząc je ponownie. Uwaga: spowoduje to usunięcie wszystkich obecnych tłumaczeń dla określonych języków.
translate -l "language_codes" -img            | Tłumaczy tylko pliki graficzne.
translate -l "language_codes" -md             | Tłumaczy tylko pliki Markdown.
translate -l "language_codes" -nb             | Tłumaczy tylko pliki notatników Jupyter (.ipynb).
translate -l "language_codes" --fix           | Przetłumacza ponownie pliki o niskich ocenach zaufania na podstawie wcześniejszych wyników oceny.
translate -l "language_codes" -d              | Włącza tryb debugowania dla szczegółowego logowania.
translate -l "language_codes" --save-logs, -s | Zapisuje logi poziomu DEBUG do plików w <root_dir>/logs/ (konsola pozostaje kontrolowana przez -d)
translate -l "language_codes" -r "root_dir"   | Określa katalog główny projektu
translate -l "language_codes" -f              | Używa trybu szybkiego dla tłumaczenia obrazów (do 3x szybsze renderowanie kosztem niewielkiej utraty jakości i wyrównania).
translate -l "language_codes" -y              | Automatycznie potwierdza wszystkie monity (przydatne w pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Włącza lub wyłącza dodawanie sekcji z informacją o tłumaczeniu maszynowym do tłumaczonych plików markdown i notatników (domyślnie włączone).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizuje sekcję języków w README (sparse checkout) z URL Twojego repozytorium.
translate -l "language_codes" --help          | szczegóły pomocy w CLI pokazujące dostępne polecenia
evaluate -l "language_code"                  | Ocena jakości tłumaczenia dla konkretnego języka i dostarcza oceny zaufania
evaluate -l "language_code" -c 0.8           | Ocena tłumaczeń z niestandardowym progiem zaufania
evaluate -l "language_code" -f               | Tryb szybkiej oceny (tylko reguły, bez LLM)
evaluate -l "language_code" -D               | Głęboka ocena (tylko LLM, bardziej szczegółowa, ale wolniejsza)
evaluate -l "language_code" --save-logs, -s  | Zapisuje logi poziomu DEBUG do plików w <root_dir>/logs/
migrate-links -l "language_codes"             | Ponowne przetworzenie przetłumaczonych plików Markdown w celu aktualizacji linków do notatników (.ipynb). Preferuje przetłumaczone notatniki, gdy są dostępne; w przeciwnym razie może odwołać się do oryginalnych.
migrate-links -l "language_codes" -r          | Określa katalog główny projektu (domyślnie: bieżący katalog).
migrate-links -l "language_codes" --dry-run   | Pokaż, które pliki uległyby zmianie bez zapisywania zmian.
migrate-links -l "language_codes" --no-fallback-to-original | Nie przepisywuj linków do oryginalnych notatników, gdy brak jest przetłumaczonych odpowiedników (aktualizuj tylko, gdy istnieją tłumaczenia).
migrate-links -l "language_codes" -d          | Włącz tryb debugowania dla szczegółowego logowania.
migrate-links -l "language_codes" --save-logs, -s | Zapisuj logi poziomu DEBUG do plików w <root_dir>/logs/
migrate-links -l "all" -y                      | Przetwarzaj wszystkie języki i auto-potwierdź monit ostrzegawczy.

## Usage examples

  1. Domyślne zachowanie (dodawanie nowych tłumaczeń bez usuwania istniejących):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj tylko nowe koreańskie tłumaczenia obrazów (bez usuwania istniejących tłumaczeń):    translate -l "ko" -img

  3. Aktualizuj wszystkie koreańskie tłumaczenia (Uwaga: Usuwa wszystkie obecne koreańskie tłumaczenia przed ponownym tłumaczeniem):    translate -l "ko" -u

  4. Aktualizuj tylko koreańskie obrazy (Uwaga: Usuwa wszystkie istniejące koreańskie obrazy przed ponownym tłumaczeniem):    translate -l "ko" -img -u

  5. Dodaj nowe tłumaczenia markdown dla koreańskiego bez wpływu na inne tłumaczenia:    translate -l "ko" -md

  6. Napraw tłumaczenia o niskim poziomie zaufania na podstawie wcześniejszych wyników: translate -l "ko" --fix

  7. Napraw tłumaczenia o niskim poziomie zaufania tylko dla konkretnych plików (markdown): translate -l "ko" --fix -md

  8. Napraw tłumaczenia o niskim poziomie zaufania tylko dla konkretnych plików (obrazy): translate -l "ko" --fix -img

  9. Użyj trybu szybkiego dla tłumaczenia obrazów:    translate -l "ko" -img -f

  10. Napraw tłumaczenia o niskim poziomie zaufania z niestandardowym progiem: translate -l "ko" --fix -c 0.8

  11. Przykład trybu debugowania: - translate -l "ko" -d: Włącz rejestrowanie debugowania.
  12. Zapisz logi do plików: translate -l "ko" -s
  13. DEBUG konsoli i DEBUG pliku: translate -l "ko" -d -s
  14. Tłumacz bez dodawania informacji o tłumaczeniu maszynowym do wyników: translate -l "ko" --no-disclaimer

  15. Migracja linków do notatników dla tłumaczeń koreańskich (aktualizacja linków do przetłumaczonych notatników, gdy dostępne):    migrate-links -l "ko"

  15. Migracja linków z suchym przebiegiem (bez zapisu do plików):    migrate-links -l "ko" --dry-run

  16. Aktualizuj linki tylko wtedy, gdy istnieją przetłumaczone notatniki (bez odwołania do oryginałów):    migrate-links -l "ko" --no-fallback-to-original

  17. Przetwarzaj wszystkie języki z monitowaniem potwierdzenia:    migrate-links -l "all"

  18. Przetwarzaj wszystkie języki i auto-potwierdź:    migrate-links -l "all" -y
  19. Zapisz logi do plików dla migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizuj informacje o językach w README za pomocą URL repozytorium:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Funkcja Beta**: Funkcjonalność oceny jest obecnie w fazie beta. Ta funkcja została udostępniona do oceny przetłumaczonych dokumentów, a metody oceny oraz szczegółowa implementacja są w trakcie rozwoju i mogą ulec zmianie.

  1. Oceń tłumaczenia koreańskie: evaluate -l "ko"

  2. Oceń z niestandardowym progiem zaufania: evaluate -l "ko" -c 0.8

  3. Szybka ocena (tylko oparte na regułach): evaluate -l "ko" -f

  4. Głęboka ocena (tylko oparte na LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznany za źródło wiarygodne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->