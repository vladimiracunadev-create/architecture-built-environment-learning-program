<div align="center">

# 🏛️ Programa Integral de Arquitectura, Construcción y Entorno Habitado

## **680 clases · 68 partes · del encargo al fin de vida**

**Currículo secuencial en español para estudiar arquitectura como sistema: personas, lugar, historia, representación, técnica, materia, recursos, operación y tiempo.**

[![CI](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program/actions/workflows/ci.yml)
[![Deploy Pages](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program/actions/workflows/deploy-pages.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program/actions/workflows/deploy-pages.yml)
[![Clases](https://img.shields.io/badge/clases-680%20·%2068%20partes-b85c38?style=for-the-badge)](INDICE_680_CLASES_v1.0.md)
[![Estado](https://img.shields.io/badge/estado-redacción%20completa-1d6b68?style=for-the-badge)](STATUS_v1.0.json)
[![Idioma](https://img.shields.io/badge/idioma-español-102f38?style=for-the-badge)](README.md)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-sitio%20HTML-ddb967?style=for-the-badge&logo=githubpages&logoColor=172526)](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/)

[🌐 Abrir el sitio](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/) · [📚 Índice de 680 clases](INDICE_680_CLASES_v1.0.md) · [🧭 Método y alcance](docs/METODO_Y_ALCANCE.md) · [📦 Artefactos](docs/ARTEFACTOS.md) · [🗺️ Roadmap](Arquitectura_FaseII_Roadmap_Final_v1.0.md)

</div>

---

> **Alcance profesional.** Completar este programa no otorga título, licencia, firma, permiso ni habilitación profesional. Los casos numéricos son didácticos salvo atribución explícita. Toda obra real requiere antecedentes, normativa vigente, especialistas competentes, coordinación, revisión y autorizaciones aplicables.

## 🎯 Qué es

Una biblioteca educativa completa y secuencial. Cada una de las **68 partes** contiene **10 clases**; la serie recorre **ARQ-001 → ARQ-680** sin huecos. El programa no termina en ese índice: incorpora **611 fuentes, 80 roles y oficios, 36 plantillas, 16 documentos transversales y 12 rutas de aprendizaje**.

- **Fundamentos y cultura:** habitar, representación, historia, crítica y composición.
- **Personas y territorio:** accesibilidad, participación, vivienda, ciudad, paisaje y riesgos.
- **Técnica integrada:** estructuras, materiales, envolvente, instalaciones, energía y construcción.
- **Gestión y ciclo de vida:** costos, contratos, obra, operación, mantenimiento y conservación.
- **Tipologías y síntesis:** vivienda, salud, transporte, industria, cultura, educación, torres y grandes obras.

## 🌐 Markdown como fuente, HTML como experiencia

Las **680 clases viven como Markdown editable** en [`classes/`](classes/). Un generador reproducible crea una página HTML por clase, **68 portadas de parte** y páginas individuales para los **755 recursos transversales**, además de la portada editorial, el catálogo con búsqueda y la navegación anterior/siguiente.

```text
classes/parte-XX/ARQ-XXX.md  ──┐
data/catalog.json             ├──> scripts/build_site.py ──> site/ ──> GitHub Pages
docs/*.md                     ──┘
```

El [lector offline original](programa-arquitectura-lector-definitivo-v1.0.html) se conserva como artefacto autosuficiente y como fuente histórica verificable de la edición definitiva v1.0.

## 🧠 Método de aprendizaje

Las clases no presentan recetas universales. Siguen una disciplina común:

1. formular una pregunta central;
2. declarar resultado de aprendizaje y continuidad;
3. distinguir dato, hipótesis, evidencia y límite;
4. resolver un caso trabajado con unidades y fronteras explícitas;
5. practicar de forma independiente;
6. identificar interfaces, responsabilidades y decisiones que siguen pendientes.

La regla transversal es simple: **entre tipologías se transfieren preguntas, mecanismos y métodos; no parámetros**.

## ✅ Estado verificable

El estado no es una consigna comercial. Los conteos siguientes se comprueban desde los archivos fuente, el catálogo canónico, el lector v1.0 y el build. La revisión automatizada confirma estructura e integridad; **no sustituye una revisión profesional externa**.

| Superficie | Estado | Evidencia |
|---|---:|---|
| Secuencia curricular | **680 / 680** | ARQ-001 → ARQ-680, sin huecos, en [`data/catalog.json`](data/catalog.json) |
| Partes curriculares | **68 / 68** | 10 clases en cada parte; ver [`INDICE_680_CLASES_v1.0.md`](INDICE_680_CLASES_v1.0.md) |
| Clases Markdown | **680** | una fuente editable por clase en [`classes/`](classes/) |
| Páginas HTML de clases | **680** | build reproducible y validador de enlaces |
| Portadas HTML de partes | **68** | una portada navegable por bloque |
| Fuentes con alcance de uso | **611** | fichas públicas extraídas del lector definitivo |
| Roles y oficios | **80** | responsabilidades, interfaces y límites |
| Plantillas | **36** | registros de decisiones, evidencia y coordinación |
| Documentos transversales | **16** | inicio, mapa, estado, método, normas, derechos y continuidad |
| Rutas de aprendizaje | **12** | recorridos temáticos sobre el currículo |
| Entradas navegables totales | **1.435** | 680 clases + 755 recursos |
| Pendientes de redacción | **0** | [`STATUS_v1.0.json`](STATUS_v1.0.json) |
| Revisión externa especializada | **pendiente** | declarada, no inferida |
| Integridad de entregables | verificada | [`SHA256SUMS.txt`](SHA256SUMS.txt) |

### Qué significa “completo”

“Completo” significa que la secuencia editorial prevista tiene 680 clases redactadas y publicables, no que cada jurisdicción, especialidad o tecnología esté agotada. Tampoco significa acreditación, vigencia normativa universal, certificación de obra ni revisión por pares. Las afirmaciones de estado actual se validan en CI; las referencias históricas a versiones previas se conservan como historia.

## 🧭 Las 68 partes

Cada parte contiene exactamente diez clases y dispone de una portada HTML navegable.

| # | Parte | Clases |
|---:|---|---:|
| 01 | Fundamentos del habitar y del oficio | ARQ-001–010 |
| 02 | Representación y pensamiento espacial | ARQ-011–020 |
| 03 | Matemática, geometría y física desde la base | ARQ-021–030 |
| 04 | Personas, investigación y programa arquitectónico | ARQ-031–040 |
| 05 | Historias globales I: orígenes y primeras ciudades | ARQ-041–050 |
| 06 | Historias globales II: redes y tradiciones preindustriales | ARQ-051–060 |
| 07 | Industrialización y arquitecturas modernas | ARQ-061–070 |
| 08 | Arquitecturas contemporáneas y pensamiento crítico | ARQ-071–080 |
| 09 | Chile, América Latina y saberes territoriales | ARQ-081–090 |
| 10 | Teoría, composición y lenguajes | ARQ-091–100 |
| 11 | Sitio, levantamiento y cartografía | ARQ-101–110 |
| 12 | Urbanismo, territorio y espacio público | ARQ-111–120 |
| 13 | Paisaje, ecología y agua | ARQ-121–130 |
| 14 | Proceso de diseño y taller de proyecto | ARQ-131–140 |
| 15 | Vivienda y formas de convivencia | ARQ-141–150 |
| 16 | Equipamientos públicos, salud, educación y cultura | ARQ-151–160 |
| 17 | Comercio, trabajo, producción e infraestructuras | ARQ-161–170 |
| 18 | Accesibilidad y diseño inclusivo | ARQ-171–180 |
| 19 | Suelo, geotecnia y fundaciones | ARQ-181–190 |
| 20 | Mecánica y comportamiento estructural | ARQ-191–200 |
| 21 | Sistemas estructurales y coordinación arquitectónica | ARQ-201–210 |
| 22 | Tierra, piedra y albañilería | ARQ-211–220 |
| 23 | Madera, bambú y materiales biobasados | ARQ-221–230 |
| 24 | Hormigón y sistemas cementicios | ARQ-231–240 |
| 25 | Acero, aluminio, vidrio y metales | ARQ-241–250 |
| 26 | Aislantes, membranas, compuestos y terminaciones | ARQ-251–260 |
| 27 | Envolvente, humedad y detalle constructivo | ARQ-261–270 |
| 28 | Clima y estrategias pasivas | ARQ-271–280 |
| 29 | Energía y desempeño del edificio | ARQ-281–290 |
| 30 | Iluminación, acústica y experiencia sensorial | ARQ-291–300 |
| 31 | Agua, saneamiento y redes sanitarias | ARQ-301–310 |
| 32 | Ventilación, climatización y calidad de aire | ARQ-311–320 |
| 33 | Electricidad, gas, comunicaciones y transporte vertical | ARQ-321–330 |
| 34 | Incendio y seguridad de vida | ARQ-331–340 |
| 35 | Sismorresistencia y continuidad funcional | ARQ-341–350 |
| 36 | Tsunamis, inundaciones y bordes de agua | ARQ-351–360 |
| 37 | Viento, tormentas, nieve, calor e incendios de interfaz | ARQ-361–370 |
| 38 | Amenazas geológicas, multirriesgo y preparación | ARQ-371–380 |
| 39 | Construcción, oficios y procesos productivos | ARQ-381–390 |
| 40 | Normas, ISO y marco jurídico de la edificación | ARQ-391–400 |
| 41 | Documentación, especificaciones y contratación | ARQ-401–410 |
| 42 | Costos, factibilidad y economía del proyecto | ARQ-411–420 |
| 43 | Gestión de obra, calidad y seguridad | ARQ-421–430 |
| 44 | BIM, interoperabilidad, computación e IA | ARQ-431–440 |
| 45 | Sostenibilidad, carbono y circularidad | ARQ-441–450 |
| 46 | Patrimonio, patologías y rehabilitación | ARQ-451–460 |
| 47 | Uso, mantenimiento y evaluación posocupacional | ARQ-461–470 |
| 48 | Taller integral, carreras e investigación | ARQ-471–480 |
| 49 | Vivienda por tipologías y edificios residenciales | ARQ-481–490 |
| 50 | Edificios altos y rascacielos | ARQ-491–500 |
| 51 | Arquitectura religiosa y ceremonial | ARQ-501–510 |
| 52 | Castillos, fortificaciones y arquitectura defensiva | ARQ-511–520 |
| 53 | Hospitales y complejos de salud | ARQ-521–530 |
| 54 | Aeropuertos y terminales aéreas | ARQ-531–540 |
| 55 | Ferrocarril, estaciones y metro | ARQ-541–550 |
| 56 | Puentes | ARQ-551–560 |
| 57 | Túneles e infraestructura subterránea | ARQ-561–570 |
| 58 | Estadios, arenas y grandes recintos | ARQ-571–580 |
| 59 | Teatros, auditorios, museos y centros culturales | ARQ-581–590 |
| 60 | Centros de datos, laboratorios y edificios científicos | ARQ-591–600 |
| 61 | Industria, logística y plantas productivas | ARQ-601–610 |
| 62 | Puertos, terminales marítimos y bordes productivos | ARQ-611–620 |
| 63 | Edificios cívicos, justicia y alta seguridad | ARQ-621–630 |
| 64 | Hoteles, comercio y hospitalidad | ARQ-631–640 |
| 65 | Escuelas, universidades y campus | ARQ-641–650 |
| 66 | Maquetas, prototipos y representación avanzada | ARQ-651–660 |
| 67 | Torres, miradores e infraestructuras especiales | ARQ-661–670 |
| 68 | Casos integradores de tipologías y grandes obras | ARQ-671–680 |

➡️ [Abrir el mapa navegable de partes](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/partes/)

## 🧩 Superficie transversal

| Recurso | Cantidad | Función |
|---|---:|---|
| [Fuentes](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/fuentes/) | 611 | documentar apoyo, consulta y límite de uso |
| [Roles y oficios](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/roles/) | 80 | distinguir quién decide, coordina, comprueba y autoriza |
| [Plantillas](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/plantillas/) | 36 | convertir el método en registros reutilizables |
| [Documentos](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/documentos/) | 16 | explicar mapa, calidad, normativa, derechos y continuidad |
| [Rutas](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/rutas/) | 12 | recorrer el programa por problema o responsabilidad |

## 🗂️ Estructura

```text
├── classes/                 # 680 clases Markdown, 68 partes
├── data/catalog.json        # catálogo canónico de las 680 clases
├── docs/                    # método, alcance y artefactos
├── assets/                  # identidad visual del sitio
├── scripts/                 # importación, build y validación
├── .github/workflows/       # CI y despliegue de GitHub Pages
├── *.pdf                    # entregables finales conservados
└── programa-...v1.0.html    # lector offline autosuficiente original
```

## 🛠️ Generar y verificar

```bash
python -m pip install -r requirements-build.txt
python scripts/build_site.py
python scripts/validate_repo.py
```

La validación comprueba secuencia completa, diez clases por parte, coherencia con `STATUS_v1.0.json`, hashes SHA-256, UTF-8 sin mojibake, **680 páginas de clase, 68 portadas de parte, 755 páginas de recursos** y todos los enlaces internos del sitio.

## ⚙️ Calidad, CI y despliegue

El repositorio no se publica a ciegas. Los mismos comandos usados en local corren en GitHub Actions.

| Workflow | Qué comprueba |
|---|---|
| [`ci.yml`](.github/workflows/ci.yml) | instala dependencias, genera el portal completo y ejecuta la validación estructural, documental, de codificación, hashes y enlaces |
| [`deploy-pages.yml`](.github/workflows/deploy-pages.yml) | reconstruye el sitio desde las fuentes Markdown, sube el artefacto y lo despliega en GitHub Pages |

El contenido generado no es la fuente de verdad: puede eliminarse y reconstruirse con `python scripts/build_site.py`. El build falla si falta una clase, una parte, una categoría transversal o si aparece un enlace interno roto.

## 🔎 Evidencia, fuentes y límites

- Cada clase explicita pregunta central, resultado, continuidad, práctica y alcance profesional.
- Una fuente se usa para sostener una afirmación delimitada; citarla no implica adoptar toda la obra ni declarar vigencia normativa global.
- Los valores sintéticos, modelos simplificados y casos ficticios permanecen identificados como tales.
- “No verificado” no equivale a cero, seguro, conforme ni inexistente.
- Entre tipologías se transfieren preguntas y mecanismos; no se transfieren parámetros sin nueva evidencia.

La revisión externa especializada sigue pendiente. Esa condición aparece en el lector, en las clases y en este README; el CI verifica consistencia editorial, no competencia profesional ni validez para construir.

## ✅ Lo que sí es / ❌ lo que no es

| Sí | No |
|---|---|
| Un currículo integral y secuencial | Una carrera acreditada |
| Material para aprender a razonar con evidencia | Un sustituto de la experiencia supervisada |
| Casos ficticios con límites declarados | Cálculos o especificaciones para construir |
| Una base abierta a revisión profesional | Una promesa de cumplimiento normativo |
| Markdown versionado y sitio HTML reproducible | Un catálogo de soluciones para copiar |

## 🤝 Contribuir

Consulta [`CONTRIBUTING.md`](CONTRIBUTING.md). Las correcciones deben identificar evidencia, alcance y superficies afectadas. La siguiente etapa prioritaria es la auditoría transversal y la revisión externa por especialidades, no aumentar el número de clases por sí mismo.

---

Hecho con criterio técnico y vocación educativa por [Vladimir Acuña](https://github.com/vladimiracunadev-create).
