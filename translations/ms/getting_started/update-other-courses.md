# Kemas kini bahagian "Kursus Lain" (repositori Microsoft Beginners)

Panduan ini menerangkan cara menjadikan bahagian "Kursus Lain" disegerakkan secara automatik menggunakan Co-op Translator, dan cara mengemas kini templat global untuk semua repositori.

- Terpakai kepada: repositori Microsoft Beginners sahaja
- Berfungsi dengan: Co-op Translator CLI dan GitHub Actions
- Sumber templat: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mula pantas: Aktifkan auto-segerak dalam repo anda

Tambah penanda berikut di sekitar bahagian "Kursus Lain" dalam README anda. Co-op Translator akan menggantikan segala-galanya antara penanda ini setiap kali dijalankan.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan—melalui CLI (contoh, `translate -l "<language codes>"`) atau GitHub Actions—ia secara automatik mengemas kini bahagian "Kursus Lain" yang dibalut oleh penanda ini.

> [!NOTE]
> Jika anda sudah mempunyai senarai sedia ada, hanya balutkan dengan penanda yang sama. Kali jalan seterusnya akan menggantikannya dengan kandungan yang distandardkan terkini.

---

## Cara menukar kandungan global

Jika anda ingin mengemas kini kandungan standard yang muncul dalam semua repositori Beginners:

1. Edit templat: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Buka pull request ke repo Co-op Translator dengan perubahan anda
3. Selepas PR digabungkan, versi Co-op Translator akan dikemas kini
4. Kali seterusnya Co-op Translator dijalankan (CLI atau GitHub Action) dalam repo sasaran, ia akan secara automatik menyegerakkan bahagian yang dikemas kini

Ini memastikan satu sumber kebenaran untuk kandungan "Kursus Lain" di semua repositori Beginners.


## Saiz Repo

Repositori boleh menjadi besar disebabkan oleh bilangan bahasa yang diterjemahkan untuk membantu pengguna akhir memberikan panduan tentang cara menggunakan clone - sparse untuk hanya menyalin bahasa yang diperlukan dan bukan keseluruhan repo

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
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk mencapai ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->