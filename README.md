# IAI600 Group 21: LLM Analysis and Prediction
## Detecting AI-Generated Text Using Machine Learning

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![IEEE Format](https://img.shields.io/badge/Format-IEEE%202--Column-red.svg)](report/IAI600_Group21_Project_Report.pdf)

This repository contains the complete implementation, datasets, experimental results, and final IEEE-style conference report for **Group 21** in course **IAI600: Introduction to AI and Machine Learning**.

---

## 🎯 Project Overview

* **Objective:** Binary text classification to distinguish between human student-written essays and Large Language Model (LLM) generated essays.
* **Problem Formulation:** Binary Supervised Classification ($y \in \{0, 1\}$).
* **Reference Notebook:** [Jocelyn Dumlao – LLM Analysis and Prediction (Kaggle)](https://www.kaggle.com/code/jocelyndumlao/llm-analysis-and-prediction)
* **Dataset:** Kaggle *LLM – Detect AI Generated Text* competition benchmark integrated with the community DAIGT paired generation corpus (6,220 total essays: 3,796 human, 2,424 AI).

---

## 📁 Repository Structure

```text
LLM-Analysis-and-Prediction/
├── data/
│   ├── train_essays.csv             # Kaggle competition corpus (1,378 essays)
│   ├── daigt_external_dataset.csv   # DAIGT paired ChatGPT generation corpus (2,421 pairs)
│   └── balanced_essays.csv          # Curated unified dataset (6,220 essays)
├── figures/
│   ├── 01_target_distribution.png
│   ├── 02_word_count_distribution.png
│   ├── 03_avg_word_length_distribution.png
│   ├── 04_correlation_heatmap.png
│   ├── 05_word_clouds.png
│   ├── 06_confusion_matrices.png
│   ├── 07_roc_curves.png
│   ├── 08_model_comparison_bar.png
│   └── 09_feature_importance.png
├── notebooks/
│   └── llm_analysis_and_prediction.ipynb   # Executed Jupyter Notebook with outputs
├── report/
│   ├── IAI600_Group21_Project_Report.pdf   # Final 4-page IEEE formatted submission report
│   ├── IAI600_Group21_Project_Report.html  # HTML source of the IEEE report
│   ├── metrics.json                        # Exact performance metrics from experiments
│   └── results_table.csv                   # Formatted evaluation metrics CSV
├── run_pipeline.py                         # End-to-end Python script to train & evaluate
├── generate_report_pdf.py                  # Script compiling IEEE Report to PDF
├── generate_mastery_handbook.py            # Script compiling Project Mastery Handbook PDF
├── generate_labs_oral_demo_guide.py        # Script compiling Labs 1, 2, 3, 5 Oral Guide PDF
├── IAI600_Group21_Project_Mastery_Handbook.pdf
├── IAI600_Oral_Demonstration_Master_Guide_Labs_1_2_3_5.pdf
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation
```

---

## 📊 Experimental Results

Evaluated on an independent, stratified holdout test partition of 1,244 unseen essays:

| Model Architecture | 5-Fold CV Accuracy | Test Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|---|
| **Linear SVM (Calibrated)** | **99.50% ± 0.14%** | **99.60%** | **99.38%** | **99.59%** | **99.49%** | **0.9999** |
| **Logistic Regression** | 99.36% ± 0.27% | 99.36% | 99.18% | 99.18% | 99.18% | 0.9996 |
| **Random Forest (100 Trees)** | 99.26% ± 0.19% | 99.36% | 99.18% | 99.18% | 99.18% | 0.9988 |
| **Multinomial Naive Bayes** | 98.49% ± 0.42% | 98.07% | 96.19% | 98.97% | 97.56% | 0.9989 |
| *Word-Count Baseline (Length Only)* | *86.86% ± 1.16%* | *88.10%* | *83.50%* | *86.60%* | *85.02%* | *0.9456* |

> **Note on Length Confounding:** The word-count-only baseline demonstrates that document length accounts for ~88.1% class separability due to student essays averaging ~478 words versus ~202 words for ChatGPT responses. TF-IDF unigram and bigram features provide the essential discriminative refinement necessary to reach >99% precision and recall.

---

## 📜 Dataset Attribution & Licensing

* **Kaggle Competition Corpus (`train_essays.csv`):** Sourced from the [Kaggle LLM – Detect AI Generated Text](https://www.kaggle.com/competitions/llm-detect-ai-generated-text) benchmark hosted by The Learning Agency Lab. Included strictly for course evaluation under educational fair use in accordance with competition benchmark guidelines.
* **DAIGT External Dataset (`daigt_external_dataset.csv`):** Community-curated paired dataset pairing student persuasive essays with ChatGPT generations across aligned writing prompts.

---

## 🚀 How to Run

### 1. Requirements
Ensure Python 3.10+ is installed:
```bash
pip install -r requirements.txt
```

### 2. Execute End-to-End Pipeline
Run the complete training, cross-validation, and plotting pipeline:
```bash
python run_pipeline.py
```

### 3. Open Interactive Jupyter Notebook
Launch Jupyter to explore or present during oral demonstrations:
```bash
jupyter notebook notebooks/llm_analysis_and_prediction.ipynb
```

### 4. Rebuild PDFs
```bash
# Rebuild the IEEE Report PDF
python generate_report_pdf.py

# Rebuild the Student Mastery Handbook PDF
python generate_mastery_handbook.py

# Rebuild the Labs 1, 2, 3, 5 Oral Demo Guide PDF
python generate_labs_oral_demo_guide.py
```

---

## 🤖 Generative AI Tool Acknowledgment
In accordance with course regulations, Google Gemini (via the Antigravity IDE) and ChatGPT were consulted as interactive learning aids for concept clarification, syntax debugging, and report formatting. All code execution, data curation, model evaluations, and conclusions were developed, verified, and authored directly by group members.
