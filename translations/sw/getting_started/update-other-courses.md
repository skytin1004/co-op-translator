# Sasisha sehemu ya "Other Courses" (Microsoft Beginners repos)

Mwongozo huu unaelezea jinsi ya kufanya sehemu ya "Other Courses" iendane moja kwa moja kwa kutumia Co‑op Translator, na jinsi ya kusasisha kiolezo cha ulimwengu kwa repos zote.

- Inahusu: Microsoft Beginners repositories pekee
- Inafanya kazi na: Co‑op Translator CLI na GitHub Actions
- Chanzo cha kiolezo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Anza haraka: Weka auto‑sync katika repo yako

Ongeza alama zifuatazo kuzunguka sehemu ya "Other Courses" katika README yako. Co‑op Translator itabadilisha kila kitu kati ya alama hizi kila endeshaji.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kila wakati Co‑op Translator inapoendeshwa—kupitia CLI (mfano, `translate -l "<language codes>"`) au GitHub Actions—inasasisha sehemu ya "Other Courses" iliyozungushwa na alama hizi kiotomatiki.

> [!NOTE]
> Ikiwa una orodha iliyopo tayari, ingia tu ndani ya alama hizo sawa. Mara ifuatayo itapitishwa, itabadilishwa na maudhui ya kisasa yaliyosanifiwa.

---

## Jinsi ya kubadili maudhui ya ulimwengu

Kama unataka kusasisha maudhui yaliyosanifiwa yanayoonekana katika repos zote za Beginners:

1. Hariri kiolezo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Fungua pull request kwa repo ya Co-op Translator na mabadiliko yako
3. Baada PR ichanganyike, toleo la Co‑op Translator litasasishwa
4. Mara ifuatayo Co‑op Translator (CLI au GitHub Action) inapoendeshwa kwenye repo lengwa, itasawazisha sehemu iliyosasishwa kiotomatiki

Hii inahakikisha chanzo kimoja cha ukweli kwa maudhui ya "Other Courses" katika repos zote za Beginners.


## Ukubwa wa Repo

Repos zinaweza kuwa kubwa kutokana na idadi ya lugha zinazotafsiriwa kusaidia watumiaji kumwelekeza jinsi ya kutumia clone - sparse ili kunakili lugha zinazohitajika tu na siyo repo nzima

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
**Kautioni**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upotoshaji. Hati halisi katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtaalamu aliyebobea inashauriwa. Hatubeba jukumu lolote kutokana na kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->