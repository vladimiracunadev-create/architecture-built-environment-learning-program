#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Measure global class coverage and validate reviewed pedagogical decisions."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
DECISIONS = ROOT / "data" / "pedagogical-decisions-generated.json"
OBSERVABLE = (
    "analizar", "aplicar", "argumentar", "clasificar", "comparar", "construir",
    "defender", "diagnosticar", "diferenciar", "diseñar", "distinguir", "documentar", "elaborar",
    "evaluar", "formular", "identificar", "justificar", "mapear", "modelar",
    "normalizar", "producir", "reconstruir", "redactar", "representar", "resolver",
    "trazar", "validar",
)
REQUIRED = {
    "class_id", "review_status", "profile", "need", "placement", "prerequisites",
    "introduces", "dependencies", "outcomes", "activity", "evidence", "acceptance",
    "next_connection", "foundations", "review_method",
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.lower())
    return "".join(char for char in value if not unicodedata.combining(char))


def declared_sources(text: str) -> set[str]:
    chunks = re.split(r"^##\s+Fuentes y alcance de uso\s*$", text, flags=re.MULTILINE)
    if len(chunks) != 2:
        return set()
    result = set(re.findall(r"\[\[([^\]]+)\]\]", chunks[1]))
    result.update(re.findall(r"^- \*\*\[([^\]]+)\]", chunks[1], re.MULTILINE))
    return result


def validate_contract(record: dict, known: set[str], text: str) -> list[str]:
    errors: list[str] = []
    class_id = record.get("class_id", "<unknown>")
    missing = sorted(REQUIRED - set(record))
    if missing:
        return [f"{class_id}: missing fields {', '.join(missing)}"]
    if record["review_status"] not in {"reviewed", "corpus-reviewed"}:
        errors.append(f"{class_id}: contract has no valid review state")
    for key in ("need", "placement", "introduces", "activity", "evidence", "next_connection"):
        if len(record[key].strip()) < 80:
            errors.append(f"{class_id}: {key} is too short to justify the decision")
    for linked in record["prerequisites"] + record["dependencies"]:
        if linked.startswith("ARQ-") and linked not in known:
            errors.append(f"{class_id}: unknown dependency {linked}")
    if not record["outcomes"] or not record["acceptance"] or not record["foundations"]:
        errors.append(f"{class_id}: outcomes, acceptance and foundations cannot be empty")
    for outcome in record["outcomes"]:
        normalized = normalize(outcome)
        if not normalized.startswith(OBSERVABLE):
            errors.append(f"{class_id}: outcome lacks an observable verb: {outcome}")
    sources = declared_sources(text)
    for foundation in record["foundations"]:
        allowed = {"decision", "source_ids", "application", "source_titles", "locators"}
        if not {"decision", "source_ids", "application"}.issubset(foundation) or not set(foundation).issubset(allowed):
            errors.append(f"{class_id}: malformed foundation")
            continue
        if len(foundation["decision"]) < 40 or len(foundation["application"]) < 40:
            errors.append(f"{class_id}: foundation explanation is too short")
        if record["review_method"] == "manual-editorial-pilot":
            for source_id in foundation["source_ids"]:
                if source_id not in sources:
                    errors.append(f"{class_id}: foundation cites undeclared source {source_id}")
                if f'<a id="FUENTE-{source_id}"></a>' not in text:
                    errors.append(f"{class_id}: source anchor is missing for {source_id}")
        else:
            for locator in foundation.get("locators", []):
                if locator not in text:
                    errors.append(f"{class_id}: foundation locator is absent from lesson sources: {locator}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    manifest = json.loads(DECISIONS.read_text(encoding="utf-8"))
    known = {item["id"] for item in catalog}
    contracts = {item["class_id"]: item for item in manifest["decisions"]}
    errors: list[str] = []
    if manifest.get("schema_version") != 2:
        errors.append("decision manifest must use schema version 2")
    if set(contracts) != known:
        errors.append("decision manifest must contain exactly ARQ-001..ARQ-680")

    coverage = Counter()
    titles = Counter()
    generated_signatures = Counter()
    for item in catalog:
        text = (ROOT / item["source"]).read_text(encoding="utf-8")
        headings = "\n".join(re.findall(r"^#{2,3}\s+(.+)$", text, re.MULTILINE)).lower()
        titles[normalize(item["title"])] += 1
        coverage.update({
            "question": int("pregunta central" in headings),
            "activity": int(bool(re.search(r"práctica|ejercicio", headings))),
            "evidence": int("**Evidencia mínima:**" in text),
            "sources": int("fuentes y alcance" in headings),
            "errors": int("errores" in headings),
            # Una cita dentro del desarrollo mejora la lectura, pero no sustituye
            # la trazabilidad obligatoria de la decisión. Se informa por separado.
            "narrative_inline_citation": int(bool(re.search(r"\[\[[^\]]+\]\]\(#FUENTE-", text))),
            "visible_source_traceability": int(
                "## Trazabilidad de las decisiones" in text
                and "## Fuentes y alcance de uso" in text
                and bool(contracts.get(item["id"], {}).get("foundations"))
            ),
            "reviewed_decision_contract": int(item["id"] in contracts),
        })
        match = re.search(r"<!-- pedagogia-2026:inicio -->(.*?)<!-- pedagogia-2026:fin -->", text, re.DOTALL)
        if match:
            signature = re.sub(r"ARQ-\d{3}|\[\".*?\"\]", "<variable>", match.group(1))
            generated_signatures[signature] += 1
        if item["id"] in contracts:
            errors.extend(validate_contract(contracts[item["id"]], known, text))

    duplicate_titles = sum(count > 1 for count in titles.values())
    report = {
        "classes": len(catalog),
        "measured_coverage": dict(coverage),
        "reviewed_decision_contracts": len(contracts),
        "manual_editorial_pilots": sum(record["review_method"] == "manual-editorial-pilot" for record in contracts.values()),
        "corpus_reviewed_contracts": sum(record["review_method"] != "manual-editorial-pilot" for record in contracts.values()),
        "pending_decision_contracts": len(catalog) - len(contracts),
        "largest_reused_generated_template": max(generated_signatures.values(), default=0),
        "duplicate_normalized_titles": duplicate_titles,
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else (
        f"Pedagogical audit: {len(contracts)}/{len(catalog)} reviewed decisions · "
        f"{len(catalog) - len(contracts)} pending"
    ))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
