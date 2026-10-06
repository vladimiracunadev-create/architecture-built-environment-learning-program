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
PROGRAM = json.loads((ROOT / "data" / "program.json").read_text(encoding="utf-8"))
EXPECTED_RESOURCES = {
    "fuentes": 611,
    "roles": 80,
    "plantillas": 36,
    "documentos": 16,
    "rutas": PROGRAM["route_count"],
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
    if PROGRAM["class_count"] != PROGRAM["part_count"] * PROGRAM["classes_per_part"]:
        fail("data/program.json class, part and class-per-part counts disagree")
    current_document_claims = {
        "docs/ARQUITECTURA_DE_EVALUACION.md": (
            f"| Clase | {PROGRAM['class_count']} |",
            f"| Parte | {PROGRAM['part_count']} |",
            f"| Ruta | {PROGRAM['route_count']} |",
        ),
        "docs/COMO_USAR_EL_PROGRAMA.md": (
            f"ARQ-001 → ARQ-{PROGRAM['class_count']:03d}.",
        ),
        "LICENSE-CONTENT.md": (
            f"las {PROGRAM['class_count']} clases, {PROGRAM['studio_session_count']} sesiones de taller",
            f"{PROGRAM['route_count']} rutas",
        ),
        "LICENSING_AUDIT.md": (
            f"{PROGRAM['class_count']} clases y {PROGRAM['part_count']} README de parte",
            "627 URLs externas únicas y 2.179 relaciones clase–fuente",
        ),
    }
    for relative, claims in current_document_claims.items():
        document = (ROOT / relative).read_text(encoding="utf-8")
        for claim in claims:
            if claim not in document:
                fail(f"current documentation claim is stale in {relative}: {claim}")
    if PROGRAM["studio_session_count"] != PROGRAM["studio_count"] * PROGRAM["sessions_per_studio"]:
        fail("data/program.json studio and session counts disagree")
    parts_manifest = json.loads(
        (ROOT / "data" / "parts.json").read_text(encoding="utf-8")
    )
    part_numbers = [item["number"] for item in parts_manifest.get("parts", [])]
    if part_numbers != list(range(1, PROGRAM["part_count"] + 1)):
        fail("data/parts.json must define every current part exactly once")
    if any(not item.get("title", "").strip() for item in parts_manifest["parts"]):
        fail("data/parts.json contains an empty title")
    catalog = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    ids = [item["id"] for item in catalog]
    expected = [f"ARQ-{number:03d}" for number in range(1, PROGRAM["class_count"] + 1)]
    if ids != expected:
        fail(f"catalog must contain exactly ARQ-001..ARQ-{PROGRAM['class_count']:03d}")
    parts = {part: 0 for part in range(1, PROGRAM["part_count"] + 1)}
    for item in catalog:
        source = ROOT / item["source"]
        if not source.is_file():
            fail(f"missing source: {item['source']}")
        text = source.read_text(encoding="utf-8")
        if not text.startswith(f"# {item['id']}"):
            fail(f"heading/id mismatch: {item['source']}")
        parts[item["part"]] += 1
    if set(parts.values()) != {PROGRAM["classes_per_part"]}:
        fail(f"every part must have {PROGRAM['classes_per_part']} lessons: {parts}")
    if not (ROOT / "classes" / "README.md").is_file():
        fail("missing classes/README.md curriculum index")
    part_readmes = list((ROOT / "classes").glob("parte-*/README.md"))
    if len(part_readmes) != PROGRAM["part_count"]:
        fail(f"found {len(part_readmes)} part README files, expected {PROGRAM['part_count']}")

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
        headings = "\n".join(re.findall(r"^#{2,3}\s+(.+)$", text, re.MULTILINE)).lower()
        for label, pattern in coverage_patterns.items():
            coverage[label] += bool(re.search(pattern, headings))
    expected_coverage = {
        "question": PROGRAM["class_count"],
        "practice": PROGRAM["class_count"],
        "sources": PROGRAM["class_count"],
        "result": PROGRAM["class_count"],
        "case": 690,
        "self_assessment": PROGRAM["class_count"],
        "continuity": PROGRAM["class_count"],
        "errors": PROGRAM["class_count"],
    }
    if dict(coverage) != expected_coverage:
        fail(
            "class documentation coverage changed; update the status document "
            f"from measured data: {dict(coverage)}"
        )

    pedagogy = json.loads((ROOT / "data" / "pedagogy.json").read_text(encoding="utf-8"))
    if pedagogy.get("schema_version") != 1:
        fail("pedagogy manifest must use schema version 1")
    if len(pedagogy.get("studios", [])) != PROGRAM["studio_count"] or len(pedagogy.get("routes", [])) != PROGRAM["route_count"]:
        fail("pedagogy manifest counts do not match data/program.json")
    studio_sessions = list((ROOT / "studios").glob("EST-??/EST-??-??.md"))
    if len(studio_sessions) != PROGRAM["studio_session_count"]:
        fail(f"found {len(studio_sessions)} studio sessions, expected {PROGRAM['studio_session_count']}")
    learning_paths = list((ROOT / "learning-paths").glob("ruta-??.md"))
    if len(learning_paths) != PROGRAM["route_count"]:
        fail(f"found {len(learning_paths)} learning paths, expected {PROGRAM['route_count']}")
    for item in catalog:
        text = (ROOT / item["source"]).read_text(encoding="utf-8")
        for marker in (
            "<!-- pedagogia-2026:inicio -->",
            "## Resultado observable, evidencia y evaluación",
            "**Criterio de aceptación:**",
            "## Autoevaluación, recuperación y continuidad",
            "<!-- pedagogia-2026:fin -->",
        ):
            if text.count(marker) != 1:
                fail(f"pedagogical contract missing or duplicated in {item['id']}: {marker}")
        if "```mermaid" not in text:
            fail(f"learning map missing in {item['id']}")

    historical_count = PROGRAM["historical_baseline"]["class_count"]
    phase_three = catalog[historical_count:]
    phase_three_questions = set()
    phase_three_critical_conditions = set()
    phase_three_topic_graphs = set()
    for item in phase_three:
        text = (ROOT / item["source"]).read_text(encoding="utf-8")
        question_match = re.search(r"## Pregunta central\s+(.+)", text)
        critical_match = re.search(
            r"\*\*Fallo crítico de esta clase:\*\* (.+?)\.", text
        )
        graph_match = re.search(r"```mermaid\n(.*?)```", text, re.DOTALL)
        if not all((question_match, critical_match, graph_match)):
            fail(f"Phase III class lacks distinct pedagogical anchors: {item['id']}")
        phase_three_questions.add(question_match.group(1).strip())
        phase_three_critical_conditions.add(critical_match.group(1).strip())
        phase_three_topic_graphs.add(graph_match.group(1).strip())
        if len(re.findall(r"\S+", text)) < 2500:
            fail(f"Phase III class is too shallow for the documented standard: {item['id']}")
    expected_phase_three = PROGRAM["class_count"] - historical_count
    if not all(
        len(values) == expected_phase_three
        for values in (
            phase_three_questions,
            phase_three_critical_conditions,
            phase_three_topic_graphs,
        )
    ):
        fail("Phase III questions, critical conditions and topic graphs must be class-specific")

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
    if bibliography["class_count"] != PROGRAM["class_count"]:
        fail("derived bibliography class count disagrees with data/program.json")
    if bibliography["unique_sources"] != len(bibliography["entries"]):
        fail("derived bibliography unique-source count disagrees with entries")
    if bibliography["citation_occurrences"] != sum(entry["usage_count"] for entry in bibliography["entries"]):
        fail("derived bibliography occurrence count disagrees with source uses")
    traceability = bibliography.get("traceability", {})
    minimum_field_coverage = {
        "function": 2112,
        "consultation_scope": 1722,
        "limitation": 1974,
        "accessed_on": 1295,
    }
    if traceability.get("required_context_fields") != list(minimum_field_coverage):
        fail("unexpected source traceability fields")
    if traceability.get("complete_uses", 0) < 1126:
        fail("complete source-use coverage regressed")
    if traceability.get("classes_with_all_uses_complete", 0) < 412:
        fail("class-level source traceability regressed")
    for field, minimum in minimum_field_coverage.items():
        if traceability.get("field_coverage", {}).get(field, 0) < minimum:
            fail(f"source traceability regressed for {field}")
    computed_complete_uses = 0
    computed_complete_classes = set()
    partial_classes = set()
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
                "traceability_status",
                "missing_fields",
            }:
                fail(f"incomplete per-class source record: {entry['id']}")
            expected_missing = [
                field for field in minimum_field_coverage if not use.get(field)
            ]
            if use["missing_fields"] != expected_missing:
                fail(f"incorrect missing source fields: {entry['id']}")
            expected_status = "complete" if not expected_missing else "partial"
            if use["traceability_status"] != expected_status:
                fail(f"incorrect source traceability status: {entry['id']}")
            if expected_status == "complete":
                computed_complete_uses += 1
                computed_complete_classes.add(use["class"])
            else:
                partial_classes.add(use["class"])
    if computed_complete_uses != traceability.get("complete_uses"):
        fail("source completeness summary disagrees with use records")
    all_complete_classes = computed_complete_classes - partial_classes
    if len(all_complete_classes) != traceability.get("classes_with_all_uses_complete"):
        fail("source class-completeness summary disagrees with use records")
    if bibliography.get("schema_version") != 3:
        fail("bibliography must use traceability schema version 3")

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
        "studios/",
        "data/pedagogy.json",
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
        fail(f"STATUS_v1.0.json no longer preserves the historical v1.0 baseline: {truth}")

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
        if len(pages) != PROGRAM["class_count"]:
            fail(f"generated site has {len(pages)} lesson pages, expected {PROGRAM['class_count']}")
        source_notices = sum(
            'data-source-traceability="true"' in page.read_text(encoding="utf-8")
            for page in pages
        )
        if source_notices != PROGRAM["class_count"]:
            fail(f"generated site has {source_notices} source-traceability notices")
        part_pages = list((site / "partes").glob("parte-*.html"))
        if len(part_pages) != PROGRAM["part_count"]:
            fail(f"generated site has {len(part_pages)} part pages, expected {PROGRAM['part_count']}")
        studio_pages = list((site / "talleres").glob("est-??/est-??-??.html"))
        if len(studio_pages) != PROGRAM["studio_session_count"]:
            fail(f"generated site has {len(studio_pages)} studio session pages, expected {PROGRAM['studio_session_count']}")
        route_pages = list((site / "rutas").glob("ruta-??.html"))
        if len(route_pages) != PROGRAM["route_count"]:
            fail(f"generated site has {len(route_pages)} learning paths, expected {PROGRAM['route_count']}")
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
            "matriz-cobertura-integral.html",
            "arquitectura-repositorio.html",
            "mapa-dependencias.html",
            "glosario.html",
            "informe-integracion-2026-10.html",
            "roadmap-integral.html",
            "partes/index.html",
            "metodo.html",
            "artefactos.html",
            "estado.html",
            "fuentes-y-evidencia.html",
            "estandar-fuentes.html",
            "estandar-documentacion-clase.html",
            "como-usar.html",
            "rutas-de-aprendizaje.html",
            "roles-y-oficios.html",
            "casos-integradores.html",
            "auditoria-documental.html",
            "auditoria-pedagogica.html",
            "procedencia-editorial.html",
            "licencias-y-derechos.html",
            "matriz-licencias.html",
            "uso-comercial.html",
            "historia-licencias.html",
            "frontera-normativa.html",
            "matriz-paridad-referencia.html",
            "seguridad-etica-profesional.html",
            "arquitectura-evaluacion.html",
            "rubrica-comun.html",
            "portafolio-evidencias.html",
            "estandar-visual.html",
            "syllabus-carga.html",
            "talleres/index.html",
            "rutas/index.html",
            "bibliografia.html",
            "bibliografia/catalogo.html",
            "sources/bibliography.json",
            ".nojekyll",
        ):
            if not (site / required).exists():
                fail(f"generated site is missing {required}")
        bibliography_catalog = (site / "bibliografia" / "catalogo.html").read_text(
            encoding="utf-8"
        )
        if bibliography_catalog.count('data-source-card="true"') != bibliography["unique_sources"]:
            fail("generated bibliography catalog does not contain every source")
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
        f"OK: {PROGRAM['class_count']} lessons · {PROGRAM['part_count']} parts · "
        f"{PROGRAM['studio_count']} studios · {PROGRAM['studio_session_count']} studio sessions · "
        f"{PROGRAM['route_count']} learning paths · 755 legacy resources · "
        f"{PROGRAM['part_count'] + 1} curriculum README files · "
        f"{bibliography['unique_sources']} source URLs · {traceability['complete_uses']} complete source uses · "
        "current documents · licensing matrix · "
        "Markdown links · checksums · UTF-8 · generated site"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
