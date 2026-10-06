# Parte 20 — Mecánica y comportamiento estructural

**Fase I · formación transversal · 10 clases · ARQ-191 → ARQ-200**

Esta parte comienza con **Camino de cargas y continuidad hasta el terreno** y culmina con **Lectura de resultados sin delegar el juicio al software**. Las diez clases forman una secuencia: cada una declara su pregunta, resultado, caso o práctica, fuentes y límites.

> Material educativo independiente. Este bloque no habilita para diseñar, calcular, firmar, autorizar ni ejecutar obras. Los parámetros de los casos no se transfieren a un proyecto real sin antecedentes, normativa y especialistas competentes.

## Problemas que articula

- **ARQ-191:** Si una cubierta recibe una carga, ¿cómo llega esa acción al terreno? 
- **ARQ-192:** ¿Qué debe conservar un diagrama cuando reemplaza un apoyo real por fuerzas y momentos desconocidos, y cómo detectar una solución algebraica que describe un sistema incapaz de sostenerse?
- **ARQ-193:** ¿Cómo pasar de una fuerza que atraviesa una pieza a una descripción de tensión y deformación sin confundir cantidad de carga, área resistente, dirección y comportamiento del material?
- **ARQ-194:** ¿Por qué dos vigas con las mismas reacciones pueden tener momentos y deformaciones diferentes, y cómo influye la disposición de su material en esa diferencia?
- **ARQ-195:** ¿Cómo puede una pieza comprimida dejar de mantener su configuración aunque sus fuerzas estén equilibradas y la tensión media parezca pequeña?
- **ARQ-196:** ¿Qué significa que una pieza se deforme sin recuperar totalmente su forma, y por qué esa capacidad no puede resumirse diciendo que «más flexible» o «más resistente» es siempre mejor?
- **ARQ-197:** ¿Cómo construir un conjunto coherente de acciones y estados de proyecto sin sumar máximos incompatibles, confundir masa con peso o tratar una deformación impuesta como si fuera siempre una fuerza conocida?
- **ARQ-198:** ¿Por qué una fuerza oscilante puede producir una respuesta muy distinta de la que sugiere su valor estático, y qué cambia al modificar masa, rigidez o amortiguamiento?
- **ARQ-199:** ¿Qué representa realmente una malla de cálculo, y por qué aumentar el número de elementos no garantiza que el modelo describa mejor el problema que se desea resolver?
- **ARQ-200:** ¿Cómo revisar una salida de cálculo de manera que una imagen convincente, un residuo pequeño o una suma correcta no sustituyan la comprensión del modelo y de sus límites?

## Recorrido clase a clase

| # | Clase |
|---:|---|
| 01 | [ARQ-191 · Camino de cargas y continuidad hasta el terreno](ARQ-191.md) |
| 02 | [ARQ-192 · Apoyos, vínculos y diagramas de cuerpo libre](ARQ-192.md) |
| 03 | [ARQ-193 · Tracción, compresión y cortante](ARQ-193.md) |
| 04 | [ARQ-194 · Flexión, rigidez y deformaciones](ARQ-194.md) |
| 05 | [ARQ-195 · Pandeo y estabilidad](ARQ-195.md) |
| 06 | [ARQ-196 · Elasticidad, plasticidad y ductilidad](ARQ-196.md) |
| 07 | [ARQ-197 · Acciones permanentes, variables y excepcionales](ARQ-197.md) |
| 08 | [ARQ-198 · Dinámica, período, amortiguamiento y resonancia](ARQ-198.md) |
| 09 | [ARQ-199 · Modelos, discretización y error de idealización](ARQ-199.md) |
| 10 | [ARQ-200 · Lectura de resultados sin delegar el juicio al software](ARQ-200.md) |

## Estado de justificación pedagógica

**Cadenas de decisión documentadas:** 10/10 clases. Cada síntesis procede de la pregunta, el resultado, la práctica, las fuentes y la vecindad curricular de la clase completa; no sustituye su narrativa.

### ARQ-191 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: Si una cubierta recibe una carga, ¿cómo llega esa acción al terreno? Nombrar vigas, pilares y fundaciones no responde todavía.

**Posición:** Abre la Parte 20 porque plantea primero el problema «Si una cubierta recibe una carga, ¿cómo llega esa acción al terreno? Nombrar vigas, pilares y fundaciones no responde todavía.». La transición desde ARQ-190 · Interpretación crítica de un informe geotécnico conserva métodos de evidencia y límites, pero no traslada parámetros del bloque anterior. Establece la pregunta y el producto base que ARQ-192 · Apoyos, vínculos y diagramas de cuerpo libre desarrollará a continuación.

**Entrada:** ARQ-190 · **Salida:** ARQ-192, ARQ-194, ARQ-201.

**Evidencia:** 1. Identificar y delimitar las condiciones necesarias para responder la pregunta central de camino de cargas y continuidad hasta el terreno. 2.

### ARQ-192 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Qué debe conservar un diagrama cuando reemplaza un apoyo real por fuerzas y momentos desconocidos, y cómo detectar una solución algebraica que describe un sistema incapaz de sostenerse?

**Posición:** Ocupa el lugar 2 de la Parte 20. Se estudia después de ARQ-191 · Camino de cargas y continuidad hasta el terreno porque usa esa base para responder «¿Qué debe conservar un diagrama cuando reemplaza un apoyo real por fuerzas y momentos desconocidos, y cómo detectar una solución algebraica que describe un sistema incapaz de sostenerse?». Se ubica antes de ARQ-193 · Tracción, compresión y cortante porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-191, ARQ-190 · **Salida:** ARQ-193, ARQ-195, ARQ-197.

**Evidencia:** ARQ-191 siguió las cargas hasta el terreno. Ahora aislaremos cuerpos y expresaremos sus restricciones. Se recupera exactamente su viga de cuatro metros, con carga uniforme de 6 kN/m y una fuerza de 8 kN situada a un metro del apoyo izquierdo.

### ARQ-193 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo pasar de una fuerza que atraviesa una pieza a una descripción de tensión y deformación sin confundir cantidad de carga, área resistente, dirección y comportamiento del material?

**Posición:** Ocupa el lugar 3 de la Parte 20. Se estudia después de ARQ-192 · Apoyos, vínculos y diagramas de cuerpo libre porque usa esa base para responder «¿Cómo pasar de una fuerza que atraviesa una pieza a una descripción de tensión y deformación sin confundir cantidad de carga, área resistente, dirección y comportamiento del material?». Se ubica antes de ARQ-194 · Flexión, rigidez y deformaciones porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-192, ARQ-025 · **Salida:** ARQ-194, ARQ-196, ARQ-199.

**Evidencia:** El diagrama de ARQ-192 entrega acciones externas. Ahora realizaremos cortes y distinguiremos esfuerzo axial, cortante, tensión normal y tensión tangencial. Resolverás una barra y una unión idealizada, con unidades coherentes, y contrastarás distintas formas de repartir una misma fuerza.

### ARQ-194 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Por qué dos vigas con las mismas reacciones pueden tener momentos y deformaciones diferentes, y cómo influye la disposición de su material en esa diferencia?

**Posición:** Ocupa el lugar 4 de la Parte 20. Se estudia después de ARQ-193 · Tracción, compresión y cortante porque usa esa base para responder «¿Por qué dos vigas con las mismas reacciones pueden tener momentos y deformaciones diferentes, y cómo influye la disposición de su material en esa diferencia?». Se ubica antes de ARQ-195 · Pandeo y estabilidad porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-193, ARQ-027 · **Salida:** ARQ-195, ARQ-200, ARQ-201.

**Evidencia:** ARQ-193 distinguió fuerza y tensión. Ahora relacionaremos equilibrio de segmentos, curvatura, rigidez flexional y desplazamiento. Se crea FLEX-01 , una viga simplemente apoyada de seis metros con carga uniforme de 4 kN/m.

### ARQ-195 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo puede una pieza comprimida dejar de mantener su configuración aunque sus fuerzas estén equilibradas y la tensión media parezca pequeña?

**Posición:** Ocupa el lugar 5 de la Parte 20. Se estudia después de ARQ-194 · Flexión, rigidez y deformaciones porque usa esa base para responder «¿Cómo puede una pieza comprimida dejar de mantener su configuración aunque sus fuerzas estén equilibradas y la tensión media parezca pequeña?». Se ubica antes de ARQ-196 · Elasticidad, plasticidad y ductilidad porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-194 · **Salida:** ARQ-196, ARQ-203, ARQ-241.

**Evidencia:** ARQ-194 relacionó flexión y desplazamiento; esta clase estudia la estabilidad de una configuración. Derivarás la carga crítica de una columna ideal articulada, analizarás sensibilidad a longitud y orientación y distinguirás desplazamiento inicial de desplazamiento adicional. PAN-01 es una columna ficticia independiente de las barras anteriores.

### ARQ-196 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Qué significa que una pieza se deforme sin recuperar totalmente su forma, y por qué esa capacidad no puede resumirse diciendo que «más flexible» o «más resistente» es siempre mejor?

**Posición:** Ocupa el lugar 6 de la Parte 20. Se estudia después de ARQ-195 · Pandeo y estabilidad porque usa esa base para responder «¿Qué significa que una pieza se deforme sin recuperar totalmente su forma, y por qué esa capacidad no puede resumirse diciendo que «más flexible» o «más resistente» es siempre mejor?». Se ubica antes de ARQ-197 · Acciones permanentes, variables y excepcionales porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-195, ARQ-193 · **Salida:** ARQ-197, ARQ-202, ARQ-235.

**Evidencia:** Hasta aquí varias expresiones utilizaron una ley elástica lineal. Esta clase separa rigidez inicial, inicio de fluencia, deformación residual, ductilidad y trabajo. Construirás una ley bilineal original, seguirás carga y descarga y calcularás áreas bajo su gráfica.

### ARQ-197 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo construir un conjunto coherente de acciones y estados de proyecto sin sumar máximos incompatibles, confundir masa con peso o tratar una deformación impuesta como si fuera siempre una fuerza conocida?

**Posición:** Ocupa el lugar 7 de la Parte 20. Se estudia después de ARQ-196 · Elasticidad, plasticidad y ductilidad porque usa esa base para responder «¿Cómo construir un conjunto coherente de acciones y estados de proyecto sin sumar máximos incompatibles, confundir masa con peso o tratar una deformación impuesta como si fuera siempre una fuerza conocida?». Se ubica antes de ARQ-198 · Dinámica, período, amortiguamiento y resonancia porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-196, ARQ-192 · **Salida:** ARQ-198, ARQ-200, ARQ-204.

**Evidencia:** Las clases anteriores estudiaron respuestas bajo datos prescritos. Ahora investigaremos de dónde proviene cada acción, cómo se organiza y qué información debe conservarse. Elaborarás un registro de acciones y tres casos ficticios; calcularás sus reacciones y analizarás una expansión térmica libre o restringida.

### ARQ-198 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Por qué una fuerza oscilante puede producir una respuesta muy distinta de la que sugiere su valor estático, y qué cambia al modificar masa, rigidez o amortiguamiento?

**Posición:** Ocupa el lugar 8 de la Parte 20. Se estudia después de ARQ-197 · Acciones permanentes, variables y excepcionales porque usa esa base para responder «¿Por qué una fuerza oscilante puede producir una respuesta muy distinta de la que sugiere su valor estático, y qué cambia al modificar masa, rigidez o amortiguamiento?». Se ubica antes de ARQ-199 · Modelos, discretización y error de idealización porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-197, ARQ-028 · **Salida:** ARQ-199, ARQ-219, ARQ-264.

**Evidencia:** ARQ-197 organizó acciones por casos. Añadiremos una dependencia temporal mediante DIN-01 , un oscilador ideal de un grado de libertad. Derivarás frecuencia natural, período y amplitud estacionaria bajo fuerza armónica.

### ARQ-199 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Qué representa realmente una malla de cálculo, y por qué aumentar el número de elementos no garantiza que el modelo describa mejor el problema que se desea resolver?

**Posición:** Ocupa el lugar 9 de la Parte 20. Se estudia después de ARQ-198 · Dinámica, período, amortiguamiento y resonancia porque usa esa base para responder «¿Qué representa realmente una malla de cálculo, y por qué aumentar el número de elementos no garantiza que el modelo describa mejor el problema que se desea resolver?». Se ubica antes de ARQ-200 · Lectura de resultados sin delegar el juicio al software porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-198, ARQ-193 · **Salida:** ARQ-200, ARQ-209, ARQ-215.

**Evidencia:** Usaremos equilibrio, elasticidad y compatibilidad de las clases anteriores para construir un modelo discreto de dos barras axiales. MEF-01 recupera, con identificador propio, el ejercicio de dos tramos de ARQ-193: cada uno mide un metro, con áreas 400 y 200 mm², E=200.000 N/mm² y fuerza final 24 kN. Su finalidad es hacer visible cada entrada, ecuación y comprobación.

### ARQ-200 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo revisar una salida de cálculo de manera que una imagen convincente, un residuo pequeño o una suma correcta no sustituyan la comprensión del modelo y de sus límites?

**Posición:** Cierra la Parte 20: integra lo producido en ARQ-199 · Modelos, discretización y error de idealización para responder «¿Cómo revisar una salida de cálculo de manera que una imagen convincente, un residuo pequeño o una suma correcta no sustituyan la comprensión del modelo y de sus límites?». La transición hacia ARQ-201 · Muros portantes y distribución del espacio transfiere el método y la disciplina de evidencia, no los datos o parámetros particulares de esta parte.

**Entrada:** ARQ-199, ARQ-194, ARQ-197 · **Salida:** ARQ-201, ARQ-210, ARQ-270.

**Evidencia:** Esta clase cierra la parte 20. Recibe EST-V191, FLEX-01/02, ACC-L/R y MEF-01 como casos diferenciados. Construirás un informe de revisión con comprobaciones reproducibles y hallazgos clasificados.

## Cómo recorrer esta parte

1. Lee las clases en orden cuando el tema sea nuevo; la continuidad está escrita dentro de cada documento.
2. Conserva separados dato, hipótesis, cálculo, evidencia, responsabilidad y autorización.
3. Resuelve la práctica independiente antes de abrir la solución orientativa o autoevaluación.
4. Revisa el apartado **Fuentes y alcance de uso**: una referencia apoya una afirmación delimitada, no certifica el caso completo.
5. Registra toda incertidumbre que cambiaría la decisión; “desconocido” no equivale a cero, seguro ni conforme.

## Navegación

[← Parte 19](../parte-19/README.md) · [Mapa de las 80 partes](../README.md) · [Parte 21 →](../parte-21/README.md)
