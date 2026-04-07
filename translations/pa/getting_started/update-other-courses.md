# "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਨੂੰ ਅਪਡੇਟ ਕਰੋ (Microsoft Beginners ਰੀਪੋਜ਼)

ਇਹ ਗਾਈਡ ਦੱਸਦੀ ਹੈ ਕਿ ਕਿਵੇਂ "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਨੂੰ Co-op Translator ਦੀ ਵਰਤੋਂ ਨਾਲ ਆਟੋ-ਸਿੰਕ੍ਰੋਨਾਈਜ਼ ਕੀਤਾ ਜਾਵੇ, ਅਤੇ ਸਾਰੇ ਰੀਪੋਜ਼ ਲਈ ਗਲੋਬਲ ਟੈਂਪਲੇਟ ਨੂੰ ਕਿਵੇਂ ਅਪਡੇਟ ਕਰਨਾ ਹੈ।

- ਲਾਗੂ ਹੁੰਦਾ ਹੈ: ਕੇਵਲ Microsoft Beginners ਰੀਪੋਜ਼ ਤੇ
- ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ: Co-op Translator CLI ਅਤੇ GitHub Actions ਨਾਲ
- ਟੈਂਪਲੇਟ ਸਰੋਤ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ: ਆਪਣੇ ਰੀਪੋ ਵਿੱਚ ਆਟੋ-ਸਿੰਕ ਐਨੇਬਲ ਕਰੋ

ਆਪਣੇ README ਵਿੱਚ "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਦੇ ਆਲੇ ਦੁਆਲੇ ਹੇਠ ਲਿਖੇ ਮਾਰਕਰز ਪਾਓ। Co-op Translator ਹਰ ਚਲਾਉਂਦਿਆਂ ਇਨ੍ਹਾਂ ਮਾਰਕਰਜ਼ ਵਿਚਕਾਰ ਦਿੱਤੇ ਸਮੱਗਰੀ ਨੂੰ ਬਦਲ ਦੇਵੇਗਾ।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
ਹਰ ਵਾਰੀ ਜਦੋਂ Co-op Translator ਚੱਲਦਾ ਹੈ—CLI ਰਾਹੀਂ (ਉਦਾਹਰਣ ਵਜੋਂ, `translate -l "<language codes>"`) ਜਾਂ GitHub Actions ਰਾਹੀਂ—ਇਹ ਆਪਣੇ ਆਪ "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਨੂੰ ਜੋ ਇਨ੍ਹਾਂ ਮਾਰਕਰਜ਼ ਵਿੱਚ ਬੰਨ੍ਹਿਆ ਹੋਇਆ ਹੈ ਅਪਡੇਟ ਕਰਦਾ ਹੈ।

> [!NOTE]  
> ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਕੋਈ ਸੂਚੀ ਹੈ, ਤਾਂ ਉਸਨੂੰ ਸਿਰਫ਼ ਇਨ੍ਹਾਂ ਮਾਰਕਰਜ਼ ਨਾਲ ਘਿਰੋ। ਅਗਲੀ ਵਾਰੀ ਚਲਾਉਣ 'ਤੇ ਇਹ ਇਸਨੂੰ ਤਾਜ਼ਾ ਅਤੇ ਸਟੈਂਡਰਡ ਸਾਮੱਗਰੀ ਨਾਲ ਬਦਲ ਦੇਵੇਗਾ।

---

## ਗਲੋਬਲ ਸਮੱਗਰੀ ਨੂੰ ਕਿਵੇਂ ਬਦਲਣਾ ਹੈ

ਜੇ ਤੁਸੀਂ ਸਟੈਂਡਰਡ ਸਮੱਗਰੀ ਨੂੰ ਅਪਡੇਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਸਾਰੇ Beginners ਰੀਪੋਜ਼ ਵਿੱਚ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ:

1. ਟੈਂਪਲੇਟ ਸੋਧੋ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. ਬਦਲਾਵਾਂ ਸਮੇਤ Co-op Translator ਰੀਪੋ ਲਈ ਪ੍ਰ Pull Request ਖੋਲ੍ਹੋ  
3. PR ਮਰਜ ਹੋਣ ਤੋਂ ਬਾਅਦ, Co-op Translator ਵਰਜ਼ਨ ਅਪਡੇਟ ਹੋ ਜਾਵੇਗਾ  
4. ਅਗਲੀ ਵਾਰੀ ਜਦੋਂ Co-op Translator (CLI ਜਾਂ GitHub Action) ਟਾਰਗੇਟ ਰੀਪੋ 'ਚ ਚੱਲੇਗਾ, ਇਹ ਸਵੈਚਾਲਿਤ ਤੌਰ 'ਤੇ ਅਪਡੇਟ ਕੀਤਾ ਸੈਕਸ਼ਨ ਸਿੰਕ ਕਰੇਗਾ

ਇਹ "ਹੋਰ ਕੋਰਸ" ਸਮੱਗਰੀ ਲਈ ਸਾਰੇ Beginners ਰੀਪੋਜ਼ ਵਿੱਚ ਇੱਕ ਇਕੱਲਾ ਸਚਾਈ ਦਾ ਸਰੋਤ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ।

## ਰੀਪੋ ਆਕਾਰ

ਭਾਸ਼ਾਵਾਂ ਦੀ ਗਿਣਤੀ ਵੱਧ ਜਾਣ ਕਾਰਨ ਰੀਪੋਜ਼ ਵੱਡੇ ਹੋ ਸਕਦੇ ਹਨ, ਜਿਹੜੀਆਂ ਅੰਤਿਮ ਉਪਭੋਗਤਿਆਂ ਨੂੰ ਮਦਦ ਕਰਨ ਲਈ ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। ਇਸ ਲਈ ਰੀਪੋ ਨੂੰ ਕਲੋਨ ਕਰਦੇ ਸਮੇਂ ਕੇਵਲ ਜ਼ਰੂਰੀ ਭਾਸ਼ਾਵਾਂ ਹੀ ਕਲੋਨ ਕਰਨ ਲਈ clone - sparse ਦਾ ਉਪਯੋਗ ਕਰਨ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਨਾ ਕਿ ਪੂਰੇ ਰੀਪੋ ਨੂੰ।  

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
**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਤਰਜਮੇ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੂ ਰਹੋ ਕਿ ਸਵੈਚਾਲਿਤ ਤਰਜਮੇ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਵਿਧਾਨਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਾਨਵੀ ਤਰਜਮੇ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਤਰਜਮੇ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->