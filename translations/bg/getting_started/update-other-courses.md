# Актуализиране на раздела "Други курсове" (репозиторита на Microsoft Beginners)

Това ръководство обяснява как да направите секцията "Други курсове" да се синхронизира автоматично с помощта на Co-op Translator и как да актуализирате глобалния шаблон за всички репозиторита.

- Отнася се за: само репозиториите на Microsoft Beginners
- Работи с: Co-op Translator CLI и GitHub Actions
- Източник на шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Бърз старт: Активиране на авто-синхронизация във вашето репо

Добавете следните маркери около секцията "Други курсове" във вашия README. Co-op Translator ще замени всичко между тези маркери при всяко изпълнение.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Всеки път, когато Co-op Translator работи — чрез CLI (напр. `translate -l "<language codes>"`) или GitHub Actions — автоматично актуализира секцията "Други курсове", обградена с тези маркери.

> [!NOTE]
> Ако вече имате съществуващ списък, просто го обградете със същите маркери. Следващото изпълнение ще го замени с най-новото стандартизирано съдържание.

---

## Как да промените глобалното съдържание

Ако искате да актуализирате стандартизираното съдържание, което се появява във всички Beginners репозитории:

1. Редактирайте шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Отворете pull request към репозиторито на Co-op Translator с вашите промени
3. След сливането на PR, версията на Co-op Translator ще бъде актуализирана
4. Следващия път, когато Co-op Translator работи (чрез CLI или GitHub Action) в целево репо, той автоматично ще синхронизира актуализираната секция

Това осигурява единен източник на истината за съдържанието "Други курсове" във всички Beginners репозитории.

## Размери на репозиториите

Репозиторите могат да станат големи поради броя на преведените езици, за да помогнат на крайните потребители с указания как да използват clone - sparse, за да клонират само необходимите езици, а не целия репо

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
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->