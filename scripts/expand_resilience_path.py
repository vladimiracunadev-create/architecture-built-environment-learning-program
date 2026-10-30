#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Register Part 84 (ARQ-831..840) in the canonical manifests.

The lesson Markdown is authored by hand in classes/parte-84/.  This helper only
updates data/program.json, data/parts.json, data/catalog.json and RUTA-35 so the
existing generators and validators can take over.  It is idempotent.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_NUMBER = 84
PART_TITLE = "Evaluación de inmuebles, seguros y eventos catastróficos"
FIRST, LAST = 831, 840


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def title_of(number: int) -> str:
    source = ROOT / "classes" / f"parte-{PART_NUMBER}" / f"ARQ-{number:03d}.md"
    first = source.read_text(encoding="utf-8").splitlines()[0]
    return re.sub(rf"^#\s+ARQ-{number:03d}\s*·\s*", "", first).strip()


def main() -> int:
    program_path = ROOT / "data" / "program.json"
    program = read(program_path)
    program["class_count"] = LAST
    program["part_count"] = PART_NUMBER
    for phase in program["phases"]:
        if phase["id"] == "IV":
            phase["title"] = "aplicación práctica para propietarios y operaciones inmobiliarias"
            phase["last_part"] = PART_NUMBER
            phase["last_class"] = f"ARQ-{LAST:03d}"
    write(program_path, program)

    parts_path = ROOT / "data" / "parts.json"
    parts = read(parts_path)
    parts["parts"] = [item for item in parts["parts"] if item["number"] != PART_NUMBER]
    parts["parts"].append({"number": PART_NUMBER, "title": PART_TITLE})
    write(parts_path, parts)

    catalog_path = ROOT / "data" / "catalog.json"
    catalog = [item for item in read(catalog_path) if int(item["id"][4:]) < FIRST]
    for number in range(FIRST, LAST + 1):
        catalog.append(
            {
                "id": f"ARQ-{number:03d}",
                "title": title_of(number),
                "part": PART_NUMBER,
                "is_new": True,
                "source": f"classes/parte-{PART_NUMBER}/ARQ-{number:03d}.md",
            }
        )
    write(catalog_path, catalog)
    print(f"Registered Part {PART_NUMBER} (ARQ-{FIRST:03d}..ARQ-{LAST:03d}) in canonical manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
