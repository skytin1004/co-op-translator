# สร้างไฟล์ *.env* ในไดเรกทอรีราก

ในบทแนะนำนี้ เราจะแนะนำวิธีการตั้งค่าตัวแปรแวดล้อมสำหรับบริการ Azure โดยใช้ไฟล์ *.env* ตัวแปรแวดล้อมช่วยให้คุณจัดการข้อมูลรับรองที่ละเอียดอ่อนอย่างปลอดภัย เช่น คีย์ API โดยไม่ต้องเขียนโค้ดลงในฐานโค้ดของคุณโดยตรง

> [!IMPORTANT]
> - ต้องกำหนดค่าบริการโมเดลภาษาเพียงบริการเดียวเท่านั้น (Azure OpenAI หรือ OpenAI) ให้กรอกตัวแปรแวดล้อมสำหรับบริการที่คุณต้องการใช้ หากตั้งค่าตัวแปรแวดล้อมสำหรับโมเดลภาษาหลายตัวพร้อมกัน ไกด์แปลร่วมจะเลือกหนึ่งบริการตามลำดับความสำคัญ
> - หากไม่ได้ตั้งค่าตัวแปรแวดล้อม Computer Vision ไกด์แปลจะเปลี่ยนเป็น [โหมด Markdown เท่านั้น](./markdown-only-mode.md) โดยอัตโนมัติ

> [!NOTE]
> คู่มือนี้เน้นบริการ Azure เป็นหลัก แต่คุณสามารถเลือกโมเดลภาษาใดก็ได้ที่รองรับจาก [รายชื่อโมเดลและบริการที่รองรับ](../README.md#-supported-models-and-services)

## สร้างไฟล์ *.env*

ในไดเรกทอรีรากของโปรเจกต์ของคุณ ให้สร้างไฟล์ชื่อ *.env* ไฟล์นี้จะเก็บตัวแปรแวดล้อมทั้งหมดในรูปแบบง่ายๆ

> [!WARNING]
> อย่าทำการคอมมิตไฟล์ *.env* ของคุณลงในระบบควบคุมเวอร์ชัน เช่น Git ให้เพิ่ม *.env* ลงในไฟล์ .gitignore เพื่อป้องกันการคอมมิตโดยไม่ตั้งใจ

1. ไปที่ไดเรกทอรีรากของโปรเจกต์ของคุณ

1. สร้างไฟล์ *.env* ในไดเรกทอรีรากของโปรเจกต์ของคุณ

1. เปิดไฟล์ *.env* และวางเทมเพลตต่อไปนี้ลงไป:

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
> หากคุณต้องการค้นหาคีย์ API และจุดสิ้นสุดของคุณ คุณสามารถดูได้ที่ [set-up-azure-ai.md](../set-up-azure-ai.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้การแปลโดยผู้เชี่ยวชาญ ทางเราจะไม่รับผิดชอบในความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->