from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "course/13-metrics-and-indicators/13c-model-routing-and-orchestration.ipynb"
BASE = "https://github.com/pedroregato/text-intelligence-lab/blob/main/docs/glossary/glossary.pt-BR.md"

LINKS = {
    "Model Routing": f"{BASE}#roteamento-de-modelos",
    "Model Orchestration": f"{BASE}#orquestração-de-modelos",
    "Quality Gate": f"{BASE}#quality-gate",
    "Escalation Rate": f"{BASE}#taxa-de-escalonamento",
    "Utility Function": f"{BASE}#função-de-utilidade",
    "Compound AI System": f"{BASE}#sistema-composto-de-ia",
    "Cost per Inference": f"{BASE}#custo-por-inferência",
    "Trade-off": f"{BASE}#trade-off",
}


def md_link(label: str) -> str:
    return f"[{label}]({LINKS[label]})"


def set_markdown(nb: dict, cell_id: str, text: str) -> None:
    for cell in nb["cells"]:
        if cell.get("id") == cell_id:
            if cell.get("cell_type") != "markdown":
                raise RuntimeError(f"Cell {cell_id} is not markdown")
            cell["source"] = text.splitlines(keepends=True)
            return
    raise RuntimeError(f"Cell {cell_id} not found")


def main() -> None:
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))

    set_markdown(
        nb,
        "c02",
        f"""## 📘 Glossário Vivo — conceitos-chave da Aula 13C

Use o Glossário Vivo durante o laboratório. Os conceitos abaixo formam a linguagem necessária para interpretar as decisões do simulador:

**{md_link('Model Routing')} · {md_link('Model Orchestration')} · {md_link('Quality Gate')} · {md_link('Escalation Rate')} · {md_link('Utility Function')} · {md_link('Compound AI System')} · {md_link('Cost per Inference')} · {md_link('Trade-off')}**

### 🧭 Durante o laboratório...

| Quando você estiver pensando em... | Consulte |
|---|---|
| escolher modelos diferentes conforme a tarefa | {md_link('Model Routing')} |
| combinar modelos ou etapas | {md_link('Model Orchestration')} |
| decidir quando aceitar ou escalar uma resposta | {md_link('Quality Gate')} |
| entender quantos casos chegam à camada premium | {md_link('Escalation Rate')} |
| equilibrar qualidade, custo e latência | {md_link('Utility Function')} |
| analisar vários componentes trabalhando juntos | {md_link('Compound AI System')} |
| estimar o impacto econômico das chamadas | {md_link('Cost per Inference')} |
| aceitar ganhos em uma dimensão e perdas em outra | {md_link('Trade-off')} |

> Não memorize os termos isoladamente. Use os links quando o comportamento do simulador levantar uma dúvida conceitual.
""",
    )

    set_markdown(
        nb,
        "c05",
        f"""## 2. Sistema composto

As linhas carregadas são candidatos `single`. O `cascade` usa a camada de menor custo como inicial e a de maior qualidade como premium. O **quality gate** controla uma **taxa de escalonamento simulada**.

Mesmo em modo EVIDENCE, o ponto intermediário do cascade é uma hipótese de engenharia até ser medido diretamente.

📚 Glossário: {md_link('Quality Gate')} · {md_link('Escalation Rate')} · {md_link('Model Routing')} · {md_link('Trade-off')}.
""",
    )

    set_markdown(
        nb,
        "c07",
        f"""## 3. 🎛️ Simulador

Os sliders mudam **prioridades**, não as medições. Ajuste qualidade, custo, latência e gate; observe ranking, escalonamento e o mapa custo × qualidade.

📚 Glossário: {md_link('Utility Function')} · {md_link('Cost per Inference')} · {md_link('Compound AI System')}.
""",
    )

    NOTEBOOK.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("Aula 13C: Glossário Vivo com links ativos aplicado.")


if __name__ == "__main__":
    main()
