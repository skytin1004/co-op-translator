# Uppdatera avsnittet "Andra kurser" (Microsoft Beginners-repos)

Denna guide förklarar hur man gör att avsnittet "Andra kurser" automatiskt synkroniseras med hjälp av Co-op Translator, och hur man uppdaterar den globala mallen för alla repos.

- Gäller för: Endast Microsoft Beginners repositories
- Fungerar med: Co-op Translator CLI och GitHub Actions
- Mallkälla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kom igång snabbt: Aktivera autosynk i ditt repo

Lägg till följande markörer runt avsnittet "Andra kurser" i din README. Co-op Translator ersätter allt mellan dessa markörer vid varje körning.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Varje gång Co-op Translator körs — via CLI (t.ex. `translate -l "<language codes>"`) eller GitHub Actions — uppdaterar den automatiskt avsnittet "Andra kurser" som är inneslutet av dessa markörer.

> [!NOTE]
> Om du redan har en lista, omslut den bara med samma markörer. Nästa körning ersätter den med det senaste standardiserade innehållet.

---

## Hur man ändrar det globala innehållet

Om du vill uppdatera det standardiserade innehållet som visas i alla Beginners repos:

1. Redigera mallen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Öppna en pull request till Co-op Translator-repot med dina ändringar
3. När PR:n har mergats uppdateras Co-op Translator-versionen
4. Nästa gång Co-op Translator körs (CLI eller GitHub Action) i ett målrepo synkroniseras den uppdaterade sektionen automatiskt

Detta säkerställer en enda sanningskälla för "Andra kurser"-innehållet i alla Beginners repositories.


## Repo-storlekar

Repos kan bli stora på grund av antalet språk som översätts för att hjälpa slutanvändare med vägledning om hur man använder clone - sparse för att bara klona nödvändiga språk och inte hela repot

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
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör anses vara den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->