#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Generate the Markdown navigation layer for all 68 curriculum parts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
READER = ROOT / "programa-arquitectura-lector-definitivo-v1.0.html"


def part_titles() -> dict[int, str]:
    text = READER.read_text(encoding="utf-8")
    matches = re.findall(r'<option value="(\d+)">(\d+)\s*·\s*([^<]+)</option>', text)
    titles = {int(value): title.strip() for value, _number, title in matches}
    if set(titles) != set(range(1, 69)):
        raise ValueError("the reader does not contain the 68 canonical part titles")
    return titles


def section(text: str, patterns: tuple[str, ...]) -> str:
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    for index, heading in enumerate(headings):
        title = heading.group(1).lower()
        if any(re.search(pattern, title) for pattern in patterns):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            value = text[heading.end() : end].strip()
            value = re.sub(r"<details.*?</details>", "", value, flags=re.DOTALL)
            value = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", value)
            value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
            value = re.sub(r"[`*_>#]", "", value)
            value = re.sub(r"\s+", " ", value).strip()
            return value
    return ""


def first_sentence(value: str, limit: int = 260) -> str:
    if not value:
        return "La clase declara su alcance, práctica y continuidad en el documento completo."
    match = re.search(r"(?<=[.!?])\s+", value)
    result = value[: match.start() + 1] if match else value
    if len(result) > limit:
        result = result[: limit - 1].rsplit(" ", 1)[0] + "…"
    return result


def relative_link(item: dict) -> str:
    return Path(item["source"]).name


def part_readme(part: int, title: str, lessons: list[dict]) -> str:
    details = []
    for item in lessons:
        text = (ROOT / item["source"]).read_text(encoding="utf-8")
        question = first_sentence(section(text, (r"pregunta central",)))
        result = first_sentence(
            section(
                text,
                (
                    r"resultado.*continuidad",
                    r"resultado de aprendizaje",
                    r"qué aprenderás",
                ),
            )
        )
        details.append((item, question, result))

    questions = "\n".join(
        f"- **{item['id']}:** {question}" for item, question, _result in details
    )
    outcomes = "\n".join(
        f"| [{item['id']}]({relative_link(item)}) | {result} |"
        for item, _question, result in details
    )
    classes = "\n".join(
        f"| {index:02d} | [{item['id']} · {item['title']}]({relative_link(item)}) |"
        for index, item in enumerate(lessons, 1)
    )
    previous = (
        f"[← Parte {part - 1:02d}](../parte-{part - 1:02d}/README.md)"
        if part > 1
        else "[← Índice general](../README.md)"
    )
    following = (
        f"[Parte {part + 1:02d} →](../parte-{part + 1:02d}/README.md)"
        if part < 68
        else "[Índice general →](../README.md)"
    )
    phase = (
        "Fase I · formación transversal"
        if part <= 48
        else "Fase II · tipologías y grandes obras"
    )
    return f"""# Parte {part:02d} — {title}

**{phase} · 10 clases · {lessons[0]['id']} → {lessons[-1]['id']}**

Esta parte comienza con **{lessons[0]['title']}** y culmina con **{lessons[-1]['title']}**. Las diez clases forman una secuencia: cada una declara su pregunta, resultado, caso o práctica, fuentes y límites.

> Material educativo independiente. Este bloque no habilita para diseñar, calcular, firmar, autorizar ni ejecutar obras. Los parámetros de los casos no se transfieren a un proyecto real sin antecedentes, normativa y especialistas competentes.

## Problemas que articula

{questions}

## Resultados y continuidad declarados

| Clase | Resultado o entrega principal |
|---|---|
{outcomes}

## Recorrido clase a clase

| # | Clase |
|---:|---|
{classes}

## Cómo recorrer esta parte

1. Lee las clases en orden cuando el tema sea nuevo; la continuidad está escrita dentro de cada documento.
2. Conserva separados dato, hipótesis, cálculo, evidencia, responsabilidad y autorización.
3. Resuelve la práctica independiente antes de abrir la solución orientativa o autoevaluación.
4. Revisa el apartado **Fuentes y alcance de uso**: una referencia apoya una afirmación delimitada, no certifica el caso completo.
5. Registra toda incertidumbre que cambiaría la decisión; “desconocido” no equivale a cero, seguro ni conforme.

## Navegación

{previous} · [Mapa de las 68 partes](../README.md) · {following}
"""


def curriculum_index(catalog: list[dict], titles: dict[int, str]) -> str:
    rows = []
    for part in range(1, 69):
        lessons = [item for item in catalog if item["part"] == part]
        focus = f"{lessons[0]['title']} → {lessons[-1]['title']}"
        rows.append(
            f"| {part:02d} | [{titles[part]}](parte-{part:02d}/README.md) | "
            f"{lessons[0]['id']}–{lessons[-1]['id']} | {focus} |"
        )
    return f"""# Currículo completo

## 680 clases · 68 partes · dos fases

Este índice es la entrada Markdown al programa. Cada parte tiene diez clases y un README propio generado desde las preguntas y resultados declarados en sus fuentes.

- **Fase I — Partes 01–48:** fundamentos, representación, historia, personas, territorio, proyecto, técnica, construcción, gestión, operación e investigación.
- **Fase II — Partes 49–68:** tipologías edilicias, infraestructuras y casos integradores.

## Anatomía documental de una clase

Las 680 clases incluyen una pregunta central, práctica independiente, fuentes con alcance de uso y límites profesionales. La formulación de resultados, casos, errores y autoevaluación evoluciona entre etapas del programa; el [estado verificable](../docs/ESTADO_VERIFICABLE.md) muestra esa cobertura sin fingir uniformidad.

## Mapa completo

| # | Parte | Clases | Recorrido |
|---:|---|---:|---|
{chr(10).join(rows)}

## Uso responsable

El orden expresa dependencias de conocimiento, no un calendario obligatorio. Estudiar el material no reemplaza formación acreditada, experiencia supervisada, normativa vigente, revisión especializada ni habilitación profesional.
"""


def write_document(path: Path, content: str, check: bool) -> None:
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            raise ValueError(f"generated documentation is stale: {path.relative_to(ROOT)}")
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if generated Markdown does not match the curriculum",
    )
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    titles = part_titles()
    for part in range(1, 69):
        lessons = [item for item in catalog if item["part"] == part]
        if len(lessons) != 10:
            raise ValueError(f"part {part} has {len(lessons)} lessons")
        path = ROOT / "classes" / f"parte-{part:02d}" / "README.md"
        write_document(
            path,
            part_readme(part, titles[part], lessons),
            args.check,
        )
    write_document(
        ROOT / "classes" / "README.md",
        curriculum_index(catalog, titles),
        args.check,
    )
    verb = "Verified" if args.check else "Generated"
    print(f"{verb} classes/README.md and 68 part README files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
