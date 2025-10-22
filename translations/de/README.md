<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:22:20+00:00",
  "source_file": "README.md",
  "language_code": "de"
}
-->
# Co-op Translator

_Automatisieren Sie mühelos die Übersetzung Ihrer Bildungsinhalte auf GitHub in mehrere Sprachen, um ein weltweites Publikum zu erreichen._

### 🌐 Mehrsprachige Unterstützung

#### Unterstützt von [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengalisch](../bn/README.md) | [Bulgarisch](../bg/README.md) | [Birmanisch (Myanmar)](../my/README.md) | [Chinesisch (Vereinfacht)](../zh/README.md) | [Chinesisch (Traditionell, Hongkong)](../hk/README.md) | [Chinesisch (Traditionell, Macau)](../mo/README.md) | [Chinesisch (Traditionell, Taiwan)](../tw/README.md) | [Kroatisch](../hr/README.md) | [Tschechisch](../cs/README.md) | [Dänisch](../da/README.md) | [Niederländisch](../nl/README.md) | [Estnisch](../et/README.md) | [Finnisch](../fi/README.md) | [Französisch](../fr/README.md) | [Deutsch](./README.md) | [Griechisch](../el/README.md) | [Hebräisch](../he/README.md) | [Hindi](../hi/README.md) | [Ungarisch](../hu/README.md) | [Indonesisch](../id/README.md) | [Italienisch](../it/README.md) | [Japanisch](../ja/README.md) | [Koreanisch](../ko/README.md) | [Litauisch](../lt/README.md) | [Malaiisch](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerianisches Pidgin](../pcm/README.md) | [Norwegisch](../no/README.md) | [Persisch (Farsi)](../fa/README.md) | [Polnisch](../pl/README.md) | [Portugiesisch (Brasilien)](../br/README.md) | [Portugiesisch (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänisch](../ro/README.md) | [Russisch](../ru/README.md) | [Serbisch (Kyrillisch)](../sr/README.md) | [Slowakisch](../sk/README.md) | [Slowenisch](../sl/README.md) | [Spanisch](../es/README.md) | [Suaheli](../sw/README.md) | [Schwedisch](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thailändisch](../th/README.md) | [Türkisch](../tr/README.md) | [Ukrainisch](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisch](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Überblick

**Co-op Translator** ermöglicht es Ihnen, Ihre Bildungsinhalte auf GitHub schnell in mehrere Sprachen zu übersetzen und so mühelos ein weltweites Publikum zu erreichen. Wenn Sie Ihre Markdown-Dateien, Bilder oder Jupyter-Notebooks aktualisieren, werden die Übersetzungen automatisch synchronisiert, damit Ihre Bildungsinhalte auf GitHub stets aktuell und relevant für internationale Nutzer bleiben.

So organisiert Co-op Translator übersetzte Bildungsinhalte auf GitHub:

![Beispiel](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.de.png)

## Schnellstart

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimale Einrichtung

- Erstellen Sie eine `.env`-Datei mit der Vorlage: [.env.template](../../.env.template)
- Konfigurieren Sie einen LLM-Anbieter (Azure OpenAI oder OpenAI)
- Für die Übersetzung von Bildern (`-img`) richten Sie zusätzlich Azure AI Vision ein
- Empfehlung: Wenn Sie Übersetzungen haben, die mit anderen Tools erstellt wurden, bereinigen Sie diese zuerst, um Konflikte zu vermeiden (zum Beispiel: `translations/`).
- Empfehlung: Fügen Sie einen Übersetzungsbereich zu Ihrer README hinzu, indem Sie die [README-Sprachenvorlage](./README_languages_template.md) verwenden
- Siehe: [Azure AI einrichten](./getting_started/set-up-azure-ai.md)

## Verwendung

Alle unterstützten Typen übersetzen:

```bash
translate -l "ko ja"
```

Nur Markdown:

```bash
translate -l "de" -md
```

Markdown + Bilder:

```bash
translate -l "pt" -md -img
```

Nur Notebooks:

```bash
translate -l "zh" -nb
```

Weitere Optionen: [Befehlsreferenz](./getting_started/command-reference.md)

## Funktionen

- Automatisierte Übersetzung für Markdown, Notebooks und Bilder
- Hält Übersetzungen bei Änderungen an der Quelle synchron
- Funktioniert lokal (CLI) oder in CI (GitHub Actions)
- Nutzt Azure OpenAI oder OpenAI; optional Azure AI Vision für Bilder
- Erhält das Markdown-Format und die Struktur

## Dokumentation

- [Kommandozeilen-Anleitung](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions Anleitung (Öffentliche Repositories & Standard-Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions Anleitung (Microsoft-Organisation-Repositories & org-weite Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Unterstützte Sprachen](./getting_started/supported-languages.md)
- [Fehlerbehebung](./getting_started/troubleshooting.md)

## Unterstützen Sie uns und fördern Sie globales Lernen

Helfen Sie mit, die Verbreitung von Bildungsinhalten weltweit zu revolutionieren! Geben Sie [Co-op Translator](https://github.com/azure/co-op-translator) einen ⭐ auf GitHub und unterstützen Sie unsere Mission, Sprachbarrieren beim Lernen und in der Technologie abzubauen. Ihr Interesse und Ihre Beiträge machen einen großen Unterschied! Code-Beiträge und Feature-Vorschläge sind jederzeit willkommen.

### Entdecken Sie Microsoft-Bildungsinhalte in Ihrer Sprache

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video-Präsentationen

Erfahren Sie mehr über Co-op Translator in unseren Präsentationen _(Klicken Sie auf das Bild unten, um das Video auf YouTube anzusehen.)_:

- **Open at Microsoft**: Eine kurze 18-minütige Einführung und Schnellstart-Anleitung zur Nutzung von Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.de.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Sie möchten zum Azure Co-op Translator beitragen? Lesen Sie bitte unsere [CONTRIBUTING.md](./CONTRIBUTING.md) für Hinweise, wie Sie Co-op Translator noch zugänglicher machen können.

## Mitwirkende

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Verhaltenskodex

Dieses Projekt folgt dem [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder
kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Verantwortungsvolle KI

Microsoft setzt sich dafür ein, dass unsere Kunden unsere KI-Produkte verantwortungsvoll nutzen, unsere Erfahrungen teilen und vertrauensbasierte Partnerschaften durch Tools wie Transparenzhinweise und Folgenabschätzungen aufbauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts Ansatz für verantwortungsvolle KI basiert auf unseren KI-Prinzipien: Fairness, Zuverlässigkeit und Sicherheit, Datenschutz und Sicherheit, Inklusivität, Transparenz und Verantwortlichkeit.

Groß angelegte Modelle für natürliche Sprache, Bilder und Sprache – wie die in diesem Beispiel verwendeten – können sich potenziell unfair, unzuverlässig oder anstößig verhalten und dadurch Schaden verursachen. Bitte lesen Sie die [Transparenzhinweise zum Azure OpenAI-Dienst](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um sich über Risiken und Einschränkungen zu informieren.

Die empfohlene Vorgehensweise zur Risikominderung ist, ein Sicherheitssystem in Ihre Architektur zu integrieren, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzebene, die in der Lage ist, schädliche nutzergenerierte und KI-generierte Inhalte in Anwendungen und Diensten zu erkennen. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie schädliches Material erkennen können. Außerdem gibt es ein interaktives Content Safety Studio, mit dem Sie Beispielcode für die Erkennung schädlicher Inhalte in verschiedenen Modalitäten ausprobieren können. Die folgende [Schnellstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch die ersten Schritte mit dem Dienst.
Ein weiterer Aspekt, den man berücksichtigen sollte, ist die Gesamtleistung der Anwendung. Bei multimodalen und Multi-Modell-Anwendungen bedeutet Leistung, dass das System so funktioniert, wie Sie und Ihre Nutzer es erwarten – einschließlich der Vermeidung schädlicher Ausgaben. Es ist wichtig, die Leistung Ihrer gesamten Anwendung anhand von [Metriken zur Generierungsqualität sowie Risiko- und Sicherheitsmetriken](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) evaluieren. Mit einem Testdatensatz oder einem Ziel werden die Generierungen Ihrer generativen KI-Anwendung quantitativ mit integrierten oder selbst definierten Evaluatoren gemessen. Um mit dem prompt flow SDK zu starten und Ihr System zu evaluieren, können Sie der [Schnellstart-Anleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nach der Durchführung eines Evaluationslaufs können Sie [die Ergebnisse im Azure AI Studio visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marken

Dieses Projekt kann Marken oder Logos von Projekten, Produkten oder Dienstleistungen enthalten. Die autorisierte Nutzung von Microsoft-Marken oder -Logos unterliegt den [Microsoft Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) und muss diesen entsprechen.
Die Verwendung von Microsoft-Marken oder -Logos in abgeänderten Versionen dieses Projekts darf nicht zu Verwirrung führen oder eine Unterstützung durch Microsoft suggerieren.
Jegliche Nutzung von Marken oder Logos Dritter unterliegt den Richtlinien der jeweiligen Dritten.

## Hilfe erhalten

Wenn Sie nicht weiterkommen oder Fragen zum Erstellen von KI-Anwendungen haben, treten Sie bei:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Wenn Sie Produktfeedback haben oder auf Fehler beim Erstellen stoßen, besuchen Sie:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.