# Glossário Vivo do TIL — F1-score e Média Harmônica

> Aprofundamento conceitual para a Aula 13 e para o **TIL Metric Scenario Lab**.

## F1-score

**English:** F1-score

Métrica que combina **Precisão (Precision)** e **Recall** por meio da **média harmônica**.

A fórmula é:

\[
F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}
\]

### O que isso significa na prática?

O F1-score só fica alto quando **Precision e Recall estão simultaneamente altos**.

Ele não funciona como uma média aritmética comum. Se uma das duas métricas estiver baixa, o F1 é puxado para baixo com força.

Exemplo:

```text
Precision = 0,90
Recall    = 0,30

Média aritmética = 0,60
F1-score         = 0,45
```

A diferença é intencional: o F1 penaliza desequilíbrios entre Precision e Recall.

### Como interpretar

```text
Precision alta + Recall alto
→ F1 tende a ser alto

Precision alta + Recall baixo
→ F1 cai

Precision baixa + Recall alto
→ F1 cai
```

> **O F1 não pergunta apenas “qual é a média?”. Ele pergunta se Precision e Recall conseguem ser boas ao mesmo tempo.**

### Limitação importante

F1 não conhece o custo do negócio.

Dois modelos podem ter F1 semelhante, mas custos muito diferentes se falsos positivos e falsos negativos tiverem impactos diferentes.

**No TIL:** na Aula 13, o F1 é usado junto com threshold, matriz de confusão e custos para mostrar que maximizar uma métrica não é necessariamente o mesmo que tomar a melhor decisão.

**Primeira aula:** 06; aprofundamento na Aula 13.

---

## Média harmônica

**English:** Harmonic Mean

Tipo de média apropriado quando queremos combinar grandezas em que **valores baixos devem ter forte influência no resultado**.

Para dois valores positivos `a` e `b`:

\[
H = \frac{2ab}{a+b}
\]

No F1-score:

```text
a = Precision
b = Recall
```

### Por que não usar simplesmente a média aritmética?

Considere:

```text
Precision = 1,00
Recall    = 0,20
```

A média aritmética seria:

```text
(1,00 + 0,20) / 2 = 0,60
```

Isso pode transmitir uma impressão excessivamente confortável.

A média harmônica produz:

```text
F1 ≈ 0,33
```

Ela evidencia que uma das duas dimensões do desempenho está muito fraca.

### Intuição

Pense em duas pernas sustentando uma estrutura:

```text
Precision ─┐
           ├─ desempenho equilibrado
Recall ────┘
```

Se uma “perna” estiver muito fraca, não faz sentido considerar o sistema equilibrado apenas porque a outra é excelente.

### Relação com outras médias

Para valores positivos, em geral:

```text
média harmônica ≤ média geométrica ≤ média aritmética
```

Quanto maior o desequilíbrio entre os valores, mais evidente tende a ser a diferença.

> **No contexto do F1, a média harmônica funciona como uma penalização natural para o desequilíbrio entre Precision e Recall.**

**No TIL:** este conceito é usado na Aula 13 para explicar por que o F1 pode ser significativamente menor que a média aritmética de Precision e Recall.

**Primeira aula:** 13 como conceito explícito.

---

## Exemplo comparativo

| Precision | Recall | Média aritmética | F1-score |
|---:|---:|---:|---:|
| 0,90 | 0,90 | 0,90 | 0,90 |
| 0,90 | 0,50 | 0,70 | 0,64 |
| 0,90 | 0,30 | 0,60 | 0,45 |
| 0,90 | 0,10 | 0,50 | 0,18 |

Observe como o F1 reage muito mais fortemente quando uma das métricas desaba.

### Pergunta para o aluno

Se `Precision = 0,98` e `Recall = 0,12`, você chamaria o modelo de equilibrado apenas porque a Precision é quase perfeita?

A resposta esperada é **não**. O F1 existe justamente para tornar esse desequilíbrio mais visível.
