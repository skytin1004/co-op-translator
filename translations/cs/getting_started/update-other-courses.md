# Aktualizace sekce „Other Courses“ (Microsoft Beginners repozitáře)

Tento průvodce vysvětluje, jak zajistit automatickou synchronizaci sekce „Other Courses“ pomocí Co‑op Translator, a jak aktualizovat globální šablonu pro všechny repozitáře.

- Platí pro: pouze Microsoft Beginners repozitáře
- Funguje s: Co‑op Translator CLI a GitHub Actions
- Zdroj šablony: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rychlý start: Povolení automatické synchronizace ve vašem repozitáři

Přidejte následující značky kolem sekce „Other Courses“ ve vašem README. Co‑op Translator při každém spuštění nahradí vše mezi těmito značkami.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pokaždé, když se Co‑op Translator spustí – přes CLI (např. `translate -l "<language codes>"`) nebo GitHub Actions – automaticky aktualizuje sekci „Other Courses“ uzavřenou mezi těmito značkami.

> [!NOTE]
> Pokud již máte existující seznam, stačí jej obalit stejnými značkami. Při dalším spuštění bude nahrazen nejnovějším standardizovaným obsahem.

---

## Jak změnit globální obsah

Pokud chcete aktualizovat standardizovaný obsah, který se zobrazuje ve všech Beginners repozitářích:

1. Upravte šablonu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otevřete pull request do repozitáře Co-op Translator se svými změnami
3. Po sloučení PR bude verze Co‑op Translatora aktualizována
4. Při dalším spuštění Co‑op Translatora (CLI nebo GitHub Action) v cílovém repozitáři dojde k automatické synchronizaci aktualizované sekce

Tím je zajištěn jediný zdroj pravdy pro obsah sekce „Other Courses“ ve všech Beginners repozitářích.


## Velikost repozitářů

Repozitáře mohou být velké kvůli velkému počtu přeložených jazyků, aby bylo možné uživatelům poskytnout návod, jak použít clone - sparse pro stažení pouze nezbytných jazyků a nikoliv celého repozitáře

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
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, berte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->