# Cómo contribuir

Gracias por ayudar a mejorar el programa.

## Antes de proponer un cambio

Lee [Método y alcance](docs/METODO_Y_ALCANCE.md), [Fuentes y evidencia](docs/FUENTES_Y_EVIDENCIA.md) y [Estado verificable](docs/ESTADO_VERIFICABLE.md). Este repositorio acepta correcciones editoriales, actualización de fuentes, mejoras pedagógicas y cambios del generador.

Una contribución a una clase debe conservar su identificador `ARQ-XXX`, parte y continuidad. Cuando actualice evidencia, debe indicar qué afirmación respalda la fuente, su jurisdicción y los límites de transferencia.

## Principios editoriales

- Conserva la numeración, la parte y la continuidad de la clase.
- Separa datos, hipótesis, cálculos, evidencia y autorización.
- No conviertas una referencia internacional en normativa local.
- No presentes un caso didáctico como proyecto ejecutable.
- No uses “completo”, “validado” o “certificado” sin definir la dimensión y la evidencia.
- Distingue un marcador de estado actual de una referencia histórica.
- Cita fuentes originales, declara el alcance de uso y explica las excepciones a la pauta de clase.
- Mantén el texto en UTF-8 y evita información personal innecesaria.

## Flujo

1. Crea una rama descriptiva.
2. Edita la fuente Markdown en `classes/`.
3. Ejecuta `python scripts/generate_curriculum_docs.py --check`.
4. Ejecuta `python scripts/build_bibliography.py --check`.
5. Ejecuta `python scripts/build_site.py`.
6. Ejecuta `python scripts/validate_repo.py`.
7. Abre un pull request explicando el cambio, la evidencia y las superficies revisadas.

El directorio `site/` es generado y no se versiona.

## Lista de comprobación

- [ ] Los enlaces locales funcionan.
- [ ] Las fuentes respaldan la afirmación concreta y no se presentan fuera de contexto.
- [ ] Los conteos del README y del estado verificable siguen coincidiendo con el repositorio.
- [ ] Se revisaron las páginas HTML afectadas, incluida una vista estrecha cuando cambia el diseño.
- [ ] No se añadieron secretos, datos personales ni material sin procedencia.
- [ ] Las tres comprobaciones locales terminan correctamente.

La aprobación editorial de un pull request no equivale a una revisión profesional externa del programa completo.
