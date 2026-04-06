# Co-op Translator

_Eğitim amaçlı GitHub içeriğinizin projeleriniz ilerledikçe kolayca otomatik olarak çevrilmesini ve birden çok dilde bakımını yapın._

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

### 🌐 Çok Dilli Destek

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) tarafından desteklenmektedir

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](./README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Yerel Olarak Klonlamayı mı Tercih Edersiniz?**
>
> Bu depo, indirilen boyutu önemli ölçüde artıran 50+ dil çevirisini içerir. Çeviriler olmadan klonlamak için sparse checkout kullanın:
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
> Bu, kursu tamamlamanız için gereken her şeyi çok daha hızlı indirme ile size sağlar.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Genel Bakış

**Co-op Translator**, eğitim amaçlı GitHub içeriğinizi birden çok dile zahmetsizce yerelleştirmenize yardımcı olur.  
Markdown dosyalarınızı, resimlerinizi veya defterlerinizi güncellediğinizde, çeviriler otomatik olarak senkronize kalır; böylece içeriğiniz dünya çapındaki öğrenenler için doğru ve güncel olur.

Çevrilmiş içeriğin nasıl organize edildiğine dair örnek:

![Example](../../translated_images/tr/translation-ex.0c8aa6a7ee0aad2b.webp)

## Çeviri durumu nasıl yönetilir

Co-op Translator çevrilmiş içeriği **sürüm kontrollü yazılım ürünleri** olarak yönetir,  
statik dosyalar olarak değil.

Araç, çevrilmiş Markdown, resim ve defterlerin durumunu  
**dil kapsamlı meta veriler** kullanarak takip eder.

Bu tasarım Co-op Translator'ın:

- Güncel olmayan çevirileri güvenilir şekilde tespit etmesini
- Markdown, resim ve defterlere tutarlı yaklaşmasını
- Büyük, hızlı hareket eden, çok dilli depolarda güvenli ölçeklenmesini

sağlar.

Çevirileri yönetilen ürünler olarak modelleyerek,  
çeviri iş akışları modern yazılım  
bağımlılık ve ürün yönetimi uygulamalarıyla doğal olarak uyumlu hale gelir.

→ [Çeviri durumu nasıl yönetilir](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Hızlı başlangıç

```bash
# Sanal bir ortam oluşturun ve etkinleştirin (önerilir)
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
# GHCR'den genel imajı çek
docker pull ghcr.io/azure/co-op-translator:latest
# Mevcut klasör takılı ve .env sağlanmış şekilde çalıştır (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal kurulum

1. Desteklenen bir Python sürümüne sahip olduğunuzu doğrulayın (şu anda 3.10-3.12). Poetry (pyproject.toml) bunu otomatik yönetir.
2. Şablonu kullanarak bir `.env` dosyası oluşturun: [.env.template](../../.env.template)
3. Bir LLM sağlayıcısını yapılandırın (Azure OpenAI veya OpenAI)
4. (Opsiyonel) Resim çevirisi için (`-img`) Azure AI Vision yapılandırması yapın
5. (Opsiyonel) `_1`, `_2` gibi son eklerle değişkenleri çoğaltarak birden çok kimlik bilgisi seti yapılandırabilirsiniz. Bir setteki tüm değişkenlerin aynı son eki paylaşması gerekir.
6. (Önerilen) Önceki çevirileri çakışmaları önlemek için temizleyin (ör. `translations/`)
7. (Önerilen) README dosyanıza bir çeviri bölümü ekleyin, [README diller şablonu](./getting_started/README_languages_template.md) kullanarak
8. Bakınız: [Azure AI Kurulumu](./getting_started/set-up-azure-ai.md)

## Kullanım

Tüm desteklenen türleri çevirin:

```bash
translate -l "ko ja"
```

Sadece Markdown:

```bash
translate -l "de" -md
```

Markdown + resimler:

```bash
translate -l "pt" -md -img
```

Sadece defterler:

```bash
translate -l "zh" -nb
```

Daha fazla parametre: [Komut referansı](./getting_started/command-reference.md)

## Özellikler

- Markdown, defterler ve resimler için otomatik çeviri
- Kaynak değişikliklerle çevirileri senkron tutar
- Yerelde (CLI) veya CI'da (GitHub Actions) çalışır
- Azure OpenAI veya OpenAI kullanır; resimler için opsiyonel Azure AI Vision
- Markdown biçimlendirmesini ve yapısını korur

## Dokümantasyon

- [Komut satırı rehberi](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions rehberi (Açık depolar & standart gizli anahtarlar)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions rehberi (Microsoft organizasyon depoları & organizasyon seviyesinde kurulumlar)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README diller şablonu](./getting_started/README_languages_template.md)
- [Desteklenen diller](./getting_started/supported-languages.md)
- [Katkıda bulunma](./CONTRIBUTING.md)
- [Sorun Giderme](./getting_started/troubleshooting.md)

### Microsoft'a özgü rehber
> [!NOTE]
> Sadece Microsoft “Yeni Başlayanlar” depolarının bakımcıları için.

- [“Diğer kurslar” listesini güncelleme (sadece MS Yeni Başlayanlar depoları için)](./getting_started/update-other-courses.md)

## Bizi destekleyin ve küresel öğrenimi teşvik edin

Eğitim içeriklerinin dünya çapında paylaşım şeklini devrimleştirmek için bize katılın! [Co-op Translator](https://github.com/azure/co-op-translator)'a GitHub'da bir ⭐ verin ve öğrenme ile teknolojide dil engellerini kaldırma misyonumuzu destekleyin. İlginiz ve katkılarınız büyük fark yaratır! Kod katkıları ve özellik önerileri her zaman memnuniyetle karşılanır.

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

👉 Aşağıdaki görsele tıklayarak YouTube’da izleyin.

- **Open at Microsoft**: Co-op Translator nasıl kullanılır hakkında kısa 18 dakikalık tanıtım ve hızlı rehber.

  [![Open at Microsoft](../../translated_images/tr/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Katkıda bulunma

Bu proje katkıları ve önerileri memnuniyetle karşılar. Azure Co-op Translator'a katkıda bulunmak ister misiniz? Lütfen Co-op Translator'ı daha erişilebilir hale getirmemize nasıl yardımcı olabileceğiniz hakkında kılavuzlar için [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasına bakınız.

## Katkıda bulunanlar
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kurallarını](https://opensource.microsoft.com/codeofconduct/) kabul etmiştir.
Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasına bakabilir veya 
ek sorularınız veya yorumlarınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresi ile iletişime geçebilirsiniz.

## Sorumlu AI

Microsoft, müşterilerimizin AI ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmaya, deneyimlerimizi paylaşmaya ve Transparency Notes ve Impact Assessments gibi araçlar aracılığıyla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların birçoğu [https://aka.ms/RAI](https://aka.ms/RAI) adresinde bulunabilir.
Microsoft'un sorumlu AI yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve emniyet, kapsayıcılık, şeffaflık ve hesap verebilirlik gibi AI ilkelerimize dayanır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görüntü ve konuşma modelleri potansiyel olarak adaletsiz, güvenilmez veya rahatsız edici davranışlar sergileyerek zarar verebilirler. Riskler ve sınırlamalar hakkında bilgi sahibi olmak için lütfen [Azure OpenAI servisi Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) belgesine bakınız.

Bu riskleri azaltmak için önerilen yaklaşım, zararlı davranışları algılayıp önleyebilen bir güvenlik sistemini mimarinize dahil etmektir. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulamalarda ve servislerde zararlı kullanıcı üretimi ve AI üretimi içeriği tespit edebilen bağımsız bir koruma katmanı sağlar. Azure AI Content Safety, zararlı materyalleri tespit etmenizi sağlayan metin ve görüntü API'lerini içerir. Ayrıca farklı modalitelerde zararlı içeriği tespit etmek için örnek kodları inceleyebileceğiniz, keşfedebileceğiniz ve deneyebileceğiniz etkileşimli bir Content Safety Studio’ya sahibiz. Aşağıdaki [hızlı başlangıç dökümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) size servise istek yapma sürecinde rehberlik eder.

Değerlendirmeniz gereken bir diğer nokta ise genel uygulama performansıdır. Çok modlu ve çok modelleri kullanan uygulamalarda, performans sistemin sizin ve kullanıcılarınızın beklentileri doğrultusunda çalışması, zararlı çıktı üretmemesi anlamına gelir. Genel uygulamanızın performansını [üretim kalitesi ve risk ve güvenlik metrikleri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanarak değerlendirmeniz önemlidir.

AI uygulamanızı geliştirme ortamınızda [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ile değerlendirebilirsiniz. Test veri seti veya hedef verilerek, sizin üretici AI uygulamanızın üretimleri, yerleşik değerlendiriciler veya sizin seçtiğiniz özel değerlendiricilerle nicel olarak ölçülür. Sisteminizi değerlendirmek için prompt flow sdk’sına başlamak üzere [hızlı başlangıç kılavuzunu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) takip edebilirsiniz. Bir değerlendirme çalışması tamamlandığında, sonuçları [Azure AI Studio'da görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ticari Markalar

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarını veya logolarını yetkili kullanımı, 
[Microsoft'un Ticari Marka ve Marka Kılavuzları](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)'na tabi olup bu kurallara uygun olmalıdır.
Microsoft ticari markalarının veya logolarının bu projenin değiştirilmiş sürümlerinde kullanımı, karışıklık yaratmamalı veya Microsoft sponsorluğunu ima etmemelidir.
Üçüncü taraf ticari markalarının veya logolarının herhangi bir kullanımı, o üçüncü tarafın politikalarına tabidir.

## Yardım Almak

Takılırsanız veya AI uygulamaları geliştirme ile ilgili herhangi bir sorunuz olursa katılın:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ürün geri bildirimi veya hata bildirimi yapmak için ziyaret edin:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->