# Kök dizinde *.env* dosyasını oluşturun

Bu öğreticide, Azure hizmetleri için ortam değişkenlerinizi *.env* dosyası kullanarak nasıl ayarlayacağınızı anlatacağız. Ortam değişkenleri, API anahtarları gibi gizli kimlik bilgilerini güvenli bir şekilde yönetmenize olanak tanır ve bunları kod tabanınıza sabitlemeden saklamanızı sağlar.

> [!IMPORTANT]
> - Sadece bir dil modeli servisi (Azure OpenAI veya OpenAI) yapılandırılması gerekir. Tercih ettiğiniz hizmetin ortam değişkenlerini doldurun. Birden fazla dil modeli için ortam değişkenleri ayarlanırsa, co-op translator önceliğe göre birini seçer.
> - Eğer Computer Vision ortam değişkenleri ayarlanmazsa, çevirmen otomatik olarak [sadece Markdown modu](./markdown-only-mode.md) üzerinden çalışır.

> [!NOTE]
> Bu rehber öncelikle Azure hizmetlerine odaklanmaktadır, ancak [desteklenen modeller ve hizmetler listesi](../README.md#-supported-models-and-services) içerisinden herhangi bir desteklenen dil modelini seçebilirsiniz.

## *.env* dosyasını oluşturun

Projenizin kök dizininde, *.env* adlı bir dosya oluşturun. Bu dosya, tüm ortam değişkenlerinizi basit bir formatta saklayacaktır.

> [!WARNING]
> *.env* dosyanızı Git gibi sürüm kontrol sistemlerine göndermeyin. Yanlışlıkla gönderilmeyi önlemek için *.env* dosyasını .gitignore dosyanıza ekleyin.

1. Projenizin kök dizinine gidin.

1. Projenizin kök dizininde bir *.env* dosyası oluşturun.

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
> API anahtarlarınızı ve uç noktalarınızı bulmak isterseniz, [set-up-azure-ai.md](../set-up-azure-ai.md) dosyasına başvurabilirsiniz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->