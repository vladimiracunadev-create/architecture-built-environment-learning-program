# Estado verificable del programa

**Corte documental: 24 de septiembre de 2026 · edición definitiva v1.0**

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

Se inspeccionaron los encabezados y el texto completo de las 680 fuentes Markdown. Los tres componentes transversales están presentes en todo el corpus; otros aparecen según la etapa y la plantilla editorial usada.

| Componente documental | Clases que lo declaran | Lectura correcta |
|---|---:|---|
| Pregunta central | **680/680** | presente en todo el programa |
| Práctica o ejercicio | **680/680** | actividad propia del tema |
| Fuentes y alcance de uso | **680/680** | apoyo y límite declarados |
| Resultado o entrega explícitos | **645/680** | 35 clases usan una formulación anterior o distribuida |
| Caso trabajado o razonado | **532/680** | no todas las clases necesitan el mismo tipo de caso |
| Autoevaluación o solución | **650/680** | cobertura amplia, no total |
| Continuidad explícita | **555/680** | el índice conserva la secuencia donde no hay bloque dedicado |
| Errores frecuentes | **284/680** | componente no uniforme |

La mediana es de **1.796 palabras por clase**; el corpus curricular supera **1,1 millones de palabras**. Longitud no equivale a calidad: estas cifras sólo describen el material que debe revisar una persona especialista.

## 3. Fuentes y procedencia

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

## 4. Publicación y artefactos

| Salida | Estado | Comprobación |
|---|---|---|
| GitHub Pages | publicada | build reproducible desde Markdown |
| Páginas de clase | **680** | una por ARQ |
| Portadas de parte | **68** | una por bloque |
| Recursos transversales | **755** | 611 fuentes, 80 roles, 36 plantillas, 16 documentos y 12 rutas |
| Lector offline | conservado | HTML autosuficiente v1.0 |
| PDF de las 20 clases finales | conservado | SHA-256 versionado |
| PDF de ARQ-680 | conservado | SHA-256 versionado |
| Enlaces internos del sitio | verificados | `scripts/validate_repo.py` |
| Codificación UTF-8 | verificada | control de mojibake en Markdown |

## 5. Qué sigue pendiente

1. **Revisión externa por especialidades.** No se ha realizado una revisión integral por arquitectura, estructuras, geotecnia, instalaciones, incendio, accesibilidad, patrimonio, costos, construcción y operación.
2. **Vigencia de fuentes externas.** El repositorio registra fuentes y límites, pero todavía no ejecuta una comprobación periódica de disponibilidad, sustitución o retiro.
3. **Uniformidad editorial.** Resultados, continuidad, errores y autoevaluación no usan todavía la misma pauta en las 680 clases.
4. **Licencias y terceros.** Código propio bajo Apache-2.0 y contenido original bajo CC BY-NC-SA 4.0. Las obras externas conservan sus derechos y requieren revisar sus términos antes de reutilizarlas.
5. **Lector offline histórico.** Conserva documentos de etapas anteriores. Cuando una afirmación histórica contradice el estado actual, este documento y las fuentes Markdown actuales prevalecen como marcador de estado.
6. **Accesibilidad especializada.** El sitio usa HTML semántico, navegación por teclado y diseño adaptable; no cuenta aún con auditoría WCAG externa.

## Cómo reproducir la comprobación

```bash
python scripts/generate_curriculum_docs.py
python scripts/build_bibliography.py
python scripts/build_site.py
python scripts/validate_repo.py
```

El CI ejecuta el build y la validación en cada push y pull request. Que el CI esté en verde demuestra que las comprobaciones automatizadas pasaron; no demuestra corrección disciplinar de cada clase.
