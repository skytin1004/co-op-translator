# Актуализиране на секцията "Други Курсове" (репозитории за Microsoft Beginners)

Това ръководство обяснява как да направите секцията "Други Курсове" авто-синхронизираща се, използвайки Co‑op Translator, и как да актуализирате глобалния шаблон за всички репозитории.

- Приложимо за: само репозитории Microsoft Beginners
- Работи с: Co‑op Translator CLI и GitHub Actions
- Източник на шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Бърз старт: Активиране на авто-синхронизацията в репото ви

Добавете следните маркери около секцията "Други Курсове" във вашия README. Co‑op Translator ще замени всичко между тези маркери при всяко стартиране.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Всеки път когато Co‑op Translator се изпълни — чрез CLI (например `translate -l "<language codes>"`) или GitHub Actions — автоматично актуализира секцията "Други Курсове", обградена от тези маркери.

> [!NOTE]
> Ако имате съществуващ списък, просто го оградете с тези маркери. Следващото изпълнение ще го замени с най-новото стандартизирано съдържание.

---

## Как да промените глобалното съдържание

Ако искате да актуализирате стандартизираното съдържание, което се показва във всички репозитории Beginners:

1. Редактирайте шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Отворете pull request към репото на Co-op Translator с вашите промени
3. След като PR бъде обединено, версията на Co‑op Translator ще бъде актуализирана
4. Следващия път, когато Co‑op Translator стартира (CLI или GitHub Action) в целевото репо, той автоматично ще синхронизира актуализираната секция

Това гарантира единен източник на истина за съдържанието на "Други Курсове" във всички репозитории Beginners.


## Размери на репозиториите

Репозиториите могат да станат големи заради броя езици, на които са преведени, за да се помогне на крайните потребители. Затова се предоставят насоки за използване на clone - sparse, за да се клонират само необходимите езици, а не цялото репо.

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
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->