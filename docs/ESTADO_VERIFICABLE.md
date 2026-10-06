# Estado verificable del programa

**Corte documental: 6 de octubre de 2026 · edición 2026.10**

Este documento separa integridad curricular, cobertura pedagógica, trazabilidad de fuentes, publicación técnica y revisión profesional. Los conteos vigentes proceden de `data/program.json` y de validaciones reproducibles; `STATUS_v1.0.json` conserva únicamente la entrega histórica de 680 clases.

## 1. Integridad curricular

| Comprobación | Resultado actual | Fuente de verdad |
|---|---:|---|
| Identificadores consecutivos | **800/800** | `data/catalog.json`: ARQ-001 → ARQ-800 |
| Partes curriculares | **80/80** | `data/parts.json` y `classes/parte-01` → `parte-80` |
| Clases por parte | **10 en cada una** | validador estructural |
| Clases Markdown | **800** | `classes/parte-XX/ARQ-XXX.md` |
| README de parte | **80** | uno por carpeta, generado desde las clases |
| Fases | **3** | formación transversal; tipologías; profundización y especialización |

“800/800” significa que la malla editorial prevista por la edición 2026.10 está redactada. No significa revisión por pares, acreditación, vigencia normativa universal ni aptitud para ejecutar una obra.

## 2. Cobertura pedagógica dentro de las clases

`scripts/audit_pedagogical_traceability.py --json` inspecciona las 800 fuentes Markdown. La capa común se genera desde `data/pedagogy.json` y se comprueba con `scripts/apply_pedagogy.py --check`.

| Componente documental | Cobertura | Lectura correcta |
|---|---:|---|
| Pregunta central | **800/800** | problema delimitado en todo el programa |
| Práctica o ejercicio | **800/800** | actividad propia del tema |
| Evidencia explícita | **800/800** | producto revisable y criterio de aceptación |
| Fuentes y alcance de uso | **800/800** | apoyo y límite declarados |
| Mapa visual de aprendizaje | **800/800** | dependencias y transferencia visibles |
| Autoevaluación, errores, recuperación y continuidad | **800/800** | revisión y avance explícitos |
| Cadena de decisión documentada | **800/800** | necesidad, posición, dependencias, fuentes, actividad y evidencia |
| Casos trabajados o razonados | **690/800** | se emplean cuando la disciplina requiere reconstruir una situación |
| Piloto con revisión editorial manual profunda | **5/800** | muestra inicial, intermedia, normativa, avanzada y final del núcleo previo |
| Títulos normalizados duplicados | **0** | control de inflación temática |

El corpus contiene aproximadamente **2,04 millones de unidades separadas por espacio**, con mediana de **2.685,5 por clase**. La longitud describe escala editorial; no demuestra calidad o aprendizaje.

## 3. Talleres, rutas y portafolio

| Superficie | Resultado actual |
|---|---:|
| Talleres verticales | **10** |
| Sesiones integradoras | **60** |
| Fases por taller | **6**: diagnóstico, investigación, alternativas, crítica, revisión y defensa |
| Rutas con diagnóstico, checkpoints, salida y capstone | **33/33** |
| Dimensiones de la rúbrica común | **5** |
| Umbral documental | **80/100**, ninguna dimensión bajo 60 % |
| Pilotos con estudiantes | **pendiente** |
| Carga horaria observada | **pendiente** |

## 4. Fuentes y procedencia

| Superficie | Resultado |
|---|---:|
| Relaciones clase–fuente derivadas | **2.179** |
| URLs externas únicas en clases | **627** |
| Dominios externos en clases | **190** |
| Clases con apartado de fuentes | **800/800** |
| Relaciones con función declarada | **2.112/2.179** |
| Relaciones con alcance consultado | **1.725/2.179** |
| Relaciones con límite declarado | **1.974/2.179** |
| Relaciones con fecha de consulta | **1.298/2.179** |
| Relaciones contextualmente completas | **1.126/2.179** |
| Clases con todos sus usos completos | **412/800** |
| Verificación periódica de disponibilidad externa | **pendiente** |
| Revisión normativa por jurisdicción | **pendiente** |

Las 611 fichas del lector offline son un inventario histórico. `sources/bibliography.json` es el registro actual derivado de las clases y conserva los faltantes como datos explícitos, sin inventar fechas, páginas o alcances.

## 5. Publicación y artefactos

| Salida | Estado | Comprobación |
|---|---|---|
| GitHub Pages | generable | build reproducible desde Markdown y manifiestos |
| Páginas de clase | **800** | una por ARQ |
| Portadas de parte | **80** | una por bloque |
| Páginas de taller | **70** | diez portadas + 60 sesiones |
| Rutas pedagógicas | **33** | entrada, recorrido, checkpoints, salida y capstone |
| Recursos transversales del lector v1.0 | **755** | colección histórica conservada |
| Lector offline y PDF v1.0 | conservados | hashes versionados |
| Enlaces internos, UTF-8 y salidas | verificables | `scripts/validate_repo.py` |

## 6. Brechas abiertas

1. **Revisión externa por especialidades.** Falta revisión integral por arquitectura, estructuras, geotecnia, instalaciones, incendio, accesibilidad, patrimonio, costos, construcción, operación y educación.
2. **Pilotos pedagógicos.** Falta medir comprensión, abandono, tiempos, crítica, recuperación y transferencia con estudiantes reales.
3. **Carga y calendario.** No se publican horas ni créditos hasta observarlos en condiciones declaradas.
4. **Fuentes.** 1.053 usos requieren completar uno o más campos contextuales; también falta vigilancia periódica de disponibilidad y vigencia.
5. **Visuales disciplinares.** Existen mapas de aprendizaje; deben ampliarse planos, cortes, mapas, detalles y diagramas técnicos por especialidad.
6. **Accesibilidad especializada.** El sitio usa estructura semántica y diseño adaptable, pero no cuenta con auditoría WCAG externa.

El [roadmap integral](../ROADMAP_INTEGRAL.md) conserva el orden de resolución, responsables documentales y condiciones de cierre de estas brechas.

## Cómo reproducir la comprobación

```bash
python scripts/generate_curriculum_docs.py --check
python scripts/build_pedagogical_decisions.py --check
python scripts/apply_pedagogy.py --check
python scripts/audit_pedagogical_traceability.py --json
python scripts/build_bibliography.py --check
python scripts/build_site.py
python scripts/validate_repo.py
```

Un CI verde demuestra coherencia reproducible del repositorio. No demuestra corrección disciplinar de cada clase, vigencia legal ni eficacia educativa.
