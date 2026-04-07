# Sasisha sehemu ya "Kozi Nyingine" (Repositories za Microsoft Beginners)

Mwongozo huu unaeleza jinsi ya kufanya sehemu ya "Kozi Nyingine" iendane moja kwa moja kwa kutumia Co-op Translator, na jinsi ya kusasisha kiolezo cha ulimwengu kwa repositories zote.

- Inatumika kwa: Repositories za Microsoft Beginners pekee
- Inafanya kazi na: Co-op Translator CLI na GitHub Actions
- Chanzo cha kiolezo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Anza haraka: Weka uoanishaji wa moja kwa moja katika repo yako

Ongeza alama zifuatazo kuzunguka sehemu ya "Kozi Nyingine" katika README yako. Co-op Translator itabadilisha kila kitu kilicho kati ya alama hizi kila mara inapoendesha.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kila mara Co-op Translator inapoendesha—kupitia CLI (mfano, `translate -l "<language codes>"`) au GitHub Actions—inasasisha sehemu ya "Kozi Nyingine" iliyozungushwa na alama hizi kiotomatiki.

> [!NOTE]
> Ikiwa una orodha iliyopo tayari, fonyesha tu kwa alama zile zile. Ukurasa unaofuata utaitafuta na kuiweka na maudhui yaliyoboreshwa ya kiwango cha juu.

---

## Jinsi ya kubadilisha maudhui ya ulimwengu

Ikiwa ungependa kusasisha maudhui ya kiwango cha juu yanayoonekana katika repositories zote za Beginners:

1. Hariri kiolezo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Fungua pull request kwenda repo ya Co-op Translator na mabadiliko yako
3. Baada ya PR kuunganishwa, toleo la Co-op Translator litasasishwa
4. Mara nyingine Co-op Translator itakapochukua hatua (CLI au GitHub Action) katika repo lengwa, itauoanisha sehemu iliyosasishwa kiotomatiki

Hii inahakikisha chanzo kimoja cha ukweli kwa maudhui ya "Kozi Nyingine" katika repositories zote za Beginners.


## Ukubwa wa Repos

Repositories zinaweza kuwa kubwa kwa sababu ya idadi ya lugha zinazotafsiriwa kusaidia watumiaji wa mwisho kwa kutoa mwongozo juu ya jinsi ya kutumia clone - sparse ili kunakili tu lugha muhimu na siyo repository nzima

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
**Angalizo**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Nyaraka ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba dhamana yoyote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->