# Оновлення розділу "Інші курси" (репозиторії Microsoft Beginners)

Цей посібник пояснює, як зробити автоматичну синхронізацію розділу "Інші курси" за допомогою Co-op Translator, а також як оновити глобальний шаблон для всіх репозиторіїв.

- Застосовується до: лише репозиторіїв Microsoft Beginners
- Працює з: Co-op Translator CLI та GitHub Actions
- Джерело шаблону: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Швидкий старт: увімкніть автоматичну синхронізацію у вашому репозиторії

Додайте наступні маркери навколо розділу "Інші курси" у вашому README. Co-op Translator замінюватиме все між цими маркерами при кожному запуску.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Кожного разу, коли Co-op Translator запускається — через CLI (наприклад, `translate -l "<language codes>"`) або GitHub Actions — він автоматично оновлює розділ "Інші курси", обгорнутий цими маркерами.

> [!NOTE]
> Якщо у вас є існуючий список, просто обгорніть його тими ж маркерами. Наступний запуск замінить його на останній стандартизований вміст.

---

## Як змінити глобальний вміст

Якщо ви хочете оновити стандартизований вміст, який відображається у всіх репозиторіях Beginners:

1. Змініть шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Відкрийте pull request у репозиторії Co-op Translator з вашими змінами
3. Після злиття PR версія Co-op Translator буде оновлена
4. Наступного разу, коли Co-op Translator запуститься (через CLI або GitHub Action) у цільовому репозиторії, він автоматично синхронізує оновлений розділ

Це гарантує єдине джерело правди для вмісту розділу "Інші курси" у всіх репозиторіях Beginners.


## Розмір репозиторіїв

Репозиторії можуть ставати великими через кількість перекладених мов, щоб допомогти кінцевим користувачам, надаючи рекомендації щодо використання clone - sparse для клонування лише необхідних мов, а не всього репозиторію

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
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникають унаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->