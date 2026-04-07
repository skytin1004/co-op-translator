# به‌روزرسانی بخش «دوره‌های دیگر» (مخازن Microsoft Beginners)

این راهنما توضیح می‌دهد چگونه بخش «دوره‌های دیگر» را با استفاده از Co‑op Translator به‌صورت خودکار همگام‌سازی کنید و چطور قالب جهانی را برای همه مخازن به‌روزرسانی نمایید.

- برای: فقط مخازن Microsoft Beginners
- کار با: Co‑op Translator CLI و GitHub Actions
- منبع قالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## شروع سریع: فعال‌سازی همگام‌سازی خودکار در مخزن شما

نشانه‌های زیر را دور بخش «دوره‌های دیگر» در README خود اضافه کنید. Co‑op Translator در هر اجرا همه چیز بین این نشانه‌ها را جایگزین می‌کند.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

هر بار که Co‑op Translator اجرا شود — از طریق CLI (مثلاً `translate -l "<language codes>"`) یا GitHub Actions — بخش «دوره‌های دیگر» که با این نشانه‌ها محصور شده است را به‌صورت خودکار به‌روزرسانی می‌کند.

> [!NOTE]
> اگر فهرستی موجود دارید، کافی است تنها آن را با همان نشانه‌ها محصور کنید. اجرای بعدی آن را با محتوای استاندارد و به‌روز جایگزین خواهد کرد.

---

## چگونه محتوای جهانی را تغییر دهیم

اگر می‌خواهید محتوای استانداردی که در همه مخازن Beginners ظاهر می‌شود را به‌روزرسانی کنید:

1. قالب را ویرایش کنید: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. یک pull request به مخزن Co-op Translator با تغییرات خود باز کنید
3. پس از ادغام PR، نسخه Co‑op Translator به‌روزرسانی خواهد شد
4. دفعه بعد که Co‑op Translator (CLI یا GitHub Action) در یک مخزن هدف اجرا شود، بخش به‌روزشده را به‌صورت خودکار همگام خواهد کرد

این روش منبع حقیقت تکی برای محتوای «دوره‌های دیگر» در تمام مخازن Beginners را تضمین می‌کند.

## اندازه مخازن

مخازن می‌توانند به دلیل تعداد زبان‌های ترجمه شده بزرگ شوند تا به کاربران نهایی کمک کنند. راهنمایی برای استفاده از clone - sparse ارائه شده است تا تنها زبان‌های ضروری کلون شود و کل مخزن کلون نگردد.

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
**توضیحات مهم**:  
این سند با استفاده از سرویس ترجمه خودکار [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما به دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقصی باشند. سند اصلی به زبان مبدأ باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->