# Estándar obligatorio de documentación de una clase

> **Principio rector:** una clase no es solo un tema: es una decisión sustentada.

Este documento define cómo se crea, revisa y acepta una clase del programa. No es una plantilla para rellenar mecánicamente. Es un protocolo editorial: cada sección debe contener razonamiento específico del tema, la posición curricular y las fuentes efectivamente utilizadas.

## 1. Condición mínima de existencia

Una clase sólo se justifica si puede demostrar la cadena completa:

```text
necesidad → fundamento → fuente → prerrequisitos → contenido
→ experiencia → evidencia → evaluación → resultado → continuidad
```

La cadena también debe poder recorrerse en sentido inverso. Si un resultado no conduce a una evidencia concreta, o una decisión no conduce a un fundamento y una fuente, la clase permanece editorialmente pendiente.

## 2. Preguntas que toda clase debe responder

### Qué se aprenderá

Formula una capacidad concreta. Evita usar como único resultado “comprender”, “conocer”, “aprender” o “familiarizarse”. Emplea acciones observables: identificar, diferenciar, comparar, construir, diseñar, evaluar, diagnosticar, justificar, implementar, comprobar o validar.

### Por qué existe

Explica el problema educativo, científico, técnico, profesional o práctico que quedaría sin resolver si se eliminara la clase. Repetir el título con otras palabras no es una justificación.

### Por qué está aquí

Identifica:

- capacidades anteriores que utiliza;
- razón por la que no debería aparecer antes;
- conocimiento o método que introduce;
- clases, talleres o decisiones posteriores que dependen de ella.

La simple relación `ARQ-N → ARQ-N+1` no demuestra dependencia. Debe nombrarse qué evidencia pasa de una clase a otra.

### Qué podrá hacer el estudiante

Declara resultados observables y una evidencia que otra persona pueda revisar sin explicación oral adicional. Cada resultado debe tener al menos un criterio de aceptación.

## 3. Anatomía narrativa

La clase debe poder leerse de principio a fin. Puede adaptar el orden, pero debe cubrir estas funciones:

1. **Contexto:** situación que vuelve pertinente el aprendizaje.
2. **Pregunta o problema:** decisión que no puede resolverse todavía.
3. **Posición curricular:** entrada, aporte y continuidad.
4. **Fundamentos:** conceptos y mecanismos necesarios.
5. **Desarrollo:** explicación causal, no enumeración de términos.
6. **Visualización:** sólo cuando revele relaciones difíciles de entender en texto.
7. **Caso trabajado:** aplicación situada, con datos y fronteras explícitos.
8. **Actividad:** transferencia a una situación distinta.
9. **Evidencia:** producto, procedimiento o desempeño observable.
10. **Aceptación:** condiciones específicas de suficiencia y condiciones críticas.
11. **Errores:** confusiones previsibles y forma de diagnosticarlas.
12. **Recuperación:** cómo volver a probar el aprendizaje.
13. **Continuidad:** qué evidencia recibe la siguiente clase.
14. **Fuentes:** referencias utilizadas realmente y límites de su uso.

Una tabla puede resumir relaciones, pero nunca sustituye contexto, explicación, caso, actividad o criterio.

## 4. Documentación de fuentes

### Jerarquía preferente

1. organismos oficiales y autoridades competentes;
2. normas y estándares identificados por edición;
3. universidades y centros públicos de investigación;
4. publicaciones científicas;
5. documentación técnica oficial;
6. libros académicos o profesionales reconocidos;
7. investigaciones e informes institucionales;
8. fuentes secundarias de calidad claramente identificadas.

Blogs, páginas comerciales o agregadores pueden ayudar a localizar una fuente, pero no deben sostener por sí solos una decisión crítica cuando existe una fuente primaria accesible.

### Metadatos

Registra cuando corresponda:

- autor u organismo;
- título;
- año;
- edición o versión;
- editorial;
- DOI o ISBN;
- URL oficial;
- fecha de consulta;
- vigencia o estado conocido;
- sección, capítulo, numeral o página consultada;
- clase y afirmación donde se usa.

Un DOI, ISBN o enlace localiza una obra; no explica por qué se cita.

### Relación obligatoria

Cada uso debe declarar:

```text
fuente → concepto o afirmación → decisión de la clase
→ aplicación en actividad/evidencia → límite
```

Una bibliografía acumulada al final sin esta relación se considera incompleta.

## 5. Fuentes y secuencia curricular

Una fuente disciplinar puede sustentar un concepto, un mecanismo o un criterio. La ubicación de la clase es además una decisión editorial. Para justificarla se combinan:

- requisitos cognitivos y técnicos observables;
- evidencia que produce la clase anterior;
- complejidad creciente;
- riesgos de enseñar el contenido sin su base;
- uso posterior de la evidencia producida;
- marcos educativos cuando sean pertinentes.

No se atribuye a una norma técnica la autoría de una secuencia pedagógica que el programa decidió editorialmente.

## 6. Visualizaciones

Antes de añadir un gráfico responde: **¿qué relación se entiende mejor aquí que sólo con texto?**

Usa:

- flujo para secuencias y decisiones;
- mapa conceptual para relaciones no lineales;
- línea de tiempo para cambios;
- árbol para alternativas o diagnóstico;
- matriz para cruces repetidos;
- sección o esquema técnico para relaciones espaciales;
- comparación para alternativas equivalentes.

Todo gráfico debe tener interpretación escrita, propósito y límites. Se rechazan diagramas genéricos que podrían copiarse sin cambios a otra clase.

## 7. Actividad, evidencia y evaluación

La actividad debe exigir usar el conocimiento, no repetirlo. Puede ser observación, cálculo, dibujo, modelo, expediente, crítica, simulación, prototipo o defensa.

La evidencia debe indicar:

- producto o desempeño;
- datos y supuestos;
- procedimiento reconstruible;
- alternativa comparada;
- fuente o método;
- límites;
- condición que obligaría a revisar la decisión.

La rúbrica común complementa los criterios particulares. Nunca reemplaza una condición crítica de seguridad, accesibilidad, exactitud, ética o responsabilidad.

## 8. Progresión por parte y programa

Cada README de parte debe explicar:

- problema general del bloque;
- capacidad de entrada;
- progresión de sus diez clases;
- razón de cada transición;
- evidencia acumulativa;
- condición de salida;
- relación con la parte anterior y posterior.

La auditoría global debe buscar saltos, duplicaciones, clases sobredimensionadas, clases superficiales, prerrequisitos ausentes y temas sin representación. Un título único no demuestra contenido único.

## 9. Antipatrones rechazados

- tema + descripción breve + tabla + enlaces;
- diagrama idéntico en muchas clases;
- resultado vago sin evidencia;
- fuente decorativa sin afirmación asociada;
- fuente secundaria presentada como autoridad primaria;
- norma extranjera presentada como obligación local;
- práctica genérica reutilizable en cualquier clase;
- promedio que oculta una condición crítica;
- navegación numérica presentada como progresión pedagógica;
- texto generado que no fue contrastado con la clase completa.

## 10. Estados editoriales

- **Estructurada:** posee las secciones mínimas.
- **Trazada:** relaciona fuentes, decisiones, actividad y evidencia.
- **Revisada en corpus:** fue contrastada con su texto completo y sus vecinas curriculares.
- **Revisión editorial profunda:** además se comprobaron críticamente fundamentos, fuentes, progresión y aceptación.
- **Revisión externa:** especialista competente revisó la materia; debe registrarse persona, alcance y fecha.

Los estados no son equivalentes. El repositorio debe publicar el estado real sin promover automáticamente una clase por haber ejecutado un generador.

## 11. Protocolo de modificación

1. Leer la clase completa y sus fuentes.
2. Leer al menos sus prerrequisitos y dependencias declaradas.
3. Revisar el README de la parte y la transición entre partes.
4. Identificar afirmaciones nuevas o modificadas.
5. Actualizar fuentes y alcance de uso.
6. Ajustar actividad, evidencia y aceptación si cambia la decisión.
7. Regenerar contratos, índices, bibliografía y sitio.
8. Ejecutar todos los validadores.
9. Inspeccionar el HTML de la clase y sus enlaces.
10. Registrar problema, evidencia, decisión, archivo y consecuencia esperada.

## 12. Controles automáticos obligatorios

CI comprueba, como mínimo:

- 800 identificadores consecutivos y 80 partes de diez clases;
- pregunta, resultado, práctica, errores, continuidad y fuentes;
- contrato de decisión por clase;
- prerrequisitos y dependencias existentes;
- resultados observables;
- actividad y evidencia no vacías;
- fuentes localizables con función y límite;
- índices y archivos generados sincronizados;
- enlaces internos, navegación, UTF-8 y ausencia de mojibake;
- sitio Pages reproducible.

Los controles automáticos detectan ausencia, deriva y contradicciones. No sustituyen juicio pedagógico ni revisión disciplinar.

## 13. Lista de aceptación editorial

- [ ] La necesidad no repite simplemente el título.
- [ ] La posición identifica evidencia que entra y sale.
- [ ] Los resultados son observables.
- [ ] El desarrollo explica causas, decisiones y consecuencias.
- [ ] La actividad transfiere el método a otro caso.
- [ ] La evidencia puede revisarse sin explicación oral.
- [ ] Los criterios son específicos y conservan condiciones críticas.
- [ ] Cada fuente respalda una afirmación o decisión identificada.
- [ ] Las fuentes primarias se priorizan y las secundarias se declaran.
- [ ] El gráfico, si existe, aporta una relación concreta.
- [ ] Los errores frecuentes son propios de la materia.
- [ ] La continuidad nombra qué se reutiliza después.
- [ ] Los límites profesionales, normativos y territoriales permanecen visibles.

Una clase que no satisface esta lista permanece pendiente aunque compile, tenga muchas palabras o incluya varias referencias.
