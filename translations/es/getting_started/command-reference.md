# Referencia de comandos

La CLI de **Co-op Translator** ofrece varias opciones para personalizar el proceso de traducción:

Comando                                      | Descripción
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce tu proyecto a los idiomas especificados. Ejemplo: translate -l "es fr de" traduce al español, francés y alemán. Usa translate -l "all" para traducir a todos los idiomas soportados.
translate -l "language_codes" -u              | Actualiza las traducciones eliminando las existentes y volviéndolas a crear. Advertencia: Esto eliminará todas las traducciones actuales para los idiomas especificados.
translate -l "language_codes" -img            | Traduce solo archivos de imagen.
translate -l "language_codes" -md             | Traduce solo archivos Markdown.
translate -l "language_codes" -nb             | Traduce solo archivos Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraducce archivos con puntajes bajos de confianza basándose en resultados de evaluaciones previas.
translate -l "language_codes" -d              | Activa el modo debug para obtener un registro detallado.
translate -l "language_codes" --save-logs, -s | Guarda registros a nivel DEBUG en archivos bajo <root_dir>/logs/ (la consola sigue controlada por -d)
translate -l "language_codes" -r "root_dir"   | Especifica el directorio raíz del proyecto
translate -l "language_codes" -f              | Usa modo rápido para la traducción de imágenes (hasta 3x más rápido con un ligero costo en calidad y alineación).
translate -l "language_codes" -y              | Confirma automáticamente todas las solicitudes (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Habilita o deshabilita agregar una sección de aviso de traducción automática en markdown traducido y notebooks (por defecto: habilitado).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliza el aviso de la sección de idiomas en el README (cotejo disperso) con la URL de tu repositorio.
translate -l "language_codes" --help          | muestra detalles de ayuda dentro de la CLI mostrando comandos disponibles
evaluate -l "language_code"                  | Evalúa la calidad de la traducción para un idioma específico y proporciona puntajes de confianza
evaluate -l "language_code" -c 0.8           | Evalúa traducciones con un umbral de confianza personalizado
evaluate -l "language_code" -f               | Modo de evaluación rápida (solo reglas, sin LLM)
evaluate -l "language_code" -D               | Modo de evaluación profunda (solo LLM, más exhaustivo pero más lento)
evaluate -l "language_code" --save-logs, -s  | Guarda registros a nivel DEBUG en archivos bajo <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocesa archivos Markdown traducidos para actualizar enlaces a notebooks (.ipynb). Prefiere notebooks traducidos cuando están disponibles; de lo contrario puede recurrir a notebooks originales.
migrate-links -l "language_codes" -r          | Especifica el directorio raíz del proyecto (por defecto: directorio actual).
migrate-links -l "language_codes" --dry-run   | Muestra qué archivos cambiarían sin escribir cambios.
migrate-links -l "language_codes" --no-fallback-to-original | No reescribe enlaces a notebooks originales cuando faltan sus equivalentes traducidos (actualiza sólo si existe versión traducida).
migrate-links -l "language_codes" -d          | Activa modo debug para registro detallado.
migrate-links -l "language_codes" --save-logs, -s | Guarda registros a nivel DEBUG en archivos bajo <root_dir>/logs/
migrate-links -l "all" -y                      | Procesa todos los idiomas y confirma automáticamente la advertencia.

## Ejemplos de uso

  1. Comportamiento por defecto (agrega nuevas traducciones sin eliminar las existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Agrega solo nuevas traducciones de imágenes en coreano (no se eliminan traducciones existentes):    translate -l "ko" -img

  3. Actualiza todas las traducciones en coreano (Advertencia: Esto elimina todas las traducciones coreanas existentes antes de retraducir):    translate -l "ko" -u

  4. Actualiza solo las imágenes coreanas (Advertencia: Esto elimina todas las imágenes coreanas existentes antes de retraducir):    translate -l "ko" -img -u

  5. Agrega nuevas traducciones markdown para coreano sin afectar otras traducciones:    translate -l "ko" -md

  6. Arregla traducciones con baja confianza basándose en evaluaciones previas: translate -l "ko" --fix

  7. Arregla traducciones con baja confianza solo para archivos específicos (markdown): translate -l "ko" --fix -md

  8. Arregla traducciones con baja confianza solo para archivos específicos (imágenes): translate -l "ko" --fix -img

  9. Usa modo rápido para traducción de imágenes:    translate -l "ko" -img -f

  10. Arregla traducciones con baja confianza con umbral personalizado: translate -l "ko" --fix -c 0.8

  11. Ejemplo modo debug: - translate -l "ko" -d: Activa registro debug.
  12. Guarda registros en archivos: translate -l "ko" -s
  13. DEBUG en consola y en archivos: translate -l "ko" -d -s
  14. Traduce sin agregar avisos de traducción automática en las salidas: translate -l "ko" --no-disclaimer

  15. Migra enlaces de notebooks para traducciones coreanas (actualiza enlaces a notebooks traducidos cuando están disponibles):    migrate-links -l "ko"

  15. Migra enlaces en modo dry-run (sin escribir archivos):    migrate-links -l "ko" --dry-run

  16. Solo actualiza enlaces cuando existen notebooks traducidos (sin recurrir a originales):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesa todos los idiomas con solicitud de confirmación:    migrate-links -l "all"

  18. Procesa todos los idiomas y confirma automáticamente:    migrate-links -l "all" -y
  19. Guarda registros en archivos para migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliza el aviso de idiomas del README con la URL de tu repo:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Ejemplos de evaluación

> [!WARNING]  
> **Función Beta**: La funcionalidad de evaluación está actualmente en beta. Esta función fue lanzada para evaluar documentos traducidos, y los métodos de evaluación y la implementación detallada aún están en desarrollo y pueden cambiar.

  1. Evalúa traducciones coreanas: evaluate -l "ko"

  2. Evalúa con umbral de confianza personalizado: evaluate -l "ko" -c 0.8

  3. Evaluación rápida (solo reglas): evaluate -l "ko" -f

  4. Evaluación profunda (solo LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción AI [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->