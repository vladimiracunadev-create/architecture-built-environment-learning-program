# Auditoría de licenciamiento de segundo nivel

**Corte:** 6 de octubre de 2026
**Naturaleza:** revisión técnica, documental y automatizada del repositorio; no es una opinión legal.

## Resultado ejecutivo

Se conserva el modelo existente: Apache-2.0 para código propio; CC BY-NC-SA 4.0 para contenido pedagógico original; inventarios específicos para datos y activos; derechos de sus titulares para terceros; y protección de marca separada. La revisión no cambia el número de clases, partes ni la estructura pedagógica.

## Evidencia examinada

- árbol completo versionado, 800 clases y 80 README de parte;
- archivos legales, README, documentación, clases, fuentes, datos, scripts, activos y workflows;
- dos PDF, lector offline, generador de GitHub Pages y salida `site/` reconstruida;
- historial versionado, ramas remotas y autores de commit observables;
- 627 URLs externas únicas y 2.179 relaciones clase–fuente;
- pipeline local y workflows de `main`.

## RESUELTO

- `LICENSE` coincide por SHA-256 (`c95bae1d…ccefe2c`) con el texto completo de Apache License 2.0 usado por el proyecto y el validador detecta cualquier alteración.
- [La matriz real](docs/LICENSING_MATRIX.md) delimita por familias código, 800 clases, 80 índices de parte, documentación, catálogos, datos, SVG, PDF, lector offline y sitio generado.
- Los diez scripts y dos workflows propios llevan `SPDX-License-Identifier: Apache-2.0`; no se añadieron encabezados repetitivos a las 800 clases.
- El contenido CC se limita a la expresión pedagógica original y excluye normas, documentación institucional, papers, libros, planos, fotografías, fabricantes y demás material externo.
- El registro de fuentes usa esquema v2: título, autor u organización declarada o dominio inferido, URL, tipo, uso por clase, alcance, límite, fecha cuando consta, estado de licencia y política de redistribución.
- Las 627 licencias externas permanecen `unknown` porque las clases no aportan una declaración verificable de licencia; por ello los 627 registros se marcan `link-only` y no se presume derecho de copia.
- La [frontera normativa](docs/NORMATIVE_BOUNDARY.md) separa conocimiento didáctico de documento técnico oficial y de habilitación profesional.
- `assets/mark.svg` queda coherentemente descrito como obra gráfica CC BY-NC-SA 4.0 y, en paralelo, identificador cuya marca no queda licenciada. No se añaden restricciones de copyright incompatibles con CC.
- PDF, lector y sitio se documentan como artefactos por capas; generar o empaquetar no crea una licencia única nueva.
- [Uso comercial](docs/COMMERCIAL_USE.md) explica el código Apache, la limitación NC del contenido público, permisos separados y posibles aplicaciones externas.
- [Contribuciones](CONTRIBUTING.md) asigna código a Apache-2.0 y contenido a CC BY-NC-SA 4.0, exige derechos suficientes y adopta DCO 1.1 para procedencia de código sin introducir un CLA.
- [Historia de licencias](docs/LICENSING_HISTORY.md) conserva como no licenciadas explícitamente las revisiones `8037bf0f86` a `b9b4421dca` y registra la adopción del régimen en `6165418bcf` sin retroactividad inventada.
- `scripts/validate_repo.py` comprueba archivos legales, texto Apache, SPDX, enlaces, inventarios, esquema de fuentes, marca, capas generadas, copyright, placeholders, conteos, hashes y UTF-8; CI lo ejecuta antes y después de generar el sitio.

## RIESGO RESIDUAL

- La trazabilidad automática extrae 2.112 funciones, 1.725 alcances, 1.974 límites y 1.298 fechas de las 2.179 relaciones. Hay 1.126 usos contextualmente completos; los valores ausentes permanecen `null` y no se inventan metadatos.
- La disponibilidad, vigencia, versión y términos de las URLs externas pueden cambiar.
- Los PDF y el lector histórico sólo pueden auditarse hasta la procedencia documentada y sus hashes; su formato compuesto dificulta la señalización a nivel de fragmento.
- Los workflows usan versiones mayores de acciones de GitHub, no SHAs inmutables. Esto es un riesgo de cadena de suministro, no una contradicción del modelo de licencias.
- La rama `main` no está protegida por reglas remotas en el corte observado; el CI verde reduce errores, pero no obliga técnicamente a pasarlo antes de cada push.

## REQUIERE REVISIÓN HUMANA

- confirmar autoría y permisos cuando se aporte texto, datos o activos nuevos;
- revisar periódicamente las fuentes de mayor impacto y registrar licencia sólo con evidencia del titular;
- inspeccionar visualmente cambios futuros en PDF, SVG, lector y Pages;
- evaluar si una modificación de `mark.svg` o del nombre puede generar confusión sobre oficialidad;
- revisar contribuciones educativas firmadas, porque DCO está diseñado principalmente para procedencia de código y la aceptación del contenido depende además de la declaración CC de `CONTRIBUTING.md`.

## REQUIERE EVENTUAL REVISIÓN JURÍDICA

- solicitudes de uso comercial del contenido, doble licencia o acuerdos de distribución;
- adopción futura de CLA si se desea relicenciar contribuciones de terceros; no debe presumirse efecto retroactivo;
- búsqueda, registro o defensa de marca y criterios de uso nominativo en jurisdicciones concretas;
- reutilización sustancial de normas, documentación técnica, imágenes, planos, bases de datos o material con licencia desconocida;
- análisis de una obra o despliegue profesional real, que queda fuera de esta auditoría.

## Criterio de mantenimiento

La automatización prueba consistencia y presencia, no titularidad ni legalidad. Todo activo o dataset nuevo debe registrarse antes de incorporarse; toda fuente sin permiso claro debe enlazarse; y cualquier cambio del régimen requiere actualizar conjuntamente matriz, inventarios, historia, auditoría, contribuciones y validador.
