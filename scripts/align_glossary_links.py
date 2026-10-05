"""Audit and normalize direct TIL Living Glossary links in course notebooks.

The script is intentionally conservative:
- it only edits markdown regions explicitly identified as glossary content;
- it links only terms that resolve to the canonical glossary or an explicit alias;
- unresolved terms are reported and left untouched;
- it never performs global prose replacement.

Usage
-----
Audit only:
    python scripts/align_glossary_links.py --check

Apply safe fixes:
    python scripts/align_glossary_links.py --apply

Limit to selected lessons/notebooks:
    python scripts/align_glossary_links.py --check --match "11-bert|13c"

After an Aula 13C change, --apply regenerates its dedicated Kaggle wrapper
through scripts/build_kaggle_13c_wrapper.py when that builder is available.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
GLOSSARY_DIR = ROOT / "docs" / "glossary"
GLOSSARY_MAIN = GLOSSARY_DIR / "glossary.yaml"
GLOSSARY_EXT = GLOSSARY_DIR / "glossary.extensions.yaml"
GLOSSARY_URL = (
    "https://github.com/pedroregato/text-intelligence-lab/blob/main/"
    "docs/glossary/glossary.pt-BR.md"
)

MANUAL_ALIASES = {
    "texto bruto": "raw-text",
    "treino/teste": "train-test-split",
    "gridsearchcv": "grid-search",
    "grid search": "grid-search",
    "tfidfvectorizer": "tfidf",
    "tf-idf": "tfidf",
    "llm": "large-language-model",
    "modelo autoregressivo": "autoregressive-model",
    "classification head": "classification-head",
    "cabeça da classificação": "classification-head",
    "cabeça de classificação": "classification-head",
    "pré-treinamento": "pretrained-model",
    "modelo pré-treinado": "pretrained-model",
    "sequence classification": "sequence-classification",
    "multinomialnb": "multinomial-naive-bayes",
    "naive bayes multinomial": "multinomial-naive-bayes",
    "word embedding": "embedding",
    "vetor denso": "dense-vector",
    "cosine similarity": "cosine-similarity",
    "top k": "top-k",
    "top-k": "top-k",
    "top p": "top-p",
    "top-p": "top-p",
    "eos": "eos-token",
    "structured output": "structured-output",
    "quality gate": "quality-gate",
    "escalation rate": "escalation-rate",
    "utility function": "utility-function",
    "model routing": "model-routing",
    "model orchestration": "model-orchestration",
    "compound ai system": "compound-ai-system",
    "cost per inference": "cost-per-inference",
}

EDITORIAL_LABELS = {
    "glossário",
    "glossário:",
    "glossário vivo",
    "palavras-chave",
    "palavras-chave:",
    "leitura pelo glossário",
    "leitura pelo glossário:",
    "glossário em contexto",
    "glossário em contexto:",
    "mindset til",
    "mindset semântico til",
    "mindset semântico til:",
    "conceitos centrais no glossário vivo",
    "conceitos do glossário",
}


@dataclass(frozen=True)
class GlossaryTerm:
    id: str
    pt: str
    en: str
    anchor: str

    @property
    def url(self) -> str:
        return f"{GLOSSARY_URL}#{self.anchor}"


def normalize(text: str) -> str:
    text = text.strip().casefold()
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[\s_]+", " ", text)
    text = text.replace("–", "-").replace("—", "-")
    return text.strip(" .,:;()[]{}")


def github_anchor(text: str) -> str:
    text = text.strip().casefold()
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"[^\w\-\sÀ-ÿ]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_terms() -> tuple[dict[str, GlossaryTerm], dict[str, GlossaryTerm]]:
    records = []
    for path in (GLOSSARY_MAIN, GLOSSARY_EXT):
        records.extend(load_yaml(path).get("terms", []))

    by_id: dict[str, GlossaryTerm] = {}
    aliases: dict[str, GlossaryTerm] = {}

    for item in records:
        pt = item["pt-BR"]["term"]
        en = item["en"]["term"]
        term = GlossaryTerm(
            id=item["id"],
            pt=pt,
            en=en,
            anchor=github_anchor(pt),
        )
        by_id[term.id] = term

        candidates = {
            term.id,
            pt,
            en,
            item["pt-BR"].get("english_term", ""),
        }
        for candidate in candidates:
            if candidate:
                aliases[normalize(candidate)] = term

    for alias, term_id in MANUAL_ALIASES.items():
        if term_id in by_id:
            aliases[normalize(alias)] = by_id[term_id]

    return by_id, aliases


def resolve(label: str, aliases: dict[str, GlossaryTerm]) -> GlossaryTerm | None:
    clean = re.sub(r"[*_`]", "", label).strip()
    return aliases.get(normalize(clean))


def is_editorial_label(label: str) -> bool:
    return normalize(label) in {normalize(x) for x in EDITORIAL_LABELS}


def direct_link(label: str, term: GlossaryTerm) -> str:
    return f"[{label.strip()}]({term.url})"


def link_bold_segment(
    segment: str,
    aliases: dict[str, GlossaryTerm],
    unresolved: set[str],
) -> tuple[str, int]:
    parts = re.split(r"(\s+[·•]\s+)", segment)
    changed = 0
    out: list[str] = []

    for part in parts:
        if re.fullmatch(r"\s+[·•]\s+", part):
            out.append(part)
            continue

        raw = part
        label = raw.strip()
        if not label:
            out.append(raw)
            continue

        if is_editorial_label(label):
            out.append(raw)
            continue

        term = resolve(label, aliases)
        if term:
            prefix = raw[: len(raw) - len(raw.lstrip())]
            suffix = raw[len(raw.rstrip()) :]
            out.append(prefix + direct_link(label, term) + suffix)
            changed += 1
        else:
            unresolved.add(label)
            out.append(raw)

    return "".join(out), changed


BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def link_glossary_line(
    line: str,
    aliases: dict[str, GlossaryTerm],
    unresolved: set[str],
) -> tuple[str, int]:
    if "](" in line and line.count("**") == 0:
        return line, 0

    total = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal total
        inner = match.group(1)

        if "](" in inner:
            return match.group(0)

        linked, count = link_bold_segment(inner, aliases, unresolved)
        total += count
        return f"**{linked}**"

    return BOLD_RE.sub(repl, line), total


def is_concept_inventory_line(line: str) -> bool:
    return bool(
        re.search(
            r"(conceitos?\s+(?:centrais|chave)|palavras-chave)\s*:",
            line,
            flags=re.IGNORECASE,
        )
    )


def is_glossary_callout(line: str) -> bool:
    return bool(
        re.search(
            r"(?:📚\s*)?Gloss[aá]rio(?:\s+em\s+contexto)?\s*:",
            line,
            flags=re.IGNORECASE,
        )
    )


def is_glossary_table_row(line: str) -> bool:
    # Typical Aula 11 map row: | **pré-treinamento** | ... |
    return line.lstrip().startswith("|") and "**" in line


def heading_level(line: str) -> int | None:
    m = re.match(r"^\s*(#{1,6})\s+", line)
    return len(m.group(1)) if m else None


def transform_markdown(
    text: str,
    aliases: dict[str, GlossaryTerm],
) -> tuple[str, int, set[str]]:
    lines = text.splitlines(keepends=True)
    unresolved: set[str] = set()
    linked = 0

    in_glossary = False
    glossary_level: int | None = None
    output: list[str] = []

    for line in lines:
        stripped = line.rstrip("\r\n")
        level = heading_level(stripped)

        if re.search(r"Gloss[aá]rio", stripped, flags=re.IGNORECASE) and level:
            in_glossary = True
            glossary_level = level
            output.append(line)
            continue

        if (
            in_glossary
            and level is not None
            and glossary_level is not None
            and level <= glossary_level
        ):
            in_glossary = False
            glossary_level = None

        should_process = (
            is_glossary_callout(stripped)
            or (in_glossary and is_concept_inventory_line(stripped))
            or (in_glossary and is_glossary_table_row(stripped))
        )

        if should_process:
            converted, count = link_glossary_line(
                stripped,
                aliases,
                unresolved,
            )
            linked += count
            newline = line[len(stripped) :]
            output.append(converted + newline)
        else:
            output.append(line)

    return "".join(output), linked, unresolved


def iter_notebooks(match: str | None) -> Iterable[Path]:
    for path in sorted(COURSE.rglob("*.ipynb")):
        if "course-home" in path.parts:
            continue

        relative = path.relative_to(ROOT).as_posix()
        if match and not re.search(match, relative, flags=re.IGNORECASE):
            continue

        yield path


def process_notebook(
    path: Path,
    aliases: dict[str, GlossaryTerm],
    apply: bool,
) -> tuple[int, set[str], bool]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    linked = 0
    unresolved: set[str] = set()
    changed = False

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue

        source = "".join(cell.get("source", []))
        if "gloss" not in source.casefold() and "📚" not in source:
            continue

        transformed, count, missing = transform_markdown(source, aliases)
        linked += count
        unresolved.update(missing)

        if transformed != source:
            changed = True
            cell["source"] = transformed.splitlines(keepends=True)

    if changed and apply:
        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )

    return linked, unresolved, changed


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="audit only")
    mode.add_argument("--apply", action="store_true", help="write safe fixes")
    parser.add_argument(
        "--match",
        help="regex used to limit notebook paths, e.g. '11-bert|13c'",
    )
    args = parser.parse_args()

    _, aliases = load_terms()

    total_links = 0
    changed_paths: list[Path] = []
    unresolved_global: dict[str, set[str]] = {}

    print("TIL Glossary Link Alignment")
    print("=" * 30)

    for path in iter_notebooks(args.match):
        links, unresolved, changed = process_notebook(
            path,
            aliases,
            apply=args.apply,
        )

        if links or unresolved or changed:
            rel = path.relative_to(ROOT).as_posix()
            status = "CHANGED" if changed else "OK"
            print(f"{status:7} | {links:3d} link(s) | {rel}")
            total_links += links

            if changed:
                changed_paths.append(path)

            if unresolved:
                unresolved_global[rel] = unresolved
                for label in sorted(unresolved, key=str.casefold):
                    print(f"          unresolved: {label}")

    print()
    print(f"Resolvable links found: {total_links}")
    print(f"Notebook(s) needing change: {len(changed_paths)}")
    print(
        "Notebook(s) with unresolved glossary labels: "
        f"{len(unresolved_global)}"
    )

    if args.check and changed_paths:
        print("\nRun with --apply to write the safe fixes.")

    if args.apply and any(
        p.name == "13c-model-routing-and-orchestration.ipynb"
        for p in changed_paths
    ):
        builder = ROOT / "scripts" / "build_kaggle_13c_wrapper.py"
        if builder.exists():
            print("\nRefreshing dedicated Aula 13C Kaggle wrapper...")
            subprocess.run(
                [sys.executable, str(builder)],
                cwd=ROOT,
                check=True,
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
