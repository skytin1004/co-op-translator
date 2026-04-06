# สร้างไฟล์ *.env* ในไดเรกทอรีรูท

ในบทช่วยสอนนี้ เราจะแนะนำวิธีตั้งค่าตัวแปรสภาพแวดล้อมสำหรับบริการ Azure โดยใช้ไฟล์ *.env* ตัวแปรสภาพแวดล้อมช่วยให้คุณจัดการข้อมูลรับรองที่ละเอียดอ่อน เช่น คีย์ API ได้อย่างปลอดภัยโดยไม่ต้องฝังลงในโค้ดของคุณ

> [!IMPORTANT]
> - ต้องกำหนดค่าบริการโมเดลภาษาหนึ่งบริการเท่านั้น (Azure OpenAI หรือ OpenAI) กรอกตัวแปรสภาพแวดล้อมสำหรับบริการที่คุณต้องการ หากตั้งค่าตัวแปรสภาพแวดล้อมสำหรับโมเดลภาษาหลายตัว แปลความร่วมมือจะเลือกหนึ่งตัวตามลำดับความสำคัญ
> - หากไม่ได้ตั้งค่าตัวแปรสภาพแวดล้อม Computer Vision ตัวแปลจะสลับไปที่ [โหมด Markdown เท่านั้น](./markdown-only-mode.md) อัตโนมัติ

> [!NOTE]
> คู่มือนี้เน้นที่บริการ Azure เป็นหลัก แต่คุณสามารถเลือกโมเดลภาษาที่รองรับใด ๆ จาก [รายการโมเดลและบริการที่รองรับ](../README.md#-supported-models-and-services)

## สร้างไฟล์ *.env*

ในไดเรกทอรีรูทของโปรเจกต์ของคุณ ให้สร้างไฟล์ชื่อ *.env* ไฟล์นี้จะเก็บตัวแปรสภาพแวดล้อมทั้งหมดของคุณในรูปแบบที่เรียบง่าย

> [!WARNING]
> อย่าคอมมิตไฟล์ *.env* ของคุณลงในระบบควบคุมเวอร์ชันเช่น Git ให้เพิ่ม *.env* ลงในไฟล์ .gitignore ของคุณเพื่อป้องกันการคอมมิตโดยไม่ตั้งใจ

1. ไปที่ไดเรกทอรีรูทของโปรเจกต์ของคุณ

1. สร้างไฟล์ *.env* ในไดเรกทอรีรูทของโปรเจกต์ของคุณ

1. เปิดไฟล์ *.env* และวางเทมเพลตต่อไปนี้:

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
> หากต้องการค้นหาคีย์ API และจุดสิ้นสุดของคุณ คุณสามารถอ้างอิงได้ที่ [set-up-azure-ai.md](../set-up-azure-ai.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ในขณะที่เราพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เป็นทางการ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->