# "Diğer Kurslar" bölümünü güncelle (Microsoft Yeni Başlayanlar depoları)

Bu kılavuz, "Diğer Kurslar" bölümünün Co‑op Translator kullanılarak otomatik olarak nasıl senkronize edileceğini ve tüm depolar için genel şablonun nasıl güncelleneceğini açıklar.

- Geçerlidir: Sadece Microsoft Yeni Başlayanlar depoları için
- Şu araçlarla çalışır: Co‑op Translator CLI ve GitHub Actions
- Şablon kaynağı: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hızlı başlangıç: Depoda otomatik senkronizasyonu etkinleştirin

README dosyanızdaki "Diğer Kurslar" bölümü etrafına aşağıdaki işaretleyicileri ekleyin. Co‑op Translator, bu işaretleyiciler arasındaki her şeyi her çalıştırmada değiştirecektir.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator her çalıştırıldığında — CLI (örneğin, `translate -l "<language codes>"`) veya GitHub Actions aracılığıyla — bu işaretleyiciler arasında yer alan "Diğer Kurslar" bölümünü otomatik olarak günceller.

> [!NOTE]
> Zaten bir listeniz varsa, sadece aynı işaretleyicilerle sarın. Sonraki çalıştırma, bunu en güncel standartlaştırılmış içerikle değiştirecektir.

---

## Genel içeriği nasıl değiştirirsiniz

Tüm Yeni Başlayanlar depolarında görünen standartlaştırılmış içeriği güncellemek isterseniz:

1. Şablonu düzenleyin: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Değişikliklerinizle birlikte Co-op Translator deposuna bir pull request açın
3. PR kabul edildikten sonra, Co‑op Translator sürümü güncellenecektir
4. Hedef depoda Co‑op Translator (CLI veya GitHub Action) bir sonraki çalıştırıldığında, güncellenen bölüm otomatik olarak senkronize edilecektir

Bu, tüm Yeni Başlayanlar depoları arasında "Diğer Kurslar" içeriği için tek bir doğruluk kaynağı sağlar.


## Depo Boyutları

Depolar, çeviri yapılan dil sayısı nedeniyle büyük hale gelebilir; son kullanıcılara yalnızca gerekli dilleri klonlamak ve tüm depoyu değil, clone - sparse nasıl kullanacaklarını göstermek için rehberlik sağlar.

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
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->