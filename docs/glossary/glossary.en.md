# TIL Living Glossary — EN

> Generated from `glossary.yaml` + curriculum extensions. Do not edit manually as the primary source.

## Data

A recorded representation of facts, observations, measurements, categories, events, or other information that can be stored, inspected, processed, or analyzed.

**In TIL:** In TIL, text becomes data when it can be organized, observed, measured, transformed, and used in experiments.

**Example:** A DataFrame row containing an id, channel, label, and text.

**First lesson:** 01

## Observable data

Data whose values, structure, state, or outputs can be directly examined.

**In TIL:** The learner should be able to inspect records, columns, metrics, generated files, or runtime information instead of merely assuming that something happened.

**Example:** A displayed DataFrame or a Kaggle evidence JSON file.

**First lesson:** 00

## Inspectable data

Data that can be systematically examined to understand structure, quality, consistency, anomalies, missing values, and duplicates.

**In TIL:** Inspection means asking how many documents exist, which fields are empty, which labels are missing, and what metadata is available.

**Example:** Counting empty texts and duplicates before modeling.

**First lesson:** 01

## Reproducibility

The ability to repeat an analytical or computational procedure from documented inputs, code, conditions, and steps and obtain the same or substantively equivalent outcome.

**In TIL:** GitHub preserves the canonical source; Kaggle provides the execution environment; outputs and evidence make results verifiable.

**Example:** Re-running a notebook and generating the same type of evidence file.

**First lesson:** 00

## Evidence

An observable artifact or result that supports a technical conclusion.

**In TIL:** The course prioritizes evidence over assumption.

**Example:** A Kaggle COMPLETE status, a metric, a log, or a generated JSON file.

**First lesson:** 00

## Document

An individual unit of text selected for analysis.

**In TIL:** In Lesson 1, each DataFrame row represents one document.

**Example:** A message, email, news article, review, contract, or support ticket.

**First lesson:** 01

## Corpus

A collection of documents organized for linguistic, statistical, or computational analysis.

**In TIL:** A corpus may be small and artificial for learning or contain millions of documents in production.

**Example:** The customer-service message collection used in Lesson 1.

**First lesson:** 01

## Dataset

An organized collection of data used for analysis, experimentation, or modeling.

**In TIL:** A corpus is a dataset whose central analytical object is text, while it may also contain non-text fields.

**Example:** A DataFrame with id, channel, label, and text.

**First lesson:** 01

## Metadata

Data that describes or provides context about other data.

**In TIL:** id, channel, and label describe the document; text contains the textual content.

**Example:** The source channel of a message.

**First lesson:** 01

## Label

A known category, class, or target value associated with an observation.

**In TIL:** Later, labels may serve as targets in supervised learning tasks.

**Example:** question, complaint, or praise.

**First lesson:** 01

## Class

One of the possible categories in a classification problem.

**In TIL:** If complaint, praise, and question are possible labels, each represents a class.

**Example:** The complaint class.

**First lesson:** 01

## Raw text

Text in its original or minimally processed form before transformations for analysis or modeling.

**In TIL:** The text column in Lesson 1 contains raw text.

**Example:** My order has not arrived yet.

**First lesson:** 01

## Missing value

A field whose expected value is absent or undefined.

**In TIL:** A missing label is different from an empty text and may require different treatment.

**Example:** A label equal to None.

**First lesson:** 01

## Duplicate

A repeated observation or value appearing more than once in a dataset.

**In TIL:** Duplicates should be investigated before being automatically removed.

**Example:** Two messages with the same text.

**First lesson:** 01

## Runtime

The software and system environment in which code is actually executed.

**In TIL:** It includes Python version, operating system, working directory, and available libraries.

**Example:** Kaggle running Python on Linux.

**First lesson:** 00

## Output

Any result produced by executing code.

**In TIL:** It may be a displayed value, table, file, metric, log, or chart.

**Example:** til_environment_evidence.json.

**First lesson:** 00

## Experiment

A structured procedure designed to test a hypothesis or validate an assumption.

**In TIL:** TIL experiments record objective, hypothesis, environment, procedure, evidence, result, and conclusion.

**Example:** EDU-INFRA-001.

**First lesson:** 00

## Source of truth

The location considered the authoritative and canonical version of an artifact.

**In TIL:** GitHub is TIL's source of truth; Kaggle is the primary execution environment.

**Example:** The canonical notebook lives in the GitHub repository.

**First lesson:** 00

## Versioning

The systematic tracking of changes to code, documents, data, or other artifacts over time.

**In TIL:** Git/GitHub maintains canonical history; Kaggle Versions records execution versions.

**Example:** A commit that changes a lesson.

**First lesson:** 00

## Feature

A measurable or encoded characteristic used as input to an analytical or predictive model.

**In TIL:** Raw text is not yet a numerical feature matrix; future lessons will show how to represent it.

**Example:** Term counts or TF-IDF values.

**First lesson:** 01

## Model

A mathematical or computational representation used to describe patterns or make predictions.

**In TIL:** Models appear only after the course establishes data, representation, and evaluation foundations.

**Example:** A classifier trained to predict document categories.

**First lesson:** 01

## Classification

A predictive task in which an observation is assigned to one of several predefined classes.

**In TIL:** TIL will use classification for document and message problems.

**Example:** Classifying a message as complaint, praise, or question.

**First lesson:** 01

## Bag-of-Words

A text representation that describes a document through occurrences of vocabulary terms without directly preserving full word order.

**In TIL:** In Lesson 3, Bag-of-Words is the first bridge between text and a numerical representation usable by traditional models.

**Example:** Document words become matrix columns and their values represent counts.

**First lesson:** 03

## Vocabulary

The set of distinct terms recognized by a text representation in a corpus.

**In TIL:** Each vocabulary term produced by CountVectorizer may become a feature.

**Example:** service, excellent, liked, and not.

**First lesson:** 03

## Document-term matrix

A matrix whose rows represent documents, columns represent terms, and values represent a measure associated with term occurrence.

**In TIL:** In Lesson 3, values are counts produced by CountVectorizer.

**Example:** One row per message and one column per vocabulary word.

**First lesson:** 03

## Sparse matrix

An efficient matrix structure for data in which most values are zero.

**In TIL:** Text representations are often sparse because each document contains only a small fraction of the full vocabulary.

**Example:** CountVectorizer's default output before calling toarray().

**First lesson:** 03

## CountVectorizer

A scikit-learn class that converts a collection of text documents into a matrix of token counts.

**In TIL:** It is used in Lesson 3 to build the vocabulary, features, and Bag-of-Words matrix.

**Example:** vectorizer.fit_transform(texts).

**First lesson:** 03

## Term Frequency

A measure of how frequently a term appears within a document.

**In TIL:** In Lesson 4, TF is the first component of TF-IDF weighting.

**Example:** How many times a word appears in a message.

**First lesson:** 04

## Inverse Document Frequency

A measure that downweights terms appearing in many documents and relatively upweights rarer terms.

**In TIL:** In Lesson 4, IDF helps distinguish common terms from more discriminative ones.

**Example:** service receives a lower IDF when it appears in every document.

**First lesson:** 04

## TF-IDF

A weighting technique that combines term frequency within a document with term rarity across the corpus.

**In TIL:** In Lesson 4, TF-IDF transforms documents into weighted features that can be more informative than raw counts.

**Example:** Specific terms receive higher weight than terms occurring in every document.

**First lesson:** 04

## TfidfVectorizer

A scikit-learn class that converts text documents into a TF-IDF-weighted feature matrix.

**In TIL:** It is the main tool used in Lesson 4.

**Example:** vectorizer.fit_transform(texts).

**First lesson:** 04

## Supervised learning

A Machine Learning approach in which a model learns from examples associated with known target answers.

**In TIL:** In Lesson 5, each text has a known label used during training.

**Example:** Messages labeled as question, complaint, or praise.

**First lesson:** 05

## Train/test split

Splitting a dataset into one portion used for training and another reserved for evaluation.

**In TIL:** In Lesson 5, train_test_split prevents evaluating the model only on examples used for learning.

**Example:** 67% of examples for training and 33% for testing.

**First lesson:** 05

## Multinomial Naive Bayes

A probabilistic algorithm often used as a baseline for text classification with count-based or weighted features.

**In TIL:** In Lesson 5, MultinomialNB receives TF-IDF features and learns to predict classes.

**Example:** MultinomialNB() inside a Pipeline.

**First lesson:** 05

## Accuracy

The proportion of correct predictions among all predictions made.

**In TIL:** In Lesson 5, accuracy is introduced as a first metric with the caveat that it should not be interpreted alone.

**Example:** 3 correct predictions out of 4 correspond to accuracy 0.75.

**First lesson:** 05

## Confusion matrix

A table crossing true and predicted classes to show correct predictions and error types.

**In TIL:** In Lesson 6, the confusion matrix shows which classes are being confused.

**Example:** Rows represent true classes and columns predicted classes.

**First lesson:** 06

## Precision

The proportion of predictions for a class that are correct.

**In TIL:** In Lesson 6, precision matters when false positives are costly.

**Example:** Of everything predicted as complaint, how much was actually complaint.

**First lesson:** 06

## Recall

The proportion of actual examples of a class that the model successfully identifies.

**In TIL:** In Lesson 6, recall matters when missing positive examples is especially costly.

**Example:** Of all real complaints, how many were detected.

**First lesson:** 06

## F1-score

The harmonic mean of precision and recall.

**In TIL:** In Lesson 6, F1-score is introduced as a way to balance both metrics.

**Example:** Useful when precision and recall must be considered together.

**First lesson:** 06

## Macro average

The unweighted mean of a metric computed separately for each class.

**In TIL:** In Lesson 6, macro average gives equal weight to each class.

**Example:** Mean of class F1-scores without weighting by class size.

**First lesson:** 06

## Weighted average

A metric average weighted by the number of examples in each class.

**In TIL:** In Lesson 6, weighted average is compared with macro average for differently sized classes.

**Example:** Larger classes contribute more to the average.

**First lesson:** 06

## Cross-validation

An evaluation strategy that splits training data into multiple parts and rotates which parts are used for training and validation.

**In TIL:** In Lesson 7, cross-validation allows configuration comparison without using the final test set.

**Example:** 3-fold cross-validation.

**First lesson:** 07

## Hyperparameter

A configuration set before training that controls the behavior of an algorithm or pipeline.

**In TIL:** In Lesson 7, ngram_range, min_df, and alpha are tuned hyperparameters.

**Example:** classifier__alpha equal to 0.5 or 1.0.

**First lesson:** 07

## Grid Search

A search strategy that systematically evaluates predefined combinations of hyperparameters.

**In TIL:** In Lesson 7, GridSearchCV combines Grid Search and cross-validation to select configurations.

**Example:** Testing different ngram_range, min_df, and alpha values.

**First lesson:** 07

## Overfitting

A situation in which a model or selection process fits observed data too closely and loses generalization ability.

**In TIL:** In Lesson 7, repeatedly consulting the test set during tuning is presented as a risk of test-set overfitting.

**Example:** Repeatedly choosing configurations based on the final test score.

**First lesson:** 07

## Token

A unit produced by segmenting text for computational processing.

**In TIL:** In Lesson 2, we begin by treating words as tokens, although other techniques may use subwords or characters.

**Example:** In "excellent service", excellent and service may be tokens.

**First lesson:** 02

## Tokenization

The process of splitting text into smaller units called tokens.

**In TIL:** In Lesson 2, we compare a simple split strategy with regular-expression tokenization.

**Example:** '"excellent service" becomes ["excellent", "service"].'

**First lesson:** 02

## Text normalization

A set of transformations used to reduce superficial text variation while preserving information relevant to the problem.

**In TIL:** In Lesson 2, lowercasing and trimming whitespace are used as simple examples.

**Example:** '" SERVICE " becomes "service".'

**First lesson:** 02

## Regular expression

A compact pattern language used to locate, validate, or extract character sequences.

**In TIL:** In Lesson 2, Python's standard re library is used to extract tokens with a simple pattern.

**Example:** re.findall(r"\\b\\w+\\b", text).

**First lesson:** 02

## N-gram

A sequence of n consecutive tokens used as a unit of text representation.

**In TIL:** In Lesson 8, n-grams preserve some local context that is lost when using only isolated words.

**Example:** In "did not like", "not like" can be a bigram.

**First lesson:** 08

## Unigram

An n-gram consisting of a single token.

**In TIL:** In Lesson 8, unigrams represent the traditional isolated-word case.

**Example:** "service" is a unigram.

**First lesson:** 08

## Bigram

An n-gram consisting of two consecutive tokens.

**In TIL:** In Lesson 8, bigrams show how combinations such as "not like" can become explicit features.

**Example:** "not like" is a bigram.

**First lesson:** 08

## Trigram

An n-gram consisting of three consecutive tokens.

**In TIL:** In Lesson 8, trigrams illustrate the gain in context and the increase in dimensionality.

**Example:** "did not like" is a trigram.

**First lesson:** 08

## Dimensionality

The number of dimensions or features used to represent data.

**In TIL:** In Lesson 8, adding bigrams and trigrams increases the number of columns in the text matrix.

**Example:** A vocabulary with 5000 features produces a 5000-dimensional representation.

**First lesson:** 08

## Embedding

A learned vector representation that maps entities such as words into a continuous numerical space.

**In TIL:** In Lesson 9, words stop occupying exclusive dimensions and are represented by dense vectors.

**Example:** service may be represented by [0.18, -0.42, 0.77, ...].

**First lesson:** 09

## Dense vector

A vector in which most positions contain informative values, unlike sparse representations dominated by zeros.

**In TIL:** In Lesson 9, word embeddings are relatively low-dimensional dense vectors.

**Example:** "[0.18, -0.42, 0.77, 0.11]."

**First lesson:** 09

## Distributed representation

A representation in which information is not concentrated in a single dimension but distributed across multiple vector dimensions.

**In TIL:** In Lesson 9, lexical meaning is approximated by distributed patterns learned from context.

**Example:** Similar words may share nearby patterns across many dimensions.

**First lesson:** 09

## Cosine similarity

A similarity measure based on the angle between two vectors.

**In TIL:** In Lesson 9, it is used to compare word embeddings.

**Example:** Vectors pointing in very similar directions have similarity close to 1.

**First lesson:** 09

## Word2Vec

A family of neural methods that learns word embeddings from occurrence contexts.

**In TIL:** In Lesson 9, a small Word2Vec model is trained with gensim for observation.

**Example:** Skip-gram predicts context words from a central word.

**First lesson:** 09

## FastText

An embedding method that also represents words through subword units.

**In TIL:** In Lesson 9, FastText is introduced as useful for morphological variation and rare words.

**Example:** A word may be composed from several character fragments.

**First lesson:** 09

## Static embedding

An embedding that essentially assigns the same representation to a word regardless of its context.

**In TIL:** In Lesson 9, this limitation prepares the later transition to contextual embeddings.

**Example:** bank receives the same representation in different senses.

**First lesson:** 09

## Contextual embedding

A vector representation whose value depends on the context in which a token appears.

**In TIL:** In Lesson 10, the same word receives different vectors in sentences with different meanings.

**Example:** bank in a financial context and bank in a river context.

**First lesson:** 10

## Attention

A mechanism that computes relevance weights between sequence elements to combine contextual information.

**In TIL:** In Lesson 10, attention is introduced as a basis for contextualizing tokens in Transformers.

**Example:** A token may assign greater weight to relevant surrounding words.

**First lesson:** 10

## Self-attention

A form of attention in which elements of the same sequence interact with one another.

**In TIL:** In Lesson 10, self-attention lets each token consider other tokens in the sentence.

**Example:** bank considers river in a sentence when building its contextual representation.

**First lesson:** 10

## Transformer

A neural architecture based on attention mechanisms for processing sequences and building contextual representations.

**In TIL:** In Lesson 10, Transformers are introduced as the foundation of many modern language models.

**Example:** BERT and many autoregressive models use Transformer architecture.

**First lesson:** 10

## Subword tokenization

A strategy that splits words into smaller reusable units to reduce vocabulary and rare-word problems.

**In TIL:** In Lesson 10, subwords are introduced as common units in Transformer tokenizers.

**Example:** A rare word may be split into fragments known by the vocabulary.

**First lesson:** 10

## Pretrained model

A model that has already been trained on a large dataset before being reused for another task.

**In TIL:** In Lesson 10, a pretrained encoder is used only for inference and contextual embedding observation.

**Example:** distilbert-base-uncased loaded to extract representations.

**First lesson:** 10

## Fine-tuning

The process of adapting a pretrained model to a specific task using labeled data from the new task.

**In TIL:** In Lesson 11, a multilingual Transformer is fine-tuned to classify messages into three categories.

**Example:** Adapting a pretrained encoder to predict question, complaint, or praise.

**First lesson:** 11

## Transfer learning

A strategy that reuses knowledge learned in one task or domain to accelerate or improve learning in another task.

**In TIL:** In Lesson 11, pretrained linguistic knowledge is transferred to message classification.

**Example:** Reusing BERT instead of training a language model from scratch.

**First lesson:** 11

## Sequence classification

A task in which an entire text sequence receives a class or label.

**In TIL:** In Lesson 11, each message receives one of the labels question, complaint, or praise.

**Example:** Classifying a customer-service message into a category.

**First lesson:** 11

## Epoch

One complete pass of the training algorithm through all examples in the training set.

**In TIL:** In Lesson 11, a single epoch is used to keep the experiment lightweight and didactic.

**Example:** num_train_epochs=1.

**First lesson:** 11

## Batch

A small group of examples processed together during a training step.

**In TIL:** In Lesson 11, batch size controls how many messages are processed in each step.

**Example:** per_device_train_batch_size=4.

**First lesson:** 11

## Learning rate

A hyperparameter that controls the size of weight updates during training.

**In TIL:** In Lesson 11, a small rate is used for fine-tuning a pretrained model.

**Example:** learning_rate=2e-5.

**First lesson:** 11

## Tokenizer

A component that converts text into units and numerical identifiers compatible with a model vocabulary.

**In TIL:** In Lesson 11, the tokenizer prepares messages for Transformer input.

**Example:** AutoTokenizer.from_pretrained(...).

**First lesson:** 11

## Baseline

A reference model or result used to compare more complex approaches.

**In TIL:** In Lesson 12, classical models provide a reference for deciding whether Transformer complexity is justified.

**Example:** TF-IDF + LinearSVC can serve as a strong baseline for text classification.

**First lesson:** 12

## Logistic Regression

A discriminative linear model used for classification by estimating class-associated scores.

**In TIL:** In Lesson 12, it is compared with Naive Bayes and LinearSVC using the same TF-IDF representation.

**Example:** LogisticRegression(max_iter=1000).

**First lesson:** 12

## LinearSVC

A linear SVM classifier that seeks a decision boundary with a wide margin between classes.

**In TIL:** In Lesson 12, it is used as a strong baseline for high-dimensional text spaces.

**Example:** LinearSVC(random_state=42).

**First lesson:** 12

## Margin

The distance between a decision boundary and the nearest examples in margin-based models.

**In TIL:** In Lesson 12, it helps explain how LinearSVC works.

**Example:** SVMs seek to separate classes with a wide margin.

**First lesson:** 12

## Coefficient

A weight learned by a linear model indicating a feature's contribution to the decision.

**In TIL:** In Lesson 12, LinearSVC coefficients are inspected to identify features strongly associated with classes.

**Example:** A large positive coefficient may favor a specific class.

**First lesson:** 12

## False Positive

A truly negative case incorrectly classified as positive.

**In TIL:** In Lesson 13, false positives are linked to the cost of incorrect alerts and unnecessary reviews.

**Example:** A legitimate transaction flagged as fraud.

**First lesson:** 13

## False Negative

A truly positive case incorrectly classified as negative.

**In TIL:** In Lesson 13, false negatives represent important cases the system failed to detect.

**Example:** A fraudulent transaction classified as legitimate.

**First lesson:** 13

## Specificity

The proportion of truly negative cases correctly identified as negative.

**In TIL:** In Lesson 13, it complements recall by describing behavior on the negative class.

**Example:** TN / (TN + FP).

**First lesson:** 13

## Balanced Accuracy

A metric that balances performance across classes, reducing the effect of class imbalance.

**In TIL:** In Lesson 13, it is introduced as an alternative to plain accuracy in imbalanced settings.

**Example:** In binary classification, it can be seen as the mean of recall and specificity.

**First lesson:** 13

## Support

The number of true examples belonging to a class in an evaluated dataset.

**In TIL:** In Lesson 13, support helps explain why weighted averages may be dominated by larger classes.

**Example:** A class with 900 examples has much more support than a class with 20.

**First lesson:** 13

## Decision Threshold

A cutoff used to convert a score or probability into a class decision.

**In TIL:** In Lesson 13, changing the threshold demonstrates the trade-off between precision and recall.

**Example:** score >= 0.50 implies the positive class.

**First lesson:** 13

## Abstention Rate

The proportion of cases where a system avoids making an automatic decision and routes the case elsewhere.

**In TIL:** In Lesson 13, it appears as an operational indicator alongside quality and latency.

**Example:** The model abstains on 8% of cases and sends them to human review.

**First lesson:** 13

## Didactic proxy

A simplified representation used to approximate a real concept, cost, behavior, or consequence for learning purposes without claiming to reproduce the full complexity of the original phenomenon.

**In TIL:** In Lesson 13 and the Metric Scenario Lab, monetary values assigned to errors may act as didactic proxies to make trade-offs visible and comparable. They should not be confused with a complete valuation of human, ethical, social, or regulatory consequences.

**Example:** Assigning R$ 500 to a false negative in a medical simulation can help compare scenarios, but that amount does not represent the value of a human life or exhaust the impact of a missed diagnosis.

**First lesson:** 13

## Trade-off

A situation in which improving one dimension of a decision tends to worsen another, requiring a balance between objectives that cannot all be maximized simultaneously.

**In TIL:** In Lesson 13, lowering a decision threshold may increase recall and reduce false negatives, but it may also increase false positives and reduce precision. The best point depends on context, costs, and system goals.

**Example:** In medical triage, accepting more false positives may be a reasonable trade-off if it significantly reduces the risk of missing seriously ill patients.

**First lesson:** 13

## Harmonic Mean

A type of mean that gives relatively greater influence to smaller values and is therefore useful when a result should be considered strong only if all combined components are also strong.

**In TIL:** In F1-score, the harmonic mean combines Precision and Recall and penalizes imbalance: one very high metric does not easily compensate for the other being very low.

**Example:** With Precision 0.90 and Recall 0.30, the arithmetic mean is 0.60 while F1, based on the harmonic mean, is 0.45.

**First lesson:** 13

## Model Routing

A strategy that decides which model, tool, or execution path should receive each input based on criteria such as difficulty, confidence, cost, latency, or risk.

**In TIL:** In Lesson 13C, the router can keep simple cases on the economical model and send low-confidence cases to a stronger layer.

**Example:** A short unambiguous message may be classified by the baseline while an ambiguous case is routed to the Transformer.

**First lesson:** 13C

## Model Orchestration

Coordination of multiple models and processing stages in one workflow, including routing rules, evaluation, review, fallback, and escalation.

**In TIL:** Lesson 13C compares single, cascade, and critique strategies to show that the system can matter more than an isolated model.

**Example:** An economical model produces the first answer, a gate evaluates quality, and a premium model is invoked only when needed.

**First lesson:** 13C

## Quality Gate

An evaluation rule or mechanism that decides whether an output has sufficient quality to be accepted or must be rejected, revised, or escalated.

**In TIL:** In the 13C simulator, making the gate stricter increases the share of cases sent to the premium layer and changes quality, cost, and latency.

**Example:** If classifier confidence falls below 0.70, the case may be sent to a stronger model or human review.

**First lesson:** 13C

## Escalation Rate

The proportion of cases that leave the initial layer and are sent to a more expensive, slower, more specialized, or human stage.

**In TIL:** In Lesson 13C, escalation rate is a key operational metric for understanding how much the cascade actually uses the premium layer.

**Example:** A 25% escalation rate means one in four cases goes beyond the initial model.

**First lesson:** 13C

## Utility Function

A function that combines different objectives into a common score to make the priorities used in a decision explicit.

**In TIL:** The 13C simulator uses a simple function that rewards quality and penalizes cost and latency, with weights chosen by the learner.

**Example:** U = wq·Q − wc·C − wl·L can compare systems when quality, cost, and latency have different importance.

**First lesson:** 13C

## Compound AI System

An AI system composed of multiple coordinated components such as models, tools, retrievers, rules, verifiers, and human stages.

**In TIL:** Lesson 13C expands evaluation from an isolated model to the whole system, including routing, gates, cost, latency, and review.

**Example:** A baseline classifies first, a Transformer handles difficult cases, and a human reviews critical situations.

**First lesson:** 13C

## Cost per Inference

The cost associated with processing one input through the system, potentially including compute, tokens, API calls, infrastructure, and human stages.

**In TIL:** In 13C, cost may be provided as currency or a relative index as long as the unit is consistent across compared systems.

**Example:** If one thousand classifications cost R$ 12 in compute resources, the average cost per inference is R$ 0.012.

**First lesson:** 13C

## Large Language Model (LLM)

A large-scale language model trained on large amounts of data to learn statistical language patterns and perform tasks such as text generation, transformation, and analysis.

**In TIL:** In Lesson 14, an LLM is treated as a model class with broad generative capability, not as an automatic replacement for classifiers, encoders, or rules.

**Example:** An LLM can receive an instruction and produce a natural-language summary.

**First lesson:** 14

## Autoregressive Model

A model that produces a sequence by estimating the distribution of the next element from the elements already present in the context.

**In TIL:** In Lesson 14, text generation is introduced as repeated next-token prediction: the selected token becomes part of the context for the next step.

**Example:** After the context “The service was”, the model estimates probabilities for possible next tokens.

**First lesson:** 14

## Prompt

Text or a set of instructions and data provided to a model as part of the context to guide a response or generation.

**In TIL:** In Lesson 14, a prompt is treated as contextual model input, not as a guarantee of correct behavior.

**Example:** “Summarize the support interaction in three sentences” is an instruction that can be part of a prompt.

**First lesson:** 14

## Context

The set of tokens and information available to the model when it computes its next output.

**In TIL:** In Lesson 14, context may include instructions, examples, user text, and tokens already generated.

**Example:** An instruction, a document excerpt, and a partial answer can coexist in the context.

**First lesson:** 14

## Context Window

The amount of context a model can consider in one execution, usually expressed as a number of tokens.

**In TIL:** In Lesson 14, context window connects model capability with cost, latency, and the need to select relevant information.

**Example:** A text longer than the available context window must be reduced, chunked, or handled through another strategy.

**First lesson:** 14

## Logits

Unnormalized numerical scores produced by a model before being converted into probabilities.

**In TIL:** In Lesson 14, didactic logits are transformed with softmax to visualize a distribution over possible next tokens.

**Example:** The values 2.2, 1.5, and 0.7 can be logits associated with three candidate tokens.

**First lesson:** 14

## Generation

The process of producing an output sequence from a model, often by choosing successive tokens conditioned on context.

**In TIL:** In Lesson 14, generation is contrasted with classification to show that producing new text is a different capability from choosing a class.

**Example:** Producing a free-form summary from a conversation is a generation task.

**First lesson:** 14

## Greedy Decoding

A decoding strategy that selects the highest-probability token at each step.

**In TIL:** In Lesson 14, greedy decoding provides a deterministic reference for comparison with sampling strategies.

**Example:** If “great” has the highest probability, greedy decoding selects “great” as the next token.

**First lesson:** 14

## Sampling

A selection strategy in which the next token is drawn from a probability distribution, possibly modified by decoding parameters.

**In TIL:** In Lesson 14, sampling is used to show why two generations can diverge even from the same context.

**Example:** Tokens with probabilities 0.6 and 0.3 can both be selected in different runs.

**First lesson:** 14

## Temperature

A decoding parameter that changes the concentration of the distribution used to select tokens.

**In TIL:** In Lesson 14, temperature is interpreted probabilistically: lower values tend to concentrate the distribution while higher values tend to spread it.

**Example:** Applying softmax(logits / temperature) with a lower temperature can increase the dominance of the most likely token.

**First lesson:** 14

## Top-k

A decoding strategy that restricts selection to the k highest-probability tokens at a generation step.

**In TIL:** In Lesson 14, top-k shows how to limit the candidate set without confusing sampling restriction with a quality guarantee.

**Example:** With top-k = 2, only the two most likely tokens remain candidates for the next step.

**First lesson:** 14

## Top-p

A decoding strategy that keeps the smallest set of tokens whose cumulative probability reaches a threshold p.

**In TIL:** In Lesson 14, top-p is introduced as an adaptive candidate filter, also known as nucleus sampling.

**Example:** With top-p = 0.80, the set grows until cumulative probability reaches at least 80%.

**First lesson:** 14

## Structured Output

An output generated according to an explicit structure or contract of fields, types, or format that can be validated programmatically.

**In TIL:** In Lesson 14, structured output separates the ability to generate content from the need to verify that a response satisfies an expected schema.

**Example:** A JSON object with sentiment and confidence fields can be validated after generation.

**First lesson:** 14

## Hallucination

A term used for generated outputs that contain claims unsupported by the context, available evidence, or relevant facts, even when they sound plausible.

**In TIL:** In Lesson 14, the term is used cautiously and does not replace analysis of specific failure types such as invalid format, constraint loss, or factual error.

**Example:** A model stating a fact that is absent from a provided document can be treated as a form of hallucination.

**First lesson:** 14

## Information Retrieval

The process of locating and ranking potentially relevant items for a query within a collection.

**In TIL:** In Lesson 15, retrieval is studied separately from generation so learners can observe how evidence is found before any response is generated.

**Example:** Finding the most relevant documents for the query “how to request a refund”.

**First lesson:** 15

## Query

A representation of an information need used to search a collection.

**In TIL:** In Lesson 15, a query is compared with documents or chunks to produce scores and a ranking.

**Example:** “what is the refund deadline” is a query over the corpus.

**First lesson:** 15

## Lexical Search

Search based mainly on matching and weighting terms present in the query and documents.

**In TIL:** In Lesson 15, TF-IDF and cosine similarity provide the lexical reference for comparing a query with documents.

**Example:** A query containing “refund” tends to retrieve documents that also contain that term.

**First lesson:** 15

## Semantic Search

Search that compares vector representations to bring items together by meaning rather than only by literal term overlap.

**In TIL:** In Lesson 15, didactic dense vectors illustrate how lexically different expressions can be close in a semantic space.

**Example:** “reset password” and “forgot my credential” can have high similarity even with different wording.

**First lesson:** 15

## Ranking

An ordering of candidates according to a score or relevance criterion for a query.

**In TIL:** In Lesson 15, ranking makes visible which documents or chunks are prioritized by a retrieval method.

**Example:** D2 may rank first because it received the highest score for the refund query.

**First lesson:** 15

## Retrieval Score

A value produced by a retrieval method to represent the relative proximity or relevance between a query and an item.

**In TIL:** In Lesson 15, cosine similarity is used as a score in lexical and semantic examples.

**Example:** A score of 0.62 may rank a document above another with 0.31 for the same query.

**First lesson:** 15

## Top-k Retrieval

Selection of the k highest-ranked items returned by a retrieval system.

**In TIL:** In Lesson 15, retrieval top-k is explicitly distinguished from top-k used in generation decoding.

**Example:** Top-k = 3 returns the three documents with the highest scores for the query.

**First lesson:** 15

## Chunk

A segmented unit of a document used as an independent item for processing or retrieval.

**In TIL:** In Lesson 15, sentences are used as chunks to observe how granularity changes ranking.

**Example:** A sentence about a refund deadline can be a chunk separate from other information in the same document.

**First lesson:** 15

## Chunking

The process of splitting documents into smaller units for indexing, retrieval, or processing.

**In TIL:** In Lesson 15, chunking shows the trade-off between broad context and local retrieval precision.

**Example:** Splitting a long document into sentences before calculating retrieval scores.

**First lesson:** 15

## Overlap

Content shared between adjacent chunks to reduce context loss at segmentation boundaries.

**In TIL:** In Lesson 15, overlap is introduced conceptually as a chunking decision that increases redundancy and index cost.

**Example:** Two consecutive chunks may share the last sentence of the first as the first sentence of the second.

**First lesson:** 15

## Grounding

The practice of tying a response, claim, or decision to explicitly available and retrievable evidence.

**In TIL:** In Lesson 15, grounding is demonstrated without an LLM: the deterministic answer is built only from the retrieved evidence pack.

**Example:** Answering the refund deadline while pointing to the chunk that explicitly contains that information.

**First lesson:** 15

## Evidence Pack

An organized set of retrieved evidence and metadata prepared to support a response, decision, or later system stage.

**In TIL:** In Lesson 15, the evidence pack contains the query, chunk identifier, retrieved text, and retrieval score.

**Example:** An object containing the query, C3, the chunk text, and its similarity score.

**First lesson:** 15

## Retrieval-Augmented Generation (RAG)

An architecture that combines evidence retrieval with generation by placing retrieved information into the context used to produce an answer.

**In TIL:** In Lesson 16, RAG is decomposed into retrieval, evidence selection, context construction, generation, grounding, and evaluation.

**Example:** A question retrieves two relevant passages and the generator produces an answer using only those passages.

**First lesson:** 16

## Generation-only

A configuration in which an answer is produced without an explicit retrieval step over external evidence.

**In TIL:** In Lesson 16, generation-only is used as an architectural baseline for comparison with the RAG flow.

**Example:** Answering a question directly from the prompt without consulting the didactic corpus.

**First lesson:** 16

## Context Construction

The stage that organizes instructions, the query, and retrieved evidence into a structured input for the generator.

**In TIL:** In Lesson 16, the context is shown explicitly so learners can see which passages reach the generation stage.

**Example:** Combining an instruction, retrieved C1 and C2, and the question into one input block.

**First lesson:** 16

## Grounded Answer

An answer whose claim can be traced back to evidence explicitly available in the context or evidence pack.

**In TIL:** In Lesson 16, an answer is considered grounded only when the information used appears in the retrieved evidence.

**Example:** Answering “five business days” and identifying C3 as the source.

**First lesson:** 16

## Groundedness

The degree to which claims in an answer are supported by evidence provided to the system.

**In TIL:** In Lesson 16, groundedness is treated as distinct from fluency or plausibility.

**Example:** An answer may sound good but have low groundedness if it adds facts absent from the evidence pack.

**First lesson:** 16

## Source Attribution

An explicit association between a claim in an answer and the source or passage that supports it.

**In TIL:** In Lesson 16, attribution makes answer provenance auditable and separates correctness from traceability.

**Example:** The answer includes “[C2]” next to the information it uses.

**First lesson:** 16

## Retrieval Failure

A failure in which the retrieval stage does not retrieve the needed evidence or prioritizes unsuitable evidence.

**In TIL:** In Lesson 16, this failure type is separated from later context or generation errors.

**Example:** The corpus contains the answer, but the correct passage does not appear in top-k.

**First lesson:** 16

## Context Failure

A failure in which suitable evidence was retrieved but is organized, truncated, or presented in a way that harms the next stage.

**In TIL:** In Lesson 16, context failure shows that correct retrieval does not guarantee useful context.

**Example:** The correct passage is retrieved but left out of the block given to the generator.

**First lesson:** 16

## Generation Failure

A failure in which the context contains sufficient evidence but the generated output ignores, distorts, or extrapolates beyond that evidence.

**In TIL:** In Lesson 16, generation failure is isolated from retrieval failures to support diagnosis and observability.

**Example:** The context states five business days, but the answer says ten days.

**First lesson:** 16

## Insufficient Evidence

A condition in which the available evidence does not adequately support a specific answer.

**In TIL:** In Lesson 16, the system should recognize this condition and prefer abstention, broader search, or escalation.

**Example:** No retrieved chunk contains information about the requested deadline.

**First lesson:** 16

## Factuality

The degree to which a claim or answer corresponds to relevant facts or reality.

**In TIL:** In Lesson 16, factuality is distinguished from groundedness: an answer can be supported by a source and still be wrong if that source is incorrect or outdated.

**Example:** The answer correctly cites an old document stating ten days even though the current rule is five.

**First lesson:** 16

## Evidence Governance

A set of practices for controlling the origin, authority, validity, freshness, versioning, and use of evidence in a system.

**In TIL:** In Lesson 16, evidence governance explains why technically correct retrieval and grounding do not guarantee factuality.

**Example:** The system only considers current, approved documents with identified sources.

**First lesson:** 16

## Freshness

A property indicating how current and still valid an item of evidence is for the question or decision being considered.

**In TIL:** In Lesson 16, freshness is a governance factor that can make a grounded answer factually wrong when the source is outdated.

**Example:** A policy published in 2024 was replaced by a 2026 version.

**First lesson:** 16

## Authority Level

An indication of the strength or priority of a source for supporting a claim, decision, or policy.

**In TIL:** In Lesson 16, authority level helps distinguish official, secondary, or informal sources when evidence conflicts.

**Example:** A current official policy has priority over an old unreviewed FAQ.

**First lesson:** 16

## Tool Calling

Mechanism by which a system requests execution of an external tool through a structured call.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Function Calling

A form of tool calling in which the external capability is represented as a function with a defined name, arguments, and contract.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Tool Contract

Explicit specification of a tool's name, description, inputs, validation, output, and error semantics.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Input Schema

Structured description of the fields, types, required properties, and constraints accepted by a tool call.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Tool Registry

Structured catalog of available tools, their contracts, and execution mechanisms.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Side Effect

Observable state change caused by an operation beyond its direct return value.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Approval Gate

Control point requiring explicit authorization before a potentially sensitive or irreversible action.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Tool Observability

Ability to record and inspect tool selection, arguments, validation, execution, result, latency, and errors.

**In TIL:** In Lesson 17, the concept is applied to the TIL Tool Registry lab and the transition from answering to structured action.

**Example:** The learner inspects the call, validates arguments, and observes the result or error before the final response.

**First lesson:** 17

## Deterministic Workflow

Execution flow in which the sequence of steps, rules, and transitions is explicitly defined by the system.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Workflow State

Explicit data structure representing a workflow's progress, inputs, outputs, attempts, errors, and decisions.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Retry

Controlled re-attempt to execute a step after a failure considered recoverable.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Idempotency

Property by which repeating an operation with the same input does not produce unintended additional effects.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Checkpoint

Persistent or explicit record of an intermediate state that allows a workflow to be inspected or resumed.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Retryable Error

Failure that may justify an automatic retry under explicit limits and conditions.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Workflow Observability

Ability to inspect steps, state, attempts, latency, errors, checkpoints, and decisions during workflow execution.

**In TIL:** In Lesson 18, the concept is used in the TIL Lesson Release Workflow lab.

**Example:** The learner executes, interrupts, resumes, and observes a deterministic workflow under explicit rules.

**First lesson:** 18

## Typed Decision

Decision represented by an explicit structure with defined fields instead of free text used directly to control execution.

**In TIL:** In Lesson 18, the concept separates decision production, routing policy, and workflow execution.

**Example:** The same choice can proceed to execution, escalation, or human review depending on confidence and configured policy.

**First lesson:** 18

## Decision Contract

Explicit schema defining the fields, types, and expected semantics of a decision consumed by a workflow.

**In TIL:** In Lesson 18, the concept separates decision production, routing policy, and workflow execution.

**Example:** The same choice can proceed to execution, escalation, or human review depending on confidence and configured policy.

**First lesson:** 18

## Confidence-Gated Routing

Strategy in which decision confidence is interpreted by an explicit policy to choose among execution, escalation, or review.

**In TIL:** In Lesson 18, the concept separates decision production, routing policy, and workflow execution.

**Example:** The same choice can proceed to execution, escalation, or human review depending on confidence and configured policy.

**First lesson:** 18

## Routing Policy

Explicit set of rules that transforms decision signals, such as choice and confidence, into an execution route.

**In TIL:** In Lesson 18, the concept separates decision production, routing policy, and workflow execution.

**Example:** The same choice can proceed to execution, escalation, or human review depending on confidence and configured policy.

**First lesson:** 18

## Model Context Protocol (MCP)

Open protocol for standardizing how AI applications discover, access, and invoke capabilities and context exposed by servers.

**In TIL:** In Lesson 19, MCP is studied as a standardized integration layer, separate from workflows and agent autonomy.

**Example:** A host uses an MCP client to discover tools, resources, and prompts from a server without knowing its internal implementation.

**First lesson:** 19

## MCP Host

Application that coordinates the experience and contains or manages one or more MCP clients.

**In TIL:** In Lesson 19, the host is the application that decides how to consume MCP capabilities under its own policies.

**Example:** An AI application keeps an MCP client connected to a TIL teaching server.

**First lesson:** 19

## MCP Client

Component that communicates with an MCP server, discovers capabilities, and performs protocol operations.

**In TIL:** In Lesson 19, Client(mcp) is used in-process to observe discovery and invocation without introducing network transport.

**Example:** The client lists tools and then calls get_lesson_status.

**First lesson:** 19

## MCP Server

Component that exposes capabilities through MCP, such as tools, resources, and prompts.

**In TIL:** In Lesson 19, MCPServer registers deterministic local capabilities with no external side effects.

**Example:** The TIL Lesson Server exposes a tool, a resource, and a prompt.

**First lesson:** 19

## Capability Discovery

Mechanism by which a client inspects capabilities and contracts exposed by a server before using them.

**In TIL:** In Lesson 19, discovery makes tools, resources, prompts, and their metadata visible before invocation.

**Example:** The client runs list_tools() and observes names, descriptions, and input schemas.

**First lesson:** 19

## MCP Tool

Invocable capability representing an operation exposed by an MCP server.

**In TIL:** In Lesson 19, tools preserve explicit contracts for input, validation, execution, and result.

**Example:** get_lesson_status receives lesson_id and returns the simulated status of a lesson.

**First lesson:** 19

## MCP Resource

Addressable content or context that can be read by an MCP client.

**In TIL:** In Lesson 19, resources are distinguished from tools because they represent content rather than an operation.

**Example:** til://lessons/status exposes the simulated lesson status.

**First lesson:** 19

## MCP Prompt

Message template exposed by an MCP server to be selected and rendered by a host or user.

**In TIL:** In Lesson 19, prompts are rendered without calling an external LLM, separating templates from model execution.

**Example:** review_release produces a review message for a release note.

**First lesson:** 19

## Protocol Version

Identifier of a protocol revision defining expected semantics and capabilities between participants.

**In TIL:** In Lesson 19, MCP revision 2026-07-28 is declared explicitly to avoid mixing modern and legacy examples.

**Example:** The client inspects protocol_version before calling capabilities.

**First lesson:** 19

## Transport

Mechanism used to carry communication between client and server without changing the semantic role of capabilities.

**In TIL:** In Lesson 19, in-process is used in the core lab while stdio and Streamable HTTP are introduced conceptually.

**Example:** The same tool can preserve its contract when accessed through a different transport.

**First lesson:** 19

## Authorization

Policy determining whether an authenticated or identified caller may perform an action or access a resource.

**In TIL:** In Lesson 19, authorization is separated from model confidence and from the mere existence of a capability.

**Example:** A tool being available on the server does not imply every caller is authorized to execute it.

**First lesson:** 19
