# "Diğer Kurslar" bölümünü güncelle (Microsoft Başlangıç depoları)

Bu kılavuz, "Diğer Kurslar" bölümünün Co‑op Translator kullanarak otomatik eşzamanlanmasının nasıl yapılacağını ve tüm depolar için küresel şablonun nasıl güncelleneceğini açıklar.

- Geçerlidir: Yalnızca Microsoft Başlangıç depoları için
- Çalışır: Co‑op Translator CLI ve GitHub Actions ile
- Şablon kaynağı: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hızlı başlangıç: Depoda otomatik eşzamanlamayı etkinleştir

README dosyanızdaki "Diğer Kurslar" bölümü çevresine aşağıdaki işaretleyicileri ekleyin. Co‑op Translator her çalıştırmada bu işaretleyiciler arasındaki her şeyi değiştirecektir.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator her çalıştığında—CLI ile (örneğin `translate -l "<dil kodları>"`) veya GitHub Actions üzerinden—bu işaretleyicilerle çevrili "Diğer Kurslar" bölümünü otomatik olarak günceller.

> [!NOTE]
> Zaten bir listeniz varsa, sadece aynı işaretleyicilerle sarın. Bir sonraki çalıştırmada içerik en son standart hale getirilmiş içerikle değiştirilecektir.

---

## Küresel içeriği nasıl değiştirirsiniz

Tüm Başlangıç depolarında görünecek standart içeriği güncellemek istiyorsanız:

1. Şablonu düzenleyin: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Değişikliklerinizle birlikte Co-op Translator deposuna bir pull request açın
3. PR birleştirildikten sonra Co‑op Translator sürümü güncellenecektir
4. Hedef depoda Co‑op Translator (CLI veya GitHub Action) bir dahaki sefere çalıştığında, güncellenmiş bölüm otomatik olarak eşzamanlanacaktır

Bu, tüm Başlangıç depolarında "Diğer Kurslar" içeriği için tek bir gerçek kaynak olmasını sağlar.


## Depo Boyutları

Çevrilen dil sayısı nedeniyle depolar büyük hale gelebilir; bu da son kullanıcıya yalnızca gerekli dilleri klonlayıp tüm depoyu değil, clone - sparse kullanımına ilişkin rehberlik sağlamaya yardımcı olur.

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
**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğinin farkında olmanız önemlidir. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanımı sonucunda oluşabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->