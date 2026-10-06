# Método y alcance

## Qué es este programa

Una malla educativa secuencial de **800 clases en 80 partes**, complementada por **diez talleres verticales con 60 sesiones** y 33 rutas verificables. Integra historia, representación, personas, territorio, estructuras, materiales, instalaciones, gestión, patrimonio, operación, tipologías complejas, investigación, práctica profesional y tecnologías contemporáneas.

La unidad de trabajo es la clase Markdown. Las 800 clases son la fuente editorial; los índices de parte y GitHub Pages son superficies de acceso derivadas. La estructura completa puede recorrerse desde el [índice curricular](../classes/README.md).

Cada clase busca que el estudiante pueda:

1. formular una pregunta central;
2. distinguir datos, hipótesis y evidencia;
3. reconstruir un caso trabajado;
4. resolver una práctica independiente;
5. declarar qué conclusión está respaldada y cuál excedería el modelo;
6. identificar la disciplina, el documento o la autoridad que debe intervenir.

## Arquitectura pedagógica

El programa avanza en tres fases:

1. **Fase I, fundamentos transversales (ARQ-001–480):** desarrolla lenguaje, representación, historia, territorio, desempeño, sistemas, coordinación y gestión.
2. **Fase II, tipologías y obras complejas (ARQ-481–680):** aplica preguntas y métodos a vivienda, salud, transporte, cultura, industria, infraestructura, educación y casos integradores.
3. **Fase III, profundización, especialización e innovación responsable (ARQ-681–800):** amplía investigación, práctica, representación avanzada, computación, IA, fabricación, política urbana, infraestructura, adaptación, reutilización, cuidados y entornos extremos.

La secuencia no pretende que una clase agote un tema. Cada parte organiza diez clases y cada índice de parte extrae sus preguntas centrales, resultados y enlaces reales. Las [rutas de aprendizaje](RUTAS_DE_APRENDIZAJE.md) permiten una lectura transversal y los talleres obligan a integrar, recibir crítica, revisar y defender.

## Patrón de una clase

La cobertura efectiva combina bloques detectables y una cadena de decisión específica. Las 800 clases contienen pregunta central, práctica, fuentes, resultados, autoevaluación, errores frecuentes, continuidad, mapa visual, criterio de aceptación y recuperación; además relacionan necesidad, posición, prerrequisitos, fuentes, actividad, evidencia y continuidad. La pauta obligatoria está en el [Estándar de documentación de una clase](ESTANDAR_DOCUMENTACION_CLASE.md).

El contrato generado reconstruye elementos específicos desde la clase completa; no debe sustituir su narrativa. Un bloque cumple funciones distintas:

- la **pregunta central** delimita el problema;
- los **resultados** expresan lo que debería poder producir o justificar el estudiante;
- el **caso** muestra el método en una situación acotada;
- la **práctica** obliga a transferirlo a otra situación;
- la **autoevaluación** permite contrastar el razonamiento;
- los **errores frecuentes** hacen visibles fallos de método;
- las **fuentes** permiten rastrear conceptos y límites;
- la **continuidad** conecta la clase con la secuencia.
- el **mapa visual** hace explícita la relación concreta entre prerrequisitos, fuentes, actividad, evidencia y continuidad;
- el **criterio de aceptación** transforma una tarea en desempeño observable;
- la **recuperación** comprueba que el método puede reconstruirse después de la lectura.

Las fuentes canónicas son `data/pedagogy.json`, los cinco pilotos de `data/pedagogical-decisions.json` y el manifiesto reproducible `data/pedagogical-decisions-generated.json`. `scripts/build_pedagogical_decisions.py --check` y `scripts/apply_pedagogy.py --check` impiden que clases, decisiones, talleres y rutas se desincronicen.

## Método de evidencia

Una referencia se usa para respaldar una afirmación concreta y debe interpretarse según su naturaleza:

- una norma o guía puede describir un criterio dentro de su jurisdicción;
- un organismo público puede aportar datos, definiciones o procedimientos;
- una universidad o manual técnico puede explicar un mecanismo;
- un caso editorial puede demostrar un proceso sin constituir una especificación construible.

El programa separa procedencia, interpretación y uso didáctico. La existencia de un enlace no demuestra por sí sola actualidad, suficiencia ni aplicabilidad local. El inventario y las limitaciones se detallan en [Fuentes y evidencia](FUENTES_Y_EVIDENCIA.md).

## Escala de conclusiones

Cada actividad debería permitir distinguir cuatro niveles:

1. **Observación:** qué muestran los datos o el documento.
2. **Inferencia:** qué explicación es razonable bajo hipótesis declaradas.
3. **Decisión didáctica:** qué opción se explora para aprender y comparar.
4. **Decisión profesional:** qué requiere responsables habilitados, normativa vigente, coordinación y validación específica.

Saltar del primer nivel al cuarto es un error de alcance, aunque el cálculo intermedio sea correcto.

## Qué no es

Este material no es una carrera acreditada, licencia profesional, norma técnica, cálculo firmado, permiso ni instrucción para ejecutar obras. Los casos numéricos son didácticos salvo atribución explícita. Una fuente internacional puede explicar un mecanismo sin convertirse en exigencia chilena.

## Regla de transferencia

Entre tipologías se transfieren **preguntas, mecanismos y métodos**, no parámetros. Una casa no hereda caudales hospitalarios; una escuela no hereda anchos aeroportuarios; un centro de datos no hereda criterios de ocupación de una torre.

Antes de transferir un criterio se debe revisar, como mínimo, función, usuarios, escala, clima, sitio, sistema constructivo, fase del proyecto, jurisdicción y consecuencias de fallo.

## Formas de uso

El repositorio admite cuatro modos documentados:

- **secuencial**, clase por clase;
- **por ruta**, para profundizar un eje temático;
- **por rol u oficio**, para conectar entregables y responsabilidades.
- **por taller vertical**, para producir, recibir crítica, revisar y defender una integración.

Las instrucciones y ritmos sugeridos están en [Cómo usar el programa](COMO_USAR_EL_PROGRAMA.md). El mapa de responsabilidades está en [Roles y oficios](ROLES_Y_OFICIOS.md) y la integración entre especialidades en [Casos integradores](CASOS_INTEGRADORES.md).

## Estado editorial

La redacción de la malla y la arquitectura pedagógica documental están completas. La efectividad con estudiantes, la carga real y la revisión externa por especialidades continúan siendo etapas independientes. La evolución recomendada es pilotar rutas y talleres, auditar clases de alto riesgo, actualizar normas y fuentes y producir segundas ediciones cuando la evidencia lo justifique.

“Completa” se refiere únicamente a que existen las 800 fichas planificadas para la edición 2026.10. No significa homogeneidad total, acreditación, certificación, validación normativa ni revisión externa. Las cifras actuales, el método para reproducirlas y las brechas conocidas se mantienen en [Estado verificable](ESTADO_VERIFICABLE.md).

## Fuentes de verdad del repositorio

- `data/program.json` y `data/parts.json`: edición, conteos, fases y títulos canónicos.
- `classes/`: contenido editorial de las clases.
- `docs/ESTANDAR_DOCUMENTACION_CLASE.md`: regla obligatoria de creación, revisión y aceptación.
- `data/pedagogical-decisions-generated.json`: cadena específica de decisión de las 800 clases.
- `classes/README.md` y `classes/parte-XX/README.md`: navegación curricular generada.
- `docs/ESTADO_VERIFICABLE.md`: estado documental actual y brechas.
- `scripts/generate_curriculum_docs.py`: generación de índices curriculares.
- `scripts/build_site.py`: transformación de Markdown y catálogo a HTML.
- `scripts/validate_repo.py`: controles reproducibles de estructura, cobertura, enlaces, codificación y artefactos.
- Los archivos con sufijo `v1.0` conservan el contexto de una entrega histórica; no sustituyen el estado actual.
