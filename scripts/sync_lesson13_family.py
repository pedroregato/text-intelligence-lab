from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LESSON_13 = ROOT / "course/13-metrics-and-indicators/13-til-metrics-and-indicators.ipynb"
LESSON_13B = ROOT / "course/13-metrics-and-indicators/metric-scenario-lab/13b-til-metric-scenario-lab.ipynb"
LESSON_13C = ROOT / "course/13-metrics-and-indicators/13c-model-routing-and-orchestration.ipynb"

GLOSSARY_BASE = "https://github.com/pedroregato/text-intelligence-lab/blob/main/docs/glossary/glossary.pt-BR.md"
GLOSSARY_LINKS = {
    "Baseline": f"{GLOSSARY_BASE}#baseline",
    "Model Routing": f"{GLOSSARY_BASE}#roteamento-de-modelos",
    "Model Orchestration": f"{GLOSSARY_BASE}#orquestração-de-modelos",
    "Quality Gate": f"{GLOSSARY_BASE}#quality-gate",
    "Escalation Rate": f"{GLOSSARY_BASE}#taxa-de-escalonamento",
    "Utility Function": f"{GLOSSARY_BASE}#função-de-utilidade",
    "Compound AI System": f"{GLOSSARY_BASE}#sistema-composto-de-ia",
    "Cost per Inference": f"{GLOSSARY_BASE}#custo-por-inferência",
    "Trade-off": f"{GLOSSARY_BASE}#trade-off",
}


def glossary_link(label: str) -> str:
    return f"[{label}]({GLOSSARY_LINKS[label]})"


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


def code_cell(cell_id: str, text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": cell_id,
        "metadata": {},
        "outputs": [],
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


def replace_markdown(nb: dict, cell_id: str, text: str) -> None:
    for i, cell in enumerate(nb["cells"]):
        if cell.get("id") == cell_id:
            nb["cells"][i] = markdown_cell(cell_id, text)
            return
    raise RuntimeError(f"Cell {cell_id} not found")


def sync_13() -> None:
    nb = load(LESSON_13)
    text = (
        "## Próximos laboratórios da Aula 13\n\n"
        "A interpretação das métricas continua em dois laboratórios complementares:\n\n"
        "- **Aula 13B — Metric Scenario Lab:** thresholds, cenários e custos de erro;\n"
        "- **Aula 13C — Model Routing, Orchestration e Utility:** quality gates, custo, latência e sistemas compostos de IA.\n\n"
        "```text\n"
        "métrica → custo do erro → threshold → cenário → routing → orchestration\n"
        "```\n\n"
        "A 13C também introduz a distinção entre **DEMO** e **EVIDENCE**: proxies didáticos são úteis para aprender, mas decisões arquiteturais reais exigem medições versionadas e comparáveis.\n"
    )
    upsert_last(nb, markdown_cell("til13-next-labs", text))
    save(LESSON_13, nb)
    print(f"OK: {LESSON_13.relative_to(ROOT)}")


def sync_13b() -> None:
    nb = load(LESSON_13B)

    headless_note = (
        "### Evidência estática antes da interação\n\n"
        "O painel interativo é uma camada de exploração. Para manter o notebook **headless-first**, o cenário padrão abaixo também é calculado de forma determinística e deve aparecer em uma execução `Run All` sem qualquer clique.\n"
    )
    upsert_after(nb, "lab-05", markdown_cell("lab-headless-note", headless_note))

    static_code = '''cfg = SCENARIOS['Fraude bancária']
cm_default = simulate(cfg['prevalence'], cfg['separation'], cfg['threshold'])
metrics_default = metrics_from_cm(cm_default)
cost_default = expected_cost(
    cm_default,
    cfg['cost_fp'],
    cfg['cost_fn'],
    cfg['review_cost'],
    cfg['inference_cost']
)

static_summary = pd.DataFrame({
    'Indicador': list(metrics_default) + ['FP', 'FN', 'Custo esperado'],
    'Valor': list(metrics_default.values()) + [cm_default['FP'], cm_default['FN'], cost_default]
})

display(static_summary)
'''
    upsert_after(nb, "lab-headless-note", code_cell("lab-headless-default", static_code))

    text = (
        "## Próximo passo — da métrica ao sistema\n\n"
        "Depois de explorar thresholds e custos de erro, avance para a **Aula 13C — Model Routing, Orchestration e Utility**.\n\n"
        "A pergunta muda de:\n\n"
        "> Qual threshold produz a melhor combinação de métricas?\n\n"
        "para:\n\n"
        "> Qual arquitetura entrega qualidade suficiente com custo, latência e risco aceitáveis?\n\n"
        "Na 13C, a interatividade segue o padrão **headless-first**: `Run All` deve terminar sem intervenção humana e os controles interativos são uma camada opcional de exploração.\n"
    )
    upsert_last(nb, markdown_cell("til13b-next-13c", text))
    save(LESSON_13B, nb)
    print(f"OK: {LESSON_13B.relative_to(ROOT)}")


def clean_c08() -> list[str]:
    text = '''sty={"description_width":"140px"}
lay=widgets.Layout(width="95%")

q=widgets.IntSlider(value=60,min=0,max=100,step=5,description="Qualidade",style=sty,layout=lay,continuous_update=False)
c=widgets.IntSlider(value=25,min=0,max=100,step=5,description="Custo",style=sty,layout=lay,continuous_update=False)
l=widgets.IntSlider(value=15,min=0,max=100,step=5,description="Latência",style=sty,layout=lay,continuous_update=False)
g=widgets.FloatSlider(value=.45,min=0,max=1,step=.05,description="Quality gate",style=sty,layout=lay,continuous_update=False)

preset=widgets.ToggleButtons(options=[("Equilibrado","b"),("Qualidade","q"),("Custo","c"),("Latência","l")],value="b")
run_button=widgets.Button(description="Simular cenário",button_style="primary",icon="play")
out=widgets.Output()


def render(_=None):
    d,x,w=evaluate(q.value,c.value,l.value,g.value)
    with out:
        clear_output(wait=True)
        win=d.iloc[0]
        note="evidência versionada" if MODE=="EVIDENCE" else "proxies sintéticos"
        display(Markdown(
            f"**Vencedor do cenário:** `{win.system}` · dados: **{note}**  \\n"
            f"**Cascade:** `{x['cheap']}` → `{x['premium']}` · escalonamento **{x['escalation_rate']:.0%}**"
        ))
        z=d[["system","architecture","quality","cost_per_1000","latency_ms","escalation_rate","utility"]].copy()
        z.insert(0,"rank",range(1,len(z)+1))
        display(z.round(4))

        fig,ax=plt.subplots(figsize=(8,5))
        for _,r in d.iterrows():
            ax.scatter(r.cost_per_1000,r.quality,s=90)
            ax.annotate(r.system,(r.cost_per_1000,r.quality),xytext=(5,5),textcoords="offset points")
        ax.set(xlabel="Custo / 1.000 inferências",ylabel="Qualidade",title=f"Custo × qualidade — {MODE}")
        ax.grid(alpha=.25)
        plt.show()
        plt.close(fig)

        fig,ax=plt.subplots(figsize=(8,4))
        ax.bar(d.system,d.utility)
        ax.axhline(0,lw=1)
        ax.set_ylabel("Utility")
        plt.xticks(rotation=25,ha="right")
        plt.show()
        plt.close(fig)


def choose(ch):
    if ch.get("name")!="value":
        return
    vals={"b":(60,25,15),"q":(85,10,5),"c":(40,50,10),"l":(40,10,50)}
    q.value,c.value,l.value=vals[ch["new"]]


preset.observe(choose,names="value")
run_button.on_click(render)

display(widgets.VBox([
    widgets.HTML(f"<b>Dados:</b> {MODE}<br>Ajuste os parâmetros e clique em <b>Simular cenário</b>."),
    preset,q,c,l,g,run_button,out
]))
'''
    return text.splitlines(keepends=True)


def sync_13c() -> None:
    nb = load(LESSON_13C)
    by_id = {cell.get("id"): cell for cell in nb["cells"]}
    if "c08" not in by_id:
        raise RuntimeError("Cell c08 not found in Aula 13C")

    by_id["c08"]["source"] = clean_c08()

    glossary_text = f"""## 📘 Glossário Vivo — conceitos-chave da Aula 13C

Use o Glossário Vivo durante o laboratório. Os conceitos abaixo formam a linguagem necessária para interpretar as decisões do simulador:

**{glossary_link('Baseline')} · {glossary_link('Model Routing')} · {glossary_link('Model Orchestration')} · {glossary_link('Quality Gate')} · {glossary_link('Escalation Rate')} · {glossary_link('Utility Function')} · {glossary_link('Compound AI System')} · {glossary_link('Cost per Inference')} · {glossary_link('Trade-off')}**

### 🧭 Durante o laboratório...

| Quando você estiver pensando em... | Consulte |
|---|---|
| estabelecer uma referência simples para comparação | {glossary_link('Baseline')} |
| escolher modelos diferentes conforme a tarefa | {glossary_link('Model Routing')} |
| combinar modelos ou etapas | {glossary_link('Model Orchestration')} |
| decidir quando aceitar ou escalar uma resposta | {glossary_link('Quality Gate')} |
| entender quantos casos chegam à camada premium | {glossary_link('Escalation Rate')} |
| equilibrar qualidade, custo e latência | {glossary_link('Utility Function')} |
| analisar vários componentes trabalhando juntos | {glossary_link('Compound AI System')} |
| estimar o impacto econômico das chamadas | {glossary_link('Cost per Inference')} |
| aceitar ganhos em uma dimensão e perdas em outra | {glossary_link('Trade-off')} |

> Não memorize os termos isoladamente. Use os links quando o comportamento do simulador levantar uma dúvida conceitual.
"""
    replace_markdown(nb, "c02", glossary_text)

    status_text = f"""### Estado de execução e evidência

Este notebook segue o padrão **headless-first** do TIL: a execução completa (`Run All`) não depende de interação humana. Os widgets são uma camada opcional e o cenário interativo só é calculado quando o aluno clica em **Simular cenário**.

O notebook foi validado em execução local headless e no Kaggle.

O próximo marco experimental é substituir os proxies `DEMO` por medições comparáveis do experimento `EDU-ORCH-001`, começando pelo {glossary_link('Baseline')} **TF-IDF + classificador clássico** versus **DistilBERT multilíngue**.
"""
    upsert_after(nb, "c03", markdown_cell("c03b-headless-status", status_text))

    system_text = f"""## 2. Sistema composto

As linhas carregadas são candidatos `single`. O `cascade` usa a camada de menor custo como inicial e a de maior qualidade como premium. O **quality gate** controla uma **taxa de escalonamento simulada**.

Mesmo em modo EVIDENCE, o ponto intermediário do cascade é uma hipótese de engenharia até ser medido diretamente.

📚 Glossário: {glossary_link('Quality Gate')} · {glossary_link('Escalation Rate')} · {glossary_link('Model Routing')} · {glossary_link('Trade-off')}.
"""
    replace_markdown(nb, "c05", system_text)

    simulator_text = f"""## 3. 🎛️ Simulador

Os sliders mudam **prioridades**, não as medições. Ajuste qualidade, custo, latência e gate; observe ranking, escalonamento e o mapa custo × qualidade.

📚 Glossário: {glossary_link('Utility Function')} · {glossary_link('Cost per Inference')} · {glossary_link('Compound AI System')}.
"""
    replace_markdown(nb, "c07", simulator_text)

    next_text = f"""## 7. Próximo experimento — ativar EVIDENCE com dados reais

A aula está pronta para consumir evidência real, mas não devemos preencher `til-model-evidence.csv` apenas para tornar o simulador mais convincente.

O experimento `docs/experiments/EDU-ORCH-001-model-evidence-baseline-vs-transformer.md` define o próximo passo:

```text
mesmo dataset/split
→ {glossary_link('Baseline')} TF-IDF + classificador clássico
→ DistilBERT multilíngue
→ qualidade + latência + custo
→ proveniência
→ til-model-evidence.csv
→ modo EVIDENCE
```

Até que essas medições existam, **DEMO continua sendo a representação correta e honesta**.
"""
    upsert_last(nb, markdown_cell("c13-next-evidence", next_text))

    save(LESSON_13C, nb)
    print(f"OK: {LESSON_13C.relative_to(ROOT)}")


def main() -> None:
    sync_13()
    sync_13b()
    sync_13c()
    print("Lesson 13 family synchronized.")


if __name__ == "__main__":
    main()
