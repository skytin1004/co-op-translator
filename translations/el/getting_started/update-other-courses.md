# Ενημέρωση της ενότητας "Άλλα Μαθήματα" (Microsoft Beginners αποθετήρια)

Αυτός ο οδηγός εξηγεί πώς να κάνετε την ενότητα "Άλλα Μαθήματα" να συγχρονίζεται αυτόματα χρησιμοποιώντας το Co‑op Translator, και πώς να ενημερώσετε το παγκόσμιο πρότυπο για όλα τα αποθετήρια.

- Ισχύει για: Μόνο αποθετήρια Microsoft Beginners
- Λειτουργεί με: Co‑op Translator CLI και GitHub Actions
- Πηγή προτύπου: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Γρήγορη εκκίνηση: Ενεργοποίηση αυτόματου συγχρονισμού στο αποθετήριό σας

Προσθέστε τους ακόλουθους δείκτες γύρω από την ενότητα "Άλλα Μαθήματα" στο README σας. Το Co‑op Translator θα αντικαθιστά όλα τα στοιχεία μεταξύ αυτών των δεικτών σε κάθε εκτέλεση.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Κάθε φορά που εκτελείται το Co‑op Translator—μέσω CLI (π.χ., `translate -l "<language codes>"`) ή GitHub Actions—ενημερώνει αυτόματα την ενότητα "Άλλα Μαθήματα" που περικλείεται από αυτούς τους δείκτες.

> [!NOTE]
> Εάν έχετε ήδη μια λίστα, απλώς τυλίξτε την με τους ίδιους δείκτες. Η επόμενη εκτέλεση θα την αντικαταστήσει με το πιο πρόσφατο τυποποιημένο περιεχόμενο.

---

## Πώς να αλλάξετε το παγκόσμιο περιεχόμενο

Εάν θέλετε να ενημερώσετε το τυποποιημένο περιεχόμενο που εμφανίζεται σε όλα τα Beginners αποθετήρια:

1. Επεξεργαστείτε το πρότυπο: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Ανοίξτε ένα pull request στο αποθετήριο Co-op Translator με τις αλλαγές σας
3. Αφού συγχωνευτεί το PR, η έκδοση του Co‑op Translator θα ενημερωθεί
4. Την επόμενη φορά που θα εκτελεστεί το Co‑op Translator (CLI ή GitHub Action) σε ένα αποθετήριο-στόχο, θα συγχρονίσει αυτόματα την ενημερωμένη ενότητα

Αυτό εξασφαλίζει μια μοναδική πηγή αλήθειας για το περιεχόμενο "Άλλα Μαθήματα" σε όλα τα αποθετήρια Beginners.


## Μέγεθος Αποθετηρίων

Τα αποθετήρια μπορούν να γίνουν μεγάλα λόγω του αριθμού των γλωσσών στις οποίες έχει γίνει η μετάφραση για να βοηθήσουν τους τελικούς χρήστες παρέχοντας καθοδήγηση για το πώς να χρησιμοποιούν το clone - sparse ώστε να κλωνοποιούν μόνο τις απαραίτητες γλώσσες και όχι ολόκληρο το αποθετήριο

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
**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->