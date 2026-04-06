# Frissítse az „Egyéb tanfolyamok” részt (Microsoft kezdő adattárak)

Ez az útmutató elmagyarázza, hogyan lehet az „Egyéb tanfolyamok” részt automatikusan szinkronizálni a Co-op Translator használatával, valamint hogyan frissítheti a globális sablont az összes adattár számára.

- Alkalmazható: csak Microsoft kezdő adattárakra
- Működik: Co-op Translator CLI-vel és GitHub Actions-szel
- Sablon forrása: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Gyors indítás: Auto-sync engedélyezése az adattáradban

Add hozzá a következő jelölőket az „Egyéb tanfolyamok” rész köré a README-dben. A Co-op Translator minden futtatáskor kicseréli a jelölők közötti tartalmat.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Minden alkalommal, amikor a Co-op Translator fut – akár CLI-n keresztül (pl. `translate -l "<nyelvkódok>"`), akár GitHub Actions által – automatikusan frissíti az ezekkel a jelölőkkel körülvett „Egyéb tanfolyamok” részt.

> [!NOTE]
> Ha már van meglévő listád, csak vedd körbe ugyanazokkal a jelölőkkel. A következő futtatás lecseréli azt a legfrissebb szabványosított tartalomra.

---

## Hogyan változtasd meg a globális tartalmat

Ha frissíteni szeretnéd a szabványosított tartalmat, amely minden kezdő adattárban megjelenik:

1. Szerkeszd a sablont: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Nyiss egy pull request-et a Co-op Translator adattárába a változtatásaiddal
3. Miután a PR beolvadt, frissül a Co-op Translator verziója
4. Amikor legközelebb fut a Co-op Translator (CLI vagy GitHub Action) egy célzott adattárban, automatikusan szinkronizálja a frissített részt

Ez biztosítja az „Egyéb tanfolyamok” tartalmának egyetlen valós forrását az összes kezdő adattárban.

## Az adattárak mérete

Az adattárak nagyokká válhatnak a lefordított nyelvek száma miatt, hogy segítsék a végfelhasználókat az útmutatással, hogyan használják a clone - sparse parancsot csak a szükséges nyelvek klónozásához, nem pedig az egész adattárhoz.

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
**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) használatával fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->