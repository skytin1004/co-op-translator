# Referință comandă

CLI-ul **Co-op Translator** oferă mai multe opțiuni pentru a personaliza procesul de traducere:

Comandă                                       | Descriere
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce proiectul tău în limbile specificate. Exemplu: translate -l "es fr de" traduce în spaniolă, franceză și germană. Folosește translate -l "all" pentru a traduce în toate limbile suportate.
translate -l "language_codes" -u              | Actualizează traducerile prin ștergerea celor existente și recrearea lor. Atenție: Aceasta va șterge toate traducerile curente pentru limbile specificate.
translate -l "language_codes" -img            | Traduce doar fișierele de tip imagine.
translate -l "language_codes" -md             | Traduce doar fișierele Markdown.
translate -l "language_codes" -nb             | Traduce doar fișierele de tip Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraduce fișierele cu scoruri scăzute de încredere bazate pe rezultatele evaluărilor anterioare.
translate -l "language_codes" -d              | Activează modul debug pentru logare detaliată.
translate -l "language_codes" --save-logs, -s | Salvează log-urile la nivel DEBUG în fișiere sub <root_dir>/logs/ (consola rămâne controlată de -d)
translate -l "language_codes" -r "root_dir"   | Specifică directorul rădăcină al proiectului.
translate -l "language_codes" -f              | Folosește modul rapid pentru traducerea imaginilor (până la de 3 ori mai rapid, cu un mic cost pentru calitate și aliniere).
translate -l "language_codes" -y              | Confirmă automat toate prompturile (util pentru pipeline-uri CI/CD).
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Activează sau dezactivează adăugarea unei secțiuni de avertisment privind traducerea automată în markdown tradus și notebook-uri (implicit: activat).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizează secțiunea de limbaje din README (checkout parțial) cu URL-ul depozitului tău.
translate -l "language_codes" --help          | Afișează detalii de ajutor în CLI cu comenzile disponibile.
evaluate -l "language_code"                  | Evaluează calitatea traducerii pentru o limbă specifică și oferă scoruri de încredere.
evaluate -l "language_code" -c 0.8           | Evaluează traducerile cu un prag personalizat de încredere.
evaluate -l "language_code" -f               | Mod de evaluare rapidă (doar pe bază de reguli, fără LLM).
evaluate -l "language_code" -D               | Mod de evaluare aprofundată (bazată pe LLM, mai amănunțit dar mai lent).
evaluate -l "language_code" --save-logs, -s  | Salvează log-urile la nivel DEBUG în fișiere sub <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocesează fișierele Markdown traduse pentru a actualiza link-urile către notebook-uri (.ipynb). Preferă notebook-urile traduse când sunt disponibile; altfel poate reveni la originalele.
migrate-links -l "language_codes" -r          | Specifică directorul rădăcină al proiectului (implicit: directorul curent).
migrate-links -l "language_codes" --dry-run   | Arată care fișiere s-ar schimba fără a scrie efectiv modificări.
migrate-links -l "language_codes" --no-fallback-to-original | Nu rescrie link-urile către notebook-urile originale când echivalentele traduse lipsesc (actualizează doar când există traduse).
migrate-links -l "language_codes" -d          | Activează modul debug pentru logare detaliată.
migrate-links -l "language_codes" --save-logs, -s | Salvează log-urile la nivel DEBUG în fișiere sub <root_dir>/logs/
migrate-links -l "all" -y                      | Procesează toate limbile și confirmă automat promptul de avertizare.

## Exemple de utilizare

  1. Comportament implicit (adaugă traduceri noi fără a șterge pe cele existente):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adaugă doar traduceri noi de imagini coreene (nu se șterg traducerile existente):    translate -l "ko" -img

  3. Actualizează toate traducerile coreene (Atenție: Aceasta șterge toate traducerile coreene existente înainte de retraducere):    translate -l "ko" -u

  4. Actualizează doar imaginile coreene (Atenție: Aceasta șterge toate imaginile coreene existente înainte de retraducere):    translate -l "ko" -img -u

  5. Adaugă traduceri noi markdown pentru coreeană fără a afecta alte traduceri:    translate -l "ko" -md

  6. Repară traducerile cu nivel scăzut de încredere pe baza rezultatelor evaluărilor anterioare: translate -l "ko" --fix

  7. Repară traducerile cu nivel scăzut de încredere doar pentru fișiere specifice (markdown): translate -l "ko" --fix -md

  8. Repară traducerile cu nivel scăzut de încredere doar pentru fișiere specifice (imagini): translate -l "ko" --fix -img

  9. Folosește modul rapid pentru traducerea imaginilor:    translate -l "ko" -img -f

  10. Repară traducerile cu nivel scăzut de încredere cu prag personalizat: translate -l "ko" --fix -c 0.8

  11. Exemplu mod debug: - translate -l "ko" -d: Activează logarea debug.
  12. Salvează loguri în fișiere: translate -l "ko" -s
  13. DEBUG în consolă și DEBUG în fișiere: translate -l "ko" -d -s
  14. Traduce fără a adăuga avertismente privind traducerea automată în ieșiri: translate -l "ko" --no-disclaimer

  15. Migrează link-urile din notebook-uri pentru traducerile coreene (actualizează link-urile către notebook-urile traduse dacă sunt disponibile):    migrate-links -l "ko"

  15. Migrează link-urile în modul dry-run (fără scrierea modificărilor în fișiere):    migrate-links -l "ko" --dry-run

  16. Actualizează link-urile doar când există notebook-uri traduse (nu revine la cele originale):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesează toate limbile cu prompt de confirmare:    migrate-links -l "all"

  18. Procesează toate limbile și confirmă automat:    migrate-links -l "all" -y
  19. Salvează log-uri în fișiere pentru migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizează avertismentul din README despre limbaje cu URL-ul depozitului tău:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exemple de evaluare

> [!WARNING]  
> **Funcționalitate Beta**: Funcționalitatea de evaluare este momentan în beta. Această funcție a fost lansată pentru a evalua documentele traduse, iar metodele de evaluare și implementarea detaliată sunt încă în curs de dezvoltare și pot suferi modificări.

  1. Evaluează traducerile în coreeană: evaluate -l "ko"

  2. Evaluează cu prag personalizat de încredere: evaluate -l "ko" -c 0.8

  3. Evaluare rapidă (doar pe bază de reguli): evaluate -l "ko" -f

  4. Evaluare aprofundată (bazată pe LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertisment**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->