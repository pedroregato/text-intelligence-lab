"""Build the dedicated Kaggle wrapper for TIL Lesson 13C.

The canonical lesson remains under course/13-metrics-and-indicators.
This builder copies that notebook and injects the measured EDU-ORCH
evidence CSVs so the Kaggle kernel runs in EVIDENCE mode with Internet OFF.
"""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK = ROOT / "course" / "13-metrics-and-indicators" / "13c-model-routing-and-orchestration.ipynb"
MODEL_EVIDENCE = ROOT / "data" / "model-evidence" / "til-model-evidence.csv"
ROUTING_EVIDENCE = ROOT / "data" / "model-evidence" / "til-routing-evidence.csv"
WRAPPER_DIR = ROOT / "kaggle" / "til-13c"
WRAPPER_NOTEBOOK = WRAPPER_DIR / "13c-model-routing-and-orchestration.ipynb"


def injection_cell(model_csv: str, routing_csv: str) -> dict:
    source = f'''# AUTO-GENERATED KAGGLE WRAPPER INPUTS — do not edit here.
from pathlib import Path

evidence_dir = Path("data/model-evidence")
evidence_dir.mkdir(parents=True, exist_ok=True)

(evidence_dir / "til-model-evidence.csv").write_text({model_csv!r}, encoding="utf-8")
(evidence_dir / "til-routing-evidence.csv").write_text({routing_csv!r}, encoding="utf-8")

print("Evidências EDU-ORCH materializadas para a Aula 13C.")
print("Model evidence:", evidence_dir / "til-model-evidence.csv")
print("Routing evidence:", evidence_dir / "til-routing-evidence.csv")
'''
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": "til13c-kaggle-evidence",
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def main() -> None:
    notebook = json.loads(SOURCE_NOTEBOOK.read_text(encoding="utf-8"))
    notebook["cells"] = [
        cell for cell in notebook["cells"]
        if cell.get("id") != "til13c-kaggle-evidence"
    ]

    first_code = next(
        (i for i, cell in enumerate(notebook["cells"]) if cell.get("cell_type") == "code"),
        0,
    )
    notebook["cells"].insert(
        first_code,
        injection_cell(
            MODEL_EVIDENCE.read_text(encoding="utf-8"),
            ROUTING_EVIDENCE.read_text(encoding="utf-8"),
        ),
    )

    WRAPPER_DIR.mkdir(parents=True, exist_ok=True)
    WRAPPER_NOTEBOOK.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(f"Generated: {WRAPPER_NOTEBOOK}")


if __name__ == "__main__":
    main()
