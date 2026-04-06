# রুট ডিরেক্টরিতে *.env* ফাইল তৈরি করুন

এই টিউটোরিয়ালে, আমরা আপনাকে Azure পরিষেবার জন্য আপনার পরিবেশ ভেরিয়েবলগুলি একটি *.env* ফাইল ব্যবহার করে সেট আপ করার জন্য নির্দেশনা দেব। পরিবেশ ভেরিয়েবলগুলি আপনাকে সংবেদনশীল ক্রেডেনশিয়াল, যেমন API কী, নিরাপদভাবে পরিচালনা করার সুযোগ দেয়, যা আপনার কোডবেসে হার্ড-কোড করা হয় না।

> [!IMPORTANT]
> - শুধুমাত্র একটি ভাষা মডেল পরিষেবা (Azure OpenAI অথবা OpenAI) কনফিগার করতে হবে। আপনার পছন্দসই পরিষেবার জন্য পরিবেশ ভেরিয়েবলগুলি পূরণ করুন। যদি একাধিক ভাষা মডেলের জন্য পরিবেশ ভেরিয়েবল সেট করা থাকে, তবে co-op translator অগ্রাধিকারের ভিত্তিতে একটি নির্বাচন করবে।
> - যদি Computer Vision পরিবেশ ভেরিয়েবল সেট না করা হয়, তবে অনুবাদক স্বয়ংক্রিয়ভাবে [Markdown-only mode](./markdown-only-mode.md) এ স্যুইচ করবে।

> [!NOTE]
> এই নির্দেশিকা মূলত Azure পরিষেবাগুলির উপর ফোকাস করে, তবে আপনি [supported models and services list](../README.md#-supported-models-and-services) থেকে যেকোন সমর্থিত ভাষা মডেল বেছে নিতে পারেন।

## *.env* ফাইল তৈরি করুন

আপনার প্রকল্পের রুট ডিরেক্টরিতে, একটি ফাইল তৈরি করুন যার নাম হবে *.env*। এই ফাইলটি আপনার সমস্ত পরিবেশ ভেরিয়েবলগুলোকে সহজ ফরম্যাটে সংরক্ষণ করবে।

> [!WARNING]
> আপনার *.env* ফাইলটি গিটের মত ভার্সন কন্ট্রোল সিস্টেমে কমিট করবেন না। দুর্ঘটনাজনিত কমিট প্রতিরোধে *.env* ফাইলকে আপনার .gitignore ফাইলে যুক্ত করুন।

1. আপনার প্রকল্পের রুট ডিরেক্টরিতে যান।

1. প্রকল্পের রুট ডিরেক্টরিতে একটি *.env* ফাইল তৈরি করুন।

1. *.env* ফাইলটি খুলুন এবং নিম্নলিখিত টেমপ্লেটটি পেস্ট করুন:

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
> যদি আপনি আপনার API কী এবং এন্ডপয়েন্টগুলি খুঁজে পেতে চান, তবে আপনি [set-up-azure-ai.md](../set-up-azure-ai.md) রেফার করতে পারেন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকারোক্তি**:  
এই নথিটি এআই অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে জানুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। আসল নথিটি তার স্থানীয় ভাষায় কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে উদ্ভূত কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->