# Opdater sektionen "Andre kurser" (Microsoft Beginners repos)

Denne vejledning forklarer, hvordan man får sektionen "Andre kurser" til at synkronisere automatisk ved hjælp af Co-op Translator, og hvordan man opdaterer den globale skabelon for alle repos.

- Gælder for: Kun Microsoft Beginners repositories
- Virker med: Co-op Translator CLI og GitHub Actions
- Skabelonkilde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hurtig start: Aktivér autosynkronisering i dit repo

Tilføj følgende markører omkring sektionen "Andre kurser" i din README. Co-op Translator vil erstatte alt imellem disse markører ved hver kørsel.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Hver gang Co-op Translator kører—via CLI (f.eks. `translate -l "<language codes>"`) eller GitHub Actions—opdaterer den automatisk sektionen "Andre kurser" indrammet af disse markører.

> [!NOTE]
> Hvis du har en eksisterende liste, skal du bare omgive den med de samme markører. Næste kørsel erstatter den med det seneste standardiserede indhold.

---

## Sådan ændrer du det globale indhold

Hvis du ønsker at opdatere det standardiserede indhold, der vises i alle Beginners repos:

1. Rediger skabelonen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Åbn en pull request til Co-op Translator-repoet med dine ændringer
3. Når PR'en er flettet, bliver Co-op Translator-versionen opdateret
4. Næste gang Co-op Translator kører (CLI eller GitHub Action) i et målrettet repo, synkroniseres den opdaterede sektion automatisk

Dette sikrer en enkelt sandhedskilde for "Andre kurser"-indholdet på tværs af alle Beginners repositories.


## Repo størrelser

Repos kan blive store på grund af det antal sprog, der oversættes til, for at hjælpe slutbrugere med vejledning i, hvordan man bruger clone - sparse til kun at klone nødvendige sprog og ikke hele repoet

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
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->