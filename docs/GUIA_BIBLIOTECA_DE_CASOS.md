# Guía de la biblioteca de casos de catástrofes y eventos

Cómo se registra, se actualiza y se valida un caso en [`cases/catastrofes-chile`](../cases/catastrofes-chile/README.md). La biblioteca existe para que una clase pueda apoyarse en eventos reales sin copiar titulares ni inventar cifras.

## Qué es un caso y qué no es

Un caso es una **ficha** con una fuente primaria, la fecha de su consulta y un estado de verificación para cada dato. No es un informe técnico del evento, no atribuye causas constructivas sin inspección y no compara eventos entre sí sin datos homogéneos. Las lecciones de diseño solo aparecen cuando existe evidencia sobre las edificaciones.

## Estados de verificación

| Estado | Cuándo se usa |
|---|---|
| `CONFIRMADO` | el dato figura en una fuente primaria o técnica leída; se escribe «como contenido de» la fuente |
| `PRELIMINAR` | balance parcial, fuente leída solo en resumen, o dato que cambiará |
| `HIPÓTESIS` | pregunta de investigación o conjetura razonable; nunca se presenta como hallazgo |
| `SIN_DATOS` | no se consultó o la fuente no lo informa |

Un dato con dos cifras en conflicto se registra con ambas fuentes y fechas y se marca `SIN_DATOS` o `PRELIMINAR`; no se promedia ni se elige la más conveniente.

## Capas de información

Cada comunicado se separa en **pronóstico**, **alerta o decisión**, **observación** e **impacto** (clase ARQ-834). Una ficha puede tener solo algunas capas; las celdas vacías son información.

## Fuentes aceptables

Se prefieren comunicados y documentos de SENAPRED, Dirección Meteorológica de Chile, DGA, SERNAGEOMIN, SHOA, MINVU, CONAF, CMF y municipalidades, más literatura revisada por pares. Una nota de prensa sirve para localizar la fuente primaria, no para sustituirla. Un resultado de IA nunca es una fuente. Si el documento no pudo leerse completo, la ficha lo dice («leído solo en resumen», «no pudo leerse»).

## Estructura de una ficha

Título con identificador y evento; estado general con método y fecha de consulta; tabla de fuentes con fecha del documento; sección por capa de información; tabla de campos con estado; hipótesis de investigación; clases relacionadas con un ejercicio; **límites de transferencia**. La numeración es `CAT-NNN` para eventos históricos y `CAT-AAAA-NNN` para los de un año en curso.

## Cómo agregar un caso

1. Crear `cases/catastrofes-chile/CAT-….md` con la estructura anterior.
2. Añadir una fila al registro de `cases/catastrofes-chile/README.md` con un enlace al archivo.
3. Ejecutar `python scripts/validate_resilience.py`: comprueba encabezado, estado general, estados válidos, URL de fuente, enlaces relativos, presencia de «Límites de transferencia» y que la ficha esté en el registro.
4. Si el caso respalda una clase, enlazarlo desde la clase o desde su ruta, y regenerar con el flujo de [Arquitectura del repositorio](ARQUITECTURA_DEL_REPOSITORIO.md).

## Lo que la validación no garantiza

Que pase `validate_resilience.py` significa que la ficha tiene forma correcta y enlaces vivos dentro del repositorio. No significa que la cifra sea la oficial de cierre, que la fuente diga lo que la ficha dice ni que el caso sea representativo. La lectura de las fuentes y su contraste siguen siendo trabajo editorial y, para conclusiones técnicas, de especialistas.

## Mantenimiento

No existe monitoreo automático de las fuentes ni de la vigencia de las normas. Cada ficha debe revisarse cuando la autoridad publique un informe de cierre. El registro conserva la cronología de 2026 como incompleta: faltan eventos de verano en zonas áridas, tormentas eléctricas, marejadas y sequía, porque no se encontraron fuentes oficiales de ellos en las páginas consultadas.
