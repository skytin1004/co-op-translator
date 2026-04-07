# การตั้งค่า Azure AI สำหรับ Co-op Translator (Azure OpneAI & Azure AI Vision)

คำแนะนำนี้จะนำคุณผ่านการตั้งค่า Azure OpenAI สำหรับการแปลภาษา และ Azure Computer Vision สำหรับการวิเคราะห์เนื้อหาภาพ (ซึ่งสามารถใช้สำหรับการแปลภาพ) ภายใน Azure AI Foundry

**ข้อกำหนดเบื้องต้น:**
- บัญชี Azure ที่มีการสมัครใช้งานที่ใช้งานอยู่
- สิทธิ์ที่เพียงพอในการสร้างทรัพยากรและการปรับใช้ในการสมัครใช้งาน Azure ของคุณ

## สร้างโครงการ Azure AI

คุณจะเริ่มต้นด้วยการสร้างโครงการ Azure AI ซึ่งทำหน้าที่เป็นศูนย์กลางสำหรับจัดการทรัพยากร AI ของคุณ

1. ไปที่ [https://ai.azure.com](https://ai.azure.com) และลงชื่อเข้าใช้ด้วยบัญชี Azure ของคุณ

1. เลือก **+Create** เพื่อสร้างโครงการใหม่

1. ดำเนินการดังต่อไปนี้:
   - กรอก **ชื่อโครงการ** (เช่น `CoopTranslator-Project`)
   - เลือก **AI hub**  (เช่น `CoopTranslator-Hub`) (สร้างใหม่หากจำเป็น)

1. คลิก "**Review and Create**" เพื่อสร้างโครงการของคุณ คุณจะถูกนำไปยังหน้าสรุปโครงการของคุณ

## ตั้งค่า Azure OpenAI สำหรับการแปลภาษา

ภายในโครงการของคุณ คุณจะปรับใช้โมเดล Azure OpenAI เพื่อทำหน้าที่เป็น backend สำหรับการแปลข้อความ

### ไปที่โครงการของคุณ

ถ้ายังไม่ได้อยู่ ให้เปิดโครงการที่คุณสร้างขึ้นใหม่ (เช่น `CoopTranslator-Project`) ใน Azure AI Foundry

### ปรับใช้โมเดล OpenAI

1. จากเมนูด้านซ้ายของโครงการคุณ ใต้ "My assets" เลือก "**Models + endpoints**"

1. เลือก **+ Deploy model**

1. เลือก **Deploy Base Model**

1. คุณจะเห็นรายชื่อโมเดลที่ใช้ได้ กรองหรือค้นหาโมเดล GPT ที่เหมาะสม เราแนะนำ `gpt-4o`

1. เลือกโมเดลที่ต้องการและคลิก **Confirm**

1. เลือก **Deploy**

### การกำหนดค่า Azure OpenAI

หลังจากการปรับใช้ คุณสามารถเลือกการปรับใช้จากหน้า "**Models + endpoints**" เพื่อดู **REST endpoint URL**, **Key**, **ชื่อการปรับใช้**, **ชื่อโมเดล** และ **เวอร์ชัน API** ซึ่งจะต้องใช้เพื่อนำโมเดลการแปลเข้าไปในแอปพลิเคชันของคุณ

> [!NOTE]
> คุณสามารถเลือกเวอร์ชัน API จากหน้า [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) ตามความต้องการของคุณ โปรดทราบว่า **เวอร์ชัน API** แตกต่างจาก **เวอร์ชันโมเดล** ที่แสดงในหน้า **Models + endpoints** ใน Azure AI Foundry

## ตั้งค่า Azure Computer Vision สำหรับการแปลภาพ

เพื่อเปิดใช้งานการแปลข้อความภายในภาพ คุณจะต้องค้นหา Azure AI Service API Key และ Endpoint

1. ไปที่โครงการ Azure AI ของคุณ (เช่น `CoopTranslator-Project`) ตรวจสอบให้แน่ใจว่าคุณอยู่ในหน้าสรุปโครงการ

### การกำหนดค่า Azure AI Service

ค้นหา API Key และ Endpoint จากแท็บ Azure AI Service

1. ไปที่โครงการ Azure AI ของคุณ (เช่น `CoopTranslator-Project`) ตรวจสอบให้แน่ใจว่าคุณอยู่ในหน้าสรุปโครงการ

1. ค้นหา **API Key** และ **Endpoint** จากแท็บ Azure AI Service

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

การเชื่อมต่อนี้ทำให้ความสามารถของทรัพยากร Azure AI Services ที่เชื่อมโยง (รวมถึงการวิเคราะห์ภาพ) สามารถใช้งานได้ในโครงการ AI Foundry ของคุณ จากนั้นคุณสามารถใช้การเชื่อมต่อนี้ในโน้ตบุ๊กหรือแอปพลิเคชันของคุณเพื่อสกัดข้อความจากภาพ ซึ่งต่อไปสามารถส่งไปยังโมเดล Azure OpenAI เพื่อแปลได้

## รวบรวมข้อมูลประจำตัวของคุณ

ตอนนี้คุณควรได้รวบรวมสิ่งต่อไปนี้:

**สำหรับ Azure OpenAI (การแปลข้อความ):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- ชื่อโมเดล Azure OpenAI (เช่น `gpt-4o`)
- ชื่อการปรับใช้ Azure OpenAI (เช่น `cooptranslator-gpt4o`)
- เวอร์ชัน API ของ Azure OpenAI

**สำหรับ Azure AI Services (การสกัดข้อความจากภาพผ่าน Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ตัวอย่าง: การกำหนดค่าตัวแปรสภาพแวดล้อม (Preview)

ในภายหลัง เมื่อสร้างแอปพลิเคชันของคุณ คุณน่าจะกำหนดค่ามันโดยใช้ข้อมูลประจำตัวที่รวบรวมไว้ เช่น อาจตั้งเป็นตัวแปรสภาพแวดล้อมดังนี้:

```bash
# ข้อมูลรับรองบริการ Azure AI (จำเป็นสำหรับการแปลภาพ)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # เช่น, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ชุดสำรองเลือกได้: ทำซ้ำตัวแปรโดยมีคำต่อท้าย _1/_2 (ใช้ดัชนีเดียวกันสำหรับตัวแปรทั้งหมดในชุด)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# ข้อมูลรับรอง Azure OpenAI (จำเป็นสำหรับการแปลข้อความ)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # เช่น, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # เช่น, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # เช่น, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # เช่น, 2024-12-01-preview

# ชุดสำรองเลือกได้: ทำซ้ำชุด AZURE_OPENAI_* ทั้งหมดโดยมีคำต่อท้าย _1/_2 (ใช้ดัชนีเดียวกันสำหรับตัวแปรทั้งหมด)
```

---

### การอ่านเพิ่มเติม

- [วิธีสร้างโครงการใน Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [วิธีสร้างทรัพยากร Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [วิธีปรับใช้โมเดล OpenAI ใน Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่ถูกต้อง สำหรับข้อมูลที่มีความสำคัญ ควรใช้บริการแปลโดยมืออาชีพที่เป็นมนุษย์ เราไม่มีความรับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่อาจเกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->