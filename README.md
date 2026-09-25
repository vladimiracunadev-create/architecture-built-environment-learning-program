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

Una biblioteca educativa completa y secuencial. Cada una de las **68 partes** contiene **10 clases**; la serie recorre **ARQ-001 → ARQ-680** sin huecos.

- **Fundamentos y cultura:** habitar, representación, historia, crítica y composición.
- **Personas y territorio:** accesibilidad, participación, vivienda, ciudad, paisaje y riesgos.
- **Técnica integrada:** estructuras, materiales, envolvente, instalaciones, energía y construcción.
- **Gestión y ciclo de vida:** costos, contratos, obra, operación, mantenimiento y conservación.
- **Tipologías y síntesis:** vivienda, salud, transporte, industria, cultura, educación, torres y grandes obras.

## 🌐 Markdown como fuente, HTML como experiencia

Las **680 clases viven como Markdown editable** en [`classes/`](classes/). Un generador reproducible crea una página HTML por clase, una portada editorial, un catálogo con búsqueda, navegación anterior/siguiente, páginas de fuentes y una versión imprimible.

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

| Superficie | Estado | Evidencia |
|---|---:|---|
| Partes curriculares | **68** | [`STATUS_v1.0.json`](STATUS_v1.0.json) y catálogo generado |
| Clases planificadas | **680** | [`INDICE_680_CLASES_v1.0.md`](INDICE_680_CLASES_v1.0.md) |
| Clases redactadas | **680** | 680 fuentes en [`classes/`](classes/) |
| Pendientes de redacción | **0** | [`STATUS_v1.0.json`](STATUS_v1.0.json) |
| Revisión externa especializada | **pendiente** | declarada, no inferida |
| Integridad de entregables | verificada | [`SHA256SUMS.txt`](SHA256SUMS.txt) |

## 🗂️ Estructura

```text
├── classes/                 # 680 clases Markdown, 68 partes
├── data/catalog.json        # catálogo canónico generado desde el lector v1.0
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

La validación comprueba secuencia completa, diez clases por parte, coherencia con `STATUS_v1.0.json`, hashes SHA-256, UTF-8 sin mojibake y las 680 salidas HTML.

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
