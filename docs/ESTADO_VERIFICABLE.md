# Estado verificable del programa

**Corte documental: 30 de octubre de 2026 · edición 2026.10**

Este documento separa integridad curricular, cobertura pedagógica, trazabilidad de fuentes, publicación técnica y revisión profesional. Los conteos vigentes proceden de `data/program.json` y de validaciones reproducibles; `STATUS_v1.0.json` conserva únicamente la entrega histórica de 680 clases.

## 1. Integridad curricular

| Comprobación | Resultado actual | Fuente de verdad |
|---|---:|---|
| Identificadores consecutivos | **840/840** | `data/catalog.json`: ARQ-001 → ARQ-840 |
| Partes curriculares | **84/84** | `data/parts.json` y `classes/parte-01` → `parte-84` |
| Clases por parte | **10 en cada una** | validador estructural |
| Clases Markdown | **840** | `classes/parte-XX/ARQ-XXX.md` |
| README de parte | **84** | uno por carpeta, generado desde las clases |
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

La [auditoría de diferencias](AUDITORIA_DIFERENCIAS_800_CLASES.md) inspecciona duplicación y proximidad editorial. Los 840 archivos y las 840 preguntas son distintos. Fase III conserva 120 preguntas, condiciones críticas y gráficas propias sin explicaciones largas no autorizadas repetidas en más de diez clases; Fase IV añade 40 archivos, preguntas, condiciones y gráficas distintas. El corpus tiene una mediana de **2.895 palabras por clase**. Longitud y unicidad verbal describen escala editorial; no demuestran calidad o aprendizaje.

## 3. Talleres, rutas y portafolio

| Superficie | Resultado actual |
|---|---:|
| Talleres verticales | **10** |
| Sesiones integradoras | **60** |
| Fases por taller | **6**: diagnóstico, investigación, alternativas, crítica, revisión y defensa |
| Rutas con diagnóstico, checkpoints, salida y capstone | **35/35** |
| Dimensiones de la rúbrica común | **5** |
| Umbral documental | **80/100**, ninguna dimensión bajo 60 % |
| Fichas de la biblioteca de catástrofes | **15** (2 `CONFIRMADO` como contenido de fuente técnica leída; el resto `PRELIMINAR`) |
| Afirmaciones normativas verificadas | **25** en `data/verificacion.json` (seguros, liquidación de siniestros y diseño sísmico) |
| Fuentes vigiladas | **17** en `data/vigilancia.json` |
| Cronología de 2026 | enero (calor e incendios), marzo (río atmosférico), julio (sistema frontal), agosto (frontal en Antofagasta y tornado), septiembre y octubre (pronósticos), escasez hídrica y tormentas eléctricas; se incorporan las marejadas, el tornado de Diguillín y las lluvias altiplánicas al leer su fuente |
| Pilotos con estudiantes | **pendiente** |
| Carga horaria observada | **pendiente** |

## 4. Fuentes y procedencia

| Superficie | Resultado |
|---|---:|
| Relaciones clase–fuente derivadas | **2.449** |
| URLs externas únicas en clases | **638** |
| Dominios externos en clases | **193** |
| Clases con apartado de fuentes | **840/840** |
| Relaciones con función declarada | **2.382/2.449** |
| Relaciones con alcance consultado | **1.995/2.449** |
| Relaciones con límite declarado | **2.244/2.449** |
| Relaciones con fecha de consulta | **1.568/2.449** |
| Relaciones contextualmente completas | **1.396/2.449** |
| Clases con todos sus usos completos | **452/840** |
| Verificación periódica de disponibilidad externa | **implementada** (`scripts/check_sources.py`, mensual; comprueba que el enlace responda, no su contenido) |
| Revisión normativa por jurisdicción | **parcial**: 25 afirmaciones (seguros, liquidación y diseño sísmico) verificadas contra texto oficial; LGUC, OGUC y NCh se leen por predio y edición |

Las 611 fichas del lector offline son un inventario histórico. `sources/bibliography.json` es el registro actual derivado de las clases y conserva los faltantes como datos explícitos, sin inventar fechas, páginas o alcances.

## 5. Publicación y artefactos

| Salida | Estado | Comprobación |
|---|---|---|
| GitHub Pages | generable | build reproducible desde Markdown y manifiestos |
| Páginas de clase | **840** | una por ARQ |
| Portadas de parte | **84** | una por bloque |
| Páginas de taller | **70** | diez portadas + 60 sesiones |
| Rutas pedagógicas | **35** | entrada, recorrido, checkpoints, salida y capstone |
| Casos domésticos aplicados | **2** | casa nueva de 80 m² y ampliación de 24 m², ambos didácticos |
| Casos de decisión y evaluación | **3** | decisión integral de construcción resiliente, evaluación técnica de inmuebles (con diez laboratorios resueltos) y biblioteca de 15 fichas de eventos |
| Presupuestos verificables | **2 CSV + 1 XLSX** | esquema, fórmulas y controles validados en CI |
| Recursos transversales del lector v1.0 | **755** | colección histórica conservada |
| Lector offline y PDF v1.0 | conservados | hashes versionados |
| Enlaces internos, UTF-8 y salidas | verificables | `scripts/validate_repo.py` |

## 6. Brechas abiertas

1. **Revisión externa por especialidades.** El programa se verifica con fuentes oficiales y con su propio estándar (véanse los [niveles de verificación](NIVELES_DE_VERIFICACION.md)); no emite ni reemplaza dictámenes. Una revisión profesional independiente, si se obtiene, se registrará con alcance, fecha y revisor.
2. **Pilotos pedagógicos.** La eficacia con estudiantes no está medida; mientras tanto el programa ofrece seis instrumentos de autoverificación del aprendizaje (véanse los niveles de verificación).
3. **Carga y calendario.** No se publican horas ni créditos hasta observarlos en condiciones declaradas.
4. **Fuentes.** 1.053 usos requieren completar uno o más campos contextuales. La disponibilidad se vigila cada mes y la vigencia se revisa con la frecuencia de `data/vigilancia.json`.
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
