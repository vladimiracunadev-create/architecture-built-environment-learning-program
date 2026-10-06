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
| `classes/` | 800 clases y 80 portadas de parte |
| `studios/` | 10 talleres verticales y 60 sesiones |
| `learning-paths/` | 33 recorridos con entrada, salida y capstone |
| `docs/` | método, auditoría, cobertura, evaluación, derechos y mantenimiento |
| `data/` | manifiestos canónicos y registros pedagógicos |
| `sources/` | bibliografía derivada y su estado de trazabilidad |
| `scripts/` | importación histórica, generación, auditoría, build y validación |
| `site/` | portal estático reproducible para GitHub Pages |
| `templates/` y `evidence/` | instrumentos y convención de entregas del estudiante |
| `.github/workflows/` | gates de coherencia y publicación |

## Artefactos históricos en la raíz

Los archivos con sufijo `v1.0`, `INDICE_680_CLASES_v1.0.md`, `STATUS_v1.0.json`, el lector HTML y los PDF son fotografías de la entrega histórica de 680 clases. Se conservan en sus rutas originales para no romper enlaces ni checksums. No son fuentes de verdad del programa actual. `data/program.json` declara explícitamente esta frontera.

## Flujo de modificación

1. Modificar una fuente canónica o una clase.
2. Regenerar bibliografía y decisiones.
3. Aplicar la capa pedagógica.
4. Regenerar índices y sitio.
5. Ejecutar auditoría, validación y comprobación de deriva.
6. Revisar el diff y mantener separadas las referencias históricas.

Los comandos canónicos están en [Estado verificable](ESTADO_VERIFICABLE.md).
