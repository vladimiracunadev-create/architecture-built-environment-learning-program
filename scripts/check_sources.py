#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Comprueba que las fuentes oficiales que el programa vigila sigan respondiendo.

Qué hace: pide cada localizador de `data/vigilancia.json` (y, con `--bibliography`, los de
`sources/bibliography.json`) con un identificador honesto de agente, registra el código HTTP y
escribe un informe en `docs/audits/source-check.md` y `data/audits/source-check.json`.

Qué NO hace: no lee el contenido, no detecta cambios normativos ni sustituye la revisión que
`vigilancia.json` asigna a cada ítem. Un enlace vivo no prueba que la norma siga vigente; un enlace
caído puede deberse a una protección del sitio y no a que la fuente haya desaparecido.

Uso:
    python scripts/check_sources.py                      # solo la lista de vigilancia
    python scripts/check_sources.py --bibliography 40    # además 40 URLs de la bibliografía
    python scripts/check_sources.py --strict             # sale con error si algún ítem de vigilancia falla
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import ssl
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WATCH = ROOT / "data" / "vigilancia.json"
BIBLIOGRAPHY = ROOT / "sources" / "bibliography.json"
JSON_OUT = ROOT / "data" / "audits" / "source-check.json"
MD_OUT = ROOT / "docs" / "audits" / "source-check.md"
AGENT = "architecture-built-environment-learning-program/source-check (+https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program)"


def probe(url: str, timeout: float = 20.0) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": AGENT}, method="GET")
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            return {"url": url, "status": response.status, "final_url": response.geturl(), "error": None}
    except urllib.error.HTTPError as error:
        return {"url": url, "status": error.code, "final_url": url, "error": error.reason}
    except Exception as error:  # noqa: BLE001 - la causa se registra, no se interpreta
        return {"url": url, "status": None, "final_url": url, "error": f"{type(error).__name__}: {error}"}


def classify(result: dict) -> str:
    status = result["status"]
    if status is not None and 200 <= status < 400:
        return "responde"
    if status in (401, 403, 429):
        return "bloquea clientes automáticos"
    if status is None:
        return "sin respuesta"
    return "error HTTP"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bibliography", type=int, default=0, help="número de URLs de la bibliografía a comprobar además")
    parser.add_argument("--strict", action="store_true", help="falla si algún ítem de vigilancia no responde")
    parser.add_argument("--no-write", action="store_true", help="no escribe informes")
    args = parser.parse_args()

    watch = json.loads(WATCH.read_text(encoding="utf-8"))["items"]
    targets = [(item["id"], item["title"], item["url"], item["frequency"]) for item in watch]
    if args.bibliography:
        entries = json.loads(BIBLIOGRAPHY.read_text(encoding="utf-8"))["entries"][: args.bibliography]
        targets += [(entry["id"], entry["title"], entry["locator"], "según uso") for entry in entries]

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda target: probe(target[2]), targets))

    rows = []
    for (identifier, title, url, frequency), result in zip(targets, results):
        rows.append({"id": identifier, "title": title, "frequency": frequency, "state": classify(result), **result})

    today = dt.date.today().isoformat()
    summary = {state: sum(1 for row in rows if row["state"] == state) for state in sorted({row["state"] for row in rows})}
    if not args.no_write:
        JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
        MD_OUT.parent.mkdir(parents=True, exist_ok=True)
        JSON_OUT.write_text(json.dumps({"checked_on": today, "summary": summary, "results": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        lines = [
            "# Comprobación de disponibilidad de fuentes",
            "",
            f"**Fecha:** {today}. Generado por `scripts/check_sources.py`. Comprueba que el localizador responda; **no** lee el contenido ni confirma vigencia normativa.",
            "",
            "| Estado | Cantidad |",
            "|---|---:|",
            *[f"| {state} | {count} |" for state, count in summary.items()],
            "",
            "| ID | Fuente | HTTP | Estado | Frecuencia de revisión |",
            "|---|---|---:|---|---|",
            *[f"| {row['id']} | {row['title'][:70]} | {row['status'] or '—'} | {row['state']} | {row['frequency']} |" for row in rows],
            "",
        ]
        MD_OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    for state, count in summary.items():
        print(f"{state}: {count}")
    failing = [row for row in rows if row["id"].startswith("VIG-") and row["state"] in {"sin respuesta", "error HTTP"}]
    if failing:
        for row in failing:
            print(f"  revisar {row['id']}: {row['title']} ({row['status'] or row['error']})")
    return 1 if (args.strict and failing) else 0


if __name__ == "__main__":
    raise SystemExit(main())
