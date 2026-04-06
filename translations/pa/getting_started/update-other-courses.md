# "ਦੂਜੇ ਕੋਰਸ" ਭਾਗ ਨੂੰ ਅੱਪਡੇਟ ਕਰੋ (Microsoft Beginners ਰਿਪੋਜ਼)

ਇਹ ਗਾਈਡ ਸਮਝਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ "ਦੂਜੇ ਕੋਰਸ" ਭਾਗ ਨੂੰ Co‑op Translator ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਟੋ‑ਸਿੰਕ ਕਰਨ ਲਈ ਬਣਾਇਆ ਜਾਵੇ, ਅਤੇ ਸਾਰੇ ਰਿਪੋਜ਼ ਲਈ ਗਲੋਬਲ ਟੈਂਪਲੇਟ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ।

- ਲਾਗੂ ਹੁੰਦਾ ਹੈ: ਕੇਵਲ Microsoft Beginners ਰਿਪੋਜ਼
- ਕੰਮ ਕਰਦਾ ਹੈ: Co‑op Translator CLI ਅਤੇ GitHub Actions ਨਾਲ
- ਟੈਂਪਲੇਟ ਸਰੋਤ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ਤੇਜ਼ ਸ਼ੁਰੂਆਤ: ਆਪਣੇ ਰਿਪੋ ਵਿੱਚ ਆਟੋ‑ਸਿੰਕ ਸਹੀਕਾਰ ਕਰੋ

ਆਪਣੇ README ਵਿੱਚ "ਦੂਜੇ ਕੋਰਸ" ਭਾਗ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਹੇਠਾਂ ਦਿੱਤੇ ਗਏ ਮਾਰਕਰ ਸ਼ਾਮਲ ਕਰੋ। Co‑op Translator ਹਰ ਦਫਾ ਇਹ ਮਾਰਕਰਾਂ ਵਿੱਚ ਦੇ ਬੀਚ ਵਾਲੀ ਸਾਰੀ ਸਮੱਗਰੀ ਬਦਲ ਦੇਵੇਗਾ।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ਹਰ ਵਾਰ ਜਦੋਂ Co‑op Translator ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ—CLI ਰਾਹੀਂ (ਜਿਵੇਂ ਕਿ `translate -l "<language codes>"`) ਜਾਂ GitHub Actions ਰਾਹੀਂ—ਇਹ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਇਨ੍ਹਾਂ ਮਾਰਕਰਾਂ ਨਾਲ ਘੇਰੀ ਹੋਈ "ਦੂਜੇ ਕੋਰਸ" ਭਾਗ ਨੂੰ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ।

> [!NOTE]
> ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਤੋਂ ਕੋਈ ਸੂਚੀ ਹੈ, ਤਾਂ ਬੱਸ ਇਸਨੂੰ ਉਨ੍ਹਾਂ ਹੀ ਮਾਰਕਰਾਂ ਨਾਲ ਲਪੇਟੋ। ਅਗਲਾ ਰਨ ਇਸਨੂੰ ਨਵੀਨਤਮ ਐੱਦ੍ਹਾਰਿਤ ਸਮੱਗਰੀ ਨਾਲ ਬਦਲ ਦੇਵੇਗਾ।

---

## ਗਲੋਬਲ ਸਮੱਗਰੀ ਕਿਵੇਂ ਬਦਲੋ

ਜੇ ਤੁਸੀਂ ਸਾਰੇ Beginners ਰਿਪੋਜ਼ ਵਿੱਚ ਜੋ ਮਿਆਰੀਕ੍ਰਿਤ ਸਮੱਗਰੀ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ, ਉਸ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ:

1. ਟੈਂਪਲੇਟ ਸੋਧੋ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. ਆਪਣੇ ਬਦਲਾਵਾਂ ਨਾਲ Co-op Translator ਰਿਪੋ ਵਿੱਚ ਇੱਕ pull request ਖੋਲ੍ਹੋ
3. PR ਮੇਰਜ ਹੋਣ ਤੋਂ ਬਾਅਦ, Co‑op Translator ਦਾ ਵਰਜਨ ਅੱਪਡੇਟ ਹੋ ਜਾਵੇਗਾ
4. ਅਗਲੀ ਵਾਰੀ ਜਦੋਂ Co‑op Translator (CLI ਜਾਂ GitHub Action) ਕਿਸੇ ਨਿਸ਼ਚਿਤ ਰਿਪੋ ਵਿੱਚ ਚਲੇਗਾ, ਤਾਂ ਇਹ ਅੱਪਡੇਟ ਕੀਤਾ ਭਾਗ ਆਪਣੇ ਆਪ ਸਿੰਕ ਹੋ ਜਾਵੇਗਾ

ਇਹ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਸਾਰੇ Beginners ਰਿਪੋਜ਼ ਵਿੱਚ "ਦੂਜੇ ਕੋਰਸ" ਦੀ ਸਮੱਗਰੀ ਲਈ ਇਕੋ ਸੱਚਾਈ ਦਾ ਸਰੋਤ ਹੈ।

## ਰਿਪੋ ਦਾ ਆਕਾਰ

ਰਿਪੋ ਬਹੁਤ ਵੱਡੇ ਹੋ ਸਕਦੇ ਹਨ ਕਿਉਂਕਿ ਬਹੁਤ ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜੋ ਅੰਤ ਉਪਭੋਗਤਿਆਂ ਨੂੰ ਮਦਦ ਕਰਨ ਲਈ ਹੁੰਦਾ ਹੈ ਕਿ ਕਿਵੇਂ clone - sparse ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਿਰਫ਼ ਜ਼ਰੂਰੀ ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਕਲੋਨ ਕੀਤਾ ਜਾਵੇ ਅਤੇ ਪੂਰਾ ਰਿਪੋ ਨਾ ਕਲੋਨ ਕੀਤਾ ਜਾਵੇ

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
**ਅਸਵੀਕਾਰੋਕਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰੱਥਾ ਹੋ ਸਕਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->