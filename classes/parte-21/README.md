# Parte 21 — Sistemas estructurales y coordinación arquitectónica

**Fase I · formación transversal · 10 clases · ARQ-201 → ARQ-210**

Esta parte comienza con **Muros portantes y distribución del espacio** y culmina con **Coordinación entre estructura, envolvente e instalaciones**. Las diez clases forman una secuencia: cada una declara su pregunta, resultado, caso o práctica, fuentes y límites.

> Material educativo independiente. Este bloque no habilita para diseñar, calcular, firmar, autorizar ni ejecutar obras. Los parámetros de los casos no se transfieren a un proyecto real sin antecedentes, normativa y especialistas competentes.

## Problemas que articula

- **ARQ-201:** ¿Cómo organizar espacios mediante muros portantes sin confundir continuidad visual, transmisión de cargas y posibilidad de abrir o transformar esos muros?
- **ARQ-202:** ¿Qué libertad espacial ofrece un pórtico y qué condiciones deben cumplir sus uniones, columnas y sistemas de estabilidad para que esa libertad no sea solo una imagen de planta abierta?
- **ARQ-203:** ¿Cómo transforma una diagonal una fuerza horizontal en acciones axiales, y por qué dos diagonales dibujadas no equivalen necesariamente al doble de rigidez en cualquier sentido de carga?
- **ARQ-204:** ¿Cómo distinguir el trabajo de un piso bajo cargas verticales de su función como diafragma, y por qué su reparto no puede decidirse únicamente mirando la proporción del rectángulo?
- **ARQ-205:** ¿Cómo permite una cercha transmitir cargas mediante fuerzas axiales y qué se pierde al reducir su altura, introducir cargas entre nudos o ignorar sus conexiones fuera del plano?
- **ARQ-206:** ¿Cuándo una forma curva transmite una carga principalmente por compresión y qué ocurre cuando la misma geometría recibe una distribución diferente?
- **ARQ-207:** ¿Cómo depende la estabilidad de un sistema tensado de su geometría y estado de tensión, y por qué una membrana o un cable no pueden analizarse como una viga simplemente más liviana?
- **ARQ-208:** ¿Qué necesita ocurrir entre dos piezas para que trabajen conjuntamente, y por qué sumar materiales o colocar elementos prefabricados en posición no garantiza continuidad estructural?
- **ARQ-209:** ¿Cómo influyen posición y rigidez de los elementos verticales en el movimiento de un piso, y por qué una junta o un núcleo necesitan estudiarse como parte de una trayectoria completa?
- **ARQ-210:** ¿Cómo coordinar estructura, envolvente e instalaciones de modo que una alternativa que parece resolver una interferencia no cree otra ni cambie silenciosamente las hipótesis del proyecto?

## Recorrido clase a clase

| # | Clase |
|---:|---|
| 01 | [ARQ-201 · Muros portantes y distribución del espacio](ARQ-201.md) |
| 02 | [ARQ-202 · Pórticos y plantas flexibles](ARQ-202.md) |
| 03 | [ARQ-203 · Arriostramientos y diagonales](ARQ-203.md) |
| 04 | [ARQ-204 · Losas y sistemas de piso](ARQ-204.md) |
| 05 | [ARQ-205 · Cerchas, cubiertas y grandes luces](ARQ-205.md) |
| 06 | [ARQ-206 · Arcos, bóvedas y cascarones](ARQ-206.md) |
| 07 | [ARQ-207 · Estructuras tensadas y neumáticas](ARQ-207.md) |
| 08 | [ARQ-208 · Sistemas mixtos y prefabricación](ARQ-208.md) |
| 09 | [ARQ-209 · Núcleos, juntas y continuidad vertical](ARQ-209.md) |
| 10 | [ARQ-210 · Coordinación entre estructura, envolvente e instalaciones](ARQ-210.md) |

## Estado de justificación pedagógica

**Cadenas de decisión documentadas:** 10/10 clases. Cada síntesis procede de la pregunta, el resultado, la práctica, las fuentes y la vecindad curricular de la clase completa; no sustituye su narrativa.

### ARQ-201 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo organizar espacios mediante muros portantes sin confundir continuidad visual, transmisión de cargas y posibilidad de abrir o transformar esos muros?

**Posición:** Abre la Parte 21 porque plantea primero el problema «¿Cómo organizar espacios mediante muros portantes sin confundir continuidad visual, transmisión de cargas y posibilidad de abrir o transformar esos muros?». La transición desde ARQ-200 · Lectura de resultados sin delegar el juicio al software conserva métodos de evidencia y límites, pero no traslada parámetros del bloque anterior. Establece la pregunta y el producto base que ARQ-202 · Pórticos y plantas flexibles desarrollará a continuación.

**Entrada:** ARQ-200, ARQ-191 · **Salida:** ARQ-202, ARQ-204, ARQ-212.

**Evidencia:** La parte 21 abre EST-HALL-01 , un recinto ficticio de 18 m en x por 12 m en y:216 m². Para comparar trayectorias se prescribe una carga superficial de 5 kN/m² sobre su plano superior. Esa acción comparativa no incluye automáticamente el peso de muros, fundaciones o alternativas futuras.

### ARQ-202 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Qué libertad espacial ofrece un pórtico y qué condiciones deben cumplir sus uniones, columnas y sistemas de estabilidad para que esa libertad no sea solo una imagen de planta abierta?

**Posición:** Ocupa el lugar 2 de la Parte 21. Se estudia después de ARQ-201 · Muros portantes y distribución del espacio porque usa esa base para responder «¿Qué libertad espacial ofrece un pórtico y qué condiciones deben cumplir sus uniones, columnas y sistemas de estabilidad para que esa libertad no sea solo una imagen de planta abierta?». Se ubica antes de ARQ-203 · Arriostramientos y diagonales porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-201, ARQ-194 · **Salida:** ARQ-203, ARQ-204.

**Evidencia:** Se conserva EST-HALL-01:18×12 m y 5 kN/m² sobre el plano superior. HALL-PORT-01 es una alternativa a los tres muros, no una adición automática a ellos. Definiremos una retícula, un reparto gravitatorio idealizado y dos modelos de respuesta lateral con diferentes restricciones al giro.

### ARQ-203 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo transforma una diagonal una fuerza horizontal en acciones axiales, y por qué dos diagonales dibujadas no equivalen necesariamente al doble de rigidez en cualquier sentido de carga?

**Posición:** Ocupa el lugar 3 de la Parte 21. Se estudia después de ARQ-202 · Pórticos y plantas flexibles porque usa esa base para responder «¿Cómo transforma una diagonal una fuerza horizontal en acciones axiales, y por qué dos diagonales dibujadas no equivalen necesariamente al doble de rigidez en cualquier sentido de carga?». Se ubica antes de ARQ-204 · Losas y sistemas de piso porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-202, ARQ-193, ARQ-195 · **Salida:** ARQ-204, ARQ-345.

**Evidencia:** ARQ-202 mostró la importancia de los giros en los marcos. Ahora estudiaremos ARR-01 , un paño auxiliar de 4 m de ancho y 3 m de altura con una diagonal desde la esquina inferior izquierda a la superior derecha. No se ha ubicado ese paño en HALL ni se le ha asignado una acción sísmica de diseño.

### ARQ-204 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo distinguir el trabajo de un piso bajo cargas verticales de su función como diafragma, y por qué su reparto no puede decidirse únicamente mirando la proporción del rectángulo?

**Posición:** Ocupa el lugar 4 de la Parte 21. Se estudia después de ARQ-203 · Arriostramientos y diagonales porque usa esa base para responder «¿Cómo distinguir el trabajo de un piso bajo cargas verticales de su función como diafragma, y por qué su reparto no puede decidirse únicamente mirando la proporción del rectángulo?». Se ubica antes de ARQ-205 · Cerchas, cubiertas y grandes luces porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-203, ARQ-194 · **Salida:** ARQ-205, ARQ-245, ARQ-346.

**Evidencia:** Se conserva la planta de referencia EST-HALL-01 y su carga superficial de 5 kN/m². Estudiaremos franjas unidireccionales, el significado de una placa y las consecuencias de apoyos, huecos y voladizos. Las alternativas de muros y pórticos siguen siendo alternativas; no se suman sus reacciones.

### ARQ-205 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo permite una cercha transmitir cargas mediante fuerzas axiales y qué se pierde al reducir su altura, introducir cargas entre nudos o ignorar sus conexiones fuera del plano?

**Posición:** Ocupa el lugar 5 de la Parte 21. Se estudia después de ARQ-204 · Losas y sistemas de piso porque usa esa base para responder «¿Cómo permite una cercha transmitir cargas mediante fuerzas axiales y qué se pierde al reducir su altura, introducir cargas entre nudos o ignorar sus conexiones fuera del plano?». Se ubica antes de ARQ-206 · Arcos, bóvedas y cascarones porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-204, ARQ-192, ARQ-193 · **Salida:** ARQ-206.

**Evidencia:** Después de pisos y arriostramientos, construiremos CER-01 , una cercha triangular independiente de HALL. Tiene A(0,0), B(8,0) y C(4,3), en metros. A es articulación y B rodillo horizontal.

### ARQ-206 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cuándo una forma curva transmite una carga principalmente por compresión y qué ocurre cuando la misma geometría recibe una distribución diferente?

**Posición:** Ocupa el lugar 6 de la Parte 21. Se estudia después de ARQ-205 · Cerchas, cubiertas y grandes luces porque usa esa base para responder «¿Cuándo una forma curva transmite una carga principalmente por compresión y qué ocurre cuando la misma geometría recibe una distribución diferente?». Se ubica antes de ARQ-207 · Estructuras tensadas y neumáticas porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-205, ARQ-054, ARQ-194 · **Salida:** ARQ-207.

**Evidencia:** Las clases históricas estudiaron arcos como construcciones y sistemas espaciales. Ahora profundizamos su mecánica mediante ARCO-01 , un arco parabólico triarticulado de doce metros de luz y tres de flecha geométrica. Se compararán carga uniforme completa y carga uniforme solo en una mitad.

### ARQ-207 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo depende la estabilidad de un sistema tensado de su geometría y estado de tensión, y por qué una membrana o un cable no pueden analizarse como una viga simplemente más liviana?

**Posición:** Ocupa el lugar 7 de la Parte 21. Se estudia después de ARQ-206 · Arcos, bóvedas y cascarones porque usa esa base para responder «¿Cómo depende la estabilidad de un sistema tensado de su geometría y estado de tensión, y por qué una membrana o un cable no pueden analizarse como una viga simplemente más liviana?». Se ubica antes de ARQ-208 · Sistemas mixtos y prefabricación porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-206 · **Salida:** ARQ-208.

**Evidencia:** ARQ-206 estudió una forma curva comprimida. Ahora construiremos CAB-01 , un cable ideal entre apoyos a igual altura, y MEM-01 , una membrana esférica bajo presión diferencial uniforme. Son modelos independientes, no partes conectadas de HALL.

### ARQ-208 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Qué necesita ocurrir entre dos piezas para que trabajen conjuntamente, y por qué sumar materiales o colocar elementos prefabricados en posición no garantiza continuidad estructural?

**Posición:** Ocupa el lugar 8 de la Parte 21. Se estudia después de ARQ-207 · Estructuras tensadas y neumáticas porque usa esa base para responder «¿Qué necesita ocurrir entre dos piezas para que trabajen conjuntamente, y por qué sumar materiales o colocar elementos prefabricados en posición no garantiza continuidad estructural?». Se ubica antes de ARQ-209 · Núcleos, juntas y continuidad vertical porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-207, ARQ-194 · **Salida:** ARQ-209, ARQ-210, ARQ-215.

**Evidencia:** Estudiaremos MIX-01 , dos capas rectangulares idénticas de material elástico ideal, y compararemos deslizamiento libre con cooperación completa. Después examinaremos un presupuesto de tolerancias de prefabricación independiente, PRE-TOL-01 . No se asignan esos materiales a HALL ni se especifican conectores comerciales.

### ARQ-209 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo influyen posición y rigidez de los elementos verticales en el movimiento de un piso, y por qué una junta o un núcleo necesitan estudiarse como parte de una trayectoria completa?

**Posición:** Ocupa el lugar 9 de la Parte 21. Se estudia después de ARQ-208 · Sistemas mixtos y prefabricación porque usa esa base para responder «¿Cómo influyen posición y rigidez de los elementos verticales en el movimiento de un piso, y por qué una junta o un núcleo necesitan estudiarse como parte de una trayectoria completa?». Se ubica antes de ARQ-210 · Coordinación entre estructura, envolvente e instalaciones porque la evidencia producida aquí debe estar disponible para ese paso.

**Entrada:** ARQ-208, ARQ-189, ARQ-199 · **Salida:** ARQ-210, ARQ-226, ARQ-343.

**Evidencia:** Esta clase conecta pórticos, arriostramientos y diafragmas mediante DIA-01 , un piso rígido ideal con tres líneas resistentes a acciones en dirección y. No es la respuesta sísmica de HALL. Resolverás traslación, rotación y reparto de fuerzas; después estudiarás movimientos relativos de dos bordes.

### ARQ-210 · decisión sustentada

**Necesidad:** Esta clase existe para resolver una necesidad concreta del recorrido: ¿Cómo coordinar estructura, envolvente e instalaciones de modo que una alternativa que parece resolver una interferencia no cree otra ni cambie silenciosamente las hipótesis del proyecto?

**Posición:** Cierra la Parte 21: integra lo producido en ARQ-209 · Núcleos, juntas y continuidad vertical para responder «¿Cómo coordinar estructura, envolvente e instalaciones de modo que una alternativa que parece resolver una interferencia no cree otra ni cambie silenciosamente las hipótesis del proyecto?». La transición hacia ARQ-211 · Tierra como material: variabilidad y caracterización transfiere el método y la disciplina de evidencia, no los datos o parámetros particulares de esta parte.

**Entrada:** ARQ-209, ARQ-200, ARQ-208 · **Salida:** ARQ-211, ARQ-212, ARQ-216.

**Evidencia:** Esta clase cierra las partes 20 y 21. Recupera EST-HALL-01 como referencia espacial de 18×12 m y 216 m². Las alternativas de muros, pórticos y pisos son comparaciones, no un sistema combinado ya verificado.

## Cómo recorrer esta parte

1. Lee las clases en orden cuando el tema sea nuevo; la continuidad está escrita dentro de cada documento.
2. Conserva separados dato, hipótesis, cálculo, evidencia, responsabilidad y autorización.
3. Resuelve la práctica independiente antes de abrir la solución orientativa o autoevaluación.
4. Revisa el apartado **Fuentes y alcance de uso**: una referencia apoya una afirmación delimitada, no certifica el caso completo.
5. Registra toda incertidumbre que cambiaría la decisión; “desconocido” no equivale a cero, seguro ni conforme.

## Navegación

[← Parte 20](../parte-20/README.md) · [Mapa de las 80 partes](../README.md) · [Parte 22 →](../parte-22/README.md)
