<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:05:35+00:00",
  "source_file": "README.md",
  "language_code": "sv"
}
-->
# Co-op Translator

_Automatisera enkelt översättningen av ditt utbildningsinnehåll på GitHub till flera språk och nå en global publik._

### 🌐 Stöd för flera språk

#### Stöds av <a href="https://github.com/Azure/Co-op-Translator">Co-op Translator</a>

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
<a href="./translations/ar/README.md">Arabiska</a> | <a href="./translations/bn/README.md">Bengali</a> | <a href="./translations/bg/README.md">Bulgariska</a> | <a href="./translations/my/README.md">Burmesiska (Myanmar)</a> | <a href="./translations/zh/README.md">Kinesiska (Förenklad)</a> | <a href="./translations/hk/README.md">Kinesiska (Traditionell, Hong Kong)</a> | <a href="./translations/mo/README.md">Kinesiska (Traditionell, Macau)</a> | <a href="./translations/tw/README.md">Kinesiska (Traditionell, Taiwan)</a> | <a href="./translations/hr/README.md">Kroatiska</a> | <a href="./translations/cs/README.md">Tjeckiska</a> | <a href="./translations/da/README.md">Danska</a> | <a href="./translations/nl/README.md">Nederländska</a> | <a href="./translations/et/README.md">Estniska</a> | <a href="./translations/fi/README.md">Finska</a> | <a href="./translations/fr/README.md">Franska</a> | <a href="./translations/de/README.md">Tyska</a> | <a href="./translations/el/README.md">Grekiska</a> | <a href="./translations/he/README.md">Hebreiska</a> | <a href="./translations/hi/README.md">Hindi</a> | <a href="./translations/hu/README.md">Ungerska</a> | <a href="./translations/id/README.md">Indonesiska</a> | <a href="./translations/it/README.md">Italienska</a> | <a href="./translations/ja/README.md">Japanska</a> | <a href="./translations/ko/README.md">Koreanska</a> | <a href="./translations/lt/README.md">Litauiska</a> | <a href="./translations/ms/README.md">Malajiska</a> | <a href="./translations/mr/README.md">Marathi</a> | <a href="./translations/ne/README.md">Nepali</a> | <a href="./translations/pcm/README.md">Nigeriansk pidgin</a> | <a href="./translations/no/README.md">Norska</a> | <a href="./translations/fa/README.md">Persiska (Farsi)</a> | <a href="./translations/pl/README.md">Polska</a> | <a href="./translations/br/README.md">Portugisiska (Brasilien)</a> | <a href="./translations/pt/README.md">Portugisiska (Portugal)</a> | <a href="./translations/pa/README.md">Punjabi (Gurmukhi)</a> | <a href="./translations/ro/README.md">Rumänska</a> | <a href="./translations/ru/README.md">Ryska</a> | <a href="./translations/sr/README.md">Serbiska (Kyrilliska)</a> | <a href="./translations/sk/README.md">Slovakiska</a> | <a href="./translations/sl/README.md">Slovenska</a> | <a href="./translations/es/README.md">Spanska</a> | <a href="./translations/sw/README.md">Swahili</a> | <a href="./translations/sv/README.md">Svenska</a> | <a href="./translations/tl/README.md">Tagalog (Filipino)</a> | <a href="./translations/ta/README.md">Tamil</a> | <a href="./translations/th/README.md">Thailändska</a> | <a href="./translations/tr/README.md">Turkiska</a> | <a href="./translations/uk/README.md">Ukrainska</a> | <a href="./translations/ur/README.md">Urdu</a> | <a href="./translations/vi/README.md">Vietnamesiska</a>
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Översikt

**Co-op Translator** gör det enkelt att snabbt översätta ditt utbildningsinnehåll på GitHub till flera språk, så att du kan nå en global publik utan ansträngning. När du uppdaterar dina Markdown-filer, bilder eller Jupyter-notebooks synkroniseras översättningarna automatiskt så att ditt utbildningsinnehåll på GitHub alltid är aktuellt och relevant för internationella användare.

Se hur Co-op Translator organiserar översatt utbildningsinnehåll på GitHub:

![Exempel](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sv.png)

## Kom igång snabbt

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

## Minimal installation

- Skapa en `.env` med hjälp av mallen: [.env.template](../../.env.template)
- Konfigurera en LLM-leverantör (Azure OpenAI eller OpenAI)
- För bildöversättning (`-img`), konfigurera även Azure AI Vision
- Rekommenderat: Om du har översättningar från andra verktyg, rensa dem först för att undvika konflikter (t.ex. `translations/`).
- Rekommenderat: Lägg till en översättningssektion i din README med hjälp av [README languages template](./README_languages_template.md)
- Se: [Konfigurera Azure AI](./getting_started/set-up-azure-ai.md)

## Användning

Översätt alla stödda typer:

```bash
translate -l "ko ja"
```

Endast Markdown:

```bash
translate -l "de" -md
```

Markdown + bilder:

```bash
translate -l "pt" -md -img
```

Endast notebooks:

```bash
translate -l "zh" -nb
```

Fler flaggor: [Kommandoreferens](./getting_started/command-reference.md)

## Funktioner

- Automatisk översättning av Markdown, notebooks och bilder
- Håller översättningarna synkroniserade med källändringar
- Fungerar lokalt (CLI) eller i CI (GitHub Actions)
- Använder Azure OpenAI eller OpenAI; valfritt Azure AI Vision för bilder
- Bevarar Markdown-format och struktur

## Dokumentation

- [Kommandoradsguide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions-guide (Publika repos & standardhemligheter)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions-guide (Microsoft-organisationens repos & org-nivå)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Stödda språk](./getting_started/supported-languages.md)
- [Felsökning](./getting_started/troubleshooting.md)

## Stöd oss och främja globalt lärande

Var med och förändra hur utbildningsinnehåll delas globalt! Ge [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub och stöd vårt uppdrag att bryta språkbarriärer inom lärande och teknik. Ditt intresse och dina bidrag gör stor skillnad! Kodbidrag och förslag på funktioner är alltid välkomna.

### Utforska Microsofts utbildningsinnehåll på ditt språk

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

## Videopresentationer

Lär dig mer om Co-op Translator genom våra presentationer _(Klicka på bilden nedan för att se på YouTube.)_:

- **Open at Microsoft**: En kort 18-minuters introduktion och snabbguide om hur du använder Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sv.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidra

Detta projekt välkomnar bidrag och förslag. Vill du bidra till Azure Co-op Translator? Läs vår [CONTRIBUTING.md](./CONTRIBUTING.md) för riktlinjer om hur du kan hjälpa till att göra Co-op Translator mer tillgänglig.

## Bidragsgivare

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Uppförandekod

Detta projekt har antagit <a href="https://opensource.microsoft.com/codeofconduct/">Microsoft Open Source Code of Conduct</a>.
För mer information, se <a href="https://opensource.microsoft.com/codeofconduct/faq/">Code of Conduct FAQ</a> eller
kontakta <a href="mailto:opencode@microsoft.com">opencode@microsoft.com</a> om du har ytterligare frågor eller kommentarer.

## Ansvarsfull AI

Microsoft är engagerade i att hjälpa våra kunder använda våra AI-produkter ansvarsfullt, dela våra lärdomar och bygga förtroendebaserade partnerskap genom verktyg som Transparency Notes och Impact Assessments. Många av dessa resurser finns på <a href="https://aka.ms/RAI">https://aka.ms/RAI</a>.
Microsofts syn på ansvarsfull AI bygger på våra AI-principer: rättvisa, tillförlitlighet och säkerhet, integritet och säkerhet, inkludering, transparens och ansvarstagande.

Storskaliga modeller för språk, bild och tal – som de som används i detta exempel – kan ibland bete sig på sätt som är orättvisa, opålitliga eller stötande, vilket kan orsaka skada. Läs gärna <a href="https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text">Azure OpenAI service Transparency note</a> för att vara medveten om risker och begränsningar.

Det rekommenderade sättet att minska dessa risker är att inkludera ett säkerhetssystem i din arkitektur som kan upptäcka och förhindra skadligt beteende. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> ger ett oberoende skyddslager som kan upptäcka skadligt användargenererat och AI-genererat innehåll i applikationer och tjänster. Azure AI Content Safety innehåller text- och bild-API:er som låter dig upptäcka skadligt material. Vi har också ett interaktivt Content Safety Studio där du kan testa och utforska kodexempel för att upptäcka skadligt innehåll i olika format. Följande <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">snabbstartsdokumentation</a> guidar dig genom hur du gör förfrågningar till tjänsten.
En annan aspekt att ta hänsyn till är applikationens övergripande prestanda. Med multimodala och multi-modell-applikationer innebär prestanda att systemet fungerar som du och dina användare förväntar er, inklusive att det inte genererar skadliga resultat. Det är viktigt att utvärdera prestandan för hela din applikation med hjälp av [genereringskvalitet samt risk- och säkerhetsmått](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan utvärdera din AI-applikation i din utvecklingsmiljö med hjälp av [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Med antingen en testdatamängd eller ett mål mäts dina generativa AI-applikationers resultat kvantitativt med inbyggda eller egna utvärderingsverktyg som du väljer. För att komma igång med prompt flow sdk för att utvärdera ditt system kan du följa [snabbstartsguiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). När du har genomfört en utvärderingskörning kan du [visualisera resultaten i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varumärken

Detta projekt kan innehålla varumärken eller logotyper för projekt, produkter eller tjänster. Auktoriserad användning av Microsofts
varumärken eller logotyper omfattas av och måste följa
[Microsofts riktlinjer för varumärken och varumärkesanvändning](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Användning av Microsofts varumärken eller logotyper i modifierade versioner av detta projekt får inte orsaka förväxling eller antyda att Microsoft står bakom projektet.
All användning av tredje parts varumärken eller logotyper omfattas av dessa tredje parters policyer.

## Få hjälp

Om du kör fast eller har frågor om att bygga AI-appar, gå med i:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Om du har produktfeedback eller stöter på fel under utvecklingen, besök:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.