# Обновление раздела «Другие курсы» (репозитории Microsoft Beginners)

Это руководство объясняет, как сделать раздел «Другие курсы» автоматически синхронизируемым с помощью Co-op Translator и как обновить глобальный шаблон для всех репозиториев.

- Применимо к: только репозиториям Microsoft Beginners
- Работает с: Co-op Translator CLI и GitHub Actions
- Исходный шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Быстрый старт: Включите авто-синхронизацию в вашем репозитории

Добавьте следующие маркеры вокруг раздела «Другие курсы» в вашем README. Co-op Translator будет заменять все, что находится между этими маркерами при каждом запуске.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Каждый раз, когда Co-op Translator запускается — через CLI (например, `translate -l "<language codes>"`) или GitHub Actions — он автоматически обновляет раздел «Другие курсы», заключённый в эти маркеры.

> [!NOTE]
> Если у вас есть существующий список, просто оберните его теми же маркерами. Следующий запуск заменит его на последний стандартизированный контент.

---

## Как изменить глобальный контент

Если вы хотите обновить стандартизированный контент, который отображается во всех репозиториях Beginners:

1. Отредактируйте шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Откройте pull request в репозиторий Co-op Translator с вашими изменениями
3. После слияния PR версия Co-op Translator будет обновлена
4. В следующий раз, когда Co-op Translator запустится (через CLI или GitHub Action) в целевом репозитории, он автоматически синхронизирует обновлённый раздел

Это обеспечивает единый источник правды для контента раздела «Другие курсы» во всех репозиториях Beginners.


## Размеры репозиториев

Репозитории могут стать большими из-за количества переводимых языков, чтобы помочь конечным пользователям получить руководство по использованию clone - sparse для клонирования только необходимых языков, а не всего репозитория.

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
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод специалистом. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->