# Ενημέρωση της ενότητας "Άλλα Μαθήματα" (Microsoft Beginners αποθετήρια)

Αυτός ο οδηγός εξηγεί πώς να κάνετε την ενότητα "Άλλα Μαθήματα" να συγχρονίζεται αυτόματα χρησιμοποιώντας το Co‑op Translator, και πώς να ενημερώσετε το παγκόσμιο πρότυπο για όλα τα αποθετήρια.

- Ισχύει για: μόνο αποθετήρια Microsoft Beginners  
- Λειτουργεί με: Co‑op Translator CLI και GitHub Actions  
- Πηγή προτύπου: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Γρήγορη εκκίνηση: Ενεργοποίηση αυτόματου συγχρονισμού στο αποθετήριό σας

Προσθέστε τους παρακάτω δείκτες γύρω από την ενότητα "Άλλα Μαθήματα" στο README σας. Το Co‑op Translator θα αντικαθιστά όλα όσα βρίσκονται ανάμεσα σε αυτούς τους δείκτες κάθε φορά που εκτελείται.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
Κάθε φορά που το Co‑op Translator εκτελείται—μέσω CLI (π.χ., `translate -l "<language codes>"`) ή GitHub Actions—ενημερώνει αυτόματα την ενότητα "Άλλα Μαθήματα" που περικλείεται από αυτούς τους δείκτες.

> [!NOTE]  
> Αν έχετε ήδη μια λίστα, απλώς περικλείστε την με τους ίδιους δείκτες. Στην επόμενη εκτέλεση θα αντικατασταθεί με το πιο πρόσφατο τυποποιημένο περιεχόμενο.

---

## Πώς να αλλάξετε το παγκόσμιο περιεχόμενο

Αν θέλετε να ενημερώσετε το τυποποιημένο περιεχόμενο που εμφανίζεται σε όλα τα αποθετήρια Beginners:

1. Επεξεργαστείτε το πρότυπο: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. Ανοίξτε ένα pull request στο αποθετήριο Co-op Translator με τις αλλαγές σας  
3. Μετά τη συγχώνευση του PR, η έκδοση του Co‑op Translator θα ενημερωθεί  
4. Την επόμενη φορά που το Co‑op Translator θα εκτελεστεί (CLI ή GitHub Action) σε κάποιο στόχο αποθετήριο, θα συγχρονίσει αυτόματα την ενημερωμένη ενότητα

Αυτό διασφαλίζει μια ενιαία πηγή αλήθειας για το περιεχόμενο "Άλλα Μαθήματα" σε όλα τα αποθετήρια Beginners.

## Μέγεθος Αποθετηρίων

Τα αποθετήρια μπορεί να γίνουν μεγάλα λόγω του αριθμού των μεταφρασμένων γλωσσών, για να βοηθηθούν οι τελικοί χρήστες να καθοδηγηθούν στο πώς να χρησιμοποιήσουν το clone - sparse ώστε να κλωνοποιηθούν μόνο οι απαραίτητες γλώσσες και όχι ολόκληρο το αποθετήριο

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
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις μπορεί να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται ως η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->