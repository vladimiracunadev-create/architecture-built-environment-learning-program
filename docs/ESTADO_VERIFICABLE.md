# Estado verificable del programa

**Corte documental: 12 de octubre de 2026 · edición 2026.10**

Este documento separa integridad curricular, cobertura pedagógica, trazabilidad de fuentes, publicación técnica y revisión profesional. Los conteos vigentes proceden de `data/program.json` y de validaciones reproducibles; `STATUS_v1.0.json` conserva únicamente la entrega histórica de 680 clases.

## 1. Integridad curricular

| Comprobación | Resultado actual | Fuente de verdad |
|---|---:|---|
| Identificadores consecutivos | **830/830** | `data/catalog.json`: ARQ-001 → ARQ-830 |
| Partes curriculares | **83/83** | `data/parts.json` y `classes/parte-01` → `parte-83` |
| Clases por parte | **10 en cada una** | validador estructural |
| Clases Markdown | **840** | `classes/parte-XX/ARQ-XXX.md` |
| README de parte | **83** | uno por carpeta, generado desde las clases |
| Fases | **4** | formación transversal; tipologías; profundización; aplicación integrada a vivienda |

“840/840” significa que la malla editorial prevista por la edición 2026.10 está redactada. No significa revisión por pares, acreditación, vigencia normativa universal ni aptitud para ejecutar una obra.

## 2. Cobertura pedagógica dentro de las clases

`scripts/audit_pedagogical_traceability.py --json` inspecciona las 840 fuentes Markdown. La capa común se genera desde `data/pedagogy.json` y se comprueba con `scripts/apply_pedagogy.py --check`.

| Componente documental | Cobertura | Lectura correcta |
|---|---:|---|
| Pregunta central | **840/840** | problema delimitado en todo el programa |
| Práctica o ejercicio | **840/840** | actividad propia del tema |
| Evidencia explícita | **840/840** | producto revisable y criterio de aceptación |
| Fuentes y alcance de uso | **840/840** | apoyo y límite declarados |
| Mapa visual de aprendizaje | **840/840** | dependencias y transferencia visibles |
| Autoevaluación, errores, recuperación y continuidad | **840/840** | revisión y avance explícitos |
| Cadena de decisión documentada | **840/840** | necesidad, posición, dependencias, fuentes, actividad y evidencia |
| Casos trabajados o razonados | **730/840** | se emplean cuando la disciplina requiere reconstruir una situación |
| Piloto con revisión editorial manual profunda | **5/840** | muestra del núcleo previo |
| Títulos normalizados duplicados | **0** | control de inflación temática |

La [auditoría de diferencias](AUDITORIA_DIFERENCIAS_800_CLASES.md) inspecciona duplicación y proximidad editorial. Los 840 archivos y las 840 preguntas son distintos. Fase III conserva 120 preguntas, condiciones críticas y gráficas propias sin explicaciones largas no autorizadas repetidas en más de diez clases; Fase IV añade 40 archivos, preguntas, condiciones y gráficas distintas. El corpus tiene una mediana de **2.889 palabras por clase**. Longitud y unicidad verbal describen escala editorial; no demuestran calidad o aprendizaje.

## 3. Talleres, rutas y portafolio

| Superficie | Resultado actual |
|---|---:|
| Talleres verticales | **10** |
| Sesiones integradoras | **60** |
| Fases por taller | **6**: diagnóstico, investigación, alternativas, crítica, revisión y defensa |
| Rutas con diagnóstico, checkpoints, salida y capstone | **35/35** |
| Dimensiones de la rúbrica común | **5** |
| Umbral documental | **80/100**, ninguna dimensión bajo 60 % |
| Pilotos con estudiantes | **pendiente** |
| Carga horaria observada | **pendiente** |

## 4. Fuentes y procedencia

| Superficie | Resultado |
|---|---:|
| Relaciones clase–fuente derivadas | **2.441** |
| URLs externas únicas en clases | **635** |
| Dominios externos en clases | **190** |
| Clases con apartado de fuentes | **840/840** |
| Relaciones con función declarada | **2.374/2.441** |
| Relaciones con alcance consultado | **1.987/2.441** |
| Relaciones con límite declarado | **2.236/2.441** |
| Relaciones con fecha de consulta | **1.560/2.441** |
| Relaciones contextualmente completas | **1.388/2.441** |
| Clases con todos sus usos completos | **452/840** |
| Verificación periódica de disponibilidad externa | **pendiente** |
| Revisión normativa por jurisdicción | **pendiente** |

Las 611 fichas del lector offline son un inventario histórico. `sources/bibliography.json` es el registro actual derivado de las clases y conserva los faltantes como datos explícitos, sin inventar fechas, páginas o alcances.

## 5. Publicación y artefactos

| Salida | Estado | Comprobación |
|---|---|---|
| GitHub Pages | generable | build reproducible desde Markdown y manifiestos |
| Páginas de clase | **840** | una por ARQ |
| Portadas de parte | **83** | una por bloque |
| Páginas de taller | **70** | diez portadas + 60 sesiones |
| Rutas pedagógicas | **35** | entrada, recorrido, checkpoints, salida y capstone |
| Casos domésticos aplicados | **2** | casa nueva de 80 m² y ampliación de 24 m², ambos didácticos |
| Presupuestos verificables | **2 CSV + 1 XLSX** | esquema, fórmulas y controles validados en CI |
| Recursos transversales del lector v1.0 | **755** | colección histórica conservada |
| Lector offline y PDF v1.0 | conservados | hashes versionados |
| Enlaces internos, UTF-8 y salidas | verificables | `scripts/validate_repo.py` |

## 6. Brechas abiertas

1. **Revisión externa por especialidades.** Falta revisión integral por arquitectura, estructuras, geotecnia, instalaciones, incendio, accesibilidad, patrimonio, costos, construcción, operación y educación.
2. **Pilotos pedagógicos.** Falta medir comprensión, abandono, tiempos, crítica, recuperación y transferencia con estudiantes reales.
3. **Carga y calendario.** No se publican horas ni créditos hasta observarlos en condiciones declaradas.
4. **Fuentes.** 1.053 usos requieren completar uno o más campos contextuales; también falta vigilancia periódica de disponibilidad y vigencia.
5. **Precios locales.** Los valores de los casos y la planilla son hipótesis didácticas y deben reemplazarse por cotizaciones comparables, fechadas y ubicadas.
6. **Accesibilidad especializada.** El sitio usa estructura semántica y diseño adaptable, pero no cuenta con auditoría WCAG externa.
7. **Diferenciación del núcleo anterior.** La auditoría detecta 142 patrones editoriales largos presentes en más de diez clases; su corrección requiere cambiar mecanismos, casos, evidencias y gráficas, no sólo vocabulario.

El [roadmap integral](../ROADMAP_INTEGRAL.md) conserva el orden de resolución, responsables documentales y condiciones de cierre de estas brechas.

## Cómo reproducir la comprobación

```bash
python scripts/generate_curriculum_docs.py --check
python scripts/build_pedagogical_decisions.py --check
python scripts/apply_pedagogy.py --check
python scripts/audit_pedagogical_traceability.py --json
python scripts/audit_class_distinctness.py --check
python scripts/build_bibliography.py --check
python scripts/validate_homeowner_budget.py
python scripts/build_site.py
python scripts/validate_repo.py
```

Un CI verde demuestra coherencia reproducible del repositorio. No demuestra corrección disciplinar de cada clase, vigencia legal ni eficacia educativa.
