#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate curriculum truth, UTF-8 text, generated pages and internal links."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_RESOURCES = {
    "fuentes": 611,
    "roles": 80,
    "plantillas": 36,
    "documentos": 16,
    "rutas": 12,
}
APACHE_2_LICENSE_SHA256 = "c95bae1d1ce0235ecccd3560b772ec1efb97f348a79f0fbe0a634f0c2ccefe2c"
REQUIRED_LEGAL_FILES = (
    "LICENSE",
    "LICENSE-CONTENT.md",
    "DATA_LICENSES.md",
    "ASSET_LICENSES.md",
    "THIRD_PARTY_NOTICES.md",
    "TRADEMARKS.md",
    "LICENSING_AUDIT.md",
    "DCO",
    "docs/LICENSING_MATRIX.md",
    "docs/COMMERCIAL_USE.md",
    "docs/LICENSING_HISTORY.md",
    "docs/NORMATIVE_BOUNDARY.md",
)


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
    if not (ROOT / "classes" / "README.md").is_file():
        fail("missing classes/README.md curriculum index")
    part_readmes = list((ROOT / "classes").glob("parte-*/README.md"))
    if len(part_readmes) != 68:
        fail(f"found {len(part_readmes)} part README files, expected 68")

    coverage_patterns = {
        "question": r"pregunta central",
        "practice": r"práctica|ejercicio",
        "sources": r"fuentes y alcance",
        "result": r"resultado|qué aprenderás",
        "case": r"caso",
        "self_assessment": r"autoevaluación|solución razonada",
        "continuity": r"continuidad|siguiente|enlace",
        "errors": r"errores",
    }
    coverage = Counter()
    for item in catalog:
        text = (ROOT / item["source"]).read_text(encoding="utf-8")
        headings = "\n".join(re.findall(r"^##\s+(.+)$", text, re.MULTILINE)).lower()
        for label, pattern in coverage_patterns.items():
            coverage[label] += bool(re.search(pattern, headings))
    expected_coverage = {
        "question": 680,
        "practice": 680,
        "sources": 680,
        "result": 645,
        "case": 532,
        "self_assessment": 650,
        "continuity": 555,
        "errors": 284,
    }
    if dict(coverage) != expected_coverage:
        fail(
            "class documentation coverage changed; update the status document "
            f"from measured data: {dict(coverage)}"
        )

    reader_text = (
        ROOT / "programa-arquitectura-lector-definitivo-v1.0.html"
    ).read_text(encoding="utf-8")
    marker = "const ENTRIES="
    start = reader_text.index(marker) + len(marker)
    end = reader_text.index("];\nconst byId", start) + 1
    legacy = json.loads(reader_text[start:end])
    legacy_counts = Counter(entry["kind"] for entry in legacy)
    expected_legacy = Counter(
        {
            "redactada": 680,
            "fuente": 611,
            "rol": 80,
            "plantilla": 36,
            "documento": 16,
            "ruta": 12,
        }
    )
    if legacy_counts != expected_legacy:
        fail(f"legacy resource counts changed: {dict(legacy_counts)}")
    domains = set()
    for entry in legacy:
        if entry["kind"] != "fuente":
            continue
        for url in re.findall(r'https?://[^\s<"]+', entry["html"]):
            domains.add(urlsplit(url.rstrip(".,);")).netloc.lower().removeprefix("www."))
    if len(domains) != 177:
        fail(f"source-domain count changed: {len(domains)}")

    bibliography = json.loads(
        (ROOT / "sources" / "bibliography.json").read_text(encoding="utf-8")
    )
    bibliography_truth = (
        bibliography["class_count"],
        bibliography["citation_occurrences"],
        bibliography["unique_sources"],
        bibliography["unique_domains"],
        len(bibliography["entries"]),
    )
    if bibliography_truth != (680, 1939, 622, 189, 622):
        fail(f"derived bibliography changed: {bibliography_truth}")
    for entry in bibliography["entries"]:
        if not entry["locator"].startswith("https://") or not entry["used_in"]:
            fail(f"incomplete bibliography entry: {entry['id']}")
        required_source_fields = {
            "type",
            "title",
            "locator",
            "publisher_or_author",
            "authority_domain",
            "license",
            "redistribution",
            "used_in",
            "uses",
        }
        if not required_source_fields.issubset(entry):
            fail(f"source traceability fields missing: {entry['id']}")
        if entry["redistribution"] != "link-only":
            fail(f"external source is not link-only: {entry['id']}")
        if entry["license"].get("status") not in {"unknown", "declared-in-class"}:
            fail(f"invalid source license status: {entry['id']}")
        if entry["used_in"] != [use["class"] for use in entry["uses"]]:
            fail(f"source use records disagree: {entry['id']}")
        for use in entry["uses"]:
            if set(use) != {
                "class",
                "function",
                "consultation_scope",
                "limitation",
                "accessed_on",
            }:
                fail(f"incomplete per-class source record: {entry['id']}")
    if bibliography.get("schema_version") != 2:
        fail("bibliography must use traceability schema version 2")

    for required_license in REQUIRED_LEGAL_FILES:
        if not (ROOT / required_license).is_file():
            fail(f"missing license or notice: {required_license}")
    license_digest = hashlib.sha256((ROOT / "LICENSE").read_bytes()).hexdigest()
    if license_digest != APACHE_2_LICENSE_SHA256:
        fail("LICENSE is not the verified, unmodified Apache License 2.0 text")

    code_files = sorted((ROOT / "scripts").glob("*.py")) + sorted(
        (ROOT / ".github" / "workflows").glob("*.yml")
    ) + [ROOT / ".github" / "pull_request_template.md"]
    for path in code_files:
        opening = "\n".join(path.read_text(encoding="utf-8").splitlines()[:5])
        if "SPDX-License-Identifier: Apache-2.0" not in opening:
            fail(f"missing Apache-2.0 SPDX identifier: {path.relative_to(ROOT)}")

    assets_notice = (ROOT / "ASSET_LICENSES.md").read_text(encoding="utf-8")
    assets = [path for path in (ROOT / "assets").rglob("*") if path.is_file()]
    assets += [path for path in ROOT.glob("*.pdf") if path.is_file()]
    assets += [
        ROOT / "programa-arquitectura-lector-definitivo-v1.0.html",
    ]
    for path in assets:
        relative = path.relative_to(ROOT).as_posix()
        if f"`{relative}`" not in assets_notice:
            fail(f"asset is not inventoried: {relative}")

    data_notice = (ROOT / "DATA_LICENSES.md").read_text(encoding="utf-8")
    datasets = sorted((ROOT / "data").glob("*.json")) + sorted(
        (ROOT / "sources").glob("*.json")
    ) + [ROOT / "STATUS_v1.0.json"]
    for path in datasets:
        relative = path.relative_to(ROOT).as_posix()
        if f"`{relative}`" not in data_notice:
            fail(f"dataset is not inventoried: {relative}")

    content_license = (ROOT / "LICENSE-CONTENT.md").read_text(encoding="utf-8")
    trademarks = (ROOT / "TRADEMARKS.md").read_text(encoding="utf-8")
    matrix = (ROOT / "docs" / "LICENSING_MATRIX.md").read_text(encoding="utf-8")
    if "Copyright © 2026 Vladimir Acuña" not in content_license:
        fail("content copyright notice is missing")
    for marker in ("assets/mark.svg", "CC BY-NC-SA 4.0", "no añade una restricción de copyright"):
        if marker not in assets_notice + "\n" + trademarks:
            fail(f"copyright/trademark boundary is missing: {marker}")
    for marker in (
        "scripts/*.py",
        "classes/parte-XX/ARQ-XXX.md",
        "sources/bibliography.json",
        "programa-arquitectura-lector-definitivo-v1.0.html",
        "site/",
    ):
        if marker not in matrix:
            fail(f"licensing matrix is missing family: {marker}")

    legal_text = "\n".join(
        (ROOT / path).read_text(encoding="utf-8")
        for path in REQUIRED_LEGAL_FILES
        if path not in {"LICENSE", "DCO"}
    )
    placeholder = re.search(r"\b(?:TODO|TBD|PLACEHOLDER|INSERT HERE)\b", legal_text)
    if placeholder:
        fail(f"placeholder in licensing documents: {placeholder.group(0)}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "Apache--2.0",
        "CC%20BY--NC--SA%204.0",
        "GitHub stars",
        "GitHub forks",
        "followers",
        "Procedencia editorial",
        "matriz real de licencias",
        "Uso comercial",
    ):
        if marker not in readme:
            fail(f"README is missing required publication marker: {marker}")

    forbidden = ("mÃ", "Ã¡", "Ã©", "Ã³", "Â·", "ðŸ", "â€“", "â€”")
    for path in ROOT.rglob("*.md"):
        if (
            ".reference-modern-cybersecurity-program" in path.parts
            or ".vendor" in path.parts
        ):
            continue
        text = path.read_text(encoding="utf-8")
        if any(token in text for token in forbidden):
            fail(f"possible mojibake: {path.relative_to(ROOT)}")

    markdown_broken = []
    for page in ROOT.rglob("*.md"):
        if (
            ".reference-modern-cybersecurity-program" in page.parts
            or ".vendor" in page.parts
        ):
            continue
        text = page.read_text(encoding="utf-8")
        for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            raw = raw.strip()
            if raw.startswith("<") and ">" in raw:
                raw = raw[1 : raw.index(">")]
            else:
                raw = raw.split(maxsplit=1)[0]
            parsed = urlsplit(raw)
            if (
                not raw
                or raw.startswith(("#", "//"))
                or parsed.scheme
                or not parsed.path
            ):
                continue
            target = (
                ROOT / unquote(parsed.path).lstrip("/")
                if parsed.path.startswith("/")
                else page.parent / unquote(parsed.path)
            ).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                markdown_broken.append(
                    f"{page.relative_to(ROOT)} -> {raw} (outside repository)"
                )
                continue
            if not target.exists():
                markdown_broken.append(f"{page.relative_to(ROOT)} -> {raw}")
    if markdown_broken:
        fail("broken Markdown links:\n" + "\n".join(markdown_broken[:25]))

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
        part_pages = list((site / "partes").glob("parte-*.html"))
        if len(part_pages) != 68:
            fail(f"generated site has {len(part_pages)} part pages, expected 68")
        for folder, expected_count in EXPECTED_RESOURCES.items():
            resource_pages = [path for path in (site / folder).glob("*.html") if path.name != "index.html"]
            if len(resource_pages) != expected_count:
                fail(
                    f"generated site has {len(resource_pages)} pages in {folder}, "
                    f"expected {expected_count}"
                )
        for required in (
            "index.html",
            "catalogo.html",
            "recursos.html",
            "documentacion.html",
            "partes/index.html",
            "metodo.html",
            "artefactos.html",
            "estado.html",
            "fuentes-y-evidencia.html",
            "como-usar.html",
            "rutas-de-aprendizaje.html",
            "roles-y-oficios.html",
            "casos-integradores.html",
            "auditoria-documental.html",
            "procedencia-editorial.html",
            "licencias-y-derechos.html",
            "matriz-licencias.html",
            "uso-comercial.html",
            "historia-licencias.html",
            "frontera-normativa.html",
            "matriz-paridad-referencia.html",
            "seguridad-etica-profesional.html",
            "bibliografia.html",
            "sources/bibliography.json",
            ".nojekyll",
        ):
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
        generated_notice = (site / "index.html").read_text(encoding="utf-8")
        if "Cada componente conserva su régimen" not in generated_notice:
            fail("generated site is missing the layered-license notice")
    print(
        "OK: 680 lessons · 68 parts · 755 resources · "
        "69 curriculum README files · 622 source URLs · licensing matrix · "
        "Markdown links · checksums · UTF-8 · generated site"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
