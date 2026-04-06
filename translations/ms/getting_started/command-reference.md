# Rujukan arahan

CLI **Co-op Translator** menawarkan beberapa pilihan untuk menyesuaikan proses terjemahan:

Command                                       | Penerangan
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Menterjemah projek anda ke dalam bahasa yang ditentukan. Contoh: translate -l "es fr de" menterjemah ke Sepanyol, Perancis, dan Jerman. Gunakan translate -l "all" untuk menterjemah ke semua bahasa yang disokong.
translate -l "language_codes" -u              | Mengemas kini terjemahan dengan memadam yang sedia ada dan membuatnya semula. Amaran: Ini akan memadam semua terjemahan semasa untuk bahasa yang ditentukan.
translate -l "language_codes" -img            | Menterjemah hanya fail imej.
translate -l "language_codes" -md             | Menterjemah hanya fail Markdown.
translate -l "language_codes" -nb             | Menterjemah hanya fail Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Menterjemah semula fail dengan skor keyakinan rendah berdasarkan keputusan penilaian terdahulu.
translate -l "language_codes" -d              | Mengaktifkan mod debug untuk log terperinci.
translate -l "language_codes" --save-logs, -s | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/ (konsol dikawal oleh -d)
translate -l "language_codes" -r "root_dir"   | Menentukan direktori akar projek
translate -l "language_codes" -f              | Menggunakan mod pantas untuk terjemahan imej (hingga 3x lebih pantas tetapi dengan sedikit kos pada kualiti dan penjajaran).
translate -l "language_codes" -y              | Mengesahkan semua arahan secara automatik (berguna untuk saluran CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Mengaktifkan atau menyahaktifkan penambahan seksyen penafian terjemahan mesin kepada markdown dan notebook yang diterjemah (lalai: diaktifkan).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Peribadikan penasihat seksyen bahasa README (sparse checkout) dengan URL repositori anda.
translate -l "language_codes" --help          | butiran bantuan dalam CLI yang menunjukkan arahan tersedia
evaluate -l "language_code"                  | Menilai kualiti terjemahan untuk bahasa tertentu dan menyediakan skor keyakinan
evaluate -l "language_code" -c 0.8           | Menilai terjemahan dengan ambang keyakinan tersuai
evaluate -l "language_code" -f               | Mod penilaian pantas (berdasarkan peraturan sahaja, tanpa LLM)
evaluate -l "language_code" -D               | Mod penilaian mendalam (berdasarkan LLM sahaja, lebih menyeluruh tetapi lebih perlahan)
evaluate -l "language_code" --save-logs, -s  | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/
migrate-links -l "language_codes"             | Memproses semula fail Markdown yang diterjemah untuk mengemas kini pautan ke notebook (.ipynb). Mengutamakan notebook diterjemah jika tersedia; jika tidak boleh menggunakan notebook asal.
migrate-links -l "language_codes" -r          | Menentukan direktori akar projek (lalai: direktori semasa).
migrate-links -l "language_codes" --dry-run   | Tunjukkan fail yang akan berubah tanpa menulis perubahan.
migrate-links -l "language_codes" --no-fallback-to-original | Jangan tulis semula pautan ke notebook asal apabila terjemahan tiada (kemas kini hanya apabila terjemahan wujud).
migrate-links -l "language_codes" -d          | Mengaktifkan mod debug untuk log terperinci.
migrate-links -l "language_codes" --save-logs, -s | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/
migrate-links -l "all" -y                      | Memproses semua bahasa dan mengesahkan arahan amaran secara automatik.

## Contoh penggunaan

  1. Tingkah laku lalai (tambah terjemahan baru tanpa memadam terjemahan sedia ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Tambah hanya terjemahan imej Korea baru (tiada terjemahan sedia ada dipadam):    translate -l "ko" -img

  3. Kemas kini semua terjemahan Korea (Amaran: Ini memadam semua terjemahan Korea sedia ada sebelum menterjemah semula):    translate -l "ko" -u

  4. Kemas kini hanya imej Korea (Amaran: Ini memadam semua imej Korea sedia ada sebelum menterjemah semula):    translate -l "ko" -img -u

  5. Tambah terjemahan markdown baru untuk Korea tanpa menjejaskan terjemahan lain:    translate -l "ko" -md

  6. Betulkan terjemahan dengan keyakinan rendah berdasarkan keputusan penilaian terdahulu: translate -l "ko" --fix

  7. Betulkan terjemahan dengan keyakinan rendah untuk fail tertentu sahaja (markdown): translate -l "ko" --fix -md

  8. Betulkan terjemahan dengan keyakinan rendah untuk fail tertentu sahaja (imej): translate -l "ko" --fix -img

  9. Gunakan mod pantas untuk terjemahan imej:    translate -l "ko" -img -f

  10. Betulkan terjemahan dengan keyakinan rendah dengan ambang tersuai: translate -l "ko" --fix -c 0.8

  11. Contoh mod debug: - translate -l "ko" -d: Aktifkan log debug.
  12. Simpan log ke fail: translate -l "ko" -s
  13. DEBUG konsol dan DEBUG fail: translate -l "ko" -d -s
  14. Terjemah tanpa menambah penafian terjemahan mesin ke output: translate -l "ko" --no-disclaimer

  15. Migrasi pautan notebook untuk terjemahan Korea (kemas kini pautan ke notebook diterjemah apabila tersedia):    migrate-links -l "ko"

  15. Migrasi pautan dengan dry-run (tiada penulisan fail):    migrate-links -l "ko" --dry-run

  16. Hanya kemas kini pautan apabila notebook diterjemah wujud (jangan guna kembali kepada asal):    migrate-links -l "ko" --no-fallback-to-original

  17. Proses semua bahasa dengan arahan pengesahan:    migrate-links -l "all"

  18. Proses semua bahasa dan auto-sahkan:    migrate-links -l "all" -y
  19. Simpan log ke fail untuk migrate-links:    migrate-links -l "ko ja" -s

  20. Peribadikan penasihat bahasa README dengan URL repo anda:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Contoh Penilaian

> [!WARNING]  
> **Ciri Beta**: Fungsi penilaian kini dalam versi beta. Ciri ini dikeluarkan untuk menilai dokumen yang diterjemah, dan kaedah penilaian serta pelaksanaan terperinci masih dalam pembangunan dan tertakluk kepada perubahan.

  1. Nilai terjemahan Korea: evaluate -l "ko"

  2. Nilai dengan ambang keyakinan tersuai: evaluate -l "ko" -c 0.8

  3. Penilaian pantas (berdasarkan peraturan sahaja): evaluate -l "ko" -f

  4. Penilaian mendalam (berdasarkan LLM sahaja): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->