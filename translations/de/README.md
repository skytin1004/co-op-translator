# Co-op Translator

_Ergänzen Sie problemlos automatisierte Übersetzungen und pflegen Sie diese für Ihre pädagogischen GitHub-Inhalte in mehreren Sprachen, während sich Ihr Projekt weiterentwickelt._

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
[Arabisch](../ar/README.md) | [Bengalisch](../bn/README.md) | [Bulgarisch](../bg/README.md) | [Birmanisch (Myanmar)](../my/README.md) | [Chinesisch (vereinfacht)](../zh-CN/README.md) | [Chinesisch (traditionell, Hongkong)](../zh-HK/README.md) | [Chinesisch (traditionell, Macau)](../zh-MO/README.md) | [Chinesisch (traditionell, Taiwan)](../zh-TW/README.md) | [Kroatisch](../hr/README.md) | [Tschechisch](../cs/README.md) | [Dänisch](../da/README.md) | [Niederländisch](../nl/README.md) | [Estnisch](../et/README.md) | [Finnisch](../fi/README.md) | [Französisch](../fr/README.md) | [Deutsch](./README.md) | [Griechisch](../el/README.md) | [Hebräisch](../he/README.md) | [Hindi](../hi/README.md) | [Ungarisch](../hu/README.md) | [Indonesisch](../id/README.md) | [Italienisch](../it/README.md) | [Japanisch](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreanisch](../ko/README.md) | [Litauisch](../lt/README.md) | [Malaiisch](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisch](../ne/README.md) | [Nigerianisches Pidgin](../pcm/README.md) | [Norwegisch](../no/README.md) | [Persisch (Farsi)](../fa/README.md) | [Polnisch](../pl/README.md) | [Portugiesisch (Brasilien)](../pt-BR/README.md) | [Portugiesisch (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänisch](../ro/README.md) | [Russisch](../ru/README.md) | [Serbisch (Kyrillisch)](../sr/README.md) | [Slowakisch](../sk/README.md) | [Slowenisch](../sl/README.md) | [Spanisch](../es/README.md) | [Suaheli](../sw/README.md) | [Schwedisch](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändisch](../th/README.md) | [Türkisch](../tr/README.md) | [Ukrainisch](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisch](../vi/README.md)

> **Möchten Sie lieber lokal klonen?**
>
> Dieses Repository enthält über 50 Sprachübersetzungen, was die Downloadgröße erheblich erhöht. Um ohne Übersetzungen zu klonen, verwenden Sie Sparse Checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Dies gibt Ihnen alles, was Sie benötigen, um den Kurs mit viel schnellerem Download abzuschließen.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Übersicht

**Co-op Translator** hilft Ihnen, Ihre pädagogischen GitHub-Inhalte mühelos in mehrere Sprachen zu lokalisieren.
Wenn Sie Ihre Markdown-Dateien, Bilder oder Notebooks aktualisieren, bleiben die Übersetzungen automatisch synchronisiert, sodass Ihre Inhalte für Lernende weltweit genau und aktuell bleiben.

Beispiel, wie übersetzte Inhalte organisiert sind:

![Example](../../imgs/translation-ex.png)

## Wie der Übersetzungsstatus verwaltet wird

Co-op Translator verwaltet übersetzte Inhalte als **versionierte Software-Artefakte**,  
nicht als statische Dateien.

Das Tool verfolgt den Status von übersetztem Markdown, Bildern und Notebooks
mithilfe von **sprachenspezifischen Metadaten**.

Dieses Design erlaubt Co-op Translator:

- Veraltete Übersetzungen zuverlässig zu erkennen
- Markdown, Bilder und Notebooks einheitlich zu behandeln
- Sicher in großen, schnelllebigen mehrsprachigen Repositories zu skalieren

Indem Übersetzungen als verwaltete Artefakte modelliert werden,
passen Übersetzungs-Workflows natürlich zu modernen
Software-Dependency- und Artefaktmanagement-Praktiken.

→ [Wie der Übersetzungsstatus verwaltet wird](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Schnellstart

```bash
# Erstellen und aktivieren Sie eine virtuelle Umgebung (empfohlen)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installieren Sie das Paket
pip install co-op-translator
# Übersetzen
translate -l "ko ja fr" -md
```

Docker:

```bash
# Ziehen Sie das öffentliche Image von GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Führen Sie es mit dem aktuellen Ordner gemountet und .env bereitgestellt aus (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimale Einrichtung

1. Stellen Sie sicher, dass Sie eine unterstützte Python-Version haben (aktuell 3.10-3.12). In poetry (pyproject.toml) wird dies automatisch gehandhabt.
2. Erstellen Sie eine `.env`-Datei mit der Vorlage: [.env.template](../../.env.template)
3. Konfigurieren Sie einen LLM-Anbieter (Azure OpenAI oder OpenAI)
4. (Optional) Für Bildübersetzungen (`-img`), konfigurieren Sie Azure AI Vision
5. (Optional) Sie können mehrere Anmeldedatensätze konfigurieren, indem Sie Variablen mit Suffixen wie `_1`, `_2` usw. duplizieren. Alle Variablen eines Satzes müssen denselben Suffix haben.
6. (Empfohlen) Bereinigen Sie frühere Übersetzungen, um Konflikte zu vermeiden (z.B. `translations/`)
7. (Empfohlen) Fügen Sie einen Übersetzungsabschnitt in Ihr README mit der [README Sprachvorlage](./getting_started/README_languages_template.md) hinzu
8. Siehe: [Azure AI einrichten](./getting_started/set-up-azure-ai.md)

## Nutzung

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

Weitere Optionen: [Befehlsreferenz](./getting_started/command-reference.md)

## Features

- Automatische Übersetzung für Markdown, Notebooks und Bilder
- Hält Übersetzungen synchron mit Quelländerungen
- Funktioniert lokal (CLI) oder in CI (GitHub Actions)
- Verwendet Azure OpenAI oder OpenAI; optional Azure AI Vision für Bilder
- Bewahrt Markdown-Formatierung und -Struktur

## Dokumentation

- [Kommandozeilenanleitung](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions Anleitung (öffentliche Repositories & Standard-Geheimnisse)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions Anleitung (Microsoft Organisations-Repositories & org-weite Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README-Sprachvorlage](./getting_started/README_languages_template.md)
- [Unterstützte Sprachen](./getting_started/supported-languages.md)
- [Beitragen](./CONTRIBUTING.md)
- [Fehlerbehebung](./getting_started/troubleshooting.md)

### Microsoft-spezifische Anleitung
> [!NOTE]
> Nur für Betreuer der Microsoft „Für Anfänger“-Repositories.

- [Aktualisierung der Liste „andere Kurse“ (nur für MS Anfänger Repositories)](./getting_started/update-other-courses.md)

## Unterstützen Sie uns und fördern Sie globales Lernen

Begleiten Sie uns bei der Revolutionierung der globalen Verbreitung von Bildung! Geben Sie [Co-op Translator](https://github.com/azure/co-op-translator) ein ⭐ auf GitHub und unterstützen Sie unsere Mission, Sprachbarrieren im Lernen und in der Technologie abzubauen. Ihr Interesse und Ihre Beiträge bewirken viel! Codebeiträge und Funktionsvorschläge sind stets willkommen.

### Entdecken Sie Microsoft-Schulinhalte in Ihrer Sprache

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

👉 Klicken Sie unten auf das Bild, um YouTube anzusehen.

- **Open at Microsoft**: Eine kurze 18-minütige Einführung und Schnellstartanleitung, wie man Co-op Translator verwendet.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Interessiert an einer Mitarbeit am Azure Co-op Translator? Bitte lesen Sie unsere [CONTRIBUTING.md](./CONTRIBUTING.md) für Richtlinien, wie Sie Co-op Translator zugänglicher machen können.

## Mitwirkende
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen.  
Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder  
kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Verantwortungsvolle KI

Microsoft engagiert sich dafür, unseren Kunden zu helfen, unsere KI-Produkte verantwortungsvoll einzusetzen, unsere Erkenntnisse zu teilen und vertrauensbasierte Partnerschaften durch Tools wie Transparency Notes und Impact Assessments aufzubauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).  
Der Ansatz von Microsoft zur verantwortungsvollen KI basiert auf unseren KI-Prinzipien Fairness, Zuverlässigkeit und Sicherheit, Datenschutz und Sicherheit, Inklusivität, Transparenz und Verantwortlichkeit.

Groß angelegte Modelle für natürliche Sprache, Bild und Sprache – wie die in diesem Beispiel verwendeten – können potenziell auf unfaire, unzuverlässige oder anstößige Weise reagieren und dadurch Schäden verursachen. Bitte konsultieren Sie die [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um über Risiken und Einschränkungen informiert zu sein.

Der empfohlene Ansatz zur Minderung dieser Risiken besteht darin, in Ihrer Architektur ein Sicherheitssystem zu integrieren, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzschicht, die schädliche von Nutzern oder KI generierte Inhalte in Anwendungen und Diensten erkennen kann. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie potenziell schädliches Material erkennen können. Wir bieten außerdem ein interaktives Content Safety Studio, mit dem Sie Beispielcode zur Erkennung schädlicher Inhalte über verschiedene Modalitäten hinweg ansehen, erkunden und ausprobieren können. Die folgende [Quickstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch die Nutzung des Dienstes.

Ein weiterer Aspekt, den Sie berücksichtigen sollten, ist die Gesamtleistung der Anwendung. Bei multimodalen und multimodellbasierten Anwendungen verstehen wir unter Leistung, dass das System so funktioniert, wie Sie und Ihre Nutzer es erwarten, einschließlich darin, keine schädlichen Ausgaben zu generieren. Es ist wichtig, die Leistung Ihrer gesamten Anwendung anhand von [Qualitäts- und Risiko- und Sicherheitsmetriken für Generierungen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) evaluieren. Basierend auf einem Testdatensatz oder einem Ziel können Ihre generativen KI-Ergebnisse quantitativ mit integrierten Evaluatoren oder benutzerdefinierten Evaluatoren Ihrer Wahl gemessen werden. Um mit dem prompt flow SDK zur Evaluierung Ihres Systems zu beginnen, können Sie der [Quickstart-Anleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nachdem Sie einen Evaluierungslauf ausgeführt haben, können Sie [die Ergebnisse in Azure AI Studio visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marken

Dieses Projekt kann Marken oder Logos von Projekten, Produkten oder Diensten enthalten. Die autorisierte Nutzung von Microsoft-Marken oder Logos unterliegt den  
[Microsoft Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Die Verwendung von Microsoft-Marken oder Logos in modifizierten Versionen dieses Projekts darf keine Verwirrung stiften oder eine Microsoft-Unterstützung suggerieren.  
Die Nutzung von Marken oder Logos Dritter unterliegt den jeweiligen Richtlinien dieser Drittanbieter.

## Hilfe erhalten

Wenn Sie nicht weiterkommen oder Fragen zum Erstellen von KI-Apps haben, treten Sie bei:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Wenn Sie Produkt-Feedback oder Fehler beim Erstellen melden möchten, besuchen Sie:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das ursprüngliche Dokument in seiner Originalsprache ist als maßgebliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->