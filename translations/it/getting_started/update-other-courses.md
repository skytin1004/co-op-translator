# Aggiorna la sezione "Altri Corsi" (repository Microsoft Beginners)

Questa guida spiega come fare in modo che la sezione "Altri Corsi" si auto-sincronizzi usando Co-op Translator e come aggiornare il modello globale per tutti i repository.

- Si applica a: solo repository Microsoft Beginners
- Funziona con: Co-op Translator CLI e GitHub Actions
- Fonte del modello: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Avvio rapido: Abilitare l'auto-sincronizzazione nel tuo repository

Aggiungi i seguenti marker intorno alla sezione "Altri Corsi" nel tuo README. Co-op Translator sostituirà tutto ciò che si trova tra questi marker ad ogni esecuzione.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Ogni volta che Co-op Translator viene eseguito — tramite CLI (es. `translate -l "<language codes>"`) o GitHub Actions — aggiorna automaticamente la sezione "Altri Corsi" racchiusa da questi marker.

> [!NOTE]
> Se possiedi già una lista esistente, basta racchiuderla con gli stessi marker. La prossima esecuzione la sostituirà con il contenuto standardizzato più recente.

---

## Come modificare il contenuto globale

Se desideri aggiornare il contenuto standardizzato che appare in tutti i repository Beginners:

1. Modifica il modello: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Apri una pull request al repository Co-op Translator con le tue modifiche
3. Dopo che la PR è stata unita, la versione di Co-op Translator sarà aggiornata
4. La prossima volta che Co-op Translator verrà eseguito (CLI o GitHub Action) in un repository destinatario, sincronizzerà automaticamente la sezione aggiornata

Questo assicura una singola fonte di verità per il contenuto "Altri Corsi" in tutti i repository Beginners.


## Dimensioni dei repository

I repository possono diventare grandi a causa del numero di lingue tradotte per aiutare gli utenti finali, fornendo indicazioni su come usare clone - sparse per clonare solo le lingue necessarie e non l'intero repository

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire accuratezza, si prega di essere consapevoli che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->