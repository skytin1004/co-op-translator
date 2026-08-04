Modo japonés: preservar estrictamente los tokens Markdown.

Reglas (deben seguirse):
1) Mantener los enlaces Markdown exactamente: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [texto traducido](../../../../../../src/co_op_translator/templates/language/misma URL).
2) NUNCA reescribir los enlaces como texto plano (p. ej., 「text」（URL）, text (URL)).
3) Traducir solo el texto del enlace; mantener la estructura Markdown y la URL sin cambios.
4) No agregar 「」 alrededor de un enlace Markdown a menos que la gramática externa del enlace lo requiera.

LA ESTRUCTURA ES MÁS IMPORTANTE QUE EL ESTILO.
No optimizar la naturalidad japonesa si los tokens Markdown cambiarían.

Ejemplo
Fuente: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Correcto: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Incorrecto: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->