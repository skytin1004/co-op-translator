# Поддерживаемые языки

В таблице ниже перечислены языки, поддерживаемые на данный момент **Co-op Translator**. В ней указаны коды языков, названия языков и известные проблемы, связанные с каждым языком. Если вы хотите добавить поддержку нового языка, пожалуйста, добавьте соответствующий код языка, название и подходящий шрифт в файл `font_language_mappings.yml`, расположенный по адресу `src/co_op_translator/fonts/`, и отправьте pull request после тестирования.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Английский           | NotoSans-Medium.ttf               | No          | No           |
| fr            | Французский          | NotoSans-Medium.ttf               | No          | No           |
| es            | Испанский            | NotoSans-Medium.ttf               | No          | No           |
| de            | Немецкий             | NotoSans-Medium.ttf               | No          | No           |
| ru            | Русский              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Арабский             | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Персидский (фарси)   | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | Урду                 | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh-CN         | Китайский (упрощённый)| NotoSansCJK-Medium.ttc           | No          | No           |
| zh-MO         | Китайский (традиционный, Макао) | NotoSansCJK-Medium.ttc  | No          | No           |
| zh-HK         | Китайский (традиционный, Гонконг) | NotoSansCJK-Medium.ttc | No          | No           |
| zh-TW         | Китайский (традиционный, Тайвань) | NotoSansCJK-Medium.ttc  | No          | No           |
| ja            | Японский             | NotoSansCJK-Medium.ttc           | No          | No           |
| ko            | Корейский            | NotoSansCJK-Medium.ttc           | No          | No           |
| hi            | Хинди                | NotoSansDevanagari-Medium.ttf    | No          | No           |
| bn            | Бенгальский          | NotoSansBengali-Medium.ttf       | No          | No           |
| mr            | Маратхи              | NotoSansDevanagari-Medium.ttf    | No          | No           |
| ne            | Непальский           | NotoSansDevanagari-Medium.ttf    | No          | No           |
| pa            | Панджаби (гурмукхи)  | NotoSansGurmukhi-Medium.ttf      | No          | No           |
| pt-PT         | Португальский (Португалия)| NotoSans-Medium.ttf           | No          | No           |
| pt-BR         | Португальский (Бразилия)| NotoSans-Medium.ttf            | No          | No           |
| it            | Итальянский          | NotoSans-Medium.ttf               | No          | No           |
| lt            | Литовский            | NotoSans-Medium.ttf               | No          | No           |
| pl            | Польский             | NotoSans-Medium.ttf               | No          | No           |
| tr            | Турецкий             | NotoSans-Medium.ttf               | No          | No           |
| el            | Греческий            | NotoSans-Medium.ttf               | No          | No           |
| th            | Тайский              | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Шведский             | NotoSans-Medium.ttf               | No          | No           |
| da            | Датский              | NotoSans-Medium.ttf               | No          | No           |
| no            | Норвежский           | NotoSans-Medium.ttf               | No          | No           |
| fi            | Финский              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Нидерландский        | NotoSans-Medium.ttf               | No          | No           |
| he            | Иврит                | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Вьетнамский          | NotoSans-Medium.ttf               | No          | No           |
| id            | Индонезийский        | NotoSans-Medium.ttf               | No          | No           |
| ms            | Малайский            | NotoSans-Medium.ttf               | No          | No           |
| tl            | Тагальский (филиппинский) | NotoSans-Medium.ttf          | No          | No           |
| sw            | Свахили              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Венгерский           | NotoSans-Medium.ttf               | No          | No           |
| cs            | Чешский              | NotoSans-Medium.ttf               | No          | No           |
| sk            | Словацкий            | NotoSans-Medium.ttf               | No          | No           |
| ro            | Румынский            | NotoSans-Medium.ttf               | No          | No           |
| bg            | Болгарский           | NotoSans-Medium.ttf               | No          | No           |
| sr            | Сербский (кириллица) | NotoSans-Medium.ttf               | No          | No           |
| hr            | Хорватский           | NotoSans-Medium.ttf               | No          | No           |
| sl            | Словенский           | NotoSans-Medium.ttf               | No          | No           |
| uk            | Украинский           | NotoSans-Medium.ttf               | No          | No           |
| my            | Бирманский (Мьянма)  | NotoSansMyanmar-Medium.ttf        | No          | No           |
| ta            | Тамильский           | NotoSansTamil-Medium.ttf          | No          | No           |
| et            | Эстонский            | NotoSans-Medium.ttf               | No          | No           |
| pcm           | Нигерийский пиджин   | NotoSans-Medium.ttf               | No          | No           |
| te            | Телугу               | NotoSans-Medium.ttf               | No          | No           |
| ml            | Малаялам             | NotoSans-Medium.ttf               | No          | No           |
| kn            | Каннада              | NotoSans-Medium.ttf               | No          | No           |
| km            | Кхмерский            | NotoSansKhmer-Medium.ttf          | No          | No           |

## Добавление нового языка

Хотите добавить новый язык? Пожалуйста, следуйте руководству по внесению изменений:

- См. раздел Contributing: [Contribute a new language](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Данный документ был переведен с помощью сервиса искусственного интеллекта [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши стремления к точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или искажения, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->