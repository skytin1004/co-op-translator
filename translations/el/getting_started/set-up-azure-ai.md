# Ρύθμιση του Azure AI για το Co-op Translator (Azure OpneAI & Azure AI Vision)

Αυτός ο οδηγός σας καθοδηγεί στη ρύθμιση του Azure OpenAI για μετάφραση γλωσσών και του Azure Computer Vision για ανάλυση περιεχομένου εικόνων (το οποίο μπορεί να χρησιμοποιηθεί για μετάφραση βασισμένη σε εικόνες) εντός του Azure AI Foundry.

**Προαπαιτούμενα:**
- Ένας λογαριασμός Azure με ενεργή συνδρομή.
- Επαρκή δικαιώματα για τη δημιουργία πόρων και αναπτύξεων στη συνδρομή Azure σας.

## Δημιουργία ενός Azure AI Project

Ξεκινάτε δημιουργώντας ένα Azure AI Project, που λειτουργεί ως κεντρικός χώρος για τη διαχείριση των πόρων AI σας.

1. Μεταβείτε στο [https://ai.azure.com](https://ai.azure.com) και συνδεθείτε με τον λογαριασμό Azure σας.

1. Επιλέξτε **+Create** για να δημιουργήσετε ένα νέο έργο.

1. Εκτελέστε τις ακόλουθες ενέργειες:
   - Εισάγετε ένα **Όνομα έργου** (π.χ., `CoopTranslator-Project`).
   - Επιλέξτε το **AI hub** (π.χ., `CoopTranslator-Hub`) (Δημιουργήστε ένα νέο αν χρειάζεται).

1. Κάντε κλικ στο "**Review and Create**" για να ρυθμίσετε το έργο σας. Θα μεταβείτε στη σελίδα επισκόπησης του έργου σας.

## Ρύθμιση Azure OpenAI για μετάφραση γλώσσας

Μέσα στο έργο σας, θα αναπτύξετε ένα μοντέλο Azure OpenAI που θα λειτουργεί ως το backend για μετάφραση κειμένου.

### Πλοήγηση στο έργο σας

Εάν δεν βρίσκεστε ήδη εκεί, ανοίξτε το νεοδημιουργημένο έργο σας (π.χ., `CoopTranslator-Project`) στο Azure AI Foundry.

### Ανάπτυξη ενός μοντέλου OpenAI

1. Από το αριστερό μενού του έργου σας, κάτω από "My assets", επιλέξτε "**Models + endpoints**".

1. Επιλέξτε **+ Deploy model**.

1. Επιλέξτε **Deploy Base Model**.

1. Θα σας παρουσιαστεί μια λίστα διαθέσιμων μοντέλων. Φιλτράρετε ή αναζητήστε ένα κατάλληλο μοντέλο GPT. Συνιστούμε το `gpt-4o`.

1. Επιλέξτε το επιθυμητό μοντέλο και κάντε κλικ στο **Confirm**.

1. Επιλέξτε **Deploy**.

### Διαμόρφωση Azure OpenAI

Μόλις αναπτυχθεί, μπορείτε να επιλέξετε την ανάπτυξη από τη σελίδα "**Models + endpoints**" για να βρείτε το **REST endpoint URL**, **Key**, **Όνομα ανάπτυξης**, **Όνομα μοντέλου** και **Έκδοση API**. Αυτά θα χρειαστούν για την ενσωμάτωση του μοντέλου μετάφρασης στην εφαρμογή σας.

> [!NOTE]
> Μπορείτε να επιλέξετε εκδόσεις API από τη σελίδα [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) με βάση τις απαιτήσεις σας. Να γνωρίζετε ότι η **Έκδοση API** διαφέρει από την **Έκδοση μοντέλου** που εμφανίζεται στη σελίδα **Models + endpoints** στο Azure AI Foundry.

## Ρύθμιση Azure Computer Vision για μετάφραση εικόνων

Για να ενεργοποιήσετε τη μετάφραση κειμένου μέσα σε εικόνες, χρειάζεται να βρείτε το API Key και το Endpoint της υπηρεσίας Azure AI.

1. Μεταβείτε στο Azure AI Project σας (π.χ., `CoopTranslator-Project`). Βεβαιωθείτε ότι βρίσκεστε στη σελίδα επισκόπησης του έργου.

### Διαμόρφωση Azure AI Service

Βρείτε το API Key και το Endpoint από την υπηρεσία Azure AI Service.

1. Μεταβείτε στο Azure AI Project σας (π.χ., `CoopTranslator-Project`). Βεβαιωθείτε ότι βρίσκεστε στη σελίδα επισκόπησης του έργου.

1. Βρείτε το **API Key** και το **Endpoint** από την καρτέλα Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Αυτή η σύνδεση καθιστά τις δυνατότητες του συνδεδεμένου πόρου Azure AI Services (συμπεριλαμβανομένης της ανάλυσης εικόνας) διαθέσιμες στο έργο AI Foundry σας. Μπορείτε στη συνέχεια να χρησιμοποιήσετε αυτή τη σύνδεση στα notebooks ή τις εφαρμογές σας για εξαγωγή κειμένου από εικόνες, το οποίο στη συνέχεια μπορεί να αποσταλεί στο μοντέλο Azure OpenAI για μετάφραση.

## Συγκέντρωση των Διαπιστευτηρίων σας

Μέχρι τώρα, θα πρέπει να έχετε συλλέξει τα εξής:

**Για Azure OpenAI (Μετάφραση κειμένου):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Όνομα μοντέλου Azure OpenAI (π.χ., `gpt-4o`)
- Όνομα ανάπτυξης Azure OpenAI (π.χ., `cooptranslator-gpt4o`)
- Έκδοση Azure OpenAI API

**Για τις Υπηρεσίες Azure AI (Εξαγωγή κειμένου εικόνας μέσω Vision):**
- Endpoint Azure AI Service
- Azure AI Service API Key

### Παράδειγμα: Διαμόρφωση μεταβλητών περιβάλλοντος (Προεπισκόπηση)

Αργότερα, όταν δημιουργείτε την εφαρμογή σας, πιθανώς θα τη διαμορφώσετε χρησιμοποιώντας αυτά τα συλλεγμένα διαπιστευτήρια. Για παράδειγμα, μπορεί να τα ορίσετε ως μεταβλητές περιβάλλοντος ως εξής:

```bash
# Διαπιστευτήρια υπηρεσίας Azure AI (Απαραίτητα για μετάφραση εικόνας)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # π.χ., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Προαιρετικά σύνολα εφεδρείας: διπλασιάστε τις μεταβλητές με κατάληξη _1/_2 (ίδιος δείκτης για όλες τις μεταβλητές στο σύνολο)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Διαπιστευτήρια Azure OpenAI (Απαραίτητα για μετάφραση κειμένου)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # π.χ., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # π.χ., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # π.χ., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # π.χ., 2024-12-01-preview

# Προαιρετικά σύνολα εφεδρείας: διπλασιάστε ολόκληρο το σύνολο AZURE_OPENAI_* με κατάληξη _1/_2 (ίδιος δείκτης για όλες τις μεταβλητές)
```

---

### Επιπλέον Ανάγνωση

- [Πώς να δημιουργήσετε ένα έργο στο Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Πώς να δημιουργήσετε πόρους Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Πώς να αναπτύξετε μοντέλα OpenAI στο Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις μπορεί να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε καμία ευθύνη για τυχόν παρεξηγήσεις ή παρανοήσεις που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->