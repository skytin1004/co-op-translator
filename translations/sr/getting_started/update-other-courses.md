# Ажурирање секције "Други курсеви" (репозиторијуми Microsoft Beginners)

Овај водич објашњава како аутоматски синхронизовати секцију "Други курсеви" користећи Co‑op Translator, и како ажурирати глобални шаблон за све репозиторијуме.

- Односи се на: Само Microsoft Beginners репозиторијуме
- Ради са: Co‑op Translator CLI и GitHub Actions
- Извор шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Брзи почетак: Омогућите аутоматску синхронизацију у вашем репо-у

Додајте следеће ознаке око секције "Други курсеви" у вашем README-у. Co‑op Translator ће заменити све између ових ознака сваки пут када се покрене.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Сваки пут када се Co‑op Translator покрене — преко CLI-а (нпр. `translate -l "<language codes>"`) или GitHub Actions — аутоматски ажурира секцију "Други курсеви" коју окружују ове ознаке.

> [!NOTE]
> Ако већ имате листу, само је обавијте са истим ознакама. Следеће покретање ће је заменити најновијим стандардизованим садржајем.

---

## Како променити глобални садржај

Ако желите да ажурирате стандардизовани садржај који се појављује у свим Beginners репозиторијумима:

1. Уредите шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Отворите pull request у Co-op Translator репозиторијум са вашим изменама
3. Након што се PR уједини, верзија Co‑op Translator-а ће бити ажурирана
4. Следећи пут када се Co‑op Translator покрене (CLI или GitHub Action) у циљаном репозиторijуму, аутоматски ће синхронизовати ажурирану секцију

Ово обезбеђује један извор истине за садржај "Други курсеви" у свим Beginners репозиторијумима.

## Величине репо-а

Репозиторијуми могу постати велики због броја преведених језика како би се помоћима крајњим корисницима пружила упутства како да користе clone - sparse да би клонирали само потребне језике, а не цео репозиторијум

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
**Поништење одговорности**:  
Овај документ је преведен коришћењем АИ преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која могу настати коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->