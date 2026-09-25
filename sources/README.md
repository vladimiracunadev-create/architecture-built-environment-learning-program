# Registro central de fuentes

Este directorio responde de forma auditable a **qué fuentes utiliza cada clase**.

| Medida | Resultado |
|---|---:|
| Clases inspeccionadas | **680** |
| Apariciones de URL en fuentes | **1939** |
| URLs externas únicas | **622** |
| Dominios únicos | **189** |

El registro completo está en [`bibliography.json`](bibliography.json). Su esquema v2 registra o infiere: título; autor, organización o dominio de autoridad; URL; fecha de consulta cuando consta en la clase; tipo de fuente; función, alcance y límite por clase; licencia cuando se declara; y si el recurso se redistribuye o sólo se enlaza.

La política conservadora es `redistribution: link-only`. Cuando la licencia no consta se registra como `unknown`; eso no significa dominio público ni permiso para copiar.

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

El registro demuestra que una URL aparece en la sección de fuentes de una clase y permite localizar sus usos. No demuestra que la fuente siga disponible, que se haya leído íntegramente, que sea aplicable en una jurisdicción concreta ni que su institución respalde el programa.

Para entender de dónde provienen la secuencia, las indicaciones y los ejercicios, consulta [Procedencia editorial](../docs/PROCEDENCIA_EDITORIAL.md). Para el criterio de uso y límites, consulta [Fuentes y evidencia](../docs/FUENTES_Y_EVIDENCIA.md).

## Regeneración

```bash
python scripts/build_bibliography.py
python scripts/build_bibliography.py --check
```

No edites los archivos de este directorio a mano: corrige la clase Markdown correspondiente y regenera.
