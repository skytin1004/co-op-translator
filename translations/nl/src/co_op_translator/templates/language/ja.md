Japanse modus: Markdown-tokens strikt behouden.

Regels (moeten worden gevolgd):
1) Houd Markdown-links exact zoals ze zijn: [tekst](../../../../../../src/co_op_translator/templates/language/URL) -> [vertaalde tekst](../../../../../../src/co_op_translator/templates/language/dezelfde URL).
2) Herschrijf links NOOIT als platte tekst (bijv. 「tekst」（URL）, tekst (URL)).
3) Vertaal alleen de linktekst; behoud de Markdown-structuur en URL ongewijzigd.
4) Voeg geen 「」 toe rond een Markdown-link, tenzij de grammatica buiten de link dat vereist.

STRUCTUUR IS BELANGRIJKER DAN STIJL.
Optimaliseer de natuurlijke Japanse taal niet als dat zou leiden tot wijziging van Markdown-tokens.

Voorbeeld
Bron: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Correct: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Incorrect: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, moet u er rekening mee houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of foutieve interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->