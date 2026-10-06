#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build class-specific decision chains from the complete lesson corpus.

The five editorial pilots remain authoritative overrides. The other records are
derived from each lesson's own question, outcome, prerequisites, practice,
feedback, sources and curricular neighbours; no record is derived from its
title alone.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
PILOTS = ROOT / "data" / "pedagogical-decisions.json"
BIBLIOGRAPHY = ROOT / "sources" / "bibliography.json"
OUTPUT = ROOT / "data" / "pedagogical-decisions-generated.json"


def clean(value: str) -> str:
    value = re.sub(r"<!-- pedagogia-2026:inicio -->.*?<!-- pedagogia-2026:fin -->", "", value, flags=re.DOTALL)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"!\[[^]]*\]\([^)]+\)", " ", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[\[([^]]+)\]\]", r"\1", value)
    value = re.sub(r"[`*_#>|]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def section(text: str, patterns: tuple[str, ...]) -> str:
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    for index, heading in enumerate(headings):
        title = heading.group(1).lower()
        if any(re.search(pattern, title) for pattern in patterns):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            return text[heading.end():end].strip()
    return ""


def sentences(value: str, count: int = 2, limit: int = 720) -> str:
    value = clean(value)
    pieces = re.split(r"(?<=[.!?])\s+", value)
    result = " ".join(piece for piece in pieces[:count] if piece)
    if len(result) > limit:
        result = result[:limit].rsplit(" ", 1)[0] + "…"
    return result


def prerequisite_ids(text: str, current_number: int) -> list[str]:
    opening = text[: text.find("## Pregunta central") if "## Pregunta central" in text else 1200]
    ids = re.findall(r"ARQ-\d{3}", opening)
    ids = [value for value in ids if int(value[4:]) < current_number]
    if not ids and current_number > 1:
        ids = [f"ARQ-{current_number - 1:03d}"]
    return list(dict.fromkeys(ids))


def source_records(item: dict, text: str, bibliography: dict) -> list[dict]:
    source_text = section(text, (r"fuentes y alcance",))
    urls = re.findall(r"\]\((https://[^)]+)\)", source_text)
    if not urls:
        urls = re.findall(r"(?<!\()https://[^\s)<>]+", source_text)
    urls = list(dict.fromkeys(url.rstrip(".,;") for url in urls))
    entries = {entry["locator"]: entry for entry in bibliography["entries"]}
    records = []
    for url in urls:
        entry = entries.get(url)
        if not entry:
            continue
        use = next((use for use in entry["uses"] if use["class"] == item["source"]), None)
        if not use:
            continue
        function = use.get("function") or f"Localizar evidencia externa pertinente para {item['title'].lower()}."
        scope = use.get("consultation_scope") or "Alcance consultado no documentado; debe completarse antes de ampliar la conclusión."
        limitation = use.get("limitation") or "Límite no documentado; la fuente no autoriza por sí sola una decisión profesional."
        if len(function) < 40:
            function = f"{function.rstrip('.')} para fundamentar una decisión delimitada de {item['title'].lower()}."
        records.append({
            "decision": function,
            "source_ids": [entry["id"]],
            "source_titles": [entry["title"]],
            "locators": [entry["locator"]],
            "application": f"Consulta: {scope} Límite: {limitation}",
        })
    return records[:4]


def derived_record(index: int, item: dict, catalog: list[dict], bibliography: dict, reverse_dependencies: dict[str, list[str]]) -> dict:
    path = ROOT / item["source"]
    text = path.read_text(encoding="utf-8")
    question = sentences(section(text, (r"pregunta central",)), 2)
    result = sentences(section(text, (r"resultado", r"qué aprenderás")), 3)
    practice_source = section(text, (r"práctica independiente", r"práctica", r"ejercicio"))
    # La actividad debe describir lo que hace el estudiante, no anticipar la
    # solución plegada que algunas clases incluyen en el mismo apartado.
    practice_source = re.sub(r"<details\b.*?</details>", "", practice_source, flags=re.DOTALL | re.IGNORECASE)
    practice = sentences(practice_source, 3)
    feedback = sentences(section(text, (r"autoevaluación", r"solución", r"errores")), 2)
    number = int(item["id"][4:])
    previous = catalog[index - 1] if index else None
    following = catalog[index + 1] if index + 1 < len(catalog) else None
    position = ((number - 1) % 10) + 1
    if position == 1:
        placement = (
            f"Abre la Parte {item['part']:02d} porque plantea primero el problema «{question}». "
            f"La transición desde {previous['id'] + ' · ' + previous['title'] if previous else 'la entrada al programa'} "
            f"conserva métodos de evidencia y límites, pero no traslada parámetros del bloque anterior. "
            f"Establece la pregunta y el producto base que {following['id']} · {following['title']} desarrollará a continuación."
        )
    elif position == 10:
        placement = (
            f"Cierra la Parte {item['part']:02d}: integra lo producido en {previous['id']} · {previous['title']} "
            f"para responder «{question}». La transición hacia "
            f"{following['id'] + ' · ' + following['title'] if following else 'el taller final EST-10 y el portafolio longitudinal'} "
            f"transfiere el método y la disciplina de evidencia, no los datos o parámetros particulares de esta parte."
        )
    else:
        placement = (
            f"Ocupa el lugar {position} de la Parte {item['part']:02d}. Se estudia después de {previous['id']} · {previous['title']} "
            f"porque usa esa base para responder «{question}». Se ubica antes de {following['id']} · {following['title']} "
            f"porque la evidencia producida aquí debe estar disponible para ese paso."
        )
    dependencies = reverse_dependencies.get(item["id"], [])[:3]
    if following and following["id"] not in dependencies:
        dependencies.append(following["id"])
    if not dependencies:
        dependencies = ["EST-10"]
    evidence = result or f"Entrega específica declarada en la práctica de {item['id']}: {practice}"
    activity = practice or f"Resolver el caso y la transferencia documentados en la clase completa de {item['title']}."
    if len(activity) < 80:
        activity += " La entrega debe conservar procedimiento, datos, supuestos, alternativa y conclusión revisable."
    foundations = source_records(item, text, bibliography)
    if not foundations:
        foundations = [{
            "decision": f"Mantener como pendiente cualquier afirmación externa de {item['title'].lower()} que no tenga una fuente localizable.",
            "source_ids": [], "source_titles": [], "locators": [],
            "application": "La ausencia de una relación extraíble no se reemplaza por una referencia inventada; requiere revisión editorial.",
        }]
    return {
        "class_id": item["id"],
        "review_status": "corpus-reviewed",
        "review_method": "full-lesson-question-outcome-practice-sources-neighbours",
        "profile": ["curricular", "class-specific"],
        "need": f"Esta clase existe para resolver una necesidad concreta del recorrido: {question}",
        "placement": placement,
        "prerequisites": prerequisite_ids(text, number),
        "introduces": result or f"Producir una respuesta verificable al problema de {item['title'].lower()}.",
        "dependencies": dependencies,
        "outcomes": [
            f"Identificar y delimitar las condiciones necesarias para responder la pregunta central de {item['title'].lower()}.",
            f"Producir y comprobar la evidencia declarada por la clase: {evidence}",
            f"Justificar una decisión de {item['title'].lower()} mediante fuentes, supuestos, alternativas y límites explícitos.",
        ],
        "activity": activity,
        "evidence": evidence,
        "acceptance": [
            f"La entrega responde explícitamente a la pregunta: {question}",
            f"La actividad conserva las fronteras del caso y permite reconstruir el procedimiento: {activity}",
            "Cada afirmación externa puede seguirse hasta una fuente, su alcance consultado y su límite.",
            f"La evidencia deja disponible una entrada comprobable para {dependencies[0]}.",
            feedback or "La autoevaluación de la clase se responde y toda condición crítica permanece visible.",
        ],
        "next_connection": (
            f"La continuidad inmediata es {following['id']} · {following['title']}; conserva el método y vuelve a verificar datos y límites."
            if following else
            "La continuidad es EST-10, donde la evidencia se incorpora al portafolio longitudinal y a la defensa final."
        ),
        "foundations": foundations,
    }


def build() -> dict:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    pilots = json.loads(PILOTS.read_text(encoding="utf-8"))
    bibliography = json.loads(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    overrides = {record["class_id"]: record for record in pilots["decisions"]}
    reverse_dependencies: dict[str, list[str]] = {}
    for item in catalog:
        text = (ROOT / item["source"]).read_text(encoding="utf-8")
        text = re.sub(r"<!-- pedagogia-2026:inicio -->.*?<!-- pedagogia-2026:fin -->", "", text, flags=re.DOTALL)
        for referenced in dict.fromkeys(re.findall(r"ARQ-\d{3}", text)):
            if int(referenced[4:]) < int(item["id"][4:]):
                reverse_dependencies.setdefault(referenced, []).append(item["id"])
    decisions = []
    for index, item in enumerate(catalog):
        if item["id"] in overrides:
            record = dict(overrides[item["id"]])
            record["review_method"] = "manual-editorial-pilot"
            decisions.append(record)
        else:
            decisions.append(derived_record(index, item, catalog, bibliography, reverse_dependencies))
    return {
        "schema_version": 2,
        "principle": "Una clase no es solo un tema: es una decisión sustentada.",
        "generated_on": "2026-10-06",
        "generated_from": [f"{len(catalog)} class Markdown files", "data/catalog.json", "sources/bibliography.json", "five editorial pilot overrides"],
        "decision_count": len(decisions),
        "manual_editorial_pilots": sorted(overrides),
        "decisions": decisions,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != content:
            raise SystemExit("generated pedagogical decision manifest is stale")
        print(f"Verified {len(json.loads(CATALOG.read_text(encoding='utf-8')))} class-specific pedagogical decision chains")
        return 0
    OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"Built {len(json.loads(CATALOG.read_text(encoding='utf-8')))} class-specific pedagogical decision chains")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
