# Memperbarui bagian "Kursus Lainnya" (Repositori Microsoft Beginners)

Panduan ini menjelaskan cara membuat bagian "Kursus Lainnya" sinkron otomatis menggunakan Co‑op Translator, dan cara memperbarui template global untuk semua repositori.

- Berlaku untuk: hanya repositori Microsoft Beginners
- Bekerja dengan: Co‑op Translator CLI dan GitHub Actions
- Sumber template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Memulai cepat: Aktifkan sinkron otomatis di repositori Anda

Tambahkan penanda berikut di sekitar bagian "Kursus Lainnya" dalam README Anda. Co‑op Translator akan mengganti semua isi di antara penanda ini setiap kali dijalankan.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co‑op Translator dijalankan—melalui CLI (misalnya, `translate -l "<language codes>"`) atau GitHub Actions—ia secara otomatis memperbarui bagian "Kursus Lainnya" yang dibungkus oleh penanda ini.

> [!NOTE]
> Jika Anda sudah memiliki daftar yang ada, cukup bungkus dengan penanda yang sama. Jalankan berikutnya akan menggantinya dengan konten standar terbaru.

---

## Cara mengubah konten global

Jika Anda ingin memperbarui konten standar yang muncul di semua repositori Beginners:

1. Edit templatenya: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Buka pull request ke repositori Co-op Translator dengan perubahan Anda
3. Setelah PR digabungkan, versi Co‑op Translator akan diperbarui
4. Berikutnya Co‑op Translator dijalankan (CLI atau GitHub Action) di repositori target, secara otomatis akan menyinkronkan bagian yang diperbarui

Ini memastikan sumber kebenaran tunggal untuk konten "Kursus Lainnya" di semua repositori Beginners.


## Ukuran Repo

Repositori bisa menjadi besar karena jumlah bahasa yang diterjemahkan untuk membantu pengguna akhir memberikan panduan cara menggunakan clone - sparse agar hanya meng-kloning bahasa yang diperlukan dan tidak seluruh repo

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->