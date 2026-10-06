# Roadmap integral del programa

**Última actualización:** 6 de octubre de 2026 · **Edición activa:** 2026.10

Este documento conserva el alcance general, el método de trabajo y las condiciones de cierre. Evita que una futura ampliación olvide áreas, duplique clases o declare resuelto algo que necesita evidencia externa.

## Principio rector

> Mejorar sin romper. Profundizar sin duplicar. Ampliar sin perder lo que ya existe.

El orden obligatorio es:

```text
DESCUBRIR → INVENTARIAR → AUDITAR → MAPEAR → REUTILIZAR
→ DETECTAR BRECHAS → PROFUNDIZAR → INTEGRAR → VALIDAR → DOCUMENTAR
```

No se inicia una expansión creando títulos. Primero se actualiza la [matriz de cobertura](docs/MATRIZ_COBERTURA_INTEGRAL.md), se identifica la evidencia existente y se decide si corresponde conectar, profundizar, corregir o crear.

## Estado del alcance general

| Frente | Estado | Evidencia actual | Cómo se resuelve o mantiene | Condición de cierre |
|---|---|---|---|---|
| Fundamentos, teoría e historia | implementado | Partes 01, 05–10 | conservar secuencia; ampliar sólo casos o perspectivas faltantes | revisión externa por historia y teoría |
| Chile y Latinoamérica | implementado con brecha | Parte 09 y conexiones territoriales | añadir casos regionales con fuentes primarias y voces autorizadas | muestra equilibrada por macrozona y revisión local |
| Representación y maquetas | implementado y ampliado | Partes 02, 66, 71 y 74 | incorporar visuales originales y ejercicios de fabricación | recursos accesibles y prueba con estudiantes |
| Matemática y física | implementado | Partes 03 y 20–38 | mejorar recuperación diagnóstica y problemas graduados | revisión disciplinar y pilotaje de dificultad |
| Estructuras y geotecnia | implementado | Partes 19–21 y 35 | conservar frontera profesional; añadir casos de falla documentados | revisión por ingeniería estructural y geotecnia |
| Materiales y construcción | implementado y ampliado | Partes 22–27, 39, 74 y 77 | sumar ensayos, muestras y datos regionales cuando existan | protocolo presencial y revisión de seguridad |
| Instalaciones | implementado | Partes 31–34 | actualizar referencias por jurisdicción y conectar con tipologías | revisión sanitaria, eléctrica, mecánica e incendio |
| Tipologías | implementado | Partes 15–17 y 49–67 | profundizar según demanda sin duplicar sistemas comunes | revisión sectorial por muestras |
| Infraestructura | implementado y ampliado | Partes 54–57, 62, 67 y 76 | modelar redes, dependencias, nivel de servicio y continuidad | revisión arquitectura–ingeniería–territorio |
| Urbanismo, paisaje y territorio | implementado y ampliado | Partes 11–13 y 75–77 | incorporar datos locales, participación y efectos distributivos | piloto territorial con consentimiento |
| Sostenibilidad y ciencia del edificio | implementado y ampliado | Partes 27–30, 32, 45 y 77 | mantener fronteras y actualizar clima/factores | medición real y revisión de modelos |
| Riesgos y resiliencia | implementado | Partes 35–38, 76 y 80 | mantener foco chileno y dependencias críticas | simulacro o caso validado con actores competentes |
| Patrimonio y reutilización | implementado y ampliado | Partes 46 y 78 | ampliar casos locales, HBIM y seguimiento de intervención | revisión patrimonial y de compatibilidad |
| BIM y openBIM | implementado | Partes 44, 72–74 | añadir archivos de intercambio y pruebas entre herramientas | conjunto de prueba reproducible |
| Diseño computacional | implementado y ampliado | Parte 72 | publicar ejercicios ejecutables y pruebas | repositorio de código con resultados reproducibles |
| Inteligencia artificial | implementado y ampliado | Partes 44 y 73 | evaluar usos por versión, datos, riesgo, supervisión y retiro | benchmark documentado y revisión independiente |
| Legislación y normativa | implementado con mantenimiento continuo | Parte 40 y fuentes chilenas distribuidas | revisar únicamente fuentes oficiales con fecha y jurisdicción | revisión periódica; nunca se marca cerrada permanentemente |
| Economía, negocio y gestión | implementado y ampliado | Partes 41–43 y 70 | añadir casos contractuales y económicos fechados | revisión profesional y jurídica |
| Práctica profesional | implementado y ampliado | Partes 48 y 70 | simular reuniones, propuestas, negociación y control documental | evaluación por profesional en ejercicio |
| Investigación | implementado y ampliado | Partes 04, 48 y 69 | añadir datasets y protocolos docentes | tesis piloto reproducible y revisión ética |
| Personas, sociedad y accesibilidad | implementado y ampliado | Partes 04, 18, 75 y 79 | coevaluar con personas y comunidades bajo consentimiento | evidencia de participación y correcciones incorporadas |
| Taller vertical y proyectos | implementado y ampliado | EST-01–10 | pilotar carga, crítica, iteración y transferencia | resultados de cohortes y ajustes documentados |
| Evaluación y portafolio | implementado | rúbrica, evidencias y talleres | medir fiabilidad entre evaluadores y calidad de retroalimentación | piloto con doble corrección |
| Rutas de especialización | implementado | 33 rutas | revisar solapamientos sin duplicar clases | diagnóstico, capstone y salida comprobados por ruta |
| Glosario | implementado con mantenimiento continuo | `docs/GLOSARIO_ACUMULATIVO.md` | añadir sólo términos conectados a clases y relaciones | revisión terminológica por disciplina |
| Fuentes y trazabilidad | implementado con brecha conocida | 2.179 usos; 1.126 completos | completar alcance, límite, fecha y función sin inferir datos | 100 % de usos contextualmente completos |
| Recursos visuales | parcial | diagramas de dependencia y visuales distribuidos | priorizar sección, detalle, mapa y comparación que enseñen | auditoría visual y accesibilidad |
| Revisión externa | pendiente | estado publicado como pendiente | muestra estratificada por especialidad y riesgo | revisores, alcance, fecha y cambios registrados |
| Pilotos pedagógicos | pendiente | arquitectura de evaluación definida | ejecutar cohortes pequeñas y medir tiempo, errores y transferencia | informe de resultados y decisiones de revisión |

## Plan por horizontes

### Horizonte A — integridad automática

Objetivo: impedir regresiones de estructura y navegación.

- derivar conteos desde `data/program.json`;
- comprobar identificadores, partes, talleres, rutas y fuentes;
- comprobar enlaces internos, UTF-8, archivos huérfanos y salidas del sitio;
- distinguir marcadores actuales de artefactos históricos;
- publicar el resultado en CI.

**Evidencia de cierre:** todos los comandos de validación terminan con código 0 y el diff generado es reproducible.

### Horizonte B — coherencia pedagógica

Objetivo: comprobar que cada clase justifica su existencia y se conecta con el recorrido.

- revisar preguntas, resultados, práctica, evidencia y aceptación;
- auditar prerrequisitos y dependencias;
- detectar títulos o contenidos redundantes;
- medir párrafos repetidos, sustancia propia y pares cercanos con la [auditoría de diferencias](docs/AUDITORIA_DIFERENCIAS_800_CLASES.md);
- reescribir primero las partes 61–62 y 65–66, y luego 49–60, mediante casos, mecanismos, evidencias y gráficas propias;
- revisar que la dificultad aumente entre fases;
- comprobar que las rutas reutilicen el núcleo.

**Evidencia de cierre:** 800 contratos válidos, sin identificadores desconocidos ni títulos duplicados; Fase III sin párrafos editoriales largos no autorizados repetidos en más de diez clases; y revisión manual documentada de las familias históricas priorizadas.

### Horizonte C — profundidad disciplinar

Objetivo: contrastar afirmaciones, casos, métodos y fronteras con especialistas.

- seleccionar muestras por área, nivel y consecuencia de error;
- registrar revisor, alcance, fecha, objeción y corrección;
- priorizar estructura, geotecnia, incendio, instalaciones, normativa, accesibilidad y salud;
- conservar desacuerdos y asuntos abiertos.

**Evidencia de cierre:** actas de revisión y cambios trazables; no basta una aprobación informal.

### Horizonte D — validación con estudiantes y usuarios

Objetivo: medir si la arquitectura documental produce aprendizaje y transferencia.

- pilotar diagnósticos, clases, talleres y recuperación espaciada;
- registrar tiempo, abandono, errores, calidad de evidencia y cambios entre versiones;
- probar accesibilidad con personas diversas;
- ajustar carga sin inventar equivalencias académicas.

**Evidencia de cierre:** informe de piloto, datos anonimizados, límites y cambios aplicados.

### Horizonte E — vigencia y mantenimiento

Objetivo: sostener un programa vivo sin convertir disponibilidad web en validez.

- comprobar enlaces de forma separada de CI determinista;
- revisar normas y legislación por fuente oficial, versión y fecha;
- actualizar herramientas sólo cuando cambie el principio transferible o el flujo de trabajo;
- revisar temas emergentes sin desplazar fundamentos;
- publicar una nueva entrada del informe sin reescribir historia.

**Evidencia de cierre:** revisión fechada, diferencias registradas y fuente oficial archivada por referencia cuando la licencia lo permita.

## Método para resolver una brecha

| Paso | Pregunta | Salida obligatoria |
|---:|---|---|
| 1 | ¿Dónde aparece hoy? | rutas y clases exactas |
| 2 | ¿Qué capacidad ya existe? | evidencia reutilizable |
| 3 | ¿La brecha es de ausencia, profundidad, conexión, fuente o práctica? | diagnóstico tipificado |
| 4 | ¿Puede resolverse conectando o ampliando? | decisión de no duplicación |
| 5 | ¿Qué fuente permite sostener la ampliación? | función, alcance, límite y fecha |
| 6 | ¿Qué hará el estudiante? | actividad y evidencia observable |
| 7 | ¿Qué condición crítica no puede promediarse? | criterio de aceptación |
| 8 | ¿Qué clase o proyecto reutiliza la salida? | dependencia explícita |
| 9 | ¿Qué prueba automática y revisión humana corresponden? | plan de validación |
| 10 | ¿Qué sigue abierto? | riesgo, responsable y próximo paso |

## Criterio para añadir clases

Una clase nueva debe aportar una competencia nueva, profundidad demostrable, integración necesaria, práctica significativa, caso esencial o especialización legítima. Si el contenido puede incorporarse a una clase existente sin volverla inmanejable, se amplía esa clase. Si dos clases producen la misma evidencia, se consolidan. El número 800 describe la edición actual; no es una cuota futura.

## Registro de decisiones

| Fecha | Decisión | Evidencia | Consecuencia |
|---|---|---|---|
| 2026-10-06 | preservar ARQ-001–680 como núcleo y añadir Fase III | auditoría de cobertura y solicitud de más clases y temas | numeración continua ARQ-681–800 |
| 2026-10-06 | centralizar conteos y títulos | valores repetidos en scripts, CI y docs; títulos leídos desde HTML histórico | `data/program.json` y `data/parts.json` pasan a ser canónicos |
| 2026-10-06 | ampliar de 12 a 33 rutas | lista de especializaciones y cobertura existente reutilizable | rutas especializadas sin duplicar clases |
| 2026-10-06 | añadir EST-09 y EST-10 | nuevas capacidades de investigación, prototipo y transferencia | 60 sesiones integradoras |
| 2026-10-06 | mantener artefactos v1.0 en raíz | enlaces y checksums históricos | preservación explícita; no son estado actual |
| 2026-10-06 | auditar diferencias de las 800 clases y reescribir Fase III | 800 filas comparadas; homogeneidad detectada en los primeros textos nuevos | 120 desarrollos ampliados; deuda histórica priorizada por partes |

## Documentos de control

- [Matriz de cobertura integral](docs/MATRIZ_COBERTURA_INTEGRAL.md)
- [Mapa de dependencias](docs/MAPA_DE_DEPENDENCIAS.md)
- [Arquitectura del repositorio](docs/ARQUITECTURA_DEL_REPOSITORIO.md)
- [Estado verificable](docs/ESTADO_VERIFICABLE.md)
- [Informe de integración 2026.10](docs/INFORME_INTEGRACION_2026-10.md)
- [Estándar de documentación de clase](docs/ESTANDAR_DOCUMENTACION_CLASE.md)
- [Auditoría de diferencias entre las 800 clases](docs/AUDITORIA_DIFERENCIAS_800_CLASES.md)
- [Estándar de fuentes](docs/ESTANDAR_DE_FUENTES.md)

Toda iteración futura debe actualizar este roadmap cuando cambie una prioridad, condición de cierre o brecha; los hitos históricos se agregan, no se reescriben.
