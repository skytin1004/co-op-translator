# Komandų nuoroda

**Co-op Translator** CLI siūlo keletą parinkčių, leidžiančių suasmeninti vertimo procesą:

Komanda                                      | Aprašymas
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Verčia jūsų projektą į nurodytas kalbas. Pavyzdys: translate -l "es fr de" verčia į ispanų, prancūzų ir vokiečių kalbas. Naudokite translate -l "all", kad išverstumėte visomis palaikomomis kalbomis.
translate -l "language_codes" -u              | Atnaujina vertimus ištrindama esamus ir juos sukurdama iš naujo. Įspėjimas: tai ištrins visus esamus nurodytų kalbų vertimus.
translate -l "language_codes" -img            | Verčia tik paveikslėlių failus.
translate -l "language_codes" -md             | Verčia tik Markdown failus.
translate -l "language_codes" -nb             | Verčia tik Jupyter užrašų knygelių failus (.ipynb).
translate -l "language_codes" --fix           | Iš naujo verčia failus, kurių vertimo pasitikėjimo lygis yra žemas, remiantis ankstesnių vertinimų rezultatais.
translate -l "language_codes" -d              | Įjungia derinimo režimą detaliam žurnale.
translate -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge (konsolės žurnalas valdomas per -d).
translate -l "language_codes" -r "root_dir"   | Nurodo projekto pagrindinį katalogą.
translate -l "language_codes" -f              | Naudoja greitą režimą paveikslėlių vertimui (iki 3 kartų greitesnis piešimo laikas, šiek tiek blogesnė kokybė ir išlyginimas).
translate -l "language_codes" -y              | Automatiškai patvirtina visus raginimus (naudinga CI/CD procesuose).
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Įjungia arba išjungia mašininio vertimo atsakomybės skyrių pridėjimą prie verčiamų markdown ir užrašų knygelių (numatyta: įjungta).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizuoja README kalbų skyriaus patarimus (retas atsisiuntimas) su jūsų saugyklos URL.
translate -l "language_codes" --help          | CLI pagalbos informacija su galimomis komandomis.
evaluate -l "language_code"                    | Įvertina vertimo kokybę tam tikrai kalbai ir pateikia pasitikėjimo balus.
evaluate -l "language_code" -c 0.8             | Įvertina vertimus su pasirinktiniu pasitikėjimo slenksčiu.
evaluate -l "language_code" -f                 | Greitas vertinimo režimas (tik pagal taisykles, be LLM).
evaluate -l "language_code" -D                 | Gilus vertinimo režimas (tik LLM pagrindu, atidžiau, bet lėčiau).
evaluate -l "language_code" --save-logs, -s    | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge.
migrate-links -l "language_codes"               | Perdirba išverstus Markdown failus atnaujinti nuorodas į užrašų knygeles (.ipynb). Teikia pirmenybę išverstoms užrašų knygelėms, jei jų nėra - naudoja originalias.
migrate-links -l "language_codes" -r            | Nurodo projekto pagrindinį katalogą (numatyta: esamas katalogas).
migrate-links -l "language_codes" --dry-run     | Rodo, kurie failai būtų pakeisti, bet nekeičia failų.
migrate-links -l "language_codes" --no-fallback-to-original | Nerevoliucionuoja nuorodų į originalias užrašų knygeles, kai trūksta išverstų (atnaujina tik jei išverstos yra).
migrate-links -l "language_codes" -d            | Įjungia derinimo režimą detaliam žurnale.
migrate-links -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge.
migrate-links -l "all" -y                        | Apdoroja visas kalbas ir automatiškai patvirtina įspėjimo raginimą.

## Naudojimo pavyzdžiai

  1. Numatytoji elgsena (papildyti naujus vertimus neištrinant esamų):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Pridėti tik naujus korėjiečių paveikslėlių vertimus (esami vertimai neištrinami):    translate -l "ko" -img

  3. Atnaujinti visus korėjiečių vertimus (Įspėjimas: tai ištrins visus esamus korėjiečių vertimus prieš verčiant iš naujo):    translate -l "ko" -u

  4. Atnaujinti tik korėjiečių paveikslėlius (Įspėjimas: tai ištrins visus esamus korėjiečių paveikslėlius prieš verčiant iš naujo):    translate -l "ko" -img -u

  5. Pridėti naujus markdown vertimus korėjiečių kalba nekeičiant kitų vertimų:    translate -l "ko" -md

  6. Pataisyti žemos kokybės vertimus remiantis ankstesnių vertinimų rezultatais: translate -l "ko" --fix

  7. Pataisyti žemos kokybės vertimus tik konkretiems failams (markdown): translate -l "ko" --fix -md

  8. Pataisyti žemos kokybės vertimus tik konkretiems failams (paveikslėliai): translate -l "ko" --fix -img

  9. Naudoti greitą režimą paveikslėlių vertimui:    translate -l "ko" -img -f

  10. Pataisyti žemos kokybės vertimus su pasirinktiniu slenksčiu: translate -l "ko" --fix -c 0.8

  11. Derinimo režimo pavyzdys: - translate -l "ko" -d: Įjungia derinimo įrašymą.
  12. Išsaugoti žurnalus į failus: translate -l "ko" -s
  13. Konsolės DEBUG ir failo DEBUG: translate -l "ko" -d -s
  14. Versti neišvedant mašininio vertimo atsakomybės skyrių: translate -l "ko" --no-disclaimer

  15. Migracijos nuorodos korėjiečių vertimams (atnaujina nuorodas į išverstus užrašų knygeles, jei yra):    migrate-links -l "ko"

  15. Migracija su dry-run (be failų rašymo):    migrate-links -l "ko" --dry-run

  16. Nuorodų atnaujinimas tik tada, kai yra išverstos užrašų knygelės (nevykdo gražinimo į originalus):    migrate-links -l "ko" --no-fallback-to-original

  17. Apdoroti visas kalbas su patvirtinimo raginimu:    migrate-links -l "all"

  18. Apdoroti visas kalbas ir automatiškai patvirtinti:    migrate-links -l "all" -y
  19. Išsaugoti žurnalus failuose migracijos nuorodoms:    migrate-links -l "ko ja" -s

  20. Personalizuoti README kalbų patarimus su savo saugyklos URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Vertinimo pavyzdžiai

> [!WARNING]  
> **Beta funkcija**: Vertinimo funkcionalumas šiuo metu yra beta versijoje. Šis įrankis išleistas tam, kad įvertintų išverstus dokumentus, o vertinimo metodai bei detalus įgyvendinimas dar vystomi ir gali keistis.

  1. Įvertinti korėjiečių vertimus: evaluate -l "ko"

  2. Įvertinti su pasirinktiniu pasitikėjimo slenksčiu: evaluate -l "ko" -c 0.8

  3. Greitas vertinimas (tik pagal taisykles): evaluate -l "ko" -f

  4. Gilus vertinimas (tik LLM pagrindu): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas pagrindiniu šaltiniu. Esant kritinei informacijai, rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->