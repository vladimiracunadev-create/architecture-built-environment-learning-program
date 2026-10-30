#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate the disaster-case library, RUTA-35 and the didactic calculations of Part 84.

This is a structural and arithmetic check.  Passing it does not establish that a case
is technically accurate, that a source says what a card claims, or that the material
is pedagogically effective; those need specialist review.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases" / "catastrofes-chile"
STATES = {"CONFIRMADO", "PRELIMINAR", "HIPÓTESIS", "SIN_DATOS"}
STATE_RE = re.compile(r"`([A-ZÁÉÍÓÚ_]+)`")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def clp(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def check_cases() -> int:
    readme = (CASES / "README.md").read_text(encoding="utf-8")
    cards = sorted(path for path in CASES.glob("CAT-*.md"))
    if not cards:
        fail("no case cards found")
    for card in cards:
        text = card.read_text(encoding="utf-8")
        if not text.startswith(f"# {card.stem} ·"):
            fail(f"{card.name}: heading must start with its identifier")
        general = re.search(r"\*\*Estado general:\*\* `([^`]+)`", text)
        if not general or general.group(1) not in STATES:
            fail(f"{card.name}: missing or invalid general state")
        used = {value for value in STATE_RE.findall(text) if value.isupper() and len(value) > 5}
        invalid = used - STATES
        if invalid:
            fail(f"{card.name}: unknown verification states {sorted(invalid)}")
        if "Límites de transferencia" not in text:
            fail(f"{card.name}: missing 'Límites de transferencia'")
        if general.group(1) in {"CONFIRMADO", "PRELIMINAR"} and not re.search(r"https://", text):
            fail(f"{card.name}: a verified or preliminary case needs at least one source URL")
        if general.group(1) != "SIN_DATOS" and "Consultad" not in text and "consultad" not in text:
            fail(f"{card.name}: state the consultation date or method")
        if f"({card.name})" not in readme:
            fail(f"{card.name}: not linked from the case registry")
        for relative in re.findall(r"\]\((?!https?://|#)([^)]+)\)", text):
            if not (card.parent / relative.split("#")[0]).exists():
                fail(f"{card.name}: broken relative link {relative}")
    return len(cards)


def check_route() -> None:
    pedagogy = json.loads((ROOT / "data" / "pedagogy.json").read_text(encoding="utf-8"))
    route = next((item for item in pedagogy["routes"] if item["id"] == "RUTA-35"), None)
    if route is None:
        fail("RUTA-35 is not registered")
    catalog = {item["id"] for item in json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))}
    sequence = route.get("class_sequence", [])
    if len(sequence) != len(set(sequence)) or not set(sequence) <= catalog:
        fail("RUTA-35 class_sequence has duplicates or unknown classes")
    for number in range(831, 841):
        if f"ARQ-{number}" not in sequence:
            fail(f"RUTA-35 omits ARQ-{number}")
    for case_file in route.get("case_files", []):
        if not (ROOT / case_file).is_file():
            fail(f"RUTA-35 case file missing: {case_file}")
    studio = next(item for item in pedagogy["studios"] if item["id"] == route["capstone"])
    if "RUTA-35" not in studio["route_ids"]:
        fail("RUTA-35 capstone studio does not list the route")


def check_arithmetic() -> None:
    reconstruction = round(90 * 850_000 * 1.12 * 1.10)
    ratio = 60_000_000 / reconstruction
    paid = round(20_000_000 * ratio)
    class_832 = (ROOT / "classes" / "parte-84" / "ARQ-832.md").read_text(encoding="utf-8")
    expected = {
        clp(reconstruction): "valor de reconstrucción",
        clp(round(paid, -3)): "indemnización proporcional",
        clp(reconstruction - 60_000_000): "retención en el escenario extremo",
    }
    for value, label in expected.items():
        if value not in class_832:
            fail(f"ARQ-832: {label} {value} not found")
    low = 525_000 + 130_000 + 48_000 + 158_400
    medium = 720_000 + 180_000 + 72_000 + 220_000
    high = 975_000 + 260_000 + 108_000 + 308_000
    class_839 = (ROOT / "classes" / "parte-84" / "ARQ-839.md").read_text(encoding="utf-8")
    for label, value in (("bajo", low), ("medio", medium), ("alto", high), ("total", round(medium * 1.15))):
        if clp(value) not in class_839:
            fail(f"ARQ-839: {label} total {clp(value)} not found")
    scenarios = ((0.05, 5_000_000), (0.01, 40_000_000), (0.002, reconstruction))
    gross = round(sum(prob * loss for prob, loss in scenarios))
    ratio_exact = 60_000_000 / reconstruction

    def retained(loss: int, proportional: bool) -> float:
        base = loss * ratio_exact if proportional else loss
        return loss - min(max(base - 300_000, 0), 60_000_000)

    with_rule = round(sum(prob * retained(loss, True) for prob, loss in scenarios))
    without_rule = round(sum(prob * retained(loss, False) for prob, loss in scenarios))
    for label, value in (("pérdida bruta", gross), ("retenida con regla", with_rule), ("retenida sin regla", without_rule)):
        if clp(value) not in class_832:
            fail(f"ARQ-832: {label} {clp(value)} not found")
    class_835 = (ROOT / "classes" / "parte-84" / "ARQ-835.md").read_text(encoding="utf-8")
    if clp(98_000_000 + 1_200_000 - 86_000_000) not in class_835 or "la brecha baja" in class_835:
        fail("ARQ-835: gap arithmetic is inconsistent")
    corrective = 3 * 650_000 + 480_000
    corrective_total = round(corrective * 1.15)
    for label, value in (
        ("correctivo", corrective_total),
        ("diferencia con cinco años preventivos", corrective_total - 5 * 210_000),
        ("esperado al 20 %", round(0.2 * corrective_total)),
    ):
        if clp(value) not in class_839:
            fail(f"ARQ-839: {label} {clp(value)} not found")

    solution = (ROOT / "cases" / "DECISION-INTEGRAL-RESILIENTE-SOLUCION.md").read_text(encoding="utf-8")
    annuity = (1 - 1.04**-20) / 0.04
    construction = 100 * 850_000
    terrains = {
        "A": dict(land=60_000_000, studies=2_800_000, mitigation=9_500_000, scenarios=((0.10, 4_000_000), (0.02, 22_000_000), (0.004, 60_000_000)), covered=False),
        "B": dict(land=38_000_000, studies=6_500_000, mitigation=18_000_000, scenarios=((0.05, 6_000_000), (0.01, 35_000_000), (0.003, 93_500_000)), covered=False),
        "C": dict(land=52_000_000, studies=2_200_000, mitigation=7_000_000, scenarios=((0.03, 8_000_000), (0.006, 45_000_000), (0.002, 93_500_000)), covered=True),
    }
    for name, data in terrains.items():
        initial = data["land"] + construction + data["studies"] + data["mitigation"]
        retained = [loss - (min(max(loss - 500_000, 0), 85_000_000) if data["covered"] else 0) for _, loss in data["scenarios"]]
        expected_retained = sum(prob * value for (prob, _), value in zip(data["scenarios"], retained))
        present_value = expected_retained * annuity
        for label, value in (
            ("costo inicial", initial),
            ("pérdida retenida", round(expected_retained)),
            ("valor presente", round(present_value)),
            ("total", round(initial + present_value)),
            ("extremo retenido", round(retained[-1])),
        ):
            if clp(value) not in solution:
                fail(f"integrated case, terrain {name}: {label} {clp(value)} not found")
    for number in range(831, 841):
        text = (ROOT / "classes" / "parte-84" / f"ARQ-{number}.md").read_text(encoding="utf-8")
        if "no certifica" not in text and "no es " not in text:
            fail(f"ARQ-{number}: professional-limit statement missing")



LEDGER = ROOT / "data" / "verificacion.json"
ARTICLE_RE = re.compile(r"arts?\.\s*((?:\d{2,3}(?:\s*n\.º\s*\d+(?:\s*y\s*\d+)?)?(?:\s*(?:,|y)\s*)?)+)")


def check_ledger() -> int:
    """Every article cited in ARQ-831..833 must exist in the verified-claims ledger."""
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    levels = set(ledger["levels"])
    instruments = set(ledger["instruments"])
    seen: set[str] = set()
    known_articles: set[str] = set()
    for claim in ledger["claims"]:
        if claim["id"] in seen:
            fail(f"verification ledger: duplicate claim {claim['id']}")
        seen.add(claim["id"])
        if claim["instrument"] not in instruments or claim["level"] not in levels:
            fail(f"verification ledger: invalid instrument or level in {claim['id']}")
        if not claim["claim"].strip() or not claim["used_in"]:
            fail(f"verification ledger: empty claim or usage in {claim['id']}")
        for used in claim["used_in"]:
            if used.startswith("ARQ-"):
                number = int(used[4:])
                target = ROOT / "classes" / f"parte-{(number - 1) // 10 + 1:02d}" / f"{used}.md"
            else:
                target = ROOT / used
            if not target.is_file():
                fail(f"verification ledger: {claim['id']} points to missing {used}")
        known_articles.add(claim["article"])
    for number in (831, 832, 833):
        text = (ROOT / "classes" / "parte-84" / f"ARQ-{number}.md").read_text(encoding="utf-8")
        cited = {value for match in ARTICLE_RE.findall(text) for value in re.findall(r"\d{2,3}", re.sub(r"n\.º\s*\d+(?:\s*y\s*\d+)?", "", match))}
        missing = cited - known_articles
        if missing:
            fail(f"ARQ-{number}: cited articles without a verified claim: {sorted(missing)}")
    return len(ledger["claims"])


REQUIRED_HEADINGS = {
    "pregunta central": r"^## Pregunta central",
    "problema y resultado": r"^## Problema y resultado",
    "mapa de la decisión": r"^## Mapa específico",
    "práctica guiada": r"^## Práctica guiada",
    "ejercicio independiente": r"^## Ejercicio independiente",
    "errores y recuperación": r"^## Errores típicos y recuperación",
    "evaluación por evidencias": r"^## Evaluación por evidencias",
    "continuidad": r"^## Continuidad",
    "fuentes": r"^## Fuentes y alcance de uso",
    "autoevaluación solucionada": r"^## Autoevaluación con solución razonada",
}


def check_part_84_standard() -> None:
    """Automated reading of docs/ESTANDAR_DOCUMENTACION_CLASE.md for the Part 84 classes."""
    for number in range(831, 841):
        name = f"ARQ-{number}"
        text = (ROOT / "classes" / "parte-84" / f"{name}.md").read_text(encoding="utf-8")
        for label, pattern in REQUIRED_HEADINGS.items():
            if not re.search(pattern, text, re.MULTILINE):
                fail(f"{name}: missing section '{label}'")
        if len(re.findall(r"^## .*[Cc]aso", text, re.MULTILINE)) < 1 or len(re.findall(r"[Cc]aso resuelto", text)) < 2:
            fail(f"{name}: needs at least two worked cases")
        if "**Fallo crítico de esta clase:**" not in text or "```mermaid" not in text:
            fail(f"{name}: missing critical failure or learning map")
        if "**Prerrequisitos recomendados:**" not in text:
            fail(f"{name}: missing prerequisites")
        opening = text[:900]
        if "Material educativo" not in opening:
            fail(f"{name}: missing educational-material statement in the opening")
        if "CLP" in text and "HIPOT" not in text.upper():
            fail(f"{name}: CLP amounts must be labeled HIPOTÉTICO")
        solved = re.search(r"## Autoevaluación con solución razonada\n(.*?)(?=\n## )", text, re.DOTALL)
        if not solved or len(re.findall(r"^\d+\. ", solved.group(1), re.MULTILINE)) < 5:
            fail(f"{name}: self-assessment needs at least five solved items")
        sources = re.findall(r"\*\*Fecha de consulta:\*\*", text)
        if len(sources) < 2:
            fail(f"{name}: needs at least two sources with consultation date")
        for match in re.finditer(r"(?i)garantiza(?:r|mos)?", text):
            context = text[max(0, match.start() - 25) : match.end()].lower()
            if "no " not in context and "ni " not in context:
                fail(f"{name}: unqualified wording near '{text[match.start() - 40 : match.end() + 20]}'")

def main() -> int:
    cards = check_cases()
    check_route()
    check_arithmetic()
    claims = check_ledger()
    check_part_84_standard()
    print(f"OK: {cards} case cards, RUTA-35, Part 84 calculations and standard, {claims} verified claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
