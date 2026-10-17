#!/usr/bin/env python3
"""Validate the constrained TIL-EP-001 principles index without third-party YAML packages.

This is a *lexical/contract* check for the current catalog layout; it is not a
general-purpose YAML parser or a substitute for editorial review.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs" / "principles"
YAML = BASE / "principles-catalog.yaml"
MARKDOWN = BASE / "engineering-principles.md"
SPEC = ROOT / "docs" / "proposals" / "TIL-EP-001-engineering-principles.md"
IDS = [f"TIL-PRINCIPLE-{i:03d}" for i in range(1, 9)]


def extract_sections(text: str, pattern: str) -> dict[str, str]:
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    found: dict[str, str] = {}
    for i, match in enumerate(matches):
        key = match.group(1)
        if key in found:
            raise ValueError(f"duplicate principle {key}")
        found[key] = text[match.end(): matches[i + 1].start() if i + 1 < len(matches) else len(text)]
    return found


def validate() -> None:
    source = SPEC.read_text(encoding="utf-8")
    md = MARKDOWN.read_text(encoding="utf-8")
    yaml = YAML.read_text(encoding="utf-8")

    spec_parts = extract_sections(source, r"^### (TIL-PRINCIPLE-\d{3}) — ")
    md_parts = extract_sections(md, r"^## (TIL-PRINCIPLE-\d{3}) — ")
    yaml_parts = extract_sections(yaml, r"^  - id: (TIL-PRINCIPLE-\d{3})$")

    for name, parts in (("spec", spec_parts), ("markdown", md_parts), ("yaml", yaml_parts)):
        if list(parts) != IDS:
            raise ValueError(f"{name}: expected ordered IDs {IDS}, got {list(parts)}")

    if not re.search(r"^catalog_status: Proposed$", yaml, re.MULTILINE):
        raise ValueError("catalog must remain Proposed until human review")

    for ident in IDS:
        lema_source = re.search(r"^> \*\*(.*?)\*\*$", spec_parts[ident], re.MULTILINE)
        lema_md = re.search(r"^> (.+)$", md_parts[ident], re.MULTILINE)
        lema_yaml = re.search(r"^    lemma: (.+)$", yaml_parts[ident], re.MULTILINE)
        if not all((lema_source, lema_md, lema_yaml)):
            raise ValueError(f"{ident}: missing lemma")
        literal = json.loads(lema_yaml.group(1))  # YAML strings use JSON-compatible double quotes
        if not (lema_source.group(1) == lema_md.group(1) == literal):
            raise ValueError(f"{ident}: original lemma was modified")
        if not re.search(r"^    status: Proposed$", yaml_parts[ident], re.MULTILINE):
            raise ValueError(f"{ident}: status must be Proposed")
        for key in ("title", "verification", "limitation", "origin", "pilot_evidence"):
            matched = re.search(rf"^    {key}: (.+)$", yaml_parts[ident], re.MULTILINE)
            if not matched:
                raise ValueError(f"{ident}: missing {key}")
            if key in ("origin", "pilot_evidence"):
                relative_path = matched.group(1).strip().strip('"')
                if not (ROOT / relative_path).is_file():
                    raise ValueError(f"{ident}: missing linked file {relative_path}")
        for heading in ("Critério verificável", "Teste de aplicação (auditável)",
                        "Exemplo", "Contraexemplo ou condição de contorno", "Limitação"):
            if not re.search(rf"^\*\*{re.escape(heading)}:\*\*", md_parts[ident], re.MULTILINE):
                raise ValueError(f"{ident}: missing {heading}")

    print(f"PASS: {len(IDS)} principles, literal lemmas, statuses, fields and evidence paths")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
