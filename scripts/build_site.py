#!/usr/bin/env python3
"""Build the GitHub Pages site from the Markdown source of all lessons."""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
CATALOG_PATH = ROOT / "data" / "catalog.json"
READER = ROOT / "programa-arquitectura-lector-definitivo-v1.0.html"
REPO_URL = "https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program"
PAGES_URL = "https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/"
STARS_URL = f"{REPO_URL}/stargazers"

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
    "ESTADO_VERIFICABLE.md": ("estado.html", "Estado verificable"),
    "FUENTES_Y_EVIDENCIA.md": ("fuentes-y-evidencia.html", "Fuentes y evidencia"),
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
    "MATRIZ_PARIDAD_REFERENCIA.md": (
        "matriz-paridad-referencia.html",
        "Matriz de paridad con la referencia",
    ),
    "SEGURIDAD_Y_ETICA_PROFESIONAL.md": (
        "seguridad-etica-profesional.html",
        "Seguridad y ética profesional",
    ),
}


def load_catalog() -> list[dict]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


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
    text = READER.read_text(encoding="utf-8")
    matches = re.findall(r'<option value="(\d+)">(\d+)\s*·\s*([^<]+)</option>', text)
    titles = {int(value): html.unescape(title).strip() for value, _number, title in matches}
    if set(titles) != set(range(1, 69)):
        raise ValueError("could not recover the 68 canonical part titles")
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
    return re.sub(
        r'href="#(FUENTE-[^"]+)"',
        lambda match: f'href="../fuentes/{match.group(1).lower()}.html"',
        rendered,
    )


def render_document_markdown(text: str) -> str:
    rendered = render_markdown(text)
    for filename, (slug, _title) in DOC_PAGES.items():
        rendered = rendered.replace(f'href="{filename}"', f'href="{slug}"')
        rendered = rendered.replace(f'href="../docs/{filename}"', f'href="{slug}"')
    return (
        rendered.replace('href="../classes/README.md"', 'href="partes/index.html"')
        .replace('href="../README.md"', 'href="index.html"')
        .replace('href="../sources/README.md"', 'href="bibliografia.html"')
        .replace('href="../sources/bibliography.json"', 'href="sources/bibliography.json"')
        .replace('href="bibliography.json"', 'href="sources/bibliography.json"')
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
<a class="brand" href="{prefix}index.html">⌂ ARQ · 680</a><nav class="nav" aria-label="Principal"><a href="{prefix}partes/index.html">Partes</a><a href="{prefix}catalogo.html">Clases</a><a href="{prefix}documentacion.html">Documentación</a><a href="{prefix}recursos.html">Recursos</a><a href="{prefix}artefactos.html">Descargas</a><a href="{REPO_URL}">GitHub</a></nav>
</div></header>{body}<footer class="footer"><div class="inner"><small><strong>Programa Integral de Arquitectura, Construcción y Entorno Habitado.</strong><br>Copyright © 2026 Vladimir Acuña · contenido <a href="{REPO_URL}/blob/main/LICENSE-CONTENT.md">CC BY-NC-SA 4.0</a> · código <a href="{REPO_URL}/blob/main/LICENSE">Apache-2.0</a>.<br>Material educativo independiente: no otorga título, licencia profesional ni autorización para ejecutar obras.</small><small><strong>¿Te resulta útil? <a href="{STARS_URL}">⭐ Dale una estrella</a></strong><br><a href="{prefix}catalogo.html">680 clases</a> · <a href="{prefix}procedencia-editorial.html">Procedencia</a> · <a href="{prefix}licencias-y-derechos.html">Licencias</a> · <a href="{REPO_URL}">GitHub</a></small></div></footer></body></html>"""


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
        for part in range(1, 69)
    )
    resources = "".join(
        f'<a class="resource-card" href="{folder}/index.html"><strong>{counts[kind]}</strong><b>{label}</b><span>{description}</span></a>'
        for kind, (folder, label, description) in RESOURCE_TYPES.items()
    )
    body = f"""<main id="main"><section class="hero"><div class="inner"><p class="eyebrow">Edición definitiva v1.0 · Español · 24 septiembre 2026</p><h1>Arquitectura,<br>construcción y<br>entorno habitado</h1><p>Del encargo al uso, la conservación y el fin de vida. Un programa secuencial para estudiar personas, lugar, historia, materia, técnica, recursos, operación y tiempo.</p><div class="actions"><a class="button primary" href="catalogo.html">Explorar las 680 clases</a><a class="button" href="#estado">Comprobar el estado</a></div></div></section>
<div class="wrap"><section class="stats" aria-label="Cifras verificadas"><div class="stat"><strong>680</strong><span>clases completas</span></div><div class="stat"><strong>68</strong><span>partes · 10 clases cada una</span></div><div class="stat"><strong>1.435</strong><span>entradas navegables</span></div><div class="stat"><strong>0</strong><span>clases pendientes</span></div></section>
<section class="section" id="estado"><p class="eyebrow" style="color:var(--clay)">Estado real</p><h2>Qué demuestra el repositorio y qué permanece abierto</h2><p class="lede">“Completo” describe la malla editorial. No significa que todas las clases tengan idéntica pauta, que las fuentes sigan vigentes en toda jurisdicción ni que exista revisión profesional externa.</p><table class="status-table"><thead><tr><th>Dimensión</th><th>Evidencia comprobada</th><th>Límite abierto</th></tr></thead><tbody><tr><td>Integridad curricular</td><td class="status-ok">680/680 · 68 partes · 10 clases por parte</td><td>No acredita calidad disciplinar.</td></tr><tr><td>Anclas de clase</td><td class="status-ok">680 preguntas · 680 prácticas · 680 apartados de fuentes</td><td>Resultados, casos, errores y autoevaluación no son uniformes.</td></tr><tr><td>Procedencia</td><td class="status-ok">1.939 relaciones · 622 URLs · 189 dominios</td><td>Vigencia externa y aplicabilidad normativa pendientes.</td></tr><tr><td>Publicación</td><td class="status-ok">Markdown, HTML, lector offline y PDF verificables</td><td>Auditoría WCAG especializada pendiente.</td></tr><tr><td>Derechos</td><td class="status-ok">Apache-2.0 para código · CC BY-NC-SA 4.0 para contenido</td><td>Obras externas conservan sus derechos.</td></tr><tr><td>Revisión externa</td><td class="status-pending">Declarada sin ocultarla</td><td>Revisión profesional y pedagógica pendiente.</td></tr></tbody></table><p><a href="estado.html">Abrir metodología, cobertura y pendientes →</a></p></section>
</div><section class="band"><div class="wrap section"><p class="eyebrow" style="color:var(--clay)">Biblioteca completa</p><h2>Más que un índice de clases</h2><p class="lede">Roles, recorridos, instrumentos, documentos y referencias conservan el mismo alcance editorial del lector original y ahora tienen URL propia.</p><div class="resource-grid">{resources}</div></div></section>
<div class="wrap"><section class="section"><p class="eyebrow" style="color:var(--clay)">De punta a punta</p><h2>Aprender a decidir, no a copiar soluciones</h2><div class="grid"><article class="card"><span class="num">01 · Secuencia</span><h3>Del fundamento a la integración</h3><p>Representación, historia, territorio, estructuras, instalaciones, gestión, patrimonio y grandes tipologías.</p></article><article class="card"><span class="num">02 · Evidencia</span><h3>Dato, hipótesis y límite</h3><p>Las fuentes enseñan mecanismos y contexto; no se convierten automáticamente en norma aplicable a una obra.</p></article><article class="card"><span class="num">03 · Ciclo de vida</span><h3>Proyecto, obra y operación</h3><p>Las decisiones se siguen desde el encargo hasta el mantenimiento, la adaptación y el fin de vida.</p></article></div></section>
<section class="section"><h2>Las 68 partes</h2><p class="lede">Cada bloque contiene diez clases y una portada propia con su intervalo, foco y acceso directo.</p><div class="part-grid">{parts}</div></section>
<section class="section"><div class="callout"><h2>Alcance profesional explícito</h2><p>Completar este programa no otorga título, licencia, firma, permiso ni habilitación profesional. Los casos numéricos son didácticos salvo atribución explícita. Toda obra real requiere antecedentes, normativa vigente, especialistas competentes, coordinación, revisión y autorizaciones aplicables.</p><p><a href="metodo.html">Leer método, límites y criterios de transferencia →</a></p></div></section>
<section class="section"><h2>Markdown como fuente; HTML como experiencia</h2><p class="lede">Las 680 clases viven como Markdown versionado. El build produce el portal, 68 portadas de parte, páginas de clase y las 755 fichas transversales. El lector offline original y los PDF permanecen disponibles como artefactos.</p><div class="actions"><a class="button primary" style="background:var(--teal);color:#fff;border-color:var(--teal)" href="catalogo.html">Abrir catálogo</a><a class="button" style="color:var(--teal);border-color:var(--teal)" href="artefactos.html">Ver artefactos</a></div></section></div></main>"""
    return shell("Arquitectura, construcción y entorno habitado", body, description="680 clases, 68 partes y 755 recursos sobre arquitectura, construcción y entorno habitado.")


def catalog_page(catalog: list[dict]) -> str:
    cards = "".join(
        f'<a class="lesson-link" data-title="{html.escape((item["id"]+" "+item["title"]).lower())}" data-part="{item["part"]}" href="clases/{item["id"].lower()}.html"><span class="lesson-code">{item["id"]}</span><span class="lesson-title">{html.escape(item["title"])}</span></a>'
        for item in catalog
    )
    options = "".join(f'<option value="{part}">Parte {part:02d}</option>' for part in range(1, 69))
    script = """<script>const q=document.querySelector('#q'),p=document.querySelector('#part'),cards=[...document.querySelectorAll('.lesson-link')],count=document.querySelector('#count');function filter(){const t=q.value.trim().toLocaleLowerCase('es').normalize('NFD').replace(/[\\u0300-\\u036f]/g,''),part=p.value;let n=0;for(const c of cards){const key=c.dataset.title.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');const show=(!t||key.includes(t))&&(!part||c.dataset.part===part);c.classList.toggle('hide',!show);if(show)n++}count.textContent=n+' clases visibles'}q.addEventListener('input',filter);p.addEventListener('change',filter);filter()</script>"""
    body = f'<main id="main" class="wrap section"><p class="kicker">Catálogo completo</p><h1>680 clases · 68 partes</h1><p class="lede">Busca por identificador o concepto. Cada parte contiene diez clases y conserva la secuencia ARQ-001 → ARQ-680.</p><div class="catalog-tools"><label>Buscar clase<input id="q" type="search" placeholder="Ej. madera, sismo, ARQ-240"></label><label>Filtrar por parte<select id="part"><option value="">Todas las partes</option>{options}</select></label></div><p id="count" class="lede" aria-live="polite"></p><div class="catalog-list">{cards}</div>{script}</main>'
    return shell("Catálogo de 680 clases · Arquitectura", body)


def parts_index(catalog: list[dict], titles: dict[int, str]) -> str:
    cards = "".join(
        f'<a class="part-card" href="parte-{part:02d}.html"><small>Parte {part:02d}</small><strong>{html.escape(titles[part])}</strong><span>ARQ-{(part-1)*10+1:03d} → ARQ-{part*10:03d} · 10 clases</span></a>'
        for part in range(1, 69)
    )
    body = f'<main id="main" class="wrap section"><p class="kicker">Mapa curricular</p><h1>68 partes · 680 clases</h1><p class="lede">La secuencia completa, desde fundamentos del habitar hasta casos integradores de tipologías y grandes obras.</p><div class="part-grid">{cards}</div></main>'
    return shell("68 partes · Arquitectura", body, prefix="../")


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


def documentation_portal() -> str:
    cards = "".join(
        f'<a class="resource-card" href="{slug}"><b>{html.escape(title)}</b><span>{html.escape(description)}</span></a>'
        for filename, (slug, title), description in (
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
                "COMO_USAR_EL_PROGRAMA.md",
                DOC_PAGES["COMO_USAR_EL_PROGRAMA.md"],
                "entradas para estudiantes, docentes, profesionales y mandantes",
            ),
            (
                "RUTAS_DE_APRENDIZAJE.md",
                DOC_PAGES["RUTAS_DE_APRENDIZAJE.md"],
                "doce recorridos temáticos a través del currículo",
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
                "MATRIZ_PARIDAD_REFERENCIA.md",
                DOC_PAGES["MATRIZ_PARIDAD_REFERENCIA.md"],
                "qué se aplicó, adaptó o descartó y por qué",
            ),
            (
                "SEGURIDAD_Y_ETICA_PROFESIONAL.md",
                DOC_PAGES["SEGURIDAD_Y_ETICA_PROFESIONAL.md"],
                "límites para obras, emergencias, personas, patrimonio e IA",
            ),
        )
    )
    cards += '<a class="resource-card" href="bibliografia.html"><b>Registro central de fuentes</b><span>622 URLs externas y las 680 clases que las utilizan</span></a>'
    body = f'<main id="main" class="wrap section"><p class="kicker">Documentación del programa</p><h1>Leer antes de contar</h1><p class="lede">Método, procedencia, uso, cobertura y límites documentados fuera del README para que cada afirmación pueda revisarse.</p><div class="resource-grid">{cards}</div></main>'
    return shell("Documentación · Arquitectura", body)


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


def main() -> int:
    catalog = load_catalog()
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
    write("documentacion.html", documentation_portal())
    write("partes/index.html", parts_index(catalog, titles))
    for part in range(1, 69):
        write(f"partes/parte-{part:02d}.html", part_page(part, catalog, titles))

    for index, item in enumerate(catalog):
        content = render_markdown((ROOT / item["source"]).read_text(encoding="utf-8"))
        previous = catalog[index - 1] if index else None
        following = catalog[index + 1] if index + 1 < len(catalog) else None
        body = f'<main id="main" class="doc"><p class="kicker">Parte {item["part"]:02d} · Clase {index+1} de 680</p>{content}{nav(previous, following)}</main>'
        write(f'clases/{item["id"].lower()}.html', shell(f'{item["id"]} · {item["title"]}', body, description=item["title"], prefix="../"))

    for kind, (folder, _label, _description) in RESOURCE_TYPES.items():
        write(f"{folder}/index.html", resource_index(kind, entries))
    for entry in resource_entries:
        write(entry_path(entry), resource_page(entry, lookup))

    page_from_markdown("metodo.html", ROOT / "docs" / "METODO_Y_ALCANCE.md", "Método y alcance · Arquitectura")
    page_from_markdown("artefactos.html", ROOT / "docs" / "ARTEFACTOS.md", "Descargas · Arquitectura")
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
            f'<main id="main" class="doc">{rendered_bibliography}</main>',
        ),
    )
    bibliography_target = OUT / "sources" / "bibliography.json"
    bibliography_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "sources" / "bibliography.json", bibliography_target)
    shutil.copy2(READER, OUT / "lector-offline-v1.0.html")
    for filename in ("Arquitectura_20_Clases_Finales_v1.0.pdf", "ARQ-680_Clase_Completa_v1.0.pdf"):
        shutil.copy2(ROOT / filename, OUT / filename)
    write(".nojekyll", "")
    write("404.html", shell("Página no encontrada", '<main id="main" class="doc"><h1>Página no encontrada</h1><p>Vuelve al <a href="index.html">inicio</a> o consulta el <a href="catalogo.html">catálogo completo</a>.</p></main>'))
    print(
        f"Built {len(catalog)} lessons, 68 part pages, "
        f"{len(resource_entries)} resource pages and the portal in {OUT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
