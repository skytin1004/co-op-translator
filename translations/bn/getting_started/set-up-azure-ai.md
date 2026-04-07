# Co-op Translator এর জন্য Azure AI সেট আপ করুন (Azure OpneAI ও Azure AI Vision)

এই নির্দেশিকা আপনাকে Azure AI Foundry এর মধ্যে ভাষা অনুবাদের জন্য Azure OpenAI এবং ছবি বিষয়বস্তু বিশ্লেষণের জন্য Azure Computer Vision (যা পরে ছবি ভিত্তিক অনুবাদের জন্য ব্যবহার করা যেতে পারে) সেটআপ করার প্রক্রিয়া দেখাবে।

**প্রয়োজনীয়তা:**
- একটি সক্রিয় সাবস্ক্রিপশন সহ Azure খাতা।
- আপনার Azure সাবস্ক্রিপশনে রিসোর্স এবং ডিপ্লয়মেন্ট তৈরি করার যথেষ্ট অনুমতি।

## একটি Azure AI প্রকল্প তৈরি করুন

আপনি Azure AI প্রকল্প তৈরি করার মাধ্যমে শুরু করবেন, যা আপনার AI রিসোর্সগুলি পরিচালনার জন্য একটি কেন্দ্রীয় স্থান হিসেবে কাজ করে।

1. [https://ai.azure.com](https://ai.azure.com) এ যান এবং আপনার Azure একাউন্ট দিয়ে সাইন ইন করুন।

1. একটি নতুন প্রকল্প তৈরি করতে **+Create** নির্বাচন করুন।

1. নিম্নলিখিত কাজগুলি সম্পাদন করুন:
   - একটি **Project name** লিখুন (যেমন, `CoopTranslator-Project`)।
   - **AI hub** নির্বাচন করুন (যেমন, `CoopTranslator-Hub`) (প্রয়োজনে নতুন একটি তৈরি করুন)।

1. আপনার প্রকল্প সেটআপ করতে "**Review and Create**" ক্লিক করুন। আপনাকে আপনার প্রকল্পের ওভারভিউ পৃষ্ঠায় নিয়ে যাওয়া হবে।

## ভাষা অনুবাদের জন্য Azure OpenAI সেট আপ করুন

আপনার প্রকল্পের মধ্যে, আপনি একটি Azure OpenAI মডেল ডিপ্লয় করবেন যা পাঠ্য অনুবাদের জন্য ব্যাকএন্ড হিসেবে কাজ করবে।

### আপনার প্রকল্পে নেভিগেট করুন

যদি ইতিমধ্যে না থেকে থাকে, আপনার সদ্য তৈরি করা প্রকল্পটি (যেমন, `CoopTranslator-Project`) Azure AI Foundry তে খুলুন।

### একটি OpenAI মডেল ডিপ্লয় করুন

1. আপনার প্রকল্পের বাম দিকের মেনু থেকে, "My assets" এর অধীনে, "**Models + endpoints**" নির্বাচন করুন।

1. **+ Deploy model** নির্বাচন করুন।

1. **Deploy Base Model** নির্বাচন করুন।

1. উপলব্ধ মডেলের একটি তালিকা আপনাকে দেখানো হবে। একটি উপযুক্ত GPT মডেল ফিল্টার করুন বা সন্ধান করুন। আমরা `gpt-4o` সুপারিশ করি।

1. আপনার পছন্দসই মডেল নির্বাচন করুন এবং **Confirm** ক্লিক করুন।

1. **Deploy** নির্বাচন করুন।

### Azure OpenAI কনফিগারেশন

একবার ডিপ্লয় হলে, আপনি "**Models + endpoints**" পাতাটি থেকে ডিপ্লয়মেন্ট সিলেক্ট করে এর **REST endpoint URL**, **Key**, **Deployment name**, **Model name** এবং **API version** দেখতে পারবেন। এগুলি আপনার অ্যাপ্লিকেশনে অনুবাদ মডেল সংযুক্ত করার জন্য প্রয়োজন।

> [!NOTE]
> আপনার প্রয়োজন অনুসারে [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) পেজ থেকে API ভার্সন নির্বাচন করতে পারেন। মনে রাখবেন, **API version** হল Azure AI Foundry এর "**Models + endpoints**" পেজে প্রদর্শিত **Model version** থেকে ভিন্ন।

## ছবি অনুবাদের জন্য Azure Computer Vision সেটআপ করুন

চিত্রের মধ্যে লেখা অনুবাদের সক্ষমতা সক্ষম করতে, আপনাকে Azure AI Service এর API Key এবং Endpoint খুঁজে বের করতে হবে।

1. আপনার Azure AI প্রকল্প (যেমন, `CoopTranslator-Project`) এ নেভিগেট করুন। নিশ্চিত করুন আপনি প্রকল্পের ওভারভিউ পৃষ্ঠায় আছেন।

### Azure AI Service কনফিগারেশন

Azure AI Service থেকে API Key এবং Endpoint খুঁজুন।

1. আপনার Azure AI প্রকল্পে (যেমন, `CoopTranslator-Project`) যান। নিশ্চিত করুন আপনি প্রকল্পের ওভারভিউ পৃষ্ঠায় আছেন।

1. Azure AI Service ট্যাব থেকে **API Key** এবং **Endpoint** খুঁজুন।

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

এই সংযোগটি সংযুক্ত Azure AI Services রিসোর্সের ক্ষমতা (ছবি বিশ্লেষণ সহ) আপনার AI Foundry প্রকল্পে উপলব্ধ করে। তারপর আপনি আপনার নোটবুক বা অ্যাপ্লিকেশনগুলিতে এই সংযোগ ব্যবহার করে ছবির থেকে লেখা আহরণ করতে পারেন, যা পরে অনুবাদের জন্য Azure OpenAI মডেলে পাঠানো যাবে।

## আপনার শংসাপত্রগুলো একত্রিত করা

এখন পর্যন্ত, আপনাকে নিম্নলিখিত জিনিসগুলো সংগ্রহ করা উচিত:

**Azure OpenAI (টেক্সট অনুবাদ) এর জন্য:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (যেমন, `gpt-4o`)
- Azure OpenAI Deployment Name (যেমন, `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (ভিশনের মাধ্যমে ছবি লেখা আহরণ) এর জন্য:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### উদাহরণ: পরিবেশ পরিবর্তনশীল কনফিগারেশন (পূর্বাবস্থা)

পরে, আপনার অ্যাপ্লিকেশন তৈরি করার সময়, আপনি সম্ভবত এগুলোকে পরিবেশ পরিবর্তনশীল হিসেবে কনফিগার করবেন, উদাহরণস্বরূপ:

```bash
# আজুর এআই সার্ভিস ক্রিডেনশিয়ালস (ছবি অনুবাদের জন্য প্রয়োজন)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # উদাহরণস্বরূপ, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ঐচ্ছিক ফ্যালব্যাক সেট: ভ্যারিয়েবলগুলির সাথে অতিরিক্ত _1/_2 (সেটের সকল ভ্যারিয়েবলের জন্য একই সূচক)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# আজুর ওপেনএআই ক্রিডেনশিয়ালস (টেক্সট অনুবাদের জন্য প্রয়োজন)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # উদাহরণস্বরূপ, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # উদাহরণস্বরূপ, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # উদাহরণস্বরূপ, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # উদাহরণস্বরূপ, 2024-12-01-প্রিভিউ

# ঐচ্ছিক ফ্যালব্যাক সেট: সম্পূর্ণ AZURE_OPENAI_* সেটটির নকল suffix _1/_2 সহ (সকল ভ্যারিয়েবলের জন্য একই সূচক)
```

---

### আরও পড়ুন

- [Azure AI Foundry এ কীভাবে একটি প্রকল্প তৈরি করবেন](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI রিসোর্স কীভাবে তৈরি করবেন](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry এ OpenAI মডেল কীভাবে ডিপ্লয় করবেন](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই ডকুমেন্টটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে বুঝবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় লেখা ডকুমেন্টটিকেই সর্বোচ্চ অথরিটেটিভ সূত্র হিসেবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে যে কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নয়।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->