# Aktualizacja sekcji "Other Courses" (repozytoria Microsoft Beginners)

Ten przewodnik wyjaśnia, jak automatycznie synchronizować sekcję "Other Courses" za pomocą Co‑op Translator oraz jak zaktualizować globalny szablon dla wszystkich repozytoriów.

- Dotyczy: tylko repozytoriów Microsoft Beginners
- Działa z: Co‑op Translator CLI i GitHub Actions
- Źródło szablonu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Szybki start: Włącz auto‑synchronizację w swoim repo

Dodaj następujące markery wokół sekcji "Other Courses" w swoim README. Co‑op Translator za każdym razem zastąpi wszystko pomiędzy tymi markerami.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Za każdym razem, gdy Co‑op Translator uruchamia się — przez CLI (np. `translate -l "<language codes>"`) lub GitHub Actions — automatycznie aktualizuje sekcję "Other Courses" otoczoną tymi markerami.

> [!NOTE]
> Jeśli masz już istniejącą listę, po prostu opakuj ją tymi samymi markerami. Przy następnym uruchomieniu zostanie ona zastąpiona najnowszą, ustandaryzowaną treścią.

---

## Jak zmienić globalną zawartość

Jeśli chcesz zaktualizować ustandaryzowaną zawartość pojawiającą się we wszystkich repozytoriach Beginners:

1. Edytuj szablon: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otwórz pull request w repozytorium Co-op Translator ze swoimi zmianami
3. Po zmergowaniu PR wersja Co‑op Translator zostanie zaktualizowana
4. Następnym razem, gdy Co‑op Translator uruchomi się (CLI lub GitHub Action) w docelowym repozytorium, automatycznie zsynchronizuje zaktualizowaną sekcję

Zapewnia to jedno źródło prawdy dla treści "Other Courses" we wszystkich repozytoriach Beginners.


## Rozmiary repozytoriów

Repozytoria mogą stać się duże ze względu na liczbę tłumaczonych języków, aby pomóc użytkownikom końcowym w korzystaniu z polecenia clone - sparse, pozwalającego na sklonowanie tylko niezbędnych języków, a nie całego repozytorium.

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
Dokument ten został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy uznać za źródło ostateczne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->