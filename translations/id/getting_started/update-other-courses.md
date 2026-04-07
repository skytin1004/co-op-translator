# Perbarui bagian "Other Courses" (repos Microsoft Beginners)

Panduan ini menjelaskan cara membuat bagian "Other Courses" tersinkronisasi otomatis menggunakan Co-op Translator, dan cara memperbarui template global untuk semua repos.

- Berlaku untuk: Hanya repositori Microsoft Beginners
- Bekerja dengan: Co-op Translator CLI dan GitHub Actions
- Sumber template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mulai cepat: Aktifkan auto-sync di repo Anda

Tambahkan penanda berikut di sekitar bagian "Other Courses" di README Anda. Co-op Translator akan mengganti semua yang ada di antara penanda ini pada setiap kali dijalankan.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan—melalui CLI (misalnya, `translate -l "<language codes>"`) atau GitHub Actions—ini secara otomatis memperbarui bagian "Other Courses" yang dibungkus oleh penanda ini.

> [!NOTE]
> Jika Anda memiliki daftar yang sudah ada, cukup bungkus dengan penanda yang sama. Jalankan berikutnya akan menggantinya dengan konten standar terbaru.

---

## Cara mengubah konten global

Jika Anda ingin memperbarui konten standar yang muncul di semua repo Beginners:

1. Edit templatenya: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Buka pull request ke repo Co-op Translator dengan perubahan Anda
3. Setelah PR digabungkan, versi Co-op Translator akan diperbarui
4. Berikutnya saat Co-op Translator dijalankan (CLI atau GitHub Action) di repo target, itu akan otomatis menyinkronkan bagian yang diperbarui

Ini menjamin sumber kebenaran tunggal untuk konten "Other Courses" di seluruh repositori Beginners.


## Ukuran Repo

Repo dapat menjadi besar akibat banyaknya bahasa yang diterjemahkan untuk membantu pengguna akhir dengan panduan cara menggunakan clone - sparse agar hanya meng-clone bahasa yang diperlukan, bukan seluruh repo

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
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->