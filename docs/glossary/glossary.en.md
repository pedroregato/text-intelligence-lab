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
