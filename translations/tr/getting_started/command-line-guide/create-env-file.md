# Kök dizinde *.env* dosyasını oluşturun

Bu öğreticide, bir *.env* dosyası kullanarak Azure servisleri için ortam değişkenlerinizi nasıl ayarlayacağınızı göstereceğiz. Ortam değişkenleri, API anahtarları gibi hassas kimlik bilgilerini kod tabanınıza sert kodlama yapmadan güvenli bir şekilde yönetmenize olanak tanır.

> [!IMPORTANT]
> - Yalnızca bir dil modeli servisi (Azure OpenAI veya OpenAI) yapılandırılmalıdır. Tercih ettiğiniz servis için ortam değişkenlerini doldurun. Birden fazla dil modeli için ortam değişkenleri ayarlanırsa, co-op çevirmen önceliğe göre birini seçecektir.
> - Bilgisayarla Görüntü Ortam değişkenleri ayarlanmadıysa, çevirmen otomatik olarak [Sadece Markdown modu](./markdown-only-mode.md)'na geçecektir.

> [!NOTE]
> Bu kılavuz ağırlıklı olarak Azure servislerine odaklanmaktadır, ancak [desteklenen modeller ve servisler listesi](../README.md#-supported-models-and-services)'nden herhangi bir desteklenen dil modeli seçebilirsiniz.

## *.env* dosyasını oluşturun

Projenizin kök dizininde, *.env* adlı bir dosya oluşturun. Bu dosya, tüm ortam değişkenlerinizi basit bir formatta saklayacaktır.

> [!WARNING]
> *.env* dosyanızı Git gibi sürüm kontrol sistemlerine göndermeyin. Yanlışlıkla gönderimleri önlemek için *.env* dosyasını .gitignore dosyanıza ekleyin.

1. Projenizin kök dizinine gidin.

1. Projenizin kök dizininde *.env* dosyasını oluşturun.

1. *.env* dosyasını açın ve aşağıdaki şablonu yapıştırın:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> API anahtarlarınızı ve uç noktalarınızı bulmak isterseniz, [set-up-azure-ai.md](../set-up-azure-ai.md) dosyasına bakabilirsiniz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etmemize rağmen, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini unutmayınız. Orijinal belge, ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->