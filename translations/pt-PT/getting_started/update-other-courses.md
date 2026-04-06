# Atualizar a secção "Outros Cursos" (repositórios Microsoft Beginners)

Este guia explica como fazer a secção "Outros Cursos" sincronizar automaticamente usando o Co‑op Translator, e como atualizar o template global para todos os repositórios.

- Aplica-se a: apenas repositórios Microsoft Beginners
- Funciona com: Co‑op Translator CLI e GitHub Actions
- Fonte do template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Início rápido: Ativar a sincronização automática no seu repositório

Adicione os seguintes marcadores à volta da secção "Outros Cursos" no seu README. O Co‑op Translator irá substituir tudo entre estes marcadores a cada execução.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co‑op Translator é executado—via CLI (por exemplo, `translate -l "<language codes>"`) ou GitHub Actions—atualiza automaticamente a secção "Outros Cursos" enquadrada por estes marcadores.

> [!NOTE]
> Se já tiver uma lista existente, basta envolvê-la com os mesmos marcadores. A próxima execução irá substituí-la pelo conteúdo padronizado mais recente.

---

## Como alterar o conteúdo global

Se quiser atualizar o conteúdo padronizado que aparece em todos os repositórios Beginners:

1. Edite o template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abra um pull request no repositório Co-op Translator com as suas alterações
3. Após a fusão do PR, a versão do Co‑op Translator será atualizada
4. Da próxima vez que o Co‑op Translator for executado (CLI ou GitHub Action) num repositório alvo, irá sincronizar automaticamente a secção atualizada

Isto garante uma fonte de verdade única para o conteúdo "Outros Cursos" em todos os repositórios Beginners.


## Tamanhos dos Repositórios

Os repositórios podem tornar-se grandes devido ao número de idiomas traduzidos para ajudar os utilizadores finais, fornecendo orientações sobre como usar clone - sparse para clonar apenas os idiomas necessários e não o repositório inteiro

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
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em consideração que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->