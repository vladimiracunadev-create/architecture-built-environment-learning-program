# Geotecnia y sismo: leer un informe y formular el encargo

Ejercicios para [ARQ-181–190](../classes/parte-19/README.md) y [ARQ-341–350](../classes/parte-35/README.md), usados en el [caso integrador](DECISION-INTEGRAL-RESILIENTE.md). Enseñan a **interpretar** un informe de mecánica de suelos y a **formular el encargo** a quien corresponde. No son recomendaciones de cimentación ni reemplazan estudios, ensayos o cálculos de profesionales habilitados.

## Base normativa que se usa (verificada)

El diseño sísmico de edificios en Chile se rige por el Decreto Supremo 61 de 2011 del MINVU, publicado el 13 de diciembre de 2011, que deroga el DS 117 de 2010. Su texto fue leído desde LeyChile (lectura asistida de los artículos 1 a 6; el resto del texto no se leyó). Los elementos que este caso usa están registrados en [`data/verificacion.json`](../data/verificacion.json):

- **Art. 1.** El diseño sísmico debe cumplir el decreto; en lo que éste no cubre ni contradice, rige supletoriamente la NCh 433 (versión 1996 con modificación de 2009).
- **Art. 2.** No aplica a obras civiles como puentes, presas, túneles, acueductos, muelles o canales, ni a instalaciones industriales.
- **Art. 5.** La clasificación del suelo se basa en la velocidad de ondas de corte Vs30; para edificios con subterráneo la exploración llega al menos 15 m bajo la fundación; se aceptan métodos como *down-hole*, *cross-hole*, perfilaje de suspensión y ondas superficiales (SASW, MASW, ReMi) y **no** se permite estimar Vs a partir de Vp; las propiedades del suelo deben evaluarse hasta 30 m o hasta roca en conjuntos de vivienda sobre sitios de más de 8.000 m², en estructuras de cinco o más pisos y en edificios de categoría III y IV; para estructuras pequeñas de categoría III o IV (menos de 500 m² construidos, hasta dos niveles y menos de 8 m de altura) se exime la medición *in situ* a cambio de un estudio de suelos según NCh 1508 que descarte suelos problemáticos y del uso del tipo de suelo más desfavorable (E) en el método estático.
- **Art. 6.** Los tipos de suelo van de A (roca) a E; hay suelos que **no** pueden clasificarse solo por Vs30 y exigen estudios de amplificación: potencialmente licuables, susceptibles de densificación por vibración, colapsables, orgánicos, finos saturados gruesos de alto límite líquido y finos saturados muy sensibles; los sitios de topografía irregular quedan fuera de la clasificación.

**Vigilancia.** El INN publicó la norma NCh 433:2026 (registro en su tienda con fecha 26 de marzo de 2026, visto solo como resultado de búsqueda). El propio DS 61 declara que rige hasta que exista una norma técnica que el MINVU declare oficial. Si esa norma fue oficializada y cómo se relaciona con el decreto es un dato a **verificar en la edición vigente** antes de aplicar cualquier artículo; está en la [lista de vigilancia](../data/vigilancia.json).

## Ejercicio 1 · Leer un extracto de informe geotécnico (datos HIPOTÉTICOS)

Terreno de 1.800 m² para dos edificios residenciales de 4 pisos (categoría II). El informe extracto:

| Calicata | Profundidad (m) | Descripción | Observación |
|---|---:|---|---|
| C-1 | 0,0–0,6 | relleno antrópico con escombros | no controlado |
| C-1 | 0,6–2,5 | arena limosa suelta, húmeda | napa a 2,3 m al momento de la calicata (septiembre) |
| C-1 | 2,5–3,5 | arena media a gruesa, medianamente densa | — |
| C-2 | 0,0–0,3 | tierra vegetal | — |
| C-2 | 0,3–3,0 | arcilla de plasticidad media, rígida | sin napa hasta 3,0 m |

El informe concluye: «suelo de fundación apto para fundaciones superficiales con tensión admisible a definir por el calculista».

**Preguntas.**
1. ¿Qué tipos de suelo distintos hay en un mismo terreno y por qué importa?
2. ¿Qué elementos del extracto exigirían **más estudio** antes de usar esa conclusión?
3. ¿Qué cosas **no** puede deducir el propietario?
4. ¿Qué pediría al autor del informe?

**Solución razonada.**
1. Hay un relleno no controlado en C-1, una arena limosa suelta bajo napa cercana en C-1 y una arcilla rígida en C-2: dos perfiles distintos en 1.800 m² (a una distancia no declarada) sugieren variabilidad lateral que una conclusión única no refleja.
2. Una arena suelta, saturada y con napa a 2,3 m es un perfil que obliga a evaluar **licuefacción** y asentamientos; el DS 61 (art. 6) incluye los suelos potencialmente licuables entre los que requieren estudios de amplificación y no se clasifican solo por Vs30. El relleno no controlado exige remoción o tratamiento. La napa se midió en septiembre, de modo que su variación estacional (ARQ-184) es desconocida. Los edificios de cuatro pisos no llegan al umbral de cinco, pero el sitio de 1.800 m² con dos edificios exige que el especialista justifique qué exploración aplica; el art. 5 pide evaluar hasta 30 m para estructuras de cinco o más pisos y para conjuntos sobre 8.000 m², de modo que el informe debe declarar bajo qué criterio se limitó la profundidad.
3. El propietario no puede deducir que «apto para fundaciones superficiales» sea compatible con el perfil descrito, ni la tensión admisible, ni que el relleno pueda quedar. Tampoco puede afirmar que no hay riesgo de licuefacción. Eso corresponde al ingeniero geotécnico y al calculista.
4. Pedir: sondajes o ensayos adicionales (un número y profundidad justificados), medición de Vs30 con un método aceptado por el art. 5, evaluación explícita de licuefacción y asentamientos, la variación estacional de la napa, el tratamiento del relleno, la clasificación del suelo con su criterio y las limitaciones del estudio.

## Ejercicio 2 · Formular el encargo geotécnico

Redacta los **términos de referencia** del encargo de una página. La solución modelo contiene:

1. **Antecedentes:** ubicación, superficie, tipo y número de pisos de la estructura, categoría de ocupación, subterráneos previstos, cargas aproximadas informadas por el proyectista.
2. **Alcance de la exploración:** número y profundidad de sondajes o calicatas justificados con las condiciones del art. 5 (pisos, superficie del sitio, categoría, subterráneo: al menos 15 m bajo la fundación), con ensayos de laboratorio previstos (granulometría, plasticidad, humedad, densidad, etc.).
3. **Medición de Vs30:** método aceptado entre los del art. 5; la medición de Vs no puede obtenerse de Vp.
4. **Suelos especiales:** pedir que el informe declare si hay suelos de los listados en el art. 6 y, si los hay, que proponga el estudio de amplificación correspondiente.
5. **Napa y agua:** medición, estacionalidad y efecto sobre la fundación y los subterráneos.
6. **Entregables:** perfil estratigráfico, clasificación sísmica del suelo, parámetros para el diseño, recomendaciones de fundación como **alternativas a justificar por el calculista**, limitaciones y supuestos.
7. **Firma y responsabilidad:** quién suscribe, qué responsabilidad declara y qué laboratorio ejecuta los ensayos.
8. **Cronograma y costo:** rangos HIPOTÉTICOS con fecha; el costo no puede condicionar el alcance técnico mínimo.

Criterio de aceptación: otra persona debe poder leer los términos y saber qué se exploró, hasta dónde, con qué método y qué quedó fuera.

## Ejercicio 3 · Cuándo se detiene

Marca como **detención** (hasta contar con estudio) cualquiera de estas condiciones: relleno no controlado bajo la fundación; napa alta con arena suelta; suelo orgánico o colapsable; ladera o topografía irregular sin estudio de estabilidad; informe sin declaración de limitaciones; contradicción entre calicatas y conclusión. Ninguna puntuación favorable de otras variables compensa una condición de detención.

## Resultado

La evidencia es: el análisis escrito del extracto, los términos de referencia y la lista de condiciones de detención. Se evalúa con la [rúbrica común](../docs/RUBRICA_COMUN.md).
