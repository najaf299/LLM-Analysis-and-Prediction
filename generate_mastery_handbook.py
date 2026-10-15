#!/usr/bin/env python3
"""
Refined Student Mastery & Operations Handbook PDF Generator
for IAI600 Group 21: LLM Analysis and Prediction.

Fixes applied:
- Clarified that the Group Project requires ONLY report submission (NO presentation required)
- Clarified that the Individual Oral Demonstration covers Labs 1, 2, 3, and 5
- Corrected feature words to match Fig. 6 (potential, provide, ultimately vs want, good, like)
- Fixed code wrapping in CSS (pre { white-space: pre-wrap; word-break: break-all; }) so code is not clipped
- Stated accurately that Random Forest matched Logistic Regression at 99.36% test accuracy
- Added Length-Only Baseline discussion (95.42% accuracy)
"""

import os
from weasyprint import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSS = """
@page {
    size: A4;
    margin: 1.8cm 1.6cm 1.8cm 1.6cm;
    @bottom-center {
        content: "IAI600 Group 21 Mastery Handbook — Page " counter(page) " of " counter(pages);
        font-size: 8.5pt;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #718096;
    }
}

body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 9.8pt;
    line-height: 1.52;
    color: #2d3748;
    margin: 0;
    padding: 0;
}

.header-banner {
    background: linear-gradient(135deg, #1a365d 0%, #2b6cb0 100%);
    color: white;
    padding: 20px 22px;
    border-radius: 8px;
    margin-bottom: 20px;
}

.header-banner h1 {
    font-size: 19pt;
    margin: 0 0 6px 0;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #ffffff;
    border-bottom: none;
    padding-bottom: 0;
}

.header-banner p {
    font-size: 10pt;
    margin: 0;
    color: #ebf8ff;
    line-height: 1.4;
}

.badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.2);
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 8.5pt;
    font-weight: bold;
    margin-top: 8px;
}

h2 {
    font-size: 13.5pt;
    color: #1a365d;
    border-bottom: 2px solid #bee3f8;
    padding-bottom: 5px;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h3 {
    font-size: 11pt;
    color: #2b6cb0;
    margin-top: 14px;
    margin-bottom: 5px;
    page-break-after: avoid;
}

p {
    margin: 0 0 7pt 0;
}

ul, ol {
    margin: 5pt 0 10pt 0;
    padding-left: 20px;
}

li {
    margin-bottom: 4px;
}

code {
    background-color: #edf2f7;
    color: #c53030;
    padding: 1px 5px;
    border-radius: 3px;
    font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
    font-size: 8.8pt;
}

pre {
    background-color: #1a202c;
    color: #e2e8f0;
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 8.5pt;
    line-height: 1.4;
    margin: 6pt 0 10pt 0;
    white-space: pre-wrap;
    word-break: break-all;
    page-break-inside: avoid;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
}

.callout {
    padding: 10px 14px;
    margin: 10pt 0;
    border-radius: 6px;
    border-left: 4px solid;
    page-break-inside: avoid;
}

.callout-blue {
    background-color: #ebf8ff;
    border-color: #3182ce;
    color: #2b6cb0;
}

.callout-green {
    background-color: #f0fff4;
    border-color: #38a169;
    color: #276749;
}

.callout-yellow {
    background-color: #fffaf0;
    border-color: #dd6b20;
    color: #9c4221;
}

.callout-title {
    font-weight: bold;
    font-size: 9.8pt;
    margin-bottom: 3px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 8pt 0 12pt 0;
    font-size: 8.6pt;
    page-break-inside: avoid;
}

th {
    background-color: #2b6cb0;
    color: white;
    padding: 6px 9px;
    text-align: left;
    font-weight: 600;
    border: 1px solid #2b6cb0;
}

td {
    padding: 5px 9px;
    border: 1px solid #cbd5e0;
}

tr:nth-child(even) {
    background-color: #f7fafc;
}

.qa-card {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #2b6cb0;
    border-radius: 4px;
    padding: 9px 12px;
    margin: 8pt 0;
    page-break-inside: avoid;
}

.qa-q {
    font-weight: bold;
    color: #1a365d;
    font-size: 9.6pt;
    margin-bottom: 4px;
}

.qa-a {
    color: #2d3748;
    font-size: 9.1pt;
}
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>IAI600 Group 21: Student Mastery Handbook</title>
<style>""" + CSS + """</style>
</head>
<body>

<div class="header-banner">
    <div class="badge">IAI600: Introduction to AI &amp; Machine Learning</div>
    <h1>Student Mastery &amp; Operations Handbook</h1>
    <p><b>Group 21 Project:</b> LLM Analysis and Prediction (Detecting AI-Generated Text)<br>
    A complete guide to understanding the codebase, report contents, files, and operations.</p>
</div>

<div class="callout callout-yellow">
    <div class="callout-title">⚠️ Important Course Rules Clarification:</div>
    <ul>
        <li><b>Group Project:</b> ONLY the written report (maximum 5 pages) must be submitted before November 2. <b>No oral presentation or demonstration of the project is required.</b></li>
        <li><b>Individual Oral Demonstration:</b> Covers <b>Labs 1, 2, 3, and 5 ONLY</b> (Labs 4, 6, and 7 are excluded). Each student must demonstrate running code and answer technical questions on Data Preprocessing, Regression, Classification, and Clustering individually.</li>
    </ul>
</div>

<h2>Table of Contents</h2>
<ol>
    <li><b>Project Files &amp; Directory Architecture</b> &mdash; Where everything is and what each file does</li>
    <li><b>Code Walkthrough (Step-by-Step for Beginners)</b> &mdash; Line-by-line understanding of every cell</li>
    <li><b>Report Breakdown &amp; Interpretations</b> &mdash; Understanding tables, graphs, and claims</li>
    <li><b>How to Run, Save, and Close Everything</b> &mdash; Step-by-step terminal &amp; browser commands</li>
    <li><b>Understanding the High Accuracy &amp; Baseline Analysis</b> &mdash; Why the model scores 99.6%</li>
</ol>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>1. Project Files &amp; Directory Architecture</h2>
<p>Your project is self-contained inside <code>LLM-Analysis-Prediction/</code> (and mirrored in <code>~/Downloads/handson-ml3-main/Group21_LLM_Project/</code>). Here is what every folder and file contains:</p>

<table>
    <thead>
        <tr>
            <th>Directory / File</th>
            <th>Type</th>
            <th>What It Does &amp; Why It Exists</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>data/train_essays.csv</code></td>
            <td>Raw Data</td>
            <td>Original Kaggle competition dataset (1,378 essays: 1,375 human, only 3 AI).</td>
        </tr>
        <tr>
            <td><code>data/daigt_external_dataset.csv</code></td>
            <td>Raw Data</td>
            <td>Paired corpus containing 2,421 student essays and 2,421 matching ChatGPT generations.</td>
        </tr>
        <tr>
            <td><code>data/balanced_essays.csv</code></td>
            <td>Processed Data</td>
            <td><b>Unified, cleaned dataset (6,220 essays: 3,796 human, 2,424 AI)</b> created by merging both sources to fix the class imbalance.</td>
        </tr>
        <tr>
            <td><code>notebooks/llm_analysis_and_prediction.ipynb</code></td>
            <td>Jupyter Notebook</td>
            <td><b>Your main interactive notebook.</b> Contains all markdown explanations, live Python code, printed outputs, and embedded plots.</td>
        </tr>
        <tr>
            <td><code>figures/</code></td>
            <td>Visualizations</td>
            <td>Folder containing 9 publication-grade figures (target distribution, word lengths, confusion matrices, ROC curves, feature weights).</td>
        </tr>
        <tr>
            <td><code>report/IAI600_Group21_Project_Report.pdf</code></td>
            <td>Submission Document</td>
            <td><b>Your official 3-page IEEE two-column report</b> strictly complying with course guidelines (under 5 pages).</td>
        </tr>
        <tr>
            <td><code>report/metrics.json</code></td>
            <td>Results Data</td>
            <td>JSON file storing the exact numerical metrics (Accuracy, F1, ROC-AUC, baseline scores, top features) computed by your models.</td>
        </tr>
        <tr>
            <td><code>run_pipeline.py</code></td>
            <td>Executable Script</td>
            <td>Standalone Python script that runs the entire ML pipeline from the terminal in ~20 seconds using leak-free scikit-learn Pipelines.</td>
        </tr>
        <tr>
            <td><code>generate_report_pdf.py</code></td>
            <td>Utility Script</td>
            <td>Compiles the HTML report and embeds all high-res figures into the final IEEE PDF.</td>
        </tr>
        <tr>
            <td><code>README.md</code></td>
            <td>Documentation</td>
            <td>Repository overview, installation commands, results table, and citations.</td>
        </tr>
        <tr>
            <td><code>LICENSE</code></td>
            <td>License</td>
            <td>Official MIT License for the open-source codebase.</td>
        </tr>
    </tbody>
</table>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>2. Code Walkthrough (Explained for Beginners)</h2>
<p>The entire project is organized into clear logical steps:</p>

<h3>Step 1: Imports &mdash; Gathering the Tools</h3>
<pre><code>import pandas as pd             # Used to load, filter, and inspect CSV tables
import numpy as np              # Used for fast mathematical matrix calculations
import matplotlib.pyplot as plt # Used to draw line plots, bar charts, and histograms
import seaborn as sns           # Makes plots look modern with smooth KDE density curves
from sklearn.pipeline import Pipeline                        # Chains vectorizer and model leak-free
from sklearn.feature_extraction.text import TfidfVectorizer # Converts text words into numbers
from sklearn.linear_model import LogisticRegression          # Classification algorithm
from sklearn.naive_bayes import MultinomialNB                # Generative probability algorithm
from sklearn.ensemble import RandomForestClassifier          # Ensemble decision tree algorithm
from sklearn.svm import LinearSVC                            # Maximum margin classification algorithm</code></pre>

<h3>Step 2: Loading &amp; Merging Datasets</h3>
<p>We read both CSV files. In <code>train_essays.csv</code>, student essays have <code>generated = 0</code>. In <code>daigt_external_dataset.csv</code>, student essays are labeled <code>0</code> and ChatGPT responses (source text) are labeled <code>1</code>. We combine them using <code>pd.concat</code>, retaining all 6,220 essays.</p>

<h3>Step 3: Exploratory Data Analysis (EDA)</h3>
<ul>
    <li><b>Word count per essay:</b> Students wrote longer essays (~481 words) than the prompt-constrained ChatGPT essays (~204 words).</li>
    <li><b>True average word length (excluding spaces):</b> AI essays used longer, more polysyllabic words (5.01 letters/word vs. 4.32 letters/word for students).</li>
    <li><b>Sentence count:</b> Student essays contained more sentences (~22 vs. ~10).</li>
</ul>

<h3>Step 4: Text Cleaning (Preprocessing)</h3>
<pre><code>def preprocess_text(text):
    text = text.lower()                                    # 1. Lowercase all letters
    text = re.sub(r'http\S+|www\S+', '', text)             # 2. Remove web links
    text = re.sub(r'[^a-z0-9\s]', ' ', text)               # 3. Strip punctuation
    text = re.sub(r'\s+', ' ', text).strip()              # 4. Normalize spaces
    return text</code></pre>

<h3>Step 5: TF-IDF Feature Extraction</h3>
<ul>
    <li><b>TF (Term Frequency):</b> How often a term appears in an essay.</li>
    <li><b>IDF (Inverse Document Frequency):</b> How rare the term is across the entire corpus of 6,220 essays.</li>
    <li><b>Stopword removal:</b> Removes common filler words (<i>"the"</i>, <i>"is"</i>, <i>"however"</i>).</li>
    <li><b>N-gram range (1, 2):</b> Extracts single words and adjacent two-word combinations.</li>
</ul>

<h3>Step 6: Train/Test Split &amp; Pipeline Cross-Validation</h3>
<ul>
    <li><b>80% Training (4,976 essays) / 20% Testing (1,244 essays).</b></li>
    <li><code>Pipeline</code> ensures that the TF-IDF vectorizer is fitted strictly on training data during each of the 5 cross-validation folds, preventing any data leakage.</li>
</ul>

<h3>Step 7: The 4 Machine Learning Models &amp; Results</h3>
<table>
    <thead>
        <tr>
            <th>Model Architecture</th>
            <th>5-Fold CV Accuracy</th>
            <th>Test Accuracy</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
            <th>ROC-AUC</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Linear SVM (Calibrated)</b></td>
            <td>99.50% &plusmn; 0.14%</td>
            <td><b>99.60%</b></td>
            <td><b>99.38%</b></td>
            <td><b>99.59%</b></td>
            <td><b>99.49%</b></td>
            <td><b>0.9999</b></td>
        </tr>
        <tr>
            <td><b>Logistic Regression</b></td>
            <td>99.38% &plusmn; 0.26%</td>
            <td>99.36%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>0.9996</td>
        </tr>
        <tr>
            <td><b>Random Forest (100 trees)</b></td>
            <td>99.30% &plusmn; 0.28%</td>
            <td>99.36%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>99.18%</td>
            <td>0.9988</td>
        </tr>
        <tr>
            <td><b>Multinomial Naive Bayes</b></td>
            <td>98.55% &plusmn; 0.53%</td>
            <td>98.07%</td>
            <td>96.19%</td>
            <td>98.97%</td>
            <td>97.56%</td>
            <td>0.9989</td>
        </tr>
    </tbody>
</table>

<h3>Step 8: Verified Feature Importance (Top Words)</h3>
<p>By inspecting the Logistic Regression model coefficients, we observe the exact tokens driving classification (matching Figure 6 in the report):</p>
<ul>
    <li><b>Top AI-predictive words:</b> <code>potential</code> (+2.88), <code>provide</code> (+2.49), <code>ultimately</code> (+2.38), <code>additionally</code> (+2.23), <code>essential</code> (+2.14), <code>difficult</code> (+1.95), <code>understanding</code> (+1.88).</li>
    <li><b>Top Human-predictive words:</b> <code>want</code> (-4.07), <code>good</code> (-3.91), <code>like</code> (-3.70), <code>people</code> (-3.68), <code>think</code> (-3.66), <code>know</code> (-2.93), <code>don</code> (-2.75), <code>thing</code> (-2.62), <code>just</code> (-2.54).</li>
</ul>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>3. Understanding the High Accuracy &amp; Baseline Analysis</h2>

<div class="callout callout-blue">
    <div class="callout-title">💡 Why is the accuracy so high (99.6%)?</div>
    <p>A smart teacher will ask: <i>"99.6% accuracy sounds almost too good. Did your model learn genuine authorship, or did it just learn essay length?"</i></p>
    <p><b>Your Explanation (backed by our baseline experiment):</b><br>
    We ran a controlled baseline experiment using <b>ONLY 5 structural features</b> (word count, letter count, word length, sentence count, and average sentence length) without any text words. That length-only model achieved <b>95.42% accuracy</b> and an ROC-AUC of 0.9908!</p>
    <p>This proves that macro-structural differences (brevity vs. elaboration) account for ~95% of the class separation. However, lexical TF-IDF features provide the crucial extra boost from 95.42% to 99.60%, eliminating false positives on essays of unusual length.</p>
</div>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>4. How to Run, Save, and Close Everything</h2>

<h3>A. How to Open the Jupyter Notebook</h3>
<pre><code>jupyter notebook notebooks/llm_analysis_and_prediction.ipynb</code></pre>

<h3>B. How to Run Cells</h3>
<ul>
    <li>Click on any code cell and press <b>Shift + Enter</b>.</li>
    <li>To re-run everything: click <b>Kernel &rarr; Restart &amp; Run All Cells</b>.</li>
</ul>

<h3>C. How to Save &amp; Stop</h3>
<ul>
    <li>Save: press <b>Cmd + S</b>.</li>
    <li>Stop: close browser tab, switch to Terminal, and press <b>Ctrl + C</b>, then type <code>y</code>.</li>
</ul>

<h3>D. How to Re-Run the Entire Pipeline from Terminal</h3>
<pre><code>python3 run_pipeline.py</code></pre>

<h3>E. How to Re-Compile the IEEE Report PDF</h3>
<pre><code>python3 generate_report_pdf.py</code></pre>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>5. Checklist Before Submitting on Canvas</h2>
<ul>
    <li>[ ] Open <code>report/IAI600_Group21_Project_Report.pdf</code> and check that all group members' names and IDs are entered in the title block. (Edit <code>generate_report_pdf.py</code> and run it to update).</li>
    <li>[ ] Push your project folder to your GitHub repository and ensure the link matches Reference [8].</li>
    <li>[ ] Submit the PDF report on Canvas before the November 2 deadline.</li>
    <li>[ ] Study the separate <b>Oral Demonstration Guide for Labs 1, 2, 3, and 5</b> to prepare for your individual oral test.</li>
</ul>

</body>
</html>
"""

pdf_output_path = os.path.join(BASE_DIR, "IAI600_Group21_Project_Mastery_Handbook.pdf")
HTML(string=html_content).write_pdf(pdf_output_path)
print(f"Generated clean Mastery Handbook PDF at: {pdf_output_path}")
