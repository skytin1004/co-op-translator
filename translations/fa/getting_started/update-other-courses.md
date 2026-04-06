# به‌روزرسانی بخش «دوره‌های دیگر» (مخازن مبتدیان مایکروسافت)

این راهنما توضیح می‌دهد چگونه بخش «دوره‌های دیگر» را با استفاده از Co‑op Translator به‌صورت خودکار همگام‌سازی کنید و چگونه قالب جهانی برای همه مخازن را به‌روزرسانی نمایید.

- اعمال برای: فقط مخازن مبتدیان مایکروسافت
- کار با: رابط خط فرمان Co‑op Translator و GitHub Actions
- منبع قالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## شروع سریع: فعال‌سازی همگام‌سازی خودکار در مخزن شما

علامت‌های زیر را در اطراف بخش «دوره‌های دیگر» در README خود اضافه کنید. Co‑op Translator هر بار که اجرا می‌شود، همه چیز بین این علامت‌ها را جایگزین خواهد کرد.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

هر بار که Co‑op Translator اجرا می‌شود—از طریق CLI (مثلاً `translate -l "<language codes>"`) یا GitHub Actions—بخش «دوره‌های دیگر» که با این علامت‌ها محدود شده است را به‌صورت خودکار به‌روزرسانی می‌کند.

> [!NOTE]
> اگر یک فهرست موجود دارید، فقط آن را با همان علامت‌ها بپیچید. اجرای بعدی آن را با محتوای استانداردشده و جدید جایگزین خواهد کرد.

---

## چگونه محتوای جهانی را تغییر دهیم

اگر می‌خواهید محتوای استانداردشده‌ای که در همه مخازن مبتدیان نمایش داده می‌شود را به‌روزرسانی کنید:

1. قالب را ویرایش کنید: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. یک pull request به مخزن Co-op Translator با تغییرات خود باز کنید
3. پس از ادغام PR، نسخه Co‑op Translator به‌روزرسانی خواهد شد
4. دفعه بعد که Co‑op Translator اجرا شود (CLI یا GitHub Action) در مخزن هدف، بخش به‌روزشده به‌صورت خودکار همگام‌سازی خواهد شد

این تضمین می‌کند که یک منبع حقیقت واحد برای محتوای «دوره‌های دیگر» در تمام مخازن مبتدیان وجود داشته باشد.

## اندازه مخازن

مخازن می‌توانند به دلیل تعداد زبان‌هایی که برای کمک به کاربران نهایی ترجمه شده‌اند، بزرگ شوند تا راهنمایی ارائه شود چگونه تنها زبان‌های لازم را با clone - sparse کلون کنند و کل مخزن را کلون نکنند.

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
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان بومی خود باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->