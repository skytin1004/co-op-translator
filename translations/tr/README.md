# Co-op Translator

_Eğitim amaçlı GitHub içeriğinizin çevirilerini, projeniz geliştikçe birden çok dilde kolayca otomatikleştirin ve bakımını yapın._

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

### 🌐 Çoklu Dil Desteği

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) tarafından desteklenmektedir

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](./README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Yerel olarak klonlamayı mı tercih ediyorsunuz?**
>
> Bu depo 50'den fazla dil çevirisi içerir, bu da indirme boyutunu önemli ölçüde artırır. Çeviri olmadan klonlamak için sparse checkout kullanın:
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
> Bu, kursu tamamlamak için ihtiyacınız olan her şeyi çok daha hızlı bir indirme ile sağlar.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Genel Bakış

**Co-op Translator**, eğitim materyallerinizi GitHub üzerinde birden fazla dile zahmetsizce yerelleştirmenize yardımcı olur.  
Markdown dosyalarınızı, görsellerinizi veya defterlerinizi güncellediğinizde, çeviriler otomatik olarak senkronize edilir, böylece dünyadaki öğrenenler için içeriğiniz doğru ve güncel kalır.

Çevrilmiş içeriğin nasıl organize edildiğine dair örnek:

![Example](../../imgs/translation-ex.png)

## Çeviri durumu nasıl yönetilir

Co-op Translator, çevrilmiş içeriği **sürüm kontrollü yazılım ürünleri** olarak yönetir,  
statik dosyalar olarak değil.

Araç, çevrilmiş Markdown, görseller ve defterlerin durumunu  
**dil bazlı meta veriler** kullanarak izler.

Bu tasarım Co-op Translator'a şu avantajları sağlar:

- Güncelliğini yitirmiş çevirileri güvenilir şekilde tespit etme  
- Markdown, görsel ve defterlere tutarlı yaklaşım  
- Hızlı değişen, çok dilli büyük depolarda güvenle ölçeklendirme

Çevirileri yönetilen ürünler olarak modelleyerek,  
çeviri iş akışları modern  
yazılım bağımlılık ve ürün yönetimi uygulamalarına doğal olarak uyum sağlar.

→ [Çeviri durumu nasıl yönetilir](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Hızlı başlangıç

```bash
# Bir sanal ortam oluşturun ve etkinleştirin (önerilir)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Paketi yükleyin
pip install co-op-translator
# Çevir
translate -l "ko ja fr" -md
```

Docker:

```bash
# Kamu imajını GHCR'den çek
docker pull ghcr.io/azure/co-op-translator:latest
# Geçerli klasörü bağlayarak ve .env dosyasını sağlayarak çalıştır (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal kurulum

1. Desteklenen bir Python sürümüne sahip olduğunuzu doğrulayın (şu anda 3.10-3.12). Poetry (pyproject.toml) bunu otomatik olarak halleder.  
2. Şablon kullanarak `.env` dosyası oluşturun: [.env.template](../../.env.template)  
3. Bir LLM sağlayıcısı yapılandırın (Azure OpenAI veya OpenAI)  
4. (İsteğe bağlı) Görsel çeviri için (`-img`) Azure AI Vision ayarlayın  
5. (İsteğe bağlı) Değişkenleri `_1`, `_2` gibi son eklerle çoğaltarak birden fazla kimlik bilgisi seti yapılandırabilirsiniz. Her set içindeki tüm değişkenler aynı son eki paylaşmalıdır.  
6. (Önerilen) Önceki çevirileri çakışmayı önlemek için temizleyin (örneğin, `translations/`)  
7. (Önerilen) README dosyanıza [README dillere şablon](./getting_started/README_languages_template.md) ile bir çeviri bölümü ekleyin  
8. Bkz: [Azure AI Kurulumu](./getting_started/set-up-azure-ai.md)

## Kullanım

Tüm desteklenen türleri çevirin:

```bash
translate -l "ko ja"
```

Sadece Markdown:

```bash
translate -l "de" -md
```

Markdown + görseller:

```bash
translate -l "pt" -md -img
```

Sadece defterler:

```bash
translate -l "zh" -nb
```

Daha fazla seçenek: [Komut referansı](./getting_started/command-reference.md)

## Özellikler

- Markdown, defter ve görsel çevirilerini otomatikleştirir  
- Kaynak değişiklikleri ile çevirileri senkron tutar  
- Yerelde (CLI) veya CI'da (GitHub Actions) çalışır  
- Azure OpenAI veya OpenAI kullanır; görseller için isteğe bağlı Azure AI Vision  
- Markdown biçimlendirmesini ve yapısını korur  

## Dokümanlar

- [Komut satırı rehberi](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions rehberi (Genel kamu depoları ve standart sırlar)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions rehberi (Microsoft organizasyon depoları ve organizasyon düzeyi kurulumlar)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README dillere şablon](./getting_started/README_languages_template.md)  
- [Desteklenen diller](./getting_started/supported-languages.md)  
- [Katkıda bulunma](./CONTRIBUTING.md)  
- [Sorun giderme](./getting_started/troubleshooting.md)  

### Microsoft'a özel rehber
> [!NOTE]
> Yalnızca Microsoft “Yeni Başlayanlar” depolarının bakımcıları için.

- [“Diğer kurslar” listesini güncelleme (yalnızca MS Yeni Başlayanlar depoları için)](./getting_started/update-other-courses.md)

## Bizi destekleyin ve küresel öğrenmeyi teşvik edin

Eğitim içeriğinin dünya çapında paylaşım şeklini devrimleştirirken bize katılın!  
[Co-op Translator](https://github.com/azure/co-op-translator) projesine GitHub’da ⭐ verin ve öğrenme ile teknoloji alanındaki dil bariyerlerini kaldırma misyonumuzu destekleyin. İlginiz ve katkılarınız büyük fark yaratır! Kod katkıları ve özellik önerileri her zaman hoş karşılanır.

### Microsoft eğitim içeriklerini kendi dilinizde keşfedin

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

## Video sunumlar

👉 İzlemek için aşağıdaki resme tıklayın.

- **Microsoft'ta Açık (Open at Microsoft)**: Co-op Translator'ın kısa 18 dakikalık tanıtım ve hızlı kullanma rehberi.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Katkıda Bulunma

Bu proje katkı ve önerilere açıktır. Azure Co-op Translator'a katkıda bulunmak mı istiyorsunuz? Lütfen Co-op Translator’ı daha erişilebilir kılmak için nasıl katkıda bulunabileceğinize dair rehberimiz olan [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasını inceleyin.

## Katkıda bulunanlar
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Davranış Kuralları

Bu proje, [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/)nu benimsemiştir.  
Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasına bakabilir veya herhangi bir ek soru ya da yorum için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresiyle iletişime geçebilirsiniz.

## Sorumlu Yapay Zeka

Microsoft, müşterilerimizin yapay zeka ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmaya, deneyimlerimizi paylaşmaya ve Transparanlık Notları ve Etki Değerlendirmeleri gibi araçlar aracılığıyla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların birçoğuna [https://aka.ms/RAI](https://aka.ms/RAI) adresinden ulaşabilirsiniz.  
Microsoft'un sorumlu yapay zeka yaklaşımı; adalet, güvenilirlik ve güvenlik, gizlilik ve emniyet, kapsayıcılık, şeffaflık ve hesap verebilirlik yapay zeka ilkelerine dayanmaktadır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görsel ve konuşma modelleri, adaletsiz, güvensiz veya rahatsız edici biçimde davranabilir ve dolayısıyla zarar verebilir. Riskler ve kısıtlamalar hakkında bilgi edinmek için lütfen [Azure OpenAI hizmeti Transparanlık notuna](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) bakınız.

Bu riskleri azaltmak için önerilen yaklaşım, mimarinizde zarar verici davranışları tespit edip önleyebilen bir güvenlik sistemi bulundurmaktır. [Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-services/content-safety/overview) uygulamalarda ve hizmetlerde, zararlı kullanıcı ve yapay zeka kaynaklı içerikleri tespit edebilen bağımsız bir koruma katmanı sağlar. Azure AI İçerik Güvenliği, zararlı materyalleri tespit etmeyi sağlayan metin ve görsel API'lerini içermektedir. Ayrıca, farklı modalitelerde zararlı içeriği tespit etmek için örnek kodları inceleyip deneyimleyebileceğiniz etkileşimli bir İçerik Güvenliği Stüdyosu bulunmaktadır. Aşağıdaki [hızlı başlangıç dokümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) servise istek yapmanın yolunu gösterir.

Dikkate alınması gereken bir diğer konu ise genel uygulama performansıdır. Çok modalitli ve çok modeller içeren uygulamalarda, performans sistemin sizin ve kullanıcılarınızın beklentileri doğrultusunda çalışması, zararlı çıktılar üretmemesi anlamına gelir. Genel uygulamanızın performansını değerlendirmek için [üretim kalitesi ve risk ile güvenlik ölçütlerini](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanmanız önemlidir.

Yapay zeka uygulamanızı geliştirme ortamınızda [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ile değerlendirebilirsiniz. Test veri kümesi ya da hedef verildiğinde, üretici yapay zeka uygulama sonuçlarınız yerleşik veya seçtiğiniz özel değerlendiricilerle sayısal olarak ölçülür. Sistemizi değerlendirmek için prompt flow sdk kullanımına başlamak adına [hızlı başlangıç rehberini](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) takip edebilirsiniz. Değerlendirme çalışmasını yürüttüğünüzde, sonucu [Azure AI Studio'da görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ticari Markalar

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı,  
[Microsoft'un Ticari Marka ve Marka Kılavuzları](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)na tabidir ve bu kurallara uyulmalıdır.  
Microsoft ticari markalarının veya logolarının değiştirilmiş sürümlerinde kullanılması, karışıklığa yol açmamalı veya Microsoft sponsorluğu gibi yanlış anlamalara neden olmamalıdır.  
Üçüncü taraf ticari markalarının veya logolarının kullanımı ise ilgili üçüncü taraf politikalarına bağlıdır.

## Yardım Alma

Takıldığınızda veya yapay zeka uygulamaları geliştirme ile ilgili sorularınız olduğunda katılabilirsiniz:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ürün geribildirimi ya da uygulamayı oluştururken karşılaştığınız hatalar için ziyaret edin:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->