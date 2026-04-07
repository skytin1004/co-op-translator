# Actualizar la sección "Otros Cursos" (repositorios Microsoft Beginners)

Esta guía explica cómo hacer que la sección "Otros Cursos" se sincronice automáticamente usando Co-op Translator, y cómo actualizar la plantilla global para todos los repositorios.

- Aplica a: solo repositorios Microsoft Beginners
- Funciona con: Co-op Translator CLI y GitHub Actions
- Fuente de la plantilla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Inicio rápido: Habilitar sincronización automática en tu repositorio

Agrega los siguientes marcadores alrededor de la sección "Otros Cursos" en tu README. Co-op Translator reemplazará todo lo que esté entre estos marcadores en cada ejecución.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que Co-op Translator se ejecute, ya sea por CLI (por ejemplo, `translate -l "<language codes>"`) o GitHub Actions, actualizará automáticamente la sección "Otros Cursos" delimitada por estos marcadores.

> [!NOTE]
> Si ya tienes una lista existente, solo envuélvela con los mismos marcadores. La siguiente ejecución la reemplazará con el contenido estandarizado más reciente.

---

## Cómo cambiar el contenido global

Si quieres actualizar el contenido estandarizado que aparece en todos los repos de Beginners:

1. Edita la plantilla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abre un pull request en el repositorio de Co-op Translator con tus cambios
3. Después de que se fusione el PR, la versión de Co-op Translator se actualizará
4. La próxima vez que Co-op Translator se ejecute (CLI o GitHub Action) en un repositorio objetivo, sincronizará automáticamente la sección actualizada

Esto asegura una única fuente de verdad para el contenido de "Otros Cursos" en todos los repositorios de Beginners.


## Tamaños de los repositorios

Los repos pueden volverse grandes debido a la cantidad de idiomas a los que se traduce para ayudar a los usuarios finales a proporcionar guía sobre cómo usar clone - sparse para clonar solo los idiomas necesarios y no todo el repositorio

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
**Aviso**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->