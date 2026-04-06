# Atualize a seção "Outros Cursos" (repositórios Microsoft Beginners)

Este guia explica como fazer a seção "Outros Cursos" sincronizar automaticamente usando o Co‑op Translator, e como atualizar o template global para todos os repositórios.

- Aplica-se a: repositórios Microsoft Beginners somente
- Funciona com: Co‑op Translator CLI e GitHub Actions
- Fonte do template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Início rápido: Ative a sincronização automática em seu repositório

Adicione os seguintes marcadores ao redor da seção "Outros Cursos" no seu README. O Co‑op Translator substituirá tudo entre esses marcadores a cada execução.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co‑op Translator é executado — via CLI (por exemplo, `translate -l "<language codes>"`) ou GitHub Actions — ele atualiza automaticamente a seção "Outros Cursos" envolvida por esses marcadores.

> [!NOTE]
> Se você já possui uma lista existente, basta envolvê-la com os mesmos marcadores. Na próxima execução, ela será substituída pelo conteúdo padronizado mais recente.

---

## Como alterar o conteúdo global

Se você deseja atualizar o conteúdo padronizado que aparece em todos os repositórios Beginners:

1. Edite o template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abra um pull request para o repositório Co-op Translator com suas alterações
3. Após o PR ser mesclado, a versão do Co‑op Translator será atualizada
4. Na próxima vez que o Co‑op Translator for executado (CLI ou GitHub Action) em um repositório alvo, ele sincronizará automaticamente a seção atualizada

Isso garante uma única fonte de verdade para o conteúdo "Outros Cursos" em todos os repositórios Beginners.

## Tamanhos dos repositórios

Os repositórios podem ficar grandes devido à quantidade de idiomas traduzidos para ajudar os usuários finais, fornecendo orientações sobre como usar clone - sparse para clonar somente os idiomas necessários e não o repositório inteiro

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
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos empenhemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->