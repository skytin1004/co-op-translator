# Buat fail *.env* di direktori root

Dalam tutorial ini, kami akan membimbing anda melalui penyediaan pemboleh ubah persekitaran untuk perkhidmatan Azure menggunakan fail *.env*. Pemboleh ubah persekitaran membolehkan anda menguruskan kelayakan sensitif dengan selamat, seperti kunci API, tanpa perlu menyandarkan mereka secara terus dalam kod anda.

> [!IMPORTANT]
> - Hanya satu perkhidmatan model bahasa (Azure OpenAI atau OpenAI) perlu dikonfigurasi. Isikan pemboleh ubah persekitaran untuk perkhidmatan pilihan anda. Jika pemboleh ubah persekitaran untuk pelbagai model bahasa ditetapkan, penterjemah koperasi akan memilih satu berdasarkan keutamaan.
> - Jika pemboleh ubah persekitaran Computer Vision tidak ditetapkan, penterjemah akan secara automatik bertukar ke [mod Markdown sahaja](./markdown-only-mode.md).

> [!NOTE]
> Panduan ini terutamanya memfokuskan kepada perkhidmatan Azure, tetapi anda boleh memilih mana-mana model bahasa yang disokong dari [senarai model dan perkhidmatan yang disokong](../README.md#-supported-models-and-services).

## Buat fail *.env*

Di direktori root projek anda, buat fail bernama *.env*. Fail ini akan menyimpan semua pemboleh ubah persekitaran anda dalam format yang mudah.

> [!WARNING]
> Jangan komit fail *.env* anda ke sistem kawalan versi seperti Git. Tambahkan *.env* ke fail .gitignore anda untuk mengelakkan komit tidak sengaja.

1. Navigasi ke direktori root projek anda.

1. Buat fail *.env* di direktori root projek anda.

1. Buka fail *.env* dan tampal templat berikut:

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
> Jika anda ingin mencari kunci API dan titik akhir anda, anda boleh merujuk kepada [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->