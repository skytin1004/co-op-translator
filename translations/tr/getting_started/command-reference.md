# Komut referansı

**Co-op Translator** CLI, çeviri sürecini özelleştirmek için çeşitli seçenekler sunar:

Komut                                        | Açıklama
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Projenizi belirtilen dillere çevirir. Örnek: translate -l "es fr de" İspanyolca, Fransızca ve Almancaya çeviri yapar. Tüm desteklenen dillere çevirmek için translate -l "all" kullanın.
translate -l "language_codes" -u              | Var olan çevirileri silip yeniden oluşturarak çevirileri günceller. Uyarı: Bu, belirtilen diller için mevcut tüm çevirileri silecektir.
translate -l "language_codes" -img            | Sadece resim dosyalarını çevirir.
translate -l "language_codes" -md             | Sadece Markdown dosyalarını çevirir.
translate -l "language_codes" -nb             | Sadece Jupyter notebook dosyalarını (.ipynb) çevirir.
translate -l "language_codes" --fix           | Önceki değerlendirme sonuçlarına göre düşük güven skorları olan dosyaları yeniden çevirir.
translate -l "language_codes" -d              | Ayrıntılı günlük kaydı için hata ayıklama modunu etkinleştirir.
translate -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altındaki dosyalara kaydeder (konsol -d ile kontrol edilir)
translate -l "language_codes" -r "root_dir"   | Projenin kök dizinini belirtir
translate -l "language_codes" -f              | Resim çevirisi için hızlı modu kullanır (biraz kalite ve hizalamada fedakarlık ile 3 kata kadar daha hızlı çizim).
translate -l "language_codes" -y              | Tüm komut istemlerini otomatik olarak onaylar (CI/CD boru hatları için faydalı)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Çevrilmiş markdown ve notebooklara makine çevirisi sorumluluk reddi bölümü eklemeyi etkinleştirir veya devre dışı bırakır (varsayılan: etkin).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | README diller bölümü tavsiyesini (seyrek çekim) depolar URL'nizle kişiselleştirir.
translate -l "language_codes" --help          | CLI içindeki kullanılabilir komutları gösteren yardım detayları
evaluate -l "language_code"                  | Belirli bir dil için çeviri kalitesini değerlendirir ve güven skorları sağlar
evaluate -l "language_code" -c 0.8           | Özel güven eşiği ile çevirileri değerlendirir
evaluate -l "language_code" -f               | Hızlı değerlendirme modu (yalnızca kural tabanlı, LLM yok)
evaluate -l "language_code" -D               | Derin değerlendirme modu (yalnızca LLM tabanlı, daha kapsamlı ama daha yavaş)
evaluate -l "language_code" --save-logs, -s  | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altındaki dosyalara kaydeder
migrate-links -l "language_codes"             | Çevrilmiş Markdown dosyalarını yeniden işleyerek notebooklara (.ipynb) olan bağlantıları günceller. Çevrilmiş notebooklar varsa onlar tercih edilir; yoksa orijinal notebooklara dönebilir.
migrate-links -l "language_codes" -r          | Proje kök dizinini belirtir (varsayılan: mevcut dizin).
migrate-links -l "language_codes" --dry-run   | Dosya değişikliklerini yazmadan hangi dosyaların değişeceğini gösterir.
migrate-links -l "language_codes" --no-fallback-to-original | Çevrilmiş karşılıkları eksik olduğunda orijinal notebook bağlantılarını yeniden yazmaz (yalnızca çevirilmiş varsa günceller).
migrate-links -l "language_codes" -d          | Ayrıntılı günlük kaydı için hata ayıklama modunu etkinleştirir.
migrate-links -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altındaki dosyalara kaydeder
migrate-links -l "all" -y                      | Tüm dilleri işler ve uyarı komut istemini otomatik onaylar.

## Kullanım örnekleri

  1. Varsayılan davranış (var olanları silmeden yeni çeviriler ekler):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Sadece yeni Korece resim çevirileri ekle (var olan çeviriler silinmez):    translate -l "ko" -img

  3. Tüm Korece çevirileri güncelle (Uyarı: Bu, yeniden çevirmeden önce tüm mevcut Korece çevirileri siler):    translate -l "ko" -u

  4. Sadece Korece resimleri güncelle (Uyarı: Bu, yeniden çevirmeden önce mevcut tüm Korece resimleri siler):    translate -l "ko" -img -u

  5. Diğer çevirilere dokunmadan Korece için yeni markdown çevirileri ekle:    translate -l "ko" -md

  6. Önceki değerlendirme sonuçlarına dayalı düşük güven çevirilerini düzelt: translate -l "ko" --fix

  7. Sadece belirli dosyalar için düşük güven çevirilerini düzelt (markdown): translate -l "ko" --fix -md

  8. Sadece belirli dosyalar için düşük güven çevirilerini düzelt (resimler): translate -l "ko" --fix -img

  9. Resim çevirisi için hızlı mod kullan:    translate -l "ko" -img -f

  10. Özel eşik ile düşük güven çevirilerini düzelt: translate -l "ko" --fix -c 0.8

  11. Hata ayıklama modu örneği: - translate -l "ko" -d: Hata ayıklama günlüklerini etkinleştir.
  12. Günlükleri dosyalara kaydet: translate -l "ko" -s
  13. Konsol DEBUG ve dosya DEBUG: translate -l "ko" -d -s
  14. Çıktılara makine çevirisi sorumluluk reddi eklemeden çevir: translate -l "ko" --no-disclaimer

  15. Korece çeviriler için notebook bağlantılarını taşımak (mevcutsa çevrilmiş notebook bağlantılarını güncelle):    migrate-links -l "ko"

  15. Kuru çalıştırma ile bağlantıları taşımak (dosya yazmaz):    migrate-links -l "ko" --dry-run

  16. Çevrilmiş notebooklar varsa güncelle (orijinallere geri dönme):    migrate-links -l "ko" --no-fallback-to-original

  17. Onay komut istemi ile tüm dilleri işle:    migrate-links -l "all"

  18. Tüm dilleri işle ve otomatik onayla:    migrate-links -l "all" -y
  19. migrate-links için günlükleri dosyalara kaydet:    migrate-links -l "ko ja" -s

  20. README dilleri tavsiyesini depo URL'nizle kişiselleştir:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Değerlendirme Örnekleri

> [!WARNING]  
> **Beta Özellik**: Değerlendirme işlevi şu anda beta aşamasındadır. Bu özellik, çevrilmiş belgeleri değerlendirmek için yayınlanmıştır ve değerlendirme yöntemleri ile ayrıntılı uygulama hâlen geliştirilmekte olup değişikliklere tabidir.

  1. Korece çevirileri değerlendir: evaluate -l "ko"

  2. Özel güven eşiği ile değerlendir: evaluate -l "ko" -c 0.8

  3. Hızlı değerlendirme (yalnızca kural tabanlı): evaluate -l "ko" -f

  4. Derin değerlendirme (yalnızca LLM tabanlı): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamaya çalışsak da, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek yanlış anlamalar veya yanlış yorumlardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->