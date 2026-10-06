# Informe de integración y ampliación 2026.10

## Qué existía

El repositorio contenía 680 clases en 68 partes, ocho talleres con 48 sesiones, doce rutas, un catálogo JSON, una capa pedagógica reproducible, 622 fuentes únicas, un sitio estático y artefactos históricos v1.0. La base era extensa y técnicamente madura: todas las clases tenían pregunta, práctica, fuentes, evaluación y cadena de decisión; cinco clases contaban con revisión editorial manual profunda.

## Qué se conservó

- ARQ-001–680 y sus rutas permanecen con los mismos identificadores y archivos.
- Los artefactos v1.0, sus rutas y checksums se conservan como historia verificable.
- Se mantuvieron Python, Markdown, JSON, GitHub Actions y el generador del sitio.
- La rúbrica, licencias, fronteras profesionales y método de fuentes siguen vigentes.
- Las doce rutas iniciales continúan disponibles como recorridos amplios.

## Qué se reorganizó

- `data/program.json` es ahora la fuente canónica de conteos, edición y fases.
- `data/parts.json` reemplaza la dependencia impropia del lector HTML histórico para obtener títulos actuales.
- Validadores y generadores derivan conteos del manifiesto en vez de repetir 680/68/8/48/12.
- `docs/ARQUITECTURA_DEL_REPOSITORIO.md` distingue fuentes, salidas y artefactos históricos.
- `docs/MAPA_DE_DEPENDENCIAS.md` publica la cadena prerrequisito → clase → evidencia → proyecto → especialización.

## Qué se profundizó y creó

- **120 clases nuevas**, ARQ-681–800, con pregunta, propósito, resultados, explicación, contexto profesional, método, diagrama, caso, práctica guiada, ejercicio autónomo, errores, evaluación, recuperación y fuentes. Cada una declara una secuencia, evidencia, condición crítica y gráfica propias.
- **12 partes nuevas**, 69–80, que forman la Fase III de profundización, especialización e innovación responsable.
- **2 talleres nuevos**, EST-09 y EST-10, con doce sesiones adicionales.
- **21 rutas especializadas nuevas**, para un total de 33, que cubren urbanismo, paisaje, vivienda, diseño computacional, fabricación digital, bioclimática, iluminación, acústica, interiores, salud, educación, transporte, infraestructura, industria, centros de datos, sismo, resiliencia, desarrollo inmobiliario, investigación, visualización e IA.
- Matriz de cobertura integral, mapa de dependencias, glosario bilingüe y este informe.
- Auditoría reproducible de diferencias, con un registro CSV de las 800 clases, huellas de contenido, proporción de prosa propia y par más parecido dentro de cada parte.

## Duplicados evitados

Las nuevas rutas reutilizan partes existentes y no replican clases. BIM, sostenibilidad, patrimonio, estructuras, construcción y gestión conservan sus bloques; la Fase III añade profundidad donde había cobertura concentrada. La IA se amplió como especialización transversal, sin reemplazar diseño, historia, técnica o responsabilidad profesional.

## Fuentes añadidas

La expansión incorporó cinco localizadores únicos y reutilizó fuentes oficiales ya trazadas. Entre las autoridades empleadas están NIST, NASA, UN-Habitat, UNDRR, OMS, U.S. National Park Service, W3C, buildingSMART, EPA, BCN, RIBA y ARB. Cada uso nuevo declara consulta, apoyo, límite y fecha. Una ficha pública no se presenta como lectura íntegra ni como normativa chilena.

## Decisiones pedagógicas

- La Fase III exige núcleo común o evidencia equivalente.
- Cada parte añade una familia coherente de diez decisiones y un producto acumulativo.
- EST-09 comprueba investigación, datos y prototipado; EST-10 exige transferencia interdisciplinaria.
- Las 120 clases nuevas tienen entre 3.455 y 3.863 palabras bajo el conteo léxico del auditor; las 120 preguntas, condiciones críticas y gráficas temáticas son distintas y CI comprueba esa unicidad.
- Tras detectar una voz demasiado uniforme, se sustituyeron los párrafos comunes de método, contexto, errores y recuperación por desarrollos basados en los pasos, la evidencia, el caso y la condición crítica de cada clase. No quedan párrafos editoriales largos no autorizados repetidos en más de diez clases de Fase III.
- El caso común de decisión multicriterio enseña a no promediar condiciones críticas y se contextualiza en cada tema; no se presenta como algoritmo universal.

## Brechas pendientes

1. Revisión externa por especialidades y jurisdicción.
2. Pilotos con estudiantes para medir comprensión, carga, abandono y transferencia.
3. Revisión en vivo y periódica de URLs y normativa cambiante.
4. Más visuales disciplinares: plantas, cortes, mapas, detalles y datos descargables.
5. Prácticas presenciales, ensayos físicos y acceso a fabricación supervisada.
6. Coevaluación con comunidades y personas usuarias bajo consentimiento.
7. Diferenciación del núcleo anterior: 129 patrones editoriales largos todavía aparecen en más de diez clases, con prioridad en las partes 61–62, 65–66 y 49–60.

## Riesgos técnicos

- El corpus y el sitio crecen de forma significativa; el build debe vigilar tiempo y tamaño de artefacto.
- Los artefactos históricos contienen cifras de 680 clases que deben conservarse como historia, no actualizarse como estado actual.
- Las clases generadas desde una fuente editorial común requieren revisión humana continuada para evitar homogeneidad narrativa.

## Próximos pasos

Priorizar la reescritura diferencial de las partes identificadas por [`AUDITORIA_DIFERENCIAS_800_CLASES.md`](AUDITORIA_DIFERENCIAS_800_CLASES.md), una revisión externa por muestras estratificadas de las 80 partes, un piloto de EST-01, EST-06, EST-09 y EST-10, visuales originales y el registro de tiempos reales antes de publicar cargas o equivalencias académicas.
