# Kommandoreference

**Co-op Translator** CLI tilbyder flere muligheder for at tilpasse oversættelsesprocessen:

Command                                       | Beskrivelse
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Oversætter dit projekt til angivne sprog. Eksempel: translate -l "es fr de" oversætter til spansk, fransk og tysk. Brug translate -l "all" for at oversætte til alle understøttede sprog.
translate -l "language_codes" -u              | Opdaterer oversættelser ved at slette eksisterende og genoprette dem. Advarsel: Dette sletter alle nuværende oversættelser for angivne sprog.
translate -l "language_codes" -img            | Oversætter kun billedfiler.
translate -l "language_codes" -md             | Oversætter kun Markdown-filer.
translate -l "language_codes" -nb             | Oversætter kun Jupyter-notebook-filer (.ipynb).
translate -l "language_codes" --fix           | Genoversætter filer med lav tillidsgrad baseret på tidligere evalueringsresultater.
translate -l "language_codes" -d              | Aktiverer fejlsøgningsmodus for detaljeret logning.
translate -l "language_codes" --save-logs, -s | Gemmer DEBUG-niveau logs til filer under <root_dir>/logs/ (konsol styres stadig af -d)
translate -l "language_codes" -r "root_dir"   | Angiver rodmappen for projektet
translate -l "language_codes" -f              | Bruger hurtigmodus til billedoversættelse (op til 3x hurtigere gengivelse med en lille omkostning på kvalitet og justering).
translate -l "language_codes" -y              | Bekræft automatisk alle forespørgsler (brugbart til CI/CD-pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktiver eller deaktiver tilføjelse af en disclaimer for maskinoversættelse i oversatte markdown og notebooks (standard: aktiveret).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Tilpas vejledning om README-sprogssektionen (sparse checkout) med dit repository-URL.
translate -l "language_codes" --help          | hjælpedetaljer i CLI, der viser tilgængelige kommandoer
evaluate -l "language_code"                  | Evaluerer oversættelseskvalitet for et specifikt sprog og leverer tillidsvurderinger
evaluate -l "language_code" -c 0.8           | Evaluerer oversættelser med brugerdefineret tillidstærskel
evaluate -l "language_code" -f               | Hurtig evalueringsmodus (kun regelbaseret, ingen LLM)
evaluate -l "language_code" -D               | Dyb evalueringsmodus (kun LLM-baseret, mere grundig men langsommere)
evaluate -l "language_code" --save-logs, -s  | Gemmer DEBUG-niveau logs til filer under <root_dir>/logs/
migrate-links -l "language_codes"             | Genbehandler oversatte Markdown-filer for at opdatere links til notebooks (.ipynb). Foretrækker oversatte notebooks, hvis tilgængelige; ellers kan falde tilbage til originale notebooks.
migrate-links -l "language_codes" -r          | Angiv projektets rodmappe (standard: nuværende mappe).
migrate-links -l "language_codes" --dry-run   | Vis hvilke filer der ville ændres uden at skrive ændringer.
migrate-links -l "language_codes" --no-fallback-to-original | Omdan ikke links til originale notebooks, når oversatte modstykker mangler (opdater kun når oversat findes).
migrate-links -l "language_codes" -d          | Aktiver fejlsøgningsmodus for detaljeret logning.
migrate-links -l "language_codes" --save-logs, -s | Gem DEBUG-niveau logs til filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Bearbejd alle sprog og bekræft advarselsforespørgslen automatisk.

## Brugseksempler

  1. Standardadfærd (tilføj nye oversættelser uden at slette eksisterende):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Tilføj kun nye koreanske billedoversættelser (ingen eksisterende oversættelser slettes):    translate -l "ko" -img

  3. Opdater alle koreanske oversættelser (Advarsel: Dette sletter alle eksisterende koreanske oversættelser før genoversættelse):    translate -l "ko" -u

  4. Opdater kun koreanske billeder (Advarsel: Dette sletter alle eksisterende koreanske billeder før genoversættelse):    translate -l "ko" -img -u

  5. Tilføj nye markdown-oversættelser for koreansk uden at påvirke andre oversættelser:    translate -l "ko" -md

  6. Ret oversættelser med lav tillid baseret på tidligere evalueringsresultater: translate -l "ko" --fix

  7. Ret oversættelser med lav tillid kun for specifikke filer (markdown): translate -l "ko" --fix -md

  8. Ret oversættelser med lav tillid kun for specifikke filer (billeder): translate -l "ko" --fix -img

  9. Brug hurtigmodus til billedoversættelse:    translate -l "ko" -img -f

  10. Ret oversættelser med lav tillid med brugerdefineret tærskel: translate -l "ko" --fix -c 0.8

  11. Eksempel på fejlsøgningsmodus: - translate -l "ko" -d: Aktiver fejllogs.
  12. Gem logs til filer: translate -l "ko" -s
  13. Konsol DEBUG og fil DEBUG: translate -l "ko" -d -s
  14. Oversæt uden at tilføje machine translation disclaimers til output: translate -l "ko" --no-disclaimer

  15. Migrer notebook-links for koreanske oversættelser (opdater links til oversatte notebooks når tilgængelige):    migrate-links -l "ko"

  15. Migrer links med dry-run (ingen filskrivninger):    migrate-links -l "ko" --dry-run

  16. Opdater kun links når oversatte notebooks findes (falder ikke tilbage til originalerne):    migrate-links -l "ko" --no-fallback-to-original

  17. Behandl alle sprog med bekræftelsesprompt:    migrate-links -l "all"

  18. Behandl alle sprog og bekræft automatisk:    migrate-links -l "all" -y
  19. Gem logs til filer for migrate-links:    migrate-links -l "ko ja" -s

  20. Tilpas README sprogvejledning med dit repository-URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluerings-eksempler

> [!WARNING]  
> **Beta-funktion**: Evalueringsfunktionaliteten er i øjeblikket i beta. Denne funktion blev udgivet til at evaluere oversatte dokumenter, og evalueringsmetoder samt detaljeret implementering er stadig under udvikling og kan ændres.

  1. Evaluer koreanske oversættelser: evaluate -l "ko"

  2. Evaluer med brugerdefineret tillidstærskel: evaluate -l "ko" -c 0.8

  3. Hurtig evaluering (kun regelbaseret): evaluate -l "ko" -f

  4. Dyb evaluering (kun LLM-baseret): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->