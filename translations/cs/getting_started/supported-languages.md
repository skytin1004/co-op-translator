# Podporované jazyky

Tabulka níže uvádí jazyky aktuálně podporované **Co-op Translator**. Obsahuje kódy jazyků, názvy jazyků a případné známé problémy spojené s každým jazykem. Pokud byste chtěli přidat podporu pro nový jazyk, přidejte příslušný kód jazyka, název a vhodné písmo do souboru `font_language_mappings.yml` umístěného v `src/co_op_translator/fonts/` a po otestování odešlete pull request.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Angličtina           | NotoSans-Medium.ttf               | Ne          | Ne           |
| fr            | Francouzština        | NotoSans-Medium.ttf               | Ne          | Ne           |
| es            | Španělština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| de            | Němčina              | NotoSans-Medium.ttf               | Ne          | Ne           |
| ru            | Ruština              | NotoSans-Medium.ttf               | Ne          | Ne           |
| ar            | Arabština            | NotoSansArabic-Medium.ttf         | Ano         | Ne           |
| fa            | Perština (Farsi)     | NotoSansArabic-Medium.ttf         | Ano         | Ne           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Ano         | Ne           |
| zh-CN         | Čínština (zjednodušená) | NotoSansCJK-Medium.ttc         | Ne          | Ne           |
| zh-MO         | Čínština (tradiční, Macao) | NotoSansCJK-Medium.ttc      | Ne          | Ne           |
| zh-HK         | Čínština (tradiční, Hongkong) | NotoSansCJK-Medium.ttc  | Ne          | Ne           |
| zh-TW         | Čínština (tradiční, Tchaj-wan) | NotoSansCJK-Medium.ttc   | Ne          | Ne           |
| ja            | Japonština           | NotoSansCJK-Medium.ttc            | Ne          | Ne           |
| ko            | Korejština           | NotoSansCJK-Medium.ttc            | Ne          | Ne           |
| hi            | Hindština            | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| bn            | Bengálština          | NotoSansBengali-Medium.ttf        | Ne          | Ne           |
| mr            | Maráthština          | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| ne            | Nepálština           | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| pa            | Pandžábština (Gurmukhi) | NotoSansGurmukhi-Medium.ttf    | Ne          | Ne           |
| pt-PT         | Portugalština        | NotoSans-Medium.ttf               | Ne          | Ne           |
| pt-BR         | Brazilská portugalština | NotoSans-Medium.ttf             | Ne          | Ne           |
| it            | Italština            | NotoSans-Medium.ttf               | Ne          | Ne           |
| lt            | Litevština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| pl            | Polština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| tr            | Turečtina            | NotoSans-Medium.ttf               | Ne          | Ne           |
| el            | Řečtina              | NotoSans-Medium.ttf               | Ne          | Ne           |
| th            | Thajština            | NotoSansThai-Medium.ttf           | Ne          | Ne           |
| sv            | Švédština            | NotoSans-Medium.ttf               | Ne          | Ne           |
| da            | Dánština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| no            | Norština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| fi            | Finština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| nl            | Nizozemština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| he            | Hebrejština          | NotoSansHebrew-Medium.ttf         | Ano         | Ne           |
| vi            | Vietnamština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| id            | Indonéština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| ms            | Malajština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| tl            | Tagalog (filipínština) | NotoSans-Medium.ttf             | Ne          | Ne           |
| sw            | Svahilština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| hu            | Maďarština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| cs            | Čeština              | NotoSans-Medium.ttf               | Ne          | Ne           |
| sk            | Slovenština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| ro            | Rumunština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| bg            | Bulharština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| sr            | Srbština (cyrilice)  | NotoSans-Medium.ttf               | Ne          | Ne           |
| hr            | Chorvatština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| sl            | Slovinština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| uk            | Ukrajinština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| my            | Barmsko (Myanmar)    | NotoSansMyanmar-Medium.ttf        | Ne          | Ne           |
| ta            | Tamilština           | NotoSansTamil-Medium.ttf          | Ne          | Ne           |
| et            | Estonština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| pcm           | Nigerijská pidžin    | NotoSans-Medium.ttf               | Ne          | Ne           |
| te            | Telugština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| ml            | Malajalámština       | NotoSans-Medium.ttf               | Ne          | Ne           |
| kn            | Kannadština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| km            | Khmerština           | NotoSansKhmer-Medium.ttf          | Ne          | Ne           |

## Přidání nového jazyka

Máte zájem přidat nový jazyk? Postupujte podle příručky pro přispívání:

- Viz Příspěvky: [Přispět nový jazyk](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za žádné nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->