# Actualizați secțiunea "Other Courses" (repos Microsoft Beginners)

Acest ghid explică cum să faceți ca secțiunea "Other Courses" să se auto‑sincronizeze folosind Co‑op Translator și cum să actualizați șablonul global pentru toate repozitoriile.

- Se aplică pentru: doar repozitoriile Microsoft Beginners
- Funcționează cu: Co‑op Translator CLI și GitHub Actions
- Sursa șablonului: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Pornire rapidă: Activați auto-sincronizarea în repo-ul dvs.

Adăugați următorii markeri în jurul secțiunii "Other Courses" din README-ul dvs. Co‑op Translator va înlocui tot ce este între acești markeri la fiecare rulare.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

De fiecare dată când Co‑op Translator rulează — prin CLI (de exemplu, `translate -l "<language codes>"`) sau GitHub Actions — actualizează automat secțiunea "Other Courses" încadrată de acești markeri.

> [!NOTE]
> Dacă aveți o listă existentă, doar încadrați-o cu aceiași markeri. Următoarea rulare o va înlocui cu conținutul standardizat cel mai recent.

---

## Cum să modificați conținutul global

Dacă doriți să actualizați conținutul standardizat care apare în toate repozitoriile Beginners:

1. Editați șablonul: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Deschideți un pull request către repo-ul Co-op Translator cu modificările dvs.
3. După ce PR-ul este integrat, versiunea Co‑op Translator va fi actualizată
4. Data viitoare când Co‑op Translator rulează (CLI sau GitHub Action) într-un repo țintă, va sincroniza automat secțiunea actualizată

Acest lucru asigură o singură sursă de adevăr pentru conținutul "Other Courses" în toate repozitoriile Beginners.

## Dimensiuni repo

Repo-urile pot deveni mari din cauza numărului limbilor traduse pentru a ajuta utilizatorii finali, oferind indicații despre cum să folosească clone - sparse pentru a clona doar limbile necesare și nu întregul repo

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
**Disclaimer**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->