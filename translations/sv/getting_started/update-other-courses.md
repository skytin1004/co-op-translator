# Uppdatera avsnittet "Other Courses" (Microsoft Beginners-repositorier)

Denna guide förklarar hur man gör avsnittet "Other Courses" automatiskt synkroniserat med hjälp av Co‑op Translator, och hur man uppdaterar den globala mallen för alla repositorier.

- Gäller för: Endast Microsoft Beginners-repositorier
- Fungerar med: Co‑op Translator CLI och GitHub Actions
- Mallkälla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kom igång snabbt: Aktivera autosynk i ditt repo

Lägg till följande markörer runt avsnittet "Other Courses" i din README. Co‑op Translator kommer att ersätta allt mellan dessa markörer vid varje körning.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Varje gång Co‑op Translator körs—via CLI (t.ex. `translate -l "<language codes>"`) eller GitHub Actions—uppdateras automatiskt avsnittet "Other Courses" inneslutet av dessa markörer.

> [!NOTE]
> Om du har en befintlig lista, omslut den bara med samma markörer. Nästa körning kommer att ersätta den med det senaste standardiserade innehållet.

---

## Hur man ändrar det globala innehållet

Om du vill uppdatera det standardiserade innehållet som visas i alla Beginners-repos:

1. Redigera mallen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Öppna en pull request i Co-op Translator-repot med dina ändringar
3. Efter att PR:en är sammanslagen kommer Co‑op Translator-versionen att uppdateras
4. Nästa gång Co‑op Translator körs (CLI eller GitHub Action) i ett mållager, synkroniseras det uppdaterade avsnittet automatiskt

Detta säkerställer en enda sanningskälla för innehållet i "Other Courses" över alla Beginners-repositorier.


## Repo-storlekar

Repositorierna kan bli stora på grund av antalet språk som översätts för att hjälpa slutanvändare att få vägledning om hur man använder clone - sparse för att bara klona nödvändiga språk och inte hela repot

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
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->