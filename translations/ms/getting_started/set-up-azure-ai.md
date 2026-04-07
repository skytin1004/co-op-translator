# Tetapkan Azure AI untuk Co-op Translator (Azure OpneAI & Azure AI Vision)

Panduan ini membimbing anda melalui proses menyiapkan Azure OpenAI untuk penterjemahan bahasa dan Azure Computer Vision untuk analisis kandungan imej (yang kemudian boleh digunakan untuk penterjemahan berasaskan imej) dalam Azure AI Foundry.

**Prasyarat:**
- Akaun Azure dengan langganan yang aktif.
- Kebenaran mencukupi untuk mencipta sumber dan deployment dalam langganan Azure anda.

## Cipta Projek Azure AI

Anda akan bermula dengan mencipta Projek Azure AI, yang bertindak sebagai tempat pusat untuk menguruskan sumber AI anda.

1. Navigasi ke [https://ai.azure.com](https://ai.azure.com) dan log masuk dengan akaun Azure anda.

1. Pilih **+Create** untuk mencipta projek baru.

1. Lakukan tugasan berikut:
   - Masukkan **Nama Projek** (contoh, `CoopTranslator-Project`).
   - Pilih **AI hub** (contoh, `CoopTranslator-Hub`) (Cipta yang baru jika perlu).

1. Klik "**Review and Create**" untuk menyiapkan projek anda. Anda akan dibawa ke halaman gambaran projek anda.

## Tetapkan Azure OpenAI untuk Penterjemahan Bahasa

Dalam projek anda, anda akan memdeploy model Azure OpenAI untuk berfungsi sebagai backend bagi penterjemahan teks.

### Navigasi ke Projek Anda

Jika belum berada di sana, buka projek yang baru anda cipta (contoh, `CoopTranslator-Project`) dalam Azure AI Foundry.

### Deploy Model OpenAI

1. Dari menu sebelah kiri projek anda, bawah "My assets", pilih "**Models + endpoints**".

1. Pilih **+ Deploy model**.

1. Pilih **Deploy Base Model**.

1. Anda akan dipaparkan dengan senarai model yang tersedia. Tapis atau cari model GPT yang sesuai. Kami mengesyorkan `gpt-4o`.

1. Pilih model yang dikehendaki dan klik **Confirm**.

1. Pilih **Deploy**.

### Konfigurasi Azure OpenAI

Selepas deployment, anda boleh memilih deployment dari halaman "**Models + endpoints**" untuk mencari **REST endpoint URL**, **Kunci**, **Nama deployment**, **Nama model** dan **Versi API**. Semua ini diperlukan untuk mengintegrasikan model penterjemahan ke dalam aplikasi anda.

> [!NOTE]
> Anda boleh memilih versi API dari halaman [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) berdasarkan keperluan anda. Perlu diingat bahawa **Versi API** berbeza daripada **Versi Model** yang dipaparkan pada halaman **Models + endpoints** dalam Azure AI Foundry.

## Tetapkan Azure Computer Vision untuk Penterjemahan Imej

Untuk membolehkan penterjemahan teks dalam imej, anda perlu mencari Kunci API dan Endpoint Azure AI Service.

1. Navigasi ke Projek Azure AI anda (contoh, `CoopTranslator-Project`). Pastikan anda berada di halaman gambaran projek.

### Konfigurasi Perkhidmatan Azure AI

Cari Kunci API dan Endpoint dari Perkhidmatan Azure AI.

1. Navigasi ke Projek Azure AI anda (contoh, `CoopTranslator-Project`). Pastikan anda berada di halaman gambaran projek.

1. Cari **Kunci API** dan **Endpoint** pada tab Perkhidmatan Azure AI.

    ![Cari Kunci API dan Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Sambungan ini membolehkan kemampuan sumber Perkhidmatan Azure AI yang dipautkan (termasuk analisis imej) tersedia untuk projek AI Foundry anda. Anda boleh menggunakan sambungan ini dalam notebook atau aplikasi anda untuk mengekstrak teks dari imej, yang kemudian boleh dihantar ke model Azure OpenAI untuk penterjemahan.

## Menggabungkan Kredensial Anda

Setakat ini, anda sepatutnya telah mengumpul perkara berikut:

**Untuk Azure OpenAI (Penterjemahan Teks):**
- Endpoint Azure OpenAI
- Kunci API Azure OpenAI
- Nama Model Azure OpenAI (contoh, `gpt-4o`)
- Nama Deployment Azure OpenAI (contoh, `cooptranslator-gpt4o`)
- Versi API Azure OpenAI

**Untuk Perkhidmatan Azure AI (Pengekstrakan Teks Imej melalui Vision):**
- Endpoint Perkhidmatan Azure AI
- Kunci API Perkhidmatan Azure AI

### Contoh: Konfigurasi Pembolehubah Persekitaran (Pratonton)

Kemudian, semasa membina aplikasi anda, anda mungkin akan mengkonfigurasikannya menggunakan kredensial yang dikumpulkan ini. Sebagai contoh, anda mungkin menetapkannya sebagai pembolehubah persekitaran seperti ini:

```bash
# Kredit Perkhidmatan Azure AI (Diperlukan untuk terjemahan imej)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # contohnya, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Set sandaran pilihan: duplikasi pembolehubah dengan akhiran _1/_2 (indeks yang sama untuk semua pembolehubah dalam set)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Kredit Azure OpenAI (Diperlukan untuk terjemahan teks)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # contohnya, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # contohnya, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # contohnya, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # contohnya, 2024-12-01-preview

# Set sandaran pilihan: duplikasi keseluruhan set AZURE_OPENAI_* dengan akhiran _1/_2 (indeks yang sama untuk semua pembolehubah)
```

---

### Bacaan Lanjut

- [Cara Mencipta projek dalam Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Cara Mencipta sumber Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Cara Menyebarkan model OpenAI dalam Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->