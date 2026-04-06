# Marejeleo ya amri

CLI ya **Co-op Translator** inatoa chaguzi kadhaa za kubinafsisha mchakato wa tafsiri:

Amri                                        | Maelezo
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Inatafsiri mradi wako katika lugha zilizotajwa. Mfano: translate -l "es fr de" inatafsiri kwa Kihispania, Kifaransa, na Kijerumani. Tumia translate -l "all" kutafsiri kwa lugha zote zinazoungiwa mkono.
translate -l "language_codes" -u              | Inasasisha tafsiri kwa kufuta zilizopo na kuzirekebisha tena. Onyo: Hii itafuta tafsiri zote za sasa kwa lugha zilizotajwa.
translate -l "language_codes" -img            | Inatafsiri faili za picha pekee.
translate -l "language_codes" -md             | Inatafsiri faili za Markdown pekee.
translate -l "language_codes" -nb             | Inatafsiri faili za daftari la Jupyter (.ipynb) pekee.
translate -l "language_codes" --fix           | Inarejesha tena faili zilizo na viwango vya chini vya kuaminika kulingana na matokeo ya tathmini ya awali.
translate -l "language_codes" -d              | Inaamsha hali ya uchambuzi kwa kumbukumbu za kina.
translate -l "language_codes" --save-logs, -s | Hifadhi kumbukumbu za kiwango cha DEBUG kwa faili chini ya <root_dir>/logs/ (konsoli bado inasimamiwa na -d)
translate -l "language_codes" -r "root_dir"   | Inaeleza saraka kuu ya mradi
translate -l "language_codes" -f              | Inatumia hali ya haraka kwa tafsiri ya picha (haraka kwa mara 3 katika kuchora kwa gharama kidogo kwa ubora na upangaji).
translate -l "language_codes" -y              | Inathibitisha moja kwa moja kuuliza yote (inayofaa kwa mitiririko ya CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Weka au zima sehemu ya mkupuo wa kutafsiri kwa mashine katika markdown na daftari la tafsiri (chaguo-msingi: imewezeshwa).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Binafsisha maelezo ya sehemu ya lugha kwenye README (uchaguaji mdogo) kwa URL ya ghala lako.
translate -l "language_codes" --help          | maelezo ya msaada ndani ya CLI yanaonyesha amri zinazopatikana
evaluate -l "language_code"                  | Inapima ubora wa tafsiri kwa lugha maalum na hutoa viwango vya kuaminika
evaluate -l "language_code" -c 0.8           | Inapima tafsiri kwa kikomo maalum cha kuaminika
evaluate -l "language_code" -f               | Hali ya tathmini ya haraka (kulingana na kanuni tu, si LLM)
evaluate -l "language_code" -D               | Hali ya tathmini ya kina (inotumia LLM pekee, ndefu zaidi lakini polepole)
evaluate -l "language_code" --save-logs, -s  | Hifadhi kumbukumbu za kiwango cha DEBUG kwa faili chini ya <root_dir>/logs/
migrate-links -l "language_codes"             | Anasaidia tena faili za Markdown zilizotafsiriwa ili kusasisha viungo vya daftari (.ipynb). Inapendelea daftari zilizotafsiriwa pale zinapopatikana; vinginevyo inaweza kurejea kwenye daftari asili.
migrate-links -l "language_codes" -r          | Eleza saraka kuu ya mradi (chaguo-msingi: saraka ya sasa).
migrate-links -l "language_codes" --dry-run   | Onyesha faili gani zingebadilika bila kuandika mabadiliko.
migrate-links -l "language_codes" --no-fallback-to-original | Usibadilishe viungo kwenda kwenye daftari asili pale daftari zilizotafsiriwa zikikosekana (sasisha viungo tu wakati tafsiri ipo).
migrate-links -l "language_codes" -d          | Wezesha hali ya uchambuzi kwa kumbukumbu za kina.
migrate-links -l "language_codes" --save-logs, -s | Hifadhi kumbukumbu za kiwango cha DEBUG kwa faili chini ya <root_dir>/logs/
migrate-links -l "all" -y                      | Shughulikia lugha zote na thibitisha moja kwa moja onyo la kuuliza.

## Mifano ya Matumizi

  1. Tabia ya chaguo-msingi (ongeza tafsiri mpya bila kufuta zilizopo):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ongeza tafsiri mpya za picha za Kikoriani tu (hapafutwi tafsiri zilizopo):    translate -l "ko" -img

  3. Sasisha tafsiri zote za Kikoriani (Onyo: Hii inafuta tafsiri zote za Kikoriani zilizopo kabla ya kutafsiri tena):    translate -l "ko" -u

  4. Sasisha picha za Kikoriani pekee (Onyo: Hii inafuta picha zote za Kikoriani zilizopo kabla ya kutafsiri tena):    translate -l "ko" -img -u

  5. Ongeza tafsiri mpya za markdown za Kikoriani bila kuathiri tafsiri nyingine:    translate -l "ko" -md

  6. Rekebisha tafsiri zenye viwango vya chini vya kuaminika kulingana na matokeo ya tathmini ya awali: translate -l "ko" --fix

  7. Rekebisha tafsiri zenye viwango vya chini kwa faili maalum pekee (markdown): translate -l "ko" --fix -md

  8. Rekebisha tafsiri zenye viwango vya chini kwa faili maalum pekee (picha): translate -l "ko" --fix -img

  9. Tumia hali ya haraka kwa tafsiri ya picha:    translate -l "ko" -img -f

  10. Rekebisha tafsiri zenye viwango vya chini kwa kikomo kibinafsi: translate -l "ko" --fix -c 0.8

  11. Mfano wa hali ya uchambuzi: - translate -l "ko" -d: Weka kumbukumbu za uchambuzi.
  12. Hifadhi kumbukumbu kwenye faili: translate -l "ko" -s
  13. DEBUG ya konzoli na DEBUG ya faili: translate -l "ko" -d -s
  14. Tafsiri bila kuongeza mkupuo wa kutafsiri kwa mashine kwenye matokeo: translate -l "ko" --no-disclaimer

  15. Hamisha viungo vya daftari kwa tafsiri za Kikoriani (sasisha viungo kwenda daftari zilizotafsiriwa pale zinapokuwepo):    migrate-links -l "ko"

  15. Hamisha viungo kwa jaribio la kavu (bila kuandika faili):    migrate-links -l "ko" --dry-run

  16. Sasisha viungo tu wakati daftari zilizotafsiriwa zipo (usirejee kwenye asili):    migrate-links -l "ko" --no-fallback-to-original

  17. Shughulikia lugha zote na kuuliza uthibitisho:    migrate-links -l "all"

  18. Shughulikia lugha zote na kuthibitisha moja kwa moja:    migrate-links -l "all" -y
  19. Hifadhi kumbukumbu kwenye faili kwa migrate-links:    migrate-links -l "ko ja" -s

  20. Binafsisha maelezo ya lugha kwenye README kwa URL ya ghala lako:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Mifano ya Tathmini

> [!WARNING]  
> **Kipengele cha Beta**: Kazi ya tathmini kwa sasa iko katika beta. Kipengele hiki kimetolewa kutathmini hati zilizotafsiriwa, na mbinu za tathmini pamoja na utekelezaji wa kina bado ziko katika maendeleo na zinaweza kubadilika.

  1. Tathmini tafsiri za Kikoriani: evaluate -l "ko"

  2. Tathmini kwa kikomo maalum cha kuaminika: evaluate -l "ko" -c 0.8

  3. Tathmini ya haraka (kanuni tu): evaluate -l "ko" -f

  4. Tathmini ya kina (inotumia LLM tu): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kauli ya Kutolewa**:
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au kasoro. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya mwanadamu inapendekezwa. Hatuwajibiki kwa maelewano au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->