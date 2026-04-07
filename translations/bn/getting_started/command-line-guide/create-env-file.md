# রুট ডিরেক্টরিতে *.env* ফাইল তৈরি করুন

এই টিউটোরিয়ালে, আমরা আপনাকে Azure পরিষেবাগুলির জন্য পরিবেশ ভেরিয়েবল সেটআপ করার নির্দেশনা দিবো *.env* ফাইল ব্যবহার করে। পরিবেশ ভেরিয়েবলগুলি আপনাকে নিরাপদে সংবেদনশীল ক্রেডেনশিয়ালগুলি, যেমন API কী, কোডবেসে হার্ড-কোড না করেই পরিচালনা করতে দেয়।

> [!IMPORTANT]
> - কেবল একটি ভাষা মডেল পরিষেবা (Azure OpenAI বা OpenAI) কনফিগার করা প্রয়োজন। আপনার পREFERRED পরিষেবার জন্য পরিবেশ ভেরিয়েবলগুলি পূরণ করুন। যদি একাধিক ভাষা মডেলের জন্য পরিবেশ ভেরিয়েবল সেট করা হয়, তাহলে কো-অপ ট্রান্সলেটর অগ্রাধিকারের ভিত্তিতে একটি নির্বাচন করবে।
> - যদি কম্পিউটার ভিশনের পরিবেশ ভেরিয়েবল সেট না করা থাকে, ট্রান্সলেটর স্বয়ংক্রিয়ভাবে [Markdown-only mode](./markdown-only-mode.md)-এ সুইচ করবে।

> [!NOTE]
> এই গাইড প্রধানত Azure পরিষেবার ওপর ফোকাস করে, তবে আপনি [supported models and services list](../README.md#-supported-models-and-services)-এর যে কোনো সমর্থিত ভাষা মডেল বেছে নিতে পারেন।

## *.env* ফাইল তৈরি করুন

আপনার প্রকল্পের রুট ডিরেক্টরিতে *.env* নামে একটি ফাইল তৈরি করুন। এই ফাইলে আপনার সব পরিবেশ ভেরিয়েবলগুলি সহজ ফরম্যাটে সংরক্ষণ করা হবে।

> [!WARNING]
> আপনার *.env* ফাইলটি গিটের মতো ভার্শন কন্ট্রোল সিস্টেমে কমিট করবেন না। দুর্ঘটনাজনিত কমিট এড়াতে *.env* কে আপনার .gitignore ফাইলে যোগ করুন।

1. আপনার প্রকল্পের রুট ডিরেক্টরিতে যান।

1. প্রকল্পের রুট ডিরেক্টরিতে একটি *.env* ফাইল তৈরি করুন।

1. *.env* ফাইলটি খুলুন এবং নিচের টেম্পলেটটিকে পেস্ট করুন:

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
> আপনার API কী এবং এন্ডপয়েন্টগুলি খুঁজে পেতে চাইলে, আপনি [set-up-azure-ai.md](../set-up-azure-ai.md) দেখুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বিজ্ঞপ্তি**:  
এই ডকুমেন্টটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা যথাযথতার প্রচেষ্টা করি, দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথি তার নিজস্ব ভাষায় কর্তৃত্বমূলক উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারের ফলে উদ্ভূত যে কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->