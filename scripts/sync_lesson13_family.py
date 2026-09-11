from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LESSON_13 = ROOT / "course/13-metrics-and-indicators/13-til-metrics-and-indicators.ipynb"
LESSON_13B = ROOT / "course/13-metrics-and-indicators/metric-scenario-lab/13b-til-metric-scenario-lab.ipynb"
LESSON_13C = ROOT / "course/13-metrics-and-indicators/13c-model-routing-and-orchestration.ipynb"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, nb: dict) -> None:
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def markdown_cell(cell_id: str, text: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {},
        "source": text.splitlines(keepends=True),
    }


def upsert_after(nb: dict, after_id: str, cell: dict) -> None:
    cells = nb["cells"]
    for i, current in enumerate(cells):
        if current.get("id") == cell["id"]:
            cells[i] = cell
            return
    for i, current in enumerate(cells):
        if current.get("id") == after_id:
            cells.insert(i + 1, cell)
            return
    cells.append(cell)


def upsert_last(nb: dict, cell: dict) -> None:
    for i, current in enumerate(nb["cells"]):
        if current.get("id") == cell["id"]:
            nb["cells"][i] = cell
            return
    nb["cells"].append(cell)


def sync_13() -> None:
    nb = load(LESSON_13)
    upsert_last(
        nb,
        markdown_cell(
            "til13-next-labs",
            """## Próximos laboratórios da Aula 13\n\n"
            "A interpretação das métricas continua em dois laboratórios complementares:\n\n"
            "- **Aula 13B — Metric Scenario Lab:** thresholds, cenários e custos de erro;\n"
            "- **Aula 13C — Model Routing, Orchestration e Utility:** quality gates, custo, latência e sistemas compostos de IA.\n\n"
            "```text\n"
            "métrica → custo do erro → threshold → cenário → routing → orchestration\n"
            "```\n\n"
            "A 13C também introduz a distinção entre **DEMO** e **EVIDENCE**: proxies didáticos são úteis para aprender, mas decisões arquiteturais reais exigem medições versionadas e comparáveis.\n"
            """,
        ),
    )
    save(LESSON_13, nb)
    print(f"OK: {LESSON_13.relative_to(ROOT)}")


def sync_13b() -> None:
    nb = load(LESSON_13B)
    upsert_last(
        nb,
        markdown_cell(
            "til13b-next-13c",
            """## Próximo passo — da métrica ao sistema\n\n"
            "Depois de explorar thresholds e custos de erro, avance para a **Aula 13C — Model Routing, Orchestration e Utility**.\n\n"
            "A pergunta muda de:\n\n"
            "> Qual threshold produz a melhor combinação de métricas?\n\n"
            "para:\n\n"
            "> Qual arquitetura entrega qualidade suficiente com custo, latência e risco aceitáveis?\n\n"
            "Na 13C, a interatividade segue o padrão **headless-first**: `Run All` deve terminar sem intervenção humana e os controles interativos são uma camada opcional de exploração.\n"
            """,
        ),
    )
    save(LESSON_13B, nb)
    print(f"OK: {LESSON_13B.relative_to(ROOT)}")


def clean_c08() -> list[str]:
    text = '''sty={"description_width":"140px"}\nlay=widgets.Layout(width="95%")\n\nq=widgets.IntSlider(\n    value=60,\n    min=0,\n    max=100,\n    step=5,\n    description="Qualidade",\n    style=sty,\n    layout=lay,\n    continuous_update=False\n)\n\nc=widgets.IntSlider(\n    value=25,\n    min=0,\n    max=100,\n    step=5,\n    description="Custo",\n    style=sty,\n    layout=lay,\n    continuous_update=False\n)\n\nl=widgets.IntSlider(\n    value=15,\n    min=0,\n    max=100,\n    step=5,\n    description="Latência",\n    style=sty,\n    layout=lay,\n    continuous_update=False\n)\n\ng=widgets.FloatSlider(\n    value=.45,\n    min=0,\n    max=1,\n    step=.05,\n    description="Quality gate",\n    style=sty,\n    layout=lay,\n    continuous_update=False\n)\n\npreset=widgets.ToggleButtons(\n    options=[\n        ("Equilibrado","b"),\n        ("Qualidade","q"),\n        ("Custo","c"),\n        ("Latência","l")\n    ],\n    value="b"\n)\n\nrun_button=widgets.Button(\n    description="Simular cenário",\n    button_style="primary",\n    icon="play"\n)\n\nout=widgets.Output()\n\n\ndef render(_=None):\n\n    d,x,w=evaluate(\n        q.value,\n        c.value,\n        l.value,\n        g.value\n    )\n\n    with out:\n\n        clear_output(wait=True)\n\n        win=d.iloc[0]\n\n        note=(\n            "evidência versionada"\n            if MODE=="EVIDENCE"\n            else "proxies sintéticos"\n        )\n\n        display(\n            Markdown(\n                f"**Vencedor do cenário:** `{win.system}` "\n                f"· dados: **{note}**  \\n"\n                f"**Cascade:** `{x['cheap']}` → "\n                f"`{x['premium']}` "\n                f"· escalonamento "\n                f"**{x['escalation_rate']:.0%}**"\n            )\n        )\n\n        z=d[\n            [\n                "system",\n                "architecture",\n                "quality",\n                "cost_per_1000",\n                "latency_ms",\n                "escalation_rate",\n                "utility"\n            ]\n        ].copy()\n\n        z.insert(\n            0,\n            "rank",\n            range(1,len(z)+1)\n        )\n\n        display(z.round(4))\n\n        fig,ax=plt.subplots(figsize=(8,5))\n\n        for _,r in d.iterrows():\n\n            ax.scatter(\n                r.cost_per_1000,\n                r.quality,\n                s=90\n            )\n\n            ax.annotate(\n                r.system,\n                (\n                    r.cost_per_1000,\n                    r.quality\n                ),\n                xytext=(5,5),\n                textcoords="offset points"\n            )\n\n        ax.set(\n            xlabel="Custo / 1.000 inferências",\n            ylabel="Qualidade",\n            title=f"Custo × qualidade — {MODE}"\n        )\n\n        ax.grid(alpha=.25)\n\n        plt.show()\n        plt.close(fig)\n\n        fig,ax=plt.subplots(figsize=(8,4))\n\n        ax.bar(\n            d.system,\n            d.utility\n        )\n\n        ax.axhline(\n            0,\n            lw=1\n        )\n\n        ax.set_ylabel("Utility")\n\n        plt.xticks(\n            rotation=25,\n            ha="right"\n        )\n\n        plt.show()\n        plt.close(fig)\n\n\ndef choose(ch):\n\n    if ch.get("name")!="value":\n        return\n\n    vals={\n        "b":(60,25,15),\n        "q":(85,10,5),\n        "c":(40,50,10),\n        "l":(40,10,50)\n    }\n\n    q.value,c.value,l.value=vals[ch["new"]]\n\n\npreset.observe(\n    choose,\n    names="value"\n)\n\nrun_button.on_click(render)\n\n\ndisplay(\n    widgets.VBox(\n        [\n            widgets.HTML(\n                f"<b>Dados:</b> {MODE}<br>"\n                "Ajuste os parâmetros e clique "\n                "em <b>Simular cenário</b>."\n            ),\n            preset,\n            q,\n            c,\n            l,\n            g,\n            run_button,\n            out\n        ]\n    )\n)\n'''
    return text.splitlines(keepends=True)


def sync_13c() -> None:
    nb = load(LESSON_13C)
    by_id = {cell.get("id"): cell for cell in nb["cells"]}
    if "c08" not in by_id:
        raise RuntimeError("Cell c08 not found in Aula 13C")

    by_id["c08"]["source"] = clean_c08()

    upsert_after(
        nb,
        "c03",
        markdown_cell(
            "c03b-headless-status",
            """### Estado de execução e evidência\n\n"
            "Este notebook segue o padrão **headless-first** do TIL: a execução completa (`Run All`) não depende de interação humana. Os widgets são uma camada opcional e o cenário interativo só é calculado quando o aluno clica em **Simular cenário**.\n\n"
            "O notebook foi validado em execução local headless e no Kaggle.\n\n"
            "O próximo marco experimental é substituir os proxies `DEMO` por medições comparáveis do experimento `EDU-ORCH-001`, começando por **TF-IDF + classificador clássico** versus **DistilBERT multilíngue**.\n"
            """,
        ),
    )

    upsert_last(
        nb,
        markdown_cell(
            "c13-next-evidence",
            """## 7. Próximo experimento — ativar EVIDENCE com dados reais\n\n"
            "A aula está pronta para consumir evidência real, mas não devemos preencher `til-model-evidence.csv` apenas para tornar o simulador mais convincente.\n\n"
            "O experimento `docs/experiments/EDU-ORCH-001-model-evidence-baseline-vs-transformer.md` define o próximo passo:\n\n"
            "```text\n"
            "mesmo dataset/split\n"
            "→ TF-IDF + classificador clássico\n"
            "→ DistilBERT multilíngue\n"
            "→ qualidade + latência + custo\n"
            "→ proveniência\n"
            "→ til-model-evidence.csv\n"
            "→ modo EVIDENCE\n"
            "```\n\n"
            "Até que essas medições existam, **DEMO continua sendo a representação correta e honesta**.\n"
            """,
        ),
    )

    save(LESSON_13C, nb)
    print(f"OK: {LESSON_13C.relative_to(ROOT)}")


def main() -> None:
    sync_13()
    sync_13b()
    sync_13c()
    print("Lesson 13 family synchronized.")


if __name__ == "__main__":
    main()
