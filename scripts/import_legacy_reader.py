#!/usr/bin/env python3
"""Recover the 680 Markdown lessons embedded in the definitive v1.0 reader."""

from __future__ import annotations

import json
import html
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READER = ROOT / "programa-arquitectura-lector-definitivo-v1.0.html"
CLASSES = ROOT / "classes"
CATALOG = ROOT / "data" / "catalog.json"


def entries() -> list[dict]:
    text = READER.read_text(encoding="utf-8")
    marker = "const ENTRIES="
    start = text.index(marker) + len(marker)
    end = text.index("];\nconst byId", start) + 1
    return json.loads(text[start:end])


def inline(fragment: str) -> str:
    fragment = re.sub(
        r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>',
        lambda match: f'[{inline(match.group(2))}]({html.unescape(match.group(1))})',
        fragment,
        flags=re.DOTALL | re.IGNORECASE,
    )
    replacements = (
        (r"<(?:strong|b)>(.*?)</(?:strong|b)>", r"**\1**"),
        (r"<(?:em|i)>(.*?)</(?:em|i)>", r"*\1*"),
        (r"<code>(.*?)</code>", r"`\1`"),
        (r"<br\s*/?>", "\n"),
    )
    for pattern, replacement in replacements:
        fragment = re.sub(pattern, replacement, fragment, flags=re.DOTALL | re.IGNORECASE)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return html.unescape(fragment).strip()


def html_to_markdown(source: str) -> str:
    """Convert the conservative HTML emitted by the legacy reader to Markdown."""
    protected: list[str] = []

    def protect(match: re.Match) -> str:
        token = f"@@PROTECTED-{len(protected)}@@"
        protected.append(match.group(0))
        return f"\n\n{token}\n\n"

    text = re.sub(r"<(?:table|details)\b.*?</(?:table|details)>", protect, source,
                  flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(
        r'<pre><code(?:\s+class="[^"]*")?>(.*?)</code></pre>',
        lambda match: "\n\n```\n" + html.unescape(match.group(1)).strip("\n") + "\n```\n\n",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    for level in range(1, 7):
        text = re.sub(
            rf"<h{level}[^>]*>(.*?)</h{level}>",
            lambda match, n=level: "\n\n" + "#" * n + " " + inline(match.group(1)) + "\n\n",
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )
    text = re.sub(
        r"<blockquote[^>]*>(.*?)</blockquote>",
        lambda match: "\n\n" + "\n".join("> " + line for line in inline(match.group(1)).splitlines()) + "\n\n",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(
        r"<li[^>]*>(.*?)</li>",
        lambda match: "\n- " + inline(match.group(1)),
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(r"</?(?:ul|ol)[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(
        r"<p[^>]*>(.*?)</p>",
        lambda match: "\n\n" + inline(match.group(1)) + "\n\n",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(r"<hr\s*/?>", "\n\n---\n\n", text, flags=re.IGNORECASE)
    text = inline(text)
    for index, block in enumerate(protected):
        text = text.replace(f"@@PROTECTED-{index}@@", block)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return unicodedata.normalize("NFC", text)


def clean_markdown(entry: dict) -> str:
    return html_to_markdown(entry["html"])


def write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    source = entries()
    lessons = sorted(
        (item for item in source if item["kind"] == "redactada"),
        key=lambda item: item["id"],
    )
    expected = [f"ARQ-{number:03d}" for number in range(1, 681)]
    actual = [item["id"] for item in lessons]
    if actual != expected:
        raise SystemExit("The embedded lesson sequence is not ARQ-001..ARQ-680")

    catalog = []
    for item in lessons:
        lesson_path = CLASSES / f"parte-{item['part']:02d}" / f"{item['id']}.md"
        write_if_changed(lesson_path, clean_markdown(item))
        catalog.append(
            {
                "id": item["id"],
                "title": item["title"],
                "part": item["part"],
                "is_new": bool(item.get("is_new")),
                "source": lesson_path.relative_to(ROOT).as_posix(),
            }
        )

    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    CATALOG.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Recovered {len(catalog)} lessons in 68 parts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
