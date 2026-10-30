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
    for number in range(831, 841):
        text = (ROOT / "classes" / "parte-84" / f"ARQ-{number}.md").read_text(encoding="utf-8")
        if "no certifica" not in text and "no es " not in text:
            fail(f"ARQ-{number}: professional-limit statement missing")


def main() -> int:
    cards = check_cases()
    check_route()
    check_arithmetic()
    print(f"OK: {cards} case cards, RUTA-35 and Part 84 didactic calculations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
