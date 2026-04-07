# 🌐 Υποστήριξη Πολλών Γλωσσών (Πρότυπο)

Υπεύθυνοι συντήρησης: Το παρακάτω μπλοκ είναι ένα παράδειγμα "όλων των γλωσσών" το οποίο διαχειρίζεται το Co-op Translator.

- Εάν θέλετε το Co-op Translator να κρατά αυτόν τον κατάλογο εντελώς ενημερωμένο αυτόματα όταν εκτελείτε `translate` (οποιαδήποτε επιλογή γλώσσας), κρατήστε τους δύο σχολιασμούς όπως είναι.
- Εάν θέλετε να εμφανίσετε μόνο ένα υποσύνολο γλωσσών, διαγράψτε τους δύο σχολιασμούς και αφαιρέστε τις γλώσσες που δεν θέλετε να καταχωρίσετε. Αφού αφαιρέσετε τους σχολιασμούς, το Co-op Translator δεν θα αντικαθιστά πλέον αυτό το τμήμα αυτόματα.

- Η ενότητα περιλαμβάνει πλέον μια συμβουλή "Προτιμάτε να Κλωνοποιήσετε Τοπικά;" για να βοηθήσει τους χρήστες να κλωνοποιήσουν χωρίς το μεγάλο φόρτο των μεταφράσεων. Μπορείτε να εξατομικεύσετε τη συμβουλή με το URL του αποθετηρίου σας εκτελώντας, για παράδειγμα:
  - `translate -l "ko" --repo-url "https://github.com/org/repo.git"`

```markdown

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](./README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρά τις προσπάθειές μας για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->