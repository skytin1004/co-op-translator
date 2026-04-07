# Co-op Translator

_Automatizza facilmente e mantieni le traduzioni per i tuoi contenuti educativi su GitHub in più lingue man mano che il tuo progetto evolve._

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

### 🌐 Supporto Multilingue

#### Supportato da [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](./README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Preferisci clonare localmente?**
>
> Questo repository include più di 50 traduzioni linguistiche che aumentano significativamente la dimensione del download. Per clonare senza le traduzioni, usa il sparse checkout:
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
> Questo ti fornisce tutto il necessario per completare il corso con un download molto più veloce.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Panoramica

**Co-op Translator** ti aiuta a localizzare senza sforzo i tuoi contenuti educativi su GitHub in più lingue.  
Quando aggiorni i tuoi file Markdown, immagini o notebook, le traduzioni restano automaticamente sincronizzate, assicurando che i tuoi contenuti siano sempre accurati e aggiornati per gli studenti in tutto il mondo.

Esempio di come il contenuto tradotto è organizzato:

![Example](../../translated_images/it/translation-ex.0c8aa6a7ee0aad2b.webp)

## Come viene gestito lo stato della traduzione

Co-op Translator gestisce il contenuto tradotto come **artifacts software versionati**,  
non come file statici.

Lo strumento traccia lo stato di Markdown, immagini e notebook tradotti  
utilizzando **metadati con campo linguistico**.

Questo design permette a Co-op Translator di:

- Rilevare in modo affidabile le traduzioni obsolete  
- Trattare coerentemente Markdown, immagini e notebook  
- Scalare in sicurezza su repository multi-lingua grandi e dinamici  

Modellando le traduzioni come artifact gestiti,  
i flussi di lavoro di traduzione si allineano naturalmente con le moderne  
pratiche di gestione delle dipendenze e degli artifact software.

→ [Come viene gestito lo stato della traduzione](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Avvio rapido

```bash
# Crea e attiva un ambiente virtuale (consigliato)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installa il pacchetto
pip install co-op-translator
# Traduci
translate -l "ko ja fr" -md
```

Docker:

```bash
# Estrai l'immagine pubblica da GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Esegui con la cartella corrente montata e .env fornito (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configurazione minimale

1. Verifica di avere una versione di Python supportata (attualmente 3.10-3.12). In poetry (pyproject.toml) questo è gestito automaticamente.  
2. Crea un file `.env` usando il modello: [.env.template](../../.env.template)  
3. Configura un provider LLM (Azure OpenAI o OpenAI)  
4. (Opzionale) Per la traduzione delle immagini (`-img`), configura Azure AI Vision  
5. (Opzionale) Puoi configurare più set di credenziali duplicando le variabili con suffissi come `_1`, `_2`, ecc. Tutte le variabili in un set devono condividere lo stesso suffisso.  
6. (Consigliato) Pulisci eventuali traduzioni precedenti per evitare conflitti (es. `translations/`)  
7. (Consigliato) Aggiungi una sezione di traduzione al tuo README usando il [template README languages](./getting_started/README_languages_template.md)  
8. Vedi: [Configurare Azure AI](./getting_started/set-up-azure-ai.md)

## Uso

Traduci tutti i tipi supportati:

```bash
translate -l "ko ja"
```

Solo Markdown:

```bash
translate -l "de" -md
```

Markdown + immagini:

```bash
translate -l "pt" -md -img
```

Solo notebook:

```bash
translate -l "zh" -nb
```

Altri flag: [Riferimento comandi](./getting_started/command-reference.md)

## Caratteristiche

- Traduzione automatica per Markdown, notebook e immagini  
- Mantiene le traduzioni sincronizzate con le modifiche alla sorgente  
- Funziona localmente (CLI) o in CI (GitHub Actions)  
- Usa Azure OpenAI o OpenAI; facoltativo Azure AI Vision per le immagini  
- Preserva la formattazione e la struttura Markdown  

## Documentazione

- [Guida da linea di comando](./getting_started/command-line-guide/command-line-guide.md)  
- [Guida GitHub Actions (repository pubblici & segreti standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Guida GitHub Actions (repository Microsoft di organizzazione & setup a livello di org)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Template README languages](./getting_started/README_languages_template.md)  
- [Lingue supportate](./getting_started/supported-languages.md)  
- [Contribuire](./CONTRIBUTING.md)  
- [Risoluzione problemi](./getting_started/troubleshooting.md)  

### Guida specifica Microsoft
> [!NOTE]
> Solo per i manutentori dei repository Microsoft “For Beginners”.

- [Aggiornare la lista “other courses” (solo per repository MS Beginners)](./getting_started/update-other-courses.md)

## Supportaci e promuovi l’apprendimento globale

Unisciti a noi nel rivoluzionare il modo in cui i contenuti educativi vengono condivisi a livello globale! Dai una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) su GitHub e sostieni la nostra missione di abbattere le barriere linguistiche nell’apprendimento e nella tecnologia. Il tuo interesse e i tuoi contributi fanno una grande differenza! Sono sempre benvenuti contributi di codice e suggerimenti per nuove funzionalità.

### Esplora i contenuti educativi Microsoft nella tua lingua

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

## Presentazioni video

👉 Clicca sull'immagine sottostante per guardare su YouTube.

- **Open at Microsoft**: Una breve introduzione di 18 minuti e guida rapida su come usare Co-op Translator.

  [![Open at Microsoft](../../translated_images/it/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuire

Questo progetto accoglie contributi e suggerimenti. Sei interessato a contribuire ad Azure Co-op Translator? Consulta il nostro [CONTRIBUTING.md](./CONTRIBUTING.md) per le linee guida su come aiutare a rendere Co-op Translator più accessibile.

## Contributors
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Codice di Condotta

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Per maggiori informazioni vedi le [FAQ sul Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/) o
contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per qualsiasi domanda o commento aggiuntivo.

## Intelligenza Artificiale Responsabile

Microsoft si impegna ad aiutare i nostri clienti a utilizzare i nostri prodotti di intelligenza artificiale in modo responsabile, condividendo le nostre esperienze e costruendo partnership basate sulla fiducia attraverso strumenti come le Note di Trasparenza e le Valutazioni d’Impatto. Molte di queste risorse sono disponibili su [https://aka.ms/RAI](https://aka.ms/RAI).
L’approccio di Microsoft all’intelligenza artificiale responsabile si basa sui nostri principi di IA: equità, affidabilità e sicurezza, privacy e protezione, inclusività, trasparenza e responsabilità.

I modelli su larga scala di linguaggio naturale, immagini e voce - come quelli usati in questo esempio - possono potenzialmente comportarsi in modi ingiusti, inaffidabili o offensivi, causando danni. Consultare la [nota di trasparenza del servizio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) per essere informati sui rischi e le limitazioni.

L’approccio raccomandato per mitigare questi rischi è includere un sistema di sicurezza nella propria architettura in grado di rilevare e prevenire comportamenti dannosi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornisce un livello indipendente di protezione, in grado di rilevare contenuti dannosi generati dagli utenti e dall’IA nelle applicazioni e nei servizi. Azure AI Content Safety include API per testo e immagini che permettono di rilevare materiale dannoso. Abbiamo anche un Content Safety Studio interattivo che consente di visualizzare, esplorare e provare codici di esempio per il rilevamento di contenuti dannosi in diverse modalità. La seguente [documentazione quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ti guida nel fare richieste al servizio.

Un altro aspetto da considerare è la performance complessiva dell’applicazione. Con applicazioni multimodali e multimodello, consideriamo la performance come la capacità del sistema di funzionare come tu e i tuoi utenti vi aspettereste, incluso non generare output dannosi. È importante valutare la performance della tua applicazione complessiva utilizzando [metriche di qualità di generazione e di rischio e sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puoi valutare la tua applicazione AI nel tuo ambiente di sviluppo utilizzando l’[SDK prompt flow](https://microsoft.github.io/promptflow/index.html). Dato un dataset di test o un obiettivo, le generazioni della tua applicazione di IA generativa vengono misurate quantitativamente con valutatori integrati o valutatori personalizzati a tua scelta. Per iniziare con l’SDK prompt flow per valutare il tuo sistema, puoi seguire la [guida quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto può contenere marchi o loghi di progetti, prodotti o servizi. L’uso autorizzato dei marchi o loghi Microsoft
è soggetto e deve seguire
[le linee guida sui Marchi e Brand di Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
L’uso dei marchi o loghi Microsoft in versioni modificate di questo progetto non deve causare confusione o implicare sponsorizzazione da parte di Microsoft.
Qualsiasi uso di marchi o loghi di terze parti è soggetto alle politiche di tali terze parti.

## Ottenere Aiuto

Se sei bloccato o hai domande sulla creazione di app AI, unisciti a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se hai feedback sul prodotto o errori durante lo sviluppo visita:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l'accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non ci assumiamo alcuna responsabilità per malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->