# Co-op Translator

_Ermöglichen Sie die einfache Automatisierung und Pflege von Übersetzungen für Ihre edukativen GitHub-Inhalte in mehreren Sprachen, während Ihr Projekt sich weiterentwickelt._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Mehrsprachige Unterstützung

#### Unterstützt von [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](./README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Bevorzugen Sie die lokale Klonung?**
>
> Dieses Repository enthält über 50 Sprachübersetzungen, was die Downloadgröße erheblich erhöht. Wenn Sie ohne Übersetzungen klonen möchten, verwenden Sie sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> So erhalten Sie alles, was Sie benötigen, um den Kurs abzuschließen, mit deutlich schnellerem Download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Überblick

**Co-op Translator** hilft Ihnen, Ihre edukativen GitHub-Inhalte mühelos in mehrere Sprachen zu lokalisieren.  
Wenn Sie Ihre Markdown-Dateien, Bilder oder Notebooks aktualisieren, bleiben die Übersetzungen automatisch synchronisiert und stellen sicher, dass Ihre Inhalte für Lernende weltweit genau und aktuell bleiben.

Beispiel, wie übersetzter Inhalt organisiert ist:

![Example](../../translated_images/de/translation-ex.0c8aa6a7ee0aad2b.webp)

## Wie der Übersetzungsstatus verwaltet wird

Co-op Translator verwaltet übersetzten Inhalt als **versionierte Software-Artefakte**,  
nicht als statische Dateien.

Das Tool verfolgt den Status der übersetzten Markdown, Bilder und Notebooks  
mithilfe von **sprachspezifischen Metadaten**.

Dieses Design ermöglicht es Co-op Translator:

- Zuverlässig veraltete Übersetzungen zu erkennen  
- Markdown, Bilder und Notebooks konsistent zu behandeln  
- Sicher in großen, schnelllebigen, mehrsprachigen Repositories zu skalieren

Indem Übersetzungen als verwaltete Artefakte modelliert werden,  
richten sich Übersetzungs-Workflows natürlich an modernen  
Software-Abhängigkeits- und Artefakt-Management-Praktiken aus.

→ [Wie der Übersetzungsstatus verwaltet wird](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Schnellstart

```bash
# Erstellen und aktivieren Sie eine virtuelle Umgebung (empfohlen)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Paket installieren
pip install co-op-translator
# Übersetzen
translate -l "ko ja fr" -md
```

Docker:

```bash
# Ziehen Sie das öffentliche Image von GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Führen Sie es mit dem aktuellen Ordner als Mount und bereitgestellter .env aus (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimale Einrichtung

1. Stellen Sie sicher, dass Sie eine unterstützte Python-Version haben (derzeit 3.10-3.12). In poetry (pyproject.toml) wird dies automatisch gehandhabt.  
2. Erstellen Sie eine `.env`-Datei mit der Vorlage: [.env.template](../../.env.template)  
3. Konfigurieren Sie einen LLM-Anbieter (Azure OpenAI oder OpenAI)  
4. (Optional) Für die Bildübersetzung (`-img`) konfigurieren Sie Azure AI Vision  
5. (Optional) Sie können mehrere Anmelde-Datensätze konfigurieren, indem Sie Variablen mit Suffixen wie `_1`, `_2` usw. duplizieren. Alle Variablen in einem Satz müssen das gleiche Suffix haben.  
6. (Empfohlen) Bereinigen Sie vorherige Übersetzungen, um Konflikte zu vermeiden (z. B. `translations/`)  
7. (Empfohlen) Fügen Sie einen Übersetzungsabschnitt zu Ihrem README hinzu mit der [README Sprachvorlage](./getting_started/README_languages_template.md)  
8. Siehe: [Azure AI einrichten](./getting_started/set-up-azure-ai.md)

## Verwendung

Übersetzen Sie alle unterstützten Typen:

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

Weitere Flags: [Befehlsreferenz](./getting_started/command-reference.md)

## Funktionen

- Automatisierte Übersetzung für Markdown, Notebooks und Bilder  
- Hält Übersetzungen synchron mit Quelländerungen  
- Funktioniert lokal (CLI) oder in CI (GitHub Actions)  
- Nutzt Azure OpenAI oder OpenAI; optional Azure AI Vision für Bilder  
- Erhält Markdown-Formatierung und -Struktur

## Dokumentation

- [Kommandozeilen-Anleitung](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions Anleitung (öffentliche Repositories & Standard-Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions Anleitung (Microsoft Organisations-Repositories & organisationale Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README Sprachvorlage](./getting_started/README_languages_template.md)  
- [Unterstützte Sprachen](./getting_started/supported-languages.md)  
- [Mitwirken](./CONTRIBUTING.md)  
- [Fehlerbehebung](./getting_started/troubleshooting.md)  

### Microsoft-spezifische Anleitung
> [!NOTE]
> Nur für Betreuer der Microsoft „Für Anfänger“ Repositories.

- [Die Liste „andere Kurse“ aktualisieren (nur für MS Anfänger Repositories)](./getting_started/update-other-courses.md)

## Unterstützen Sie uns und fördern Sie globales Lernen

Schließen Sie sich uns an, um zu revolutionieren, wie edukative Inhalte weltweit geteilt werden! Geben Sie [Co-op Translator](https://github.com/azure/co-op-translator) einen ⭐ auf GitHub und unterstützen Sie unsere Mission, Sprachbarrieren im Lernen und in der Technologie zu überwinden. Ihr Interesse und Ihre Beiträge bewirken viel! Code-Beiträge und Funktionsvorschläge sind jederzeit willkommen.

### Erkunden Sie Microsoft Bildungsinhalte in Ihrer Sprache

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)  
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

👉 Klicken Sie auf das Bild unten, um es auf YouTube anzusehen.

- **Open at Microsoft**: Eine kurze 18-minütige Einführung und schnelle Anleitung zur Nutzung von Co-op Translator.

  [![Open at Microsoft](../../translated_images/de/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Möchten Sie zum Azure Co-op Translator beitragen? Bitte lesen Sie unsere [CONTRIBUTING.md](./CONTRIBUTING.md) für Richtlinien, wie Sie dazu beitragen können, Co-op Translator zugänglicher zu machen.

## Mitwirkende
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen.
Weitere Informationen finden Sie in der [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder
kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Verantwortungsbewusste KI

Microsoft engagiert sich dafür, unseren Kunden zu helfen, unsere KI-Produkte verantwortungsvoll zu nutzen, unsere Erkenntnisse zu teilen und vertrauensbasierte Partnerschaften durch Tools wie Transparenznotizen und Einflussbewertungen aufzubauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).
Der Ansatz von Microsoft zur verantwortungsvollen KI basiert auf unseren KI-Prinzipien Fairness, Zuverlässigkeit und Sicherheit, Datenschutz und Sicherheit, Inklusivität, Transparenz und Verantwortung.

Groß angelegte Modelle für natürliche Sprache, Bild und Sprache – wie die in diesem Beispiel verwendeten – können potenziell Verhaltensweisen zeigen, die unfair, unzuverlässig oder anstößig sind und dadurch Schäden verursachen. Bitte konsultieren Sie die [Transparenznotiz zum Azure OpenAI-Dienst](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um über Risiken und Einschränkungen informiert zu sein.

Der empfohlene Ansatz zur Minderung dieser Risiken besteht darin, ein Sicherheitssystem in Ihre Architektur einzubinden, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzschicht, die schädliche benutzergenerierte und KI-generierte Inhalte in Anwendungen und Diensten erkennen kann. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie schädliches Material erkennen können. Wir bieten auch ein interaktives Content Safety Studio, das es Ihnen ermöglicht, Beispielcode zur Erkennung schädlicher Inhalte über verschiedene Modalitäten hinweg anzusehen, zu erkunden und auszuprobieren. Die folgende [Schnellstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch die Anfragen an den Dienst.

Ein weiterer zu berücksichtigender Aspekt ist die Gesamtleistung der Anwendung. Bei multimodalen und multimodellbasierten Anwendungen verstehen wir unter Leistung, dass das System so arbeitet, wie Sie und Ihre Benutzer es erwarten, einschließlich der Nicht-Erzeugung schädlicher Ausgaben. Es ist wichtig, die Leistung Ihrer Gesamtanwendung mithilfe von [Generierungsqualität sowie Risiko- und Sicherheitsmetriken](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) bewerten. Anhand eines Testdatensatzes oder Ziels werden Ihre generativen KI-Ausgaben quantitativ mit integrierten Evaluatoren oder kundenspezifischen Evaluatoren Ihrer Wahl gemessen. Um mit dem prompt flow SDK zur Bewertung Ihres Systems zu beginnen, können Sie der [Schnellstartanleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nach Ausführung eines Bewertungslaufs können Sie [die Ergebnisse im Azure AI Studio visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marken

Dieses Projekt kann Marken oder Logos von Projekten, Produkten oder Diensten enthalten. Die autorisierte Nutzung von Microsoft
Marken oder Logos unterliegt und muss den
[Microsoft Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) folgen.
Die Verwendung von Microsoft-Marken oder Logos in modifizierten Versionen dieses Projekts darf keine Verwirrung stiften oder eine Microsoft-Unterstützung suggerieren.
Die Verwendung von Marken oder Logos Dritter unterliegt den jeweiligen Richtlinien dieser Drittanbieter.

## Hilfe erhalten

Wenn Sie nicht weiterkommen oder Fragen zum Erstellen von KI-Anwendungen haben, treten Sie bei:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Wenn Sie Produktfeedback haben oder beim Erstellen auf Fehler stoßen, besuchen Sie:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in der Ursprungssprache gilt als maßgebliche Quelle. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->