#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build a central source registry from the canonical class catalog."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = json.loads((ROOT / "data" / "program.json").read_text(encoding="utf-8"))
OUT_JSON = ROOT / "sources" / "bibliography.json"
OUT_README = ROOT / "sources" / "README.md"
SOURCE_HEADING = "## Fuentes y alcance de uso"
TRACE_FIELDS = ("function", "consultation_scope", "limitation", "accessed_on")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
DATE_RE = re.compile(
    r"\b(?:[0-3]?\d[-/]\d{1,2}[-/]20\d{2}|[0-3]?\d\s+de\s+"
    r"(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+de\s+20\d{2})\b",
    re.IGNORECASE,
)
LICENSE_RE = re.compile(
    r"\b(Apache-2\.0|BSD-3-Clause|CC BY(?:-NC)?(?:-SA)? 4\.0|CC0-1\.0)\b",
    re.IGNORECASE,
)


def class_files() -> list[Path]:
    return sorted(ROOT.glob("classes/parte-[0-9][0-9]/ARQ-[0-9][0-9][0-9].md"))


def clean_url(value: str) -> str:
    return value.rstrip(".,;:")


def clean_label(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = URL_RE.sub(" ", value)
    value = re.sub(r"\[\[([^\]]+)\]\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[*_#`]", "", value)
    value = re.sub(r"^\s*[-–—:]\s*", "", value)
    value = re.sub(r"\s+", " ", value).strip(" —–-:;|")
    return value


def title_for(lines: list[str], index: int) -> str:
    for offset in range(1, 4):
        if index - offset < 0:
            break
        raw = lines[index - offset].strip()
        if raw.startswith("### "):
            candidate = clean_label(raw)
            if candidate:
                return candidate
        if raw and not raw.startswith(("Consulta", "Uso", "**Consulta", "**Apoyo", "**Límite")):
            break
    current = clean_label(lines[index])
    if " — " in current:
        current = current.split(" — ", 1)[0].strip()
    if len(current) >= 8:
        return current
    for offset in range(1, 5):
        if index - offset < 0:
            break
        candidate = clean_label(lines[index - offset])
        if candidate and not candidate.lower().startswith(("uso y límite", "consulta:", "apoyo:", "límite:")):
            return candidate
    return "Fuente externa"


def publisher_or_author_for(lines: list[str], index: int, domain: str) -> dict:
    current = clean_label(lines[index])
    if " — " in current:
        value = current.rsplit(" — ", 1)[-1].strip(" .")
        if value:
            return {"name": value, "basis": "class-text"}
    for offset in range(1, 4):
        if index - offset < 0:
            break
        raw = lines[index - offset].strip()
        if raw.startswith("### "):
            value = current.strip(" .")
            if value:
                return {"name": value, "basis": "class-text"}
        if raw:
            break
    return {"name": domain, "basis": "authority-domain-inferred"}


def source_context(lines: list[str], index: int) -> str:
    selected = [lines[index]]
    for line in lines[index + 1 : index + 6]:
        stripped = line.strip()
        if URL_RE.search(line) or stripped.startswith(("### ", "- **[[", "- **[")):
            break
        selected.append(line)
    return "\n".join(selected)


def labeled_value(text: str, labels: tuple[str, ...]) -> str | None:
    alternatives = "|".join(re.escape(label) for label in labels)
    match = re.search(
        rf"(?:\*\*)?(?:{alternatives})(?:\*\*)?\s*:\s*(.+?)(?=(?:\s+\*\*)?(?:Consulta|Apoyo|Uso|Alcance de consulta|Límite)(?:\*\*)?\s*:|$)",
        text.replace("\n", " "),
        re.IGNORECASE,
    )
    return clean_label(match.group(1)) if match else None


def consultation_date(text: str) -> str | None:
    candidates = []
    for match in re.finditer(r"consult\w{0,20}.{0,45}", text, re.IGNORECASE):
        date = DATE_RE.search(match.group(0))
        if date:
            candidates.append(date.group(0))
    return candidates[-1] if candidates else None


def declared_license(text: str) -> dict:
    match = LICENSE_RE.search(text)
    if not match:
        return {"status": "unknown", "identifier": None}
    return {"status": "declared-in-class", "identifier": match.group(1)}


def source_type(domain: str) -> str:
    if domain == "iso.org" or "standards" in domain:
        return "standard"
    if domain.endswith(".gov") or ".gov." in domain or domain in {"bcn.cl", "gov.uk"}:
        return "public-body"
    if domain.endswith(".edu") or "university" in domain or domain in {"ocw.mit.edu", "openstax.org"}:
        return "academic"
    return "reference"


def build_registry() -> dict:
    files = class_files()
    if len(files) != PROGRAM["class_count"]:
        raise SystemExit(f"expected {PROGRAM['class_count']} class files, found {len(files)}")

    records: dict[str, dict] = {}
    citations = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        if SOURCE_HEADING not in text:
            raise SystemExit(f"missing source section: {path.relative_to(ROOT)}")
        section = text.split(SOURCE_HEADING, 1)[1]
        lines = section.splitlines()
        class_accessed_on = consultation_date(section)
        relative = path.relative_to(ROOT).as_posix()
        seen_in_class: set[str] = set()
        for index, line in enumerate(lines):
            for raw_url in URL_RE.findall(line):
                url = clean_url(raw_url)
                if url in seen_in_class:
                    continue
                seen_in_class.add(url)
                citations += 1
                domain = urlparse(url).netloc.lower().removeprefix("www.")
                context = source_context(lines, index)
                record = records.setdefault(
                    url,
                    {
                        "id": f"source-{re.sub(r'[^a-z0-9]+', '-', domain).strip('-')}-{hashlib.sha1(url.encode()).hexdigest()[:10]}",
                        "type": source_type(domain),
                        "title": title_for(lines, index),
                        "locator": url,
                        "publisher_or_author": publisher_or_author_for(lines, index, domain),
                        "authority_domain": domain,
                        "status": "registrada-no-verificada-en-vivo",
                        "license": declared_license(context),
                        "redistribution": "link-only",
                        "used_in": [],
                        "uses": [],
                    },
                )
                if relative not in record["used_in"]:
                    record["used_in"].append(relative)
                    record["uses"].append(
                        {
                            "class": relative,
                            "function": labeled_value(context, ("Apoyo", "Uso", "Uso y límite")),
                            "consultation_scope": labeled_value(context, ("Consulta", "Alcance de consulta")),
                            "limitation": labeled_value(context, ("Límite",)),
                            "accessed_on": consultation_date(context) or class_accessed_on,
                        }
                    )

    entries = sorted(records.values(), key=lambda item: (item["authority_domain"], item["title"], item["locator"]))
    for entry in entries:
        entry["usage_count"] = len(entry["used_in"])
        for use in entry["uses"]:
            missing = [field for field in TRACE_FIELDS if not use.get(field)]
            use["traceability_status"] = "complete" if not missing else "partial"
            use["missing_fields"] = missing

    uses = [use for entry in entries for use in entry["uses"]]
    uses_by_class: dict[str, list[dict]] = {}
    for use in uses:
        uses_by_class.setdefault(use["class"], []).append(use)
    field_coverage = {
        field: sum(bool(use.get(field)) for use in uses) for field in TRACE_FIELDS
    }
    complete_uses = sum(use["traceability_status"] == "complete" for use in uses)
    complete_classes = sum(
        all(use["traceability_status"] == "complete" for use in class_uses)
        for class_uses in uses_by_class.values()
    )

    return {
        "schema_version": 3,
        "generated_from": "classes/parte-XX/ARQ-XXX.md",
        "generated_on": "2026-10-06",
        "policy": (
            "Registro derivado de las secciones 'Fuentes y alcance de uso'. "
            "Una URL registrada demuestra trazabilidad editorial, no vigencia, lectura íntegra, "
            "aplicabilidad normativa, permiso de redistribución ni respaldo institucional. "
            "Si no consta una licencia, se registra como desconocida y se conserva sólo el enlace."
        ),
        "class_count": len(files),
        "citation_occurrences": citations,
        "unique_sources": len(entries),
        "unique_domains": len({entry["authority_domain"] for entry in entries}),
        "traceability": {
            "required_context_fields": list(TRACE_FIELDS),
            "field_coverage": field_coverage,
            "complete_uses": complete_uses,
            "partial_uses": len(uses) - complete_uses,
            "classes_with_all_uses_complete": complete_classes,
            "classes_requiring_context_review": len(uses_by_class) - complete_classes,
            "live_availability_check": "not-implemented",
            "normative_currency_review": "pending",
        },
        "entries": entries,
    }


def render_readme(registry: dict) -> str:
    domains = Counter(entry["authority_domain"] for entry in registry["entries"])
    source_types = Counter(entry["type"] for entry in registry["entries"])
    trace = registry["traceability"]
    field_labels = {
        "function": "Afirmación o función que apoya",
        "consultation_scope": "Parte o alcance efectivamente consultado",
        "limitation": "Límite de interpretación",
        "accessed_on": "Fecha de consulta",
    }
    coverage_rows = "\n".join(
        f"| {field_labels[field]} | **{trace['field_coverage'][field]}/{registry['citation_occurrences']}** | "
        f"**{trace['field_coverage'][field] / registry['citation_occurrences']:.1%}** |"
        for field in TRACE_FIELDS
    )
    rows = "\n".join(f"| `{domain}` | {count} |" for domain, count in domains.most_common(20))
    return f"""# Registro central de fuentes

Este directorio responde de forma auditable a **qué fuentes utiliza cada clase**.

| Medida | Resultado |
|---|---:|
| Clases inspeccionadas | **{registry['class_count']}** |
| Apariciones de URL en fuentes | **{registry['citation_occurrences']}** |
| URLs externas únicas | **{registry['unique_sources']}** |
| Dominios únicos | **{registry['unique_domains']}** |
| Usos con contexto completo | **{trace['complete_uses']}/{registry['citation_occurrences']}** |
| Clases con todos sus usos completos | **{trace['classes_with_all_uses_complete']}/{registry['class_count']}** |

El registro completo está en [`bibliography.json`](bibliography.json). Su esquema v3 registra o infiere: título; autor, organización o dominio de autoridad; URL; fecha de consulta cuando consta en la clase; tipo de fuente; función, alcance y límite por clase; licencia cuando se declara; y si el recurso se redistribuye o sólo se enlaza. Cada relación queda marcada como `complete` o `partial` e incluye la lista exacta de campos ausentes.

La política conservadora es `redistribution: link-only`. Cuando la licencia no consta se registra como `unknown`; eso no significa dominio público ni permiso para copiar.

## Una URL no basta

La presencia de un enlace demuestra localización, no calidad bibliográfica ni validez. Una relación clase–fuente es **contextualmente completa** sólo cuando declara los cuatro campos siguientes:

| Campo exigido | Cobertura actual | Porcentaje |
|---|---:|---:|
{coverage_rows}

En conjunto, **{trace['complete_uses']}/{registry['citation_occurrences']} ({trace['complete_uses'] / registry['citation_occurrences']:.1%})** usos tienen los cuatro campos y **{trace['partial_uses']}** requieren revisión editorial. Esto se publica como brecha; no se reemplaza con inferencias o fechas inventadas.

## Requisitos según el tipo de fuente

| Tipo | Registros | Identificación mínima adicional |
|---|---:|---|
| Norma o estándar | {source_types['standard']} | organismo, código, edición o año, jurisdicción y artículo/sección consultada |
| Organismo público | {source_types['public-body']} | institución, documento o página, fecha/versión y competencia territorial |
| Académica o educativa | {source_types['academic']} | autoría, título, institución/editorial, edición o año y capítulo/página cuando corresponda |
| Referencia web | {source_types['reference']} | autor o institución, título, fecha de publicación/actualización y sección consultada |

Los libros deben añadir editorial, edición, año, ISBN cuando exista y páginas o capítulos consultados. Un DOI, ISBN o URL es un localizador: no sustituye la explicación de qué afirmación respalda.

## Procedencias más frecuentes

| Dominio | URLs únicas |
|---|---:|
{rows}

## Qué demuestra y qué no

El registro demuestra que una URL aparece en la sección de fuentes de una clase y permite localizar sus usos. No demuestra que la fuente siga disponible, que se haya leído íntegramente, que sea aplicable en una jurisdicción concreta ni que su institución respalde el programa. La disponibilidad en vivo de las {registry['unique_sources']} URLs y la vigencia normativa siguen pendientes.

Para entender de dónde provienen la secuencia, las indicaciones y los ejercicios, consulta [Procedencia editorial](../docs/PROCEDENCIA_EDITORIAL.md). Para el criterio de uso y límites, consulta [Fuentes y evidencia](../docs/FUENTES_Y_EVIDENCIA.md).

## Regeneración

```bash
python scripts/build_bibliography.py
python scripts/build_bibliography.py --check
```

No edites los archivos de este directorio a mano: corrige la clase Markdown correspondiente y regenera.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    registry = build_registry()
    json_text = json.dumps(registry, ensure_ascii=False, indent=2) + "\n"
    readme_text = render_readme(registry)
    expected = {OUT_JSON: json_text, OUT_README: readme_text}

    if args.check:
        stale = [path for path, value in expected.items() if not path.exists() or path.read_text(encoding="utf-8") != value]
        if stale:
            raise SystemExit("stale bibliography files: " + ", ".join(str(path.relative_to(ROOT)) for path in stale))
        print(
            f"Verified {registry['unique_sources']} unique source URLs, "
            f"{registry['citation_occurrences']} citations, {registry['unique_domains']} domains and "
            f"{registry['traceability']['complete_uses']} complete source uses"
        )
        return 0

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    for path, value in expected.items():
        path.write_text(value, encoding="utf-8", newline="\n")
    print(
        f"Built {registry['unique_sources']} unique source URLs, "
        f"{registry['citation_occurrences']} citations, {registry['unique_domains']} domains and "
        f"{registry['traceability']['complete_uses']} complete source uses"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
