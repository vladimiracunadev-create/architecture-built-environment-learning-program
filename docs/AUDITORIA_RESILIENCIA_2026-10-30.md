# Auditoría de seguridad y resiliencia — 2026-10-30

**Línea base verificada:** HEAD `84518c1`, rama `main`. 830 clases ARQ-001–830, 83 partes, 4 fases, 34 rutas, 10 talleres, 60 sesiones, 631 URLs de fuente únicas, 2.419 relaciones clase–fuente (1.366 completas). Los nueve controles de CI estaban en verde antes de intervenir.

> CI correcto ≠ exactitud técnica garantizada ≠ validación profesional ≠ eficacia pedagógica demostrada. Este documento es una auditoría editorial, no una certificación técnica.

## 1. Reconfirmación de los problemas conocidos

| Antecedente | Estado en este HEAD | Acción |
|---|---|---|
| 1.053 relaciones clase–fuente incompletas | Confirmado (2.419 − 1.366 = 1.053) | `REVISIÓN_ESPECIALIZADA_PENDIENTE`; no se completan metadatos sin consulta real |
| Cinco clases con revisión manual profunda | Confirmado por el contador del CI | Sin cambio; ver §4 |
| Patrones editoriales largos compartidos | Medidos por `audit_class_distinctness.py --check` | Sin regresión |
| Pilotos con estudiantes | No existen | Declarado en §6 |
| Revisión profesional externa | Pendiente | Declarado en §6 |
| Referencias a 33 rutas / tres fases | `generate_curriculum_docs.py` y `classes/README.md` decían «tres fases» y omitían la Fase IV | **CORREGIDO**: el generador deriva el número de fases de `data/program.json` y lista la Fase IV (Partes 81–83) |
| Otras menciones de 33 rutas / 800 clases | Solo en documentos fechados (`AUDITORIA_RUTA_VIVIENDA_2026-10-12.md`, `INFORME_INTEGRACION_2026-10.md`, `ROADMAP_INTEGRAL.md`) | `CONSERVAR` como historia; no se reescriben |
| Conteos rígidos en CI | Persisten en el resumen de `ci.yml` (texto informativo; las verificaciones reales leen `data/program.json`) | Pendiente: derivar el resumen de `program.json` |
| Enlaces, legislación y versiones normativas | No re-verificados contra fuentes oficiales en esta sesión | `REVISIÓN_ESPECIALIZADA_PENDIENTE` |

## 2. Hallazgo principal: la cobertura temática ya existe; los seguros son la brecha real

El programa ya contiene las competencias que pedía la ampliación. Se conservan:

| Tema | Clases existentes | Decisión |
|---|---|---|
| Geología, suelos, geotecnia, fundaciones | ARQ-181–190 | `CONSERVAR`; `PROFUNDIZAR` por ejercicio (§5) |
| Amenazas hidrometeorológicas, geológicas, encadenadas | ARQ-351–380 | `CONSERVAR`; `CONECTAR` con el expediente integrador |
| Sismo y estructura | ARQ-341–350 | `CONSERVAR` |
| Territorio, predio y restricciones | ARQ-101–110, 391–400 | `CONSERVAR`; `CONECTAR` |
| Costo de ciclo de vida y sensibilidad | ARQ-418, 420 | `CONECTAR` con escenarios de pérdida |
| Operación y mantenimiento | ARQ-461–470 | `CONSERVAR` |
| Reconstrucción y memoria | ARQ-088, 379 | `CONECTAR` con la biblioteca de casos |
| **Seguros y gestión económica del riesgo** | ARQ-694, 819 mencionan «seguro» como etiqueta; en ARQ-694 no aparecen póliza, deducible, infraseguro ni CMF | **Brecha real** → [guía de seguros](SEGUROS_Y_GESTION_ECONOMICA_DEL_RIESGO.md) |

Los casos de catástrofes chilenas no estaban organizados como biblioteca → [cases/catastrofes-chile](../cases/catastrofes-chile/README.md). El proyecto longitudinal de decisión de emplazamiento no existía → [Decisión integral de construcción resiliente](../cases/DECISION-INTEGRAL-RESILIENTE.md).

## 3. Matriz de integración por IDs y rutas

| Bloque | Qué se integra | Rutas | Talleres |
|---|---|---|---|
| ARQ-081–090 | casos históricos de reconstrucción (ARQ-088) | RUTA-04 | EST-02 |
| ARQ-101–110 | ficha de terreno y comparación de predios | RUTA-04, 12, 34 | EST-02 |
| ARQ-181–190 | informe geotécnico y encargo profesional | RUTA-05, 12 | EST-04 |
| ARQ-341–380 | matriz multiamenaza y escenarios encadenados | RUTA-05, 28, 29 | EST-05 |
| ARQ-391–400 | obligación vs. estándar vs. recomendación | RUTA-12, 34 | EST-06 |
| ARQ-418, 420, 694, 819 | seguros, deducibles, pérdida anual esperada vs. escenario extremo | RUTA-07, 12, 34 | EST-06 |
| ARQ-461–470 | mantenimiento planificado vs. correctivo | RUTA-11 | EST-07 |
| ARQ-751–770 | infraestructura crítica y continuidad | RUTA-25, 29 | EST-07, EST-10 |
| ARQ-801–830 | aplicación a vivienda y ampliación | RUTA-15, 34 | EST-02, EST-06 |

Las rutas no cambian de número ni de identificador. El enriquecimiento ocurre por documentos de caso y guías, no por rutas nuevas: no se identificó un perfil de aprendizaje distinto de los 34 existentes.

## 4. Decisiones sobre clases nuevas

**No se crea ninguna clase en esta intervención.** Justificación individual:

- *Territorio y selección de terreno:* ya desarrollado en ARQ-101–110, 360 y 391–400. Se integra mediante el expediente integrador.
- *Mecánica de suelos:* ARQ-181–190 cubre el eje; la profundización es por ejercicio, no por clase.
- *Amenazas:* ARQ-351–380 cubre las 14 dimensiones pedidas a nivel de clase; la verificación fenómeno por fenómeno queda pendiente (§6).
- *Seguros:* cumple varios criterios de nueva clase (competencia no desarrollada, problema propio, evidencia nueva), pero crearla exige una Parte 84 completa (10 clases), actualizar manifiestos, validadores, CI, índices, bibliografía y sitio, y fuentes primarias que aún no se han consultado. Se difiere con **candidato registrado**: *ARQ-831 · Pólizas, coberturas y exclusiones de inmuebles y obra*, con prerrequisitos ARQ-418, 420, 694. Mientras tanto, la guía de seguros cubre el contenido sin tocar la numeración.

## 5. Profundizaciones por ejercicio (sin alterar las clases)

- Interpretar un informe geotécnico: qué datos debe contener, qué preguntas hacer al especialista, qué conclusión **no** puede extraer el propietario.
- Encargo geotécnico: formular alcance, profundidad esperada, cadena de custodia y entregables.
- Estos ejercicios viven en el expediente integrador y no son recomendaciones de cimentación.

## 6. Limitaciones y revisiones pendientes

- Ninguna norma, artículo, póliza ni cifra de catástrofe fue consultada en fuente primaria en esta intervención; todo ello queda `SIN_DATOS` o `REVISIÓN_ESPECIALIZADA_PENDIENTE`.
- Cronología 2026 de eventos: no construida; requiere consulta a Dirección Meteorológica, SENAPRED, SERNAGEOMIN, DGA, SHOA y CONAF.
- Sin pilotos con estudiantes ni revisión profesional (ingeniería geotécnica, estructural, derecho urbanístico, seguros).
- No existe monitoreo automatizado de normativa; el inventario de vigilancia está en la guía de seguros y en el README de casos.
- Los 142 patrones editoriales compartidos y las 1.053 relaciones de fuente incompletas siguen siendo trabajo de profundización editorial por clase.

## 7. Actualización posterior: lo que se construyó

Esta sección registra la ejecución posterior al diagnóstico. La línea base de las secciones 1–6 se conserva como foto inicial y sus afirmaciones de «no se crea ninguna clase» y «ninguna norma leída» quedan superadas por lo que sigue.

- **Parte 84 · Evaluación de inmuebles, seguros y eventos catastróficos (ARQ-831–840).** La competencia de seguros cumplía los criterios de clase nueva y la ruta de evaluación de inmuebles para corredores añadió cinco competencias sin clase equivalente. Se crearon diez clases, de entre 3.284 y 4.480 palabras cada una (con el contrato pedagógico generado), sin renumerar ARQ-001–830. Las fases siguen siendo cuatro; la Fase IV amplía su alcance a ARQ-801–840. Tras una primera versión más breve, cada clase incorporó un segundo caso resuelto con cifras y una autoevaluación con solución razonada.
- **Seguros con base legal.** ARQ-831–833 citan artículos de la Ley 20.667 (Título VIII del Libro II del Código de Comercio) a partir de una lectura asistida del texto y de la nota educativa de la CMF. Sigue pendiente contrastar con la versión consolidada vigente y leer el reglamento de liquidadores.
- **RUTA-35** (evaluación técnica de inmuebles para corredores de propiedades), capstone EST-06, sobre 44 clases.
- **Biblioteca de casos:** diez fichas (CAT-001, 003, 004, 005 y CAT-2026-001 a 006). Ninguna llega a `CONFIRMADO` como caso; se leyeron comunicados de SENAPRED, avisos e informes de la DMC y un artículo académico sobre el 27F. Dos fichas de 2026 son solo de pronóstico y alertas.
- **Rutas con extensión de riesgo:** RUTA-04, 05, 06, 07, 11, 12, 15, 18, 25, 28, 29, 30 y 34.
- **Controles:** `scripts/validate_resilience.py` (estructura de fichas, RUTA-35 y cálculos didácticos, entre ellos la pérdida esperada y el costo correctivo), resumen de CI derivado de `data/program.json`, cifras de fuentes derivadas de la bibliografía en el validador y generador de fases corregido.
- **Documentación:** guía de la biblioteca de casos, tabla de scripts y flujo de regeneración en la arquitectura del repositorio, CONTRIBUTING con el flujo completo y glosario ordenado.

### Pendientes que este repositorio no puede resolver por sí solo

- Revisión de especialistas: ingeniería geotécnica y estructural, derecho de seguros y de corretaje, tasación y seguros.
- Contraste con corredores, tasadores y aseguradores en ejercicio, y pilotos con estudiantes.
- Lectura íntegra de los informes técnicos de SERNAGEOMIN, CONAF, DGA y SHOA, y de los balances de cierre de SENAPRED.
- Eventos de 2026 sin fuente oficial hallada: lluvias altiplánicas de verano, tormentas eléctricas, marejadas y sequía.
- Vigilancia periódica de normas y fuentes: sigue siendo manual y no hay monitoreo automático.
