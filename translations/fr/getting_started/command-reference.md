# Référence des commandes

L'interface en ligne de commande **Co-op Translator** offre plusieurs options pour personnaliser le processus de traduction :

Commande                                     | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduit votre projet dans les langues spécifiées. Exemple : translate -l "es fr de" traduit en espagnol, français et allemand. Utilisez translate -l "all" pour traduire dans toutes les langues prises en charge.
translate -l "language_codes" -u              | Met à jour les traductions en supprimant les existantes et en les recréant. Avertissement : cela supprimera toutes les traductions actuelles pour les langues spécifiées.
translate -l "language_codes" -img            | Traduit uniquement les fichiers image.
translate -l "language_codes" -md             | Traduit uniquement les fichiers Markdown.
translate -l "language_codes" -nb             | Traduit uniquement les fichiers Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraduit les fichiers avec un faible niveau de confiance basé sur les résultats d'évaluation précédents.
translate -l "language_codes" -d              | Active le mode débogage pour un journal détaillé.
translate -l "language_codes" --save-logs, -s | Enregistre les journaux de niveau DEBUG dans des fichiers sous <root_dir>/logs/ (la console reste contrôlée par -d)
translate -l "language_codes" -r "root_dir"   | Spécifie le répertoire racine du projet
translate -l "language_codes" -f              | Utilise le mode rapide pour la traduction d'images (jusqu'à 3x plus rapide au prix d'une légère perte de qualité et d'alignement).
translate -l "language_codes" -y              | Confirme automatiquement toutes les invites (utile pour les pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Active ou désactive l'ajout d'une section de clause de non-responsabilité de traduction automatique dans les markdowns et notebooks traduits (par défaut : activé).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personnalise la section des langues du README (sparse checkout) avec l'URL de votre dépôt.
translate -l "language_codes" --help          | détails d'aide dans l'interface CLI affichant les commandes disponibles
evaluate -l "language_code"                  | Évalue la qualité de la traduction pour une langue spécifique et fournit des scores de confiance
evaluate -l "language_code" -c 0.8           | Évalue les traductions avec un seuil de confiance personnalisé
evaluate -l "language_code" -f               | Mode d'évaluation rapide (basé sur des règles uniquement, sans LLM)
evaluate -l "language_code" -D               | Mode d'évaluation approfondi (basé sur LLM uniquement, plus complet mais plus lent)
evaluate -l "language_code" --save-logs, -s  | Enregistre les journaux de niveau DEBUG dans des fichiers sous <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocesse les fichiers Markdown traduits afin de mettre à jour les liens vers les notebooks (.ipynb). Prend en préférence les notebooks traduits lorsqu'ils sont disponibles ; sinon, peut revenir aux notebooks originaux.
migrate-links -l "language_codes" -r          | Spécifie le répertoire racine du projet (par défaut : répertoire courant).
migrate-links -l "language_codes" --dry-run   | Montre quels fichiers seraient modifiés sans écrire les modifications.
migrate-links -l "language_codes" --no-fallback-to-original | Ne pas réécrire les liens vers les notebooks originaux quand les équivalents traduits manquent (mettre à jour uniquement si la traduction existe).
migrate-links -l "language_codes" -d          | Active le mode débogage pour un journal détaillé.
migrate-links -l "language_codes" --save-logs, -s | Enregistre les journaux de niveau DEBUG dans des fichiers sous <root_dir>/logs/
migrate-links -l "all" -y                      | Traite toutes les langues et confirme automatiquement l'invite d'avertissement.

## Exemples d'utilisation

  1. Comportement par défaut (ajoute de nouvelles traductions sans supprimer les existantes) :   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Ajouter uniquement de nouvelles traductions d'images en coréen (aucune traduction existante supprimée) :    translate -l "ko" -img

  3. Mettre à jour toutes les traductions coréennes (Attention : cela supprime toutes les traductions coréennes existantes avant de retraduire) :    translate -l "ko" -u

  4. Mettre à jour uniquement les images coréennes (Attention : cela supprime toutes les images coréennes existantes avant de retraduire) :    translate -l "ko" -img -u

  5. Ajouter de nouvelles traductions markdown pour le coréen sans affecter les autres traductions :    translate -l "ko" -md

  6. Corriger les traductions à faible confiance sur la base des résultats d’évaluation précédents : translate -l "ko" --fix

  7. Corriger uniquement les traductions à faible confiance pour certains fichiers (markdown) : translate -l "ko" --fix -md

  8. Corriger uniquement les traductions à faible confiance pour certains fichiers (images) : translate -l "ko" --fix -img

  9. Utiliser le mode rapide pour la traduction d'images :    translate -l "ko" -img -f

  10. Corriger les traductions à faible confiance avec un seuil personnalisé : translate -l "ko" --fix -c 0.8

  11. Exemple de mode débogage : - translate -l "ko" -d : Active le journal de débogage.
  12. Enregistrer les journaux dans des fichiers : translate -l "ko" -s
  13. DEBUG console et DEBUG fichier : translate -l "ko" -d -s
  14. Traduire sans ajouter de clauses de non-responsabilité de traduction automatique aux sorties : translate -l "ko" --no-disclaimer

  15. Migrer les liens de notebooks pour les traductions coréennes (mettre à jour les liens vers les notebooks traduits lorsqu'ils sont disponibles) :    migrate-links -l "ko"

  15. Migration des liens avec dry-run (aucune écriture dans les fichiers) :    migrate-links -l "ko" --dry-run

  16. Mettre à jour uniquement les liens quand les notebooks traduits existent (ne pas revenir aux originaux) :    migrate-links -l "ko" --no-fallback-to-original

  17. Traiter toutes les langues avec invite de confirmation :    migrate-links -l "all"

  18. Traiter toutes les langues et confirmer automatiquement :    migrate-links -l "all" -y
  19. Enregistrer les journaux dans des fichiers pour migrate-links :    migrate-links -l "ko ja" -s

  20. Personnaliser le conseil des langues dans le README avec l'URL de votre dépôt :
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exemples d'évaluation

> [!WARNING]  
> **Fonctionnalité Beta** : La fonctionnalité d'évaluation est actuellement en version bêta. Cette fonctionnalité a été publiée pour évaluer les documents traduits, et les méthodes d'évaluation ainsi que la mise en œuvre détaillée sont encore en développement et susceptibles d'être modifiées.

  1. Évaluer les traductions coréennes : evaluate -l "ko"

  2. Évaluer avec un seuil de confiance personnalisé : evaluate -l "ko" -c 0.8

  3. Évaluation rapide (basée uniquement sur des règles) : evaluate -l "ko" -f

  4. Évaluation approfondie (basée uniquement sur LLM) : evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous efforts pour assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de faire appel à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->