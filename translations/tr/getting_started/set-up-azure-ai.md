# Co-op Translator için Azure AI Kurulumu (Azure OpenAI & Azure AI Vision)

Bu kılavuz, dil çevirisi için Azure OpenAI ve Azure AI Foundry içinde görüntü tabanlı çeviri için kullanılabilecek görüntü içeriği analizi için Azure Computer Vision kurulumu adımlarını size göstermektedir.

**Ön Koşullar:**
- Aktif aboneliğe sahip bir Azure hesabı.
- Azure aboneliğinizde kaynaklar ve dağıtımlar oluşturmak için yeterli izinler.

## Bir Azure AI Projesi Oluşturun

Yapay zeka kaynaklarınızı yönetmek için merkezi bir yer olarak hizmet veren bir Azure AI Projesi oluşturarak başlayacaksınız.

1. [https://ai.azure.com](https://ai.azure.com) adresine gidin ve Azure hesabınızla oturum açın.

1. Yeni bir proje oluşturmak için **+Create** seçeneğini belirleyin.

1. Aşağıdaki görevleri yapın:
   - Bir **Proje adı** girin (örneğin, `CoopTranslator-Project`).
   - **AI hub** seçin (örneğin, `CoopTranslator-Hub`) (Gerekirse yeni bir tane oluşturun).

1. Projenizi oluşturmak için "**Review and Create**" seçeneğine tıklayın. Projenizin genel bakış sayfasına yönlendirileceksiniz.

## Dil Çevirisi için Azure OpenAI Kurulumu

Projeniz içinde, metin çevirisi için backend olarak hizmet verecek bir Azure OpenAI modeli dağıtacaksınız.

### Projenize Gidin

Henüz yapmadıysanız, Azure AI Foundry'de yeni oluşturduğunuz projeyi (örneğin, `CoopTranslator-Project`) açın.

### Bir OpenAI Modeli Dağıtın

1. Projenizin sol menüsünden, "My assets" altında "**Models + endpoints**" seçeneğini tıklayın.

1. **+ Deploy model** seçeneğini seçin.

1. **Deploy Base Model** seçin.

1. Mevcut modellerin listesi gösterilecektir. Uygun bir GPT modeli arayın veya filtreleyin. `gpt-4o` modelini öneriyoruz.

1. İstediğiniz modeli seçin ve **Confirm** butonuna tıklayın.

1. **Deploy** seçeneğini seçin.

### Azure OpenAI yapılandırması

Model dağıtıldıktan sonra, "**Models + endpoints**" sayfasından dağıtımı seçerek **REST endpoint URL'si**, **Anahtar**, **Dağıtım adı**, **Model adı** ve **API sürümü** bilgilerini görebilirsiniz. Bunlar, çeviri modelini uygulamanıza entegre etmek için gerekecektir.

> [!NOTE]
> İhtiyaçlarınıza göre API sürümlerini [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) sayfasından seçebilirsiniz. Azure AI Foundry'deki **Models + endpoints** sayfasında gösterilen **Model sürümü** ile **API sürümü**nin farklı olduğunu unutmayın.

## Görüntü Çevirisi için Azure Computer Vision Kurulumu

Görüntü içindeki metinlerin çevirisini etkinleştirmek için Azure AI Hizmeti API Anahtarını ve Uç Noktasını bulmanız gerekir.

1. Azure AI Projenize (örneğin, `CoopTranslator-Project`) gidin. Proje genel bakış sayfasında olduğunuzdan emin olun.

### Azure AI Hizmeti yapılandırması

Azure AI Hizmeti'nden API Anahtarı ve Uç Noktayı bulun.

1. Azure AI Projenize (örneğin, `CoopTranslator-Project`) gidin. Proje genel bakış sayfasında olduğunuzdan emin olun.

1. Azure AI Hizmeti sekmesinden **API Anahtarı** ve **Uç Noktayı** bulun.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Bu bağlantı, bağlı Azure AI Hizmetleri kaynağının (görüntü analizi dahil) özelliklerini AI Foundry projenize sunar. Daha sonra bu bağlantıyı not defterlerinizde veya uygulamalarınızda görüntülerden metin çıkarmak için kullanabilir, ardından bu metni çeviri için Azure OpenAI modeline gönderebilirsiniz.

## Kimlik Bilgilerinizi Konsolide Etme

Şimdiye kadar aşağıdaki bilgileri toplamanız gerekir:

**Azure OpenAI için (Metin Çevirisi):**
- Azure OpenAI Uç Noktası
- Azure OpenAI API Anahtarı
- Azure OpenAI Model Adı (örneğin, `gpt-4o`)
- Azure OpenAI Dağıtım Adı (örneğin, `cooptranslator-gpt4o`)
- Azure OpenAI API Sürümü

**Azure AI Hizmetleri için (Vision ile Görüntüden Metin Çıkarma):**
- Azure AI Hizmeti Uç Noktası
- Azure AI Hizmeti API Anahtarı

### Örnek: Ortam Değişkeni Yapılandırması (Önizleme)

Daha sonra uygulamanızı oluştururken, bu kimlik bilgilerini büyük ihtimalle ortam değişkenleri olarak yapılandıracaksınız. Örneğin, şöyle ayarlayabilirsiniz:

```bash
# Azure AI Servis Kimlik Bilgileri (Görüntü çevirisi için gereklidir)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # Örneğin, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Opsiyonel yedek setler: _1/_2 son eki ile çoğaltılmış değişkenler (set içindeki tüm değişkenler için aynı indeks)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI Kimlik Bilgileri (Metin çevirisi için gereklidir)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # Örneğin, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # Örneğin, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # Örneğin, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # Örneğin, 2024-12-01-preview

# Opsiyonel yedek setler: AZURE_OPENAI_* tam setini _1/_2 son eki ile çoğaltın (tüm değişkenler için aynı indeks)
```

---

### Daha Fazla Okuma

- [Azure AI Foundry'de bir proje nasıl oluşturulur](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI kaynakları nasıl oluşturulur](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundryde OpenAI modelleri nasıl dağıtılır](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->