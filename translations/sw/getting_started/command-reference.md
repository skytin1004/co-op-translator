# Marejeleo ya amri

CLI ya **Co-op Translator** inatoa chaguzi kadhaa za kubinafsisha mchakato wa tafsiri:

Amri                                         | Maelezo
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Hutafsiri mradi wako kwa lugha zilizobainishwa. Mfano: translate -l "es fr de" hutafsiri kwa Kihispania, Kifaransa, na Kijerumani. Tumia translate -l "all" kutafsiri kwa lugha zote zinazoungwa mkono.
translate -l "language_codes" -u              | Huvunja tafsiri zilizopo tena kwa kufuta za zamani na kuzitengeneza upya. Onyo: Hii itafuta tafsiri zote za sasa za lugha zilizobainishwa.
translate -l "language_codes" -img            | Hutafsiri faili za picha tu.
translate -l "language_codes" -md             | Hutafsiri faili za Markdown tu.
translate -l "language_codes" -nb             | Hutafsiri faili za daftari la Jupyter (.ipynb) tu.
translate -l "language_codes" --fix           | Hutafsiri upya faili zilizo na alama za kuaminika kidogo kulingana na matokeo ya tathmini ya awali.
translate -l "language_codes" -d              | Huongeza hali ya utatuzi kwa ufafanuzi wa kina wa kumbukumbu.
translate -l "language_codes" --save-logs, -s | Hifadhi kumbukumbu za kiwango cha DEBUG kwenye faili chini ya <root_dir>/logs/ (ukurasa wa amri unaendelea kudhibitiwa na -d)
translate -l "language_codes" -r "root_dir"   | Inabainisha saraka kuu ya mradi
translate -l "language_codes" -f              | Inatumia hali ya haraka kwa tafsiri ya picha (kinafanya mchoro haraka mara 3 kwa gharama kidogo ya ubora na upangilio).
translate -l "language_codes" -y              | Thibitisha kiotomatiki maagizo yote (muhimu kwa mifumo ya CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Washa au uzime kuongeza sehemu ya onyo la tafsiri ya mashine kwenye markdown na daftari za tafsiri (chaguo-msingi: washwa).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Badilisha ushauri wa sehemu ya lugha za README (katika uteuzi mdogo) kwa kutumia URL ya hazina yako.
translate -l "language_codes" --help          | maelezo ya msaada ndani ya CLI yanaonyesha amri zinazopatikana
evaluate -l "language_code"                  | Tathmini ubora wa tafsiri kwa lugha fulani na toa alama za kuaminika
evaluate -l "language_code" -c 0.8           | Tathmini tafsiri kwa msimamo wa kuaminika wa kibinafsi
evaluate -l "language_code" -f               | Hali ya tathmini ya haraka (kwa kutumia sheria tu, hakuna LLM)
evaluate -l "language_code" -D               | Hali ya tathmini ya kina (kwa kutumia LLM tu, zaidi lakini polepole)
evaluate -l "language_code" --save-logs, -s  | Hifadhi kumbukumbu za kiwango cha DEBUG kwenye faili chini ya <root_dir>/logs/
migrate-links -l "language_codes"             | Fanya upya faili za Markdown zilizo tafsiriwa ili kusasisha viungo kwenda daftari (.ipynb). Inapendelea daftari za tafsiri inapopatikana; vinginevyo inaweza kurudi kwenye daftari za awali.
migrate-links -l "language_codes" -r          | Baini saraka kuu ya mradi (chaguo-msingi: saraka ya sasa).
migrate-links -l "language_codes" --dry-run   | Onyesha faili gani zingebadilika bila kuandika mabadiliko.
migrate-links -l "language_codes" --no-fallback-to-original | Usibadilishe viungo kwenda daftari za asili wakati nakala za tafsiri hazipo (sasisha tu wakati tafsiri ipo).
migrate-links -l "language_codes" -d          | Washa hali ya utatuzi kwa kumbukumbu za kina.
migrate-links -l "language_codes" --save-logs, -s | Hifadhi kumbukumbu za kiwango cha DEBUG kwenye faili chini ya <root_dir>/logs/
migrate-links -l "all" -y                      | Fanyia kazi lugha zote na uthibitishe kiotomatiki onyo la tahadhari.

## Mifano ya Matumizi

  1. Tabia ya kawaida (ongeza tafsiri mpya bila kufuta zilizopo):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ongeza tafsiri mpya za picha za Kikorea pekee (hapana tafsiri zilizopo zifutwe):    translate -l "ko" -img

  3. Sasisha tafsiri zote za Kikorea (Onyo: Hii inafuta tafsiri zote za Kikorea zilizopo kabla ya kutafsiri upya):    translate -l "ko" -u

  4. Sasisha picha za Kikorea pekee (Onyo: Hii inafuta picha zote zilizopo za Kikorea kabla ya kutafsiri upya):    translate -l "ko" -img -u

  5. Ongeza tafsiri mpya za markdown kwa Kikorea bila kuathiri tafsiri zingine:    translate -l "ko" -md

  6. Rekebisha tafsiri za kuaminika kidogo kulingana na matokeo ya tathmini ya awali: translate -l "ko" --fix

  7. Rekebisha tafsiri za kuaminika kidogo kwa faili maalum pekee (markdown): translate -l "ko" --fix -md

  8. Rekebisha tafsiri za kuaminika kidogo kwa faili maalum pekee (picha): translate -l "ko" --fix -img

  9. Tumia hali ya haraka kwa tafsiri ya picha:    translate -l "ko" -img -f

  10. Rekebisha tafsiri za kuaminika kidogo kwa kiwango cha kuaminika maalum: translate -l "ko" --fix -c 0.8

  11. Mfano wa hali ya utatuzi: - translate -l "ko" -d: Washa kumbukumbu za utatuzi.
  12. Hifadhi kumbukumbu kwenye faili: translate -l "ko" -s
  13. DEBUG ya console na DEBUG ya faili: translate -l "ko" -d -s
  14. Tafsiri bila kuongeza onyo la tafsiri ya mashine kwenye matokeo: translate -l "ko" --no-disclaimer

  15. Hamisha viungo vya daftari kwa tafsiri za Kikorea (sasisha viungo kwenye daftari za tafsiri inapopatikana):    migrate-links -l "ko"

  15. Hamisha viungo kwa jaribio la kavu (hakuna kuandika faili):    migrate-links -l "ko" --dry-run

  16. Sasisha viungo tu wakati daftari za tafsiri zipo (usirudi kwenye asili):    migrate-links -l "ko" --no-fallback-to-original

  17. Fanyia kazi lugha zote kwa onyo la uthibitisho:    migrate-links -l "all"

  18. Fanyia kazi lugha zote na uthibitishe kiotomatiki:    migrate-links -l "all" -y
  19. Hifadhi kumbukumbu kwa migrate-links:    migrate-links -l "ko ja" -s

  20. Badilisha ushauri wa lugha za README kwa URL ya hazina yako:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Mifano ya Tathmini

> [!WARNING]  
> **Kipengele cha Beta**: Kazi ya tathmini kwa sasa iko katika beta. Kipengele hiki kiliwekwa kutathmini hati zilizotafsiriwa, na mbinu za tathmini na utekelezaji wa kina bado zipo kwenye maendeleo na zinaweza kubadilika.

  1. Tathmini tafsiri za Kikorea: evaluate -l "ko"

  2. Tathmini kwa msimamo wa kuaminika wa kibinafsi: evaluate -l "ko" -c 0.8

  3. Tathmini ya haraka (kwa kutumia sheria tu): evaluate -l "ko" -f

  4. Tathmini ya kina (kwa kutumia LLM tu): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Maelezo ya Kutojihusisha**:  
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei kuyumba kwa maana au makosa ya tafsiri yanayotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->