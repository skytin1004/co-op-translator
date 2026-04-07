# Mengatur Azure AI untuk Co-op Translator (Azure OpneAI & Azure AI Vision)

Panduan ini akan memandu Anda dalam mengatur Azure OpenAI untuk terjemahan bahasa dan Azure Computer Vision untuk analisis konten gambar (yang kemudian dapat digunakan untuk terjemahan berbasis gambar) dalam Azure AI Foundry.

**Persyaratan:**
- Akun Azure dengan langganan aktif.
- Izin yang cukup untuk membuat sumber daya dan deployment dalam langganan Azure Anda.

## Membuat Proyek Azure AI

Anda akan memulai dengan membuat Proyek Azure AI, yang berfungsi sebagai pusat pengelolaan sumber daya AI Anda.

1. Buka [https://ai.azure.com](https://ai.azure.com) dan masuk dengan akun Azure Anda.

1. Pilih **+Create** untuk membuat proyek baru.

1. Lakukan tugas berikut:
   - Masukkan **Nama Proyek** (misalnya, `CoopTranslator-Project`).
   - Pilih **AI hub** (misalnya, `CoopTranslator-Hub`) (Buat baru jika perlu).

1. Klik "**Review and Create**" untuk menyiapkan proyek Anda. Anda akan dibawa ke halaman ringkasan proyek Anda.

## Mengatur Azure OpenAI untuk Terjemahan Bahasa

Dalam proyek Anda, Anda akan melakukan deployment model Azure OpenAI untuk berfungsi sebagai backend untuk terjemahan teks.

### Buka Proyek Anda

Jika belum berada di sana, buka proyek yang baru dibuat (misalnya, `CoopTranslator-Project`) di Azure AI Foundry.

### Deploy Model OpenAI

1. Dari menu sebelah kiri proyek Anda, di bawah "My assets", pilih "**Models + endpoints**".

1. Pilih **+ Deploy model**.

1. Pilih **Deploy Base Model**.

1. Anda akan melihat daftar model yang tersedia. Saring atau cari model GPT yang sesuai. Kami merekomendasikan `gpt-4o`.

1. Pilih model yang diinginkan dan klik **Confirm**.

1. Pilih **Deploy**.

### Konfigurasi Azure OpenAI

Setelah deployment, Anda dapat memilih deployment dari halaman "**Models + endpoints**" untuk menemukan **REST endpoint URL**, **Key**, **Deployment name**, **Model name**, dan **API version**. Data ini dibutuhkan untuk mengintegrasikan model terjemahan ke aplikasi Anda.

> [!NOTE]
> Anda dapat memilih versi API dari halaman [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) sesuai kebutuhan Anda. Perlu diketahui bahwa **API version** berbeda dengan **Model version** yang ditampilkan pada halaman **Models + endpoints** di Azure AI Foundry.

## Mengatur Azure Computer Vision untuk Terjemahan Gambar

Untuk memungkinkan terjemahan teks dalam gambar, Anda perlu menemukan Azure AI Service API Key dan Endpoint.

1. Buka Proyek Azure AI Anda (misalnya, `CoopTranslator-Project`). Pastikan Anda berada di halaman ringkasan proyek.

### Konfigurasi Azure AI Service

Temukan API Key dan Endpoint dari Layanan Azure AI.

1. Buka Proyek Azure AI Anda (misalnya, `CoopTranslator-Project`). Pastikan Anda berada di halaman ringkasan proyek.

1. Temukan **API Key** dan **Endpoint** dari tab Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Koneksi ini membuat kemampuan sumber daya Azure AI Services terkait (termasuk analisis gambar) tersedia untuk proyek AI Foundry Anda. Anda kemudian dapat menggunakan koneksi ini di notebook atau aplikasi untuk mengekstrak teks dari gambar, yang selanjutnya dapat dikirim ke model Azure OpenAI untuk diterjemahkan.

## Mengkonsolidasikan Kredensial Anda

Saat ini, Anda seharusnya telah mengumpulkan yang berikut:

**Untuk Azure OpenAI (Terjemahan Teks):**
- Endpoint Azure OpenAI
- API Key Azure OpenAI
- Nama Model Azure OpenAI (misalnya, `gpt-4o`)
- Nama Deployment Azure OpenAI (misalnya, `cooptranslator-gpt4o`)
- Versi API Azure OpenAI

**Untuk Azure AI Services (Ekstraksi Teks Gambar melalui Vision):**
- Endpoint Azure AI Service
- API Key Azure AI Service

### Contoh: Konfigurasi Variabel Lingkungan (Pratinjau)

Nantinya, saat membangun aplikasi Anda, Anda kemungkinan akan mengkonfigurasinya menggunakan kredensial yang telah dikumpulkan ini. Misalnya, Anda mungkin menetapkannya sebagai variabel lingkungan seperti berikut:

```bash
# Kredensial Layanan AI Azure (Diperlukan untuk terjemahan gambar)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # misalnya, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Set cadangan opsional: duplikat variabel dengan akhiran _1/_2 (indeks yang sama untuk semua variabel dalam set)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Kredensial Azure OpenAI (Diperlukan untuk terjemahan teks)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # misalnya, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # misalnya, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # misalnya, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # misalnya, 2024-12-01-preview

# Set cadangan opsional: duplikat seluruh set AZURE_OPENAI_* dengan akhiran _1/_2 (indeks yang sama untuk semua variabel)
```

---

### Bacaan Lanjutan

- [Cara Membuat proyek di Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Cara Membuat sumber daya Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Cara Me-deploy model OpenAI di Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->