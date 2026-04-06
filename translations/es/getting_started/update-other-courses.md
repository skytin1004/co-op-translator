# Actualizar la sección "Otros cursos" (repositorios de Microsoft Beginners)

Esta guía explica cómo hacer que la sección "Otros cursos" se sincronice automáticamente usando Co‑op Translator, y cómo actualizar la plantilla global para todos los repositorios.

- Aplica a: Solo repositorios de Microsoft Beginners
- Funciona con: Co‑op Translator CLI y GitHub Actions
- Fuente de la plantilla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Inicio rápido: Habilitar la sincronización automática en tu repositorio

Agrega los siguientes marcadores alrededor de la sección "Otros cursos" en tu README. Co‑op Translator reemplazará todo lo que esté entre estos marcadores en cada ejecución.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que Co‑op Translator se ejecuta—ya sea por CLI (p. ej., `translate -l "<language codes>"`) o GitHub Actions—actualiza automáticamente la sección "Otros cursos" envuelta por estos marcadores.

> [!NOTE]
> Si ya tienes una lista existente, solo envuélvela con los mismos marcadores. La próxima ejecución la reemplazará con el contenido estandarizado más reciente.

---

## Cómo cambiar el contenido global

Si quieres actualizar el contenido estandarizado que aparece en todos los repositorios Beginners:

1. Edita la plantilla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abre un pull request en el repositorio de Co-op Translator con tus cambios
3. Después de que se fusione el PR, se actualizará la versión de Co‑op Translator
4. La próxima vez que Co‑op Translator se ejecute (CLI o GitHub Action) en un repositorio objetivo, sincronizará automáticamente la sección actualizada

Esto asegura una única fuente de verdad para el contenido de "Otros cursos" en todos los repositorios Beginners.


## Tamaños de los repositorios

Los repositorios pueden crecer mucho debido a la cantidad de idiomas a los que se traduce para ayudar a los usuarios finales. Proporciona una guía sobre cómo usar clone - sparse para clonar solo los idiomas necesarios y no el repositorio completo

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
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->