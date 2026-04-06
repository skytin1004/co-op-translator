# Riferimento comandi

La CLI **Co-op Translator** offre diverse opzioni per personalizzare il processo di traduzione:

Command                                       | Descrizione
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce il tuo progetto nelle lingue specificate. Esempio: translate -l "es fr de" traduce in spagnolo, francese e tedesco. Usa translate -l "all" per tradurre in tutte le lingue supportate.
translate -l "language_codes" -u              | Aggiorna le traduzioni eliminando quelle esistenti e ricreandole. Attenzione: questo eliminerà tutte le traduzioni attuali per le lingue specificate.
translate -l "language_codes" -img            | Traduce solo i file immagine.
translate -l "language_codes" -md             | Traduce solo i file Markdown.
translate -l "language_codes" -nb             | Traduce solo i file Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Ritraduce i file con punteggi di confidenza bassi basati sui risultati delle valutazioni precedenti.
translate -l "language_codes" -d              | Attiva la modalità debug per log dettagliati.
translate -l "language_codes" --save-logs, -s | Salva i log a livello DEBUG in file sotto <root_dir>/logs/ (la console rimane controllata da -d)
translate -l "language_codes" -r "root_dir"   | Specifica la directory root del progetto
translate -l "language_codes" -f              | Usa la modalità veloce per la traduzione delle immagini (fino a 3x più veloce con un leggero compromesso su qualità e allineamento).
translate -l "language_codes" -y              | Conferma automaticamente tutte le richieste (utile per pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Abilita o disabilita l'aggiunta di una sezione di disclaimer sulla traduzione automatica ai markdown e notebook tradotti (default: abilitato).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizza l’avviso nella sezione lingue del README (sparse checkout) con l'URL del tuo repository.
translate -l "language_codes" --help          | Dettagli di aiuto all'interno della CLI mostrando i comandi disponibili
evaluate -l "language_code"                  | Valuta la qualità della traduzione per una lingua specifica e fornisce punteggi di confidenza
evaluate -l "language_code" -c 0.8           | Valuta le traduzioni con soglia di confidenza personalizzata
evaluate -l "language_code" -f               | Modalità di valutazione veloce (basata solo su regole, senza LLM)
evaluate -l "language_code" -D               | Modalità di valutazione approfondita (basata solo su LLM, più accurata ma più lenta)
evaluate -l "language_code" --save-logs, -s  | Salva i log a livello DEBUG in file sotto <root_dir>/logs/
migrate-links -l "language_codes"             | Rielabora i file Markdown tradotti per aggiornare i collegamenti ai notebook (.ipynb). Preferisce i notebook tradotti quando disponibili; altrimenti può ricadere sui notebook originali.
migrate-links -l "language_codes" -r          | Specifica la directory root del progetto (default: directory corrente).
migrate-links -l "language_codes" --dry-run   | Mostra quali file cambierebbero senza scrivere modifiche.
migrate-links -l "language_codes" --no-fallback-to-original | Non riscrive i link ai notebook originali quando mancano i corrispondenti tradotti (aggiorna solo quando il tradotto esiste).
migrate-links -l "language_codes" -d          | Abilita la modalità debug per log dettagliati.
migrate-links -l "language_codes" --save-logs, -s | Salva i log a livello DEBUG in file sotto <root_dir>/logs/
migrate-links -l "all" -y                      | Elabora tutte le lingue e conferma automaticamente l'avviso.

## Esempi d’uso

  1. Comportamento predefinito (aggiunge nuove traduzioni senza eliminare quelle esistenti):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Aggiungi solo nuove traduzioni di immagini coreane (nessuna traduzione esistente viene eliminata):    translate -l "ko" -img

  3. Aggiorna tutte le traduzioni coreane (Attenzione: questo elimina tutte le traduzioni coreane esistenti prima della ritraduzione):    translate -l "ko" -u

  4. Aggiorna solo le immagini coreane (Attenzione: questo elimina tutte le immagini coreane esistenti prima della ritraduzione):    translate -l "ko" -img -u

  5. Aggiungi nuove traduzioni markdown per il coreano senza influire sulle altre traduzioni:    translate -l "ko" -md

  6. Correggi le traduzioni con bassa confidenza basate sui risultati delle valutazioni precedenti: translate -l "ko" --fix

  7. Correggi le traduzioni con bassa confidenza solo per file specifici (markdown): translate -l "ko" --fix -md

  8. Correggi le traduzioni con bassa confidenza solo per file specifici (immagini): translate -l "ko" --fix -img

  9. Usa la modalità veloce per la traduzione delle immagini:    translate -l "ko" -img -f

  10. Correggi le traduzioni con bassa confidenza con soglia personalizzata: translate -l "ko" --fix -c 0.8

  11. Esempio modalità debug: - translate -l "ko" -d: Abilita log di debug.
  12. Salva i log in file: translate -l "ko" -s
  13. DEBUG console e DEBUG file: translate -l "ko" -d -s
  14. Traduce senza aggiungere disclaimer di traduzione automatica ai risultati: translate -l "ko" --no-disclaimer

  15. Migra link ai notebook per le traduzioni coreane (aggiorna i link ai notebook tradotti se disponibili):    migrate-links -l "ko"

  15. Migra link con dry-run (nessuna scrittura su file):    migrate-links -l "ko" --dry-run

  16. Aggiorna link solo quando esistono notebook tradotti (non fare fallback agli originali):    migrate-links -l "ko" --no-fallback-to-original

  17. Elabora tutte le lingue con richiesta di conferma:    migrate-links -l "all"

  18. Elabora tutte le lingue e conferma automaticamente:    migrate-links -l "all" -y
  19. Salva i log in file per migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizza l’avviso delle lingue nel README con l’URL del tuo repo:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Esempi di valutazione

> [!WARNING]  
> **Funzionalità Beta**: La funzionalità di valutazione è attualmente in beta. Questa funzione è stata rilasciata per valutare i documenti tradotti, e i metodi di valutazione e l'implementazione dettagliata sono ancora in fase di sviluppo e soggetti a modifiche.

  1. Valuta le traduzioni coreane: evaluate -l "ko"

  2. Valuta con soglia di confidenza personalizzata: evaluate -l "ko" -c 0.8

  3. Valutazione veloce (solo basata su regole): evaluate -l "ko" -f

  4. Valutazione approfondita (solo basata su LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mentre ci impegniamo per l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->