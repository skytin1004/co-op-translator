# Ажурирање одељка "Остали курсеви" (Microsoft Beginners репозиторијуми)

Овај водич објашњава како да аутоматски синхронизујете одељак "Остали курсеви" помоћу Co‑op Translator-а, као и како да ажурирате глобални шаблон за све репозиторијуме.

- Односи се на: Само Microsoft Beginners репозиторијуме
- Ради са: Co‑op Translator CLI и GitHub Actions
- Извор шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Брзи почетак: Омогућите аутоматску синхронизацију у вашем репо-у

Додајте следеће маркере око одељка "Остали курсеви" у вашем README фајлу. Co‑op Translator ће сваки пут приликом покретања заменити све између ових маркера.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Сваки пут када Co‑op Translator покренете—путем CLI (нпр. `translate -l "<language codes>"`) или GitHub Actions—он аутоматски ажурира одељак "Остали курсеви" који је обухваћен овим маркерима.

> [!NOTE]
> Ако већ имате постојећу листу, само је омотајте истим маркерима. Следеће покретање ће ту заменити најновијим стандардизованим садржајем.

---

## Како променити глобални садржај

Уколико желите да ажурирате стандардизовани садржај који се појављује у свим Beginners репозиторијумима:

1. Уредите шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Отворите pull request ка Co-op Translator репозиторијуму са вашим изменама
3. Након што се PR споји, верзија Co‑op Translator-а ће бити ажурирана
4. Следећи пут када Co‑op Translator покренете (CLI или GitHub Action) у циљаном репозиторијуму, он ће аутоматски синхронизовати ажурирани одељак

Ово обезбеђује један извор истине за садржај "Остали курсеви" у свим Beginners репозиторијумима.


## Величине репозиторијума

Репозиторијуми могу постати велики због броја преведених језика, како би крајњим корисницима помогли и пружили упутства о коришћењу clone - sparse да би клонирали само неопходне језике а не цео репозиторијум.

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
**Одрицање**:  
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Не одговарамо за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->