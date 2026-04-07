# Co-op Translator

_Αυτοματοποιήστε εύκολα και διατηρήστε τις μεταφράσεις για το εκπαιδευτικό περιεχόμενο GitHub σας σε πολλές γλώσσες καθώς εξελίσσεται το έργο σας._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Υποστήριξη Πολλαπλών Γλωσσών

#### Υποστηρίζεται από το [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](./README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Προτιμάτε να κλωνοποιήσετε τοπικά;**
>
> Αυτό το αποθετήριο περιλαμβάνει πάνω από 50 γλωσσικές μεταφράσεις που αυξάνουν σημαντικά το μέγεθος λήψης. Για κλωνοποίηση χωρίς τις μεταφράσεις, χρησιμοποιήστε sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Αυτό σας προσφέρει όλα όσα χρειάζεστε για να ολοκληρώσετε το μάθημα με πολύ ταχύτερη λήψη.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Επισκόπηση

**Co-op Translator** σας βοηθά να τοπικοποιήσετε το εκπαιδευτικό περιεχόμενο GitHub σε πολλές γλώσσες με ευκολία.  
Όταν ενημερώνετε τα αρχεία Markdown, τις εικόνες ή τα notebooks σας, οι μεταφράσεις παραμένουν αυτόματα συγχρονισμένες, διασφαλίζοντας ότι το περιεχόμενό σας παραμένει ακριβές και ενημερωμένο για μαθητές σε όλο τον κόσμο.

Παράδειγμα του πώς οργανώνεται το μεταφρασμένο περιεχόμενο:

![Example](../../imgs/translation-ex.png)

## Πώς διαχειρίζεται η κατάσταση της μετάφρασης

Το Co-op Translator διαχειρίζεται το μεταφρασμένο περιεχόμενο ως **εκδόσιμα λογισμικά άλλα αντικείμενα**,   
όχι ως στατικά αρχεία.

Το εργαλείο παρακολουθεί την κατάσταση των μεταφρασμένων Markdown, εικόνων και notebooks  
χρησιμοποιώντας **μεταδεδομένα εστιασμένα στη γλώσσα**.

Αυτή η σχεδίαση επιτρέπει στο Co-op Translator να:

- Εντοπίζει αξιόπιστα τις ξεπερασμένες μεταφράσεις  
- Αντιμετωπίζει ομοιόμορφα τα Markdown, τις εικόνες και τα notebooks  
- Κλιμακώνεται με ασφάλεια σε μεγάλα, γρήγορα κινούμενα, πολυγλωσσικά αποθετήρια  

Με το να μοντελοποιεί τις μεταφράσεις ως διαχειριζόμενα αντικείμενα,  
οι ροές εργασίας μετάφρασης ευθυγραμμίζονται φυσικά με τις σύγχρονες  
πρακτικές διαχείρισης εξαρτήσεων και αντικειμένων λογισμικού.

→ [Πώς διαχειρίζεται η κατάσταση της μετάφρασης](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Γρήγορη εκκίνηση

```bash
# Δημιουργήστε και ενεργοποιήστε ένα εικονικό περιβάλλον (συνιστάται)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Εγκαταστήστε το πακέτο
pip install co-op-translator
# Μεταφράστε
translate -l "ko ja fr" -md
```

Docker:

```bash
# Κατεβάστε το δημόσιο εικόνα από το GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Εκτέλεση με τρέχον φάκελο συνδεδεμένο και παρεχόμενο .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Ελάχιστη ρύθμιση

1. Βεβαιωθείτε ότι έχετε μια υποστηριζόμενη έκδοση Python (επί του παρόντος 3.10-3.12). Στο poetry (pyproject.toml) αυτό χειρίζεται αυτόματα.
2. Δημιουργήστε ένα αρχείο `.env` χρησιμοποιώντας το πρότυπο: [.env.template](../../.env.template)
3. Διαμορφώστε έναν πάροχο LLM (Azure OpenAI ή OpenAI)
4. (Προαιρετικά) Για μετάφραση εικόνων (`-img`), διαμορφώστε το Azure AI Vision
5. (Προαιρετικά) Μπορείτε να διαμορφώσετε πολλαπλά σετ διαπιστευτηρίων αντιγράφοντας μεταβλητές με κατάληξη όπως `_1`, `_2`, κλπ. Όλες οι μεταβλητές σε ένα σετ πρέπει να έχουν την ίδια κατάληξη.
6. (Συνιστάται) Καθαρίστε τυχόν προηγούμενες μεταφράσεις για να αποφύγετε συγκρούσεις (π.χ., `translations/`)
7. (Συνιστάται) Προσθέστε μια ενότητα μετάφρασης στο README σας χρησιμοποιώντας το [README languages template](./getting_started/README_languages_template.md)
8. Δείτε: [Ρύθμιση Azure AI](./getting_started/set-up-azure-ai.md)

## Χρήση

Μεταφράστε όλους τους υποστηριζόμενους τύπους:

```bash
translate -l "ko ja"
```

Μόνο Markdown:

```bash
translate -l "de" -md
```

Markdown + εικόνες:

```bash
translate -l "pt" -md -img
```

Μόνο notebooks:

```bash
translate -l "zh" -nb
```

Περισσότερες επιλογές: [Αναφορά εντολών](./getting_started/command-reference.md)

## Χαρακτηριστικά

- Αυτόματη μετάφραση για Markdown, notebooks και εικόνες  
- Διατηρεί τις μεταφράσεις συγχρονισμένες με τις αλλαγές στην πηγή  
- Λειτουργεί τοπικά (CLI) ή σε CI (GitHub Actions)  
- Χρησιμοποιεί Azure OpenAI ή OpenAI· προαιρετικά Azure AI Vision για εικόνες  
- Διατηρεί τη μορφοποίηση και τη δομή του Markdown  

## Τεκμηρίωση

- [Οδηγός γραμμής εντολών](./getting_started/command-line-guide/command-line-guide.md)
- [Οδηγός GitHub Actions (Δημόσια αποθετήρια & τυπικά μυστικά)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Οδηγός GitHub Actions (Αποθετήρια οργανισμού Microsoft & ρυθμίσεις σε επίπεδο οργανισμού)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Πρότυπο γλωσσών README](./getting_started/README_languages_template.md)
- [Υποστηριζόμενες γλώσσες](./getting_started/supported-languages.md)
- [Συνεισφορά](./CONTRIBUTING.md)
- [Αντιμετώπιση προβλημάτων](./getting_started/troubleshooting.md)

### Οδηγός ειδικά για τη Microsoft
> [!NOTE]
> Για τους διαχειριστές των αποθετηρίων “Για Αρχάριους” της Microsoft μόνο.

- [Ενημέρωση της λίστας “άλλα μαθήματα” (μόνο για αποθετήρια MS Beginners)](./getting_started/update-other-courses.md)

## Υποστηρίξτε μας και προάγετε την παγκόσμια μάθηση

Ελάτε μαζί μας να φέρουμε επανάσταση στον τρόπο που κοινοποιείται το εκπαιδευτικό περιεχόμενο παγκοσμίως! Δώστε ⭐ στο [Co-op Translator](https://github.com/azure/co-op-translator) στο GitHub και υποστηρίξτε την αποστολή μας να ξεπεράσουμε τα γλωσσικά εμπόδια στη μάθηση και την τεχνολογία. Το ενδιαφέρον και οι συνεισφορές σας έχουν μεγάλη σημασία! Κώδικας συνεισφοράς και προτάσεις λειτουργιών είναι πάντα ευπρόσδεκτες.

### Εξερευνήστε εκπαιδευτικό περιεχόμενο της Microsoft στη γλώσσα σας

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video παρουσιάσεις

👉 Κάντε κλικ στην εικόνα παρακάτω για να δείτε στο YouTube.

- **Open at Microsoft**: Μια σύντομη 18λεπτη εισαγωγή και γρήγορος οδηγός για τη χρήση του Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Συνεισφορά

Αυτό το έργο καλωσορίζει συνεισφορές και προτάσεις. Ενδιαφέρεστε να συνεισφέρετε στο Azure Co-op Translator; Παρακαλούμε δείτε το [CONTRIBUTING.md](./CONTRIBUTING.md) για οδηγίες σχετικά με το πώς μπορείτε να βοηθήσετε ώστε το Co-op Translator να γίνει πιο προσβάσιμο.

## Συνεισφέροντες
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Κώδικας Συμπεριφοράς

Αυτό το έργο έχει υιοθετήσει τον [Κώδικα Συμπεριφοράς Ανοιχτού Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/).
Για περισσότερες πληροφορίες δείτε τις [Συχνές Ερωτήσεις για τον Κώδικα Συμπεριφοράς](https://opensource.microsoft.com/codeofconduct/faq/) ή επικοινωνήστε με [opencode@microsoft.com](mailto:opencode@microsoft.com) για επιπλέον ερωτήσεις ή σχόλια.

## Υπεύθυνη Τεχνητή Νοημοσύνη

Η Microsoft δεσμεύεται να βοηθά τους πελάτες της να χρησιμοποιούν τα προϊόντα AI υπεύθυνα, να μοιράζεται τα διδάγματά της και να χτίζει συνεργασίες εμπιστοσύνης μέσω εργαλείων όπως οι Σημειώσεις Διαφάνειας και οι Αξιολογήσεις Επιπτώσεων. Πολλοί από αυτούς τους πόρους βρίσκονται στη διεύθυνση [https://aka.ms/RAI](https://aka.ms/RAI).
Η προσέγγιση της Microsoft για την υπεύθυνη AI βασίζεται στις αρχές μας για την AI: δικαιοσύνη, αξιοπιστία και ασφάλεια, ιδιωτικότητα και ασφάλεια, συμπερίληψη, διαφάνεια και υπευθυνότητα.

Τα μεγάλης κλίμακας μοντέλα φυσικής γλώσσας, εικόνας και ομιλίας - όπως αυτά που χρησιμοποιούνται σε αυτό το δείγμα - μπορούν δυνητικά να εμφανίσουν συμπεριφορές που είναι άδικες, αναξιόπιστες ή προσβλητικές, προκαλώντας ζημιές. Παρακαλώ συμβουλευτείτε το [Σημείωμα Διαφάνειας της υπηρεσίας Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) για να ενημερωθείτε σχετικά με κινδύνους και περιορισμούς.

Η συνιστώμενη προσέγγιση για την αντιμετώπιση αυτών των κινδύνων είναι να συμπεριλάβετε ένα σύστημα ασφαλείας στην αρχιτεκτονική σας που μπορεί να ανιχνεύει και να αποτρέπει επιβλαβείς συμπεριφορές. Το [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) παρέχει μια ανεξάρτητη στρώση προστασίας, ικανή να ανιχνεύει επιβλαβές περιεχόμενο που δημιουργείται από χρήστες και AI σε εφαρμογές και υπηρεσίες. Το Azure AI Content Safety περιλαμβάνει text και image APIs που σας επιτρέπουν να ανιχνεύσετε επιβλαβές υλικό. Διαθέτουμε επίσης ένα διαδραστικό Content Safety Studio που σας επιτρέπει να δείτε, να εξερευνήσετε και να δοκιμάσετε κώδικα δείγματος για την ανίχνευση επιβλαβούς περιεχομένου σε διαφορετικά μέσα. Η ακόλουθη [τεκμηρίωση γρήγορης εκκίνησης](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) σας καθοδηγεί στη δημιουργία αιτημάτων προς την υπηρεσία.

Ένας ακόμη παράγοντας που πρέπει να λάβετε υπόψη είναι η συνολική απόδοση της εφαρμογής. Σε εφαρμογές πολλαπλών μέσων και πολλαπλών μοντέλων, θεωρούμε την απόδοση ως το γεγονός ότι το σύστημα λειτουργεί όπως αναμένετε εσείς και οι χρήστες σας, συμπεριλαμβανομένου του να μην παράγει επιβλαβή αποτελέσματα. Είναι σημαντικό να αξιολογήσετε την απόδοση της συνολικής εφαρμογής σας χρησιμοποιώντας [μετρικές ποιότητας παραγωγής και κινδύνου και ασφάλειας](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Μπορείτε να αξιολογήσετε την AI εφαρμογή σας στο περιβάλλον ανάπτυξης χρησιμοποιώντας το [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Δίνοντας είτε ένα δοκιμαστικό σύνολο δεδομένων είτε έναν στόχο, οι γεννήσεις της δημιουργικής σας AI εφαρμογής μετρούνται ποσοτικά με ενσωματωμένους αξιολογητές ή προσαρμοσμένους αξιολογητές της επιλογής σας. Για να ξεκινήσετε με το prompt flow sdk για την αξιολόγηση του συστήματός σας, μπορείτε να ακολουθήσετε τον [οδηγό γρήγορης εκκίνησης](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Αφού εκτελέσετε μια αξιολόγηση, μπορείτε να [οπτικοποιήσετε τα αποτελέσματα στο Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Εμπορικά Σήματα

Αυτό το έργο μπορεί να περιέχει εμπορικά σήματα ή λογότυπα για έργα, προϊόντα ή υπηρεσίες. Η εξουσιοδοτημένη χρήση
εμπορικών σημάτων ή λογοτύπων της Microsoft υπόκειται και πρέπει να ακολουθεί τις
[Οδηγίες Χρήσης Εμπορικών Σημάτων & Brand της Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Η χρήση εμπορικών σημάτων ή λογοτύπων της Microsoft σε τροποποιημένες εκδόσεις αυτού του έργου δεν πρέπει να προκαλεί σύγχυση ή να υπονοεί χορηγία από τη Microsoft.
Οποιαδήποτε χρήση εμπορικών σημάτων ή λογοτύπων τρίτων υπόκειται στις πολιτικές των τρίτων αυτών.

## Λήψη Βοήθειας

Εάν κολλήσετε ή έχετε οποιεσδήποτε ερωτήσεις σχετικά με την κατασκευή εφαρμογών AI, συμμετάσχετε:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Εάν έχετε σχόλια προϊόντος ή σφάλματα κατά την ανάπτυξη επισκεφτείτε:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->