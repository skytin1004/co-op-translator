# Co-op Translator

_Łatwe automatyczne tłumaczenie i utrzymanie tłumaczeń Twoich edukacyjnych treści GitHub na wiele języków w miarę rozwoju projektu._

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
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh-CN/README.md) | [Chiński (tradycyjny, Hongkong)](../zh-HK/README.md) | [Chiński (tradycyjny, Makau)](../zh-MO/README.md) | [Chiński (tradycyjny, Tajwan)](../zh-TW/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Holenderski](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigeryjski pidgin](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../pt-BR/README.md) | [Portugalski (Portugalia)](../pt-PT/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (Filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**
>
> To repozytorium zawiera tłumaczenia na ponad 50 języków, co znacznie zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
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
> To zapewnia wszystko, czego potrzebujesz do ukończenia kursu z dużo szybszym pobieraniem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Przegląd

**Co-op Translator** pomaga lokalizować Twoje edukacyjne treści GitHub na wiele języków bez wysiłku.  
Gdy aktualizujesz pliki Markdown, obrazy lub notatniki, tłumaczenia są automatycznie synchronizowane, zapewniając, że Twoje materiały pozostają dokładne i aktualne dla uczniów na całym świecie.

Przykład organizacji przetłumaczonych treści:

![Example](../../translated_images/pl/translation-ex.0c8aa6a7ee0aad2b.webp)

## Jak zarządzany jest stan tłumaczenia

Co-op Translator zarządza tłumaczonymi treściami jako **wersjonowanymi artefaktami oprogramowania**,  
a nie jako statycznymi plikami.

Narzędzie śledzi stan przetłumaczonego Markdown, obrazów i notatników  
używając **metadanych ograniczonych do języka**.

To rozwiązanie pozwala Co-op Translator:

- Niezawodnie wykrywać przestarzałe tłumaczenia  
- Traktować Markdown, obrazy i notatniki spójnie  
- Skalować bezpiecznie na duże, dynamiczne, wielojęzyczne repozytoria

Modelując tłumaczenia jako zarządzane artefakty,  
procesy tłumaczeniowe naturalnie dostosowują się do nowoczesnych  
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

1. Sprawdź, czy masz obsługiwaną wersję Pythona (obecnie 3.10-3.12). W poetry (pyproject.toml) jest to obsługiwane automatycznie.  
2. Utwórz plik `.env` korzystając z szablonu: [.env.template](../../.env.template)  
3. Skonfiguruj jedno źródło LLM (Azure OpenAI lub OpenAI)  
4. (Opcjonalnie) Dla tłumaczenia obrazów (`-img`) skonfiguruj Azure AI Vision  
5. (Opcjonalnie) Możesz skonfigurować kilka zestawów poświadczeń, kopiując zmienne ze znakami końcowymi, takimi jak `_1`, `_2` itd. Wszystkie zmienne w zestawie muszą mieć ten sam sufiks.  
6. (Zalecane) Wyczyść wszelkie poprzednie tłumaczenia, aby uniknąć konfliktów (np. `translations/`)  
7. (Zalecane) Dodaj sekcję tłumaczeń do swojego README używając [szablonu README languages](./getting_started/README_languages_template.md)  
8. Zobacz: [Konfiguracja Azure AI](./getting_started/set-up-azure-ai.md)

## Użycie

Przetłumacz wszystkie obsługiwane typy:

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
- Synchronizuje tłumaczenia z aktualizacjami źródłowymi  
- Działa lokalnie (CLI) lub w CI (GitHub Actions)  
- Korzysta z Azure OpenAI lub OpenAI; opcjonalnie Azure AI Vision dla obrazów  
- Zachowuje formatowanie i strukturę Markdown  

## Dokumentacja

- [Przewodnik po wierszu poleceń](./getting_started/command-line-guide/command-line-guide.md)  
- [Przewodnik GitHub Actions (Publiczne repozytoria i standardowe sekrety)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Przewodnik GitHub Actions (Repozytoria Microsoft i konfiguracje na poziomie organizacji)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Szablon języków README](./getting_started/README_languages_template.md)  
- [Obsługiwane języki](./getting_started/supported-languages.md)  
- [Współtworzenie](./CONTRIBUTING.md)  
- [Rozwiązywanie problemów](./getting_started/troubleshooting.md)

### Przewodnik specyficzny dla Microsoft  
> [!NOTE]  
> Tylko dla opiekunów repozytoriów Microsoft „Dla początkujących”.

- [Aktualizacja listy „pozostałych kursów” (tylko dla repozytoriów MS Beginners)](./getting_started/update-other-courses.md)

## Wesprzyj nas i wspieraj globalną naukę

Dołącz do nas w rewolucjonizowaniu udostępniania treści edukacyjnych na całym świecie! Daj [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHub i wspieraj naszą misję przełamywania barier językowych w nauce i technologii. Twoje zainteresowanie i wkład mają znaczący wpływ! Zachęcamy do wkładów w kod i sugestii funkcji.

### Odkryj edukacyjne materiały Microsoft w Twoim języku

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

## Prezentacje wideo

👉 Kliknij obraz poniżej, aby obejrzeć na YouTube.

- **Open at Microsoft**: Krótkie, 18-minutowe wprowadzenie i szybki przewodnik, jak korzystać z Co-op Translator.

  [![Open at Microsoft](../../translated_images/pl/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Współtworzenie

Ten projekt zachęca do wkładów i sugestii. Zainteresowany współtworzeniem Azure Co-op Translator? Zobacz nasz [CONTRIBUTING.md](./CONTRIBUTING.md), aby dowiedzieć się, jak możesz pomóc uczynić Co-op Translator bardziej dostępnym.

## Współtwórcy
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks postępowania

Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Aby uzyskać więcej informacji, zobacz [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) lub
skontaktuj się pod adresem [opencode@microsoft.com](mailto:opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Odpowiedzialna sztuczna inteligencja

Microsoft zobowiązuje się do wspierania naszych klientów w odpowiedzialnym korzystaniu z produktów AI, dzielenia się naszymi doświadczeniami oraz budowania relacji opartych na zaufaniu poprzez narzędzia takie jak Transparency Notes i Impact Assessments. Wiele z tych zasobów można znaleźć na stronie [https://aka.ms/RAI](https://aka.ms/RAI).
Podejście Microsoft do odpowiedzialnej sztucznej inteligencji opiera się na naszych zasadach AI, obejmujących sprawiedliwość, niezawodność i bezpieczeństwo, prywatność i ochronę, inkluzywność, przejrzystość oraz odpowiedzialność.

Modele języka naturalnego, obrazu i mowy na dużą skalę – takie jak te używane w tym przykładzie – mogą potencjalnie zachowywać się w sposób niesprawiedliwy, zawodny lub obraźliwy, co może powodować szkody. Prosimy o zapoznanie się z [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być poinformowanym o ryzykach i ograniczeniach.

Zalecanym podejściem do łagodzenia tych ryzyk jest uwzględnienie systemu bezpieczeństwa w architekturze, który może wykrywać i zapobiegać szkodliwym zachowaniom. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety zawiera interfejsy API tekstu i obrazu, które umożliwiają wykrywanie materiałów szkodliwych. Mamy także interaktywne Content Safety Studio, które pozwala przeglądać, badać i testować przykładowy kod do wykrywania szkodliwych treści w różnych modalnościach. Następująca [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) przeprowadzi Cię przez proces wysyłania żądań do usługi.

Kolejnym aspektem do rozważenia jest ogólna wydajność aplikacji. W aplikacjach wielomodalnych i wielomodelowych, wydajność oznacza dla nas, że system działa zgodnie z oczekiwaniami Twoimi i Twoich użytkowników, włączając w to brak generowania szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji, korzystając z [metryk jakości generowania oraz ryzyka i bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Możesz ocenić swoją aplikację AI w środowisku deweloperskim, korzystając z [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Przy użyciu zestawu testowego lub celu, generacje Twojej aplikacji generatywnej AI są ilościowo oceniane za pomocą wbudowanych lub niestandardowych ewaluatorów według Twojego wyboru. Aby rozpocząć pracę z prompt flow sdk do oceny swojego systemu, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po przeprowadzeniu biegu ewaluacji możesz [wizualizować wyniki w Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znak towarowy

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft podlega i musi przestrzegać
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować zamieszania ani sugerować sponsorowania przez Microsoft.
Jakiekolwiek użycie znaków towarowych lub logotypów stron trzecich podlega politykom tych stron trzecich.

## Uzyskaj pomoc

Jeśli napotkasz problemy lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jeśli masz opinie na temat produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie wykonane przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->