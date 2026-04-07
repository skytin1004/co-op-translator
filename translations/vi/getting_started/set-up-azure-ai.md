# Thiết lập Azure AI cho Co-op Translator (Azure OpneAI & Azure AI Vision)

Hướng dẫn này sẽ hướng dẫn bạn thiết lập Azure OpenAI để dịch ngôn ngữ và Azure Computer Vision để phân tích nội dung hình ảnh (sau đó có thể sử dụng để dịch dựa trên hình ảnh) trong Azure AI Foundry.

**Yêu cầu trước:**
- Một tài khoản Azure với đăng ký đang hoạt động.
- Quyền đủ để tạo tài nguyên và triển khai trong đăng ký Azure của bạn.

## Tạo một Dự án Azure AI

Bạn sẽ bắt đầu bằng cách tạo một Dự án Azure AI, đóng vai trò như một nơi trung tâm để quản lý các tài nguyên AI của bạn.

1. Điều hướng tới [https://ai.azure.com](https://ai.azure.com) và đăng nhập bằng tài khoản Azure của bạn.

1. Chọn **+Create** để tạo một dự án mới.

1. Thực hiện các tác vụ sau:
   - Nhập **Tên Dự án** (ví dụ, `CoopTranslator-Project`).
   - Chọn **AI hub** (ví dụ, `CoopTranslator-Hub`) (Tạo mới nếu cần).

1. Nhấn "**Review and Create**" để thiết lập dự án của bạn. Bạn sẽ được chuyển đến trang tổng quan dự án của mình.

## Thiết lập Azure OpenAI cho Dịch Ngôn ngữ

Trong dự án, bạn sẽ triển khai một mô hình Azure OpenAI để phục vụ như backend cho việc dịch văn bản.

### Điều hướng đến Dự án của bạn

Nếu chưa ở đó, mở dự án mới tạo (ví dụ, `CoopTranslator-Project`) trong Azure AI Foundry.

### Triển khai một Mô hình OpenAI

1. Từ menu bên trái của dự án, dưới "My assets", chọn "**Models + endpoints**".

1. Chọn **+ Deploy model**.

1. Chọn **Deploy Base Model**.

1. Bạn sẽ thấy danh sách các mô hình có sẵn. Lọc hoặc tìm kiếm một mô hình GPT phù hợp. Chúng tôi khuyên dùng `gpt-4o`.

1. Chọn mô hình bạn muốn và nhấn **Confirm**.

1. Chọn **Deploy**.

### Cấu hình Azure OpenAI

Khi đã triển khai, bạn có thể chọn triển khai từ trang "**Models + endpoints**" để lấy **URL REST endpoint**, **Key**, **Deployment name**, **Model name** và **API version**. Những thông tin này cần thiết để tích hợp mô hình dịch vào ứng dụng của bạn.

> [!NOTE]
> Bạn có thể chọn phiên bản API từ trang [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) dựa trên yêu cầu của bạn. Hãy lưu ý rằng **API version** khác với **Model version** được hiển thị trên trang **Models + endpoints** trong Azure AI Foundry.

## Thiết lập Azure Computer Vision cho Dịch Hình ảnh

Để cho phép dịch văn bản trong hình ảnh, bạn cần tìm Khóa API và Endpoint của Azure AI Service.

1. Điều hướng đến Dự án Azure AI của bạn (ví dụ, `CoopTranslator-Project`). Đảm bảo bạn đang ở trang tổng quan dự án.

### Cấu hình Dịch vụ Azure AI

Tìm Khóa API và Endpoint từ Dịch vụ Azure AI.

1. Điều hướng đến Dự án Azure AI của bạn (ví dụ, `CoopTranslator-Project`). Đảm bảo bạn đang ở trang tổng quan dự án.

1. Tìm **API Key** và **Endpoint** ở tab Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Kết nối này cho phép các khả năng của tài nguyên Azure AI Services liên kết (bao gồm phân tích hình ảnh) có sẵn cho dự án AI Foundry của bạn. Bạn có thể dùng kết nối này trong các notebook hoặc ứng dụng để trích xuất văn bản từ hình ảnh, sau đó gửi văn bản đó tới mô hình Azure OpenAI để dịch.

## Tổng hợp Thông tin Xác thực của bạn

Đến lúc này, bạn nên đã thu thập những thông tin sau:

**Cho Azure OpenAI (Dịch Văn bản):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Tên Mô hình Azure OpenAI (ví dụ, `gpt-4o`)
- Tên Triển khai Azure OpenAI (ví dụ, `cooptranslator-gpt4o`)
- Phiên bản API Azure OpenAI

**Cho Azure AI Services (Trích xuất Văn bản từ Hình ảnh qua Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Ví dụ: Cấu hình Biến Môi trường (Xem trước)

Sau này, khi xây dựng ứng dụng, bạn có thể cấu hình nó bằng các thông tin xác thực đã thu thập. Ví dụ, bạn có thể đặt chúng như biến môi trường như sau:

```bash
# Thông tin đăng nhập Dịch vụ AI Azure (Bắt buộc cho dịch hình ảnh)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ví dụ, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Bộ dự phòng tùy chọn: nhân bản biến với hậu tố _1/_2 (chỉ số giống nhau cho tất cả biến trong bộ)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Thông tin đăng nhập Azure OpenAI (Bắt buộc cho dịch văn bản)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ví dụ, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ví dụ, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ví dụ, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ví dụ, 2024-12-01-preview

# Bộ dự phòng tùy chọn: nhân bản toàn bộ tập AZURE_OPENAI_* với hậu tố _1/_2 (chỉ số giống nhau cho tất cả biến)
```

---

### Đọc thêm

- [Cách tạo dự án trong Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Cách tạo tài nguyên Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Cách triển khai mô hình OpenAI trong Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trách**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Trong khi chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính thống. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->