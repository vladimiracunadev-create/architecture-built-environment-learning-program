# Arquitectura del repositorio

El repositorio separa fuentes canónicas, contenido editorial, salidas generadas y artefactos históricos. Esta distinción permite ampliar el programa sin editar cifras en decenas de lugares ni confundir una versión archivada con el estado actual.

```text
data/program.json ───────────────┐
data/parts.json ──────────────┐  │
data/catalog.json ─────────┐  │  │
data/pedagogy.json ─────┐  │  │  │
classes/ + studios/ ─┐  │  │  │  │
                     ▼  ▼  ▼  ▼  ▼
      decisiones · índices · bibliografía · sitio · validación
```

## Fuentes de verdad actuales

| Ruta | Responsabilidad |
|---|---|
| `data/program.json` | edición, conteos, fases y línea base histórica |
| `data/parts.json` | número y título de cada parte |
| `data/catalog.json` | identificador, título, parte y archivo fuente de cada clase |
| `data/pedagogy.json` | evaluación, talleres y rutas |
| `classes/parte-XX/ARQ-XXX.md` | contenido editorial de las clases |
| `data/pedagogical-decisions.json` | cinco pilotos con revisión editorial manual profunda |
| `data/verificacion.json` | afirmaciones normativas verificadas contra texto oficial, con nivel y clases de uso |
| `data/vigilancia.json` | fuentes oficiales vigiladas, frecuencia de revisión y dependencias |

## Salidas derivadas

| Ruta | Generador |
|---|---|
| `classes/README.md` y `classes/parte-XX/README.md` | `scripts/generate_curriculum_docs.py` |
| `data/pedagogical-decisions-generated.json` | `scripts/build_pedagogical_decisions.py` |
| bloques pedagógicos, `studios/` y `learning-paths/` | `scripts/apply_pedagogy.py` |
| `sources/bibliography.json` y `sources/README.md` | `scripts/build_bibliography.py` |
| `data/audits/class-distinctness.json` y `docs/audits/class-distinctness.csv` | `scripts/audit_class_distinctness.py --write` |
| `site/` | `scripts/build_site.py` |

Las correcciones se hacen en la fuente correspondiente y luego se regeneran las salidas. Editar una salida sin corregir su fuente produce deriva y debe fallar en CI.

## Familias del repositorio

| Carpeta o archivo | Función |
|---|---|
| `classes/` | 840 clases y 84 portadas de parte |
| `studios/` | 10 talleres verticales y 60 sesiones |
| `learning-paths/` | 35 recorridos con entrada, salida y capstone |
| `cases/` | casos domésticos y de decisión (CASA-NUEVA-80, AMPLIACION-24, evaluación de inmuebles, decisión integral) y la [biblioteca de catástrofes](../cases/catastrofes-chile/README.md) |
| `docs/` | método, auditoría, cobertura, evaluación, derechos y mantenimiento |
| `data/` | manifiestos canónicos y registros pedagógicos |
| `sources/` | bibliografía derivada y su estado de trazabilidad |
| `scripts/` | importación histórica, generación, auditoría, build y validación |
| `site/` | portal estático reproducible para GitHub Pages |
| `templates/` y `evidence/` | instrumentos y convención de entregas del estudiante |
| `.github/workflows/` | gates de coherencia y publicación |

## Artefactos históricos en la raíz

Los archivos con sufijo `v1.0`, `INDICE_680_CLASES_v1.0.md`, `STATUS_v1.0.json`, el lector HTML y los PDF son fotografías de la entrega histórica de 680 clases. Se conservan en sus rutas originales para no romper enlaces ni checksums. No son fuentes de verdad del programa actual. `data/program.json` declara explícitamente esta frontera.

## Scripts

| Script | Función | Se ejecuta en CI |
|---|---|---|
| `generate_curriculum_docs.py` | índices de clases y portadas de parte desde manifiestos y clases | `--check` |
| `apply_pedagogy.py` | contrato pedagógico de cada clase, talleres y rutas desde `data/pedagogy.json` | `--check` |
| `build_pedagogical_decisions.py` | cadena de decisión por clase desde el corpus completo | `--check` |
| `build_bibliography.py` | bibliografía derivada y trazabilidad por uso | `--check` |
| `audit_pedagogical_traceability.py` | verifica que cada cadena apunte a fuentes existentes | `--json` |
| `audit_class_distinctness.py` | duplicación y proximidad editorial | `--check` (y `--write` para actualizar) |
| `validate_homeowner_budget.py` | plantillas de presupuesto y sus pruebas aritméticas | sí |
| `validate_resilience.py` | fichas de caso, RUTA-35, registro de afirmaciones verificadas, estándar pedagógico y cálculos de la Parte 84 | sí |
| `check_sources.py` | disponibilidad de las fuentes de `data/vigilancia.json` (y de una muestra de la bibliografía) | no; se ejecuta mensualmente en `source-watch.yml` |
| `build_site.py` | portal estático | sí |
| `validate_repo.py` | coherencia global: identificadores, partes, rutas, fuentes, enlaces, UTF-8 y sitio | sí |
| `expand_curriculum.py`, `expand_homeowner_path.py`, `expand_resilience_path.py`, `import_legacy_reader.py` | ayudantes de autoría única que registran ampliaciones en los manifiestos; **no** forman parte del flujo corriente y no deben ejecutarse sobre una rama ya ampliada sin leerlos | no |

## Flujo de modificación

1. Modificar una fuente canónica o una clase (y, si hay una parte nueva, `data/program.json`, `data/parts.json` y `data/catalog.json`).
2. Regenerar en este orden, repitiéndolo hasta que `--check` no detecte cambios, porque las salidas se alimentan entre sí: `apply_pedagogy.py`, `build_pedagogical_decisions.py`, `build_bibliography.py`, `generate_curriculum_docs.py` y `audit_class_distinctness.py --write`.
3. Actualizar a mano las cifras citadas en documentos vigentes (`docs/ESTADO_VERIFICABLE.md`, README, `docs/AUDITORIA_DIFERENCIAS_800_CLASES.md`); el validador exige algunas y deriva otras de `data/`.
4. Reconstruir el sitio y ejecutar la validación completa, incluidas las comprobaciones `--check`.
5. Revisar el diff y mantener separadas las referencias históricas, que conservan sus cifras de época.

Una comprobación verde demuestra coherencia reproducible; no demuestra exactitud técnica, validación profesional ni eficacia pedagógica.

Los comandos canónicos están en [Estado verificable](ESTADO_VERIFICABLE.md).
