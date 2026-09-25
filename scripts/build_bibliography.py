#!/usr/bin/env python3
"""Build a central source registry from the 680 class Markdown files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "sources" / "bibliography.json"
OUT_README = ROOT / "sources" / "README.md"
SOURCE_HEADING = "## Fuentes y alcance de uso"
URL_RE = re.compile(r"https?://[^\s)>\]]+")


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
    current = clean_label(lines[index])
    if len(current) >= 8:
        return current
    for offset in range(1, 5):
        if index - offset < 0:
            break
        candidate = clean_label(lines[index - offset])
        if candidate and not candidate.lower().startswith(("uso y límite", "consulta:", "apoyo:", "límite:")):
            return candidate
    return "Fuente externa"


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
    if len(files) != 680:
        raise SystemExit(f"expected 680 class files, found {len(files)}")

    records: dict[str, dict] = {}
    citations = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        if SOURCE_HEADING not in text:
            raise SystemExit(f"missing source section: {path.relative_to(ROOT)}")
        section = text.split(SOURCE_HEADING, 1)[1]
        lines = section.splitlines()
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
                record = records.setdefault(
                    url,
                    {
                        "id": f"source-{re.sub(r'[^a-z0-9]+', '-', domain).strip('-')}-{hashlib.sha1(url.encode()).hexdigest()[:10]}",
                        "type": source_type(domain),
                        "title": title_for(lines, index),
                        "locator": url,
                        "authority_domain": domain,
                        "status": "registrada-no-verificada-en-vivo",
                        "used_in": [],
                    },
                )
                if relative not in record["used_in"]:
                    record["used_in"].append(relative)

    entries = sorted(records.values(), key=lambda item: (item["authority_domain"], item["title"], item["locator"]))
    for entry in entries:
        entry["usage_count"] = len(entry["used_in"])

    return {
        "schema_version": 1,
        "generated_from": "classes/parte-XX/ARQ-XXX.md",
        "generated_on": "2026-09-24",
        "policy": (
            "Registro derivado de las secciones 'Fuentes y alcance de uso'. "
            "Una URL registrada demuestra trazabilidad editorial, no vigencia, lectura íntegra, "
            "aplicabilidad normativa ni respaldo institucional."
        ),
        "class_count": len(files),
        "citation_occurrences": citations,
        "unique_sources": len(entries),
        "unique_domains": len({entry["authority_domain"] for entry in entries}),
        "entries": entries,
    }


def render_readme(registry: dict) -> str:
    domains = Counter(entry["authority_domain"] for entry in registry["entries"])
    rows = "\n".join(f"| `{domain}` | {count} |" for domain, count in domains.most_common(20))
    return f"""# Registro central de fuentes

Este directorio responde de forma auditable a **qué fuentes utiliza cada clase**.

| Medida | Resultado |
|---|---:|
| Clases inspeccionadas | **{registry['class_count']}** |
| Apariciones de URL en fuentes | **{registry['citation_occurrences']}** |
| URLs externas únicas | **{registry['unique_sources']}** |
| Dominios únicos | **{registry['unique_domains']}** |

El registro completo está en [`bibliography.json`](bibliography.json). Cada entrada contiene el localizador, un título editorial recuperado, el dominio de autoridad y todas las clases que lo usan.

## Procedencias más frecuentes

| Dominio | URLs únicas |
|---|---:|
{rows}

## Qué demuestra y qué no

El registro demuestra que una URL aparece en la sección de fuentes de una clase y permite localizar sus usos. No demuestra que la fuente siga disponible, que se haya leído íntegramente, que sea aplicable en una jurisdicción concreta ni que su institución respalde el programa.

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
            f"{registry['citation_occurrences']} citations and {registry['unique_domains']} domains"
        )
        return 0

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    for path, value in expected.items():
        path.write_text(value, encoding="utf-8", newline="\n")
    print(
        f"Built {registry['unique_sources']} unique source URLs, "
        f"{registry['citation_occurrences']} citations and {registry['unique_domains']} domains"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
