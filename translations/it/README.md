<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:02:09+00:00",
  "source_file": "README.md",
  "language_code": "it"
}
-->
# Co-op Translator

_Automatizza facilmente la traduzione dei tuoi contenuti educativi su GitHub in più lingue per raggiungere un pubblico globale._

### 🌐 Supporto multilingue

#### Supportato da <a href="https://github.com/Azure/Co-op-Translator">Co-op Translator</a>

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
<a href="./translations/ar/README.md">Arabo</a> | <a href="./translations/bn/README.md">Bengalese</a> | <a href="./translations/bg/README.md">Bulgaro</a> | <a href="./translations/my/README.md">Birmano (Myanmar)</a> | <a href="./translations/zh/README.md">Cinese (semplificato)</a> | <a href="./translations/hk/README.md">Cinese (tradizionale, Hong Kong)</a> | <a href="./translations/mo/README.md">Cinese (tradizionale, Macao)</a> | <a href="./translations/tw/README.md">Cinese (tradizionale, Taiwan)</a> | <a href="./translations/hr/README.md">Croato</a> | <a href="./translations/cs/README.md">Ceco</a> | <a href="./translations/da/README.md">Danese</a> | <a href="./translations/nl/README.md">Olandese</a> | <a href="./translations/et/README.md">Estone</a> | <a href="./translations/fi/README.md">Finlandese</a> | <a href="./translations/fr/README.md">Francese</a> | <a href="./translations/de/README.md">Tedesco</a> | <a href="./translations/el/README.md">Greco</a> | <a href="./translations/he/README.md">Ebraico</a> | <a href="./translations/hi/README.md">Hindi</a> | <a href="./translations/hu/README.md">Ungherese</a> | <a href="./translations/id/README.md">Indonesiano</a> | <a href="./translations/it/README.md">Italiano</a> | <a href="./translations/ja/README.md">Giapponese</a> | <a href="./translations/ko/README.md">Coreano</a> | <a href="./translations/lt/README.md">Lituano</a> | <a href="./translations/ms/README.md">Malese</a> | <a href="./translations/mr/README.md">Marathi</a> | <a href="./translations/ne/README.md">Nepalese</a> | <a href="./translations/pcm/README.md">Pidgin nigeriano</a> | <a href="./translations/no/README.md">Norvegese</a> | <a href="./translations/fa/README.md">Persiano (Farsi)</a> | <a href="./translations/pl/README.md">Polacco</a> | <a href="./translations/br/README.md">Portoghese (Brasile)</a> | <a href="./translations/pt/README.md">Portoghese (Portogallo)</a> | <a href="./translations/pa/README.md">Punjabi (Gurmukhi)</a> | <a href="./translations/ro/README.md">Romeno</a> | <a href="./translations/ru/README.md">Russo</a> | <a href="./translations/sr/README.md">Serbo (Cirillico)</a> | <a href="./translations/sk/README.md">Slovacco</a> | <a href="./translations/sl/README.md">Sloveno</a> | <a href="./translations/es/README.md">Spagnolo</a> | <a href="./translations/sw/README.md">Swahili</a> | <a href="./translations/sv/README.md">Svedese</a> | <a href="./translations/tl/README.md">Tagalog (Filippino)</a> | <a href="./translations/ta/README.md">Tamil</a> | <a href="./translations/th/README.md">Thailandese</a> | <a href="./translations/tr/README.md">Turco</a> | <a href="./translations/uk/README.md">Ucraino</a> | <a href="./translations/ur/README.md">Urdu</a> | <a href="./translations/vi/README.md">Vietnamita</a>
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Panoramica

**Co-op Translator** ti permette di tradurre rapidamente i tuoi contenuti educativi su GitHub in più lingue, raggiungendo facilmente utenti da tutto il mondo. Quando aggiorni i tuoi file Markdown, immagini o notebook Jupyter, le traduzioni vengono sincronizzate automaticamente per mantenere i tuoi contenuti sempre aggiornati e rilevanti per gli utenti internazionali.

Ecco come Co-op Translator organizza i contenuti educativi tradotti su GitHub:

<img src="../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.it.png" alt="Esempio">

## Avvio rapido

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

## Configurazione minima

- Crea un file `.env` usando il modello: [.env.template](../../.env.template)
- Configura un provider LLM (Azure OpenAI oppure OpenAI)
- Per la traduzione delle immagini (`-img`), configura anche Azure AI Vision
- Consigliato: Se hai traduzioni generate da altri strumenti, puliscile prima per evitare conflitti (ad esempio: `translations/`).
- Consigliato: Aggiungi una sezione traduzioni al tuo README usando il [modello README lingue](./README_languages_template.md)
- Vedi: [Configura Azure AI](./getting_started/set-up-azure-ai.md)

## Utilizzo

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

Altre opzioni: [Riferimento comandi](./getting_started/command-reference.md)

## Funzionalità

- Traduzione automatica di Markdown, notebook e immagini
- Mantiene le traduzioni sincronizzate con le modifiche alla fonte
- Funziona in locale (CLI) o in CI (GitHub Actions)
- Utilizza Azure OpenAI o OpenAI; opzionale Azure AI Vision per le immagini
- Preserva la formattazione e la struttura del Markdown

## Documentazione

- [Guida da riga di comando](./getting_started/command-line-guide/command-line-guide.md)
- [Guida GitHub Actions (Repository pubblici & segreti standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guida GitHub Actions (Repository organizzazione Microsoft & configurazioni a livello di organizzazione)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Lingue supportate](./getting_started/supported-languages.md)
- [Risoluzione dei problemi](./getting_started/troubleshooting.md)

## Sostienici e promuovi l'apprendimento globale

Unisciti a noi per rivoluzionare la condivisione dei contenuti educativi a livello globale! Dai una ⭐ a <a href="https://github.com/azure/co-op-translator">Co-op Translator</a> su GitHub e sostieni la nostra missione di abbattere le barriere linguistiche nell'apprendimento e nella tecnologia. Il tuo interesse e i tuoi contributi fanno davvero la differenza! Sono sempre benvenuti suggerimenti e contributi al codice.

### Esplora i contenuti educativi Microsoft nella tua lingua

- <a href="https://github.com/microsoft/AZD-for-beginners">AZD for Beginners</a>
- <a href="https://github.com/microsoft/edgeai-for-beginners">Edge AI for Beginners</a>
- <a href="https://github.com/microsoft/mcp-for-beginners">Model Context Protocol (MCP) For Beginners</a>
- <a href="https://github.com/microsoft/ai-agents-for-beginners">AI Agents for Beginners</a>
- <a href="https://github.com/microsoft/Generative-AI-for-beginners-dotnet">Generative AI for Beginners using .NET</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners">Generative AI for Beginners</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners-java">Generative AI for Beginners using Java</a>
- <a href="https://aka.ms/ml-beginners">ML for Beginners</a>
- <a href="https://aka.ms/datascience-beginners">Data Science for Beginners</a>
- <a href="https://aka.ms/ai-beginners">AI for Beginners</a>
- <a href="https://github.com/microsoft/Security-101">Cybersecurity for Beginners</a>
- <a href="https://aka.ms/webdev-beginners">Web Dev for Beginners</a>
- <a href="https://aka.ms/iot-beginners">IoT for Beginners</a>
- <a href="https://github.com/microsoft/PhiCookBook">PhiCookBook</a>

## Presentazioni video

Scopri di più su Co-op Translator attraverso le nostre presentazioni _(Clicca sull'immagine qui sotto per guardare su YouTube.)_:

- **Open at Microsoft**: Una breve introduzione di 18 minuti e guida rapida su come usare Co-op Translator.

  <a href="https://www.youtube.com/watch?v=jX_swfH_KNU"><img src="../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.it.jpg" alt="Open at Microsoft"></a>

## Contribuire

Questo progetto accoglie contributi e suggerimenti. Vuoi contribuire ad Azure Co-op Translator? Consulta il nostro [CONTRIBUTING.md](./CONTRIBUTING.md) per le linee guida su come rendere Co-op Translator più accessibile.

## Collaboratori

<a href="https://github.com/Azure/co-op-translator/graphs/contributors"><img src="https://contrib.rocks/image?repo=Azure/co-op-translator" alt="co-op-translator contributors"></a>

## Codice di condotta

Questo progetto ha adottato il <a href="https://opensource.microsoft.com/codeofconduct/">Codice di condotta Open Source di Microsoft</a>.
Per maggiori informazioni consulta le <a href="https://opensource.microsoft.com/codeofconduct/faq/">FAQ sul Codice di condotta</a> oppure
contatta <a href="mailto:opencode@microsoft.com">opencode@microsoft.com</a> per domande o commenti aggiuntivi.

## AI Responsabile

Microsoft si impegna ad aiutare i propri clienti a utilizzare i prodotti AI in modo responsabile, condividendo le proprie esperienze e costruendo partnership basate sulla fiducia tramite strumenti come Transparency Notes e Impact Assessments. Molte di queste risorse sono disponibili su <a href="https://aka.ms/RAI">https://aka.ms/RAI</a>.
L'approccio di Microsoft all'AI responsabile si basa sui principi di equità, affidabilità e sicurezza, privacy e protezione, inclusività, trasparenza e responsabilità.

I modelli di linguaggio naturale, immagini e voce su larga scala – come quelli utilizzati in questo esempio – possono talvolta comportarsi in modo non equo, inaffidabile o offensivo, causando potenziali danni. Consulta la <a href="https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text">Transparency note del servizio Azure OpenAI</a> per essere informato sui rischi e le limitazioni.

Il modo consigliato per mitigare questi rischi è includere un sistema di sicurezza nell'architettura che possa rilevare e prevenire comportamenti dannosi. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> offre un livello di protezione indipendente, in grado di rilevare contenuti dannosi generati da utenti e AI in applicazioni e servizi. Azure AI Content Safety include API per testo e immagini che permettono di individuare materiale dannoso. È disponibile anche un Content Safety Studio interattivo che consente di visualizzare, esplorare e provare codice di esempio per rilevare contenuti dannosi in diverse modalità. La seguente <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">documentazione di avvio rapido</a> ti guida nella richiesta del servizio.
Un altro aspetto da considerare è la performance complessiva dell'applicazione. Con applicazioni multi-modali e multi-modello, per performance si intende che il sistema si comporti come previsto da te e dai tuoi utenti, incluso il fatto di non generare output dannosi. È importante valutare le prestazioni della tua applicazione nel suo insieme utilizzando le [metriche di qualità della generazione e di rischio e sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puoi valutare la tua applicazione AI nell'ambiente di sviluppo usando il [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Fornendo un dataset di test o un obiettivo, le generazioni della tua applicazione AI generativa vengono misurate quantitativamente tramite valutatori integrati o personalizzati a tua scelta. Per iniziare a usare il prompt flow sdk per valutare il tuo sistema, puoi seguire la [guida rapida](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto può contenere marchi o loghi relativi a progetti, prodotti o servizi. L'uso autorizzato dei marchi o loghi Microsoft è soggetto e deve rispettare le
[Linee guida sui marchi e sul brand di Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
L'utilizzo di marchi o loghi Microsoft in versioni modificate di questo progetto non deve creare confusione o suggerire una sponsorizzazione da parte di Microsoft.
Qualsiasi utilizzo di marchi o loghi di terze parti è soggetto alle politiche di tali terze parti.

## Assistenza

Se hai difficoltà o domande sulla creazione di app AI, unisciti a:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Se vuoi inviare feedback sul prodotto o riscontri errori durante lo sviluppo, visita:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Disclaimer (Avvertenza):**
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.