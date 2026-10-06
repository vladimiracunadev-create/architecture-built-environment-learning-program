#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build the GitHub Pages site from the Markdown source of all lessons."""

from __future__ import annotations

import html
import json
import re
import shutil
from collections import Counter
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
CATALOG_PATH = ROOT / "data" / "catalog.json"
PEDAGOGY_PATH = ROOT / "data" / "pedagogy.json"
BIBLIOGRAPHY_PATH = ROOT / "sources" / "bibliography.json"
PROGRAM_PATH = ROOT / "data" / "program.json"
PARTS_PATH = ROOT / "data" / "parts.json"
READER = ROOT / "programa-arquitectura-lector-definitivo-v1.0.html"
REPO_URL = "https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program"
PAGES_URL = "https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/"
STARS_URL = f"{REPO_URL}/stargazers"
PROGRAM = json.loads(PROGRAM_PATH.read_text(encoding="utf-8"))

CSS = r"""
:root{--ink:#172526;--muted:#5a6967;--paper:#f4f0e7;--card:#fffdf7;--line:#d9d4c8;--navy:#102f38;--teal:#1d6b68;--clay:#b85c38;--gold:#ddb967;--focus:#0067c5;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.65}a{color:var(--teal);text-underline-offset:3px}.skip{position:absolute;top:-80px;left:1rem;background:#fff;padding:.7rem 1rem;z-index:50}.skip:focus{top:1rem}.topbar{position:sticky;top:0;z-index:20;background:rgba(16,47,56,.96);color:#fff;border-bottom:1px solid rgba(255,255,255,.16);backdrop-filter:blur(12px)}.topbar .inner{max-width:1180px;margin:auto;padding:.72rem 1.25rem;display:flex;align-items:center;justify-content:space-between;gap:1rem}.brand{font-weight:800;color:#fff;text-decoration:none;letter-spacing:.02em}.nav{display:flex;gap:1rem;flex-wrap:wrap}.nav a{color:#eaf2ef;text-decoration:none;font-size:.9rem}.hero{position:relative;overflow:hidden;color:#fff;background:linear-gradient(135deg,#0e2932 0%,#164e52 62%,#8d472f 145%);padding:6rem 1.25rem 5rem}.hero:before{content:"";position:absolute;inset:0;opacity:.12;background-image:linear-gradient(#fff 1px,transparent 1px),linear-gradient(90deg,#fff 1px,transparent 1px);background-size:36px 36px;mask-image:linear-gradient(to bottom,#000,transparent)}.hero .inner{position:relative;max-width:1180px;margin:auto}.eyebrow{text-transform:uppercase;letter-spacing:.17em;font-size:.74rem;color:#ecd99f;font-weight:800}.hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(2.4rem,6vw,5.3rem);line-height:.98;max-width:900px;margin:.7rem 0 1.2rem;letter-spacing:-.035em}.hero p{font-size:clamp(1rem,2vw,1.28rem);max-width:760px;color:#e7efec}.actions{display:flex;gap:.75rem;flex-wrap:wrap;margin-top:1.8rem}.button{display:inline-block;padding:.72rem 1.05rem;border:1px solid rgba(255,255,255,.35);border-radius:7px;color:#fff;text-decoration:none;font-weight:750}.button.primary{background:var(--gold);color:#172526;border-color:var(--gold)}.wrap{max-width:1180px;margin:auto;padding:0 1.25rem}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin:-1.5rem auto 3rem;position:relative}.stat{background:var(--card);padding:1.35rem}.stat strong{font-family:Georgia,serif;font-size:2.1rem;color:var(--clay);display:block;line-height:1}.stat span{font-size:.84rem;color:var(--muted)}.section{padding:2.5rem 0}.section h2{font-family:Georgia,serif;font-size:clamp(1.8rem,3vw,2.5rem);margin:0 0 .6rem}.lede{color:var(--muted);max-width:760px;margin:0 0 1.5rem}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.card{background:var(--card);border:1px solid var(--line);padding:1.25rem;border-radius:8px}.card .num{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:var(--clay);font-weight:800}.card h3{margin:.35rem 0;font-size:1.05rem}.card p{margin:.3rem 0;color:var(--muted);font-size:.92rem}.catalog-tools{display:grid;grid-template-columns:1fr 220px;gap:.8rem;margin:1.5rem 0}.catalog-tools input,.catalog-tools select{width:100%;padding:.8rem;border:1px solid var(--line);border-radius:6px;background:var(--card);font:inherit}.catalog-list{display:grid;grid-template-columns:repeat(2,1fr);gap:.7rem}.lesson-link{display:flex;gap:.8rem;align-items:flex-start;background:var(--card);border:1px solid var(--line);padding:.9rem;border-radius:7px;text-decoration:none;color:var(--ink)}.lesson-link:hover{border-color:var(--teal);transform:translateY(-1px)}.lesson-code{font-size:.72rem;color:var(--clay);font-weight:850;white-space:nowrap}.lesson-title{font-size:.92rem;line-height:1.35}.doc{max-width:900px;margin:2.5rem auto 5rem;background:var(--card);border:1px solid var(--line);padding:clamp(1.2rem,4vw,3.4rem);box-shadow:0 18px 50px rgba(22,43,43,.08)}.doc h1{font-family:Georgia,serif;font-size:clamp(2rem,4vw,3.25rem);line-height:1.05;margin-top:.3rem}.doc h2{font-family:Georgia,serif;font-size:1.65rem;margin-top:2.4rem;padding-top:1rem;border-top:1px solid var(--line)}.doc h3{margin-top:1.8rem}.doc table{display:block;overflow:auto;border-collapse:collapse;margin:1.2rem 0}.doc th,.doc td{border:1px solid var(--line);padding:.65rem;min-width:120px;text-align:left;vertical-align:top}.doc th{background:#ebe6da}.doc blockquote{margin:1.2rem 0;border-left:4px solid var(--clay);padding:.2rem 1rem;color:var(--muted)}.doc code{background:#ece9df;padding:.12rem .3rem;border-radius:4px}.doc pre{overflow:auto;background:#172526;color:#f4f0e7;padding:1rem;border-radius:7px}.lesson-nav{display:grid;grid-template-columns:1fr 1fr;gap:1rem;border-top:1px solid var(--line);margin-top:2.6rem;padding-top:1.2rem}.lesson-nav a:last-child{text-align:right}.kicker{font-size:.76rem;text-transform:uppercase;letter-spacing:.13em;color:var(--clay);font-weight:850}.notice{background:#eef3ec;border-left:4px solid var(--teal);padding:.9rem 1rem;margin:1rem 0}.footer{background:var(--navy);color:#dbe7e3;margin-top:3rem}.footer .inner{max-width:1180px;margin:auto;padding:2rem 1.25rem;display:flex;justify-content:space-between;gap:2rem;flex-wrap:wrap}.footer a{color:#fff}.footer small{max-width:680px}.hide{display:none!important}
@media(max-width:780px){.nav{display:none}.hero{padding:4rem 1.1rem}.stats{grid-template-columns:repeat(2,1fr)}.grid,.catalog-list{grid-template-columns:1fr}.catalog-tools{grid-template-columns:1fr}.doc{margin:1rem .7rem 3rem;padding:1.15rem}.lesson-nav{grid-template-columns:1fr}.lesson-nav a:last-child{text-align:left}}
@media print{.topbar,.footer,.lesson-nav{display:none}.doc{border:0;box-shadow:none;margin:0;max-width:none;padding:0}body{background:#fff}.doc a{color:inherit}}
"""

CSS += r"""
.status-table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line)}.status-table th,.status-table td{padding:.85rem;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.status-table th{background:#ebe6da}.status-ok{color:var(--teal);font-weight:850}.status-pending{color:#8d472f;font-weight:850}.resource-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}.resource-card{display:block;background:var(--card);border:1px solid var(--line);border-top:4px solid var(--clay);padding:1.2rem;text-decoration:none;color:var(--ink);border-radius:7px}.resource-card strong{display:block;font-family:Georgia,serif;font-size:1.75rem;color:var(--clay)}.resource-card span{font-size:.9rem;color:var(--muted)}.part-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:.8rem}.part-card{background:var(--card);border:1px solid var(--line);padding:1rem;border-radius:7px;text-decoration:none;color:var(--ink)}.part-card small{display:block;color:var(--clay);font-weight:850}.part-card strong{display:block;margin:.2rem 0}.part-card span{font-size:.85rem;color:var(--muted)}.band{background:#e7e1d5;border-block:1px solid var(--line);margin:2rem 0}.prose{max-width:820px}.meta-line{color:var(--muted);font-size:.9rem}.inventory-list{display:grid;grid-template-columns:repeat(2,1fr);gap:.65rem}.inventory-link{background:var(--card);border:1px solid var(--line);padding:.9rem;border-radius:7px;text-decoration:none;color:var(--ink)}.inventory-link small{display:block;color:var(--clay);font-weight:800}.callout{background:#183f45;color:#eff7f3;padding:1.3rem;border-radius:8px}.callout a{color:#f4d987}@media(max-width:900px){.resource-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:780px){.part-grid,.inventory-list{grid-template-columns:1fr}}@media(max-width:480px){.resource-grid{grid-template-columns:1fr}}
"""

CSS += ".resource-card b{display:block;margin:.15rem 0 .35rem}.resource-card span{display:block}\n"

RESOURCE_TYPES = {
    "rol": ("roles", "Roles y oficios", "personas, responsabilidades y límites del trabajo"),
    "ruta": ("rutas", "Rutas de aprendizaje", "recorridos guiados a través del currículo"),
    "plantilla": ("plantillas", "Plantillas", "instrumentos para registrar decisiones y evidencia"),
    "documento": ("documentos", "Documentos transversales", "método, alcance, estado y continuidad"),
    "fuente": ("fuentes", "Fuentes", "referencias con apoyo y límites de uso"),
}

DOC_PAGES = {
    "MATRIZ_COBERTURA_INTEGRAL.md": (
        "matriz-cobertura-integral.html",
        "Matriz de cobertura integral",
    ),
    "ARQUITECTURA_DEL_REPOSITORIO.md": (
        "arquitectura-repositorio.html",
        "Arquitectura del repositorio",
    ),
    "MAPA_DE_DEPENDENCIAS.md": (
        "mapa-dependencias.html",
        "Mapa de dependencias",
    ),
    "GLOSARIO_ACUMULATIVO.md": (
        "glosario.html",
        "Glosario acumulativo",
    ),
    "INFORME_INTEGRACION_2026-10.md": (
        "informe-integracion-2026-10.html",
        "Informe de integración 2026.10",
    ),
    "ESTANDAR_DOCUMENTACION_CLASE.md": (
        "estandar-documentacion-clase.html",
        "Estándar de documentación de una clase",
    ),
    "AUDITORIA_PEDAGOGICA_Y_TRAZABILIDAD.md": (
        "auditoria-pedagogica.html",
        "Auditoría pedagógica y trazabilidad",
    ),
    "AUDITORIA_DIFERENCIAS_800_CLASES.md": (
        "auditoria-diferencias-800-clases.html",
        "Auditoría de diferencias entre las 800 clases",
    ),
    "ESTADO_VERIFICABLE.md": ("estado.html", "Estado verificable"),
    "FUENTES_Y_EVIDENCIA.md": ("fuentes-y-evidencia.html", "Fuentes y evidencia"),
    "ESTANDAR_DE_FUENTES.md": (
        "estandar-fuentes.html",
        "Estándar de fuentes y trazabilidad",
    ),
    "COMO_USAR_EL_PROGRAMA.md": ("como-usar.html", "Cómo usar el programa"),
    "RUTAS_DE_APRENDIZAJE.md": ("rutas-de-aprendizaje.html", "Rutas de aprendizaje"),
    "ROLES_Y_OFICIOS.md": ("roles-y-oficios.html", "Roles y oficios"),
    "CASOS_INTEGRADORES.md": ("casos-integradores.html", "Casos integradores"),
    "AUDITORIA_DOCUMENTAL_REFERENCIA.md": (
        "auditoria-documental.html",
        "Auditoría documental de la referencia",
    ),
    "PROCEDENCIA_EDITORIAL.md": (
        "procedencia-editorial.html",
        "Procedencia editorial",
    ),
    "LICENCIAS_Y_DERECHOS.md": (
        "licencias-y-derechos.html",
        "Licencias y derechos",
    ),
    "LICENSING_MATRIX.md": (
        "matriz-licencias.html",
        "Matriz real de licencias",
    ),
    "COMMERCIAL_USE.md": (
        "uso-comercial.html",
        "Uso comercial",
    ),
    "LICENSING_HISTORY.md": (
        "historia-licencias.html",
        "Historia del régimen de licencias",
    ),
    "NORMATIVE_BOUNDARY.md": (
        "frontera-normativa.html",
        "Frontera didáctica y normativa",
    ),
    "MATRIZ_PARIDAD_REFERENCIA.md": (
        "matriz-paridad-referencia.html",
        "Matriz de paridad con la referencia",
    ),
    "SEGURIDAD_Y_ETICA_PROFESIONAL.md": (
        "seguridad-etica-profesional.html",
        "Seguridad y ética profesional",
    ),
    "ARQUITECTURA_DE_EVALUACION.md": (
        "arquitectura-evaluacion.html",
        "Arquitectura de evaluación",
    ),
    "RUBRICA_COMUN.md": ("rubrica-comun.html", "Rúbrica común"),
    "PORTAFOLIO_Y_EVIDENCIAS.md": (
        "portafolio-evidencias.html",
        "Portafolio y evidencias",
    ),
    "ESTANDAR_VISUAL.md": ("estandar-visual.html", "Estándar visual"),
    "SYLLABUS_Y_CARGA.md": ("syllabus-carga.html", "Syllabus y carga"),
}


def load_catalog() -> list[dict]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def load_pedagogy() -> dict:
    return json.loads(PEDAGOGY_PATH.read_text(encoding="utf-8"))


def load_bibliography() -> dict:
    return json.loads(BIBLIOGRAPHY_PATH.read_text(encoding="utf-8"))


def source_uses_by_class(registry: dict) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = {}
    for entry in registry["entries"]:
        for use in entry["uses"]:
            result.setdefault(use["class"], []).append(use)
    return result


def source_traceability_notice(uses: list[dict]) -> str:
    complete = sum(use["traceability_status"] == "complete" for use in uses)
    missing = Counter(field for use in uses for field in use["missing_fields"])
    labels = {
        "function": "función",
        "consultation_scope": "alcance consultado",
        "limitation": "límite",
        "accessed_on": "fecha de consulta",
    }
    if missing:
        detail = ", ".join(f"{labels[field]}: {count}" for field, count in missing.items())
        status = f"{complete}/{len(uses)} usos completos; faltan {detail}."
    else:
        status = f"{complete}/{len(uses)} usos completos en los cuatro campos contextuales."
    return (
        '<aside class="notice" data-source-traceability="true">'
        '<strong>Estado de trazabilidad de esta clase.</strong> '
        f'{html.escape(status)} '
        '<a href="../bibliografia.html">Abrir el registro</a> · '
        '<a href="../estandar-fuentes.html">Revisar el estándar</a>. '
        'Este estado no demuestra vigencia ni aplicabilidad normativa.'
        '</aside>'
    )


def legacy_entries() -> list[dict]:
    text = READER.read_text(encoding="utf-8")
    marker = "const ENTRIES="
    start = text.index(marker) + len(marker)
    end = text.index("];\nconst byId", start) + 1
    return json.loads(text[start:end])


def display_title(entry: dict) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", entry["html"], re.S | re.I)
    if not match:
        return entry["title"]
    value = re.sub(r"<[^>]+>", "", match.group(1))
    value = html.unescape(value).strip()
    return re.sub(rf"^{re.escape(entry['id'])}\s*[·—:-]\s*", "", value, flags=re.I)


def part_titles() -> dict[int, str]:
    manifest = json.loads(PARTS_PATH.read_text(encoding="utf-8"))
    titles = {item["number"]: item["title"] for item in manifest["parts"]}
    if set(titles) != set(range(1, PROGRAM["part_count"] + 1)):
        raise ValueError("data/parts.json does not match data/program.json")
    return titles


def entry_path(entry: dict) -> str:
    folder = RESOURCE_TYPES[entry["kind"]][0]
    return f"{folder}/{entry['id'].lower()}.html"


def link_legacy_html(content: str, lookup: dict[str, dict]) -> str:
    def replace(match: re.Match) -> str:
        target = match.group(1)
        entry = lookup.get(target)
        if entry:
            return f'href="../{entry_path(entry)}"'
        if re.fullmatch(r"ARQ-\d{3}", target):
            return f'href="../clases/{target.lower()}.html"'
        return match.group(0)
    return re.sub(r'href="#([^"]+)"', replace, content)


def render_markdown(text: str) -> str:
    rendered = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
    )
    def source_target(match: re.Match) -> str:
        target = match.group(1)
        if f'id="{target}"' in rendered:
            return f'href="#{target}"'
        return f'href="../fuentes/{target.lower()}.html"'

    rendered = re.sub(r'href="#(FUENTE-[^"]+)"', source_target, rendered)
    return re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        lambda match: f'<pre class="mermaid">{html.unescape(match.group(1))}</pre>',
        rendered,
        flags=re.DOTALL,
    )


def render_document_markdown(text: str) -> str:
    rendered = render_markdown(text)
    rendered = re.sub(
        r'href="\.\./classes/parte-\d{2}/(ARQ-\d{3})\.md"',
        lambda match: f'href="clases/{match.group(1).lower()}.html"',
        rendered,
    )
    rendered = re.sub(
        r'href="\.\./learning-paths/(ruta-\d{2})\.md"',
        lambda match: f'href="rutas/{match.group(1)}.html"',
        rendered,
        flags=re.I,
    )
    for filename, (slug, _title) in DOC_PAGES.items():
        rendered = rendered.replace(f'href="{filename}"', f'href="{slug}"')
        rendered = rendered.replace(f'href="docs/{filename}"', f'href="{slug}"')
        rendered = rendered.replace(f'href="../docs/{filename}"', f'href="{slug}"')
    return (
        rendered.replace('href="../classes/README.md"', 'href="partes/index.html"')
        .replace('href="../ROADMAP_INTEGRAL.md"', 'href="roadmap-integral.html"')
        .replace('href="../studios/README.md"', 'href="talleres/index.html"')
        .replace('href="../README.md"', 'href="index.html"')
        .replace('href="../sources/README.md"', 'href="bibliografia.html"')
        .replace('href="../sources/bibliography.json"', 'href="sources/bibliography.json"')
        .replace('href="bibliography.json"', 'href="sources/bibliography.json"')
        .replace('href="../data/audits/class-distinctness.json"', 'href="data/audits/class-distinctness.json"')
        .replace('href="../LICENSE"', f'href="{REPO_URL}/blob/main/LICENSE"')
        .replace('href="../LICENSE-CONTENT.md"', f'href="{REPO_URL}/blob/main/LICENSE-CONTENT.md"')
        .replace('href="../DATA_LICENSES.md"', f'href="{REPO_URL}/blob/main/DATA_LICENSES.md"')
        .replace('href="../ASSET_LICENSES.md"', f'href="{REPO_URL}/blob/main/ASSET_LICENSES.md"')
        .replace('href="../THIRD_PARTY_NOTICES.md"', f'href="{REPO_URL}/blob/main/THIRD_PARTY_NOTICES.md"')
        .replace('href="../TRADEMARKS.md"', f'href="{REPO_URL}/blob/main/TRADEMARKS.md"')
        .replace('href="../LICENSING_AUDIT.md"', f'href="{REPO_URL}/blob/main/LICENSING_AUDIT.md"')
        .replace('href="../SECURITY.md"', f'href="{REPO_URL}/blob/main/SECURITY.md"')
    )


def render_part_markdown(text: str) -> str:
    rendered = render_markdown(text)
    rendered = re.sub(
        r'href="ARQ-(\d{3})\.md"',
        lambda match: f'href="../clases/arq-{match.group(1)}.html"',
        rendered,
        flags=re.I,
    )
    rendered = re.sub(
        r'href="\.\./parte-(\d{2})/README\.md"',
        lambda match: f'href="parte-{match.group(1)}.html"',
        rendered,
        flags=re.I,
    )
    return rendered.replace('href="../README.md"', 'href="index.html"')


def shell(title: str, body: str, *, description: str = "", prefix: str = "") -> str:
    safe_title = html.escape(title)
    safe_description = html.escape(description or "Programa integral de arquitectura, construcción y entorno habitado.")
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{safe_description}"><meta name="theme-color" content="#102f38">
<meta property="og:title" content="{safe_title}"><meta property="og:description" content="{safe_description}">
<meta property="og:type" content="website"><meta property="og:url" content="{PAGES_URL}">
<title>{safe_title}</title><link rel="icon" href="{prefix}assets/mark.svg"><link rel="stylesheet" href="{prefix}assets/site.css"></head>
<body><a class="skip" href="#main">Saltar al contenido</a><header class="topbar"><div class="inner">
<a class="brand" href="{prefix}index.html">⌂ ARQ · {PROGRAM['class_count']} + {PROGRAM['studio_session_count']}</a><nav class="nav" aria-label="Principal"><a href="{prefix}partes/index.html">Partes</a><a href="{prefix}catalogo.html">Clases</a><a href="{prefix}talleres/index.html">Talleres</a><a href="{prefix}rutas/index.html">Rutas</a><a href="{prefix}documentacion.html">Documentación</a><a href="{prefix}artefactos.html">Descargas</a><a href="{REPO_URL}">GitHub</a></nav>
</div></header>{body}<footer class="footer"><div class="inner"><small><strong>Programa Integral de Arquitectura, Construcción y Entorno Habitado.</strong><br>Cada componente conserva su régimen: contenido original <a href="{REPO_URL}/blob/main/LICENSE-CONTENT.md">CC BY-NC-SA 4.0</a>, código propio <a href="{REPO_URL}/blob/main/LICENSE">Apache-2.0</a> y referencias externas bajo derechos de sus titulares.<br>Material educativo independiente: no otorga título, licencia profesional ni autorización para ejecutar obras.</small><small><strong>¿Te resulta útil? <a href="{STARS_URL}">⭐ Dale una estrella</a></strong><br><a href="{prefix}catalogo.html">{PROGRAM['class_count']} clases</a> · <a href="{prefix}talleres/index.html">{PROGRAM['studio_session_count']} sesiones de taller</a> · <a href="{prefix}procedencia-editorial.html">Procedencia</a> · <a href="{prefix}licencias-y-derechos.html">Licencias</a> · <a href="{REPO_URL}">GitHub</a></small></div></footer><script type="module">import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';mermaid.initialize({{startOnLoad:false,securityLevel:'strict',theme:'neutral'}});mermaid.run({{query:'.mermaid'}});</script></body></html>"""


def write(relative: str, content: str) -> None:
    path = OUT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def nav(previous: dict | None, following: dict | None) -> str:
    def link(item: dict | None, label: str) -> str:
        if not item:
            return '<a href="../catalogo.html">Catálogo completo</a>'
        return f'<a href="{item["id"].lower()}.html"><small>{label}</small><br>{html.escape(item["id"] + " · " + item["title"])}</a>'
    return f'<nav class="lesson-nav" aria-label="Clases adyacentes">{link(previous, "← Anterior")}{link(following, "Siguiente →")}</nav>'


def landing(catalog: list[dict], entries: list[dict], titles: dict[int, str]) -> str:
    counts = {kind: sum(entry["kind"] == kind for entry in entries) for kind in RESOURCE_TYPES}
    parts = "".join(
        f'<a class="part-card" href="partes/parte-{part:02d}.html"><small>Parte {part:02d}</small><strong>{html.escape(titles[part])}</strong><span>ARQ-{(part-1)*10+1:03d} → ARQ-{part*10:03d}</span></a>'
        for part in range(1, PROGRAM["part_count"] + 1)
    )
    resources = "".join(
        f'<a class="resource-card" href="{folder}/index.html"><strong>{counts[kind]}</strong><b>{label}</b><span>{description}</span></a>'
        for kind, (folder, label, description) in RESOURCE_TYPES.items()
    )
    body = f"""<main id="main"><section class="hero"><div class="inner"><p class="eyebrow">Edición pedagógica 2026.10 · Español · evidencia y revisión</p><h1>Arquitectura,<br>construcción y<br>entorno habitado</h1><p>Del encargo al uso, la conservación y el fin de vida. {PROGRAM['class_count']} clases de referencia, {PROGRAM['studio_session_count']} sesiones de taller, {PROGRAM['route_count']} rutas y evaluación mediante evidencia, crítica, revisión y portafolio.</p><div class="actions"><a class="button primary" href="catalogo.html">Explorar las {PROGRAM['class_count']} clases</a><a class="button" href="talleres/index.html">Abrir los talleres</a><a class="button" href="#estado">Comprobar el estado</a></div></div></section>
<div class="wrap"><section class="stats" aria-label="Cifras verificadas"><div class="stat"><strong>{PROGRAM['class_count']}</strong><span>clases de referencia</span></div><div class="stat"><strong>{PROGRAM['studio_session_count']}</strong><span>sesiones en {PROGRAM['studio_count']} talleres</span></div><div class="stat"><strong>{PROGRAM['route_count']}</strong><span>rutas con diagnóstico y capstone</span></div><div class="stat"><strong>{PROGRAM['class_count']}</strong><span>mapas y criterios de aceptación</span></div></section>
<section class="section" id="estado"><p class="eyebrow" style="color:var(--clay)">Estado real</p><h2>Qué demuestra el repositorio y qué permanece abierto</h2><p class="lede">La malla está redactada y cada clase publica una cadena específica de decisión. La revisión externa por especialidades y la medición con estudiantes siguen pendientes.</p><table class="status-table"><thead><tr><th>Dimensión</th><th>Evidencia comprobada</th><th>Límite abierto</th></tr></thead><tbody><tr><td>Integridad curricular</td><td class="status-ok">{PROGRAM['class_count']}/{PROGRAM['class_count']} · {PROGRAM['part_count']} partes · {PROGRAM['classes_per_part']} clases por parte</td><td>No acredita calidad disciplinar.</td></tr><tr><td>Anatomía de clase</td><td class="status-ok">{PROGRAM['class_count']} preguntas · {PROGRAM['class_count']} actividades · {PROGRAM['class_count']} secciones de fuentes</td><td>La presencia por sí sola no demuestra calidad.</td></tr><tr><td>Decisión sustentada</td><td class="status-ok">{PROGRAM['class_count']}/{PROGRAM['class_count']} cadenas específicas</td><td>Cinco pilotos poseen revisión editorial manual profunda; la revisión externa sigue separada.</td></tr><tr><td>Integración</td><td class="status-ok">{PROGRAM['studio_count']} talleres · {PROGRAM['studio_session_count']} sesiones · crítica y revisión</td><td>No sustituye estudio, taller o supervisión profesional.</td></tr><tr><td>Procedencia</td><td class="status-ok">Registro derivado por uso y clase</td><td>La vigencia externa requiere revisión periódica.</td></tr><tr><td>Publicación</td><td class="status-ok">Markdown, HTML, lector offline y PDF verificables</td><td>Auditoría WCAG especializada pendiente.</td></tr><tr><td>Revisión externa</td><td class="status-pending">Declarada sin ocultarla</td><td>Revisión profesional por especialidades pendiente.</td></tr></tbody></table><p><a href="estandar-documentacion-clase.html">Abrir el estándar obligatorio →</a></p></section>
</div><section class="band"><div class="wrap section"><p class="eyebrow" style="color:var(--clay)">Biblioteca completa</p><h2>Más que un índice de clases</h2><p class="lede">Roles, recorridos, instrumentos, documentos y referencias conservan el mismo alcance editorial del lector original y ahora tienen URL propia.</p><div class="resource-grid">{resources}</div></div></section>
<div class="wrap"><section class="section"><p class="eyebrow" style="color:var(--clay)">De punta a punta</p><h2>Aprender a decidir, no a copiar soluciones</h2><div class="grid"><article class="card"><span class="num">01 · Secuencia</span><h3>Del fundamento a la integración</h3><p>Representación, historia, territorio, estructuras, instalaciones, gestión, patrimonio y grandes tipologías.</p></article><article class="card"><span class="num">02 · Evidencia</span><h3>El conocimiento tiene procedencia</h3><p>Cada uso se vincula con fuente, autoridad, alcance y límite. <a href="bibliografia.html">El registro publica también lo que todavía falta</a>.</p></article><article class="card"><span class="num">03 · Ciclo de vida</span><h3>Proyecto, obra y operación</h3><p>Las decisiones se siguen desde el encargo hasta el mantenimiento, la adaptación y el fin de vida.</p></article></div></section>
<section class="section"><h2>Las {PROGRAM['part_count']} partes</h2><p class="lede">Cada bloque contiene diez clases y una portada propia con su intervalo, foco y acceso directo.</p><div class="part-grid">{parts}</div></section>
<section class="section"><div class="callout"><h2>Alcance profesional explícito</h2><p>Completar este programa no otorga título, licencia, firma, permiso ni habilitación profesional. Los casos numéricos son didácticos salvo atribución explícita. Toda obra real requiere antecedentes, normativa vigente, especialistas competentes, coordinación, revisión y autorizaciones aplicables.</p><p><a href="metodo.html">Leer método, límites y criterios de transferencia →</a></p></div></section>
<section class="section"><h2>Markdown como fuente; HTML como experiencia</h2><p class="lede">Las {PROGRAM['class_count']} clases, las {PROGRAM['studio_session_count']} sesiones de taller y las {PROGRAM['route_count']} rutas viven como fuentes versionadas. El build produce el portal completo; el lector offline original y los PDF v1.0 permanecen disponibles como artefactos históricos.</p><div class="actions"><a class="button primary" style="background:var(--teal);color:#fff;border-color:var(--teal)" href="catalogo.html">Abrir catálogo</a><a class="button" style="color:var(--teal);border-color:var(--teal)" href="talleres/index.html">Abrir talleres</a><a class="button" style="color:var(--teal);border-color:var(--teal)" href="artefactos.html">Ver artefactos</a></div></section></div></main>"""
    return shell("Arquitectura, construcción y entorno habitado", body, description=f"{PROGRAM['class_count']} clases, {PROGRAM['studio_session_count']} sesiones de taller y {PROGRAM['route_count']} rutas con evaluación y portafolio sobre arquitectura, construcción y entorno habitado.")


def catalog_page(catalog: list[dict]) -> str:
    cards = "".join(
        f'<a class="lesson-link" data-title="{html.escape((item["id"]+" "+item["title"]).lower())}" data-part="{item["part"]}" href="clases/{item["id"].lower()}.html"><span class="lesson-code">{item["id"]}</span><span class="lesson-title">{html.escape(item["title"])}</span></a>'
        for item in catalog
    )
    options = "".join(f'<option value="{part}">Parte {part:02d}</option>' for part in range(1, PROGRAM["part_count"] + 1))
    script = """<script>const q=document.querySelector('#q'),p=document.querySelector('#part'),cards=[...document.querySelectorAll('.lesson-link')],count=document.querySelector('#count');function filter(){const t=q.value.trim().toLocaleLowerCase('es').normalize('NFD').replace(/[\\u0300-\\u036f]/g,''),part=p.value;let n=0;for(const c of cards){const key=c.dataset.title.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');const show=(!t||key.includes(t))&&(!part||c.dataset.part===part);c.classList.toggle('hide',!show);if(show)n++}count.textContent=n+' clases visibles'}q.addEventListener('input',filter);p.addEventListener('change',filter);filter()</script>"""
    body = f'<main id="main" class="wrap section"><p class="kicker">Catálogo completo</p><h1>{PROGRAM["class_count"]} clases · {PROGRAM["part_count"]} partes</h1><p class="lede">Busca por identificador o concepto. Cada parte contiene diez clases y conserva la secuencia ARQ-001 → ARQ-{PROGRAM["class_count"]:03d}.</p><div class="catalog-tools"><label>Buscar clase<input id="q" type="search" placeholder="Ej. madera, sismo, ARQ-240"></label><label>Filtrar por parte<select id="part"><option value="">Todas las partes</option>{options}</select></label></div><p id="count" class="lede" aria-live="polite"></p><div class="catalog-list">{cards}</div>{script}</main>'
    return shell(f"Catálogo de {PROGRAM['class_count']} clases · Arquitectura", body)


def parts_index(catalog: list[dict], titles: dict[int, str]) -> str:
    cards = "".join(
        f'<a class="part-card" href="parte-{part:02d}.html"><small>Parte {part:02d}</small><strong>{html.escape(titles[part])}</strong><span>ARQ-{(part-1)*10+1:03d} → ARQ-{part*10:03d} · 10 clases</span></a>'
        for part in range(1, PROGRAM["part_count"] + 1)
    )
    body = f'<main id="main" class="wrap section"><p class="kicker">Mapa curricular</p><h1>{PROGRAM["part_count"]} partes · {PROGRAM["class_count"]} clases</h1><p class="lede">La secuencia completa, desde fundamentos del habitar hasta especialización, innovación responsable y proyecto interdisciplinario.</p><div class="part-grid">{cards}</div></main>'
    return shell(f"{PROGRAM['part_count']} partes · Arquitectura", body, prefix="../")


def part_page(part: int, catalog: list[dict], titles: dict[int, str]) -> str:
    source = ROOT / "classes" / f"parte-{part:02d}" / "README.md"
    body = f'<main id="main" class="doc">{render_part_markdown(source.read_text(encoding="utf-8"))}</main>'
    return shell(f'Parte {part:02d} · {titles[part]}', body, prefix="../")


def resources_portal(entries: list[dict]) -> str:
    cards = []
    for kind, (folder, label, description) in RESOURCE_TYPES.items():
        count = sum(entry["kind"] == kind for entry in entries)
        cards.append(f'<a class="resource-card" href="{folder}/index.html"><strong>{count}</strong><b>{label}</b><span>{description}</span></a>')
    body = f'<main id="main" class="wrap section"><p class="kicker">Superficie de conocimiento</p><h1>755 recursos transversales</h1><p class="lede">El programa conecta el currículo con responsabilidades, recorridos, instrumentos, documentos editoriales y referencias. Cada registro del lector v1.0 tiene una página pública y enlazable.</p><div class="resource-grid">{"".join(cards)}</div><section class="section"><div class="callout"><h2>Cómo leer las fuentes</h2><p>Una referencia apoya una afirmación dentro del alcance declarado por la clase. No implica adopción íntegra, vigencia universal ni autorización normativa para un proyecto real.</p><p><a href="metodo.html">Revisar el método y los límites →</a></p></div></section></main>'
    return shell("Recursos transversales · Arquitectura", body)


def documentation_portal(registry: dict) -> str:
    cards = "".join(
        f'<a class="resource-card" href="{slug}"><b>{html.escape(title)}</b><span>{html.escape(description)}</span></a>'
        for filename, (slug, title), description in (
            (
                "MATRIZ_COBERTURA_INTEGRAL.md",
                DOC_PAGES["MATRIZ_COBERTURA_INTEGRAL.md"],
                "inventario por área, profundidad, fuentes, brechas y acción",
            ),
            (
                "ARQUITECTURA_DEL_REPOSITORIO.md",
                DOC_PAGES["ARQUITECTURA_DEL_REPOSITORIO.md"],
                "fuentes canónicas, salidas derivadas y frontera histórica",
            ),
            (
                "MAPA_DE_DEPENDENCIAS.md",
                DOC_PAGES["MAPA_DE_DEPENDENCIAS.md"],
                "prerrequisitos, prácticas, proyectos, competencias y rutas",
            ),
            (
                "GLOSARIO_ACUMULATIVO.md",
                DOC_PAGES["GLOSARIO_ACUMULATIVO.md"],
                "vocabulario bilingüe conectado con clases y usos",
            ),
            (
                "INFORME_INTEGRACION_2026-10.md",
                DOC_PAGES["INFORME_INTEGRACION_2026-10.md"],
                "contenido conservado, ampliado, reorganizado y pendiente",
            ),
            (
                "ESTANDAR_DOCUMENTACION_CLASE.md",
                DOC_PAGES["ESTANDAR_DOCUMENTACION_CLASE.md"],
                "regla obligatoria para justificar, escribir, citar, evaluar y aceptar cada clase",
            ),
            (
                "AUDITORIA_PEDAGOGICA_Y_TRAZABILIDAD.md",
                DOC_PAGES["AUDITORIA_PEDAGOGICA_Y_TRAZABILIDAD.md"],
                "diagnóstico histórico, cinco pilotos profundos, trazabilidad y brechas reales",
            ),
            (
                "AUDITORIA_DIFERENCIAS_800_CLASES.md",
                DOC_PAGES["AUDITORIA_DIFERENCIAS_800_CLASES.md"],
                "comparación clase por clase, repetición editorial y prioridades de reescritura",
            ),
            (
                "ESTADO_VERIFICABLE.md",
                DOC_PAGES["ESTADO_VERIFICABLE.md"],
                "cobertura real, método de conteo, límites y pendientes",
            ),
            (
                "FUENTES_Y_EVIDENCIA.md",
                DOC_PAGES["FUENTES_Y_EVIDENCIA.md"],
                "procedencia, jerarquía de afirmaciones y uso responsable",
            ),
            (
                "ESTANDAR_DE_FUENTES.md",
                DOC_PAGES["ESTANDAR_DE_FUENTES.md"],
                "campos mínimos para libros, normas, artículos, webs y casos",
            ),
            (
                "COMO_USAR_EL_PROGRAMA.md",
                DOC_PAGES["COMO_USAR_EL_PROGRAMA.md"],
                "entradas para estudiantes, docentes, profesionales y mandantes",
            ),
            (
                "RUTAS_DE_APRENDIZAJE.md",
                DOC_PAGES["RUTAS_DE_APRENDIZAJE.md"],
                "33 recorridos troncales y de especialización",
            ),
            (
                "ROLES_Y_OFICIOS.md",
                DOC_PAGES["ROLES_Y_OFICIOS.md"],
                "ochenta responsabilidades agrupadas por familia",
            ),
            (
                "CASOS_INTEGRADORES.md",
                DOC_PAGES["CASOS_INTEGRADORES.md"],
                "seis casos para coordinar decisiones y evidencia",
            ),
            (
                "AUDITORIA_DOCUMENTAL_REFERENCIA.md",
                DOC_PAGES["AUDITORIA_DOCUMENTAL_REFERENCIA.md"],
                "qué se aprendió de la referencia y qué no se trasladó",
            ),
            (
                "PROCEDENCIA_EDITORIAL.md",
                DOC_PAGES["PROCEDENCIA_EDITORIAL.md"],
                "de dónde provienen la secuencia, las indicaciones y las clases",
            ),
            (
                "LICENCIAS_Y_DERECHOS.md",
                DOC_PAGES["LICENCIAS_Y_DERECHOS.md"],
                "código, contenido, datos, activos y material de terceros",
            ),
            (
                "LICENSING_MATRIX.md",
                DOC_PAGES["LICENSING_MATRIX.md"],
                "alcance, origen, permisos y generación de cada familia",
            ),
            (
                "COMMERCIAL_USE.md",
                DOC_PAGES["COMMERCIAL_USE.md"],
                "código comercial, contenido no comercial y permisos separados",
            ),
            (
                "LICENSING_HISTORY.md",
                DOC_PAGES["LICENSING_HISTORY.md"],
                "revisiones sin licencia explícita y evolución del régimen",
            ),
            (
                "NORMATIVE_BOUNDARY.md",
                DOC_PAGES["NORMATIVE_BOUNDARY.md"],
                "diferencia entre explicación didáctica y documento oficial",
            ),
            (
                "MATRIZ_PARIDAD_REFERENCIA.md",
                DOC_PAGES["MATRIZ_PARIDAD_REFERENCIA.md"],
                "qué se aplicó, adaptó o descartó y por qué",
            ),
            (
                "SEGURIDAD_Y_ETICA_PROFESIONAL.md",
                DOC_PAGES["SEGURIDAD_Y_ETICA_PROFESIONAL.md"],
                "límites para obras, emergencias, personas, patrimonio e IA",
            ),
            (
                "ARQUITECTURA_DE_EVALUACION.md",
                DOC_PAGES["ARQUITECTURA_DE_EVALUACION.md"],
                "evaluación por clase, parte, ruta y programa",
            ),
            (
                "RUBRICA_COMUN.md",
                DOC_PAGES["RUBRICA_COMUN.md"],
                "cinco dimensiones, niveles y condiciones críticas",
            ),
            (
                "PORTAFOLIO_Y_EVIDENCIAS.md",
                DOC_PAGES["PORTAFOLIO_Y_EVIDENCIAS.md"],
                "versiones, crítica, revisión, privacidad y selección final",
            ),
            (
                "ESTANDAR_VISUAL.md",
                DOC_PAGES["ESTANDAR_VISUAL.md"],
                "representación disciplinar, accesibilidad y derechos",
            ),
            (
                "SYLLABUS_Y_CARGA.md",
                DOC_PAGES["SYLLABUS_Y_CARGA.md"],
                "modalidades, progresión y medición honesta de carga",
            ),
        )
    )
    cards += '<a class="resource-card" href="roadmap-integral.html"><b>Roadmap integral</b><span>alcance general, brechas, método de resolución y condiciones de cierre</span></a>'
    cards += f'<a class="resource-card" href="bibliografia.html"><b>Registro central de fuentes</b><span>{registry["unique_sources"]} URLs, {registry["citation_occurrences"]} relaciones y completitud contextual publicada</span></a>'
    body = f'<main id="main" class="wrap section"><p class="kicker">Documentación del programa</p><h1>Leer antes de contar</h1><p class="lede">Método, procedencia, uso, cobertura y límites documentados fuera del README para que cada afirmación pueda revisarse.</p><div class="resource-grid">{cards}</div></main>'
    return shell("Documentación · Arquitectura", body)


def bibliography_catalog(registry: dict) -> str:
    type_labels = {
        "standard": "Norma o estándar",
        "public-body": "Organismo público",
        "academic": "Académica o educativa",
        "reference": "Referencia web",
    }
    cards = []
    for entry in registry["entries"]:
        complete = sum(use["traceability_status"] == "complete" for use in entry["uses"])
        classes = " · ".join(
            f'<a href="../clases/{Path(path).stem.lower()}.html">{html.escape(Path(path).stem)}</a>'
            for path in entry["used_in"][:6]
        )
        if len(entry["used_in"]) > 6:
            classes += f" · +{len(entry['used_in']) - 6}"
        authority = entry["publisher_or_author"]["name"]
        search = " ".join(
            (entry["title"], authority, entry["authority_domain"], entry["type"])
        ).lower()
        cards.append(
            f'<article class="card source-card" data-source-card="true" '
            f'data-title="{html.escape(search, quote=True)}" data-type="{html.escape(entry["type"])}">'
            f'<span class="num">{html.escape(type_labels[entry["type"]])} · {html.escape(entry["authority_domain"])}</span>'
            f'<h3><a href="{html.escape(entry["locator"], quote=True)}" rel="noopener noreferrer">{html.escape(entry["title"])}</a></h3>'
            f'<p><strong>Autoridad:</strong> {html.escape(authority)}<br>'
            f'<strong>Usos:</strong> {entry["usage_count"]} · <strong>completos:</strong> {complete}/{entry["usage_count"]}<br>'
            f'<strong>Clases:</strong> {classes}</p></article>'
        )
    options = "".join(
        f'<option value="{kind}">{label}</option>' for kind, label in type_labels.items()
    )
    script = """<script>const q=document.querySelector('#source-q'),t=document.querySelector('#source-type'),cards=[...document.querySelectorAll('[data-source-card]')],count=document.querySelector('#source-count');function filter(){const text=q.value.trim().toLocaleLowerCase('es').normalize('NFD').replace(/[\\u0300-\\u036f]/g,''),type=t.value;let n=0;for(const card of cards){const key=card.dataset.title.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');const show=(!text||key.includes(text))&&(!type||card.dataset.type===type);card.classList.toggle('hide',!show);if(show)n++}count.textContent=n+' fuentes visibles'}q.addEventListener('input',filter);t.addEventListener('change',filter);filter()</script>"""
    body = (
        '<main id="main" class="wrap section"><p class="kicker">Procedencia auditable</p>'
        f'<h1>Catálogo de {registry["unique_sources"]} fuentes</h1><p class="lede">Busca por título, autoridad o dominio. '
        '“Completo” describe el contexto documental del uso; no certifica vigencia ni aplicabilidad.</p>'
        '<div class="catalog-tools"><label>Buscar fuente<input id="source-q" type="search" '
        'placeholder="Ej. ISO, accesibilidad, UNESCO"></label><label>Filtrar por tipo<select id="source-type">'
        f'<option value="">Todos los tipos</option>{options}</select></label></div>'
        f'<p id="source-count" class="lede" aria-live="polite"></p><div class="catalog-list">{"".join(cards)}</div>{script}</main>'
    )
    return shell(f"Catálogo de {registry['unique_sources']} fuentes · Arquitectura", body, prefix="../")


def resource_index(kind: str, entries: list[dict]) -> str:
    folder, label, description = RESOURCE_TYPES[kind]
    selected = [entry for entry in entries if entry["kind"] == kind]
    cards = "".join(
        f'<a class="inventory-link" href="{entry["id"].lower()}.html"><small>{html.escape(entry["id"])}</small>{html.escape(display_title(entry))}</a>'
        for entry in selected
    )
    body = f'<main id="main" class="wrap section"><p class="kicker">Inventario verificable</p><h1>{len(selected)} {html.escape(label.lower())}</h1><p class="lede">{html.escape(description.capitalize())}. Inventario derivado del lector definitivo v1.0.</p><div class="inventory-list">{cards}</div></main>'
    return shell(f'{label} · Arquitectura', body, prefix="../")


def resource_page(entry: dict, lookup: dict[str, dict]) -> str:
    _folder, label, _description = RESOURCE_TYPES[entry["kind"]]
    content = link_legacy_html(entry["html"], lookup)
    body = f'<main id="main" class="doc"><p class="kicker">{html.escape(label)} · {html.escape(entry["id"])}</p>{content}<nav class="lesson-nav"><a href="index.html">← Volver al inventario</a><a href="../recursos.html">Todos los recursos →</a></nav></main>'
    return shell(f'{display_title(entry)} · {label}', body, description=display_title(entry), prefix="../")


def page_from_markdown(name: str, source: Path, title: str) -> None:
    rendered = render_document_markdown(source.read_text(encoding="utf-8"))
    body = f'<main id="main" class="doc">{rendered}</main>'
    write(name, shell(title, body))


def render_studio_markdown(text: str, studio_id: str, *, index: bool = False) -> str:
    rendered = render_markdown(text)
    if index:
        rendered = re.sub(
            r'href="(EST-\d{2})/README\.md"',
            lambda match: f'href="{match.group(1).lower()}/index.html"',
            rendered,
        )
    else:
        rendered = re.sub(
            rf'href="{re.escape(studio_id)}-(\d{{2}})\.md"',
            lambda match: f'href="{studio_id.lower()}-{match.group(1)}.html"',
            rendered,
        )
        rendered = rendered.replace('href="README.md"', 'href="index.html"')
        rendered = rendered.replace(
            'href="../../docs/RUBRICA_COMUN.md"', 'href="../../rubrica-comun.html"'
        )
    rendered = rendered.replace(
        'href="../docs/ARQUITECTURA_DE_EVALUACION.md"',
        'href="../arquitectura-evaluacion.html"',
    ).replace(
        'href="../docs/RUBRICA_COMUN.md"',
        'href="../rubrica-comun.html"',
    ).replace(
        'href="../docs/PORTAFOLIO_Y_EVIDENCIAS.md"',
        'href="../portafolio-evidencias.html"',
    )
    return rendered


def build_studios(pedagogy: dict) -> None:
    index_text = (ROOT / "studios" / "README.md").read_text(encoding="utf-8")
    index_body = f'<main id="main" class="doc">{render_studio_markdown(index_text, "", index=True)}</main>'
    write("talleres/index.html", shell(f"{len(pedagogy['studios'])} talleres verticales · Arquitectura", index_body, prefix="../"))
    for studio in pedagogy["studios"]:
        studio_id = studio["id"]
        folder = ROOT / "studios" / studio_id
        readme = render_studio_markdown((folder / "README.md").read_text(encoding="utf-8"), studio_id)
        write(
            f"talleres/{studio_id.lower()}/index.html",
            shell(f"{studio_id} · {studio['title']}", f'<main id="main" class="doc">{readme}</main>', prefix="../../"),
        )
        for session in range(1, 7):
            source = folder / f"{studio_id}-{session:02d}.md"
            rendered = render_studio_markdown(source.read_text(encoding="utf-8"), studio_id)
            write(
                f"talleres/{studio_id.lower()}/{studio_id.lower()}-{session:02d}.html",
                shell(f"{studio_id}-{session:02d} · {studio['title']}", f'<main id="main" class="doc">{rendered}</main>', prefix="../../"),
            )


def build_learning_paths(pedagogy: dict) -> None:
    cards = "".join(
        f'<a class="inventory-link" href="{route["id"].lower()}.html"><small>{route["id"]}</small>{html.escape(route["title"])}</a>'
        for route in pedagogy["routes"]
    )
    route_count = len(pedagogy["routes"])
    body = f'<main id="main" class="wrap section"><p class="kicker">Rutas verificables</p><h1>{route_count} rutas de aprendizaje</h1><p class="lede">Cada ruta declara entrada, recorrido, checkpoints, evidencia de salida, capstone y criterio de finalización.</p><div class="inventory-list">{cards}</div></main>'
    write("rutas/index.html", shell(f"{route_count} rutas de aprendizaje · Arquitectura", body, prefix="../"))
    for route in pedagogy["routes"]:
        source = ROOT / "learning-paths" / f"{route['id'].lower()}.md"
        rendered = render_markdown(source.read_text(encoding="utf-8"))
        rendered = re.sub(
            r'href="\.\./studios/(EST-\d{2})/README\.md"',
            lambda match: f'href="../talleres/{match.group(1).lower()}/index.html"',
            rendered,
        )
        write(
            f"rutas/{route['id'].lower()}.html",
            shell(f"{route['id']} · {route['title']}", f'<main id="main" class="doc">{rendered}</main>', prefix="../"),
        )


def main() -> int:
    catalog = load_catalog()
    pedagogy = load_pedagogy()
    bibliography = load_bibliography()
    source_uses = source_uses_by_class(bibliography)
    entries = legacy_entries()
    titles = part_titles()
    resource_entries = [entry for entry in entries if entry["kind"] in RESOURCE_TYPES]
    lookup = {entry["id"]: entry for entry in resource_entries}
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    write("assets/site.css", CSS.strip() + "\n")
    shutil.copy2(ROOT / "assets" / "mark.svg", OUT / "assets" / "mark.svg")
    write("index.html", landing(catalog, entries, titles))
    write("catalogo.html", catalog_page(catalog))
    write("recursos.html", resources_portal(entries))
    write("documentacion.html", documentation_portal(bibliography))
    write("bibliografia/catalogo.html", bibliography_catalog(bibliography))
    write("partes/index.html", parts_index(catalog, titles))
    for part in range(1, PROGRAM["part_count"] + 1):
        write(f"partes/parte-{part:02d}.html", part_page(part, catalog, titles))

    for index, item in enumerate(catalog):
        content = render_markdown((ROOT / item["source"]).read_text(encoding="utf-8"))
        content = content.replace(
            'href="../../docs/RUBRICA_COMUN.md"', 'href="../rubrica-comun.html"'
        )
        traceability = source_traceability_notice(source_uses[item["source"]])
        previous = catalog[index - 1] if index else None
        following = catalog[index + 1] if index + 1 < len(catalog) else None
        body = f'<main id="main" class="doc"><p class="kicker">Parte {item["part"]:02d} · Clase {index+1} de {len(catalog)}</p>{content}{traceability}{nav(previous, following)}</main>'
        write(f'clases/{item["id"].lower()}.html', shell(f'{item["id"]} · {item["title"]}', body, description=item["title"], prefix="../"))

    for kind, (folder, _label, _description) in RESOURCE_TYPES.items():
        write(f"{folder}/index.html", resource_index(kind, entries))
    for entry in resource_entries:
        write(entry_path(entry), resource_page(entry, lookup))
    build_learning_paths(pedagogy)
    build_studios(pedagogy)

    page_from_markdown("metodo.html", ROOT / "docs" / "METODO_Y_ALCANCE.md", "Método y alcance · Arquitectura")
    page_from_markdown("artefactos.html", ROOT / "docs" / "ARTEFACTOS.md", "Descargas · Arquitectura")
    page_from_markdown("roadmap-integral.html", ROOT / "ROADMAP_INTEGRAL.md", "Roadmap integral · Arquitectura")
    for filename, (slug, title) in DOC_PAGES.items():
        rendered = render_document_markdown(
            (ROOT / "docs" / filename).read_text(encoding="utf-8")
        )
        write(
            slug,
            shell(
                f"{title} · Arquitectura",
                f'<main id="main" class="doc">{rendered}</main>',
            ),
        )
    rendered_bibliography = render_document_markdown(
        (ROOT / "sources" / "README.md").read_text(encoding="utf-8")
    )
    write(
        "bibliografia.html",
        shell(
            "Registro central de fuentes · Arquitectura",
            f'<main id="main" class="doc"><div class="notice"><strong>Explora las fuentes.</strong> <a href="bibliografia/catalogo.html">Abrir catálogo buscable de {bibliography["unique_sources"]} fuentes</a>.</div>{rendered_bibliography}</main>',
        ),
    )
    bibliography_target = OUT / "sources" / "bibliography.json"
    bibliography_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "sources" / "bibliography.json", bibliography_target)
    audit_json_target = OUT / "data" / "audits" / "class-distinctness.json"
    audit_json_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "data" / "audits" / "class-distinctness.json", audit_json_target)
    audit_csv_target = OUT / "audits" / "class-distinctness.csv"
    audit_csv_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "docs" / "audits" / "class-distinctness.csv", audit_csv_target)
    shutil.copy2(READER, OUT / "lector-offline-v1.0.html")
    for filename in ("Arquitectura_20_Clases_Finales_v1.0.pdf", "ARQ-680_Clase_Completa_v1.0.pdf"):
        shutil.copy2(ROOT / filename, OUT / filename)
    write(".nojekyll", "")
    write("404.html", shell("Página no encontrada", '<main id="main" class="doc"><h1>Página no encontrada</h1><p>Vuelve al <a href="index.html">inicio</a> o consulta el <a href="catalogo.html">catálogo completo</a>.</p></main>'))
    print(
        f"Built {len(catalog)} lessons, {PROGRAM['part_count']} part pages, "
        f"{len(resource_entries)} resource pages and the portal in {OUT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
