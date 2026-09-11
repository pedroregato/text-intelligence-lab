# EDU-ORCH-001 — Model evidence: baseline clássico vs Transformer

## Status

Planned

## Objective

Produzir o primeiro conjunto de evidências comparáveis do TIL para alimentar a Aula 13C em modo `EVIDENCE`.

A primeira comparação deve medir, sob o mesmo dataset/split e a mesma métrica de qualidade:

1. um baseline clássico baseado em TF-IDF;
2. um Transformer compacto baseado em DistilBERT multilíngue.

A camada LLM/revisão humana fica fora deste primeiro ciclo até existir uma metodologia reproduzível de custo e avaliação.

## Hypothesis

O Transformer tende a melhorar a qualidade em relação ao baseline clássico, mas com aumento de latência e custo computacional. O objetivo não é provar antecipadamente essa hipótese, e sim medir o trade-off real no ambiente do TIL.

## Required Evidence

Para cada sistema registrar:

- `system`;
- métrica de qualidade compatível, preferencialmente `f1_macro` quando apropriado ao problema;
- `cost_per_1000` em unidade declarada;
- `latency_ms` média;
- p50/p95 de latência no relatório quando viável;
- dataset e split;
- sample size;
- hardware/ambiente;
- versão do modelo;
- data da medição;
- metodologia de custo;
- observações relevantes.

## Experimental Controls

As comparações só serão consideradas válidas quando utilizarem:

- o mesmo conjunto de avaliação;
- a mesma definição de métrica de qualidade;
- pré-processamento documentado;
- metodologia de medição de latência consistente;
- unidade de custo consistente ou conversão explicitamente documentada.

## Planned Systems

### Classical baseline

Candidato inicial:

```text
texto
→ TF-IDF
→ classificador clássico
→ predição
```

O classificador deve ser selecionado entre implementações já ensinadas no TIL, sem escolher retrospectivamente apenas o resultado mais favorável.

### Transformer

Candidato inicial:

```text
texto
→ tokenizer DistilBERT multilingual
→ DistilBERT
→ cabeça de classificação / representação definida pelo experimento
→ predição
```

A versão exata do modelo e sua origem Kaggle devem ser registradas no resultado final.

## Cost Methodology

O campo `cost_per_1000` não deve misturar preço monetário e proxy computacional silenciosamente.

No primeiro ciclo, se não houver preço monetário diretamente observável, é aceitável usar uma unidade de custo computacional normalizada, desde que:

- a unidade seja declarada;
- seja aplicada de forma consistente aos sistemas comparados;
- `evidence_status` e `notes` deixem claro que se trata de estimativa/proxy.

## Procedure

```text
fixar dataset/split
→ executar baseline clássico
→ medir qualidade
→ medir latência
→ registrar custo
→ executar Transformer
→ medir qualidade
→ medir latência
→ registrar custo
→ revisar comparabilidade
→ publicar proveniência
→ atualizar til-model-evidence.csv
→ executar Aula 13C em modo EVIDENCE
```

## Acceptance Criteria

O experimento será considerado concluído quando:

1. pelo menos dois sistemas possuírem medições comparáveis;
2. nenhuma métrica for inventada ou inferida sem metodologia declarada;
3. a proveniência estiver registrada neste documento ou em artefatos associados;
4. `data/model-evidence/til-model-evidence.csv` puder ser preenchido com evidência defensável;
5. a Aula 13C detectar o CSV e executar em modo `EVIDENCE`;
6. o notebook resultante completar execução headless local e no Kaggle.

## Expected Output

- relatório experimental atualizado;
- `data/model-evidence/til-model-evidence.csv` com linhas medidas/estimadas claramente identificadas;
- Aula 13C executada em `EVIDENCE`;
- interpretação pedagógica do trade-off qualidade × custo × latência.

## Evidence

Ainda não coletada. Este documento não declara resultados antecipadamente.