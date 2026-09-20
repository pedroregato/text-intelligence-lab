# Glossário Vivo do TIL — PT-BR

> Gerado a partir de `glossary.yaml` + extensões curriculares. Não edite manualmente como fonte primária.

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

**Exemplo:** '"atendimento excelente" se torna ["atendimento", "excelente"].'

**Primeira aula:** 02

## Normalização textual

**English:** Text normalization

Conjunto de transformações aplicadas para reduzir variações superficiais do texto preservando a informação relevante ao problema.

**No TIL:** Na Aula 2, usamos minúsculas e remoção de espaços nas extremidades como exemplos simples.

**Exemplo:** '" ATENDIMENTO " se torna "atendimento".'

**Primeira aula:** 02

## Expressão regular

**English:** Regular expression

Linguagem compacta de padrões usada para localizar, validar ou extrair sequências de caracteres.

**No TIL:** Na Aula 2, a biblioteca padrão re é usada para extrair tokens com um padrão simples.

**Exemplo:** re.findall(r"\\b\\w+\\b", text).

**Primeira aula:** 02

## N-gram

**English:** N-gram

Sequência de n tokens consecutivos usada como unidade de representação textual.

**No TIL:** Na Aula 8, n-grams preservam parte do contexto local que se perde quando usamos apenas palavras isoladas.

**Exemplo:** Em "não gostei", "não gostei" é um bigrama.

**Primeira aula:** 08

## Unigrama

**English:** Unigram

N-gram formado por um único token.

**No TIL:** Na Aula 8, unigramas representam o caso tradicional de palavras isoladas.

**Exemplo:** "atendimento" é um unigrama.

**Primeira aula:** 08

## Bigrama

**English:** Bigram

N-gram formado por dois tokens consecutivos.

**No TIL:** Na Aula 8, bigramas mostram como combinações como "não gostei" podem se tornar features explícitas.

**Exemplo:** "não gostei" é um bigrama.

**Primeira aula:** 08

## Trigrama

**English:** Trigram

N-gram formado por três tokens consecutivos.

**No TIL:** Na Aula 8, trigramas ilustram o ganho de contexto e o aumento da dimensionalidade.

**Exemplo:** "não gostei do" é um trigrama.

**Primeira aula:** 08

## Dimensionalidade

**English:** Dimensionality

Número de dimensões ou features usadas para representar os dados.

**No TIL:** Na Aula 8, adicionar bigramas e trigramas aumenta o número de colunas da matriz textual.

**Exemplo:** Um vocabulário com 5000 features produz uma representação de dimensionalidade 5000.

**Primeira aula:** 08

## Embedding

**English:** Embedding

Representação vetorial aprendida que mapeia entidades, como palavras, para um espaço numérico contínuo.

**No TIL:** Na Aula 9, palavras deixam de ocupar uma dimensão exclusiva e passam a ser representadas por vetores densos.

**Exemplo:** atendimento pode ser representado por [0.18, -0.42, 0.77, ...].

**Primeira aula:** 09

## Vetor denso

**English:** Dense vector

Vetor em que a maior parte das posições contém valores informativos, em contraste com representações esparsas dominadas por zeros.

**No TIL:** Na Aula 9, embeddings de palavras são vetores densos de baixa dimensionalidade relativa.

**Exemplo:** "[0.18, -0.42, 0.77, 0.11]."

**Primeira aula:** 09

## Representação distribuída

**English:** Distributed representation

Representação em que a informação não está concentrada em uma única dimensão, mas distribuída por várias dimensões do vetor.

**No TIL:** Na Aula 9, o significado lexical é aproximado por padrões distribuídos aprendidos a partir do contexto.

**Exemplo:** Duas palavras semelhantes podem compartilhar padrões próximos em várias dimensões.

**Primeira aula:** 09

## Similaridade por cosseno

**English:** Cosine similarity

Medida de similaridade baseada no ângulo entre dois vetores.

**No TIL:** Na Aula 9, é usada para comparar embeddings de palavras.

**Exemplo:** Vetores com direções muito parecidas têm similaridade próxima de 1.

**Primeira aula:** 09

## Word2Vec

**English:** Word2Vec

Família de métodos neurais que aprende embeddings de palavras a partir de seus contextos de ocorrência.

**No TIL:** Na Aula 9, treinamos um pequeno Word2Vec com gensim apenas para observar o mecanismo.

**Exemplo:** Skip-gram tenta prever palavras de contexto a partir de uma palavra central.

**Primeira aula:** 09

## FastText

**English:** FastText

Método de embeddings que representa palavras também por unidades de subpalavras.

**No TIL:** Na Aula 9, FastText é apresentado como evolução útil para variações morfológicas e palavras raras.

**Exemplo:** Uma palavra pode ser composta por vários fragmentos de caracteres.

**Primeira aula:** 09

## Embedding estático

**English:** Static embedding

Embedding que atribui essencialmente a mesma representação a uma palavra independentemente do contexto em que ocorre.

**No TIL:** Na Aula 9, essa limitação prepara a transição futura para embeddings contextuais.

**Exemplo:** banco recebe a mesma representação em "banco aprovou" e "banco da praça".

**Primeira aula:** 09

## Embedding contextual

**English:** Contextual embedding

Representação vetorial cujo valor depende do contexto em que o token aparece.

**No TIL:** Na Aula 10, a mesma palavra recebe vetores diferentes em frases com sentidos distintos.

**Exemplo:** bank em contexto financeiro e bank em contexto geográfico.

**Primeira aula:** 10

## Atenção

**English:** Attention

Mecanismo que calcula pesos de relevância entre elementos de uma sequência para combinar informação contextual.

**No TIL:** Na Aula 10, atenção é introduzida como base para contextualizar tokens em Transformers.

**Exemplo:** Um token pode atribuir maior peso a palavras relevantes ao seu redor.

**Primeira aula:** 10

## Self-attention

**English:** Self-attention

Forma de atenção em que elementos da mesma sequência interagem entre si.

**No TIL:** Na Aula 10, self-attention permite que cada token considere os demais tokens da frase.

**Exemplo:** bank considera river em uma frase para construir sua representação contextual.

**Primeira aula:** 10

## Transformer

**English:** Transformer

Arquitetura neural baseada em mecanismos de atenção para processar sequências e construir representações contextualizadas.

**No TIL:** Na Aula 10, Transformers são apresentados como base de grande parte dos modelos modernos de linguagem.

**Exemplo:** BERT e muitos modelos autoregressivos usam arquitetura Transformer.

**Primeira aula:** 10

## Tokenização por subpalavras

**English:** Subword tokenization

Estratégia que divide palavras em unidades menores reutilizáveis para reduzir problemas de vocabulário e palavras raras.

**No TIL:** Na Aula 10, subwords são apresentados como unidades comuns em tokenizadores de Transformers.

**Exemplo:** Uma palavra rara pode ser dividida em fragmentos conhecidos pelo vocabulário.

**Primeira aula:** 10

## Modelo pré-treinado

**English:** Pretrained model

Modelo que já passou por treinamento em uma grande coleção de dados antes de ser reutilizado em outra tarefa.

**No TIL:** Na Aula 10, um encoder pré-treinado é usado apenas para inferência e observação de embeddings contextuais.

**Exemplo:** distilbert-base-uncased carregado para extrair representações.

**Primeira aula:** 10

## Fine-tuning

**English:** Fine-tuning

Processo de adaptar um modelo pré-treinado a uma tarefa específica usando dados rotulados da nova tarefa.

**No TIL:** Na Aula 11, um Transformer multilíngue é ajustado para classificar mensagens em três categorias.

**Exemplo:** Ajustar um encoder pré-treinado para prever duvida, reclamacao ou elogio.

**Primeira aula:** 11

## Transfer learning

**English:** Transfer learning

Estratégia de reutilizar conhecimento aprendido em uma tarefa ou domínio para acelerar ou melhorar o aprendizado em outra tarefa.

**No TIL:** Na Aula 11, o conhecimento linguístico do modelo pré-treinado é transferido para classificação de mensagens.

**Exemplo:** Reutilizar BERT em vez de treinar um modelo de linguagem do zero.

**Primeira aula:** 11

## Classificação de sequência

**English:** Sequence classification

Tarefa em que uma sequência textual inteira recebe uma classe ou rótulo.

**No TIL:** Na Aula 11, cada mensagem recebe uma das classes duvida, reclamacao ou elogio.

**Exemplo:** Classificar uma mensagem de atendimento em uma categoria.

**Primeira aula:** 11

## Época

**English:** Epoch

Uma passagem completa do algoritmo de treinamento por todos os exemplos do conjunto de treino.

**No TIL:** Na Aula 11, usamos uma única época para manter o experimento leve e didático.

**Exemplo:** num_train_epochs=1.

**Primeira aula:** 11

## Batch

**English:** Batch

Pequeno grupo de exemplos processados juntos durante uma etapa de treinamento.

**No TIL:** Na Aula 11, o batch size controla quantas mensagens entram em cada passo.

**Exemplo:** per_device_train_batch_size=4.

**Primeira aula:** 11

## Learning rate

**English:** Learning rate

Hiperparâmetro que controla o tamanho das atualizações aplicadas aos pesos durante o treinamento.

**No TIL:** Na Aula 11, usamos uma taxa pequena adequada ao fine-tuning de um modelo pré-treinado.

**Exemplo:** learning_rate=2e-5.

**Primeira aula:** 11

## Tokenizer

**English:** Tokenizer

Componente que converte texto em unidades e identificadores numéricos compatíveis com o vocabulário de um modelo.

**No TIL:** Na Aula 11, o tokenizer prepara as mensagens para entrada no Transformer.

**Exemplo:** AutoTokenizer.from_pretrained(...).

**Primeira aula:** 11

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

## Proxy didático

**English:** Didactic proxy

Representação simplificada usada para aproximar um conceito, custo, comportamento ou consequência real com finalidade de aprendizagem, sem pretender reproduzir toda a complexidade do fenômeno original.

**No TIL:** Na Aula 13 e no Metric Scenario Lab, valores monetários atribuídos a erros podem funcionar como proxies didáticos para tornar trade-offs visíveis e comparáveis. Eles não devem ser confundidos com uma valoração completa de consequências humanas, éticas, sociais ou regulatórias.

**Exemplo:** Atribuir R$ 500 a um falso negativo em uma simulação médica pode ajudar a comparar cenários, mas esse valor não representa o valor de uma vida nem esgota o impacto de um diagnóstico perdido.

**Primeira aula:** 13

## Trade-off

**English:** Trade-off

Situação em que melhorar uma dimensão de uma decisão tende a piorar outra, exigindo equilíbrio entre objetivos que não podem ser maximizados simultaneamente.

**No TIL:** Na Aula 13, reduzir o threshold pode aumentar o recall e diminuir falsos negativos, mas também aumentar falsos positivos e reduzir a precisão. O melhor ponto depende do contexto, dos custos e do objetivo do sistema.

**Exemplo:** Em triagem médica, aceitar mais falsos positivos pode ser um trade-off razoável se isso reduzir significativamente o risco de deixar pacientes graves sem encaminhamento.

**Primeira aula:** 13

## Média harmônica

**English:** Harmonic Mean

Tipo de média que dá influência relativamente maior aos valores menores e, por isso, é útil quando um resultado só deve ser considerado forte se todos os componentes combinados também forem fortes.

**No TIL:** No F1-score, a média harmônica combina Precisão e Recall e penaliza desequilíbrios: uma métrica muito alta não compensa facilmente a outra muito baixa.

**Exemplo:** Com Precisão de 0,90 e Recall de 0,30, a média aritmética é 0,60, enquanto o F1, baseado na média harmônica, é 0,45.

**Primeira aula:** 13

## Roteamento de modelos

**English:** Model Routing

Estratégia que decide qual modelo, ferramenta ou caminho de execução deve receber cada entrada com base em critérios como dificuldade, confiança, custo, latência ou risco.

**No TIL:** Na Aula 13C, o roteador pode manter casos simples no modelo econômico e encaminhar casos de baixa confiança para uma camada mais forte.

**Exemplo:** Uma mensagem curta e inequívoca pode ser classificada pelo baseline, enquanto um caso ambíguo é encaminhado ao Transformer.

**Primeira aula:** 13C

## Orquestração de modelos

**English:** Model Orchestration

Coordenação de múltiplos modelos e etapas de processamento em um fluxo único, incluindo regras de roteamento, avaliação, revisão, fallback e escalonamento.

**No TIL:** A Aula 13C compara estratégias single, cascade e critique para mostrar que o sistema pode ser mais importante do que um modelo isolado.

**Exemplo:** Um modelo econômico gera a primeira resposta, um gate avalia a qualidade e um modelo premium é acionado apenas quando necessário.

**Primeira aula:** 13C

## Quality gate

**English:** Quality Gate

Regra ou mecanismo de avaliação que decide se uma saída possui qualidade suficiente para ser aceita ou se precisa ser rejeitada, revisada ou escalada.

**No TIL:** No simulador 13C, tornar o gate mais rigoroso aumenta a parcela de casos que segue para a camada premium e altera qualidade, custo e latência.

**Exemplo:** Se a confiança do classificador ficar abaixo de 0,70, o caso pode ser encaminhado para um modelo mais forte ou revisão humana.

**Primeira aula:** 13C

## Taxa de escalonamento

**English:** Escalation Rate

Proporção de casos que deixa a camada inicial e é encaminhada para uma etapa mais cara, mais lenta, mais especializada ou humana.

**No TIL:** Na Aula 13C, a taxa de escalonamento é uma métrica operacional central para entender quanto o cascade realmente usa a camada premium.

**Exemplo:** Uma taxa de 25% significa que um em cada quatro casos segue além do modelo inicial.

**Primeira aula:** 13C

## Função de utilidade

**English:** Utility Function

Função que combina diferentes objetivos em uma pontuação comum para tornar explícitas as prioridades usadas em uma decisão.

**No TIL:** O simulador 13C usa uma função simples que recompensa qualidade e penaliza custo e latência, com pesos definidos pelo aluno.

**Exemplo:** U = wq·Q − wc·C − wl·L permite comparar sistemas quando qualidade, custo e latência têm importâncias diferentes.

**Primeira aula:** 13C

## Sistema composto de IA

**English:** Compound AI System

Sistema de IA formado por múltiplos componentes coordenados, como modelos, ferramentas, recuperadores, regras, verificadores e etapas humanas.

**No TIL:** A Aula 13C amplia a avaliação do modelo isolado para a avaliação do sistema completo, incluindo roteamento, gates, custo, latência e revisão.

**Exemplo:** Um baseline classifica primeiro, um Transformer trata casos difíceis e um humano revisa situações críticas.

**Primeira aula:** 13C

## Custo por inferência

**English:** Cost per Inference

Custo associado ao processamento de uma entrada pelo sistema, podendo incluir computação, tokens, chamadas de API, infraestrutura e etapas humanas.

**No TIL:** No 13C, o custo pode ser informado em unidade monetária ou índice relativo, desde que a unidade seja consistente entre os sistemas comparados.

**Exemplo:** Se mil classificações custam R$ 12 em recursos computacionais, o custo médio por inferência é R$ 0,012.

**Primeira aula:** 13C

## Large Language Model (LLM)

**English:** Large Language Model (LLM)

Modelo de linguagem de grande escala treinado em grandes volumes de dados para aprender padrões estatísticos de linguagem e executar tarefas como geração, transformação e análise de texto.

**No TIL:** Na Aula 14, LLM é tratado como uma classe de modelo com capacidade generativa ampla, não como substituto automático de classificadores, encoders ou regras.

**Exemplo:** Um LLM pode receber uma instrução e produzir um resumo em linguagem natural.

**Primeira aula:** 14

## Modelo autoregressivo

**English:** Autoregressive Model

Modelo que produz uma sequência estimando a distribuição do próximo elemento com base nos elementos anteriores já presentes no contexto.

**No TIL:** Na Aula 14, a geração textual é apresentada como repetição de next-token prediction: o token escolhido passa a integrar o contexto da próxima etapa.

**Exemplo:** Após o contexto “O atendimento foi”, o modelo estima probabilidades para possíveis próximos tokens.

**Primeira aula:** 14

## Prompt

**English:** Prompt

Texto ou conjunto de instruções e dados fornecidos ao modelo como parte do contexto para orientar uma resposta ou geração.

**No TIL:** Na Aula 14, prompt é tratado como entrada contextual do modelo, não como garantia de comportamento correto.

**Exemplo:** “Resuma o atendimento em três frases” é uma instrução que pode compor um prompt.

**Primeira aula:** 14

## Contexto

**English:** Context

Conjunto de tokens e informações disponíveis ao modelo no momento em que ele calcula sua próxima saída.

**No TIL:** Na Aula 14, o contexto pode incluir instruções, exemplos, texto do usuário e tokens já gerados.

**Exemplo:** Uma instrução, um trecho de documento e a resposta parcial podem coexistir no contexto.

**Primeira aula:** 14

## Janela de contexto

**English:** Context Window

Limite de contexto que um modelo consegue considerar em uma execução, normalmente expresso em quantidade de tokens.

**No TIL:** Na Aula 14, a janela de contexto conecta capacidade do modelo a custo, latência e necessidade de selecionar informação relevante.

**Exemplo:** Um texto maior do que a janela disponível precisa ser reduzido, segmentado ou tratado por outra estratégia.

**Primeira aula:** 14

## Logits

**English:** Logits

Valores numéricos não normalizados produzidos por um modelo antes de serem convertidos em probabilidades.

**No TIL:** Na Aula 14, logits didáticos são transformados por softmax para visualizar uma distribuição sobre possíveis próximos tokens.

**Exemplo:** Os valores 2.2, 1.5 e 0.7 podem ser logits associados a três tokens candidatos.

**Primeira aula:** 14

## Geração

**English:** Generation

Processo de produzir uma sequência de saída a partir de um modelo, frequentemente escolhendo tokens sucessivos condicionados ao contexto.

**No TIL:** Na Aula 14, geração é contrastada com classificação para mostrar que produzir texto novo é uma capacidade diferente de escolher uma classe.

**Exemplo:** Produzir um resumo livre a partir de uma conversa é uma tarefa de geração.

**Primeira aula:** 14

## Greedy decoding

**English:** Greedy Decoding

Estratégia de decodificação que escolhe, em cada etapa, o token de maior probabilidade disponível.

**No TIL:** Na Aula 14, greedy decoding serve como referência determinística para comparar com estratégias de sampling.

**Exemplo:** Se “ótimo” tem a maior probabilidade, greedy decoding escolhe “ótimo” como próximo token.

**Primeira aula:** 14

## Sampling

**English:** Sampling

Estratégia de seleção em que o próximo token é sorteado de acordo com uma distribuição de probabilidades, possivelmente modificada por parâmetros de decodificação.

**No TIL:** Na Aula 14, sampling é usado para mostrar por que duas gerações podem divergir mesmo a partir do mesmo contexto.

**Exemplo:** Tokens com probabilidades 0,6 e 0,3 podem ambos ser escolhidos em execuções diferentes.

**Primeira aula:** 14

## Temperature

**English:** Temperature

Parâmetro de decodificação que altera a concentração da distribuição usada para selecionar tokens.

**No TIL:** Na Aula 14, temperature é interpretada probabilisticamente: valores menores tendem a concentrar a distribuição e valores maiores tendem a espalhá-la.

**Exemplo:** Aplicar softmax(logits / temperature) com temperature menor pode aumentar a dominância do token mais provável.

**Primeira aula:** 14

## Top-k

**English:** Top-k

Estratégia de decodificação que restringe a escolha aos k tokens de maior probabilidade em uma etapa de geração.

**No TIL:** Na Aula 14, top-k mostra como limitar o conjunto de candidatos sem confundir restrição de amostragem com garantia de qualidade.

**Exemplo:** Com top-k = 2, apenas os dois tokens mais prováveis permanecem candidatos ao próximo passo.

**Primeira aula:** 14

## Top-p

**English:** Top-p

Estratégia de decodificação que mantém o menor conjunto de tokens cuja probabilidade acumulada atinge um limiar p.

**No TIL:** Na Aula 14, top-p é apresentado como filtro adaptativo de candidatos, também conhecido como nucleus sampling.

**Exemplo:** Com top-p = 0,80, o conjunto é ampliado até que a soma das probabilidades alcance pelo menos 80%.

**Primeira aula:** 14

## Saída estruturada

**English:** Structured Output

Saída gerada segundo uma estrutura ou contrato explícito de campos, tipos ou formato que pode ser validado programaticamente.

**No TIL:** Na Aula 14, structured output separa a capacidade de gerar conteúdo da necessidade de verificar se a resposta cumpre um schema esperado.

**Exemplo:** Um objeto JSON com os campos sentiment e confidence pode ser validado após a geração.

**Primeira aula:** 14

## Alucinação

**English:** Hallucination

Termo usado para descrever saídas geradas que apresentam conteúdo não sustentado pelo contexto, pela evidência disponível ou pelos fatos relevantes, apesar de poderem parecer plausíveis.

**No TIL:** Na Aula 14, o termo é usado com cautela e não substitui a análise de tipos específicos de falha, como formato inválido, perda de restrição ou erro factual.

**Exemplo:** O modelo afirmar um dado inexistente em um documento fornecido pode ser tratado como uma forma de alucinação.

**Primeira aula:** 14

## Retrieval

**English:** Information Retrieval

Processo de localizar e ordenar itens potencialmente relevantes para uma consulta dentro de uma coleção.

**No TIL:** Na Aula 15, retrieval é estudado separadamente de generation para tornar observável como evidências são encontradas antes de qualquer resposta ser gerada.

**Exemplo:** Buscar os documentos mais relevantes para a consulta “como solicitar reembolso”.

**Primeira aula:** 15

## Consulta

**English:** Query

Representação da necessidade de informação usada para pesquisar uma coleção.

**No TIL:** Na Aula 15, a query é comparada com documentos ou chunks para produzir scores e um ranking.

**Exemplo:** “qual é o prazo do reembolso” é uma query sobre o corpus.

**Primeira aula:** 15

## Busca lexical

**English:** Lexical Search

Busca baseada principalmente na correspondência e ponderação de termos presentes na consulta e nos documentos.

**No TIL:** Na Aula 15, TF-IDF e cosine similarity formam a referência lexical para comparar query e documentos.

**Exemplo:** Uma consulta contendo “reembolso” tende a recuperar documentos que também contêm esse termo.

**Primeira aula:** 15

## Busca semântica

**English:** Semantic Search

Busca que compara representações vetoriais com o objetivo de aproximar itens por significado, não apenas por coincidência literal de termos.

**No TIL:** Na Aula 15, vetores densos didáticos ilustram como expressões lexicalmente diferentes podem ficar próximas em um espaço semântico.

**Exemplo:** “recuperar senha” e “esqueci minha credencial” podem receber alta similaridade mesmo usando palavras diferentes.

**Primeira aula:** 15

## Ranking

**English:** Ranking

Ordenação de candidatos segundo um score ou critério de relevância para uma consulta.

**No TIL:** Na Aula 15, o ranking torna visível quais documentos ou chunks são priorizados por um método de retrieval.

**Exemplo:** D2 pode ocupar a posição 1 porque obteve o maior score para a query de reembolso.

**Primeira aula:** 15

## Score de retrieval

**English:** Retrieval Score

Valor produzido por um método de retrieval para representar a proximidade ou relevância relativa entre uma consulta e um item.

**No TIL:** Na Aula 15, cosine similarity é usada como score em exemplos lexicais e semânticos.

**Exemplo:** Um score de 0,62 pode posicionar um documento acima de outro com 0,31 para a mesma query.

**Primeira aula:** 15

## Top-k de retrieval

**English:** Top-k Retrieval

Seleção dos k itens mais bem ranqueados por um sistema de retrieval.

**No TIL:** Na Aula 15, top-k de retrieval é explicitamente diferenciado do top-k usado na decodificação de geração.

**Exemplo:** Top-k = 3 devolve os três documentos com maior score para a consulta.

**Primeira aula:** 15

## Chunk

**English:** Chunk

Unidade segmentada de um documento usada como item independente para processamento ou recuperação.

**No TIL:** Na Aula 15, sentenças são usadas como chunks para observar como a granularidade altera o ranking.

**Exemplo:** Uma sentença sobre prazo de reembolso pode ser um chunk separado de outras informações do mesmo documento.

**Primeira aula:** 15

## Chunking

**English:** Chunking

Processo de dividir documentos em unidades menores para indexação, recuperação ou processamento.

**No TIL:** Na Aula 15, chunking mostra o trade-off entre contexto amplo e precisão local na recuperação.

**Exemplo:** Dividir um documento longo em sentenças antes de calcular scores de retrieval.

**Primeira aula:** 15

## Overlap

**English:** Overlap

Trecho compartilhado entre chunks adjacentes para reduzir perda de contexto nas fronteiras de segmentação.

**No TIL:** Na Aula 15, overlap é introduzido conceitualmente como uma decisão de chunking que aumenta redundância e custo do índice.

**Exemplo:** Dois chunks consecutivos podem compartilhar a última sentença do primeiro como primeira sentença do segundo.

**Primeira aula:** 15

## Grounding

**English:** Grounding

Prática de vincular uma resposta, afirmação ou decisão a evidências explicitamente disponíveis e recuperáveis.

**No TIL:** Na Aula 15, grounding é demonstrado sem LLM: a resposta determinística é construída apenas a partir do evidence pack recuperado.

**Exemplo:** Responder o prazo de reembolso citando o chunk que contém exatamente essa informação.

**Primeira aula:** 15

## Evidence pack

**English:** Evidence Pack

Conjunto organizado de evidências recuperadas e seus metadados preparado para sustentar uma resposta, decisão ou etapa posterior do sistema.

**No TIL:** Na Aula 15, o evidence pack contém query, identificador do trecho, texto recuperado e retrieval score.

**Exemplo:** Um objeto com query, C3, o texto do chunk e seu score de similaridade.

**Primeira aula:** 15

## Retrieval-Augmented Generation (RAG)

**English:** Retrieval-Augmented Generation (RAG)

Arquitetura que combina recuperação de evidências com geração, inserindo informação recuperada no contexto usado para produzir a resposta.

**No TIL:** Na Aula 16, RAG é decomposto em retrieval, seleção de evidência, construção de contexto, geração, grounding e avaliação.

**Exemplo:** Uma pergunta recupera dois trechos relevantes e o gerador produz a resposta usando apenas esses trechos.

**Primeira aula:** 16

## Generation-only

**English:** Generation-only

Configuração em que a resposta é produzida sem uma etapa explícita de retrieval de evidências externas.

**No TIL:** Na Aula 16, generation-only funciona como baseline arquitetural para comparar com o fluxo RAG.

**Exemplo:** Responder uma pergunta diretamente a partir do prompt sem consultar o corpus didático.

**Primeira aula:** 16

## Construção de contexto

**English:** Context Construction

Etapa que organiza instruções, consulta e evidências recuperadas em uma entrada estruturada para o gerador.

**No TIL:** Na Aula 16, o contexto é mostrado explicitamente para que o aluno veja quais trechos chegam à etapa de geração.

**Exemplo:** Combinar instrução, C1 e C2 recuperados e a pergunta em um único bloco de entrada.

**Primeira aula:** 16

## Resposta fundamentada

**English:** Grounded Answer

Resposta cuja afirmação pode ser rastreada até evidências explicitamente disponíveis no contexto ou no evidence pack.

**No TIL:** Na Aula 16, uma resposta só é considerada grounded quando a informação usada aparece nas evidências recuperadas.

**Exemplo:** Responder “cinco dias úteis” e indicar C3 como fonte.

**Primeira aula:** 16

## Groundedness

**English:** Groundedness

Grau em que as afirmações de uma resposta são sustentadas pelas evidências fornecidas ao sistema.

**No TIL:** Na Aula 16, groundedness é tratada como propriedade distinta de fluência ou plausibilidade.

**Exemplo:** Uma resposta pode soar bem, mas ter groundedness baixa se incluir fatos ausentes do evidence pack.

**Primeira aula:** 16

## Atribuição de fonte

**English:** Source Attribution

Associação explícita entre uma afirmação da resposta e a fonte ou trecho que a sustenta.

**No TIL:** Na Aula 16, attribution torna a origem da resposta auditável e separa resposta correta de resposta rastreável.

**Exemplo:** A resposta indica “[C2]” ao lado da informação usada.

**Primeira aula:** 16

## Falha de retrieval

**English:** Retrieval Failure

Falha em que a etapa de retrieval não recupera a evidência necessária ou prioriza evidência inadequada.

**No TIL:** Na Aula 16, esse tipo de falha é separado de erros posteriores de contexto ou geração.

**Exemplo:** O corpus contém a resposta, mas o trecho correto não aparece no top-k.

**Primeira aula:** 16

## Falha de contexto

**English:** Context Failure

Falha em que evidências adequadas foram recuperadas, mas são organizadas, truncadas ou apresentadas de forma que prejudica a etapa seguinte.

**No TIL:** Na Aula 16, context failure mostra que retrieval correto não garante um contexto útil.

**Exemplo:** O trecho correto é recuperado, mas fica fora do bloco entregue ao gerador.

**Primeira aula:** 16

## Falha de geração

**English:** Generation Failure

Falha em que o contexto contém evidência suficiente, mas a saída gerada ignora, distorce ou extrapola essa evidência.

**No TIL:** Na Aula 16, generation failure é isolada das falhas de retrieval para facilitar diagnóstico e observabilidade.

**Exemplo:** O contexto informa cinco dias úteis, mas a resposta afirma dez dias.

**Primeira aula:** 16

## Evidência insuficiente

**English:** Insufficient Evidence

Condição em que as evidências disponíveis não sustentam de forma adequada uma resposta específica.

**No TIL:** Na Aula 16, o sistema deve reconhecer essa condição e preferir abstention, ampliar a busca ou escalar.

**Exemplo:** Nenhum chunk recuperado contém informação sobre o prazo solicitado.

**Primeira aula:** 16

## Factualidade

**English:** Factuality

Grau em que uma afirmação ou resposta corresponde aos fatos ou à realidade relevante.

**No TIL:** Na Aula 16, factualidade é diferenciada de groundedness: uma resposta pode estar apoiada em uma fonte e ainda estar errada se a fonte estiver incorreta ou desatualizada.

**Exemplo:** A resposta cita corretamente um documento antigo que afirma prazo de dez dias, embora a regra atual seja cinco.

**Primeira aula:** 16

## Governança da evidência

**English:** Evidence Governance

Conjunto de práticas para controlar origem, autoridade, validade, atualização, versionamento e uso de evidências em um sistema.

**No TIL:** Na Aula 16, governança da evidência explica por que retrieval e grounding tecnicamente corretos não garantem factualidade.

**Exemplo:** O sistema só considera documentos vigentes, aprovados e com fonte identificada.

**Primeira aula:** 16

## Atualidade da evidência

**English:** Freshness

Propriedade que indica quão atual e ainda vigente é uma evidência para a decisão ou pergunta em análise.

**No TIL:** Na Aula 16, freshness aparece como fator de governança capaz de tornar uma resposta grounded porém factualmente incorreta quando a fonte está desatualizada.

**Exemplo:** Uma política publicada em 2024 foi substituída por uma versão de 2026.

**Primeira aula:** 16

## Nível de autoridade

**English:** Authority Level

Indicação da força ou prioridade de uma fonte para sustentar uma afirmação, decisão ou política.

**No TIL:** Na Aula 16, authority level ajuda a diferenciar fontes oficiais, secundárias ou informais quando há evidências conflitantes.

**Exemplo:** Uma norma oficial vigente tem prioridade sobre uma FAQ antiga não revisada.

**Primeira aula:** 16

## Chamada de ferramenta

**English:** Tool Calling

Mecanismo pelo qual um sistema solicita a execução de uma ferramenta externa por meio de uma chamada estruturada.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Chamada de função

**English:** Function Calling

Forma de tool calling em que a capacidade externa é representada como uma função com nome, argumentos e contrato definidos.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Contrato de ferramenta

**English:** Tool Contract

Especificação explícita de nome, descrição, entradas, validação, saída e semântica de erros de uma ferramenta.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Schema de entrada

**English:** Input Schema

Descrição estruturada dos campos, tipos, obrigatoriedade e restrições aceitos por uma chamada de ferramenta.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Registro de ferramentas

**English:** Tool Registry

Catálogo estruturado de ferramentas disponíveis, seus contratos e formas de execução.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Efeito colateral

**English:** Side Effect

Alteração observável de estado causada pela execução de uma operação além do valor retornado diretamente.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Gate de aprovação

**English:** Approval Gate

Ponto de controle que exige autorização explícita antes de uma ação potencialmente sensível ou irreversível.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17

## Observabilidade de ferramentas

**English:** Tool Observability

Capacidade de registrar e inspecionar seleção da ferramenta, argumentos, validação, execução, resultado, latência e erros.

**No TIL:** Na Aula 17, o conceito é aplicado ao laboratório TIL Tool Registry e à transição de resposta para ação estruturada.

**Exemplo:** O aluno inspeciona a chamada, valida os argumentos e observa o resultado ou erro antes da resposta final.

**Primeira aula:** 17
