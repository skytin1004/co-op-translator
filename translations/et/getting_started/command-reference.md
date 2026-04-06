# Käskude viide

**Co-op Translator** CLI pakub mitmeid valikuid tõlkeprotsessi kohandamiseks:

Käsk                                             | Kirjeldus
-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                     | Tõlkib teie projekti määratud keeltesse. Näide: translate -l "es fr de" tõlgib hispaania, prantsuse ja saksa keelde. Kasutage translate -l "all", et tõlkida kõikide toetatud keelte jaoks.
translate -l "language_codes" -u                  | Uuendab tõlkeid, kustutades olemasolevad ja luues need uuesti. Teade: see kustutab kõik praegused tõlked määratud keeltes.
translate -l "language_codes" -img                | Tõlgib ainult pildifaile.
translate -l "language_codes" -md                 | Tõlgib ainult Markdown-faile.
translate -l "language_codes" -nb                 | Tõlgib ainult Jupyter märkmikufaile (.ipynb).
translate -l "language_codes" --fix               | Tõlgib uuesti failid, mille usaldusväärsuse hinnang on madal varasemate hindamistulemuste põhjal.
translate -l "language_codes" -d                  | Lubab silumisrežiimi üksikasjalikuks logimiseks.
translate -l "language_codes" --save-logs, -s     | Salvestab DEBUG-taseme logid failidesse kaustas <root_dir>/logs/ (konsool jääb -d kontrolli alla)
translate -l "language_codes" -r "root_dir"       | Määrab projekti juurkausta
translate -l "language_codes" -f                   | Kasutab piltide tõlkimiseks kiiret režiimi (kuni 3x kiirem plotimine veidi madalama kvaliteedi ja joondustulemusega).
translate -l "language_codes" -y                   | Kinnitab automaatselt kõik dialoogid (kasulik CI/CD torujuhtmete jaoks)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Lülitab sisse või välja masina tõlke kohustusliku teavituse lisamise tõlgitud markdown- ja märkmikufailidesse (vaikimisi sisse lülitatud).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Isikupärasta README keelte sektsiooni soovitusteksti oma hoidla URL-iga.
translate -l "language_codes" --help              | Abi üksikasjad CLI-s saadaolevate käskude kohta
evaluate -l "language_code"                        | Hinnake tõlke kvaliteeti konkreetse keele puhul ja andke usaldusväärsuse skoorid
evaluate -l "language_code" -c 0.8                 | Hinnake tõlkeid kohandatud usaldusväärsuse lävega
evaluate -l "language_code" -f                     | Kiire hindamisrežiim (ainult reeglipõhine, ilma LLM-ita)
evaluate -l "language_code" -D                     | Sügava hindamise režiim (ainult LLM-põhine, põhjalikum, kuid aeglasem)
evaluate -l "language_code" --save-logs, -s        | Salvestab DEBUG-taseme logid failidesse kaustas <root_dir>/logs/
migrate-links -l "language_codes"                  | Töötleb uuesti tõlgitud Markdown-faile, et uuendada lingid märkmikufailidele (.ipynb). Eelistab tõlgitud märkmikke, kui need olemas; vastasel juhul võib langetada tagasi originaalsetele märkmikele.
migrate-links -l "language_codes" -r                | Määrake projekti juurkaust (vaikimisi: praegune kataloog).
migrate-links -l "language_codes" --dry-run         | Näitab, millised failid muutuksid, ilma et muudatusi kirjutataks.
migrate-links -l "language_codes" --no-fallback-to-original | Ärge tõlked puudumisel uuendage linke originaalsetele märkmikele (uuendatakse ainult siis, kui tõlgitud versioon on olemas).
migrate-links -l "language_codes" -d                | Lubab silumisrežiimi üksikasjalikuks logimiseks.
migrate-links -l "language_codes" --save-logs, -s   | Salvestab DEBUG-taseme logid failidesse kaustas <root_dir>/logs/
migrate-links -l "all" -y                            | Töötle kõiki keeli ja kinnita hoiatusdialoog automaatselt.

## Kasutusnäited

  1. Vaikimisi käitumine (lisa uusi tõlkeid ilma olemasolevaid kustutamata):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisa ainult uued korea pilditõlked (olemasolevaid tõlkeid ei kustutata):    translate -l "ko" -img

  3. Uuenda kõiki korea tõlkeid (Hoiatus: see kustutab kõik olemasolevad korea tõlked enne uuesti tõlkimist):    translate -l "ko" -u

  4. Uuenda ainult korea pilte (Hoiatus: see kustutab kõik olemasolevad korea pildid enne uuesti tõlkimist):    translate -l "ko" -img -u

  5. Lisa uued korea markdown tõlked mõjutamata teisi tõlkeid:    translate -l "ko" -md

  6. Paranda madala usaldusväärsusega tõlkeid varasemate hindamistulemuste põhjal: translate -l "ko" --fix

  7. Paranda madala usaldusväärsusega tõlkeid ainult konkreetsetel failidel (markdown): translate -l "ko" --fix -md

  8. Paranda madala usaldusväärsusega tõlkeid ainult konkreetsetel failidel (pildid): translate -l "ko" --fix -img

  9. Kasuta piltide tõlkimiseks kiiret režiimi:    translate -l "ko" -img -f

  10. Paranda madala usaldusväärsusega tõlkeid kohandatud lävega: translate -l "ko" --fix -c 0.8

  11. Silumisrežiimi näide: - translate -l "ko" -d: Lubab silumislogi.
  12. Salvesta logid failidesse: translate -l "ko" -s
  13. Konsooli DEBUG ja faili DEBUG: translate -l "ko" -d -s
  14. Tõlkimine ilma masina tõlke vastutuseavalduse lisamiseta väljunditesse: translate -l "ko" --no-disclaimer

  15. Märkmikelingide migreerimine korea tõlgete jaoks (uuendab linke tõlgitud märkmikele, kui need olemas):    migrate-links -l "ko"

  15. Lingide migreerimine kuivjooksuga (failidesse ei kirjutata):    migrate-links -l "ko" --dry-run

  16. Uuenda linke ainult siis, kui tõlgitud märkmikud olemas (ärge langetage tagasi originaalsetele):    migrate-links -l "ko" --no-fallback-to-original

  17. Töötle kõiki keeli koos kinnituskäsuga:    migrate-links -l "all"

  18. Töötle kõiki keeli ja kinnita automaatselt:    migrate-links -l "all" -y
  19. Salvesta migrate-links logid failidesse:    migrate-links -l "ko ja" -s

  20. Isikupärasta README keelte teavitus oma repo URL-iga:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Hindamise näited

> [!WARNING]  
> **Beetafunktsioon**: Hindamisfunktsioon on praegu beetaversioonis. See funktsioon avaldati tõlgitud dokumentide hindamiseks ning hindamismeetodid ja üksikasjalik teostus on endiselt arendamisel ja võivad muutuda.

  1. Hinda korea tõlkeid: evaluate -l "ko"

  2. Hinda kohandatud usaldusväärsuse lävega: evaluate -l "ko" -c 0.8

  3. Kiire hindamine (ainult reeglipõhine): evaluate -l "ko" -f

  4. Sügav hindamine (ainult LLM-põhine): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellekti tõlkimisteenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüdleme täpsuse poole, pidage meeles, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles tuleks pidada autoriteetseks allikaks. Olulise info puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud valearusaamade või tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->