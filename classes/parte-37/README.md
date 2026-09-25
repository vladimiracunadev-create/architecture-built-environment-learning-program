# Parte 37 — Viento, tormentas, nieve, calor e incendios de interfaz

**Fase I · formación transversal · 10 clases · ARQ-361 → ARQ-370**

Esta parte comienza con **Viento: presión, succión y continuidad de fijaciones** y culmina con **Actualización del diseño ante cambio climático**. Las diez clases forman una secuencia: cada una declara su pregunta, resultado, caso o práctica, fuentes y límites.

> Material educativo independiente. Este bloque no habilita para diseñar, calcular, firmar, autorizar ni ejecutar obras. Los parámetros de los casos no se transfieren a un proyecto real sin antecedentes, normativa y especialistas competentes.

## Problemas que articula

- **ARQ-361:** ¿Cómo pasar de una condición de viento a una demanda sobre un cerramiento sin confundir velocidad, presión, fuerza, coeficientes normativos y continuidad de fijaciones?
- **ARQ-362:** ¿Cómo estudiar lluvia impulsada por viento sin confundir presión de aire, cantidad de agua incidente, penetración y funcionamiento de las capas de drenaje?
- **ARQ-363:** ¿Por qué profundidad de nieve, peso, agua equivalente y distribución de acciones no pueden tratarse como una misma magnitud al estudiar una cubierta?
- **ARQ-364:** ¿Por qué una estrategia frente a tormentas eléctricas necesita coordinar trayectorias, diferencias de potencial, sistemas y evidencia, en lugar de reducirse a colocar un dispositivo aislado?
- **ARQ-365:** ¿Cómo estudiar un espacio de refugio frente al calor sin reducir su aptitud a una temperatura promedio, a la presencia de aislamiento o a la potencia nominal de un equipo?
- **ARQ-366:** ¿Cómo estudiar pérdida de calefacción, congelación y respaldo sin confundir temperatura, energía almacenada, potencia disponible y continuidad de los servicios?
- **ARQ-367:** ¿Cómo relacionar vegetación, clima, almacenamiento y consumo sin prometer que una selección de especies o un depósito mayor resuelve por sí solo la falta de agua?
- **ARQ-368:** ¿Cómo examinar el contacto entre edificación y vegetación sin reducir el incendio de interfaz a una distancia única, un material aislado o una sola trayectoria de propagación?
- **ARQ-369:** ¿Cómo estudiar dos amenazas o una amenaza y una interrupción de suministro sin asumir independencia, duplicar consecuencias ni convertir los resultados de varios ejemplos en un único edificio ficticio?
- **ARQ-370:** ¿Cómo actualizar un proyecto frente a información climática cambiante sin reemplazar el análisis por un único factor de incremento ni confundir una sensibilidad didáctica con una proyección local?

## Resultados y continuidad declarados

| Clase | Resultado o entrega principal |
|---|---|
| [ARQ-361](ARQ-361.md) | La parte 37 comienza con VIE-PRES-01, un modelo ideal de presión sobre una superficie.  |
| [ARQ-362](ARQ-362.md) | Construirás dos modelos separados: LLV-FLUJO-01, transporte uniforme de gotas idealizadas, y LLV-BAL-01, balance de agua en un cerramiento ficticio.  |
| [ARQ-363](ARQ-363.md) | Resolverás NIE-MASA-01, dos capas ficticias de distinta densidad, y NIE-VIGA-01/02, modelos independientes de distribución de carga.  |
| [ARQ-364](ARQ-364.md) | Estudiarás un circuito matemático R–L independiente, RAY-RL-01, para distinguir corriente máxima y rapidez de cambio.  |
| [ARQ-365](ARQ-365.md) | Derivarás EXT-TERM-01, un recinto térmico ideal de un nodo, y compararás cambios de capacidad, ganancias y conductancia.  |
| [ARQ-366](ARQ-366.md) | EXT-FRIO-01 mantiene C=3,60 MJ/K y H=100 W/K del nodo anterior, pero cambia explícitamente exterior, temperatura inicial y condiciones de servicio.  |
| [ARQ-367](ARQ-367.md) | Desarrollarás SEQ-PAISAJE-01, un presupuesto de agua para una superficie vegetal ficticia, y SEQ-DEPOSITO-01, su continuidad durante tres intervalos.  |
| [ARQ-368](ARQ-368.md) | Construirás IFZ-REL-01, un grafo de exposición hipotética, y IFZ-CONTEO-01, un registro simulado de partículas depositadas.  |
| [ARQ-369](ARQ-369.md) | Recuperamos TER-SERV-01 de ARQ-357 y PLU-BASE-01 de ARQ-353, cada uno en su propia frontera.  |
| [ARQ-370](ARQ-370.md) | Esta clase cierra las partes36 y37.  |

## Recorrido clase a clase

| # | Clase |
|---:|---|
| 01 | [ARQ-361 · Viento: presión, succión y continuidad de fijaciones](ARQ-361.md) |
| 02 | [ARQ-362 · Lluvia impulsada por viento y filtraciones](ARQ-362.md) |
| 03 | [ARQ-363 · Nieve, hielo y acumulaciones](ARQ-363.md) |
| 04 | [ARQ-364 · Tormentas eléctricas y coordinación de protección](ARQ-364.md) |
| 05 | [ARQ-365 · Calor extremo y refugio térmico](ARQ-365.md) |
| 06 | [ARQ-366 · Frío extremo y continuidad de servicios](ARQ-366.md) |
| 07 | [ARQ-367 · Sequía, vegetación y disponibilidad de agua](ARQ-367.md) |
| 08 | [ARQ-368 · Incendio de interfaz urbano-forestal](ARQ-368.md) |
| 09 | [ARQ-369 · Amenazas combinadas y falla de suministros](ARQ-369.md) |
| 10 | [ARQ-370 · Actualización del diseño ante cambio climático](ARQ-370.md) |

## Cómo recorrer esta parte

1. Lee las clases en orden cuando el tema sea nuevo; la continuidad está escrita dentro de cada documento.
2. Conserva separados dato, hipótesis, cálculo, evidencia, responsabilidad y autorización.
3. Resuelve la práctica independiente antes de abrir la solución orientativa o autoevaluación.
4. Revisa el apartado **Fuentes y alcance de uso**: una referencia apoya una afirmación delimitada, no certifica el caso completo.
5. Registra toda incertidumbre que cambiaría la decisión; “desconocido” no equivale a cero, seguro ni conforme.

## Navegación

[← Parte 36](../parte-36/README.md) · [Mapa de las 68 partes](../README.md) · [Parte 38 →](../parte-38/README.md)
