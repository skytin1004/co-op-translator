# Mise à jour de la section "Autres cours" (dépôts Microsoft Beginners)

Ce guide explique comment rendre la section "Autres cours" auto‑synchronisée en utilisant Co‑op Translator, et comment mettre à jour le modèle global pour tous les dépôts.

- S'applique à : dépôts Microsoft Beginners uniquement
- Fonctionne avec : Co‑op Translator CLI et GitHub Actions
- Source du modèle : [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Démarrage rapide : activer l'auto‑synchronisation dans votre dépôt

Ajoutez les marqueurs suivants autour de la section "Autres cours" dans votre README. Co‑op Translator remplacera tout ce qui se trouve entre ces marqueurs à chaque exécution.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Chaque fois que Co‑op Translator s’exécute — via CLI (par exemple, `translate -l "<codes de langue>"`) ou GitHub Actions — il met automatiquement à jour la section "Autres cours" encadrée par ces marqueurs.

> [!NOTE]
> Si vous avez une liste existante, il vous suffit de la placer entre les mêmes marqueurs. La prochaine exécution la remplacera par le contenu standardisé le plus récent.

---

## Comment modifier le contenu global

Si vous souhaitez mettre à jour le contenu standardisé qui apparaît dans tous les dépôts Beginners :

1. Modifiez le modèle : [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Ouvrez une pull request vers le dépôt Co-op Translator avec vos modifications
3. Après la fusion de la PR, la version de Co‑op Translator sera mise à jour
4. La prochaine fois que Co‑op Translator s’exécutera (CLI ou GitHub Action) dans un dépôt cible, il synchronisera automatiquement la section mise à jour

Cela garantit une source unique de vérité pour le contenu "Autres cours" dans tous les dépôts Beginners.


## Tailles des dépôts

Les dépôts peuvent devenir volumineux en raison du nombre de langues traduites pour aider les utilisateurs finaux. Cela fournit des indications sur la façon d’utiliser clone - sparse pour ne cloner que les langues nécessaires et non l’ensemble du dépôt.

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
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->