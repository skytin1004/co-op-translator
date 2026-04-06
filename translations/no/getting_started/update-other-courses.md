# Oppdater seksjonen "Andre kurs" (Microsoft Beginners repositories)

Denne veiledningen forklarer hvordan du får seksjonen "Andre kurs" til å auto-synkronisere ved hjelp av Co-op Translator, og hvordan du oppdaterer den globale malen for alle repositories.

- Gjelder for: Kun Microsoft Beginners repositories
- Fungerer med: Co-op Translator CLI og GitHub Actions
- Mal-kilde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rask start: Aktiver auto-synk i ditt repo

Legg til følgende markører rundt seksjonen "Andre kurs" i README-filen din. Co-op Translator vil erstatte alt mellom disse markørene ved hver gjennomkjøring.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Hver gang Co-op Translator kjører—via CLI (f.eks. `translate -l "<language codes>"`) eller GitHub Actions—oppdateres automatisk seksjonen "Andre kurs" som er omsluttet av disse markørene.

> [!NOTE]
> Hvis du har en eksisterende liste, pakk den bare inn med de samme markørene. Neste kjøring vil erstatte den med det siste standardiserte innholdet.

---

## Hvordan endre det globale innholdet

Hvis du ønsker å oppdatere det standardiserte innholdet som vises i alle Beginners repositories:

1. Rediger malen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Åpne en pull request til Co-op Translator repo med dine endringer
3. Etter at PR-en er merget, vil versjonen av Co-op Translator oppdateres
4. Neste gang Co-op Translator kjører (CLI eller GitHub Action) i et mål-repo, vil den automatisk synkronisere den oppdaterte seksjonen

Dette sikrer en enkelt kilde til sannhet for innholdet i "Andre kurs" på tvers av alle Beginners repositories.


## Repo-størrelser

Repos kan bli store på grunn av antall språk som oversettes til for å hjelpe sluttbrukere med veiledning om hvordan de kan bruke clone - sparse for kun å klone nødvendige språk og ikke hele repoen

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
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt eget språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->