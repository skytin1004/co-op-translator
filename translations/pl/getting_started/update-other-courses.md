# Aktualizacja sekcji "Inne kursy" (repozytoria Microsoft Beginners)

Ten przewodnik wyjaśnia, jak automatycznie synchronizować sekcję "Inne kursy" za pomocą Co‑op Translator oraz jak zaktualizować globalny szablon dla wszystkich repozytoriów.

- Dotyczy: wyłącznie repozytoriów Microsoft Beginners
- Działa z: Co‑op Translator CLI oraz GitHub Actions
- Źródło szablonu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Szybki start: Włącz auto‑synchronizację w swoim repozytorium

Dodaj następujące znaczniki wokół sekcji "Inne kursy" w swoim pliku README. Co‑op Translator zastąpi wszystko pomiędzy tymi znacznikami przy każdym uruchomieniu.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Za każdym razem gdy Co‑op Translator się uruchomi — poprzez CLI (np. `translate -l "<language codes>"`) lub GitHub Actions — automatycznie aktualizuje sekcję "Inne kursy" otoczoną tymi znacznikami.

> [!NOTE]
> Jeśli masz już istniejącą listę, wystarczy ją otoczyć tymi samymi znacznikami. Podczas następnego uruchomienia zostanie ona zastąpiona najnowszą, ujednoliconą zawartością.

---

## Jak zmienić globalną zawartość

Jeśli chcesz zaktualizować ustandaryzowaną zawartość, która pojawia się we wszystkich repozytoriach Beginners:

1. Edytuj szablon: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. Otwórz pull request do repozytorium Co-op Translator ze swoimi zmianami  
3. Po scaleniu PR, wersja Co‑op Translatora zostanie zaktualizowana  
4. Przy następnym uruchomieniu Co‑op Translatora (CLI lub GitHub Action) w docelowym repozytorium, sekcja zostanie automatycznie zsynchronizowana

To zapewnia jedno, wiarygodne źródło prawdy dla zawartości "Inne kursy" we wszystkich repozytoriach Beginners.

## Rozmiary repozytoriów

Repozytoria mogą stać się duże ze względu na liczbę tłumaczonych języków, aby pomóc użytkownikom końcowym wskazówki, jak używać clone - sparse do klonowania tylko niezbędnych języków, a nie całego repozytorium

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->