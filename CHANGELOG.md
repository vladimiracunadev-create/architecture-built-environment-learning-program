# Historial de cambios

Registro de los hitos de la edición 2026.10 del programa. Las cifras de cada hito son las de su fecha y no se reescriben; el estado vigente está en [Estado verificable](docs/ESTADO_VERIFICABLE.md) y el orden de resolución de brechas en el [roadmap integral](ROADMAP_INTEGRAL.md).

## 2026-10-30 · Parte 84, resiliencia y verificación

- **840 clases en 84 partes.** Nueva Parte 84, *Evaluación de inmuebles, seguros y eventos catastróficos* (ARQ-831–840), sin renumerar ARQ-001–830. La Fase IV amplía su alcance a ARQ-801–840.
- **35 rutas.** Nueva RUTA-35, *Evaluación técnica de inmuebles para corredores de propiedades*, sobre 44 clases; extensión de riesgo y seguros en 13 rutas.
- **Casos.** Biblioteca de eventos en Chile con 15 fichas y estados de verificación; caso de decisión integral con solución modelo; caso de evaluación de inmuebles con diez laboratorios resueltos; ejercicios de geotecnia y sismo.
- **Verificación.** Registro de afirmaciones normativas contra texto oficial (`data/verificacion.json`), lista de fuentes vigiladas (`data/vigilancia.json`) con comprobación mensual (`scripts/check_sources.py`), auditoría automática de la Parte 84 contra el estándar de documentación y recálculo de las cifras didácticas (`scripts/validate_resilience.py`). Ver [niveles de verificación](docs/NIVELES_DE_VERIFICACION.md).
- **Documentación.** Guía de la biblioteca de casos, matriz de materiales y amenazas, flujo de regeneración y tabla de scripts en la arquitectura del repositorio, perfiles complementarios en el mapa de roles, resumen de CI derivado de `data/program.json`.
- **Correcciones.** El generador del índice curricular listaba tres fases en vez de cuatro; cifras de fuentes derivadas de la bibliografía en el validador.

## 2026-10-12 · Fase IV, vivienda propia y ampliación

- 830 clases en 83 partes (ARQ-801–830), RUTA-34, casos CASA-NUEVA-80 y AMPLIACION-24 y herramientas de presupuesto.

## 2026-10-06 · Fase III

- 800 clases en 80 partes (ARQ-681–800); 33 rutas; auditoría de diferencias entre clases y reescritura de la profundización.

## Edición v1.0

- 680 clases y artefactos históricos (índice, lector offline y PDF), conservados como fotografía de la entrega original y no modificados.

## Cómo se registra un cambio

Cada cambio relevante se agrega al principio de este archivo con su fecha, el alcance (clases, rutas, casos, controles o documentación) y la verificación que lo respalda. Los hitos históricos se agregan, no se reescriben.
