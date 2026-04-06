# Δημιουργήστε το αρχείο *.env* στον ριζικό κατάλογο

Σε αυτό το σεμινάριο, θα σας καθοδηγήσουμε στη ρύθμιση των μεταβλητών περιβάλλοντος για τις υπηρεσίες Azure χρησιμοποιώντας ένα αρχείο *.env*. Οι μεταβλητές περιβάλλοντος σας επιτρέπουν να διαχειρίζεστε με ασφάλεια ευαίσθητα διαπιστευτήρια, όπως κλειδιά API, χωρίς να χρειάζεται να τα ενσωματώνετε σκληρά στον κώδικά σας.

> [!IMPORTANT]
> - Απαιτείται να ρυθμιστεί μόνο μία υπηρεσία μοντέλου γλώσσας (Azure OpenAI ή OpenAI). Συμπληρώστε τις μεταβλητές περιβάλλοντος για την υπηρεσία που προτιμάτε. Εάν έχουν οριστεί μεταβλητές περιβάλλοντος για πολλαπλά μοντέλα γλώσσας, ο συνεργατικός μεταφραστής θα επιλέξει ένα βάσει της προτεραιότητας.
> - Εάν οι μεταβλητές περιβάλλοντος για το Computer Vision δεν έχουν οριστεί, ο μεταφραστής θα μεταβεί αυτόματα σε [λειτουργία μόνο Markdown](./markdown-only-mode.md).

> [!NOTE]
> Ο συγκεκριμένος οδηγός εστιάζει κυρίως στις υπηρεσίες Azure, αλλά μπορείτε να επιλέξετε οποιοδήποτε υποστηριζόμενο μοντέλο γλώσσας από τη [λίστα υποστηριζόμενων μοντέλων και υπηρεσιών](../README.md#-supported-models-and-services).

## Δημιουργία αρχείου *.env*

Στον ριζικό κατάλογο του έργου σας, δημιουργήστε ένα αρχείο με όνομα *.env*. Αυτό το αρχείο θα αποθηκεύει όλες τις μεταβλητές περιβάλλοντος σε απλή μορφή.

> [!WARNING]
> Μην δεσμεύετε το αρχείο *.env* σε συστήματα ελέγχου έκδοσης όπως το Git. Προσθέστε το *.env* στο αρχείο .gitignore για να αποτρέψετε τυχαίες δεσμεύσεις.

1. Μεταβείτε στον ριζικό κατάλογο του έργου σας.

1. Δημιουργήστε ένα αρχείο *.env* στον ριζικό κατάλογο του έργου σας.

1. Ανοίξτε το αρχείο *.env* και επικολλήστε το παρακάτω πρότυπο:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> Εάν θέλετε να βρείτε τα κλειδιά API και τα endpoints σας, μπορείτε να ανατρέξετε στο [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του είναι η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από ανθρώπινο μεταφραστή. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->