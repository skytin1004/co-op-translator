# Command reference

The **Co-op Translator** CLI offre diverse opzioni per personalizzare il processo di traduzione:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce il tuo progetto nelle lingue specificate. Esempio: translate -l "es fr de" traduce in spagnolo, francese e tedesco. Usa translate -l "all" per tradurre in tutte le lingue supportate.
translate -l "language_codes" -u              | Aggiorna le traduzioni eliminando quelle esistenti e ricreandole. Attenzione: questo eliminerà tutte le traduzioni attuali per le lingue specificate.
translate -l "language_codes" -img            | Traduce solo i file immagine.
translate -l "language_codes" -md             | Traduce solo i file Markdown.
translate -l "language_codes" -nb             | Traduce solo file Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Ritraduce i file con punteggi di confidenza bassi basandosi sui risultati della valutazione precedente.
translate -l "language_codes" -d              | Abilita la modalità debug per un logging dettagliato.
translate -l "language_codes" --save-logs, -s | Salva i log a livello DEBUG nei file sotto <root_dir>/logs/ (la console rimane controllata da -d)
translate -l "language_codes" -r "root_dir"   | Specifica la directory root del progetto
translate -l "language_codes" -f              | Usa la modalità veloce per la traduzione delle immagini (fino a 3x più veloce nel plotting a un leggero costo di qualità e allineamento).
translate -l "language_codes" -y              | Conferma automaticamente tutti i prompt (utile per pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Abilita o disabilita l'aggiunta di una sezione di avviso su traduzione automatica nei markdown e notebook tradotti (default: abilitato).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizza la sezione di avviso delle lingue nel README (sparse checkout) con l’URL del tuo repository.
translate -l "language_codes" --help          | dettagli di aiuto all’interno del CLI mostrando i comandi disponibili
evaluate -l "language_code"                  | Valuta la qualità della traduzione per una lingua specifica e fornisce punteggi di confidenza
evaluate -l "language_code" -c 0.8           | Valuta le traduzioni con una soglia di confidenza personalizzata
evaluate -l "language_code" -f               | Modalità di valutazione veloce (solo basata su regole, senza LLM)
evaluate -l "language_code" -D               | Modalità di valutazione profonda (basata solo su LLM, più accurata ma più lenta)
evaluate -l "language_code" --save-logs, -s  | Salva i log a livello DEBUG nei file sotto <root_dir>/logs/
migrate-links -l "language_codes"             | Rielabora i file Markdown tradotti per aggiornare i link ai notebook (.ipynb). Preferisce i notebook tradotti quando disponibili; altrimenti può ricorrere ai notebook originali.
migrate-links -l "language_codes" -r          | Specifica la directory root del progetto (default: directory corrente).
migrate-links -l "language_codes" --dry-run   | Mostra quali file verrebbero modificati senza scrivere cambiamenti.
migrate-links -l "language_codes" --no-fallback-to-original | Non riscrive i link ai notebook originali quando i corrispettivi tradotti mancano (aggiorna solo se esiste la versione tradotta).
migrate-links -l "language_codes" -d          | Abilita la modalità debug per un logging dettagliato.
migrate-links -l "language_codes" --save-logs, -s | Salva i log a livello DEBUG nei file sotto <root_dir>/logs/
migrate-links -l "all" -y                      | Elabora tutte le lingue e conferma automaticamente il prompt di avviso.

## Usage examples

  1. Comportamento predefinito (aggiunge nuove traduzioni senza eliminare quelle esistenti):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Aggiungi solo nuove traduzioni di immagini coreane (nessuna traduzione esistente viene eliminata):    translate -l "ko" -img

  3. Aggiorna tutte le traduzioni coreane (Attenzione: questo elimina tutte le traduzioni coreane esistenti prima di ritradurre):    translate -l "ko" -u

  4. Aggiorna solo le immagini coreane (Attenzione: questo elimina tutte le immagini coreane esistenti prima di ritradurre):    translate -l "ko" -img -u

  5. Aggiungi nuove traduzioni markdown per il coreano senza influenzare altre traduzioni:    translate -l "ko" -md

  6. Correggi le traduzioni a bassa confidenza basate sui risultati della valutazione precedente: translate -l "ko" --fix

  7. Correggi le traduzioni a bassa confidenza per file specifici solo (markdown): translate -l "ko" --fix -md

  8. Correggi le traduzioni a bassa confidenza per file specifici solo (immagini): translate -l "ko" --fix -img

  9. Usa la modalità veloce per la traduzione delle immagini:    translate -l "ko" -img -f

  10. Correggi le traduzioni a bassa confidenza con soglia personalizzata: translate -l "ko" --fix -c 0.8

  11. Esempio modalità debug: - translate -l "ko" -d: Abilita il logging di debug.
  12. Salva i log nei file: translate -l "ko" -s
  13. DEBUG console e DEBUG file: translate -l "ko" -d -s
  14. Traduce senza aggiungere avvisi di traduzione automatica agli output: translate -l "ko" --no-disclaimer

  15. Migra i link dei notebook per le traduzioni coreane (aggiorna i link ai notebook tradotti quando disponibili):    migrate-links -l "ko"

  15. Migra i link con dry-run (nessuna scrittura su file):    migrate-links -l "ko" --dry-run

  16. Aggiorna solo i link quando esistono i notebook tradotti (non tornare agli originali):    migrate-links -l "ko" --no-fallback-to-original

  17. Elabora tutte le lingue con prompt di conferma:    migrate-links -l "all"

  18. Elabora tutte le lingue e conferma automaticamente:    migrate-links -l "all" -y
  19. Salva i log nei file per migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizza l'avviso lingue nel README con l'URL del tuo repo:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: La funzionalità di valutazione è attualmente in beta. Questa funzionalità è stata rilasciata per valutare i documenti tradotti, e i metodi di valutazione e l'implementazione dettagliata sono ancora in fase di sviluppo e soggetti a modifiche.

  1. Valuta le traduzioni coreane: evaluate -l "ko"

  2. Valuta con soglia di confidenza personalizzata: evaluate -l "ko" -c 0.8

  3. Valutazione veloce (solo basata su regole): evaluate -l "ko" -f

  4. Valutazione approfondita (solo basata su LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di considerare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua natìa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->