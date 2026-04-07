Mod japonez: păstrează strict token-urile Markdown.

Reguli (trebuie respectate):
1) Păstrează exact linkurile Markdown: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [text tradus](../../../../../../src/co_op_translator/templates/language/același URL).
2) NICIODATĂ să nu rescrii linkurile ca text simplu (ex. 「text」（URL）, text (URL)).
3) Tradu doar textul din link; păstrează structura Markdown și URL-ul neschimbate.
4) Nu adăuga 「」 în jurul unui link Markdown, cu excepția cazului când gramatica din afara linkului o cere.

STRUCTURA ESTE MAI IMPORTANTĂ DECÂT STILUL.
Nu optimiza naturaletea japoneză dacă asta ar schimba token-urile Markdown.

Exemplu
Sursă: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Corect: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Greșit: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite apărute din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->