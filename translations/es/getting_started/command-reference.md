# Referencia de comandos

La CLI de **Co-op Translator** ofrece varias opciones para personalizar el proceso de traducción:

Comando                                       | Descripción
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce tu proyecto a los idiomas especificados. Ejemplo: translate -l "es fr de" traduce al español, francés y alemán. Usa translate -l "all" para traducir a todos los idiomas soportados.
translate -l "language_codes" -u              | Actualiza las traducciones eliminando las existentes y recreándolas. Advertencia: Esto eliminará todas las traducciones actuales para los idiomas especificados.
translate -l "language_codes" -img            | Traduce solo archivos de imagen.
translate -l "language_codes" -md             | Traduce solo archivos Markdown.
translate -l "language_codes" -nb             | Traduce solo archivos de Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraduce archivos con puntuaciones de confianza bajas según resultados de evaluaciones previas.
translate -l "language_codes" -d              | Activa el modo debug para registro detallado.
translate -l "language_codes" --save-logs, -s | Guarda en archivos los registros a nivel DEBUG bajo <root_dir>/logs/ (la consola sigue controlada por -d)
translate -l "language_codes" -r "root_dir"   | Especifica el directorio raíz del proyecto
translate -l "language_codes" -f              | Usa modo rápido para la traducción de imágenes (hasta 3x más rápido con un ligero costo en calidad y alineación).
translate -l "language_codes" -y              | Confirma automáticamente todos los avisos (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Habilita o deshabilita la adición de una sección de aviso de traducción automática en markdown y notebooks traducidos (por defecto: habilitado).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliza el aviso de la sección de idiomas del README (sparse checkout) con la URL de tu repositorio.
translate -l "language_codes" --help          | muestra detalles de ayuda dentro de la CLI con los comandos disponibles
evaluate -l "language_code"                  | Evalúa la calidad de la traducción para un idioma específico y proporciona puntuaciones de confianza
evaluate -l "language_code" -c 0.8           | Evalúa traducciones con umbral de confianza personalizado
evaluate -l "language_code" -f               | Modo de evaluación rápida (solo basado en reglas, sin LLM)
evaluate -l "language_code" -D               | Modo de evaluación profunda (solo basado en LLM, más exhaustivo pero más lento)
evaluate -l "language_code" --save-logs, -s  | Guarda en archivos los registros a nivel DEBUG bajo <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocesa archivos Markdown traducidos para actualizar enlaces a notebooks (.ipynb). Prefiere notebooks traducidos cuando están disponibles; de lo contrario puede usar notebooks originales.
migrate-links -l "language_codes" -r          | Especifica el directorio raíz del proyecto (por defecto: directorio actual).
migrate-links -l "language_codes" --dry-run   | Muestra qué archivos cambiarían sin escribir cambios.
migrate-links -l "language_codes" --no-fallback-to-original | No reescribe enlaces a notebooks originales cuando faltan equivalentes traducidos (solo actualiza si existe la traducción).
migrate-links -l "language_codes" -d          | Activa modo debug para registro detallado.
migrate-links -l "language_codes" --save-logs, -s | Guarda en archivos los registros a nivel DEBUG bajo <root_dir>/logs/
migrate-links -l "all" -y                      | Procesa todos los idiomas y confirma automáticamente la advertencia.

## Ejemplos de uso

  1. Comportamiento predeterminado (agrega nuevas traducciones sin eliminar las existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Agrega solo nuevas traducciones de imágenes en coreano (no se eliminan traducciones existentes):    translate -l "ko" -img

  3. Actualiza todas las traducciones en coreano (Advertencia: Esto elimina todas las traducciones coreanas existentes antes de retraducir):    translate -l "ko" -u

  4. Actualiza solo imágenes coreanas (Advertencia: Esto elimina todas las imágenes coreanas existentes antes de retraducir):    translate -l "ko" -img -u

  5. Agrega nuevas traducciones Markdown para coreano sin afectar otras traducciones:    translate -l "ko" -md

  6. Corrige traducciones con baja confianza según resultados de evaluación previos: translate -l "ko" --fix

  7. Corrige traducciones con baja confianza para archivos específicos únicamente (Markdown): translate -l "ko" --fix -md

  8. Corrige traducciones con baja confianza para archivos específicos únicamente (imágenes): translate -l "ko" --fix -img

  9. Usa modo rápido para la traducción de imágenes:    translate -l "ko" -img -f

  10. Corrige traducciones con baja confianza con umbral personalizado: translate -l "ko" --fix -c 0.8

  11. Ejemplo modo debug: - translate -l "ko" -d: activa registro en modo debug.
  12. Guarda registros en archivos: translate -l "ko" -s
  13. DEBUG en consola y archivo: translate -l "ko" -d -s
  14. Traduce sin agregar avisos de traducción automática en las salidas: translate -l "ko" --no-disclaimer

  15. Migra enlaces de notebooks para traducciones coreanas (actualiza enlaces a notebooks traducidos cuando están disponibles):    migrate-links -l "ko"

  15. Migra enlaces con dry-run (sin escribir archivos):    migrate-links -l "ko" --dry-run

  16. Solo actualiza enlaces cuando existan notebooks traducidos (no usa originales):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesa todos los idiomas con aviso de confirmación:    migrate-links -l "all"

  18. Procesa todos los idiomas y confirma automáticamente:    migrate-links -l "all" -y
  19. Guarda registros en archivos para migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliza el aviso de idiomas en README con la URL de tu repositorio:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Ejemplos de evaluación

> [!WARNING]  
> **Funcionalidad Beta**: La funcionalidad de evaluación está actualmente en beta. Esta función fue lanzada para evaluar documentos traducidos, y los métodos de evaluación y la implementación detallada aún están en desarrollo y sujetos a cambios.

  1. Evalúa traducciones coreanas: evaluate -l "ko"

  2. Evalúa con umbral de confianza personalizado: evaluate -l "ko" -c 0.8

  3. Evaluación rápida (solo basada en reglas): evaluate -l "ko" -f

  4. Evaluación profunda (solo basada en LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->