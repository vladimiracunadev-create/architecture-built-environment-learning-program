#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Generate and verify the pedagogical layer for lessons, studios and routes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
PEDAGOGY = ROOT / "data" / "pedagogy.json"
PEDAGOGICAL_DECISIONS = ROOT / "data" / "pedagogical-decisions.json"
START = "<!-- pedagogia-2026:inicio -->"
END = "<!-- pedagogia-2026:fin -->"

SESSION_PHASES = (
    ("01", "Diagnóstico y contrato del problema", "separar el encargo inicial de los hechos comprobados y de las preguntas pendientes"),
    ("02", "Investigación y base de evidencia", "construir una base compartida de sitio, personas, precedentes, magnitudes y límites"),
    ("03", "Alternativas comparables", "producir al menos tres respuestas que resuelvan el mismo problema sin ventajas ocultas"),
    ("04", "Crítica intermedia", "someter las alternativas a objeciones, pruebas y revisión de personas que no participaron en su elaboración"),
    ("05", "Coordinación y revisión", "revisar interfaces, consecuencias, construcción, operación y cambios derivados de la crítica"),
    ("06", "Defensa y reflexión", "defender la propuesta revisada, conservar pendientes y demostrar qué cambió durante el taller"),
)

LESSON_KINDS = {
    "histórica y crítica": set(range(5, 11)) | {46, 51, 52, 59},
    "cuantitativa": {3, 19, 20, 21, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 42, 50, 53, 54, 55, 56, 57, 58, 60, 61, 62, 67},
    "profesional y de coordinación": {39, 40, 41, 42, 43, 44, 45, 46, 47, 48},
    "proyectual": {4, 11, 12, 13, 14, 15, 16, 17, 18, 49, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68},
}

EVIDENCE_BY_KIND = {
    "histórica y crítica": "ficha comparativa con fuente, observación, interpretación, contraejemplo y límite de transferencia",
    "cuantitativa": "desarrollo reproducible con datos, unidades, hipótesis, control independiente y conclusión limitada al modelo",
    "profesional y de coordinación": "registro de decisión con alcance, interfaces, versiones, responsables, evidencia y condición de cierre",
    "proyectual": "lámina o expediente con alternativas, representación pertinente, decisión argumentada, revisión y asuntos pendientes",
    "conceptual": "mapa argumentado que defina conceptos, los aplique a un caso y muestre qué evidencia haría cambiar la decisión",
}

ERRORS_BY_KIND = {
    "histórica y crítica": "confundir descripción con explicación; atribuir intención sin fuente; copiar una forma sin sus condiciones",
    "cuantitativa": "perder unidades; ocultar hipótesis; redondear antes de tiempo; convertir el resultado del modelo en autorización",
    "profesional y de coordinación": "confundir coordinación con aprobación; perder versión o responsable; cerrar un pendiente sin evidencia",
    "proyectual": "comparar alternativas con alcances distintos; defender la imagen antes que el servicio; borrar las huellas de la revisión",
    "conceptual": "repetir definiciones sin aplicarlas; usar un ejemplo que no discrimina; presentar una preferencia como requisito",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def lesson_kind(part: int) -> str:
    for kind, parts in LESSON_KINDS.items():
        if part in parts:
            return kind
    return "conceptual"


def section_text(text: str, heading_pattern: str) -> str:
    match = re.search(
        rf"^##\s+[^\n]*(?:{heading_pattern})[^\n]*\n+(.*?)(?=^##\s+|\Z)",
        text,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return ""
    value = re.sub(r"<[^>]+>", " ", match.group(1))
    value = re.sub(r"\[[^\]]+\]\([^\)]+\)", " ", value)
    value = re.sub(r"[`*_#>|]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def short(value: str, limit: int) -> str:
    value = value.replace('"', "'").strip()
    if len(value) <= limit:
        return value
    clipped = value[: limit - 1].rsplit(" ", 1)[0]
    return clipped + "…"


def title_from(text: str, lesson_id: str) -> str:
    first = text.splitlines()[0]
    return re.sub(rf"^#\s+{re.escape(lesson_id)}\s*[·—:-]\s*", "", first).strip()


def pedagogical_block(item: dict, text: str) -> str:
    lesson_id = item["id"]
    title = title_from(text, lesson_id)
    kind = lesson_kind(item["part"])
    question = section_text(text, "pregunta central") or title
    practice = section_text(text, "práctica|ejercicio") or f"Aplicar el método de {title.lower()} a un caso nuevo."
    evidence = EVIDENCE_BY_KIND[kind]
    errors = ERRORS_BY_KIND[kind]
    q_label = short(question.split(". ")[0], 92)
    p_label = short(practice.split(". ")[0], 92)
    safe_title = short(title, 60)
    return f"""{START}
## Mapa visual de aprendizaje

```mermaid
flowchart LR
    Q["Pregunta · {q_label}"] --> M["Método · {safe_title}"]
    M --> P["Transferencia · {p_label}"]
    P --> E["Evidencia revisable"]
    E --> C{{"¿Cumple el criterio?"}}
    C -->|sí| T["Conservar y conectar"]
    C -->|no| R["Revisar y volver a probar"]
```

El diagrama representa el ciclo de aprendizaje de esta clase, no una secuencia de obra ni un procedimiento profesional.

## Resultado observable, evidencia y evaluación

**Tipo de clase:** {kind}.

**Evidencia mínima:** {evidence}.

**Archivo sugerido:** `evidence/{lesson_id}/evidencia.md`.

| Criterio | Evidencia observable |
|---|---|
| Precisión y representación · 20 % | Los conceptos, unidades y convenciones se usan de forma coherente y pueden ser reconstruidos por otra persona. |
| Evidencia y trazabilidad · 25 % | Cada afirmación importante se vincula con dato, cálculo, observación o fuente; hipótesis y desconocidos permanecen visibles. |
| Decisión y alternativas · 25 % | La decisión responde a la pregunta, compara al menos una alternativa y declara qué condición la haría cambiar. |
| Integración y ciclo de vida · 20 % | Se identifica una interfaz y una consecuencia para construcción, uso, mantenimiento, adaptación o fin de vida. |
| Comunicación, ética y límites · 10 % | El alcance se entiende sin explicación oral adicional y no se atribuyen permisos, competencias o certezas inexistentes. |

**Criterio de aceptación:** 80/100 y ningún criterio bajo 60 %. Una entrega genérica que podría reutilizarse sin cambios en otra clase no demuestra dominio. Si existe una condición crítica de seguridad, accesibilidad, evidencia o responsabilidad sin resolver, la entrega permanece pendiente aunque el promedio supere 80.

### Errores diagnósticos

En esta clase conviene vigilar especialmente: {errors}.

## Autoevaluación, recuperación y continuidad

Antes de avanzar, responde sin consultar la solución:

1. ¿Qué decisión concreta puedes tomar ahora que no podías justificar antes?
2. ¿Qué evidencia de tu entrega es comprobada y cuál continúa siendo una hipótesis?
3. ¿Qué cambio de contexto invalidaría la transferencia realizada?

Revisa la entrega a las 24–48 horas y nuevamente al cerrar la parte. Conserva la primera versión, la crítica recibida y la versión revisada: el aprendizaje se demuestra también mediante el cambio entre versiones.
{END}"""


def explicit_pedagogical_block(item: dict, contract: dict) -> str:
    lesson_id = item["id"]
    prerequisites = ", ".join(f"`{value}`" for value in contract["prerequisites"]) or "Ninguno; es la entrada al programa."
    dependencies = ", ".join(f"`{value}`" for value in contract["dependencies"])
    outcomes = "\n".join(f"{index}. {value}" for index, value in enumerate(contract["outcomes"], 1))
    acceptance = "\n".join(f"- {value}" for value in contract["acceptance"])
    source_ids = sorted({source for foundation in contract["foundations"] for source in foundation["source_ids"]})
    source_label = " + ".join(source_ids)
    foundations = "\n".join(
        f"| {index} | {foundation['decision']} | "
        f"{', '.join(f'`{source}`' for source in foundation['source_ids'])} | "
        f"{foundation['application']} |"
        for index, foundation in enumerate(contract["foundations"], 1)
    )
    prerequisite_node = prerequisites.replace("`", "")
    dependency_node = dependencies.replace("`", "")
    return f"""{START}
## Decisión pedagógica y posición curricular

### Por qué existe

{contract['need']}

### Por qué está exactamente aquí

{contract['placement']}

- **Prerrequisitos:** {prerequisites}
- **Capacidad que introduce:** {contract['introduces']}
- **Clases o experiencias que dependen de ella:** {dependencies}

```mermaid
flowchart LR
    A["Prerrequisitos · {prerequisite_node}"] --> B["{lesson_id} · necesidad y fundamento"]
    S["Fuentes · {source_label}"] --> B
    B --> C["Actividad auténtica"]
    C --> D["Evidencia auditable"]
    D --> E["Continuidad · {dependency_node}"]
```

El diagrama permite comprobar una relación que el texto lineal oculta con facilidad: esta clase recibe capacidades previas, toma decisiones apoyadas por fuentes, exige una experiencia y produce evidencia que habilita trabajo posterior. No representa un procedimiento de obra.

## Resultado observable, evidencia y evaluación

{outcomes}

## Actividad, evidencia y criterio de aceptación

**Actividad:** {contract['activity']}

**Evidencia mínima:** {contract['evidence']}

**Archivo sugerido:** `evidence/{lesson_id}/evidencia.md`.

**Criterio de aceptación:** la entrega se acepta cuando:

{acceptance}

La [rúbrica común](../../docs/RUBRICA_COMUN.md) complementa estos criterios; no los reemplaza. Una entrega puede superar un promedio y continuar pendiente si oculta una condición crítica.

## Trazabilidad de las decisiones

| # | Decisión o fundamento | Fuente utilizada | Aplicación y límite en esta clase |
|---:|---|---|---|
{foundations}

La tabla permite auditar las relaciones; la explicación, el caso y la práctica de la clase siguen siendo la documentación principal.

## Autoevaluación, recuperación y continuidad

### Errores diagnósticos

Antes de avanzar, comprueba si puedes reconstruir cada resultado sin mirar la solución, señalar qué evidencia lo sostiene y nombrar una condición que obligaría a revisar tu decisión. Conserva la primera versión, la objeción recibida y la revisión.

**Conexión siguiente:** {contract['next_connection']}
{END}"""


def enrich_lesson(text: str, item: dict, contracts: dict[str, dict]) -> str:
    contract = contracts.get(item["id"])
    block = explicit_pedagogical_block(item, contract) if contract else pedagogical_block(item, text)
    if START in text and END in text:
        return re.sub(
            rf"{re.escape(START)}.*?{re.escape(END)}",
            block,
            text,
            flags=re.DOTALL,
        )
    source_heading = re.search(r"^##\s+Fuentes y alcance de uso\s*$", text, re.MULTILINE)
    if not source_heading:
        raise ValueError(f"missing sources heading in {item['id']}")
    return text[: source_heading.start()].rstrip() + "\n\n" + block + "\n\n" + text[source_heading.start() :]


def studio_readme(studio: dict) -> str:
    sessions = "\n".join(
        f"{index}. [{studio['id']}-{code} · {title}]({studio['id']}-{code}.md)"
        for index, (code, title, _decision) in enumerate(SESSION_PHASES, 1)
    )
    routes = ", ".join(studio["route_ids"])
    return f"""# {studio['id']} · {studio['title']}

> Taller vertical después de la Parte {studio['checkpoint_after_part']:02d} · seis sesiones · rutas: {routes}

## Propósito

{studio['purpose']}

## Encargo

{studio['brief']}

## Evidencia de salida

El producto final es un **{studio['product']}**. Debe conservar diagnóstico, alternativas, crítica, revisiones y pendientes. Una entrega final sin versiones intermedias no demuestra el proceso.

## Sesiones

{sessions}

## Evaluación

Se aplica la [rúbrica común](../../docs/RUBRICA_COMUN.md): precisión y representación 20 %, evidencia y trazabilidad 25 %, decisión y alternativas 25 %, integración y ciclo de vida 20 %, y comunicación, ética y límites 10 %. Aprobación: 80/100, sin dimensión bajo 60 % y sin condición crítica ocultada.

## Límites

Es un taller académico. No constituye expediente, cálculo, permiso, especificación, instrucción de obra ni habilitación profesional.
"""


def studio_session(studio: dict, phase: tuple[str, str, str]) -> str:
    code, title, decision = phase
    sid = f"{studio['id']}-{code}"
    if code == "01":
        activity = "Redacta el contrato del caso: propósito, personas, lugar, alcance, datos confirmados, hipótesis, exclusiones y preguntas críticas."
        evidence = "contrato del caso y diagnóstico de partida"
    elif code == "02":
        activity = "Construye una base de evidencia con procedencia, fecha, escala y límite; identifica una ausencia que pueda cambiar la decisión."
        evidence = "base de evidencia y mapa de actores e interfaces"
    elif code == "03":
        activity = "Produce tres alternativas comparables y representa qué conservan, qué cambian y qué consecuencia introduce cada una."
        evidence = "tres alternativas y matriz de comparación sin puntaje agregado"
    elif code == "04":
        activity = "Presenta el trabajo a una persona ajena al caso o aplica el protocolo de autocrítica adversarial; registra objeciones sin defender inmediatamente la propuesta."
        evidence = "acta de crítica con fortalezas, objeciones, evidencia faltante y plan de revisión"
    elif code == "05":
        activity = "Revisa la propuesta a partir de la crítica; sigue cada cambio hasta los documentos, sistemas, personas y etapas que afecta."
        evidence = "versión revisada, registro de cambios y comprobación de interfaces"
    else:
        activity = "Defiende la decisión, muestra las alternativas descartadas, explica qué cambió y declara los pendientes y el siguiente responsable."
        evidence = studio["product"] + ", memoria crítica y defensa"
    return f"""# {sid} · {title}

> {studio['title']} · sesión {int(code)} de 6 · taller académico

## Decisión que habilita

Esta sesión permite **{decision}** dentro del encargo: {studio['brief'].lower()}

## Evidencia de aprendizaje

Producirás **{evidence}**. Guárdala en `evidence/{studio['id']}/{code}/` junto con las fuentes y versiones utilizadas.

## Secuencia de trabajo

1. Recupera de memoria el estado anterior del caso y marca lo que todavía no puedes sostener.
2. {activity}
3. Comprueba unidades, procedencia, escala, actores y estados temporales.
4. Formula la objeción más fuerte a tu propia decisión y registra qué evidencia la resolvería.
5. Conserva la versión anterior y explica el cambio; no sobrescribas el proceso.

## Criterio de aceptación

La evidencia es aceptable cuando otra persona puede reconstruir la decisión, distinguir datos de hipótesis, localizar al menos una alternativa real, seguir una interfaz y reconocer qué permanece pendiente. Se aplica la rúbrica común y no se compensa una condición crítica abierta con un buen promedio.

## Preguntas de crítica

- ¿Qué parte de la propuesta depende de un dato todavía no confirmado?
- ¿Qué persona, oficio o especialidad podría refutar la decisión?
- ¿Qué cambia durante construcción, uso, mantenimiento o adaptación?
- ¿Qué representación adicional permitiría revisar mejor el argumento?

## Transferencia y límites

Transfiere el método, no los parámetros del caso. Esta sesión no reemplaza revisión profesional, participación real, normativa vigente, ensayos, permisos ni documentos ejecutivos.

[← Índice del taller](README.md)
"""


def studios_index(studios: list[dict]) -> str:
    rows = "\n".join(
        f"| [{s['id']} · {s['title']}]({s['id']}/README.md) | después de Parte {s['checkpoint_after_part']:02d} | {s['product']} |"
        for s in studios
    )
    return f"""# Talleres verticales

Los ocho talleres convierten la biblioteca de 680 clases en una experiencia iterativa. Cada uno contiene seis sesiones: diagnóstico, investigación, alternativas, crítica, revisión y defensa. En total son **48 sesiones integradoras**.

| Taller | Checkpoint | Evidencia de salida |
|---|---:|---|
{rows}

## Regla de trabajo

No se evalúa solamente la entrega final. Deben conservarse la primera versión, la crítica, las decisiones de revisión y la versión defendida. La diferencia entre versiones es evidencia de aprendizaje.

Consulta también la [arquitectura de evaluación](../docs/ARQUITECTURA_DE_EVALUACION.md), la [rúbrica común](../docs/RUBRICA_COMUN.md) y la [guía de portafolio](../docs/PORTAFOLIO_Y_EVIDENCIAS.md).
"""


def route_markdown(route: dict, studios: dict[str, dict]) -> str:
    parts = " → ".join(f"Parte {part:02d}" for part in route["parts"])
    capstone = studios[route["capstone"]]
    checkpoint_ids = [
        studio["id"]
        for studio in studios.values()
        if set(studio["route_ids"]) & {route["id"]}
        and studio["checkpoint_after_part"] <= max(route["parts"])
    ]
    checkpoints = ", ".join(checkpoint_ids) or route["capstone"]
    return f"""# {route['id']} · {route['title']}

## Para quién y punto de entrada

{route['entry']}

Antes de comenzar, resuelve una clase de cada prerrequisito sin consultar la solución. Si no puedes producir su evidencia mínima, incorpora esa clase como nivelación; no conviertas el diagnóstico en una penalización.

## Recorrido principal

{parts}

Las partes se estudian en su orden interno. La ruta selecciona un recorrido y no elimina la necesidad de volver a fundamentos cuando aparece una brecha.

## Checkpoints

Talleres asociados: **{checkpoints}**. En cada checkpoint debes conservar versión inicial, crítica, revisión y reflexión. La carga horaria se publicará después de un piloto con tiempos reales; hasta entonces no se presenta una cifra inventada.

## Evidencia de salida

{route['exit']}

## Capstone

[{capstone['id']} · {capstone['title']}](../studios/{capstone['id']}/README.md): {capstone['product']}.

## Criterio de finalización

La ruta se completa con el capstone en 80/100 o más, ninguna dimensión bajo 60 %, recuperación satisfactoria de conceptos esenciales y portafolio con al menos una revisión sustantiva. Completarla no concede título, licencia, firma ni atribución profesional.
"""


def write_or_check(path: Path, expected: str, check: bool, differences: list[str]) -> None:
    expected = expected.rstrip() + "\n"
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == expected:
        return
    differences.append(path.relative_to(ROOT).as_posix())
    if not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = load_json(CATALOG)
    pedagogy = load_json(PEDAGOGY)
    decision_manifest = load_json(PEDAGOGICAL_DECISIONS)
    contracts = {record["class_id"]: record for record in decision_manifest["decisions"]}
    differences: list[str] = []

    for item in catalog:
        path = ROOT / item["source"]
        current = path.read_text(encoding="utf-8")
        write_or_check(path, enrich_lesson(current, item, contracts), args.check, differences)

    studios = pedagogy["studios"]
    write_or_check(ROOT / "studios" / "README.md", studios_index(studios), args.check, differences)
    for studio in studios:
        folder = ROOT / "studios" / studio["id"]
        write_or_check(folder / "README.md", studio_readme(studio), args.check, differences)
        for phase in SESSION_PHASES:
            write_or_check(folder / f"{studio['id']}-{phase[0]}.md", studio_session(studio, phase), args.check, differences)

    by_id = {studio["id"]: studio for studio in studios}
    for route in pedagogy["routes"]:
        write_or_check(
            ROOT / "learning-paths" / f"{route['id'].lower()}.md",
            route_markdown(route, by_id),
            args.check,
            differences,
        )

    if differences and args.check:
        print("Pedagogical outputs are stale:\n" + "\n".join(differences[:50]), file=sys.stderr)
        return 1
    action = "Verified" if args.check else "Generated"
    print(f"{action} 680 lesson contracts, 48 studio sessions and 12 learning paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
