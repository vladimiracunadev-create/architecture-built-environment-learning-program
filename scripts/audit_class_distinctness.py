# SPDX-License-Identifier: Apache-2.0
"""Audit whether the 800 lessons contain distinguishable editorial substance."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
SUMMARY_PATH = ROOT / "data" / "audits" / "class-distinctness.json"
ROWS_PATH = ROOT / "docs" / "audits" / "class-distinctness.csv"
PEDAGOGY_BLOCK = re.compile(
    r"<!-- pedagogia-2026:inicio -->.*?<!-- pedagogia-2026:fin -->",
    re.DOTALL,
)
SOURCE_SECTION = re.compile(r"\n## Fuentes y alcance de uso\n.*\Z", re.DOTALL)
WORD = re.compile(r"[a-záéíóúüñ0-9]+", re.IGNORECASE)
MERMAID = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)
QUESTION = re.compile(r"## Pregunta central\s+(.+?)(?=\n## )", re.DOTALL)
CRITICAL = re.compile(r"\*\*Fallo crítico de esta clase:\*\*\s*(.+?)\.")
DISCLAIMER = (
    "Material educativo independiente. Esta clase no sustituye formación acreditada, experiencia supervisada, "
    "encargo profesional, normativa vigente, cálculo firmado, permiso ni revisión de especialistas. Los datos del "
    "caso son didácticos y deben reemplazarse por antecedentes verificables antes de una aplicación real."
)


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def words(value: str) -> list[str]:
    return WORD.findall(value.lower())


def editorial_core(text: str) -> str:
    text = PEDAGOGY_BLOCK.sub("", text)
    text = SOURCE_SECTION.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def prose_paragraphs(text: str) -> list[str]:
    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        compact = re.sub(r"\s+", " ", block.strip())
        if not compact or compact.startswith(("#", "```", "- ")):
            continue
        if re.match(r"^\d+\.\s", compact):
            continue
        if len(words(compact)) >= 25:
            paragraphs.append(compact)
    return paragraphs


def shingles(text: str, width: int = 5) -> set[str]:
    tokens = words(text)
    return {" ".join(tokens[index : index + width]) for index in range(max(0, len(tokens) - width + 1))}


def jaccard(left: set[str], right: set[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def extract(pattern: re.Pattern[str], text: str) -> str:
    match = pattern.search(text)
    return re.sub(r"\s+", " ", match.group(1).strip()) if match else ""


def render_csv(rows: list[dict[str, object]]) -> str:
    output = io.StringIO(newline="")
    fieldnames = [
        "class_id",
        "part",
        "title",
        "words",
        "file_hash",
        "question_hash",
        "graph_hash",
        "critical_hash",
        "unique_editorial_word_share",
        "nearest_class_same_part",
        "nearest_similarity_same_part",
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def build_audit() -> tuple[dict[str, object], str, list[str]]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    records: list[dict[str, object]] = []
    paragraph_owners: defaultdict[str, set[str]] = defaultdict(set)
    for item in catalog:
        path = ROOT / item["source"]
        text = path.read_text(encoding="utf-8")
        core = editorial_core(text)
        mermaid = extract(MERMAID, core)
        question = extract(QUESTION, core)
        critical = extract(CRITICAL, core)
        paragraphs = prose_paragraphs(core)
        for paragraph in set(paragraphs):
            paragraph_owners[paragraph].add(item["id"])
        records.append(
            {
                "class_id": item["id"],
                "part": int(item["part"]),
                "title": item["title"],
                "words": len(words(text)),
                "file_hash": digest(text),
                "question_hash": digest(question),
                "graph_hash": digest(mermaid),
                "critical_hash": digest(critical),
                "question": question,
                "graph": mermaid,
                "critical": critical,
                "paragraphs": paragraphs,
                "shingles": shingles(core),
            }
        )

    by_part: defaultdict[int, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        by_part[int(record["part"])].append(record)

    rows: list[dict[str, object]] = []
    for record in records:
        neighbours = [candidate for candidate in by_part[int(record["part"])] if candidate is not record]
        similarities = [
            (jaccard(record["shingles"], candidate["shingles"]), str(candidate["class_id"]))
            for candidate in neighbours
        ]
        nearest_score, nearest_id = max(similarities, default=(0.0, ""))
        total = sum(len(words(paragraph)) for paragraph in record["paragraphs"])
        unique = sum(
            len(words(paragraph))
            for paragraph in record["paragraphs"]
            if len(paragraph_owners[paragraph]) == 1
        )
        rows.append(
            {
                "class_id": record["class_id"],
                "part": record["part"],
                "title": record["title"],
                "words": record["words"],
                "file_hash": record["file_hash"],
                "question_hash": record["question_hash"],
                "graph_hash": record["graph_hash"],
                "critical_hash": record["critical_hash"],
                "unique_editorial_word_share": f"{unique / total:.4f}" if total else "0.0000",
                "nearest_class_same_part": nearest_id,
                "nearest_similarity_same_part": f"{nearest_score:.4f}",
            }
        )

    allowed = {DISCLAIMER}
    repeated = [
        (paragraph, sorted(owners))
        for paragraph, owners in paragraph_owners.items()
        if len(owners) > 1 and paragraph not in allowed
    ]
    repeated.sort(key=lambda pair: (-len(pair[1]), pair[0]))
    phase_three_ids = {f"ARQ-{number:03d}" for number in range(681, 801)}
    phase_three_repeated = [
        {"uses": len(phase_three_ids & set(owners)), "sample_classes": sorted(phase_three_ids & set(owners))[:5], "text": paragraph}
        for paragraph, owners in repeated
        if len(phase_three_ids & set(owners)) > 10
    ]
    phase_three = [record for record in records if record["class_id"] in phase_three_ids]
    row_by_id = {str(row["class_id"]): row for row in rows}

    def similarity_summary(group: list[dict[str, object]]) -> dict[str, object]:
        unique_shares = sorted(float(row_by_id[str(record["class_id"])]["unique_editorial_word_share"]) for record in group)
        nearest = sorted(float(row_by_id[str(record["class_id"])]["nearest_similarity_same_part"]) for record in group)
        middle = len(group) // 2
        return {
            "minimum_unique_editorial_word_share": unique_shares[0],
            "median_unique_editorial_word_share": unique_shares[middle],
            "maximum_nearest_similarity_same_part": nearest[-1],
            "median_nearest_similarity_same_part": nearest[middle],
        }

    nonempty_questions = [record["question"] for record in records if record["question"]]
    nonempty_graphs = [record["graph"] for record in records if record["graph"]]
    nonempty_critical = [record["critical"] for record in records if record["critical"]]
    counts = {
        "files": len(records),
        "exact_unique_files": len({record["file_hash"] for record in records}),
        "classes_with_central_question": len(nonempty_questions),
        "unique_questions": len(set(nonempty_questions)),
        "classes_with_editorial_graph": len(nonempty_graphs),
        "unique_editorial_graphs": len(set(nonempty_graphs)),
        "classes_with_explicit_critical_condition": len(nonempty_critical),
        "unique_explicit_critical_conditions": len(set(nonempty_critical)),
        "total_words": sum(int(record["words"]) for record in records),
        "minimum_words": min(int(record["words"]) for record in records),
        "median_words": sorted(int(record["words"]) for record in records)[len(records) // 2],
        "maximum_words": max(int(record["words"]) for record in records),
        **similarity_summary(records),
    }
    phase_counts = {
        "files": len(phase_three),
        "exact_unique_files": len({record["file_hash"] for record in phase_three}),
        "unique_questions": len({record["question_hash"] for record in phase_three}),
        "unique_graphs": len({record["graph_hash"] for record in phase_three}),
        "unique_critical_conditions": len({record["critical_hash"] for record in phase_three}),
        "minimum_words": min(int(record["words"]) for record in phase_three),
        "maximum_words": max(int(record["words"]) for record in phase_three),
        "unallowed_long_paragraphs_repeated_over_ten_classes": len(phase_three_repeated),
        **similarity_summary(phase_three),
    }
    top_repeated = [
        {
            "uses": len(owners),
            "sample_classes": owners[:5],
            "text_excerpt": paragraph[:240],
        }
        for paragraph, owners in repeated[:20]
    ]
    summary: dict[str, object] = {
        "scope": "800 authored lesson files; generated pedagogy contracts and source lists excluded from editorial repetition analysis",
        "all_classes": counts,
        "phase_three_arq_681_800": phase_counts,
        "repeated_editorial_paragraphs": {
            "total_patterns_used_by_two_or_more_classes": len(repeated),
            "patterns_used_by_over_ten_classes": sum(1 for _, owners in repeated if len(owners) > 10),
            "top_patterns": top_repeated,
            "patterns_used_by_over_ten_phase_three_classes": phase_three_repeated,
        },
        "method": {
            "exactness": "SHA-256 prefixes over the complete Markdown, central question, first Mermaid graph and critical condition",
            "originality": "word-weighted share of prose paragraphs used by one class after excluding generated contracts and sources",
            "near_similarity": "Jaccard similarity of five-word shingles against the other nine classes in the same part",
        },
    }
    errors: list[str] = []
    if counts["files"] != 800 or counts["exact_unique_files"] != 800:
        errors.append("Expected 800 distinct lesson files")
    if phase_counts["unique_questions"] != 120:
        errors.append("Phase III must contain 120 distinct central questions")
    if phase_counts["unique_graphs"] != 120:
        errors.append("Phase III must contain 120 distinct topic graphs")
    if phase_counts["unique_critical_conditions"] != 120:
        errors.append("Phase III must contain 120 distinct critical conditions")
    if phase_counts["unallowed_long_paragraphs_repeated_over_ten_classes"]:
        errors.append("Phase III still contains unapproved long editorial boilerplate")
    return summary, render_csv(rows), errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Update the committed JSON summary and class-by-class CSV")
    parser.add_argument("--check", action="store_true", help="Check committed audit artifacts")
    args = parser.parse_args()
    summary, csv_text, errors = build_audit()
    json_text = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        ROWS_PATH.parent.mkdir(parents=True, exist_ok=True)
        SUMMARY_PATH.write_text(json_text, encoding="utf-8", newline="\n")
        ROWS_PATH.write_text(csv_text, encoding="utf-8", newline="\n")
    if args.check:
        if not SUMMARY_PATH.exists() or SUMMARY_PATH.read_text(encoding="utf-8") != json_text:
            errors.append(f"Stale audit summary: {SUMMARY_PATH.relative_to(ROOT)}")
        if not ROWS_PATH.exists() or ROWS_PATH.read_text(encoding="utf-8") != csv_text:
            errors.append(f"Stale class audit: {ROWS_PATH.relative_to(ROOT)}")
    print(json_text, end="")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
