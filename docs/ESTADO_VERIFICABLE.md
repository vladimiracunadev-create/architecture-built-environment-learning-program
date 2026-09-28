# Estado verificable del programa

**Corte documental: 28 de septiembre de 2026 · edición pedagógica 2026**

Este documento separa cinco dimensiones que no deben confundirse: integridad del currículo, cobertura pedagógica, trazabilidad de fuentes, publicación técnica y revisión profesional.

## 1. Integridad curricular

| Comprobación | Resultado actual | Fuente de verdad |
|---|---:|---|
| Identificadores consecutivos | **680/680** | `data/catalog.json`: ARQ-001 → ARQ-680 |
| Partes curriculares | **68/68** | `classes/parte-01` → `classes/parte-68` |
| Clases por parte | **10 en cada una** | validador estructural |
| Clases Markdown | **680** | `classes/parte-XX/ARQ-XXX.md` |
| README de parte | **68** | uno por carpeta, generado desde las clases |
| Clases pendientes de redacción | **0** | `STATUS_v1.0.json` |

“680/680” significa que la malla editorial prevista está redactada. No significa revisión por pares, acreditación, vigencia normativa universal ni aptitud para ejecutar una obra.

## 2. Cobertura pedagógica dentro de las clases

Se inspeccionaron los encabezados y el texto completo de las 680 fuentes Markdown. La capa común se genera desde `data/pedagogy.json` y se comprueba con `scripts/apply_pedagogy.py --check`.

| Componente documental | Clases que lo declaran | Lectura correcta |
|---|---:|---|
| Pregunta central | **680/680** | presente en todo el programa |
| Práctica o ejercicio | **680/680** | actividad propia del tema |
| Fuentes y alcance de uso | **680/680** | apoyo y límite declarados |
| Resultado o evidencia explícitos | **680/680** | producto revisable y ruta de archivo |
| Caso trabajado o razonado | **570/680** | incluye encabezados de nivel 2 y 3; no todas las clases necesitan el mismo tipo de caso |
| Mapa visual de aprendizaje | **680/680** | ciclo pregunta–método–evidencia–revisión |
| Criterio de aceptación | **680/680** | umbral y condiciones críticas visibles |
| Autoevaluación o solución | **680/680** | recuperación inmediata y diferida |
| Continuidad explícita | **680/680** | conexión con parte y portafolio |
| Errores diagnósticos | **680/680** | adaptados al tipo de clase |

El conteo reproducible por unidades separadas por espacio arroja una mediana de **2.104** por clase y aproximadamente **1,36 millones** en el corpus. Longitud no equivale a calidad: estas cifras sólo describen material que debe pilotarse y revisar una persona especialista.

## 3. Talleres, rutas y portafolio

| Superficie | Resultado actual |
|---|---:|
| Talleres verticales | **8** |
| Sesiones integradoras | **48** |
| Fases por taller | **6**: diagnóstico, investigación, alternativas, crítica, revisión y defensa |
| Rutas con diagnóstico, checkpoints, salida y capstone | **12/12** |
| Dimensiones de la rúbrica común | **5** |
| Umbral de aprobación documental | **80/100**, ninguna dimensión bajo 60 % |
| Pilotos con estudiantes | **pendiente** |
| Carga horaria observada | **pendiente** |

## 4. Fuentes y procedencia

| Superficie | Resultado |
|---|---:|
| Relaciones clase–fuente derivadas | **1.939** |
| URLs externas únicas en clases | **622** |
| Dominios externos en clases | **189** |
| Fichas editoriales navegables del lector v1.0 | **611** |
| Clases con apartado de fuentes | **680/680** |
| Entradas del registro derivado sin URL | **0** |
| Verificación periódica de disponibilidad externa | **no implementada** |
| Revisión de vigencia normativa por jurisdicción | **pendiente** |

Cada clase distingue qué se consultó, qué afirmación apoya y qué no permite concluir. `sources/bibliography.json` conecta cada URL con las clases que la usan. Las 611 fichas del lector son un inventario editorial histórico y navegable; no deben confundirse con las 622 URLs únicas derivadas del corpus actual.

## 5. Publicación y artefactos

| Salida | Estado | Comprobación |
|---|---|---|
| GitHub Pages | publicada | build reproducible desde Markdown |
| Páginas de clase | **680** | una por ARQ |
| Portadas de parte | **68** | una por bloque |
| Páginas de taller | **56** | ocho portadas + 48 sesiones |
| Rutas pedagógicas | **12** | entrada, recorrido, checkpoints, salida y capstone |
| Recursos transversales | **755** | 611 fuentes, 80 roles, 36 plantillas, 16 documentos y 12 rutas |
| Lector offline | conservado | HTML autosuficiente v1.0 |
| PDF de las 20 clases finales | conservado | SHA-256 versionado |
| PDF de ARQ-680 | conservado | SHA-256 versionado |
| Enlaces internos del sitio | verificados | `scripts/validate_repo.py` |
| Codificación UTF-8 | verificada | control de mojibake en Markdown |

## 6. Qué sigue pendiente

1. **Revisión externa por especialidades.** No se ha realizado una revisión integral por arquitectura, estructuras, geotecnia, instalaciones, incendio, accesibilidad, patrimonio, costos, construcción y operación.
2. **Pilotos pedagógicos.** La arquitectura documental existe; falta observar comprensión, abandono, tiempos, calidad de crítica y transferencia con estudiantes reales.
3. **Carga y calendario.** No se publican horas ni créditos hasta medirlos en condiciones declaradas.
4. **Vigencia de fuentes externas.** El repositorio registra fuentes y límites, pero todavía no ejecuta una comprobación periódica de disponibilidad, sustitución o retiro.
5. **Visuales disciplinares.** Todas las clases tienen mapa de aprendizaje; plantas, cortes, mapas, detalles y diagramas técnicos específicos deben ampliarse por especialidad.
6. **Licencias y terceros.** Código propio bajo Apache-2.0 y contenido original bajo CC BY-NC-SA 4.0. Las obras externas conservan sus derechos y requieren revisar sus términos antes de reutilizarlas.
7. **Lector offline histórico.** Conserva documentos de v1.0. Cuando una afirmación histórica contradice el estado actual, este documento y las fuentes Markdown actuales prevalecen como marcador de estado.
8. **Accesibilidad especializada.** El sitio usa HTML semántico, navegación por teclado y diseño adaptable; no cuenta aún con auditoría WCAG externa.

## Cómo reproducir la comprobación

```bash
python scripts/generate_curriculum_docs.py
python scripts/apply_pedagogy.py --check
python scripts/build_bibliography.py
python scripts/build_site.py
python scripts/validate_repo.py
```

El CI ejecuta el build y la validación en cada push y pull request. Que el CI esté en verde demuestra que las comprobaciones automatizadas pasaron; no demuestra corrección disciplinar de cada clase.
