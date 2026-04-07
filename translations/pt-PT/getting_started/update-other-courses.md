# Atualizar a secção "Outros Cursos" (repositórios Microsoft Beginners)

Este guia explica como fazer a secção "Outros Cursos" auto-sincronizar-se usando o Co-op Translator, e como atualizar o modelo global para todos os repositórios.

- Aplica-se a: apenas repositórios Microsoft Beginners
- Funciona com: Co-op Translator CLI e GitHub Actions
- Fonte do modelo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Início rápido: Ativar auto-sincronização no seu repositório

Adicione os seguintes marcadores em torno da secção "Outros Cursos" no seu README. O Co-op Translator substituirá tudo entre estes marcadores em cada execução.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que o Co-op Translator é executado — via CLI (ex.: `translate -l "<códigos de línguas>"`) ou GitHub Actions — atualiza automaticamente a secção "Outros Cursos" delimitada por estes marcadores.

> [!NOTE]
> Se já tiver uma lista existente, basta envolvê-la com os mesmos marcadores. A próxima execução irá substituí-la pelo conteúdo padronizado mais recente.

---

## Como alterar o conteúdo global

Se quiser atualizar o conteúdo padronizado que aparece em todos os repositórios Beginners:

1. Edite o modelo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abra um pull request para o repositório do Co-op Translator com as suas alterações
3. Após o PR ser aceite, a versão do Co-op Translator será atualizada
4. Na próxima vez que o Co-op Translator for executado (CLI ou GitHub Action) num repositório alvo, irá sincronizar automaticamente a secção atualizada

Isto assegura uma única fonte de verdade para o conteúdo "Outros Cursos" em todos os repositórios Beginners.


## Tamanho dos Repositórios

Os repositórios podem tornar-se grandes devido ao número de línguas para as quais são traduzidos, para ajudar os utilizadores finais, fornecendo orientação sobre como usar clone - sparse para clonar apenas as línguas necessárias e não o repositório inteiro

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
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->