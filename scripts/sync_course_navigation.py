"""Synchronize TIL lesson navigation footers from course/navigation.json.

Usage:
    python scripts/sync_course_navigation.py

The script is idempotent: it updates the existing navigation cell when present,
otherwise it appends one. It does not execute notebooks.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "course" / "navigation.json"
NAV_MARKER = "til-course-navigation"


def nav_markdown(previous, current, next_item, course_home, roadmap_url, next_planned):
    prev_label = previous["title"] if previous else course_home["title"]
    prev_url = previous["url"] if previous else course_home["url"]

    if next_item:
        next_label = next_item["title"]
        next_url = next_item["url"]
    else:
        next_label = next_planned["label"] + " — em preparação"
        next_url = roadmap_url

    return (
        "\n---\n\n"
        "## Continue no TIL\n\n"
        f"← **[Anterior: {prev_label}]({prev_url})**"
        " &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"🏠 **[Apresentação do curso]({course_home['url']})**"
        " &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"**[Próxima: {next_label}]({next_url})** →\n"
    )


def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lessons = data["lessons"]

    for index, lesson in enumerate(lessons):
        path = ROOT / lesson["path"]
        notebook = json.loads(path.read_text(encoding="utf-8"))

        previous = lessons[index - 1] if index > 0 else None
        next_item = lessons[index + 1] if index + 1 < len(lessons) else None

        source = nav_markdown(
            previous,
            lesson,
            next_item,
            data["course_home"],
            data["roadmap_url"],
            data["next_planned"],
        )

        nav_cell = {
            "cell_type": "markdown",
            "id": f"nav-{lesson['id'].lower()}",
            "metadata": {"til_navigation": True, "marker": NAV_MARKER},
            "source": source.splitlines(keepends=True),
        }

        existing = next(
            (
                i for i, cell in enumerate(notebook["cells"])
                if cell.get("metadata", {}).get("marker") == NAV_MARKER
                or cell.get("metadata", {}).get("til_navigation") is True
            ),
            None,
        )

        if existing is None:
            notebook["cells"].append(nav_cell)
        else:
            notebook["cells"][existing] = nav_cell

        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        print(f"updated: {lesson['path']}")


if __name__ == "__main__":
    main()
