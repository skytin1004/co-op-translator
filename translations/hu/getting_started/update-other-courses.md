# Frissítsd az "Egyéb tanfolyamok" szakaszt (Microsoft Beginners repók)

Ez az útmutató elmagyarázza, hogyan lehet az "Egyéb tanfolyamok" szakaszt automatikusan szinkronizálni a Co-op Translator segítségével, valamint hogyan kell frissíteni az összes repóra vonatkozó globális sablont.

- Alkalmazható: kizárólag Microsoft Beginners tárolókra
- Működik: Co-op Translator CLI-vel és GitHub Actions-szel
- Sablon forrása: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Gyors kezdés: Engedélyezd az automatikus szinkronizálást a repódban

Add hozzá a következő jelölőket az "Egyéb tanfolyamok" szakasz köré a README fájlban. A Co-op Translator minden futtatáskor kicseréli a jelölők között található tartalmat.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Minden alkalommal, amikor a Co-op Translator fut — CLI-n keresztül (pl. `translate -l "<language codes>"`) vagy GitHub Actions-en keresztül — automatikusan frissíti az ezen jelölők által keretezett "Egyéb tanfolyamok" szakaszt.

> [!NOTE]
> Ha már van meglévő listád, egyszerűen csomagold be ugyanazokkal a jelölőkkel. A következő futtatás lecseréli azt a legfrissebb, szabványosított tartalomra.

---

## Hogyan változtassuk meg a globális tartalmat

Ha frissíteni szeretnéd a szabványosított tartalmat, amely minden Beginners repóban megjelenik:

1. Szerkeszd a sablont: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Nyiss egy pull requestet a Co-op Translator repóban a változtatásaiddal
3. A PR összeolvadása után frissül a Co-op Translator verziója
4. Amikor legközelebb a Co-op Translator fut (akár CLI-n, akár GitHub Actionön) egy céltárolóban, automatikusan szinkronizálja a frissített szakaszt

Ez garantálja az "Egyéb tanfolyamok" tartalmának egyetlen, megbízható forrását az összes Beginners repó között.


## Repo méretek

A repók nagyra nőhetnek az általa támogatott nyelvek számától függően, hogy a végfelhasználók könnyebben megtalálhassák a megfelelő útmutatást, hogyan használják a clone - sparse-t csak a szükséges nyelvek klónozásához, nem az egész repóhoz.

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
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum a saját nyelvén tekintendő hivatalos forrásnak. Fontos információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->