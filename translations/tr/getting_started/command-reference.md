# Komut referansı

**Co-op Translator** CLI, çeviri sürecini kişiselleştirmek için çeşitli seçenekler sunar:

Komut                                         | Açıklama
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Projenizi belirtilen dillere çevirir. Örnek: translate -l "es fr de" İspanyolca, Fransızca ve Almanca dillerine çevirir. Tüm desteklenen dillere çevirmek için translate -l "all" kullanın.
translate -l "language_codes" -u              | Mevcut olanları silip yeniden oluşturarak çevirileri günceller. Uyarı: Bu, belirtilen diller için tüm mevcut çevirileri silecektir.
translate -l "language_codes" -img            | Yalnızca resim dosyalarını çevirir.
translate -l "language_codes" -md             | Yalnızca Markdown dosyalarını çevirir.
translate -l "language_codes" -nb             | Yalnızca Jupyter notebook dosyalarını (.ipynb) çevirir.
translate -l "language_codes" --fix           | Önceki değerlendirme sonuçlarına dayanarak düşük güven skoruna sahip dosyaları yeniden çevirir.
translate -l "language_codes" -d              | Ayrıntılı günlük kaydı için hata ayıklama modunu etkinleştirir.
translate -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder (konsol -d ile kontrol edilir)
translate -l "language_codes" -r "root_dir"   | Projenin kök dizinini belirtir
translate -l "language_codes" -f              | Resim çevirisi için hızlı modu kullanır (kalite ve hizalamada hafif bir maliyet karşılığında 3 kata kadar daha hızlı grafik çizimi).
translate -l "language_codes" -y              | Tüm istemleri otomatik onaylar (CI/CD hatları için kullanışlı)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Çevrilmiş markdown ve not defterlerine makine çeviri sorumluluğu bölümünün eklenmesini etkinleştirir veya devre dışı bırakır (varsayılan: etkin).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | README dilleri bölümü tavsiyesini depounuzun URL'si ile kişiselleştirir (use sparse checkout).
translate -l "language_codes" --help          | CLI içinde mevcut komutların yardım detayları
evaluate -l "language_code"                  | Belirli bir dil için çeviri kalitesini değerlendirir ve güven skorları sağlar
evaluate -l "language_code" -c 0.8           | Özel güven eşiği ile çevirileri değerlendirir
evaluate -l "language_code" -f               | Hızlı değerlendirme modu (yalnızca kural tabanlı, LLM yok)
evaluate -l "language_code" -D               | Derin değerlendirme modu (yalnızca LLM tabanlı, daha kapsamlı ama daha yavaş)
evaluate -l "language_code" --save-logs, -s  | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder
migrate-links -l "language_codes"             | Çevrilmiş Markdown dosyalarını yeniden işler ve notebooklar (.ipynb) için bağlantıları günceller. Çevrilmiş notebooklar varsa onları tercih eder; yoksa orijinal notebooklara geçiş yapabilir.
migrate-links -l "language_codes" -r          | Proje kök dizinini belirtir (varsayılan: mevcut dizin).
migrate-links -l "language_codes" --dry-run   | Değişecek dosyaları dosya yazmadan gösterir.
migrate-links -l "language_codes" --no-fallback-to-original | Çevrilmiş karşılıklar yoksa orijinal notebooklara bağlantıları yeniden yazmaz (sadece çevrilmiş varsa güncellenir).
migrate-links -l "language_codes" -d          | Ayrıntılı günlük kaydı için hata ayıklama modunu etkinleştirir.
migrate-links -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder
migrate-links -l "all" -y                      | Tüm dilleri işler ve uyarı istemini otomatik onaylar.

## Kullanım örnekleri

  1. Varsayılan davranış (mevcut çevirileri silmeden yeni çeviriler ekler):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Sadece yeni Korece resim çevirileri ekle (mevcut çeviriler silinmez):    translate -l "ko" -img

  3. Tüm Korece çevirileri güncelle (Uyarı: Bu, yeniden çeviri yapmadan önce tüm mevcut Korece çevirileri siler):    translate -l "ko" -u

  4. Sadece Korece resimleri güncelle (Uyarı: Bu, yeniden çeviri yapmadan önce tüm mevcut Korece resimleri siler):    translate -l "ko" -img -u

  5. Diğer çevirileri etkilemeden Korece için yeni markdown çevirileri ekle:    translate -l "ko" -md

  6. Önceki değerlendirme sonuçlarına dayanarak düşük güvenlikli çevirileri düzelt: translate -l "ko" --fix

  7. Belirli dosyalar için yalnızca düşük güvenlikli çevirileri düzelt (markdown): translate -l "ko" --fix -md

  8. Belirli dosyalar için yalnızca düşük güvenlikli çevirileri düzelt (resimler): translate -l "ko" --fix -img

  9. Resim çevirisi için hızlı modu kullan:    translate -l "ko" -img -f

  10. Özel eşik ile düşük güvenlikli çevirileri düzelt: translate -l "ko" --fix -c 0.8

  11. Hata ayıklama modu örneği: - translate -l "ko" -d: Hata ayıklama günlük kaydını etkinleştir.
  12. Günlükleri dosyalara kaydet: translate -l "ko" -s
  13. Konsol DEBUG ve dosya DEBUG: translate -l "ko" -d -s
  14. Çıktılara makine çeviri sorumluluğu eklemeden çeviri yap: translate -l "ko" --no-disclaimer

  15. Korece çeviriler için notebook bağlantılarını taşı (çevirilmiş notebooklar varsa bağlantıları güncelle):    migrate-links -l "ko"

  15. Kuru çalıştırma ile bağlantıları taşı (dosya yazmaz):    migrate-links -l "ko" --dry-run

  16. Yalnızca çevrilmiş notebooklar varsa bağlantıları güncelle (orijinal dosyalara dönme):    migrate-links -l "ko" --no-fallback-to-original

  17. Onay istemi ile tüm dilleri işle:    migrate-links -l "all"

  18. Tüm dilleri işle ve otomatik onayla:    migrate-links -l "all" -y
  19. migrate-links için günlükleri dosyalara kaydet:    migrate-links -l "ko ja" -s

  20. README dilleri tavsiyesini deponuzun URL'siyle kişiselleştir:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Değerlendirme Örnekleri

> [!WARNING]  
> **Beta Özelliği**: Değerlendirme işlevselliği şu anda beta aşamasındadır. Bu özellik, çevrilmiş belgeleri değerlendirmek için yayınlanmıştır ve değerlendirme yöntemleri ile detaylı uygulamalar hâlen geliştirme aşamasındadır ve değişikliklere tabidir.

  1. Korece çevirileri değerlendir: evaluate -l "ko"

  2. Özel güven eşiği ile değerlendir: evaluate -l "ko" -c 0.8

  3. Hızlı değerlendirme (yalnızca kural tabanlı): evaluate -l "ko" -f

  4. Derin değerlendirme (yalnızca LLM tabanlı): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->