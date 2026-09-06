# TIL Living Glossary — EN

> Generated from `glossary.yaml`. Do not edit manually as the primary source.

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

**Example:** "excellent service" becomes ["excellent", "service"].

**First lesson:** 02

## Text normalization

A set of transformations used to reduce superficial text variation while preserving information relevant to the problem.

**In TIL:** In Lesson 2, lowercasing and trimming whitespace are used as simple examples.

**Example:** " SERVICE " becomes "service".

**First lesson:** 02

## Regular expression

A compact pattern language used to locate, validate, or extract character sequences.

**In TIL:** In Lesson 2, Python's standard re library is used to extract tokens with a simple pattern.

**Example:** re.findall(r"\\b\\w+\\b", text).

**First lesson:** 02
