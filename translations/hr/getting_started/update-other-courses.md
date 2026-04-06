# Ažurirajte odjeljak "Ostali tečajevi" (Microsoft Beginners repozitoriji)

Ovaj vodič objašnjava kako automatski sinkronizirati odjeljak "Ostali tečajevi" pomoću Co-op Translatora i kako ažurirati globalni predložak za sve repozitorije.

- Odnosi se na: samo Microsoft Beginners repozitorije
- Radi s: Co-op Translator CLI i GitHub Actions
- Izvor predloška: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Brzi početak: Omogućite automatsku sinkronizaciju u svom repozitoriju

Dodajte sljedeće oznake oko odjeljka "Ostali tečajevi" u vašem README-u. Co-op Translator će zamijeniti sve između ovih oznaka svaki put kad se pokrene.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Svaki put kad se Co-op Translator pokrene—putem CLI-ja (npr. `translate -l "<language codes>"`) ili GitHub Actions—ažurira automatski odjeljak "Ostali tečajevi" omotan ovim oznakama.

> [!NOTE]
> Ako imate postojeću listu, samo je omotajte istim oznakama. Sljedeće pokretanje će je zamijeniti najnovijim standardiziranim sadržajem.

---

## Kako promijeniti globalni sadržaj

Ako želite ažurirati standardizirani sadržaj koji se pojavljuje u svim Beginners repozitorijima:

1. Uredite predložak: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otvorite pull request u Co-op Translator repozitoriju sa svojim promjenama
3. Nakon što se PR spoji, verzija Co-op Translatora će biti ažurirana
4. Sljedeći put kad se Co-op Translator pokrene (CLI ili GitHub Action) u ciljnom repozitoriju, automatski će sinkronizirati ažurirani odjeljak

Ovo osigurava jedinstveni izvor istine za sadržaj "Ostali tečajevi" u svim Beginners repozitorijima.


## Veličine repozitorija

Repozitoriji mogu postati veliki zbog broja prevedenih jezika kako bi se krajnjim korisnicima pružile upute o tome kako koristiti clone - sparse za kloniranje samo potrebnih jezika, a ne cijelog repozitorija

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
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili kriva tumačenja nastala uporabom ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->