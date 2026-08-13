#!/usr/bin/env python3
"""Snabb validering för romanprojektet Driftläge.

Valideringen använder endast Python-standardbiblioteket och är avsedd att kunna
köras både lokalt och i GitHub Actions. EPUB/PDF är exporter; de kan återskapas
från kanoniska Markdown-kapitel i `kapitel/`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

CHAPTER_RE = re.compile(r"kapitel-(\d{2})\.md$")
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")
MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]", "Kort kapitelnotering", "Kapitelnotering", "Efter kapitel")

REQUIRED_PATHS = (
    "README.md",
    "roman-bibel.md",
    "synopsis.md",
    "kapitelplan.md",
    "projektstatus.md",
    "project-index.md",
    "kapitel",
    "omslag/omslag-driftlage.png",
    "publishing/metadata.yaml",
    "publishing/epub.css",
    "publishing/fix-epub-after-pandoc.py",
    "publishing/pdf-template.tex",
    "publishing/pdf-filter.lua",
    "scripts/build_book.py",
)

REQUIRED_METADATA_KEYS = (
    "title",
    "subtitle",
    "author",
    "language",
    "cover-image",
)


def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def parse_simple_yaml_scalars(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.relative_to(root).parts:
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.is_dir():
        error(errors, f"Projektkatalogen finns inte: {root}")
        return 1

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    if errors:
        return 1

    metadata = parse_simple_yaml_scalars(root / "publishing/metadata.yaml")
    for key in REQUIRED_METADATA_KEYS:
        if not metadata.get(key):
            error(errors, f"Metadata saknar värde för: {key}")

    expected = {
        "title": "Driftläge",
        "subtitle": "En roman om kontroll, tillit och förändring",
        "author": "Erland Lindmark",
        "language": "sv-SE",
        "cover-image": "../omslag/omslag-driftlage.png",
    }
    for key, value in expected.items():
        if metadata.get(key) != value:
            error(errors, f"Metadata {key!r} är {metadata.get(key)!r}, väntat {value!r}")

    cover_rel = metadata.get("cover-image", "")
    cover_path = (root / "publishing" / cover_rel).resolve()
    try:
        cover_path.relative_to(root.resolve())
    except ValueError:
        error(errors, f"Omslagsbilden ligger utanför projektroten: {metadata.get('cover-image')}")
    else:
        if not cover_path.exists():
            error(errors, f"Omslagsbilden finns inte: {metadata.get('cover-image')}")

    chapter_dir = root / "kapitel"
    chapters: dict[int, Path] = {}
    for path in sorted(chapter_dir.iterdir()):
        if not path.is_file():
            continue
        match = CHAPTER_RE.fullmatch(path.name)
        if match:
            number = int(match.group(1))
            chapters[number] = path
        elif path.name.lower() != "kapitelmall.md" and re.search(r"kapitel.*\d", path.name, re.I):
            error(errors, f"Icke-kanonisk möjlig kapitelfil hittad: kapitel/{path.name}")

    if not chapters:
        error(errors, "Inga kanoniska kapitelfiler hittades.")
    else:
        numbers = sorted(chapters)
        expected_numbers = list(range(1, numbers[-1] + 1))
        if numbers != expected_numbers:
            error(errors, f"Kapitelserien har luckor: {numbers}, väntat {expected_numbers}")

    for number, path in sorted(chapters.items()):
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            error(errors, f"{path.relative_to(root)} är tom.")
            continue
        first = next((line for line in text.splitlines() if line.strip()), "")
        match = CHAPTER_H1_RE.match(first)
        if not match:
            error(errors, f"{path.relative_to(root)} saknar H1-format '# Kapitel {number} – Titel'.")
        else:
            h1_number = int(match.group(1))
            if h1_number != number:
                error(errors, f"{path.relative_to(root)} har H1 för kapitel {h1_number}, väntat {number}.")
            if not match.group(2).strip():
                error(errors, f"{path.relative_to(root)} saknar kapitelrubrik.")
        for marker in MARKERS:
            if marker in text:
                error(errors, f"{path.relative_to(root)} innehåller arbets-/kapitelnoteringsmarkör: {marker}")
        if re.search(r"(?m)^#{2,}\s+(Kort\s+)?Kapitelnotering\b", text):
            error(errors, f"{path.relative_to(root)} innehåller kapitelnotering som inte ska exporteras.")

    validate_markdown_links(root, errors)

    if errors:
        print(f"Validering misslyckades med {len(errors)} fel.", file=sys.stderr)
        return 1

    print(f"OK: projektet validerat. {len(chapters)} kapitel, metadata och omslag är konsekventa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
