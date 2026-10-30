# Decisión integral de construcción resiliente: solución modelo

Solución modelo del [caso conductor](DECISION-INTEGRAL-RESILIENTE.md). **Los tres terrenos, las superficies, los precios en CLP, las probabilidades y las coberturas son HIPOTÉTICOS** y se eligieron para que cada uno exhiba un peligro dominante distinto; no corresponden a predios reales ni a estudios. Lo que se ejercita es el método: separar amenaza, exposición, vulnerabilidad y riesgo; aplicar una regla de puerta; y comparar costo inicial, pérdida anual esperada y escenario extremo (método de [ARQ-832](../classes/parte-84/ARQ-832.md)). Resuelve el caso por tu cuenta antes de leer esta solución.

## 1. Datos de los terrenos

Programa común: vivienda de 100 m² construidos; costo de obra hipotético de CLP 850.000/m², es decir CLP 85.000.000 (octubre de 2026, región por definir, sin IVA).

| | Terreno A | Terreno B | Terreno C |
|---|---|---|---|
| Descripción | lote urbano plano de 300 m² junto a un estero | lote en ladera de 450 m², 22 % de pendiente, quebrada contigua, acceso de 3 m | terraza alta plana de 400 m², lejos de cauces, borde de plantación forestal |
| Precio del terreno | 60.000.000 | 38.000.000 | 52.000.000 |
| Peligro dominante (a verificar) | inundación por desborde y anegamiento | remoción en masa y escorrentía concentrada | incendio de interfaz |
| Antecedentes | vecinos reportan anegamiento; sin informe hidrológico | sin estudio de suelos ni de estabilidad | CIP residencial; suelo granular con napa profunda según un sondaje existente en el entorno (no del predio) |
| Servicios | red completa | agua y luz; alcantarillado por resolver | red parcial |

## 2. Matriz multiamenaza (amenaza, exposición, vulnerabilidad, riesgo)

| Terreno | Amenaza | Exposición | Vulnerabilidad de la vivienda | Riesgo | Datos que faltan |
|---|---|---|---|---|---|
| A | inundación fluvial y pluvial | planta baja a 0,4 m sobre la calle | muros y pisos sensibles al agua; instalaciones bajas | alto para bienes y habitabilidad | informe hidrológico y de drenaje; cotas de inundación oficiales |
| B | remoción en masa; escorrentía | ladera bajo la quebrada | fundaciones y muros de contención por diseñar | alto y de consecuencias severas | estudio de mecánica de suelos y de estabilidad de la ladera |
| C | incendio de interfaz; viento asociado | borde de plantación a distancia no medida | cubierta y revestimiento combustibles si se eligen mal | medio, controlable con diseño y entorno | distancia a vegetación, acceso de bomberos, estudio de riesgo de incendio |

La columna «riesgo» es una lectura cualitativa inicial, no un cálculo. Se actualiza cuando llegan los datos que faltan.

## 3. Condiciones legales y especialistas

Para los tres: certificado de informaciones previas, instrumento de planificación territorial vigente, áreas de riesgo y restricciones (ver [ARQ-803](../classes/parte-81/ARQ-803.md)). Para A: ingeniero civil o hidráulico (drenaje e inundación). Para B: ingeniero geotécnico y de estabilidad de taludes (véase [GEOTECNIA-INFORME-Y-ENCARGO](GEOTECNIA-INFORME-Y-ENCARGO.md)). Para C: especialista en riesgo de incendio forestal y un arquitecto para la envolvente. Para la estructura de la vivienda: ingeniero calculista; para los seguros: un corredor. Una restricción legal o una condición de áreas de riesgo sin resolver **detiene** el terreno.

## 4. Opciones de emplazamiento, estructura y materiales

- **A:** subir el nivel de piso 0,6 m sobre el nivel de inundación que determine el estudio, drenaje perimetral, instalaciones en altura, materiales de baja absorción en el primer nivel.
- **B:** emplazamiento en la parte más estable que indique el estudio, contención y drenaje de ladera, fundaciones profundas si lo exige el suelo, sin cortes sin contención.
- **C:** envolvente y cubierta de materiales no combustibles, aleros y aberturas con protección de brasas, franja de gestión de vegetación, acceso para camión de bomberos y reserva de agua; véase la [matriz de materiales y amenazas](../docs/MATRIZ_MATERIALES_AMENAZAS.md).

## 5. Presupuesto por escenarios (HIPOTÉTICO)

| Concepto | A | B | C |
|---|---:|---:|---:|
| Terreno | 60.000.000 | 38.000.000 | 52.000.000 |
| Obra (100 m² × 850.000) | 85.000.000 | 85.000.000 | 85.000.000 |
| Estudios especializados | 2.800.000 | 6.500.000 | 2.200.000 |
| Mitigación | 9.500.000 | 18.000.000 | 7.000.000 |
| **Costo inicial** | **157.300.000** | **147.500.000** | **146.200.000** |

El terreno B parece el más barato por precio de terreno, pero su costo inicial supera al de C por la mitigación y los estudios; el costo inicial por sí solo no decide.

## 6. Pérdida esperada y escenario extremo

Tres escenarios de daño por terreno con probabilidades anuales **supuestas** (sin fuente; solo para practicar), sin regla proporcional y con deducible de CLP 500.000 y suma asegurada de CLP 85.000.000. Supuesto de cobertura **a verificar con un corredor**: el peligro dominante de A (inundación) y de B (remoción en masa) está sin cobertura contratada; el de C (incendio) está cubierto.

| | Escenario | Probabilidad anual | Daño | Retenido |
|---|---|---:|---:|---:|
| A | menor / severo / total | 10 % / 2 % / 0,4 % | 4.000.000 / 22.000.000 / 60.000.000 | 4.000.000 / 22.000.000 / 60.000.000 |
| B | menor / severo / total | 5 % / 1 % / 0,3 % | 6.000.000 / 35.000.000 / 93.500.000 | 6.000.000 / 35.000.000 / 93.500.000 |
| C | menor / severo / total | 3 % / 0,6 % / 0,2 % | 8.000.000 / 45.000.000 / 93.500.000 | 500.000 / 500.000 / 8.500.000 |

| | Pérdida anual esperada bruta | Pérdida anual esperada retenida | Valor presente a 20 años de la retenida (4 %) | Costo inicial + valor presente | Retención en el escenario extremo |
|---|---:|---:|---:|---:|---:|
| A | 1.080.000 | 1.080.000 | 14.677.552 | 171.977.552 | 60.000.000 |
| B | 930.500 | 930.500 | 12.645.799 | 160.145.799 | 93.500.000 |
| C | 697.000 | 35.000 | 475.661 | 146.675.661 | 8.500.000 |

Factor de anualidad a 20 años y 4 %: 13,5903. Lectura: C combina el menor costo inicial y la menor retención, **bajo el supuesto de cobertura de incendio**; A y B retienen todo el riesgo dominante. B tiene la peor retención en el escenario extremo (CLP 93.500.000, es decir, la pérdida total de la obra), que ningún promedio anual revela.

## 7. Regla de puerta y decisión

| Terreno | ¿Peligro crítico sin resolver? | ¿Restricción legal sin resolver? | ¿Pendientes que pueden cambiar la decisión? | Resultado |
|---|---|---|---|---|
| A | sí (inundación sin informe) | no hay evidencia de una | informe hidrológico, cotas, cobertura | **REDISEÑAR** si el informe permite elevar y drenar; si no, **CAMBIAR DE TERRENO** |
| B | sí (ladera sin estudio) | no hay evidencia de una | estudio de suelos y estabilidad (CLP 6.500.000 en este ejemplo) | **ESTUDIAR MÁS**; sin estudio favorable, **NO CONSTRUIR** |
| C | no hay peligro crítico documentado | no hay evidencia de una | distancia a vegetación, acceso, estudio de incendio, sondaje del predio, cobertura | **CONSTRUIR condicionado** a los pendientes |

**Decisión final del modelo:** C, condicionada. No es una puntuación: es el único terreno donde las tres preguntas de la puerta no producen un «sí» sobre un peligro crítico. A queda como alternativa si su informe permite rediseñar; B se descarta mientras no exista estudio favorable. Un puntaje promedio favorable de B por su precio de terreno no compensaría su peligro.

## 8. Riesgo residual, mantenimiento y continuidad

- **Riesgo residual en C:** el incendio no se elimina; queda la retención de CLP 8.500.000 en el escenario extremo, la dependencia de la gestión de vegetación del entorno y la pérdida de habitabilidad temporal.
- **Mantenimiento de ciclo de vida:** limpieza anual de canaletas y aleros, control de vegetación, revisión de sellos y de la reserva de agua (método de [ARQ-839](../classes/parte-84/ARQ-839.md)).
- **Plan de emergencia y continuidad:** ruta de evacuación y punto de reunión, bolso de emergencia, copias digitales de la línea base y de la póliza ([ARQ-833](../classes/parte-84/ARQ-833.md)), alternativa de alojamiento.
- **Escenario de reparación y reconstrucción:** con pérdida total, la reconstrucción exige el valor de reposición actualizado; la hoja de cobertura de ARQ-832 se revisa cada año.

## 9. Qué cambiaría la decisión

Un informe hidrológico que fije la cota de inundación de A por debajo del piso elevado y con drenaje viable; un estudio de estabilidad que declare estable la ladera de B con una contención de costo acotado; una distancia a vegetación de C menor que la que permite una franja defendible; o una cotización que excluya la cobertura de incendio en C. Cualquiera de estos hechos reabre la tabla.

## Criterios de aceptación de la carpeta

Responde la pregunta del caso (¿construir aquí, qué falta, qué alternativas, quién interviene, cuánto cuesta, qué riesgo queda, cuándo detener?), conserva estados de verificación, rotula todo monto como HIPOTÉTICO, aplica la regla de puerta por escrito, separa pérdida esperada y escenario extremo, y declara que no es un estudio de riesgo, un informe geotécnico ni una autorización de obra.
