# Glossário Vivo do TIL — PT-BR

> Gerado a partir de `glossary.yaml`. Não edite manualmente como fonte primária.

## Dado

**English:** Data

Representação registrada de fatos, observações, medições, categorias, eventos ou outras informações que podem ser armazenadas, inspecionadas, processadas ou analisadas.

**No TIL:** No TIL, texto passa a ser tratado como dado quando pode ser organizado, observado, medido, transformado e utilizado em experimentos.

**Exemplo:** Uma linha de um DataFrame contendo id, canal, rótulo e texto.

**Primeira aula:** 01

## Dado observável

**English:** Observable data

Dado cujos valores, estrutura, estado ou outputs podem ser examinados diretamente.

**No TIL:** O aluno deve conseguir ver registros, colunas, métricas, arquivos gerados ou informações de runtime em vez de apenas assumir que algo aconteceu.

**Exemplo:** Um DataFrame exibido no notebook ou um JSON de evidência baixado do Kaggle.

**Primeira aula:** 00

## Dado inspecionável

**English:** Inspectable data

Dado que pode ser examinado sistematicamente para compreender estrutura, qualidade, consistência, anomalias, ausências e duplicações.

**No TIL:** Inspecionar significa perguntar quantos documentos existem, quais campos estão vazios, quais rótulos faltam e que metadados estão disponíveis.

**Exemplo:** Contar textos vazios e duplicatas antes de qualquer modelagem.

**Primeira aula:** 01

## Reprodutibilidade

**English:** Reproducibility

Capacidade de repetir um procedimento analítico ou computacional a partir de entradas, código, condições e passos documentados e obter resultado igual ou substantivamente equivalente.

**No TIL:** GitHub preserva a fonte canônica; Kaggle fornece o ambiente de execução; outputs e evidências permitem verificar o resultado.

**Exemplo:** Reexecutar um notebook e gerar novamente o mesmo tipo de arquivo de evidência.

**Primeira aula:** 00

## Evidência

**English:** Evidence

Artefato ou resultado observável que sustenta uma conclusão técnica.

**No TIL:** O curso prioriza evidência sobre suposição.

**Exemplo:** Status COMPLETE do Kaggle, uma métrica, um log ou um arquivo JSON gerado.

**Primeira aula:** 00

## Documento

**English:** Document

Unidade individual de texto selecionada para análise.

**No TIL:** Na Aula 1, cada linha do DataFrame representa um documento.

**Exemplo:** Uma mensagem, e-mail, notícia, avaliação, contrato ou chamado.

**Primeira aula:** 01

## Corpus

**English:** Corpus

Coleção de documentos organizada para análise linguística, estatística ou computacional.

**No TIL:** Um corpus pode ser pequeno e artificial para aprendizagem ou conter milhões de documentos em produção.

**Exemplo:** A coleção de mensagens de atendimento usada na Aula 1.

**Primeira aula:** 01

## Dataset

**English:** Dataset

Coleção organizada de dados utilizada para análise, experimentação ou modelagem.

**No TIL:** Um corpus é um dataset cujo objeto analítico central é texto, podendo também conter campos não textuais.

**Exemplo:** Um DataFrame com id, canal, rótulo e texto.

**Primeira aula:** 01

## Metadado

**English:** Metadata

Dado que descreve ou fornece contexto sobre outro dado.

**No TIL:** id, channel e label descrevem o documento; text contém o conteúdo textual.

**Exemplo:** O canal de origem de uma mensagem.

**Primeira aula:** 01

## Rótulo

**English:** Label

Categoria, classe ou valor-alvo conhecido associado a uma observação.

**No TIL:** Mais adiante, rótulos poderão servir como alvo em tarefas supervisionadas.

**Exemplo:** duvida, reclamacao ou elogio.

**Primeira aula:** 01

## Classe

**English:** Class

Uma das categorias possíveis em um problema de classificação.

**No TIL:** Se reclamacao, elogio e duvida são rótulos possíveis, cada um representa uma classe.

**Exemplo:** A classe reclamacao.

**Primeira aula:** 01

## Texto bruto

**English:** Raw text

Texto em sua forma original ou minimamente processada antes de transformações para análise ou modelagem.

**No TIL:** A coluna text da Aula 1 contém texto bruto.

**Exemplo:** Meu pedido ainda não chegou.

**Primeira aula:** 01

## Valor ausente

**English:** Missing value

Campo cujo valor esperado está ausente ou indefinido.

**No TIL:** Um label ausente é diferente de um texto vazio e pode exigir tratamento diferente.

**Exemplo:** label igual a None.

**Primeira aula:** 01

## Duplicata

**English:** Duplicate

Observação ou valor repetido que aparece mais de uma vez em um dataset.

**No TIL:** Duplicatas devem ser investigadas antes de serem removidas automaticamente.

**Exemplo:** Duas mensagens com o mesmo texto.

**Primeira aula:** 01

## Runtime

**English:** Runtime

Ambiente de software e sistema no qual o código é efetivamente executado.

**No TIL:** Inclui versão do Python, sistema operacional, diretório de trabalho e bibliotecas disponíveis.

**Exemplo:** Kaggle executando Python em Linux.

**Primeira aula:** 00

## Output

**English:** Output

Qualquer resultado produzido pela execução de código.

**No TIL:** Pode ser um valor exibido, tabela, arquivo, métrica, log ou gráfico.

**Exemplo:** til_environment_evidence.json.

**Primeira aula:** 00

## Experimento

**English:** Experiment

Procedimento estruturado concebido para testar uma hipótese ou validar uma suposição.

**No TIL:** Os experimentos do TIL registram objetivo, hipótese, ambiente, procedimento, evidência, resultado e conclusão.

**Exemplo:** EDU-INFRA-001.

**Primeira aula:** 00

## Source of truth

**English:** Source of truth

Local considerado a versão autoritativa e canônica de um artefato.

**No TIL:** GitHub é o source of truth do TIL; Kaggle é o ambiente principal de execução.

**Exemplo:** O notebook canônico está no repositório GitHub.

**Primeira aula:** 00

## Versionamento

**English:** Versioning

Rastreamento sistemático de alterações em código, documentos, dados ou outros artefatos ao longo do tempo.

**No TIL:** Git/GitHub mantém a história canônica; Kaggle Versions registra versões de execução.

**Exemplo:** Um commit que altera uma aula.

**Primeira aula:** 00

## Feature

**English:** Feature

Característica mensurável ou codificada utilizada como entrada de um modelo analítico ou preditivo.

**No TIL:** O texto bruto ainda não é uma matriz numérica de features; aulas futuras mostrarão como representá-lo.

**Exemplo:** Contagens de termos ou valores TF-IDF.

**Primeira aula:** 01

## Modelo

**English:** Model

Representação matemática ou computacional utilizada para descrever padrões ou produzir previsões.

**No TIL:** Modelos só entram depois que o curso estabelece dados, representação e avaliação.

**Exemplo:** Um classificador treinado para prever categorias de documentos.

**Primeira aula:** 01

## Classificação

**English:** Classification

Tarefa preditiva em que uma observação é atribuída a uma entre várias classes predefinidas.

**No TIL:** O TIL usará classificação em problemas de documentos e mensagens.

**Exemplo:** Classificar uma mensagem como reclamacao, elogio ou duvida.

**Primeira aula:** 01

## Bag-of-Words

**English:** Bag-of-Words

Representação textual que descreve um documento pelas ocorrências dos termos de um vocabulário, sem preservar diretamente a ordem completa das palavras.

**No TIL:** Na Aula 3, Bag-of-Words é a primeira ponte entre texto e uma representação numérica utilizável por modelos tradicionais.

**Exemplo:** As palavras de um documento tornam-se colunas de uma matriz e seus valores representam contagens.

**Primeira aula:** 03

## Vocabulário

**English:** Vocabulary

Conjunto de termos distintos reconhecidos por uma representação textual em um corpus.

**No TIL:** Cada termo do vocabulário produzido pelo CountVectorizer pode se tornar uma feature.

**Exemplo:** atendimento, excelente, gostei e não.

**Primeira aula:** 03

## Matriz documento-termo

**English:** Document-term matrix

Matriz em que as linhas representam documentos, as colunas representam termos e os valores representam alguma medida associada à ocorrência desses termos.

**No TIL:** Na Aula 3, os valores são contagens produzidas pelo CountVectorizer.

**Exemplo:** Uma linha por mensagem e uma coluna por palavra do vocabulário.

**Primeira aula:** 03

## Matriz esparsa

**English:** Sparse matrix

Estrutura matricial eficiente para dados em que a maioria dos valores é zero.

**No TIL:** Representações textuais costumam ser esparsas porque cada documento contém apenas uma pequena parte do vocabulário total.

**Exemplo:** A saída padrão de CountVectorizer antes de chamar toarray().

**Primeira aula:** 03

## CountVectorizer

**English:** CountVectorizer

Classe do scikit-learn que transforma uma coleção de documentos textuais em uma matriz de contagens de tokens.

**No TIL:** É a ferramenta usada na Aula 3 para construir vocabulário, features e a matriz Bag-of-Words.

**Exemplo:** vectorizer.fit_transform(texts).

**Primeira aula:** 03

## TF

**English:** Term Frequency

Medida da frequência de um termo dentro de um documento.

**No TIL:** Na Aula 4, TF compõe o primeiro fator da ponderação TF-IDF.

**Exemplo:** Quantas vezes uma palavra aparece em uma mensagem.

**Primeira aula:** 04

## IDF

**English:** Inverse Document Frequency

Medida que reduz o peso de termos presentes em muitos documentos e aumenta o peso relativo de termos mais raros no corpus.

**No TIL:** Na Aula 4, IDF ajuda a diferenciar termos comuns de termos mais discriminantes.

**Exemplo:** atendimento recebe menor IDF quando aparece em todos os documentos.

**Primeira aula:** 04

## TF-IDF

**English:** TF-IDF

Técnica de ponderação que combina frequência de termo no documento e raridade do termo no corpus.

**No TIL:** Na Aula 4, TF-IDF transforma documentos em features ponderadas mais informativas do que simples contagens em muitos cenários.

**Exemplo:** termos específicos recebem peso maior do que termos presentes em todos os documentos.

**Primeira aula:** 04

## TfidfVectorizer

**English:** TfidfVectorizer

Classe do scikit-learn que converte documentos textuais em uma matriz de features ponderadas por TF-IDF.

**No TIL:** É a ferramenta principal utilizada na Aula 4.

**Exemplo:** vectorizer.fit_transform(texts).

**Primeira aula:** 04

## Aprendizagem supervisionada

**English:** Supervised learning

Abordagem de Machine Learning em que o modelo aprende a partir de exemplos associados a respostas conhecidas.

**No TIL:** Na Aula 5, cada texto possui um rótulo conhecido usado durante o treinamento.

**Exemplo:** Mensagens rotuladas como duvida, reclamacao ou elogio.

**Primeira aula:** 05

## Divisão treino/teste

**English:** Train/test split

Separação de um dataset em uma parte usada para treinamento e outra reservada para avaliação.

**No TIL:** Na Aula 5, train_test_split evita avaliar o modelo apenas nos exemplos usados para aprender.

**Exemplo:** 67% dos exemplos para treino e 33% para teste.

**Primeira aula:** 05

## Multinomial Naive Bayes

**English:** Multinomial Naive Bayes

Algoritmo probabilístico frequentemente usado como baseline em classificação de texto com features de contagem ou ponderadas.

**No TIL:** Na Aula 5, MultinomialNB recebe features TF-IDF e aprende a prever classes.

**Exemplo:** MultinomialNB() dentro de um Pipeline.

**Primeira aula:** 05

## Acurácia

**English:** Accuracy

Proporção de previsões corretas entre todas as previsões realizadas.

**No TIL:** Na Aula 5, a acurácia é apresentada como uma primeira métrica, com a ressalva de que não deve ser interpretada isoladamente.

**Exemplo:** 3 acertos em 4 previsões correspondem a acurácia 0,75.

**Primeira aula:** 05

## Matriz de confusão

**English:** Confusion matrix

Tabela que cruza classes reais e previstas para mostrar acertos e tipos de erro de um classificador.

**No TIL:** Na Aula 6, a matriz de confusão permite observar quais classes estão sendo confundidas.

**Exemplo:** Linhas representam classes reais e colunas classes previstas.

**Primeira aula:** 06

## Precisão

**English:** Precision

Proporção de previsões de uma classe que estão corretas.

**No TIL:** Na Aula 6, precisão é discutida quando falsos positivos têm custo relevante.

**Exemplo:** Entre tudo que o modelo chamou de reclamacao, quanto realmente era reclamacao.

**Primeira aula:** 06

## Recall

**English:** Recall

Proporção de exemplos reais de uma classe que o modelo conseguiu identificar.

**No TIL:** Na Aula 6, recall é discutido quando perder exemplos positivos é especialmente custoso.

**Exemplo:** Entre todas as reclamações reais, quantas foram detectadas.

**Primeira aula:** 06

## F1-score

**English:** F1-score

Média harmônica entre precisão e recall.

**No TIL:** Na Aula 6, F1-score é apresentado como uma forma de equilibrar as duas métricas.

**Exemplo:** Útil quando precisão e recall precisam ser considerados em conjunto.

**Primeira aula:** 06

## Macro average

**English:** Macro average

Média simples de uma métrica calculada separadamente para cada classe.

**No TIL:** Na Aula 6, macro average ajuda a dar o mesmo peso a todas as classes.

**Exemplo:** Média dos F1-scores das classes sem ponderação por tamanho.

**Primeira aula:** 06

## Weighted average

**English:** Weighted average

Média de uma métrica ponderada pelo número de exemplos de cada classe.

**No TIL:** Na Aula 6, weighted average é comparada à macro average em cenários com classes de tamanhos diferentes.

**Exemplo:** Classes maiores contribuem mais para a média.

**Primeira aula:** 06

## Validação cruzada

**English:** Cross-validation

Estratégia de avaliação que divide os dados de treinamento em múltiplas partes e alterna quais partes são usadas para treino e validação.

**No TIL:** Na Aula 7, validação cruzada permite comparar configurações sem usar o conjunto de teste final.

**Exemplo:** Validação cruzada com 3 folds.

**Primeira aula:** 07

## Hiperparâmetro

**English:** Hyperparameter

Configuração definida antes do treinamento que controla o comportamento de um algoritmo ou pipeline.

**No TIL:** Na Aula 7, ngram_range, min_df e alpha são hiperparâmetros ajustados.

**Exemplo:** classifier__alpha igual a 0.5 ou 1.0.

**Primeira aula:** 07

## Grid Search

**English:** Grid Search

Estratégia de busca que avalia sistematicamente combinações predefinidas de hiperparâmetros.

**No TIL:** Na Aula 7, GridSearchCV combina Grid Search e validação cruzada para selecionar configurações.

**Exemplo:** Testar diferentes valores de ngram_range, min_df e alpha.

**Primeira aula:** 07

## Overfitting

**English:** Overfitting

Situação em que um modelo ou processo de seleção se ajusta excessivamente aos dados observados e perde capacidade de generalização.

**No TIL:** Na Aula 7, olhar repetidamente o conjunto de teste durante o tuning é apresentado como risco de overfitting ao teste.

**Exemplo:** Escolher repetidamente configurações pela melhor nota no teste final.

**Primeira aula:** 07

## Token

**English:** Token

Unidade resultante da segmentação de um texto para processamento computacional.

**No TIL:** Na Aula 2, começamos tratando palavras como tokens, embora outras técnicas possam usar subpalavras ou caracteres.

**Exemplo:** Na frase "atendimento excelente", atendimento e excelente podem ser tokens.

**Primeira aula:** 02

## Tokenização

**English:** Tokenization

Processo de dividir texto em unidades menores chamadas tokens.

**No TIL:** Na Aula 2, comparamos uma estratégia simples com split e uma tokenização baseada em expressão regular.

**Exemplo:** "atendimento excelente" se torna ["atendimento", "excelente"].

**Primeira aula:** 02

## Normalização textual

**English:** Text normalization

Conjunto de transformações aplicadas para reduzir variações superficiais do texto preservando a informação relevante ao problema.

**No TIL:** Na Aula 2, usamos minúsculas e remoção de espaços nas extremidades como exemplos simples.

**Exemplo:** " ATENDIMENTO " se torna "atendimento".

**Primeira aula:** 02

## Expressão regular

**English:** Regular expression

Linguagem compacta de padrões usada para localizar, validar ou extrair sequências de caracteres.

**No TIL:** Na Aula 2, a biblioteca padrão re é usada para extrair tokens com um padrão simples.

**Exemplo:** re.findall(r"\\b\\w+\\b", text).

**Primeira aula:** 02


## Baseline

**English:** Baseline

Modelo ou resultado de referência usado para comparar abordagens mais complexas.

**No TIL:** Na Aula 12, modelos clássicos servem de referência para decidir se a complexidade de um Transformer se justifica.

**Exemplo:** TF-IDF + LinearSVC pode funcionar como baseline forte para classificação de texto.

**Primeira aula:** 12

## Regressão Logística

**English:** Logistic Regression

Modelo linear discriminativo usado para classificação ao estimar escores associados às classes.

**No TIL:** Na Aula 12, é comparada com Naive Bayes e LinearSVC usando a mesma representação TF-IDF.

**Exemplo:** LogisticRegression(max_iter=1000).

**Primeira aula:** 12

## LinearSVC

**English:** LinearSVC

Classificador SVM linear que busca uma fronteira de decisão com ampla margem entre classes.

**No TIL:** Na Aula 12, é usado como baseline forte para espaços textuais de alta dimensionalidade.

**Exemplo:** LinearSVC(random_state=42).

**Primeira aula:** 12

## Margem

**English:** Margin

Distância entre a fronteira de decisão e os exemplos mais próximos em modelos baseados em margem.

**No TIL:** Na Aula 12, ajuda a explicar a lógica do LinearSVC.

**Exemplo:** SVMs procuram separar classes com uma margem ampla.

**Primeira aula:** 12

## Coeficiente

**English:** Coefficient

Peso aprendido por um modelo linear para indicar a contribuição de uma feature à decisão.

**No TIL:** Na Aula 12, coeficientes do LinearSVC são inspecionados para identificar features fortemente associadas às classes.

**Exemplo:** Um coeficiente positivo alto pode favorecer uma classe específica.

**Primeira aula:** 12


## Falso positivo

**English:** False Positive

Caso negativo real que o modelo classificou incorretamente como positivo.

**No TIL:** Na Aula 13, falsos positivos são associados ao custo de alertas incorretos e revisões desnecessárias.

**Exemplo:** Uma transação legítima marcada como fraude.

**Primeira aula:** 13

## Falso negativo

**English:** False Negative

Caso positivo real que o modelo classificou incorretamente como negativo.

**No TIL:** Na Aula 13, falsos negativos representam casos importantes que o sistema deixou escapar.

**Exemplo:** Uma fraude real classificada como transação legítima.

**Primeira aula:** 13

## Especificidade

**English:** Specificity

Proporção dos negativos reais corretamente identificados como negativos.

**No TIL:** Na Aula 13, complementa o recall ao observar o comportamento sobre a classe negativa.

**Exemplo:** TN / (TN + FP).

**Primeira aula:** 13

## Balanced Accuracy

**English:** Balanced Accuracy

Métrica que dá peso equilibrado ao desempenho entre classes, reduzindo o efeito de desbalanceamento.

**No TIL:** Na Aula 13, é apresentada como alternativa à acurácia simples em cenários desbalanceados.

**Exemplo:** No caso binário, pode ser vista como a média entre recall e especificidade.

**Primeira aula:** 13

## Support

**English:** Support

Quantidade de exemplos reais pertencentes a uma classe em um conjunto avaliado.

**No TIL:** Na Aula 13, support ajuda a entender por que weighted averages podem ser dominadas por classes maiores.

**Exemplo:** Uma classe com 900 exemplos tem support muito maior que outra com 20.

**Primeira aula:** 13

## Threshold de decisão

**English:** Decision Threshold

Valor de corte usado para transformar um score ou probabilidade em uma decisão de classe.

**No TIL:** Na Aula 13, alterar o threshold mostra o trade-off entre precision e recall.

**Exemplo:** score >= 0.50 implica classe positiva.

**Primeira aula:** 13

## Taxa de abstenção

**English:** Abstention Rate

Proporção de casos em que o sistema evita emitir uma decisão automática e encaminha o caso para outro fluxo.

**No TIL:** Na Aula 13, aparece como indicador operacional ao lado de qualidade e latência.

**Exemplo:** O modelo abstém em 8% dos casos e envia esses casos para revisão humana.

**Primeira aula:** 13
