Přepínač režimu Čínština – Japonsko (Japonský režim) udržuje přísnou konzistenci tokenů Markdown.

Pravidla (dodržujte je):
1) Zachovejte odkazy Markdown přesně: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [přeložený text](../../../../../../src/co_op_translator/templates/language/stejný URL).
2) NIKDY nepřepisujte odkazy jako prostý text (např. 「text」（URL）, text (URL)).
3) Překládejte pouze text odkazu; zachovejte strukturu Markdown a URL beze změny.
4) Nepřidávejte 「」 kolem odkazu Markdown, pokud to nevyžaduje gramatika mimo odkaz.

STRUKTURA JE DŮLEŽITĚJŠÍ NEŽ STYL.
Nepřekládejte přirozenost japonštiny, pokud by to změnilo tokeny Markdown.

Příklad
Zdroj: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Správně: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Nesprávně: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí služeb automatického překladu AI [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro zásadní informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakákoli nedorozumění nebo nesprávné výklady vzniklé z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->