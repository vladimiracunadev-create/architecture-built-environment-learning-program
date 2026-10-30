# Evaluación técnica de inmuebles: laboratorios resueltos

Solución modelo de los diez laboratorios de [EVALUACION-TECNICA-INMUEBLES](EVALUACION-TECNICA-INMUEBLES.md), construida con el método de las clases [ARQ-831–840](../classes/parte-84/README.md). **Los inmuebles, las superficies, las fechas y los montos en CLP son HIPOTÉTICOS**; lo que se ejercita es el método, y las reglas oficiales que se mencionan (plazos de liquidación, artículos de la ley de seguros) están registradas con su nivel de verificación en [`data/verificacion.json`](../data/verificacion.json). Resuelve cada laboratorio por tu cuenta antes de leer su solución.

Formato común: **datos → hallazgos (observación, hipótesis, verificación, derivación) → regla de puerta → nota al cliente**. En todos los casos la puerta responde tres preguntas en orden: ¿hay peligro crítico sin resolver?, ¿hay restricción legal sin resolver?, ¿hay verificaciones pendientes que podrían cambiar la decisión?

## L1 · Departamento usado de 58 m²

**Datos.** Edificio de 1996, piso 4, escritura y recepción de 58 m², avalúo de 58 m², gasto común al día. Visita de 40 minutos sin acceso a la cubierta.
**Hallazgos.** (1) Mancha de 25 × 30 cm en el cielo del baño; hipótesis: fuga del piso superior o condensación; verificación: revisión de la red por la administración y un especialista; derivar a administración y gasfíter autorizado. (2) Tablero con tapa y sin signos visibles de modificación; **no** se declara su estado: la revisión eléctrica es de un instalador autorizado. (3) Fondo de reserva sin dato: se pide el acta.
**Puerta.** Peligro crítico: no; restricción legal: no; pendientes: causa de la humedad y acta. Resultado: **condicionar**.
**Nota al cliente.** «Documentos y superficie coinciden. Hay una mancha cuya causa debe revisarse y falta el acta del fondo de reserva; no se evaluó la estructura ni las instalaciones.»

## L2 · Casa con ampliación aparentemente no regularizada

**Datos.** Casa de 72 m² recepcionados (1998), 100 m² observados, avalúo de 100 m².
**Hallazgos.** Diferencia de superficie de 28 m² sin antecedente de permiso ni recepción; el tablero es el original. Preguntas: a la DOM, ¿existen permisos posteriores a 1998 y cuál es el procedimiento aplicable? (ver los formularios de obra menor y de edificación del MINVU); a un arquitecto, ¿es regularizable y a qué costo?
**Puerta.** Restricción legal sin resolver: sí. Resultado: **derivar** y **condicionar** cualquier oferta a la respuesta de la DOM. No se escribe «regularizable» ni «ilegal».
**Efecto en seguros.** La póliza describe 72 m²; se consulta al corredor de seguros si la superficie construida real debe declararse (agravación del riesgo, art. 526: aviso dentro de cinco días desde que se conoce un aumento sustancial).

## L3 · Propiedad comercial: inspección documental

**Datos.** Local de 120 m² con recepción de destino «oficina»; funciona una clínica dental con sala de procedimientos; patente presentada en fotografía sin fecha legible.
**Matriz de coincidencia.** Destino recepcionado: oficina; uso observado: salud; antecedente de patente: incompleto. Diferencia de destino con evidencia documental incompleta.
**Preguntas.** Municipalidad: usos admitidos en la zona según el instrumento de planificación y requisitos para el uso de salud; arquitecto: exigencias de accesibilidad, evacuación e instalaciones del nuevo destino; corredor de seguros: cambio de actividad como posible agravación del riesgo.
**Puerta.** Restricción legal sin resolver: sí. Resultado: **derivar**.

## L4 · Comparación de dos terrenos

**Datos.** Terreno A, urbano plano, CIP con uso residencial y sin afectaciones, antecedentes municipales de anegamiento en la cuadra. Terreno B, ladera de 18 % de pendiente, acceso de 3 m, sin estudio de suelos.
**Hallazgos.** A: exposición a anegamiento documentada, sin medidas ni informe hidrológico. B: pendiente, escorrentía y suelo desconocidos; sin servicios.
**Puerta.** A: peligro no resuelto → **estudiar más** (informe hidrológico y de drenaje del municipio). B: peligro y suelo desconocidos → **estudiar más** con un estudio de mecánica de suelos y de estabilidad de ladera antes de cualquier oferta. Ninguno recibe «construir» por tener un promedio de factores favorable.

## L5 · Vivienda expuesta a inundaciones

**Datos.** Casa de 1 piso a 150 m de un estero, con antecedentes de anegamiento en dos inviernos según vecinos; sin póliza de inundación.
**Hallazgos.** Marcas de humedad a 40 cm del piso en un muro posterior; hipótesis: anegamiento previo; verificación: catastro municipal, mapas de amenaza oficiales y consulta a SENAPRED.
**Seguros.** Según la guía, una póliza de incendio no cubre inundación salvo adicional; se pregunta al corredor si existe cobertura y a qué costo, o se anota la retención del riesgo.
**Puerta.** Peligro sin resolver: sí → **derivar** a un especialista en drenaje; resultado comercial: condicionar. La ficha **no** afirma que la casa «no se inunda» ni que «se inunda».

## L6 · Vivienda costera con riesgo de tsunami

**Datos.** Casa a 120 m de la costa y 6 m de altura sobre el nivel del mar según el propietario (dato sin respaldo).
**Hallazgos.** Ubicación en una zona costera; ruta de evacuación sin señalizar.
**Verificación.** Cartas de inundación por tsunami del SHOA y rutas oficiales de evacuación de SENAPRED para la comuna (consultar en los sitios de ambos organismos); la cota se verifica con un levantamiento topográfico, no con el dato del propietario.
**Puerta.** Peligro sin resolver: sí. Resultado: **derivar**; la nota informa la exposición documentada por los organismos y recomienda conocer la ruta de evacuación; no concluye que la zona «sea segura».

## L7 · Casa con humedad persistente

**Datos.** Muro exterior de un dormitorio con moho y desprendimiento de pintura de 1,2 m², empeora en invierno; hay un bajante a 30 cm.
**Hallazgos.** Observación sin causa; hipótesis rotuladas: condensación, filtración desde el bajante, humedad ascendente; verificación: medición de humedad e inspección de bajante por un especialista; fotografías fechadas y croquis.
**Estimación.** Pintura y sellos: rango hipotético CLP 180.000–420.000; **no incluye** la causa, que puede multiplicar el costo.
**Puerta.** Resultado: **condicionar** a la causa; la nota separa lo visible de lo hipotético.

## L8 · Inmueble con deterioro posterior a un sismo

**Datos.** Departamento de hormigón armado de 22 años; fisura diagonal de 0,6 mm y 45 cm en un tabique que no estaba en las fotografías de enero; olor a gas descartado por la administración.
**Hallazgos.** Fisura nueva, ancho medido con regla de 0,5 mm de resolución; hipótesis: movimiento sísmico en elemento no estructural u otra causa; derivación a ingeniero civil estructural; registro de monitoreo en cuatro fechas.
**Seguros.** Aviso al corredor y a la compañía «tan pronto como sea posible» (art. 524 n.º 7); la carpeta registra línea base, fotografías y cronología (ARQ-833). Si hay liquidación, el informe debe emitirse dentro del más breve plazo y sin exceder 45 días corridos desde la denuncia (DS 1055, art. 23).
**Puerta.** Peligro posible sin evaluar: sí → **derivar**; la operación se detiene hasta contar con la evaluación.

## L9 · Reparaciones antes de arrendar

**Datos.** Departamento de 55 m²; lista: pintura de 150 m², dos griferías, sello de ventana de 12 m lineales, piso flotante de 8 m², tablero antiguo.
**Estimación.** Es el caso de ARQ-839: total de referencia de CLP 1.370.800 sin IVA con contingencia de 15 %, rango entre CLP 861.400 y CLP 1.651.000 antes de contingencia; **sin** la revisión eléctrica, que se deriva a un instalador autorizado y puede cambiar el total.
**Plan preventivo.** Canaletas y sellos: CLP 210.000 al año; el correctivo hipotético de una filtración cuesta CLP 2.794.500, con una probabilidad supuesta que cambia la conclusión (20 % frente a 5 %).
**Puerta.** Pendiente: revisión eléctrica. Resultado: **condicionar**.

## L10 · Comparación de plusvalía entre sectores

**Datos.** Departamentos de 55 m² en A (CLP 98.000.000, estación a 600 m, 35 años, ruido diurno alto) y B (CLP 86.000.000, estación a 2,4 km, 8 años, anegamiento reportado).
**Método.** Ficha de factores en cinco grupos; hipótesis comprobables («el diferencial se explica principalmente por conectividad»); sensibilidad: con un gasto extraordinario de fachada de CLP 1.200.000 a cargo del comprador, la brecha sube de CLP 12.000.000 a CLP 13.200.000.
**Límite.** La ficha no concluye cuál inmueble vale más: faltan transacciones comparables, que corresponden a una tasación. La nota al cliente distingue lo que se sabe, lo que se supone y lo que debe resolver una tasación.
**Puerta.** Pendiente: transacciones comparables y mapa oficial de anegamiento. Resultado: **condicionar**.

## Resumen de resultados de la puerta

| Laboratorio | Resultado |
|---|---|
| L1 departamento usado | condicionar |
| L2 ampliación no regularizada | derivar |
| L3 propiedad comercial | derivar |
| L4 dos terrenos | estudiar más (ambos) |
| L5 inundación | derivar |
| L6 tsunami | derivar |
| L7 humedad persistente | condicionar |
| L8 posterior a un sismo | derivar |
| L9 reparaciones antes de arrendar | condicionar |
| L10 plusvalía entre sectores | condicionar |

Ningún laboratorio termina en «continuar»: es deliberado. Para llegar a ese resultado la carpeta tendría que mostrar que las tres preguntas de la puerta se responden «no», y los datos hipotéticos de estos ejercicios dejan siempre algo sin resolver.
