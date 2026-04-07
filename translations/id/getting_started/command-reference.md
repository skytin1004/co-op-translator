# Command reference

The **Co-op Translator** CLI menawarkan beberapa opsi untuk menyesuaikan proses terjemahan:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Menerjemahkan proyek Anda ke bahasa yang ditentukan. Contoh: translate -l "es fr de" menerjemahkan ke bahasa Spanyol, Perancis, dan Jerman. Gunakan translate -l "all" untuk menerjemahkan ke semua bahasa yang didukung.
translate -l "language_codes" -u              | Memperbarui terjemahan dengan menghapus yang sudah ada dan membuat ulang. Peringatan: Ini akan menghapus semua terjemahan saat ini untuk bahasa yang ditentukan.
translate -l "language_codes" -img            | Menerjemahkan hanya file gambar.
translate -l "language_codes" -md             | Menerjemahkan hanya file Markdown.
translate -l "language_codes" -nb             | Menerjemahkan hanya file Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Menerjemahkan ulang file dengan skor kepercayaan rendah berdasarkan hasil evaluasi sebelumnya.
translate -l "language_codes" -d              | Mengaktifkan mode debug untuk pencatatan terperinci.
translate -l "language_codes" --save-logs, -s | Simpan log level DEBUG ke file di bawah <root_dir>/logs/ (konsol tetap dikontrol oleh -d)
translate -l "language_codes" -r "root_dir"   | Menentukan direktori root dari proyek
translate -l "language_codes" -f              | Menggunakan mode cepat untuk terjemahan gambar (hingga 3x lebih cepat saat plotting dengan sedikit pengorbanan kualitas dan keselarasan).
translate -l "language_codes" -y              | Otomatis konfirmasi semua prompt (berguna untuk pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktifkan atau nonaktifkan menambahkan bagian penyangkalan terjemahan mesin ke markdown dan notebook yang diterjemahkan (default: aktif).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalisasi saran bagian bahasa README (sparse checkout) dengan URL repositori Anda.
translate -l "language_codes" --help          | detail bantuan dalam CLI yang menampilkan perintah yang tersedia
evaluate -l "language_code"                  | Mengevaluasi kualitas terjemahan untuk bahasa tertentu dan memberikan skor kepercayaan
evaluate -l "language_code" -c 0.8           | Mengevaluasi terjemahan dengan ambang batas kepercayaan khusus
evaluate -l "language_code" -f               | Mode evaluasi cepat (hanya berbasis aturan, tanpa LLM)
evaluate -l "language_code" -D               | Mode evaluasi mendalam (hanya berbasis LLM, lebih menyeluruh tapi lebih lambat)
evaluate -l "language_code" --save-logs, -s  | Simpan log level DEBUG ke file di bawah <root_dir>/logs/
migrate-links -l "language_codes"             | Memproses ulang file Markdown yang diterjemahkan untuk memperbarui tautan ke notebook (.ipynb). Mengutamakan notebook yang diterjemahkan jika tersedia; jika tidak, bisa kembali ke notebook asli.
migrate-links -l "language_codes" -r          | Menentukan direktori root proyek (default: direktori saat ini).
migrate-links -l "language_codes" --dry-run   | Menampilkan file mana yang akan diubah tanpa menulis perubahan.
migrate-links -l "language_codes" --no-fallback-to-original | Tidak menulis ulang tautan ke notebook asli saat versi terjemahan tidak ada (hanya memperbarui saat terjemahan ada).
migrate-links -l "language_codes" -d          | Mengaktifkan mode debug untuk pencatatan terperinci.
migrate-links -l "language_codes" --save-logs, -s | Simpan log level DEBUG ke file di bawah <root_dir>/logs/
migrate-links -l "all" -y                      | Proses semua bahasa dan konfirmasi otomatis pada prompt peringatan.

## Usage examples

  1. Perilaku default (menambahkan terjemahan baru tanpa menghapus yang sudah ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Menambahkan hanya terjemahan gambar Korea baru (tanpa menghapus terjemahan yang ada):    translate -l "ko" -img

  3. Memperbarui semua terjemahan Korea (Peringatan: Ini menghapus semua terjemahan Korea yang ada sebelum menerjemahkan ulang):    translate -l "ko" -u

  4. Memperbarui hanya gambar Korea (Peringatan: Ini menghapus semua gambar Korea yang ada sebelum menerjemahkan ulang):    translate -l "ko" -img -u

  5. Menambahkan terjemahan markdown baru untuk Korea tanpa memengaruhi terjemahan lain:    translate -l "ko" -md

  6. Memperbaiki terjemahan dengan kepercayaan rendah berdasarkan hasil evaluasi sebelumnya: translate -l "ko" --fix

  7. Memperbaiki terjemahan dengan kepercayaan rendah hanya untuk file tertentu (markdown): translate -l "ko" --fix -md

  8. Memperbaiki terjemahan dengan kepercayaan rendah hanya untuk file tertentu (gambar): translate -l "ko" --fix -img

  9. Menggunakan mode cepat untuk terjemahan gambar:    translate -l "ko" -img -f

  10. Memperbaiki terjemahan dengan kepercayaan rendah dengan ambang khusus: translate -l "ko" --fix -c 0.8

  11. Contoh mode debug: - translate -l "ko" -d: Mengaktifkan pencatatan debug.
  12. Menyimpan log ke file: translate -l "ko" -s
  13. DEBUG konsol dan DEBUG file: translate -l "ko" -d -s
  14. Terjemahkan tanpa menambahkan penyangkalan terjemahan mesin ke output: translate -l "ko" --no-disclaimer

  15. Migrasi tautan notebook untuk terjemahan Korea (perbarui tautan ke notebook yang diterjemahkan jika tersedia):    migrate-links -l "ko"

  15. Migrasi tautan dengan dry-run (tanpa penulisan file):    migrate-links -l "ko" --dry-run

  16. Hanya memperbarui tautan saat notebook terjemahan ada (tidak kembali ke versi asli):    migrate-links -l "ko" --no-fallback-to-original

  17. Memproses semua bahasa dengan prompt konfirmasi:    migrate-links -l "all"

  18. Memproses semua bahasa dan konfirmasi otomatis:    migrate-links -l "all" -y
  19. Menyimpan log ke file untuk migrate-links:    migrate-links -l "ko ja" -s

  20. Personalisasi saran bahasa README dengan URL repo Anda:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Fitur Beta**: Fungsi evaluasi saat ini masih dalam tahap beta. Fitur ini dirilis untuk mengevaluasi dokumen terjemahan, dan metode evaluasi serta implementasi rinciannya masih dalam pengembangan dan dapat berubah.

  1. Mengevaluasi terjemahan Korea: evaluate -l "ko"

  2. Mengevaluasi dengan ambang kepercayaan khusus: evaluate -l "ko" -c 0.8

  3. Evaluasi cepat (hanya berbasis aturan): evaluate -l "ko" -f

  4. Evaluasi mendalam (hanya berbasis LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk ketepatan, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->