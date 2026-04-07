# Co-op Translator

_Mudah mengotomatiskan dan memelihara terjemahan untuk konten edukasi GitHub Anda dalam berbagai bahasa seiring perkembangan proyek Anda._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Dukungan Multi-Bahasa

#### Didukung oleh [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](./README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Lebih suka Clone secara Lokal?**
>
> Repository ini menyertakan lebih dari 50 terjemahan bahasa yang secara signifikan meningkatkan ukuran unduhan. Untuk clone tanpa terjemahan, gunakan sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Ini memberikan Anda semua yang Anda butuhkan untuk menyelesaikan kursus dengan unduhan yang jauh lebih cepat.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ikhtisar

**Co-op Translator** membantu Anda melakukan lokalisasi konten edukasi GitHub Anda ke dalam berbagai bahasa dengan mudah.  
Saat Anda memperbarui file Markdown, gambar, atau notebook Anda, terjemahan tetap otomatis tersinkronisasi, memastikan konten Anda tetap akurat dan terbaru untuk pelajar di seluruh dunia.

Contoh bagaimana konten terjemahan diorganisasi:

![Contoh](../../imgs/translation-ex.png)

## Cara mengelola status terjemahan

Co-op Translator mengelola konten terjemahan sebagai **arsip perangkat lunak berversi**,  
bukan sebagai file statis.

Alat ini melacak status Markdown, gambar, dan notebook yang diterjemahkan  
menggunakan **metadata ruang bahasa**.

Desain ini memungkinkan Co-op Translator untuk:

- Mendeteksi terjemahan yang sudah usang dengan dapat diandalkan  
- Menangani Markdown, gambar, dan notebook secara konsisten  
- Skalabilitas yang aman di repositori multi-bahasa yang besar dan bergerak cepat  

Dengan memodelkan terjemahan sebagai arsip yang dikelola,  
alur kerja terjemahan secara alami selaras dengan praktik pengelolaan  
ketergantungan dan arsip perangkat lunak modern.

→ [Cara mengelola status terjemahan](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Memulai cepat

```bash
# Buat dan aktifkan lingkungan virtual (disarankan)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instal paket tersebut
pip install co-op-translator
# Terjemahkan
translate -l "ko ja fr" -md
```

Docker:

```bash
# Tarik gambar publik dari GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Jalankan dengan folder saat ini dipasang dan .env disediakan (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Pengaturan minimum

1. Pastikan Anda memiliki versi Python yang didukung (saat ini 3.10-3.12). Dalam poetry (pyproject.toml) ini ditangani secara otomatis.  
2. Buat file `.env` menggunakan template: [.env.template](../../.env.template)  
3. Konfigurasi satu penyedia LLM (Azure OpenAI atau OpenAI)  
4. (Opsional) Untuk terjemahan gambar (`-img`), konfigurasikan Azure AI Vision  
5. (Opsional) Anda dapat mengonfigurasi beberapa set kredensial dengan menggandakan variabel dengan akhiran seperti `_1`, `_2`, dll. Semua variabel dalam satu set harus berbagi akhiran yang sama.  
6. (Disarankan) Bersihkan terjemahan lama untuk menghindari konflik (misal: `translations/`)  
7. (Disarankan) Tambahkan bagian terjemahan ke README Anda menggunakan [template bahasa README](./getting_started/README_languages_template.md)  
8. Lihat: [Mengatur Azure AI](./getting_started/set-up-azure-ai.md)

## Penggunaan

Terjemahkan semua tipe yang didukung:

```bash
translate -l "ko ja"
```

Hanya Markdown:

```bash
translate -l "de" -md
```

Markdown + gambar:

```bash
translate -l "pt" -md -img
```

Hanya notebook:

```bash
translate -l "zh" -nb
```

Lebih banyak opsi: [Referensi perintah](./getting_started/command-reference.md)

## Fitur

- Terjemahan otomatis untuk Markdown, notebook, dan gambar  
- Menjaga terjemahan agar tetap sinkron dengan perubahan sumber  
- Berfungsi secara lokal (CLI) atau di CI (GitHub Actions)  
- Menggunakan Azure OpenAI atau OpenAI; opsional Azure AI Vision untuk gambar  
- Mempertahankan format dan struktur Markdown

## Dokumentasi

- [Panduan baris perintah](./getting_started/command-line-guide/command-line-guide.md)  
- [Panduan GitHub Actions (Repositori publik & rahasia standar)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Panduan GitHub Actions (Repositori organisasi Microsoft & pengaturan tingkat organisasi)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Template bahasa README](./getting_started/README_languages_template.md)  
- [Bahasa yang didukung](./getting_started/supported-languages.md)  
- [Berkontribusi](./CONTRIBUTING.md)  
- [Pemecahan masalah](./getting_started/troubleshooting.md)

### Panduan khusus Microsoft
> [!NOTE]
> Untuk pemelihara repositori “For Beginners” Microsoft saja.

- [Memperbarui daftar "kursus lain" (hanya untuk repositori MS Beginners)](./getting_started/update-other-courses.md)

## Dukung kami dan dorong pembelajaran global

Bergabunglah dalam merevolusi cara konten edukasi dibagikan secara global! Berikan ⭐ pada [Co-op Translator](https://github.com/azure/co-op-translator) di GitHub dan dukung misi kami untuk menghilangkan hambatan bahasa dalam pembelajaran dan teknologi. Ketertarikan dan kontribusi Anda memberikan dampak besar! Kontribusi kode dan saran fitur selalu disambut.

### Jelajahi konten edukasi Microsoft dalam bahasa Anda

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)  
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)  
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)  
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)  
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)  
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)  
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)  
- [ML for Beginners](https://aka.ms/ml-beginners)  
- [Data Science for Beginners](https://aka.ms/datascience-beginners)  
- [AI for Beginners](https://aka.ms/ai-beginners)  
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)  
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)  
- [IoT for Beginners](https://aka.ms/iot-beginners)  
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Presentasi video

👉 Klik gambar di bawah ini untuk menonton di YouTube.

- **Open at Microsoft**: Perkenalan singkat 18 menit dan panduan cepat cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Berkontribusi

Proyek ini menyambut kontribusi dan saran. Berminat berkontribusi ke Azure Co-op Translator? Silakan lihat [CONTRIBUTING.md](./CONTRIBUTING.md) untuk panduan tentang bagaimana Anda dapat membantu membuat Co-op Translator lebih mudah diakses.

## Kontributor
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kode Etik

Proyek ini telah mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk informasi lebih lanjut lihat [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## AI Bertanggung Jawab

Microsoft berkomitmen membantu pelanggan kami menggunakan produk AI kami secara bertanggung jawab, berbagi pembelajaran kami, dan membangun kemitraan berbasis kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber daya ini dapat ditemukan di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI bertanggung jawab didasarkan pada prinsip AI kami yaitu keadilan, keandalan dan keamanan, privasi dan keamanan, inklusivitas, transparansi, dan akuntabilitas.

Model bahasa alami, gambar, dan suara berskala besar - seperti yang digunakan dalam contoh ini - berpotensi berperilaku dengan cara yang tidak adil, tidak dapat diandalkan, atau menyinggung, yang dapat menyebabkan kerugian. Silakan lihat [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk mendapatkan informasi tentang risiko dan keterbatasan.

Pendekatan yang direkomendasikan untuk mengurangi risiko ini adalah dengan memasukkan sistem keamanan dalam arsitektur Anda yang dapat mendeteksi dan mencegah perilaku merugikan. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan independen, mampu mendeteksi konten berbahaya yang dibuat pengguna dan AI dalam aplikasi dan layanan. Azure AI Content Safety mencakup API teks dan gambar yang memungkinkan Anda mendeteksi materi yang berbahaya. Kami juga memiliki Content Safety Studio interaktif yang memungkinkan Anda melihat, menjelajah, dan mencoba contoh kode untuk mendeteksi konten berbahaya di berbagai modalitas. Dokumentasi [quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) memandu Anda dalam membuat permintaan ke layanan ini.

Aspek lain yang perlu dipertimbangkan adalah kinerja keseluruhan aplikasi. Dengan aplikasi multimodal dan multimodel, kami menganggap kinerja berarti sistem berfungsi seperti yang Anda dan pengguna harapkan, termasuk tidak menghasilkan output berbahaya. Penting untuk menilai kinerja aplikasi Anda secara keseluruhan menggunakan [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda dapat mengevaluasi aplikasi AI Anda di lingkungan pengembangan Anda menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan dataset uji atau target, generasi AI generatif Anda diukur secara kuantitatif menggunakan evaluator bawaan atau evaluator kustom pilihan Anda. Untuk memulai dengan prompt flow sdk guna mengevaluasi sistem Anda, Anda dapat mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah menjalankan evaluasi, Anda dapat [melihat hasilnya di Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Merek Dagang

Proyek ini mungkin berisi merek dagang atau logo untuk proyek, produk, atau layanan. Penggunaan merek dagang atau logo Microsoft yang sah tunduk pada dan harus mengikuti
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Penggunaan merek dagang atau logo Microsoft dalam versi yang dimodifikasi dari proyek ini tidak boleh menimbulkan kebingungan atau menyiratkan dukungan Microsoft.
Penggunaan merek dagang atau logo pihak ketiga tunduk pada kebijakan pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika Anda mengalami kebingungan atau memiliki pertanyaan tentang membuat aplikasi AI, bergabunglah dengan:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika Anda memiliki umpan balik produk atau mengalami kesalahan saat membangun, kunjungi:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi yang penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->