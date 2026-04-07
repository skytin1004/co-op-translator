# Tạo file *.env* trong thư mục gốc

Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn thiết lập các biến môi trường cho các dịch vụ Azure sử dụng file *.env*. Các biến môi trường cho phép bạn quản lý bảo mật các thông tin nhạy cảm, chẳng hạn như khóa API, mà không cần mã hóa trực tiếp vào mã nguồn của bạn.

> [!IMPORTANT]
> - Chỉ cần cấu hình một dịch vụ mô hình ngôn ngữ (Azure OpenAI hoặc OpenAI). Điền các biến môi trường cho dịch vụ bạn ưu tiên. Nếu các biến môi trường cho nhiều mô hình ngôn ngữ được thiết lập, co-op translator sẽ chọn một mô hình dựa trên ưu tiên.
> - Nếu các biến môi trường Computer Vision không được thiết lập, trình dịch sẽ tự động chuyển sang [chế độ chỉ Markdown](./markdown-only-mode.md).

> [!NOTE]
> Hướng dẫn này chủ yếu tập trung vào các dịch vụ Azure, nhưng bạn có thể chọn bất kỳ mô hình ngôn ngữ nào được hỗ trợ từ [danh sách các mô hình và dịch vụ được hỗ trợ](../README.md#-supported-models-and-services).

## Tạo file *.env*

Trong thư mục gốc của dự án của bạn, tạo một file có tên *.env*. File này sẽ lưu trữ tất cả các biến môi trường của bạn dưới định dạng đơn giản.

> [!WARNING]
> Không commit file *.env* của bạn vào các hệ thống quản lý phiên bản như Git. Thêm *.env* vào file .gitignore của bạn để tránh commit nhầm.

1. Chuyển đến thư mục gốc của dự án của bạn.

1. Tạo một file *.env* trong thư mục gốc của dự án của bạn.

1. Mở file *.env* và dán mẫu sau:

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
> Nếu bạn muốn tìm các khóa API và điểm cuối của mình, bạn có thể tham khảo [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo tính chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được xem là nguồn tham khảo chính thống. Đối với thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->