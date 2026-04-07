# Aktualizace sekce "Other Courses" (Microsoft Beginners repozitáře)

Tato příručka vysvětluje, jak automaticky synchronizovat sekci "Other Courses" pomocí Co-op Translator a jak aktualizovat globální šablonu pro všechny repozitáře.

- Platí pro: pouze Microsoft Beginners repozitáře
- Funguje s: Co-op Translator CLI a GitHub Actions
- Zdroj šablony: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rychlý start: Povolení auto-synchronizace ve vašem repozitáři

Přidejte následující markery kolem sekce "Other Courses" ve vašem README. Co-op Translator při každém spuštění nahradí vše mezi těmito markery.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pokaždé, když Co-op Translator běží – přes CLI (např. `translate -l "<language codes>"`) nebo GitHub Actions – automaticky aktualizuje sekci "Other Courses" uzavřenou mezi těmito markery.

> [!NOTE]
> Pokud již máte existující seznam, stačí jej obalit stejnými markery. Při dalším spuštění bude nahrazen nejaktuálnějším standardizovaným obsahem.

---

## Jak změnit globální obsah

Pokud chcete aktualizovat standardizovaný obsah, který se zobrazuje ve všech Beginners repozitářích:

1. Upravte šablonu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otevřete pull request do repozitáře Co-op Translator s vašimi změnami
3. Po sloučení PR bude verze Co-op Translator aktualizována
4. Při příštím spuštění Co-op Translatoru (CLI nebo GitHub Action) v cílovém repozitáři se automaticky synchronizuje aktualizovaná sekce

Tím je zajištěn jediný zdroj pravdy pro obsah "Other Courses" ve všech Beginners repozitářích.


## Velikosti repozitářů

Repozitáře mohou být velké kvůli počtu přeložených jazyků, aby bylo koncovým uživatelům usnadněno, jak používat clone - sparse pro klonování pouze nezbytných jazyků a ne celého repozitáře.

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
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí služby AI překladatele [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->