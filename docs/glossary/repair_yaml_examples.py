"""Repair legacy glossary YAML example scalars.

Why this exists
---------------
Some historical ``example:`` values were written as YAML plain scalars even
though they contain characters that YAML interprets structurally, for example:

    example: "atendimento excelente" se torna ["atendimento", "excelente"].
    example: [0.18, -0.42, 0.77, 0.11].

Those values are meant to be *text examples*, not YAML strings mixed with flow
collections. This helper normalizes every one-line ``example:`` value to a
single-quoted YAML string. Existing valid single-quoted examples are preserved.

Usage:
    python docs/glossary/repair_yaml_examples.py

The script is idempotent: a second run should report no changes.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "glossary.yaml"

EXAMPLE_RE = re.compile(r"^(\s+example:\s+)(.*?)(\r?\n)?$")


def is_valid_single_quoted_scalar(value: str) -> bool:
    """Return True when value is already one complete YAML single-quoted scalar."""
    if not (value.startswith("'") and value.endswith("'")):
        return False

    # Inside a YAML single-quoted scalar, a literal apostrophe is represented
    # by two consecutive single quotes. Validate that convention so malformed
    # legacy values are still repaired.
    inner = value[1:-1]
    i = 0
    while i < len(inner):
        if inner[i] == "'":
            if i + 1 >= len(inner) or inner[i + 1] != "'":
                return False
            i += 2
        else:
            i += 1
    return True


def quote_as_yaml_string(value: str) -> str:
    """Wrap arbitrary one-line text as a safe YAML single-quoted scalar."""
    return "'" + value.replace("'", "''") + "'"


def repair_line(line: str) -> tuple[str, bool]:
    match = EXAMPLE_RE.match(line)
    if not match:
        return line, False

    prefix, value, newline = match.groups()
    newline = newline or ""
    value = value.rstrip()

    # Empty values and block scalars are not one-line examples and are left as-is.
    if not value or value in {"|", ">", "|-", ">-", "|+", ">+"}:
        return line, False

    if is_valid_single_quoted_scalar(value):
        return line, False

    return f"{prefix}{quote_as_yaml_string(value)}{newline}", True


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
