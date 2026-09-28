# Registro central de fuentes

Este directorio responde de forma auditable a **qué fuentes utiliza cada clase**.

| Medida | Resultado |
|---|---:|
| Clases inspeccionadas | **680** |
| Apariciones de URL en fuentes | **1939** |
| URLs externas únicas | **622** |
| Dominios únicos | **189** |
| Usos con contexto completo | **886/1939** |
| Clases con todos sus usos completos | **292/680** |

El registro completo está en [`bibliography.json`](bibliography.json). Su esquema v3 registra o infiere: título; autor, organización o dominio de autoridad; URL; fecha de consulta cuando consta en la clase; tipo de fuente; función, alcance y límite por clase; licencia cuando se declara; y si el recurso se redistribuye o sólo se enlaza. Cada relación queda marcada como `complete` o `partial` e incluye la lista exacta de campos ausentes.

La política conservadora es `redistribution: link-only`. Cuando la licencia no consta se registra como `unknown`; eso no significa dominio público ni permiso para copiar.

## Una URL no basta

La presencia de un enlace demuestra localización, no calidad bibliográfica ni validez. Una relación clase–fuente es **contextualmente completa** sólo cuando declara los cuatro campos siguientes:

| Campo exigido | Cobertura actual | Porcentaje |
|---|---:|---:|
| Afirmación o función que apoya | **1872/1939** | **96.5%** |
| Parte o alcance efectivamente consultado | **1485/1939** | **76.6%** |
| Límite de interpretación | **1734/1939** | **89.4%** |
| Fecha de consulta | **1058/1939** | **54.6%** |

En conjunto, **886/1939 (45.7%)** usos tienen los cuatro campos y **1053** requieren revisión editorial. Esto se publica como brecha; no se reemplaza con inferencias o fechas inventadas.

## Requisitos según el tipo de fuente

| Tipo | Registros | Identificación mínima adicional |
|---|---:|---|
| Norma o estándar | 65 | organismo, código, edición o año, jurisdicción y artículo/sección consultada |
| Organismo público | 187 | institución, documento o página, fecha/versión y competencia territorial |
| Académica o educativa | 59 | autoría, título, institución/editorial, edición o año y capítulo/página cuando corresponda |
| Referencia web | 311 | autor o institución, título, fecha de publicación/actualización y sección consultada |

Los libros deben añadir editorial, edición, año, ISBN cuando exista y páginas o capítulos consultados. Un DOI, ISBN o URL es un localizador: no sustituye la explicación de qué afirmación respalda.

## Procedencias más frecuentes

| Dominio | URLs únicas |
|---|---:|
| `iso.org` | 65 |
| `whc.unesco.org` | 58 |
| `openstax.org` | 25 |
| `ocw.mit.edu` | 23 |
| `epa.gov` | 20 |
| `fhwa.dot.gov` | 14 |
| `nist.gov` | 14 |
| `research.fs.usda.gov` | 14 |
| `who.int` | 14 |
| `bigladdersoftware.com` | 13 |
| `steelconstruction.info` | 13 |
| `nps.gov` | 12 |
| `gov.uk` | 11 |
| `nrmca.org` | 11 |
| `access-board.gov` | 10 |
| `osha.gov` | 9 |
| `usgs.gov` | 9 |
| `bcn.cl` | 6 |
| `energy.gov` | 6 |
| `faa.gov` | 6 |

## Qué demuestra y qué no

El registro demuestra que una URL aparece en la sección de fuentes de una clase y permite localizar sus usos. No demuestra que la fuente siga disponible, que se haya leído íntegramente, que sea aplicable en una jurisdicción concreta ni que su institución respalde el programa. La disponibilidad en vivo de las 622 URLs y la vigencia normativa siguen pendientes.

Para entender de dónde provienen la secuencia, las indicaciones y los ejercicios, consulta [Procedencia editorial](../docs/PROCEDENCIA_EDITORIAL.md). Para el criterio de uso y límites, consulta [Fuentes y evidencia](../docs/FUENTES_Y_EVIDENCIA.md).

## Regeneración

```bash
python scripts/build_bibliography.py
python scripts/build_bibliography.py --check
```

No edites los archivos de este directorio a mano: corrige la clase Markdown correspondiente y regenera.
