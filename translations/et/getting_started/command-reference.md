# Käskude viide

**Co-op Translator** CLI pakub mitmeid valikuid tõlketegevuse kohandamiseks:

Käsk                                        | Kirjeldus
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | Tõlgib teie projekti määratud keeltesse. Näide: translate -l "es fr de" tõlgib hispaania, prantsuse ja saksa keelde. Kasutage translate -l "all", et tõlkida kõigisse toetatud keeltesse.
translate -l "language_codes" -u            | Uuendab tõlkeid, kustutades olemasolevad ja luues neid uuesti. Hoiduge: see kustutab kõik määratud keelte praegused tõlked.
translate -l "language_codes" -img          | Tõlgib ainult pildifaile.
translate -l "language_codes" -md           | Tõlgib ainult Markdown-faile.
translate -l "language_codes" -nb           | Tõlgib ainult Jupyteri märkmikefaile (.ipynb).
translate -l "language_codes" --fix         | Tõlgib uuesti faile, millele eelnevate hindamistulemuste põhjal anti madal usaldustase.
translate -l "language_codes" -d            | Lubab silumisrežiimi üksikasjalikuks logimiseks.
translate -l "language_codes" --save-logs, -s | Salvestab DEBUG-taseme logid failidesse kaustas <root_dir>/logs/ (konsoolile puudutab see -d)
translate -l "language_codes" -r "root_dir" | Määrab projekti juurkausta
translate -l "language_codes" -f            | Kasutab pildi tõlkimisel kiiret režiimi (kuni 3x kiirema joonistamisega väikese kvaliteedi ja joonduste kulu eest).
translate -l "language_codes" -y            | Automaatne kõigi toimingute kinnitamine (kasulik CI/CD töövoogudes)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Lubab või keelab automaatse masintõlke ärakirja lisamise tõlgitud Markdown'i ja märkmike lõiku (vaikimisi lubatud).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliseeri README keelte jaotises nõuandeid (sparse checkout) oma repositooriumi URL-iga.
translate -l "language_codes" --help        | Aitab CLI sees saada kasutada olevaid käske
evaluate -l "language_code"                  | Hindab tõlke kvaliteeti konkreetses keeles ja annab usaldustasemeid
evaluate -l "language_code" -c 0.8           | Hindab tõlkeid kohandatud usalduskünnisega
evaluate -l "language_code" -f               | Kiire hindamine (ainult reeglitepõhine, ilma LLMita)
evaluate -l "language_code" -D               | Sügav hindamine (ainult LLM-põhine, põhjalikum, kuid aeglasem)
evaluate -l "language_code" --save-logs, -s  | Salvestab DEBUG-taseme logid failidesse kaustas <root_dir>/logs/
migrate-links -l "language_codes"             | Töötleb uuesti tõlgitud Markdown-faile, et uuendada linke märkmikele (.ipynb). Andma eelistust tõlgitud märkmikele kui saadaval; muidu võib langetada tagasi algsete märkmikeni.
migrate-links -l "language_codes" -r          | Määratle projekti juurkaust (vaikimisi: käimasolev kataloog).
migrate-links -l "language_codes" --dry-run   | Näita, millised failid muutuksid ilma muutusi salvestamata.
migrate-links -l "language_codes" --no-fallback-to-original | Ära muuda linke algsetele märkmikele, kui tõlgitud vasted puuduvad (uuendatakse ainult kui tõlgitud versioonid olemas).
migrate-links -l "language_codes" -d          | Lubab silumisrežiimi üksikasjalikuks logimiseks.
migrate-links -l "language_codes" --save-logs, -s | Salvestab DEBUG-taseme logid failidesse kaustas <root_dir>/logs/
migrate-links -l "all" -y                      | Töötleb kõiki keeli ja kinnitab hoiatusviiba automaatselt.

## Kasutusnäited

  1. Vaikimisi käitumine (lisa uusi tõlkeid ilma olemasolevaid kustutamata):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisa ainult uued Korea pilditõlked (olemasolevaid tõlkeid ei kustutata):    translate -l "ko" -img

  3. Uuenda kõiki Korea tõlkeid (Hoida! See kustutab kõik olemasolevad Korea tõlked enne ümbertõlkimist):    translate -l "ko" -u

  4. Uuenda ainult Korea pilte (Hoida! See kustutab kõik olemasolevad Korea pildid enne ümbertõlkimist):    translate -l "ko" -img -u

  5. Lisa uued Korea Markdown'i tõlked ilma teiste tõlgete mõjutamiseta:    translate -l "ko" -md

  6. Paranda madala usaldusega tõlkeid eelnevate hindamistulemuste põhjal: translate -l "ko" --fix

  7. Paranda madala usaldusega tõlkeid ainult konkreetsetes failides (Markdown): translate -l "ko" --fix -md

  8. Paranda madala usaldusega tõlkeid ainult konkreetsetes failides (pildid): translate -l "ko" --fix -img

  9. Kasuta pildi tõlkimisel kiiret režiimi:    translate -l "ko" -img -f

  10. Paranda madala usaldusega tõlkeid kohandatud lävega: translate -l "ko" --fix -c 0.8

  11. Silumisrežiimi näide: - translate -l "ko" -d: Luba silumislogimine.
  12. Salvesta logisid failidesse: translate -l "ko" -s
  13. Konsooli DEBUG ja faili DEBUG: translate -l "ko" -d -s
  14. Tõlgi ilma masintõlke ärakirjade lisamiseta väljundisse: translate -l "ko" --no-disclaimer

  15. Migreeri Korea tõlgete märkmike lingid (uuenda linke tõlgitud märkmikele, kui saadaval):    migrate-links -l "ko"

  15. Migreeri lingid kuivjooksuga (mitte salvestada muudatusi):    migrate-links -l "ko" --dry-run

  16. Uuendada linke ainult kui tõlgitud märkmikud olemas (ära lange tagasi originaalide juurde):    migrate-links -l "ko" --no-fallback-to-original

  17. Töötle kõiki keeli kinnituseväljaga:    migrate-links -l "all"

  18. Töötle kõiki keeli ja kinnita automaatselt:    migrate-links -l "all" -y
  19. Salvesta logisid failides migrate-links jaoks:    migrate-links -l "ko ja" -s

  20. Isikupärasta README keelte osas nõuandeid oma repositooriumi URL-iga:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Hinnangu näited

> [!WARNING]  
> **Beeta funktsioon**: Hindamisfunktsionaalsus on hetkel beeta staadiumis. See funktsioon vabastati tõlgitud dokumentide hindamiseks ning hindamismeetodid ja täpsem teostus on endiselt arendamisel ja võivad muutuda.

  1. Hinda Korea tõlkeid: evaluate -l "ko"

  2. Hinda kohandatud usalduskünnisega: evaluate -l "ko" -c 0.8

  3. Kiire hindamine (ainult reeglitepõhine): evaluate -l "ko" -f

  4. Sügav hindamine (ainult LLM-põhine): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algses keeles tuleks võtta autoriteetse allikana. Olulise info puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta üheselt mõistmise või valesti tõlgendamise eest, mis võib tekkida selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->