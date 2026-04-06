# Komandų nuoroda

**Co-op Translator** CLI siūlo kelias parinktis vertimo procesui pritaikyti:

Komanda                                      | Aprašymas
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Išverčia jūsų projektą į nurodytas kalbas. Pavyzdys: translate -l "es fr de" išvers ispanų, prancūzų ir vokiečių kalbomis. Naudokite translate -l "all", kad išverstų į visas palaikomas kalbas.
translate -l "language_codes" -u              | Atnaujina vertimus ištrinant esamus ir sukuriant juos iš naujo. Įspėjimas: tai ištrins visus šiuo metu esančius vertimus nurodytomis kalbomis.
translate -l "language_codes" -img            | Verčia tik vaizdų failus.
translate -l "language_codes" -md             | Verčia tik Markdown failus.
translate -l "language_codes" -nb             | Verčia tik Jupyter užrašų knygelių failus (.ipynb).
translate -l "language_codes" --fix           | Išverčia failus iš naujo, kurių vertimų patikimumo įvertis žemas, remiantis ankstesniais įvertinimų rezultatais.
translate -l "language_codes" -d              | Įjungia žurnalo detalumo režimą.
translate -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge (konsolė lieka kontroliuojama -d parinkties)
translate -l "language_codes" -r "root_dir"   | Nurodo projekto šaknies katalogą
translate -l "language_codes" -f              | Naudoja greitą režimą vaizdų vertimui (iki 3 kartų greitesnis braižymas su šiek tiek prastesne kokybe ir suderinamumu).
translate -l "language_codes" -y              | Automatiškai patvirtina visus raginimus (naudinga CI/CD procesuose)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Įjungia arba išjungia mašininio vertimo atsakomybės apribojimo skilties pridėjimą prie išverstų markdown ir užrašų knygelių (numatytoji reikšmė: įjungta).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Asmenina README kalbų patarimų skiltį (sparse checkout) su jūsų saugyklos URL.
translate -l "language_codes" --help          | padeda CLI rodyti galimas komandas
evaluate -l "language_code"                  | Įvertina konkrečios kalbos vertimų kokybę ir pateikia pasitikėjimo balus
evaluate -l "language_code" -c 0.8           | Įvertina vertimus su pasirinktu pasitikėjimo slenksčiu
evaluate -l "language_code" -f               | Greito vertinimo režimas (tik taisyklėmis, be LLM)
evaluate -l "language_code" -D               | Gilus vertinimo režimas (tik LLM pagrindu, kruopštesnis bet lėtesnis)
evaluate -l "language_code" --save-logs, -s  | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/
migrate-links -l "language_codes"             | Pakartotinai apdoroja išverstus Markdown failus, kad atnaujintų nuorodas į užrašų knygeles (.ipynb). Pirmenybė suteikiama išverstoms užrašų knygelėms, jei yra; priešingu atveju gali grįžti prie originalių.
migrate-links -l "language_codes" -r          | Nurodo projekto šaknies katalogą (numatytas: esamas katalogas).
migrate-links -l "language_codes" --dry-run   | Parodo, kurie failai pasikeistų, bet neįrašo pakeitimų.
migrate-links -l "language_codes" --no-fallback-to-original | Nekeičia nuorodų į originalias užrašų knygeles, kai trūksta išverstų atitikmenų (atnaujina tik, kai yra išverstos).
migrate-links -l "language_codes" -d          | Įjungia žurnalo detalumo režimą.
migrate-links -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/
migrate-links -l "all" -y                      | Apdoroja visas kalbas ir automatiškai patvirtina įspėjimą.

## Naudojimo pavyzdžiai

  1. Numatytoji elgsena (papildo naujus vertimus neištrindama esamų):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Prideda tik naujus korėjiečių vaizdų vertimus (esami vertimai neištrinami):    translate -l "ko" -img

  3. Atnaujina visus korėjiečių vertimus (Įspėjimas: tai ištrins visus esamus korėjiečių vertimus prieš išverčiant iš naujo):    translate -l "ko" -u

  4. Atnaujina tik korėjiečių vaizdus (Įspėjimas: tai ištrins visus esamus korėjiečių vaizdus prieš išverčiant iš naujo):    translate -l "ko" -img -u

  5. Prideda naujus korėjiečių Markdown vertimus nepaveikdama kitų vertimų:    translate -l "ko" -md

  6. Taiso žemo pasitikėjimo vertimus, remiantis ankstesniais įvertinimų rezultatais: translate -l "ko" --fix

  7. Taiso žemo pasitikėjimo vertimus tik konkretiems failams (Markdown): translate -l "ko" --fix -md

  8. Taiso žemo pasitikėjimo vertimus tik konkretiems failams (vaizdai): translate -l "ko" --fix -img

  9. Naudoja greitą režimą vaizdų vertimui:    translate -l "ko" -img -f

  10. Taiso žemo pasitikėjimo vertimus su pasirinktu slenksčiu: translate -l "ko" --fix -c 0.8

  11. Derinimo režimo pavyzdys: - translate -l "ko" -d: Įjungia derinimo žurnalų rašymą.
  12. Žurnalų išsaugojimas į failus: translate -l "ko" -s
  13. Konsolės DEBUG ir failų DEBUG: translate -l "ko" -d -s
  14. Vertimas be mašininio vertimo atsakomybės apribojimų pridėjimo: translate -l "ko" --no-disclaimer

  15. Migravimas nuorodoms į užrašų knygeles korėjiečių vertimuose (atnaujina nuorodas į išverstus užrašų knygeles, jei yra):    migrate-links -l "ko"

  15. Migravimas su dry-run (be failų įrašymo):    migrate-links -l "ko" --dry-run

  16. Atnaujina nuorodas tik kai yra išverstų užrašų knygelių (negrįžta prie originalų):    migrate-links -l "ko" --no-fallback-to-original

  17. Apdoroja visas kalbas su patvirtinimo raginimu:    migrate-links -l "all"

  18. Apdoroja visas kalbas ir automatiškai patvirtina:    migrate-links -l "all" -y
  19. Žurnalų išsaugojimas migrate-links komandai:    migrate-links -l "ko ja" -s

  20. Prasikonsultuokite README kalbų patarimų skyrių su savo saugyklos URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Vertinimo pavyzdžiai

> [!WARNING]  
> **Beta funkcija**: Vertinimo funkcionalumas šiuo metu yra beta stadijoje. Ši funkcija išleista vertinti išverstus dokumentus, o vertinimo metodai ir detalus įgyvendinimas vis dar plėtojami ir gali keistis.

  1. Įvertinkite korėjiečių vertimus: evaluate -l "ko"

  2. Vertinimas su pasirinktu pasitikėjimo slenksčiu: evaluate -l "ko" -c 0.8

  3. Greitas vertinimas (tik taisyklėmis): evaluate -l "ko" -f

  4. Gilus vertinimas (tik LLM pagrindu): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar klaidingus interpretavimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->