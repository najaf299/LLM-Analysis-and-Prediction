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
* **Dataset:** Kaggle *LLM – Detect AI Generated Text* benchmark integrated with the DAIGT paired generation corpus (6,220 total essays).

---

## 📁 Repository Structure

```text
LLM-Analysis-and-Prediction/
├── data/
│   ├── train_essays.csv             # Kaggle competition corpus
│   ├── daigt_external_dataset.csv   # DAIGT paired LLM generation corpus
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
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation
```

---

## 📊 Experimental Results

Evaluated on an independent, stratified holdout test set of 1,244 unseen essays:

| Model Architecture | 5-Fold CV Accuracy | Test Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|---|
| **Linear SVM (Calibrated)** | **99.50% ± 0.14%** | **99.60%** | **99.38%** | **99.59%** | **99.49%** | **0.9999** |
| **Logistic Regression** | 99.36% ± 0.27% | 99.36% | 99.18% | 99.18% | 99.18% | 0.9996 |
| **Random Forest (100 Trees)** | 99.26% ± 0.19% | 99.36% | 99.18% | 99.18% | 99.18% | 0.9988 |
| **Multinomial Naive Bayes** | 98.49% ± 0.42% | 98.07% | 96.19% | 98.97% | 97.56% | 0.9989 |

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

### 4. Rebuild the IEEE Report PDF
```bash
python generate_report_pdf.py
```

---

## 🤖 Generative AI Tool Acknowledgment
In accordance with course regulations, Claude and ChatGPT were consulted as learning aids for concept clarification, syntax assistance, and report typesetting. All code execution, data curation, model evaluations, and conclusions were performed and validated by group members.
