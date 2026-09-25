#!/usr/bin/env python3
"""Validate curriculum truth, UTF-8 text, generated pages and internal links."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    catalog = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    ids = [item["id"] for item in catalog]
    expected = [f"ARQ-{number:03d}" for number in range(1, 681)]
    if ids != expected:
        fail("catalog must contain exactly ARQ-001..ARQ-680")
    parts = {part: 0 for part in range(1, 69)}
    for item in catalog:
        source = ROOT / item["source"]
        if not source.is_file():
            fail(f"missing source: {item['source']}")
        text = source.read_text(encoding="utf-8")
        if not text.startswith(f"# {item['id']}"):
            fail(f"heading/id mismatch: {item['source']}")
        parts[item["part"]] += 1
    if set(parts.values()) != {10}:
        fail(f"every part must have 10 lessons: {parts}")

    forbidden = ("mÃ", "Ã¡", "Ã©", "Ã³", "Â·", "ðŸ", "â€“", "â€”")
    for path in ROOT.rglob("*.md"):
        if ".reference-modern-cybersecurity-program" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if any(token in text for token in forbidden):
            fail(f"possible mojibake: {path.relative_to(ROOT)}")

    status = json.loads((ROOT / "STATUS_v1.0.json").read_text(encoding="utf-8"))
    truth = (status["parts"], status["planned_classes"], status["written_classes"], status["pending_classes"])
    if truth != (68, 680, 680, 0):
        fail(f"STATUS_v1.0.json contradicts the curriculum: {truth}")

    sums = {}
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, filename = line.split(maxsplit=1)
            sums[filename.strip()] = digest.lower()
    for filename, digest in sums.items():
        path = ROOT / filename
        if not path.is_file():
            fail(f"checksum target is missing: {filename}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            fail(f"checksum mismatch: {filename}")

    site = ROOT / "site"
    if site.exists():
        pages = list((site / "clases").glob("arq-*.html"))
        if len(pages) != 680:
            fail(f"generated site has {len(pages)} lesson pages, expected 680")
        for required in ("index.html", "catalogo.html", "metodo.html", "artefactos.html", ".nojekyll"):
            if not (site / required).exists():
                fail(f"generated site is missing {required}")
        broken = []
        for page in site.rglob("*.html"):
            text = page.read_text(encoding="utf-8")
            for raw in re.findall(r'(?:href|src)="([^"]+)"', text):
                parsed = urlsplit(raw)
                if parsed.scheme or raw.startswith(("#", "mailto:", "//")) or not parsed.path:
                    continue
                target = (page.parent / unquote(parsed.path)).resolve()
                try:
                    target.relative_to(site.resolve())
                except ValueError:
                    broken.append(f"{page.relative_to(site)} -> {raw} (outside site)")
                    continue
                if not target.exists():
                    broken.append(f"{page.relative_to(site)} -> {raw}")
        if broken:
            fail("broken generated links:\n" + "\n".join(broken[:25]))
    print("OK: 680 lessons · 68 parts · checksums · UTF-8 · generated site")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
