# Cómo contribuir

Gracias por ayudar a mejorar el programa.

## Antes de proponer un cambio

Lee [Método y alcance](docs/METODO_Y_ALCANCE.md), [Fuentes y evidencia](docs/FUENTES_Y_EVIDENCIA.md) y [Estado verificable](docs/ESTADO_VERIFICABLE.md). Este repositorio acepta correcciones editoriales, actualización de fuentes, mejoras pedagógicas y cambios del generador.

Una contribución a una clase debe conservar su identificador `ARQ-XXX`, parte y continuidad. Cuando actualice evidencia, debe indicar qué afirmación respalda la fuente, su jurisdicción y los límites de transferencia.

## Régimen de la contribución y procedencia

- El código, scripts, workflows, configuraciones, estilos y componentes funcionales aportados se ofrecen bajo Apache-2.0.
- El contenido educativo original aportado —texto, ejercicios, casos, rutas, plantillas y metodología— se ofrece bajo CC BY-NC-SA 4.0.
- Datos y activos requieren una entrada en `DATA_LICENSES.md` o `ASSET_LICENSES.md`; material externo requiere documentar titular, URL, licencia o permiso y alcance de reutilización.
- Al contribuir confirmas que creaste el aporte o tienes derecho suficiente para presentarlo bajo el régimen correspondiente. Una cita, acceso público o enlace no prueba ese derecho.

El proyecto adopta el [Developer Certificate of Origin 1.1](DCO) como registro ligero de procedencia para código. Firma cada commit con `git commit -s`; la línea `Signed-off-by` certifica el texto DCO sin transferir copyright. Para contenido educativo, la firma se acompaña de la confirmación explícita anterior y de la licencia CC indicada en este archivo.

No existe un CLA. Esto reduce fricción, pero significa que una futura doble licencia comercial no podrá incluir automáticamente aportes de terceros fuera de los permisos ya concedidos: habría que obtener autorizaciones adicionales o excluir/reemplazar esos aportes. Cualquier adopción futura de CLA exige una decisión documentada y no será retroactiva por presunción.

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

Todos los commits del pull request deben incluir `Signed-off-by: Nombre <correo>` mediante `git commit -s`.

El directorio `site/` es generado y no se versiona.

## Lista de comprobación

- [ ] Los enlaces locales funcionan.
- [ ] Las fuentes respaldan la afirmación concreta y no se presentan fuera de contexto.
- [ ] Los conteos del README y del estado verificable siguen coincidiendo con el repositorio.
- [ ] Se revisaron las páginas HTML afectadas, incluida una vista estrecha cuando cambia el diseño.
- [ ] No se añadieron secretos, datos personales ni material sin procedencia.
- [ ] Las tres comprobaciones locales terminan correctamente.

La aprobación editorial de un pull request no equivale a una revisión profesional externa del programa completo.
