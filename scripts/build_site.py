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

CSS = r"""
:root{--ink:#172526;--muted:#5a6967;--paper:#f4f0e7;--card:#fffdf7;--line:#d9d4c8;--navy:#102f38;--teal:#1d6b68;--clay:#b85c38;--gold:#ddb967;--focus:#0067c5;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.65}a{color:var(--teal);text-underline-offset:3px}.skip{position:absolute;top:-80px;left:1rem;background:#fff;padding:.7rem 1rem;z-index:50}.skip:focus{top:1rem}.topbar{position:sticky;top:0;z-index:20;background:rgba(16,47,56,.96);color:#fff;border-bottom:1px solid rgba(255,255,255,.16);backdrop-filter:blur(12px)}.topbar .inner{max-width:1180px;margin:auto;padding:.72rem 1.25rem;display:flex;align-items:center;justify-content:space-between;gap:1rem}.brand{font-weight:800;color:#fff;text-decoration:none;letter-spacing:.02em}.nav{display:flex;gap:1rem;flex-wrap:wrap}.nav a{color:#eaf2ef;text-decoration:none;font-size:.9rem}.hero{position:relative;overflow:hidden;color:#fff;background:linear-gradient(135deg,#0e2932 0%,#164e52 62%,#8d472f 145%);padding:6rem 1.25rem 5rem}.hero:before{content:"";position:absolute;inset:0;opacity:.12;background-image:linear-gradient(#fff 1px,transparent 1px),linear-gradient(90deg,#fff 1px,transparent 1px);background-size:36px 36px;mask-image:linear-gradient(to bottom,#000,transparent)}.hero .inner{position:relative;max-width:1180px;margin:auto}.eyebrow{text-transform:uppercase;letter-spacing:.17em;font-size:.74rem;color:#ecd99f;font-weight:800}.hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(2.4rem,6vw,5.3rem);line-height:.98;max-width:900px;margin:.7rem 0 1.2rem;letter-spacing:-.035em}.hero p{font-size:clamp(1rem,2vw,1.28rem);max-width:760px;color:#e7efec}.actions{display:flex;gap:.75rem;flex-wrap:wrap;margin-top:1.8rem}.button{display:inline-block;padding:.72rem 1.05rem;border:1px solid rgba(255,255,255,.35);border-radius:7px;color:#fff;text-decoration:none;font-weight:750}.button.primary{background:var(--gold);color:#172526;border-color:var(--gold)}.wrap{max-width:1180px;margin:auto;padding:0 1.25rem}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin:-1.5rem auto 3rem;position:relative}.stat{background:var(--card);padding:1.35rem}.stat strong{font-family:Georgia,serif;font-size:2.1rem;color:var(--clay);display:block;line-height:1}.stat span{font-size:.84rem;color:var(--muted)}.section{padding:2.5rem 0}.section h2{font-family:Georgia,serif;font-size:clamp(1.8rem,3vw,2.5rem);margin:0 0 .6rem}.lede{color:var(--muted);max-width:760px;margin:0 0 1.5rem}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.card{background:var(--card);border:1px solid var(--line);padding:1.25rem;border-radius:8px}.card .num{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:var(--clay);font-weight:800}.card h3{margin:.35rem 0;font-size:1.05rem}.card p{margin:.3rem 0;color:var(--muted);font-size:.92rem}.catalog-tools{display:grid;grid-template-columns:1fr 220px;gap:.8rem;margin:1.5rem 0}.catalog-tools input,.catalog-tools select{width:100%;padding:.8rem;border:1px solid var(--line);border-radius:6px;background:var(--card);font:inherit}.catalog-list{display:grid;grid-template-columns:repeat(2,1fr);gap:.7rem}.lesson-link{display:flex;gap:.8rem;align-items:flex-start;background:var(--card);border:1px solid var(--line);padding:.9rem;border-radius:7px;text-decoration:none;color:var(--ink)}.lesson-link:hover{border-color:var(--teal);transform:translateY(-1px)}.lesson-code{font-size:.72rem;color:var(--clay);font-weight:850;white-space:nowrap}.lesson-title{font-size:.92rem;line-height:1.35}.doc{max-width:900px;margin:2.5rem auto 5rem;background:var(--card);border:1px solid var(--line);padding:clamp(1.2rem,4vw,3.4rem);box-shadow:0 18px 50px rgba(22,43,43,.08)}.doc h1{font-family:Georgia,serif;font-size:clamp(2rem,4vw,3.25rem);line-height:1.05;margin-top:.3rem}.doc h2{font-family:Georgia,serif;font-size:1.65rem;margin-top:2.4rem;padding-top:1rem;border-top:1px solid var(--line)}.doc h3{margin-top:1.8rem}.doc table{display:block;overflow:auto;border-collapse:collapse;margin:1.2rem 0}.doc th,.doc td{border:1px solid var(--line);padding:.65rem;min-width:120px;text-align:left;vertical-align:top}.doc th{background:#ebe6da}.doc blockquote{margin:1.2rem 0;border-left:4px solid var(--clay);padding:.2rem 1rem;color:var(--muted)}.doc code{background:#ece9df;padding:.12rem .3rem;border-radius:4px}.doc pre{overflow:auto;background:#172526;color:#f4f0e7;padding:1rem;border-radius:7px}.lesson-nav{display:grid;grid-template-columns:1fr 1fr;gap:1rem;border-top:1px solid var(--line);margin-top:2.6rem;padding-top:1.2rem}.lesson-nav a:last-child{text-align:right}.kicker{font-size:.76rem;text-transform:uppercase;letter-spacing:.13em;color:var(--clay);font-weight:850}.notice{background:#eef3ec;border-left:4px solid var(--teal);padding:.9rem 1rem;margin:1rem 0}.footer{background:var(--navy);color:#dbe7e3;margin-top:3rem}.footer .inner{max-width:1180px;margin:auto;padding:2rem 1.25rem;display:flex;justify-content:space-between;gap:2rem;flex-wrap:wrap}.footer a{color:#fff}.footer small{max-width:680px}.hide{display:none!important}
@media(max-width:780px){.nav{display:none}.hero{padding:4rem 1.1rem}.stats{grid-template-columns:repeat(2,1fr)}.grid,.catalog-list{grid-template-columns:1fr}.catalog-tools{grid-template-columns:1fr}.doc{margin:1rem .7rem 3rem;padding:1.15rem}.lesson-nav{grid-template-columns:1fr}.lesson-nav a:last-child{text-align:left}}
@media print{.topbar,.footer,.lesson-nav{display:none}.doc{border:0;box-shadow:none;margin:0;max-width:none;padding:0}body{background:#fff}.doc a{color:inherit}}
"""


def load_catalog() -> list[dict]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def legacy_entries() -> list[dict]:
    text = READER.read_text(encoding="utf-8")
    marker = "const ENTRIES="
    start = text.index(marker) + len(marker)
    end = text.index("];\nconst byId", start) + 1
    return json.loads(text[start:end])


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
<a class="brand" href="{prefix}index.html">⌂ ARQ · 680</a><nav class="nav" aria-label="Principal"><a href="{prefix}catalogo.html">Clases</a><a href="{prefix}metodo.html">Método</a><a href="{prefix}artefactos.html">Descargas</a><a href="{REPO_URL}">GitHub</a></nav>
</div></header>{body}<footer class="footer"><div class="inner"><small><strong>Programa Integral de Arquitectura, Construcción y Entorno Habitado.</strong><br>Material educativo independiente. No otorga título, licencia profesional ni autorización para ejecutar obras.</small><small><a href="{prefix}catalogo.html">680 clases</a> · <a href="{prefix}metodo.html">Alcance</a> · <a href="{REPO_URL}">Código fuente</a></small></div></footer></body></html>"""


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


def landing() -> str:
    body = """<main id="main"><section class="hero"><div class="inner"><p class="eyebrow">Edición definitiva v1.0 · Español</p><h1>Arquitectura,<br>construcción y<br>entorno habitado</h1><p>Un programa secuencial para aprender a leer el proyecto como sistema: personas, lugar, materia, técnica, recursos, operación y tiempo.</p><div class="actions"><a class="button primary" href="catalogo.html">Explorar las 680 clases</a><a class="button" href="metodo.html">Conocer el método</a></div></div></section>
<div class="wrap"><section class="stats" aria-label="Cifras verificadas"><div class="stat"><strong>680</strong><span>clases completas</span></div><div class="stat"><strong>68</strong><span>partes curriculares</span></div><div class="stat"><strong>80</strong><span>roles y oficios mapeados</span></div><div class="stat"><strong>20</strong><span>clases finales en v1.0</span></div></section>
<section class="section"><p class="eyebrow" style="color:var(--clay)">De punta a punta</p><h2>Aprender a decidir, no a copiar soluciones</h2><p class="lede">Cada clase separa dato, hipótesis, cálculo, evidencia, responsabilidad y autorización. Los casos son didácticos y declaran sus fronteras.</p><div class="grid"><article class="card"><span class="num">01 · Secuencia</span><h3>De fundamentos a integración</h3><p>Representación, historia, territorio, estructuras, instalaciones, gestión, patrimonio y grandes tipologías.</p></article><article class="card"><span class="num">02 · Evidencia</span><h3>Fuentes con alcance</h3><p>Las referencias enseñan mecanismos; no se convierten automáticamente en norma aplicable a un caso real.</p></article><article class="card"><span class="num">03 · Continuidad</span><h3>Proyecto, obra y operación</h3><p>Las decisiones se siguen desde el encargo hasta el mantenimiento, la adaptación y el fin de vida.</p></article></div></section>
<section class="section"><h2>Una biblioteca abierta y navegable</h2><p class="lede">El contenido fuente vive en Markdown. El sitio transforma cada clase en una página HTML rápida, enlazable e imprimible; el lector monolítico original permanece disponible para consulta offline.</p><div class="actions"><a class="button primary" style="background:var(--teal);color:#fff;border-color:var(--teal)" href="catalogo.html">Abrir catálogo</a><a class="button" style="color:var(--teal);border-color:var(--teal)" href="artefactos.html">Descargar artefactos</a></div></section></div></main>"""
    return shell("Arquitectura, construcción y entorno habitado", body, description="680 clases en 68 partes sobre arquitectura, construcción y entorno habitado, publicadas como HTML en GitHub Pages.")


def catalog_page(catalog: list[dict]) -> str:
    cards = "".join(
        f'<a class="lesson-link" data-title="{html.escape((item["id"]+" "+item["title"]).lower())}" data-part="{item["part"]}" href="clases/{item["id"].lower()}.html"><span class="lesson-code">{item["id"]}</span><span class="lesson-title">{html.escape(item["title"])}</span></a>'
        for item in catalog
    )
    options = "".join(f'<option value="{part}">Parte {part:02d}</option>' for part in range(1, 69))
    script = """<script>const q=document.querySelector('#q'),p=document.querySelector('#part'),cards=[...document.querySelectorAll('.lesson-link')],count=document.querySelector('#count');function filter(){const t=q.value.trim().toLocaleLowerCase('es').normalize('NFD').replace(/[\\u0300-\\u036f]/g,''),part=p.value;let n=0;for(const c of cards){const key=c.dataset.title.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');const show=(!t||key.includes(t))&&(!part||c.dataset.part===part);c.classList.toggle('hide',!show);if(show)n++}count.textContent=n+' clases visibles'}q.addEventListener('input',filter);p.addEventListener('change',filter);filter()</script>"""
    body = f'<main id="main" class="wrap section"><p class="kicker">Catálogo completo</p><h1>680 clases · 68 partes</h1><p class="lede">Busca por identificador o concepto. Cada parte contiene diez clases y conserva la secuencia ARQ-001 → ARQ-680.</p><div class="catalog-tools"><label>Buscar clase<input id="q" type="search" placeholder="Ej. madera, sismo, ARQ-240"></label><label>Filtrar por parte<select id="part"><option value="">Todas las partes</option>{options}</select></label></div><p id="count" class="lede" aria-live="polite"></p><div class="catalog-list">{cards}</div>{script}</main>'
    return shell("Catálogo de 680 clases · Arquitectura", body)


def page_from_markdown(name: str, source: Path, title: str) -> None:
    rendered = render_markdown(source.read_text(encoding="utf-8"))
    body = f'<main id="main" class="doc">{rendered}</main>'
    write(name, shell(title, body))


def main() -> int:
    catalog = load_catalog()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    write("assets/site.css", CSS.strip() + "\n")
    shutil.copy2(ROOT / "assets" / "mark.svg", OUT / "assets" / "mark.svg")
    write("index.html", landing())
    write("catalogo.html", catalog_page(catalog))

    for index, item in enumerate(catalog):
        content = render_markdown((ROOT / item["source"]).read_text(encoding="utf-8"))
        previous = catalog[index - 1] if index else None
        following = catalog[index + 1] if index + 1 < len(catalog) else None
        body = f'<main id="main" class="doc"><p class="kicker">Parte {item["part"]:02d} · Clase {index+1} de 680</p>{content}{nav(previous, following)}</main>'
        write(f'clases/{item["id"].lower()}.html', shell(f'{item["id"]} · {item["title"]}', body, description=item["title"], prefix="../"))

    sources = [entry for entry in legacy_entries() if entry["kind"] == "fuente"]
    for source in sources:
        body = f'<main id="main" class="doc"><p class="kicker">Fuente y alcance de uso</p>{source["html"]}</main>'
        write(f'fuentes/{source["id"].lower()}.html', shell(source["title"], body, prefix="../"))

    page_from_markdown("metodo.html", ROOT / "docs" / "METODO_Y_ALCANCE.md", "Método y alcance · Arquitectura")
    page_from_markdown("artefactos.html", ROOT / "docs" / "ARTEFACTOS.md", "Descargas · Arquitectura")
    shutil.copy2(READER, OUT / "lector-offline-v1.0.html")
    for filename in ("Arquitectura_20_Clases_Finales_v1.0.pdf", "ARQ-680_Clase_Completa_v1.0.pdf"):
        shutil.copy2(ROOT / filename, OUT / filename)
    write(".nojekyll", "")
    write("404.html", shell("Página no encontrada", '<main id="main" class="doc"><h1>Página no encontrada</h1><p>Vuelve al <a href="index.html">inicio</a> o consulta el <a href="catalogo.html">catálogo completo</a>.</p></main>'))
    print(f"Built {len(catalog)} lessons, {len(sources)} source pages and the portal in {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
