# Estándar de fuentes y trazabilidad

## Principio

El conocimiento utilizado por el programa no se presenta como si surgiera de la nada. Toda afirmación técnica, histórica, normativa o empírica relevante debe poder reconstruirse mediante esta cadena:

```text
afirmación → fuente → localizador → autoridad → edición/fecha
           → parte consultada → uso en la clase → límite → estado de vigencia
```

La redacción, secuencia, ejercicios, casos ficticios y síntesis pedagógicas propias también se identifican como elaboración del programa. Ser original no significa carecer de antecedentes; significa que la organización y la explicación no se atribuyen falsamente a una fuente externa.

## Unidad mínima: relación clase–fuente

Una URL o referencia bibliográfica aislada no basta. Cada uso debe declarar:

1. **Identidad:** título, autor u organismo y localizador estable.
2. **Función:** afirmación, concepto, dato o método que respalda dentro de la clase.
3. **Alcance de consulta:** capítulo, página, artículo, sección, ficha o nivel de acceso efectivamente revisado.
4. **Límite:** qué no permite afirmar, transferir, calcular, autorizar o certificar.
5. **Temporalidad:** edición, versión o fecha de publicación y fecha de consulta cuando corresponda.
6. **Aplicabilidad:** jurisdicción y autoridad competente cuando la fuente pueda confundirse con un requisito.

El registro derivado marca una relación como `complete` únicamente cuando constan función, alcance de consulta, límite y fecha de consulta. `partial` significa que la fuente está localizada pero falta contexto documental; no significa que la fuente sea falsa.

## Identificación por tipo

### Libros y capítulos

- autoría o editoría;
- título de la obra y del capítulo, cuando corresponda;
- editorial, edición y año;
- páginas o capítulo consultados;
- ISBN cuando exista;
- función y límite dentro de la clase.

Una búsqueda, reseña, portada o ficha comercial no acredita lectura del libro completo.

### Artículos, tesis y publicaciones académicas

- autoría;
- título;
- revista, universidad o institución;
- año, volumen y número cuando correspondan;
- páginas;
- DOI o repositorio estable;
- parte efectivamente consultada y límite metodológico.

### Normas, leyes y reglamentos

- organismo emisor;
- código o identificador;
- título;
- edición, versión o fecha;
- jurisdicción;
- artículo, numeral, tabla o anexo consultado;
- estado de vigencia comprobado y fecha de comprobación.

Una ficha pública de ISO, por ejemplo, permite identificar un estándar, pero no equivale a consultar su texto completo. Una norma extranjera no se convierte automáticamente en requisito chileno.

### Sitios web, guías y organismos públicos

- autor u organismo responsable;
- título de la página o documento;
- fecha de publicación o actualización, cuando esté disponible;
- sección consultada;
- URL canónica y fecha de consulta;
- jurisdicción, audiencia y límite de transferencia.

### Obras, archivos, museos y casos

- institución o colección responsable;
- nombre de la obra o expediente;
- autoría, lugar y fecha cuando estén documentados;
- ficha, catálogo o documento consultado;
- diferencia entre descripción institucional, interpretación editorial y evidencia primaria.

## Jerarquía de uso

La autoridad depende de la afirmación. Para vigencia normativa se prioriza el organismo emisor o repositorio legal oficial; para mecanismos científicos, literatura académica o manuales técnicos reconocidos; para datos públicos, la institución responsable; para historia y patrimonio, fuentes primarias, archivos, catálogos razonados y bibliografía especializada.

Popularidad, buen diseño web o pertenencia a una institución prestigiosa no bastan por sí solos. Una fuente reconocida puede ser secundaria, estar desactualizada o quedar fuera de jurisdicción.

## Estados publicados

| Estado | Significado |
|---|---|
| `complete` | constan función, alcance consultado, límite y fecha de consulta |
| `partial` | existe localizador, pero falta al menos uno de esos campos |
| `registrada-no-verificada-en-vivo` | la URL fue extraída del corpus; no se comprobó disponibilidad en esta generación |
| `unknown` en licencia | no consta permiso de reutilización; sólo se conserva el enlace |

Ningún estado afirma por sí mismo que la fuente sea correcta, vigente o aplicable. La revisión disciplinar sigue siendo necesaria.

## Política de mejora

1. Corregir primero las fuentes de seguridad, accesibilidad, estructuras, incendio, normativa y responsabilidad profesional.
2. Completar después relaciones con función o límite ausentes.
3. Añadir localizadores internos —artículo, capítulo o página— sin afirmar lectura que no pueda documentarse.
4. Verificar disponibilidad y vigencia en una tarea separada, registrando fecha y resultado.
5. Regenerar `sources/bibliography.json` desde las clases; nunca editar el derivado a mano.
6. No degradar los mínimos de cobertura controlados por CI.

## Comprobación reproducible

```bash
python scripts/build_bibliography.py
python scripts/build_bibliography.py --check
python scripts/validate_repo.py
```

El estado cuantitativo vigente se publica en el [registro central](../sources/README.md) y en [Estado verificable](ESTADO_VERIFICABLE.md).
