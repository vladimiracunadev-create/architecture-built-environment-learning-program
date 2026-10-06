# Auditoría de diferencias entre las 800 clases

**Edición auditada:** 2026.10  
**Alcance:** `ARQ-001`–`ARQ-800`  
**Registro clase por clase:** [`audits/class-distinctness.csv`](audits/class-distinctness.csv)  
**Resumen legible por máquina:** [`../data/audits/class-distinctness.json`](../data/audits/class-distinctness.json)

## Por qué se hizo

Que existan 800 archivos no demuestra que existan 800 clases. Una clase puede cambiar de título y conservar el mismo razonamiento, ejercicio o texto. Esta auditoría busca esa diferencia entre **cantidad de archivos**, **estructura compartida** y **sustancia editorial propia**.

La revisión separa el contrato pedagógico generado, que debe ser común, del cuerpo escrito de cada clase. También excluye la lista final de fuentes al buscar párrafos repetidos. Así, una rúbrica compartida o dos clases que citan el mismo organismo no se confunden con duplicación de contenido.

## Qué se comprobó

| Prueba | Resultado | Lectura correcta |
|---|---:|---|
| archivos inspeccionados | 800 | cubre el catálogo completo, no una muestra |
| archivos completos exactamente distintos | 800 | no hay copias binarias de una clase con otro nombre |
| preguntas centrales presentes y distintas | 800/800 | cada clase formula una pregunta diferente |
| extensión | 1.247–4.219 palabras; mediana 2.859 | mide desarrollo, no calidad por sí sola |
| proporción mediana de prosa editorial usada por una sola clase | 94,13 % | la mayor parte del texto largo no se repite literalmente |
| mayor similitud de cinco palabras dentro de una misma parte | 67,05 % | hay bloques históricos con una base común todavía demasiado dominante |
| patrones editoriales largos repetidos en más de diez clases | 129 | la base anterior conserva familias que requieren diferenciación posterior |

La fila de cada clase incluye cantidad de palabras, huellas de archivo, pregunta, gráfico y condición crítica; proporción de prosa propia; y la clase más parecida dentro de su parte. Esto permite revisar un caso concreto sin depender de una afirmación global.

## Resultado específico de las 120 clases nuevas

Las clases `ARQ-681`–`ARQ-800` fueron reescritas después del primer diagnóstico. Antes compartían varios párrafos extensos de método, contexto profesional, errores y recuperación. Aunque sus temas y preguntas eran distintos, la lectura seguía mostrando una voz demasiado mecánica.

Después de la corrección:

| Control de Fase III | Resultado |
|---|---:|
| archivos exactamente distintos | 120/120 |
| preguntas centrales distintas | 120/120 |
| condiciones críticas distintas | 120/120 |
| diagramas temáticos Mermaid distintos | 120/120 |
| extensión | 3.455–3.863 palabras |
| menor proporción individual de prosa larga propia | 92,75 % |
| mediana de prosa larga propia | 94,05 % |
| párrafos editoriales largos no autorizados repetidos en más de diez clases | 0 |

Cada clase desarrolla ahora sus cuatro a seis pasos con entradas, operación, salida y comprobación; conecta el tema con el caso de su parte; asigna interfaces profesionales; construye errores desde su evidencia específica; y propone recuperación desde su propia secuencia. El diagrama no es decorativo: usa los pasos y la condición crítica de esa clase.

La similitud mediana de cinco palabras dentro de cada parte es 56,92 %. Este indicador incluye títulos de secciones, instrucciones de portafolio y la anatomía pedagógica estable. Por eso se lee junto con la proporción de párrafos propios y no como una sentencia aislada de duplicación.

## Diferencias reales que sí permanecen entre clases

La auditoría considera sustantivas estas dimensiones:

1. **pregunta:** qué problema debe poder responder el estudiante;
2. **secuencia:** qué operaciones ordenan el aprendizaje;
3. **evidencia:** qué objeto verificable se produce;
4. **condición crítica:** qué fallo impide aceptar una entrega convincente;
5. **caso y escala:** dónde se aplica y qué no puede transferirse sin volver a investigar;
6. **representación:** qué diagrama, plano, tabla, modelo o prototipo hace visible la relación;
7. **coordinación:** qué resuelve arquitectura y qué debe preguntar a otras disciplinas;
8. **recuperación:** cómo se vuelve a intentar sin repetir mecánicamente el mismo caso.

Compartir encabezados, una rúbrica, reglas de fuentes, límites profesionales o un formato de portafolio es una decisión pedagógica deliberada. Compartir explicaciones largas del tema, el mismo caso con sustantivos cambiados o un ejercicio que no depende de la pregunta se registra como deuda editorial.

## Dónde siguen las mayores similitudes

La auditoría no declara homogéneas las 800 clases. Las partes con menor proporción media de prosa propia son, en este orden, `62`, `61`, `66`, `65`, `58`, `57`, `49`, `50`, `56`, `60`, `55`, `54`, `59`, `53` y `52`. Son bloques de infraestructura, tipologías y tecnología que comparten explicaciones, advertencias y ejercicios cuantitativos extensos.

Los patrones repetidos cumplen a veces una función válida —por ejemplo, recordar que un cálculo didáctico no verifica seguridad integral—, pero su frecuencia puede ocultar la diferencia disciplinar. La prioridad editorial siguiente será revisar primero las partes 61–62 y 65–66, y luego 49–60. La acción correcta es sustituir párrafos comunes por mecanismos, decisiones, casos y gráficos propios; añadir el título dentro de la misma plantilla no cuenta como corrección.

## Cómo se reproduce

```bash
python scripts/audit_class_distinctness.py --check
```

El control falla si deja de haber 800 archivos distintos, si Fase III pierde alguna de sus 120 preguntas, condiciones o gráficas propias, si reaparece un párrafo editorial largo no autorizado en más de diez clases nuevas, o si el CSV y el resumen quedan desactualizados.

## Límites de la comprobación

Las huellas y métricas detectan copias, repetición y proximidad verbal. No demuestran exactitud disciplinar, eficacia con estudiantes, vigencia normativa ni calidad equivalente en las 800 clases. Esas verificaciones requieren revisión especializada, prueba docente y observación del aprendizaje. El registro permite priorizarlas sin ocultar qué partes siguen pendientes.
