# Co-op Translator

_Mudah mengautomasikan dan mengekalkan terjemahan untuk kandungan pendidikan GitHub anda dalam pelbagai bahasa seperti projek anda berkembang._

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

### 🌐 Sokongan Pelbagai Bahasa

#### Disokong oleh [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](./README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Lebih Suka Klon Secara Lokal?**
>
> Repositori ini termasuk lebih daripada 50 terjemahan bahasa yang meningkatkan saiz muat turun secara signifikan. Untuk klon tanpa terjemahan, gunakan sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Ini memberikan anda segala yang diperlukan untuk menyelesaikan kursus dengan muat turun yang jauh lebih pantas.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Gambaran Keseluruhan

**Co-op Translator** membantu anda melokalakan kandungan pendidikan GitHub anda ke dalam pelbagai bahasa dengan mudah.  
Apabila anda mengemas kini fail Markdown, imej, atau buku nota, terjemahan akan diselaraskan secara automatik, memastikan kandungan anda kekal tepat dan terkini untuk pelajar di seluruh dunia.

Contoh bagaimana kandungan terjemahan diatur:

![Example](../../translated_images/ms/translation-ex.0c8aa6a7ee0aad2b.webp)

## Bagaimana keadaan terjemahan diuruskan

Co-op Translator mengurus kandungan terjemahan sebagai **artefak perisian berperingkat versi**,  
bukan sebagai fail statik.

Alat ini menjejaki keadaan terjemahan Markdown, imej, dan buku nota  
menggunakan **metadata skop bahasa**.

Reka bentuk ini membolehkan Co-op Translator untuk:

- Mengesan terjemahan yang sudah lapuk dengan boleh dipercayai  
- Mengendalikan Markdown, imej, dan buku nota dengan konsisten  
- Melakukan skala dengan selamat merentasi repositori pelbagai bahasa yang besar dan bergerak pantas

Dengan memodelkan terjemahan sebagai artefak yang diurus,  
aliran kerja terjemahan selaras secara semula jadi dengan  
amalan pengurusan pergantungan perisian dan artefak moden.

→ [Bagaimana keadaan terjemahan diuruskan](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Mula dengan cepat

```bash
# Cipta dan aktifkan persekitaran maya (disyorkan)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Pasang pakej
pip install co-op-translator
# Terjemah
translate -l "ko ja fr" -md
```

Docker:

```bash
# Tarik imej awam dari GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Jalankan dengan folder semasa dipasang dan .env disediakan (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Persediaan minimum

1. Pastikan anda mempunyai versi Python yang disokong (kini 3.10-3.12). Dalam poetry (pyproject.toml) ini diurus secara automatik.
2. Cipta fail `.env` menggunakan templat: [.env.template](../../.env.template)
3. Konfigurasikan satu pembekal LLM (Azure OpenAI atau OpenAI)
4. (Pilihan) Untuk terjemahan imej (`-img`), konfigurasikan Azure AI Vision
5. (Pilihan) Anda boleh konfigurasikan pelbagai set kelayakan dengan menggandakan pemboleh ubah dengan akhiran seperti `_1`, `_2`, dan lain-lain. Semua pemboleh ubah dalam satu set mesti berkongsi akhiran yang sama.
6. (Disyorkan) Bersihkan sebarang terjemahan sebelumnya untuk mengelakkan konflik (contohnya, `translations/`)
7. (Disyorkan) Tambah seksyen terjemahan ke README anda menggunakan [templat bahasa README](./getting_started/README_languages_template.md)
8. Lihat: [Sediakan Azure AI](./getting_started/set-up-azure-ai.md)

## Cara penggunaan

Terjemahkan semua jenis yang disokong:

```bash
translate -l "ko ja"
```

Hanya Markdown:

```bash
translate -l "de" -md
```

Markdown + imej:

```bash
translate -l "pt" -md -img
```

Hanya buku nota:

```bash
translate -l "zh" -nb
```

Lebih banyak bendera: [Rujukan arahan](./getting_started/command-reference.md)

## Ciri-ciri

- Terjemahan automatik untuk Markdown, buku nota, dan imej  
- Menjaga terjemahan selaras dengan perubahan sumber  
- Berfungsi secara tempatan (CLI) atau dalam CI (GitHub Actions)  
- Menggunakan Azure OpenAI atau OpenAI; pilihan Azure AI Vision untuk imej  
- Memelihara format dan struktur Markdown

## Dokumentasi

- [Panduan baris perintah](./getting_started/command-line-guide/command-line-guide.md)
- [Panduan GitHub Actions (repositori awam & rahsia standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Panduan GitHub Actions (repositori organisasi Microsoft & persediaan tahap organisasi)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Templat bahasa README](./getting_started/README_languages_template.md)
- [Bahasa yang disokong](./getting_started/supported-languages.md)
- [Menyumbang](./CONTRIBUTING.md)
- [Menyelesaikan masalah](./getting_started/troubleshooting.md)

### Panduan khusus Microsoft
> [!NOTE]
> Untuk penyelenggara repositori "Untuk Pemula" Microsoft sahaja.

- [Mengemas kini senarai “kursus lain” (untuk repositori Pemula MS sahaja)](./getting_started/update-other-courses.md)

## Sokong kami dan galakkan pembelajaran global

Sertai kami dalam merevolusikan cara kandungan pendidikan dikongsi secara global! Berikan [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ di GitHub dan sokong misi kami memecahkan halangan bahasa dalam pembelajaran dan teknologi. Minat dan sumbangan anda memberi impak yang besar! Sumbangan kod dan cadangan ciri sentiasa dialu-alukan.

### Terokai kandungan pendidikan Microsoft dalam bahasa anda

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

## Persembahan video

👉 Klik imej di bawah untuk menonton di YouTube.

- **Open at Microsoft**: Pengenalan ringkas 18 minit dan panduan pantas mengenai cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../translated_images/ms/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Berminat untuk menyumbang kepada Azure Co-op Translator? Sila lihat [CONTRIBUTING.md](./CONTRIBUTING.md) kami untuk garis panduan bagaimana anda boleh membantu menjadikan Co-op Translator lebih mudah diakses.

## Penyumbang
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kod Etika

Projek ini telah mengguna pakai [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/).
Untuk maklumat lanjut, lihat [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## AI Bertanggungjawab

Microsoft komited untuk membantu pelanggan kami menggunakan produk AI kami dengan bertanggungjawab, berkongsi pembelajaran kami, dan membina hubungan berasaskan kepercayaan melalui alat seperti Nota Ketelusan dan Penilaian Impak. Banyak sumber ini boleh didapati di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI bertanggungjawab berasaskan prinsip AI kami iaitu keadilan, kebolehpercayaan dan keselamatan, privasi dan keselamatan, keterangkuman, ketelusan, dan akauntabiliti.

Model bahasa semula jadi, imej, dan ucapan berskala besar - seperti yang digunakan dalam contoh ini - berpotensi berkelakuan dengan cara yang tidak adil, tidak boleh dipercayai, atau menyinggung, yang boleh membawa mudarat. Sila rujuk [Nota Ketelusan perkhidmatan Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk dimaklumkan tentang risiko dan hadnya.

Pendekatan yang disyorkan untuk mengurangkan risiko ini adalah dengan memasukkan sistem keselamatan dalam seni bina anda yang boleh mengesan dan menghalang tingkah laku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan berdikari, mampu mengesan kandungan berbahaya yang dihasilkan oleh pengguna dan AI dalam aplikasi dan perkhidmatan. Azure AI Content Safety termasuk API teks dan imej yang membolehkan anda mengesan bahan yang berbahaya. Kami juga mempunyai Studio Keselamatan Kandungan interaktif yang membolehkan anda melihat, meneroka dan mencuba kod sampel untuk mengesan kandungan berbahaya merentas modaliti yang berbeza. Dokumentasi [quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) membimbing anda membuat permintaan kepada perkhidmatan tersebut.

Satu aspek lain yang perlu diambil kira ialah prestasi keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami menganggap prestasi bermaksud sistem berfungsi seperti yang anda dan pengguna anda jangkakan, termasuk tidak menghasilkan keluaran yang berbahaya. Penting untuk menilai prestasi keseluruhan aplikasi anda menggunakan [kualiti generasi dan metrik risiko dan keselamatan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda boleh menilai aplikasi AI anda di persekitaran pembangunan menggunakan [SDK prompt flow](https://microsoft.github.io/promptflow/index.html). Dengan menggunakan dataset ujian atau sasaran, generasi aplikasi AI generatif anda diukur secara kuantitatif dengan penilai terbina dalam atau penilai tersuai pilihan anda. Untuk mula menggunakan prompt flow sdk bagi menilai sistem anda, anda boleh mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah anda menjalankan penilaian, anda boleh [melihat hasilnya dalam Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tanda Dagangan

Projek ini mungkin mengandungi tanda dagangan atau logo untuk projek, produk, atau perkhidmatan. Penggunaan yang dibenarkan untuk
tanda dagangan atau logo Microsoft tertakluk kepada dan mesti mengikuti
[Garispanduan Tanda Dagangan & Jenama Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Penggunaan tanda dagangan atau logo Microsoft dalam versi yang diubah suai projek ini tidak boleh menyebabkan kekeliruan atau mengisyaratkan tajaan oleh Microsoft.
Sebarang penggunaan tanda dagangan atau logo pihak ketiga adalah tertakluk kepada polisi pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika anda mengalami kesulitan atau mempunyai sebarang soalan mengenai pembangunan aplikasi AI, sertai:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika anda mempunyai maklum balas produk atau ralat semasa pembangunan, lawati:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->