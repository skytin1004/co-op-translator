# Update de sectie "Andere Cursussen" (Microsoft Beginners repositories)

Deze gids legt uit hoe je de sectie "Andere Cursussen" automatisch kunt synchroniseren met Co‑op Translator, en hoe je de globale template voor alle repositories bijwerkt.

- Toepasselijk voor: Alleen Microsoft Beginners repositories
- Werkt met: Co‑op Translator CLI en GitHub Actions
- Template bron: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Snelle start: Auto-sync inschakelen in je repository

Voeg de volgende markers toe rond de sectie "Andere Cursussen" in je README. Co‑op Translator vervangt alles tussen deze markers bij elke uitvoering.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Elke keer dat Co‑op Translator draait—via CLI (bijv. `translate -l "<language codes>"`) of GitHub Actions—wordt automatisch de sectie "Andere Cursussen" die door deze markers is omgeven bijgewerkt.

> [!NOTE]
> Als je al een bestaande lijst hebt, wikkel deze dan gewoon in dezelfde markers. De volgende uitvoering zal deze vervangen door de nieuwste gestandaardiseerde inhoud.

---

## Hoe de globale inhoud te wijzigen

Als je de gestandaardiseerde inhoud wilt bijwerken die in alle Beginners repositories verschijnt:

1. Bewerk de template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open een pull request naar de Co-op Translator repository met je wijzigingen
3. Nadat de PR is gemerged, wordt de Co‑op Translator versie bijgewerkt
4. De volgende keer dat Co‑op Translator draait (CLI of GitHub Action) in een doel-repository, wordt de bijgewerkte sectie automatisch gesynchroniseerd

Dit zorgt voor een enkele bron van waarheid voor de inhoud van "Andere Cursussen" in alle Beginners repositories.

## Grootte van de repos

De repositories kunnen groot worden door het aantal vertaalde talen om eindgebruikers te helpen met richtlijnen over hoe `clone - sparse` te gebruiken om alleen de benodigde talen te klonen en niet de volledige repository.

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
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->