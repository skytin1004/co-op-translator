<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T14:09:39+00:00",
  "source_file": "README.md",
  "language_code": "sr"
}
-->
# Ко-оп Преводилац

_Аутоматизујте превођење вашег едукативног GitHub садржаја на више језика и доприте до глобалне публике._

### 🌐 Подршка за више језика

#### Подржано од стране <a href="https://github.com/Azure/Co-op-Translator">Co-op Translator</a>

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
<a href="./translations/ar/README.md">Арапски</a> | <a href="./translations/bn/README.md">Бенгалски</a> | <a href="./translations/bg/README.md">Бугарски</a> | <a href="./translations/my/README.md">Бурмански (Мјанмар)</a> | <a href="./translations/zh/README.md">Кинески (поједностављени)</a> | <a href="./translations/hk/README.md">Кинески (традиционални, Хонг Конг)</a> | <a href="./translations/mo/README.md">Кинески (традиционални, Макао)</a> | <a href="./translations/tw/README.md">Кинески (традиционални, Тајван)</a> | <a href="./translations/hr/README.md">Хрватски</a> | <a href="./translations/cs/README.md">Чешки</a> | <a href="./translations/da/README.md">Дански</a> | <a href="./translations/nl/README.md">Холандски</a> | <a href="./translations/et/README.md">Естонски</a> | <a href="./translations/fi/README.md">Фински</a> | <a href="./translations/fr/README.md">Француски</a> | <a href="./translations/de/README.md">Немачки</a> | <a href="./translations/el/README.md">Грчки</a> | <a href="./translations/he/README.md">Хебрејски</a> | <a href="./translations/hi/README.md">Хинди</a> | <a href="./translations/hu/README.md">Мађарски</a> | <a href="./translations/id/README.md">Индонежански</a> | <a href="./translations/it/README.md">Италијански</a> | <a href="./translations/ja/README.md">Јапански</a> | <a href="./translations/ko/README.md">Корејски</a> | <a href="./translations/lt/README.md">Литвански</a> | <a href="./translations/ms/README.md">Малајски</a> | <a href="./translations/mr/README.md">Марати</a> | <a href="./translations/ne/README.md">Непалски</a> | <a href="./translations/pcm/README.md">Нигеријски Пиџин</a> | <a href="./translations/no/README.md">Норвешки</a> | <a href="./translations/fa/README.md">Персијски (Фарси)</a> | <a href="./translations/pl/README.md">Пољски</a> | <a href="./translations/br/README.md">Португалски (Бразил)</a> | <a href="./translations/pt/README.md">Португалски (Португалија)</a> | <a href="./translations/pa/README.md">Пунџаби (Гурмуки)</a> | <a href="./translations/ro/README.md">Румунски</a> | <a href="./translations/ru/README.md">Руски</a> | <a href="./translations/sr/README.md">Српски (Ћирилица)</a> | <a href="./translations/sk/README.md">Словачки</a> | <a href="./translations/sl/README.md">Словеначки</a> | <a href="./translations/es/README.md">Шпански</a> | <a href="./translations/sw/README.md">Свахили</a> | <a href="./translations/sv/README.md">Шведски</a> | <a href="./translations/tl/README.md">Тагалог (Филипински)</a> | <a href="./translations/ta/README.md">Тамилски</a> | <a href="./translations/th/README.md">Тајландски</a> | <a href="./translations/tr/README.md">Турски</a> | <a href="./translations/uk/README.md">Украјински</a> | <a href="./translations/ur/README.md">Урду</a> | <a href="./translations/vi/README.md">Вијетнамски</a>
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Преглед

**Co-op Translator** вам омогућава да брзо преведете ваш едукативни GitHub садржај на више језика и лако допрете до глобалне публике. Када ажурирате ваше Markdown датотеке, слике или Jupyter свеске, преводи се аутоматски синхронизују како би ваш едукативни садржај на GitHub-у увек био свеж и релевантан за кориснике широм света.

Погледајте како Co-op Translator организује преведени едукативни GitHub садржај:

<img src="../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sr.png" alt="Пример">

## Брзи почетак

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

## Минимална подешавања

- Креирајте `.env` користећи шаблон: <a href="./.env.template">.env.template</a>
- Подесите једног LLM провајдера (Azure OpenAI или OpenAI)
- За превођење слика (`-img`), подесите и Azure AI Vision
- Препорука: Ако већ имате преводе направљене другим алатима, прво их уклоните да не би дошло до конфликта (на пример: `translations/`).
- Препорука: Додајте секцију са преводима у ваш README користећи <a href="./README_languages_template.md">README шаблон за језике</a>
- Погледајте: <a href="./getting_started/set-up-azure-ai.md">Подешавање Azure AI</a>

## Коришћење

Преведите све подржане типове:

```bash
translate -l "ko ja"
```

Само Markdown:

```bash
translate -l "de" -md
```

Markdown + слике:

```bash
translate -l "pt" -md -img
```

Само свеске:

```bash
translate -l "zh" -nb
```

Више опција: <a href="./getting_started/command-reference.md">Референца команди</a>

## Карактеристике

- Аутоматско превођење Markdown-а, свески и слика
- Држи преводе усклађене са изворним изменама
- Ради локално (CLI) или у CI (GitHub Actions)
- Користи Azure OpenAI или OpenAI; опционо Azure AI Vision за слике
- Чува Markdown формат и структуру

## Документација

- <a href="./getting_started/command-line-guide/command-line-guide.md">Водич за командну линију</a>
- <a href="./getting_started/github-actions-guide/github-actions-guide-public.md">Водич за GitHub Actions (Јавни репозиторијуми и стандардне тајне)</a>
- <a href="./getting_started/github-actions-guide/github-actions-guide-org.md">Водич за GitHub Actions (Репозиторијуми Microsoft организације и организациона подешавања)</a>
- <a href="./getting_started/supported-languages.md">Подржани језици</a>
- <a href="./getting_started/troubleshooting.md">Решавање проблема</a>

## Подржите нас и ширите глобално учење

Придружите нам се у револуцији дељења едукативног садржаја широм света! Дајте <a href="https://github.com/azure/co-op-translator">Co-op Translator</a> ⭐ на GitHub-у и подржите нашу мисију рушења језичких баријера у учењу и технологији. Ваше интересовање и доприноси чине велику разлику! Доприноси у коду и предлози за нове функције су увек добродошли.

### Истражите Microsoft едукативни садржај на вашем језику

- <a href="https://github.com/microsoft/AZD-for-beginners">AZD за почетнике</a>
- <a href="https://github.com/microsoft/edgeai-for-beginners">Edge AI за почетнике</a>
- <a href="https://github.com/microsoft/mcp-for-beginners">Model Context Protocol (MCP) за почетнике</a>
- <a href="https://github.com/microsoft/ai-agents-for-beginners">AI агенти за почетнике</a>
- <a href="https://github.com/microsoft/Generative-AI-for-beginners-dotnet">Генеративни AI за почетнике (.NET)</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners">Генеративни AI за почетнике</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners-java">Генеративни AI за почетнике (Java)</a>
- <a href="https://aka.ms/ml-beginners">Машинско учење за почетнике</a>
- <a href="https://aka.ms/datascience-beginners">Наука о подацима за почетнике</a>
- <a href="https://aka.ms/ai-beginners">AI за почетнике</a>
- <a href="https://github.com/microsoft/Security-101">Кибер безбедност за почетнике</a>
- <a href="https://aka.ms/webdev-beginners">Веб развој за почетнике</a>
- <a href="https://aka.ms/iot-beginners">IoT за почетнике</a>
- <a href="https://github.com/microsoft/PhiCookBook">PhiCookBook</a>

## Видео презентације

Сазнајте више о Co-op Translator-у кроз наше презентације _(Кликните на слику испод да гледате на YouTube.)_:

- **Open at Microsoft**: Кратак 18-минутни увод и брзи водич за коришћење Co-op Translator-а.

  <a href="https://www.youtube.com/watch?v=jX_swfH_KNU"><img src="../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sr.jpg" alt="Open at Microsoft"></a>

## Допринос

Овај пројекат је отворен за доприносе и предлоге. Желите да допринесете Azure Co-op Translator-у? Погледајте наш <a href="./CONTRIBUTING.md">CONTRIBUTING.md</a> за смернице како можете помоћи да Co-op Translator буде приступачнији.

## Доприносиоци

<a href="https://github.com/Azure/co-op-translator/graphs/contributors"><img src="https://contrib.rocks/image?repo=Azure/co-op-translator" alt="co-op-translator contributors"></a>

## Кодекс понашања

Овај пројекат је усвојио <a href="https://opensource.microsoft.com/codeofconduct/">Microsoft Open Source Кодекс понашања</a>.
За више информација погледајте <a href="https://opensource.microsoft.com/codeofconduct/faq/">FAQ о кодексу понашања</a> или
контактирајте <a href="mailto:opencode@microsoft.com">opencode@microsoft.com</a> за додатна питања или коментаре.

## Одговорна AI

Microsoft је посвећен томе да помогне корисницима да одговорно користе наше AI производе, дели наша искуства и гради партнерства заснована на поверењу кроз алате као што су Белешке о транспарентности и Процене утицаја. Многи од ових ресурса су доступни на <a href="https://aka.ms/RAI">https://aka.ms/RAI</a>.
Microsoft-ов приступ одговорној AI заснива се на нашим AI принципима: правичност, поузданост и безбедност, приватност и сигурност, инклузивност, транспарентност и одговорност.

Велики модели за обраду природног језика, слика и говора – као што су они који се користе у овом примеру – могу понекад да се понашају непредвидиво, непоуздано или увредљиво, што може довести до штетних последица. Молимо вас да прочитате <a href="https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text">Белешку о транспарентности Azure OpenAI сервиса</a> да бисте били информисани о ризицима и ограничењима.

Препоручени начин за ублажавање ових ризика је да у вашу архитектуру укључите систем безбедности који може да открије и спречи штетно понашање. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> пружа независан слој заштите, способан да открије штетан садржај који генеришу корисници или AI у апликацијама и сервисима. Azure AI Content Safety укључује API-је за текст и слике који вам омогућавају да откријете штетан материјал. Такође имамо интерактивни Content Safety Studio који вам омогућава да видите, истражите и испробате пример кода за откривање штетног садржаја у различитим форматима. Следећа <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">брза документација</a> вас води кроз слање захтева ка сервису.

Još jedan aspekt koji treba uzeti u obzir je ukupne performanse aplikacije. Kod aplikacija koje koriste više modaliteta i više modela, performanse podrazumevaju da sistem radi onako kako vi i vaši korisnici očekujete, uključujući i to da ne generiše štetne rezultate. Važno je da procenite performanse vaše aplikacije koristeći <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">metrike kvaliteta generisanja, rizika i bezbednosti</a>.

Možete da testirate vašu AI aplikaciju u razvojnom okruženju koristeći <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Na osnovu testnog skupa podataka ili cilja, generacije vaše generativne AI aplikacije se kvantitativno mere pomoću ugrađenih ili prilagođenih evaluatora po vašem izboru. Da biste započeli sa prompt flow SDK-om i procenili vaš sistem, možete pratiti <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">brzi vodič</a>. Kada pokrenete evaluaciju, možete <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">vizualizovati rezultate u Azure AI Studio</a>.

## Трговачки знаци

Овај пројекат може садржати трговачке знаке или логотипе за пројекте, производе или услуге. Овлашћена употреба Microsoft
трговачких знакова или логотипа подлеже и мора да прати
<a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Microsoft смернице за употребу трговачких знакова и бренда</a>.
Употреба Microsoft трговачких знакова или логотипа у измењеним верзијама овог пројекта не сме да изазове забуну или имплицира да је Microsoft спонзор.
Свака употреба трговачких знакова или логотипа трећих страна подлеже политикама тих трећих страна.

## Помоћ и подршка

Ако се заглавите или имате питања о развоју AI апликација, придружите се:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Ако имате повратне информације о производу или наиђете на грешке током развоја, посетите:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.