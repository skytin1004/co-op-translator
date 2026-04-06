# Japanischer Modus: Markdown-Tokens streng beibehalten

Regeln (müssen befolgt werden):
1) Markdown-Links exakt beibehalten: [Text](../../../../../../src/co_op_translator/templates/language/URL) -> [übersetzter Text](../../../../../../src/co_op_translator/templates/language/gleiche URL).
2) Links niemals als reinen Text umschreiben (z. B. 「Text」（URL）, Text (URL)).
3) Nur den Linktext übersetzen; Markdown-Struktur und URL unverändert lassen.
4) Keine 「」 um einen Markdown-Link setzen, es sei denn, es verlangt die Grammatik außerhalb des Links.

STRUKTUR IST WICHTIGER ALS STIL.
Japanische Natürlichkeit nicht optimieren, wenn sich dadurch Markdown-Tokens ändern würden.

Beispiel
Quelle: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Korrekt: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Falsch: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->