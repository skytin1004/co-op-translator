# Kemas kini seksyen "Kursus Lain" (repos Microsoft Beginners)

Panduan ini menerangkan cara untuk memastikan seksyen "Kursus Lain" diselaraskan secara automatik menggunakan Co-op Translator, serta cara mengemas kini templat global untuk semua repos.

- Terpakai kepada: repositori Microsoft Beginners sahaja
- Berfungsi dengan: Co-op Translator CLI dan GitHub Actions
- Sumber templat: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mula dengan cepat: Dayakan auto-sync dalam repo anda

Tambahkan penanda berikut di sekitar seksyen "Kursus Lain" dalam README anda. Co-op Translator akan menggantikan segala yang berada di antara penanda ini pada setiap kali dijalankan.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan—melalui CLI (contoh, `translate -l "<language codes>"`) atau GitHub Actions—ia secara automatik mengemas kini seksyen "Kursus Lain" yang dibungkus oleh penanda ini.

> [!NOTE]
> Jika anda sudah mempunyai senarai, cuma bungkuskan ia dengan penanda yang sama. Larian seterusnya akan menggantikannya dengan kandungan standard terkini.

---

## Cara mengubah kandungan global

Jika anda ingin mengemas kini kandungan standard yang muncul dalam semua repositori Beginners:

1. Sunting templat: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Buka pull request ke repositori Co-op Translator dengan perubahan anda
3. Selepas PR digabungkan, versi Co-op Translator akan dikemas kini
4. Kali berikutnya Co-op Translator dijalankan (CLI atau GitHub Action) dalam repos sasaran, ia akan menyelaraskan bahagian yang dikemas kini secara automatik

Ini memastikan satu sumber kebenaran untuk kandungan "Kursus Lain" merentasi semua repositori Beginners.

## Saiz Repo

Repos boleh menjadi besar kerana bilangan bahasa yang diterjemahkan untuk membantu pengguna akhir memberi panduan tentang cara menggunakan clone - sparse untuk hanya mengklon bahasa yang diperlukan dan bukan keseluruhan repo

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
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->