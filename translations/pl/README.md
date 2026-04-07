# Co-op Translator

_Łatwo automatyzuj i utrzymuj tłumaczenia swojego edukacyjnego zawartości na GitHubie w wielu językach w miarę rozwoju projektu._

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

### 🌐 Wsparcie wielojęzyczne

#### Wsparcie przez [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](./README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Wolisz Klonować Lokalnie?**
>
> To repozytorium zawiera ponad 50 tłumaczeń, co znacznie zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
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
> To zapewnia wszystko, czego potrzebujesz do ukończenia kursu przy znacznie szybszym pobieraniu.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Przegląd

**Co-op Translator** pomaga łatwo lokalizować edukacyjne treści na GitHubie na wiele języków.  
Gdy aktualizujesz swoje pliki Markdown, obrazy lub notatniki, tłumaczenia pozostają automatycznie zsynchronizowane, zapewniając, że Twoja zawartość jest dokładna i aktualna dla uczących się na całym świecie.

Przykład organizacji przetłumaczonej zawartości:

![Example](../../imgs/translation-ex.png)

## Jak zarządzany jest stan tłumaczenia

Co-op Translator zarządza przetłumaczoną zawartością jako **wersjonowane artefakty oprogramowania**,  
a nie jako statyczne pliki.

Narzędzie śledzi stan przetłumaczonego Markdowna, obrazów i notatników  
używając **metadanych zdefiniowanych wg języka**.

Ten projekt pozwala Co-op Translator:

- Niezawodnie wykrywać przestarzałe tłumaczenia
- Traktować Markdown, obrazy i notatniki spójnie
- Bezpiecznie skalować się w dużych, szybko zmieniających się, wielojęzycznych repozytoriach

Poprzez modelowanie tłumaczeń jako zarządzanych artefaktów,  
przepływy pracy tłumaczeń naturalnie dopasowują się do nowoczesnych  
praktyk zarządzania zależnościami i artefaktami oprogramowania.

→ [Jak zarządzany jest stan tłumaczenia](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Szybki start

```bash
# Utwórz i aktywuj środowisko wirtualne (zalecane)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Zainstaluj pakiet
pip install co-op-translator
# Przetłumacz
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pobierz publiczny obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Uruchom z zamontowanym bieżącym folderem i dostarczonym plikiem .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna konfiguracja

1. Upewnij się, że masz obsługiwaną wersję Pythona (obecnie 3.10-3.12). W poetry (pyproject.toml) jest to obsługiwane automatycznie.  
2. Utwórz plik `.env` używając szablonu: [.env.template](../../.env.template)  
3. Skonfiguruj dostawcę LLM (Azure OpenAI lub OpenAI)  
4. (Opcjonalnie) Dla tłumaczenia obrazów (`-img`), skonfiguruj Azure AI Vision  
5. (Opcjonalnie) Możesz skonfigurować wiele zestawów poświadczeń, duplikując zmienne z sufiksami takimi jak `_1`, `_2` itd. Wszystkie zmienne w zestawie muszą mieć ten sam sufiks.  
6. (Zalecane) Wyczyść poprzednie tłumaczenia, aby uniknąć konfliktów (np. `translations/`)  
7. (Zalecane) Dodaj sekcję tłumaczeń do README używając [szablonu języków README](./getting_started/README_languages_template.md)  
8. Zobacz: [Konfiguracja Azure AI](./getting_started/set-up-azure-ai.md)

## Użytkowanie

Tłumacz wszystkie obsługiwane typy:

```bash
translate -l "ko ja"
```

Tylko Markdown:

```bash
translate -l "de" -md
```

Markdown + obrazy:

```bash
translate -l "pt" -md -img
```

Tylko notatniki:

```bash
translate -l "zh" -nb
```

Więcej flag: [Referencja poleceń](./getting_started/command-reference.md)

## Funkcje

- Automatyczne tłumaczenie Markdown, notatników i obrazów  
- Utrzymuje tłumaczenia zgodne ze zmianami źródłowymi  
- Działa lokalnie (CLI) lub w CI (GitHub Actions)  
- Używa Azure OpenAI lub OpenAI; opcjonalnie Azure AI Vision dla obrazów  
- Zachowuje formatowanie i strukturę Markdown  

## Dokumentacja

- [Przewodnik po wierszu poleceń](./getting_started/command-line-guide/command-line-guide.md)  
- [Przewodnik GitHub Actions (Publiczne repozytoria i standardowe sekrety)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Przewodnik GitHub Actions (Repozytoria organizacji Microsoft i konfiguracje na poziomie organizacji)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Szablon języków README](./getting_started/README_languages_template.md)  
- [Obsługiwane języki](./getting_started/supported-languages.md)  
- [Wkład w projekt](./CONTRIBUTING.md)  
- [Rozwiązywanie problemów](./getting_started/troubleshooting.md)  

### Przewodnik specyficzny dla Microsoft  
> [!NOTE]  
> Dla opiekunów repozytoriów Microsoft „For Beginners” tylko.

- [Aktualizacja listy „inne kursy” (tylko dla repozytoriów MS Beginners)](./getting_started/update-other-courses.md)

## Wspieraj nas i rozwijaj globalną edukację

Dołącz do nas w rewolucjonizowaniu sposobu globalnego udostępniania treści edukacyjnych!  
Daj [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubie i wspieraj naszą misję przełamywania barier językowych w nauce i technologii. Twoje zainteresowanie i wkład mają znaczący wpływ! Wkład w kod i sugestie funkcji są zawsze mile widziane.

### Odkrywaj edukacyjne treści Microsoft w swoim języku

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)  
- [AZD dla początkujących](https://github.com/microsoft/AZD-for-beginners)  
- [Edge AI dla początkujących](https://github.com/microsoft/edgeai-for-beginners)  
- [Model Context Protocol (MCP) dla początkujących](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents dla początkujących](https://github.com/microsoft/ai-agents-for-beginners)  
- [Generative AI dla początkujących z użyciem .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)  
- [Generative AI dla początkujących](https://github.com/microsoft/generative-ai-for-beginners)  
- [Generative AI dla początkujących z użyciem Java](https://github.com/microsoft/generative-ai-for-beginners-java)  
- [ML dla początkujących](https://aka.ms/ml-beginners)  
- [Data Science dla początkujących](https://aka.ms/datascience-beginners)  
- [AI dla początkujących](https://aka.ms/ai-beginners)  
- [Cyberbezpieczeństwo dla początkujących](https://github.com/microsoft/Security-101)  
- [Web Dev dla początkujących](https://aka.ms/webdev-beginners)  
- [IoT dla początkujących](https://aka.ms/iot-beginners)  
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Prezentacje wideo

👉 Kliknij obraz poniżej, aby obejrzeć na YouTube.

- **Open at Microsoft**: Krótkie, 18-minutowe wprowadzenie i szybki przewodnik, jak korzystać z Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Wkład w projekt

Ten projekt chętnie przyjmuje wkład i sugestie. Interesuje Cię udział w Azure Co-op Translator? Proszę zobacz nasz [CONTRIBUTING.md](./CONTRIBUTING.md) z wytycznymi, jak możesz pomóc uczynić Co-op Translator bardziej dostępnym.

## Współtwórcy
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks postępowania

Ten projekt przyjął [Kodeks postępowania open source Microsoft](https://opensource.microsoft.com/codeofconduct/).
Więcej informacji znajdziesz w [często zadawanych pytaniach dotyczących Kodeksu postępowania](https://opensource.microsoft.com/codeofconduct/faq/) lub
skontaktuj się pod adresem [opencode@microsoft.com](mailto:opencode@microsoft.com) z dodatkowymi pytaniami lub komentarzami.

## Odpowiedzialna sztuczna inteligencja

Microsoft zobowiązuje się do pomocy naszym klientom w odpowiedzialnym korzystaniu z naszych produktów AI, dzielenia się naszymi doświadczeniami oraz budowania zaufania opartego na partnerstwie poprzez narzędzia takie jak Transparency Notes i Impact Assessments. Wiele z tych zasobów można znaleźć pod adresem [https://aka.ms/RAI](https://aka.ms/RAI).
Podejście Microsoft do odpowiedzialnej AI opiera się na naszych zasadach AI dotyczących uczciwości, niezawodności i bezpieczeństwa, prywatności i ochrony, inkluzywności, przejrzystości oraz odpowiedzialności.

Modele języka naturalnego, obrazów i mowy na dużą skalę – takie jak te używane w tym przykładzie – mogą potencjalnie zachowywać się w sposób nieuczciwy, zawodny lub obraźliwy, co może powodować szkody. Prosimy zapoznać się z [notatką o przejrzystości usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być poinformowanym o ryzykach i ograniczeniach.

Zalecanym sposobem łagodzenia tych ryzyk jest uwzględnienie w architekturze systemu bezpieczeństwa, który może wykrywać i zapobiegać szkodliwym zachowaniom. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety obejmuje API tekstowe i graficzne, które pozwalają wykrywać materiały szkodliwe. Mamy także interaktywne Content Safety Studio, które pozwala przeglądać, eksplorować i wypróbowywać przykładowy kod do wykrywania szkodliwych treści w różnych modalnościach. Poniższa [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) poprowadzi Cię przez wykonywanie żądań do usługi.

Kolejnym aspektem, który należy wziąć pod uwagę, jest ogólna wydajność aplikacji. W przypadku aplikacji multimodalnych i wielomodelowych rozumiemy wydajność jako działanie systemu zgodnie z oczekiwaniami Twoimi i Twoich użytkowników, w tym nie generowanie szkodliwych wyników. Ważne jest ocenianie wydajności całej aplikacji za pomocą [metryk jakości generowania oraz ryzyka i bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Możesz ocenić swoją aplikację AI w środowisku deweloperskim używając [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Bazując na zestawie testowym lub celu, generacje Twojej aplikacji AI są ilościowo mierzone za pomocą wbudowanych lub niestandardowych ewalwatorów. Aby zacząć pracę z prompt flow sdk do oceny systemu, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po wykonaniu uruchomienia oceny możesz [wizualizować wyniki w Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft
podlega i musi być zgodne z
[Zasadami korzystania ze znaków towarowych i marki Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować zamieszania ani sugerować sponsorowania przez Microsoft.
Każde użycie znaków towarowych lub logotypów stron trzecich podlega ich politykom.

## Uzyskiwanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jeśli masz uwagi dotyczące produktu lub błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->