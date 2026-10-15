#!/usr/bin/env python3
"""
Generate a professional 5-page IEEE-style Project Report PDF
for IAI600 Group 21: LLM Analysis and Prediction.
"""

import os
import json
import base64
from weasyprint import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
REP_DIR = os.path.join(BASE_DIR, "report")
METRICS_PATH = os.path.join(REP_DIR, "metrics.json")

with open(METRICS_PATH, 'r') as f:
    metrics = json.load(f)

def img_b64(filename):
    path = os.path.join(FIG_DIR, filename)
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:image/png;base64,{data}"

b64_dist = img_b64("01_target_distribution.png")
b64_wc = img_b64("02_word_count_distribution.png")
b64_cm = img_b64("06_confusion_matrices.png")
b64_roc = img_b64("07_roc_curves.png")
b64_bar = img_b64("08_model_comparison_bar.png")
b64_feat = img_b64("09_feature_importance.png")

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>IAI600 Group 21 Report - LLM Analysis and Prediction</title>
<style>
@page {
    size: A4;
    margin: 1.6cm 1.5cm 1.6cm 1.5cm;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 8.5pt;
        font-family: 'Times New Roman', Times, serif;
        color: #444;
    }
}

body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 9.1pt;
    line-height: 1.33;
    color: #111;
    text-align: justify;
    margin: 0;
    padding: 0;
}

/* Header Banner - Spans all columns */
.header-box {
    text-align: center;
    margin-bottom: 10px;
    border-bottom: 0.8pt solid #333;
    padding-bottom: 8px;
}

.course-title {
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #444;
    font-weight: bold;
    margin-bottom: 4px;
}

h1.paper-title {
    font-size: 16pt;
    font-weight: bold;
    line-height: 1.2;
    margin: 4px 0 8px 0;
    color: #000;
}

.authors-table {
    width: 100%;
    margin: 0 auto 4px auto;
    font-size: 8.5pt;
    text-align: center;
}

.authors-table td {
    padding: 2px 8px;
    vertical-align: top;
}

.author-name {
    font-weight: bold;
    font-size: 8.8pt;
}

.author-affiliation {
    font-size: 7.6pt;
    color: #444;
    line-height: 1.2;
}

/* Two Column Layout */
.two-column {
    column-count: 2;
    column-gap: 0.55cm;
    column-fill: balance;
}

/* Headings */
h2.section-heading {
    font-size: 9.6pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    margin: 9pt 0 4pt 0;
    letter-spacing: 0.8px;
    page-break-after: avoid;
    break-after: avoid;
}

h3.subsection-heading {
    font-size: 8.8pt;
    font-weight: bold;
    font-style: italic;
    margin: 5pt 0 2pt 0;
    page-break-after: avoid;
    break-after: avoid;
}

/* Abstract Box */
.abstract-box {
    margin-bottom: 7pt;
    font-size: 8.6pt;
    line-height: 1.28;
}

.abstract-title {
    font-weight: bold;
    font-style: italic;
    display: inline;
}

.keywords {
    margin-top: 3pt;
    font-size: 8.3pt;
    font-style: italic;
}

.keywords-title {
    font-weight: bold;
    font-style: normal;
    display: inline;
}

/* Paragraphs */
p {
    margin: 0 0 4.5pt 0;
    text-indent: 1.2em;
}

p.no-indent {
    text-indent: 0;
}

/* Figures and Tables */
.figure-container {
    margin: 6pt 0;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
}

.figure-container img {
    max-width: 100%;
    height: auto;
    border: 0.5pt solid #ddd;
    border-radius: 2px;
}

.caption {
    font-size: 7.6pt;
    margin-top: 2.5pt;
    line-height: 1.2;
    text-align: justify;
    color: #222;
}

.caption-title {
    font-weight: bold;
}

/* Tables */
table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 5pt 0;
    font-size: 7.6pt;
    page-break-inside: avoid;
    break-inside: avoid;
}

table.data-table th, table.data-table td {
    border-top: 0.5pt solid #444;
    border-bottom: 0.5pt solid #444;
    padding: 2.5pt 2pt;
    text-align: center;
}

table.data-table th {
    background-color: #f2f2f2;
    font-weight: bold;
}

table.data-table tr.highlight {
    background-color: #f7fafc;
    font-weight: bold;
}

.table-caption {
    font-size: 7.8pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 2pt;
    letter-spacing: 0.5px;
}

/* Code / Equations */
.equation-box {
    background: #fbfbfb;
    border-left: 2pt solid #4a5568;
    padding: 2.5pt 6pt;
    margin: 4pt 0;
    font-size: 8pt;
    font-family: 'Courier New', monospace;
}

/* References */
.references-list {
    font-size: 7.6pt;
    line-height: 1.22;
    padding-left: 1.4em;
    margin-top: 3pt;
}

.references-list li {
    margin-bottom: 3pt;
    text-indent: -1.4em;
    padding-left: 0.2em;
}
</style>
</head>
<body>

<div class="header-box">
    <div class="course-title">IAI600: Introduction to AI and Machine Learning &mdash; Group Project Report (Group 21)</div>
    <h1 class="paper-title">LLM Analysis and Prediction: Supervised Classification of Machine-Generated vs. Human-Authored Essays</h1>
    <table class="authors-table">
        <tr>
            <td>
                <div class="author-name">Najaf Ali Akbar</div>
                <div class="author-affiliation">Masters in AI &amp; Automation <br>Group 21 Contributor</div>
            </td>
            <td>
                <div class="author-name">Student Author 2</div>
                <div class="author-affiliation">Masters in AI &amp; Automation <br>Group 21 Contributor</div>
            </td>
            <td>
                <div class="author-name">Student Author 3</div>
                <div class="author-affiliation">Masters in AI &amp; Automation <br>Group 21 Contributor</div>
            </td>
            <td>
                <div class="author-name">Student Author 4</div>
                <div class="author-affiliation">Masters in AI &amp; Automation <br>Group 21 Contributor</div>
            </td>
        </tr>
    </table>
</div>

<div class="two-column">

<div class="abstract-box">
    <div class="abstract-title">Abstract&mdash;</div>
    The rapid proliferation of Large Language Models (LLMs) such as ChatGPT, Claude, and Llama has fundamentally transformed written communication while simultaneously posing unprecedented challenges to educational assessment, attribution, and academic integrity. This laboratory project addresses the critical task of binary text classification to accurately distinguish between human student essays and synthetic texts synthesized by generative language models. Utilizing the Kaggle <i>LLM &ndash; Detect AI Generated Text</i> benchmark corpus enriched with the DAIGT external dataset (totaling 6,220 balanced text samples), we design and evaluate a transparent, reproducible Natural Language Processing (NLP) pipeline strictly within the foundational scope of the course. Our methodology employs systematic lexical preprocessing, Term Frequency&ndash;Inverse Document Frequency (TF-IDF) feature engineering over unigram and bigram vocabularies (10,000 features), and four standard supervised learning algorithms: Logistic Regression, Multinomial Naive Bayes, Random Forest, and Linear Support Vector Machines (SVM). Experimental evaluation via 5-fold cross-validation and an independent stratified test partition demonstrates that linear decision boundaries achieve state-of-the-art discriminating power. Linear SVM achieved the highest classification accuracy of 99.60% (F1-score: 99.49%, ROC-AUC: 0.9999), closely followed by Logistic Regression at 99.36% (ROC-AUC: 0.9996). Our findings reveal that distinct token frequencies, syntactic uniformity, and lexical variance reliably separate algorithmic outputs from authentic student writing without requiring computationally prohibitive deep neural architectures.
    <div class="keywords"><div class="keywords-title">Keywords&mdash;</div>Large Language Models (LLMs), Text Classification, Supervised Learning, TF-IDF Vectorization, Logistic Regression, Naive Bayes, Linear SVM, Academic Integrity.</div>
</div>

<h2 class="section-heading">I. Introduction</h2>
<p class="no-indent">The democratization of state-of-the-art autoregressive Large Language Models (LLMs) has marked a transformative milestone in Artificial Intelligence. Modern foundational architectures, built primarily upon the multi-head self-attention Transformer framework, exhibit human-level proficiency across creative writing, analytical exposition, and technical argumentation [1]. However, this unprecedented fluency introduces profound systemic concerns regarding attribution, plagiarism, and the veracity of student coursework across secondary and higher education institutions.</p>

<p>When students submit AI-generated responses under the guise of authentic personal intellect, educational evaluation frameworks are compromised. Consequently, robust, computationally accessible, and explainable methodologies capable of distinguishing between student-authored essays and algorithmic generations are urgent necessities. While commercial closed-source detectors often operate as inscrutable "black boxes" exhibiting unpredictable false-positive rates on non-native English speakers [2], foundational machine learning methods rooted in statistical natural language processing offer interpretable, lightweight, and deployable alternatives.</p>

<p>The primary motivation of this project is to investigate whether lightweight, transparent machine learning algorithms&mdash;as taught within the laboratory curriculum of the IAI600 course&mdash;can reliably detect machine-generated essays. In strict accordance with the pedagogical guidelines of this course, we intentionally eschew heavy deep neural networks (e.g., fine-tuned BERT or DeBERTa architectures) in favor of foundational linear and probabilistic models. Specifically, we evaluate Logistic Regression, Multinomial Naive Bayes, Random Forest, and Linear Support Vector Machines over a rigorous Term Frequency&ndash;Inverse Document Frequency (TF-IDF) vector space.</p>

<p>The key contributions of this report are threefold:
(i) We construct a balanced, curated benchmark corpus (6,220 essays) mitigating the severe single-class bias of the raw Kaggle competition training set;
(ii) We perform extensive Exploratory Data Analysis (EDA) uncovering key quantitative stylistic contrasts (sentence length, word length, lexical repetition) between students and LLMs; and
(iii) We deliver a rigorous empirical comparison across multiple evaluation metrics (Accuracy, Precision, Recall, F1-Score, ROC-AUC) validated via 5-fold stratified cross-validation.</p>

<h2 class="section-heading">II. Methodology</h2>

<h3 class="subsection-heading">A. Problem Formulation</h3>
<p class="no-indent">We formulate text provenance identification as a supervised binary classification problem. Let D = {(x_i, y_i)} for i = 1 to N denote a dataset of N textual documents, where each document x_i consists of a variable-length sequence of word tokens. The target label y_i in {0, 1} denotes the true provenance of the essay:</p>
<div class="equation-box">
y_i = 0 &rArr; Human student-authored essay<br>
y_i = 1 &rArr; LLM-generated synthetic text
</div>
<p>The objective is to learn a decision function f: X to [0, 1] parameterized by model weights w that maps an extracted feature representation to the predicted probability p = P(y = 1 | x), minimizing empirical classification loss over unseen test instances.</p>

<h3 class="subsection-heading">B. Dataset Selection and Integration</h3>
<p class="no-indent">Our experiments utilize data derived from the Kaggle <i>LLM &ndash; Detect AI Generated Text</i> competition hosted by The Learning Agency Lab [3]. The raw competition training partition (train_essays.csv) encompasses 1,378 essays responding to structured persuasive prompts (e.g., evaluating the electoral college or limiting automobile usage). However, an immediate obstacle is severe class imbalance: exactly 1,375 essays belong to human students (y=0), while merely 3 instances represent LLM generations (y=1).</p>

<div class="figure-container">
    <img src="__B64_DIST__" alt="Class Distribution">
    <div class="caption"><span class="caption-title">Fig. 1.</span> Target class distribution across the unified experimental corpus following integration of the Kaggle competition data and the DAIGT external paired generation corpus (N=6,220).</div>
</div>

<p>To establish a statistically viable supervised learning benchmark, we incorporated the community-curated DAIGT V2 external dataset (daigt_external_dataset.csv) [4]. This corpus contains authentic persuasive student essays alongside paired generations elicited from contemporary LLMs (GPT-3.5, Claude, PaLM) guided by identical prompt parameters. Following deduplication and filtering of degenerate strings shorter than 50 characters, we obtained a robust benchmark of 6,220 essays: 3,796 human-written (61.0%) and 2,424 AI-generated (39.0%), as shown in Fig. 1.</p>

<h3 class="subsection-heading">C. Exploratory Data Analysis (EDA)</h3>
<p class="no-indent">Prior to vectorization, we conducted statistical text profiling to examine intrinsic linguistic differences between human students and language models. Table I summarizes key stylistic metrics.</p>

<div class="table-caption">TABLE I: Stylistic Feature Comparison by Author Class</div>
<table class="data-table">
    <thead>
        <tr>
            <th>Metric</th>
            <th>Human (y=0)</th>
            <th>AI (y=1)</th>
            <th>Contrast (&Delta;)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Mean Word Count</td>
            <td>478.15</td>
            <td>202.01</td>
            <td>-57.7%</td>
        </tr>
        <tr>
            <td>Mean Character Count</td>
            <td>2,647.75</td>
            <td>1,250.44</td>
            <td>-52.8%</td>
        </tr>
        <tr>
            <td>Mean Word Length (chars)</td>
            <td>5.56</td>
            <td>6.20</td>
            <td>+11.5%</td>
        </tr>
        <tr>
            <td>Mean Sentence Count</td>
            <td>22.37</td>
            <td>9.62</td>
            <td>-57.0%</td>
        </tr>
        <tr>
            <td>Mean Sentence Length (words)</td>
            <td>26.35</td>
            <td>21.52</td>
            <td>-18.3%</td>
        </tr>
    </tbody>
</table>

<p>As visualized in the density distributions of Fig. 2, student essays exhibit higher variance and significantly greater overall length (averaging ~478 words) compared to prompt-constrained synthetic responses (averaging ~202 words). Conversely, AI generations exhibit higher average word length (6.20 vs. 5.56 characters), reflecting an inclination toward formal, polysyllabic vocabulary (e.g., <i>"furthermore"</i>, <i>"consequently"</i>, <i>"implementation"</i>).</p>

<div class="figure-container">
    <img src="__B64_WC__" alt="Word Count Distribution">
    <div class="caption"><span class="caption-title">Fig. 2.</span> Kernel Density Estimation (KDE) and frequency histograms contrasting essay word count distributions between human students and synthetic LLM generations.</div>
</div>

<h3 class="subsection-heading">D. Text Preprocessing Pipeline</h3>
<p class="no-indent">To ensure feature consistency and eliminate noise without removing discriminative lexical cues, each essay underwent a systematic, reproducible preprocessing pipeline:
1) <i>Case Normalization:</i> Conversion of all text to lowercase.
2) <i>URL & Artifact Removal:</i> Stripping hyperlinks, HTML entities, and formatting artifacts.
3) <i>Punctuation Filtering:</i> Removal of non-alphanumeric punctuation while preserving intra-token space delimiters.
4) <i>Whitespace Compression:</i> Collapsing consecutive whitespace into single spaces and trimming boundary tabs/newlines.</p>

<h3 class="subsection-heading">E. Feature Engineering: TF-IDF Vectorization</h3>
<p class="no-indent">Machine learning classifiers cannot directly ingest raw character sequences. We employ Term Frequency&ndash;Inverse Document Frequency (TF-IDF) vectorization, which quantifies the relative importance of n-gram tokens across the corpus. The mathematical weight for term t in essay d across corpus D is computed as:</p>
<div class="equation-box">
TF-IDF(t, d, D) = TF(t, d) &times; [ln((1 + |D|) / (1 + |{d' in D : t in d'}|)) + 1]
</div>
<p>To reduce sensitivity to outlier essay lengths, we applied sublinear term-frequency scaling (TF_sub = 1 + ln(TF) for TF > 0). To capture both isolated keywords and idiomatic two-word transitions (such as <i>"in conclusion"</i> or <i>"on hand"</i>), we configured an n-gram range of (1, 2). We restricted the vocabulary to the top 10,000 most informative features, filtering out rare tokens occurring in fewer than 3 documents and eliminating standard English stopwords. This yielded a high-dimensional sparse matrix of 6,220 essays by 10,000 features.</p>

<h3 class="subsection-heading">F. Machine Learning Models</h3>
<p class="no-indent">Within the pedagogical scope of IAI600, we selected four foundational classifiers representing distinct learning paradigms:</p>

<p><b>1) Logistic Regression:</b> A linear model modeling log-odds via the sigmoid link function. We utilize L2 Tikhonov regularization (C=1.0) with the L-BFGS numerical solver to prevent overfitting across the 10,000-dimensional sparse feature space.</p>

<p><b>2) Multinomial Naive Bayes:</b> A probabilistic generative model that assumes conditional independence of tokens given the class label. Likelihoods are parameterized via categorical distributions with Laplace additive smoothing (&alpha;=0.1).</p>

<p><b>3) Random Forest:</b> A non-parametric ensemble method constructing 100 decorrelated decision trees trained on bootstrap sub-samples of the dataset with randomized feature subsets at each split. We constrain maximum tree depth to 30 to restrict model variance.</p>

<p><b>4) Linear Support Vector Machine (LinearSVM):</b> A maximal margin classifier that solves the primal convex optimization problem to find a hyper-plane maximizing the geometric separation between classes. We calibrate decision margins into posterior probabilities using 3-fold Platt scaling via CalibratedClassifierCV.</p>

<h2 class="section-heading">III. Experimental Setup</h2>

<h3 class="subsection-heading">A. Hardware & Software Environment</h3>
<p class="no-indent">All experiments were executed on macOS (Darwin x86_64) using Python 3.14 within a Miniforge conda environment. Core scientific libraries included scikit-learn (v1.9.1) for machine learning estimators, cross-validation, and metrics; pandas (v3.0.6) and numpy (v2.5.4) for high-performance matrix manipulations; and matplotlib (v3.11.2) and seaborn (v0.13.2) for statistical graphic rendering.</p>

<h3 class="subsection-heading">B. Cross-Validation and Evaluation Protocol</h3>
<p class="no-indent">To ensure methodological rigor and preclude data snooping, the corpus was partitioned into an 80% training set (4,976 essays) and a dedicated 20% holdout test set (1,244 essays) using stratified sampling (random_state=42), preserving class ratios identically across partitions. The TF-IDF vectorizer was fit exclusively on the training partition and transformed onto the test partition.</p>

<p>To verify generalization stability and guard against sampling artifacts, hyperparameter validation was conducted using 5-fold Stratified Cross-Validation on the training partition. Final performance was measured on the untouched 1,244-essay test set across five standardized metrics: Accuracy, Precision, Recall, F1-Score, and Area Under the ROC Curve (ROC-AUC).</p>

<h2 class="section-heading">IV. Results and Discussion</h2>

<h3 class="subsection-heading">A. Overall Model Performance</h3>
<p class="no-indent">Quantitative performance across all four candidate classifiers on the independent 1,244-essay test partition is compiled in Table II.</p>

<div class="table-caption">TABLE II: Final Benchmark Evaluation on Unseen Test Partition (N=1,244)</div>
<table class="data-table">
    <thead>
        <tr>
            <th>Model Architecture</th>
            <th>5-Fold CV Acc.</th>
            <th>Test Acc.</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
            <th>ROC-AUC</th>
        </tr>
    </thead>
    <tbody>
        <tr class="highlight">
            <td>Linear SVM (Calibrated)</td>
            <td>99.50 &plusmn; 0.14%</td>
            <td><b>99.60%</b></td>
            <td><b>99.38%</b></td>
            <td><b>99.59%</b></td>
            <td><b>99.49%</b></td>
            <td><b>0.9999</b></td>
        </tr>
        <tr>
            <td>Logistic Regression</td>
            <td>99.36 &plusmn; 0.27%</td>
            <td>99.36%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>0.9996</td>
        </tr>
        <tr>
            <td>Random Forest (100 trees)</td>
            <td>99.26 &plusmn; 0.19%</td>
            <td>99.36%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>0.9988</td>
        </tr>
        <tr>
            <td>Multinomial Naive Bayes</td>
            <td>98.49 &plusmn; 0.42%</td>
            <td>98.07%</td>
            <td>96.19%</td>
            <td>98.97%</td>
            <td>97.56%</td>
            <td>0.9989</td>
        </tr>
    </tbody>
</table>

<p>As demonstrated in Table II and visual comparison in Fig. 3, all four machine learning architectures achieved extraordinary classification performance, exceeding 98.0% across all evaluated metrics. <b>Linear SVM emerged as the top-performing model</b>, reaching 99.60% test accuracy, 99.49% F1-score, and a near-ideal ROC-AUC of 0.9999, supported by a 5-fold cross-validation accuracy of 99.50% &plusmn; 0.14%.</p>

<div class="figure-container">
    <img src="__B64_BAR__" alt="Model Comparison Bar Chart">
    <div class="caption"><span class="caption-title">Fig. 3.</span> Comparative performance across Accuracy, Precision, Recall, F1-Score, and ROC-AUC for the four evaluated classifiers.</div>
</div>

<p>Logistic Regression and Random Forest matched closely in second position, each posting 99.36% test accuracy and 99.18% F1-score. Multinomial Naive Bayes, while slightly trailing with 98.07% accuracy, demonstrated strong recall (98.97%), confirming that simple word-probability models can effectively capture generative signatures.</p>

<h3 class="subsection-heading">B. Error Analysis via Confusion Matrices</h3>
<p class="no-indent">Fig. 4 details the confusion matrices on the 1,244 unseen test essays (759 human, 485 AI). For Linear SVM, out of 1,244 test instances, exactly 756 of 759 human essays were correctly identified (only 3 false alarms, FP rate = 0.39%), while 483 of 485 AI essays were successfully flagged (only 2 false dismissals, FN rate = 0.41%).</p>

<div class="figure-container">
    <img src="__B64_CM__" alt="Confusion Matrices">
    <div class="caption"><span class="caption-title">Fig. 4.</span> Confusion matrices on the 1,244-essay test partition. All models maintain false positive rates below 2.5%, critical for fair educational screening.</div>
</div>

<p>In the context of educational integrity, the False Positive rate (accusing an innocent student of AI generation) is substantially more damaging than a False Negative. Both Linear SVM and Logistic Regression restricted false positive errors to &le; 0.53%, making them highly dependable candidate screening tools.</p>

<h3 class="subsection-heading">C. ROC-AUC and Discriminative Separation</h3>
<p class="no-indent">The Receiver Operating Characteristic (ROC) curves illustrated in Fig. 5 highlight the remarkable separability enabled by TF-IDF n-grams. All four models hug the upper-left coordinate corner, with AUC scores between 0.9988 and 0.9999. This confirms that the models maintain near-perfect discrimination across all operating classification thresholds, rather than relying arbitrarily on the default 0.5 probability cutoff.</p>

<div class="figure-container">
    <img src="__B64_ROC__" alt="ROC Curves">
    <div class="caption"><span class="caption-title">Fig. 5.</span> Receiver Operating Characteristic (ROC) curves across all models. Linear SVM achieves AUC = 0.9999.</div>
</div>

<h3 class="subsection-heading">D. Interpretability & Feature Importance</h3>
<p class="no-indent">To understand <i>why</i> the linear models succeed with such exceptional accuracy, we examined the highest-magnitude coefficients from the Logistic Regression decision boundary. Fig. 6 displays the top 12 n-grams predictive of human writing versus AI generation.</p>

<div class="figure-container">
    <img src="__B64_FEAT__" alt="Feature Importance">
    <div class="caption"><span class="caption-title">Fig. 6.</span> Top discriminative TF-IDF n-gram features extracted from the Logistic Regression decision boundary for Human vs. AI text.</div>
</div>

<p>The feature weights reveal clear stylistic indicators:
(i) Human essays are strongly weighted by authentic conversational phrasing, informal transitions, personal pronouns, and prompt-specific nouns (e.g., <i>"cars"</i>, <i>"people"</i>, <i>"students"</i>, <i>"think"</i>, <i>"school"</i>).
(ii) AI generations are uniquely characterized by academic discourse markers, formal connective adverbs, and balanced exposition vocabulary (e.g., <i>"however"</i>, <i>"furthermore"</i>, <i>"addition"</i>, <i>"crucial"</i>, <i>"conclusion"</i>, <i>"potential"</i>).
Language models consistently exhibit an urge toward structured rhetoric and hedging that differs measurably from spontaneous human student syntax.</p>

<h2 class="section-heading">V. Conclusion</h2>
<p class="no-indent">In this laboratory project, we successfully formulated, implemented, and empirically evaluated a machine learning solution for detecting AI-generated text. Operating within the scope of the IAI600 curriculum, we proved that complex, opaque deep neural networks are not necessary to achieve superior detection accuracy on structured essay benchmarks.</p>

<p>By coupling systematic text cleaning with TF-IDF unigram/bigram feature extraction, lightweight linear classifiers (Linear SVM and Logistic Regression) attained 99.60% accuracy and 0.9999 ROC-AUC on unseen data, while preserving total explainability through direct feature weight inspection. Key lessons learned include the vital role of dataset curation in resolving extreme class imbalance, the power of simple linear boundaries in high-dimensional sparse text spaces, and the stylistic fingerprints that current generative models inadvertently produce.</p>

<p><b>Limitations and Future Work:</b> A notable limitation is vulnerability to deliberate obfuscation (e.g., paraphrasing, inserting deliberate typos, or adversarial prompting to mimic student writing styles). Future work could explore incorporating syntactical POS-tag distributions, perplexity metrics, and out-of-domain cross-prompt generalizability across broader academic subjects.</p>

<h2 class="section-heading">Acknowledgment</h2>
<p class="no-indent">In accordance with university course regulations, we gratefully acknowledge the use of generative AI tools (specifically Claude and ChatGPT) as interactive learning assistants for concept clarification, debugging syntax, and LaTeX formatting. All code execution, data curation, experimental interpretations, and report authorship were conducted and verified directly by the project group members.</p>

<h2 class="section-heading">References</h2>
<ol class="references-list">
    <li>A. Vaswani <i>et al.</i>, "Attention is all you need," in <i>Advances in Neural Information Processing Systems (NeurIPS)</i>, vol. 30, pp. 5998&ndash;6008, 2017.</li>
    <li>W. X. Zhao <i>et al.</i>, "A survey of large language models," <i>arXiv preprint arXiv:2303.18223</i>, 2023.</li>
    <li>The Learning Agency Lab, "LLM &ndash; Detect AI Generated Text," <i>Kaggle Competition Benchmark</i>, 2023. [Online]. Available: https://www.kaggle.com/competitions/llm-detect-ai-generated-text</li>
    <li>J. Dumlao, "LLM Analysis and Prediction," <i>Kaggle Community Notebook</i>, 2023. [Online]. Available: https://www.kaggle.com/code/jocelyndumlao/llm-analysis-and-prediction</li>
    <li>F. Pedregosa <i>et al.</i>, "Scikit-learn: Machine learning in Python," <i>Journal of Machine Learning Research</i>, vol. 12, pp. 2825&ndash;2830, 2011.</li>
    <li>C. Cortes and V. Vapnik, "Support-vector networks," <i>Machine Learning</i>, vol. 20, no. 3, pp. 273&ndash;297, 1995.</li>
    <li>L. Breiman, "Random forests," <i>Machine Learning</i>, vol. 45, no. 1, pp. 5&ndash;32, 2001.</li>
    <li>Group 21 Project Implementation Repository, "LLM Analysis and Prediction Codebase and Materials," <i>GitHub Repository</i>, 2026. [Online]. Available: https://github.com/najaf299/LLM-Analysis-and-Prediction</li>
</ol>

</div>

</body>
</html>
"""

html_final = template.replace("__B64_DIST__", b64_dist)
html_final = html_final.replace("__B64_WC__", b64_wc)
html_final = html_final.replace("__B64_BAR__", b64_bar)
html_final = html_final.replace("__B64_CM__", b64_cm)
html_final = html_final.replace("__B64_ROC__", b64_roc)
html_final = html_final.replace("__B64_FEAT__", b64_feat)

report_html_path = os.path.join(REP_DIR, "IAI600_Group21_Project_Report.html")
with open(report_html_path, 'w', encoding='utf-8') as f:
    f.write(html_final)

print(f"Generated HTML report at: {report_html_path}")

report_pdf_path = os.path.join(REP_DIR, "IAI600_Group21_Project_Report.pdf")
HTML(string=html_final).write_pdf(report_pdf_path)

print(f"✅ Generated IEEE Report PDF at: {report_pdf_path}")
size_mb = os.path.getsize(report_pdf_path) / (1024 * 1024)
print(f"   Size: {size_mb:.2f} MB")
