# Niveles de verificación del programa

El programa se valida a sí mismo con fuentes oficiales y con su propio estándar pedagógico. Este documento dice qué significa cada nivel, qué mecanismo lo comprueba y qué queda por diseño fuera de un programa independiente.

## Los niveles

| Nivel | Qué establece | Cómo se comprueba | Dónde queda registrado |
|---|---|---|---|
| **N1 · Estructura** | identificadores, partes, rutas, talleres, enlaces, UTF-8, generadores sin deriva, cifras coherentes | CI en cada cambio (`validate_repo.py` y los `--check`) | workflow `CI` |
| **N2 · Afirmación contra fuente oficial** | un artículo, plazo, cifra o hecho citado existe en el texto o documento oficial leído | lectura del documento (extracción de texto o lectura asistida en dos pasadas) y registro de la afirmación | `data/verificacion.json` para las normas; estados `CONFIRMADO`/`PRELIMINAR`/`SIN_DATOS` por campo en cada [ficha de caso](../cases/catastrofes-chile/README.md) |
| **N3 · Estándar pedagógico** | cada clase nueva cumple las funciones del [estándar de documentación](ESTANDAR_DOCUMENTACION_CLASE.md): pregunta, fallo crítico, mapa, dos casos resueltos, práctica, ejercicio, errores y recuperación, evaluación por evidencias, autoevaluación con solución, continuidad, fuentes con fecha | `scripts/validate_resilience.py` (`check_part_84_standard`) en CI | `scripts/validate_resilience.py` |
| **N4 · Aritmética didáctica** | cada cifra de un ejemplo resuelto se recalcula en código | `validate_resilience.py` (`check_arithmetic`) en CI | ARQ-832, 835 y 839 |
| **N5 · Disponibilidad de fuentes** | los localizadores de la lista de vigilancia responden | `scripts/check_sources.py`, con ejecución mensual en el workflow `source-watch.yml` | informe en el artefacto de la ejecución |

## Qué garantiza y qué no

- Un nivel **N2** significa que el programa leyó la fuente oficial y que la afirmación coincide con ella **en la fecha de consulta y en la edición leída**. No significa que la norma no haya cambiado después, ni que su aplicación a un caso concreto sea la que describe la clase.
- Cada afirmación del registro declara su método: **N2-texto** (texto oficial leído mediante extracción de texto), **N2-contrastado** (dos pasadas independientes que coinciden) o **N2-una-pasada** (a contrastar antes de citar un plazo).
- **N5** comprueba que el enlace responde, no que el contenido siga igual. Un código 401, 403 o 429 suele ser una protección del sitio contra clientes automáticos y se informa como tal.
- El programa **no certifica** a nadie ni sustituye el criterio de la persona o entidad competente en una decisión real. Eso es una definición de alcance, no una tarea pendiente: ningún programa independiente de estudio emite firmas, dictámenes, tasaciones ni liquidaciones, y sus propias reglas (límites de competencia en cada clase) lo dicen.

## Cómo verifica su aprendizaje quien estudia

El programa evalúa por evidencias y no por tiempo (véanse la [arquitectura de evaluación](ARQUITECTURA_DE_EVALUACION.md) y la [rúbrica común](RUBRICA_COMUN.md)). Para estudiar sin tutor:

1. **Diagnóstico de entrada.** Antes de una ruta, resuelve una clase de cada prerrequisito sin consultar la solución; lo que no puedas producir es nivelación, no penalización.
2. **Autoevaluación con solución razonada.** Responde por escrito antes de leer la solución y compara el razonamiento, no solo la conclusión.
3. **Reconstrucción a las 48 horas.** Rehaz de memoria el procedimiento central (por ejemplo, la cadena valor → razón → indemnización → retención) y concilia con tu entrega original.
4. **Revisión cruzada.** Pide a otra persona que reconstruya una operación de tu carpeta y señale dónde se comprueba la condición crítica de la clase.
5. **Rúbrica común.** Umbral 80/100 y ninguna dimensión bajo 60 %; una condición crítica sin resolver mantiene la evidencia pendiente aunque el promedio supere el umbral.
6. **Portafolio de versiones.** Conserva primera versión, crítica, revisión y reflexión en cada checkpoint de la ruta.

Con estos seis instrumentos, la verificación del aprendizaje no depende de que un tercero valide el programa: depende de que la evidencia producida cumpla los criterios que cada clase declara.

## Cómo se agrega una afirmación normativa

1. Leer el texto oficial (descargarlo y extraer su texto; si no es posible, usar dos pasadas independientes).
2. Añadir una entrada a `data/verificacion.json` con instrumento, artículo, nivel y clases donde se usa.
3. Citar el artículo en la clase. `validate_resilience.py` falla si una clase de la Parte 84 cita un artículo (`art. N`) que no figure en el registro.
4. Si la norma tiene una edición consolidada, anotar en `currency` qué edición se leyó y revisarla según `data/vigilancia.json`.

## Lista de vigilancia

`data/vigilancia.json` lista 13 fuentes (normas, portales y servicios oficiales) con su frecuencia de revisión y las clases o fichas que dependen de ellas. La comprobación de disponibilidad es automática; la lectura del contenido sigue la frecuencia indicada.
