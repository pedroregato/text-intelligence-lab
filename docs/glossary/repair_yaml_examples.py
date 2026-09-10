"""Repair malformed glossary YAML example scalars.

This is a one-time maintenance helper for legacy entries such as:

    example: "atendimento excelente" se torna ["atendimento", "excelente"].

The value starts with a double quote but contains additional unescaped quoted
fragments, which makes the YAML invalid. The script wraps the whole scalar in
single quotes while preserving the inner double quotes.

Usage:
    python docs/glossary/repair_yaml_examples.py

The script is idempotent: running it again after the repair should make no
changes.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "glossary.yaml"

EXAMPLE_RE = re.compile(r"^(\s+example:\s+)(.*)$")


def is_single_double_quoted_scalar(value: str) -> bool:
    """Return True only when value is one complete YAML double-quoted scalar."""
    if not (value.startswith('"') and value.endswith('"')):
        return False

    escaped = False
    for index, char in enumerate(value[1:-1], start=1):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            # An unescaped quote before the final quote means the scalar closed
            # early and more text follows: exactly the legacy problem we fix.
            return False
    return True


def repair_line(line: str) -> tuple[str, bool]:
    match = EXAMPLE_RE.match(line)
    if not match:
        return line, False

    prefix, value = match.groups()
    value = value.rstrip()

    # Plain scalars and already-valid quoted scalars are left untouched.
    if not value.startswith('"') or is_single_double_quoted_scalar(value):
        return line, False

    # Single quotes are escaped in YAML by doubling them.
    safe_value = value.replace("'", "''")
    newline = "\n" if line.endswith("\n") else ""
    return f"{prefix}'{safe_value}'{newline}", True


def main() -> None:
    original_lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)
    repaired_lines = []
    changed = []

    for number, line in enumerate(original_lines, start=1):
        repaired, was_changed = repair_line(line)
        repaired_lines.append(repaired)
        if was_changed:
            changed.append(number)

    if not changed:
        print("Nenhuma correção necessária em glossary.yaml.")
        return

    SOURCE.write_text("".join(repaired_lines), encoding="utf-8")
    print(f"Corrigidas {len(changed)} linha(s): {changed}")
    print("Agora execute: python docs/glossary/build_glossary.py")


if __name__ == "__main__":
    main()
