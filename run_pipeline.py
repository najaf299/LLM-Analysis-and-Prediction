#!/usr/bin/env python3
"""
Complete end-to-end Machine Learning pipeline for Group 21:
LLM Analysis and Prediction (Human vs. AI Generated Text Detection)
Course: IAI600 - Introduction to AI and Machine Learning
"""

import os
import re
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix, ConfusionMatrixDisplay,
    classification_report
)

# -------------------------------------------------------------
# Configuration and Directories
# -------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FIG_DIR = os.path.join(BASE_DIR, "figures")
REP_DIR = os.path.join(BASE_DIR, "report")
NB_DIR = os.path.join(BASE_DIR, "notebooks")

for d in [DATA_DIR, FIG_DIR, REP_DIR, NB_DIR]:
    os.makedirs(d, exist_ok=True)

# Plot styling for high-quality IEEE figures
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300

print("=" * 70)
print("IAI600 Group 21: LLM Analysis and Prediction Pipeline")
print("=" * 70)

# -------------------------------------------------------------
# 1. Dataset Loading and Unification
# -------------------------------------------------------------
print("\n[Step 1] Loading and merging datasets...")
train_path = os.path.join(DATA_DIR, "train_essays.csv")
daigt_path = os.path.join(DATA_DIR, "daigt_external_dataset.csv")

train_df = pd.read_csv(train_path)
daigt_df = pd.read_csv(daigt_path)

print(f"  Raw train_essays.csv shape: {train_df.shape}")
print(f"  Raw daigt_external_dataset.csv shape: {daigt_df.shape}")

# In train_essays: 1375 human (0), 3 AI (1)
df1 = train_df[['text', 'generated']].copy()

# In daigt_external: 'text' is student human (0), 'source_text' is AI generated (1)
df_daigt_human = pd.DataFrame({'text': daigt_df['text'], 'generated': 0})
df_daigt_ai = pd.DataFrame({'text': daigt_df['source_text'], 'generated': 1})

# Combine
combined_df = pd.concat([df1, df_daigt_human, df_daigt_ai], ignore_index=True)
combined_df.dropna(subset=['text', 'generated'], inplace=True)
combined_df['text'] = combined_df['text'].astype(str)
combined_df.drop_duplicates(subset=['text'], inplace=True)
combined_df = combined_df[combined_df['text'].str.strip().str.len() > 50].reset_index(drop=True)

# Save unified dataset
cleaned_dataset_path = os.path.join(DATA_DIR, "balanced_essays.csv")
combined_df.to_csv(cleaned_dataset_path, index=False)
print(f"  Saved unified dataset: {cleaned_dataset_path}")
print(f"  Total records: {len(combined_df):,}")
print("  Class distribution:")
print(combined_df['generated'].value_counts())
class_counts = combined_df['generated'].value_counts().to_dict()

# -------------------------------------------------------------
# 2. Exploratory Data Analysis (EDA) & Feature Extraction for EDA
# -------------------------------------------------------------
print("\n[Step 2] Conducting Exploratory Data Analysis & generating figures...")

# Compute text statistics
combined_df['word_count'] = combined_df['text'].apply(lambda x: len(x.split()))
combined_df['char_count'] = combined_df['text'].apply(lambda x: len(x))
combined_df['avg_word_len'] = combined_df['char_count'] / combined_df['word_count'].clip(lower=1)
combined_df['sentence_count'] = combined_df['text'].apply(lambda x: len(re.split(r'[.!?]+', x)) - 1)
combined_df['sentence_count'] = combined_df['sentence_count'].clip(lower=1)
combined_df['avg_sentence_len'] = combined_df['word_count'] / combined_df['sentence_count']

# Summary table per class
eda_stats = combined_df.groupby('generated')[['word_count', 'char_count', 'avg_word_len', 'sentence_count', 'avg_sentence_len']].mean()
print("EDA Statistics by class (0=Human, 1=AI):")
print(eda_stats)

# Fig 1: Target Class Distribution
fig, ax = plt.subplots(figsize=(6, 4))
labels = ['Human-Written (0)', 'AI-Generated (1)']
counts = [class_counts[0], class_counts[1]]
colors = ['#2b6cb0', '#e53e3e']
bars = ax.bar(labels, counts, color=colors, width=0.55, edgecolor='black', linewidth=0.8)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 60, f'{int(h):,} ({h/len(combined_df)*100:.1f}%)',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_title('Dataset Target Class Distribution', fontsize=12, fontweight='bold', pad=12)
ax.set_ylabel('Number of Essays', fontsize=10)
ax.set_ylim(0, max(counts) * 1.15)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "01_target_distribution.png"), dpi=300)
plt.close(fig)

# Fig 2: Word Count Distribution (Histogram & KDE)
fig, ax = plt.subplots(figsize=(7, 4.2))
plot_df = combined_df.copy()
plot_df['Origin'] = plot_df['generated'].map({0: 'Human-Written', 1: 'AI-Generated'})
sns.histplot(data=plot_df, x='word_count', hue='Origin', palette={'Human-Written': '#2b6cb0', 'AI-Generated': '#e53e3e'},
             kde=True, bins=40, alpha=0.45, ax=ax, element='step')
ax.set_title('Essay Word Count Distribution by Origin', fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('Word Count', fontsize=10)
ax.set_ylabel('Essay Frequency', fontsize=10)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "02_word_count_distribution.png"), dpi=300)
plt.close(fig)

# Fig 3: Average Word Length Distribution
fig, ax = plt.subplots(figsize=(7, 4.2))
sns.kdeplot(data=combined_df[combined_df['generated'] == 0]['avg_word_len'], label='Human-Written',
           color='#2b6cb0', fill=True, alpha=0.35, linewidth=2, ax=ax)
sns.kdeplot(data=combined_df[combined_df['generated'] == 1]['avg_word_len'], label='AI-Generated',
           color='#e53e3e', fill=True, alpha=0.35, linewidth=2, ax=ax)
ax.set_title('Average Word Length (Characters/Word) Density', fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('Average Word Length', fontsize=10)
ax.set_ylabel('Density', fontsize=10)
ax.set_xlim(3.5, 7.0)
ax.legend(frameon=True)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "03_avg_word_length_distribution.png"), dpi=300)
plt.close(fig)

# Fig 4: Correlation Heatmap
fig, ax = plt.subplots(figsize=(6, 4.5))
corr_features = ['word_count', 'char_count', 'avg_word_len', 'sentence_count', 'avg_sentence_len', 'generated']
corr = combined_df[corr_features].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', cbar=True, ax=ax, linewidths=0.5)
ax.set_title('Correlation Matrix of Extracted Stylistic Features', fontsize=11, fontweight='bold', pad=10)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "04_correlation_heatmap.png"), dpi=300)
plt.close(fig)

# Fig 5: Word Clouds
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
human_text = " ".join(combined_df[combined_df['generated'] == 0]['text'].sample(n=min(500, class_counts[0]), random_state=42))
ai_text = " ".join(combined_df[combined_df['generated'] == 1]['text'].sample(n=min(500, class_counts[1]), random_state=42))

wc_human = WordCloud(width=600, height=350, background_color='white', colormap='Blues', max_words=80).generate(human_text)
wc_ai = WordCloud(width=600, height=350, background_color='white', colormap='Reds', max_words=80).generate(ai_text)

axes[0].imshow(wc_human, interpolation='bilinear')
axes[0].set_title('Most Frequent Words: Human Essays', fontsize=11, fontweight='bold')
axes[0].axis('off')

axes[1].imshow(wc_ai, interpolation='bilinear')
axes[1].set_title('Most Frequent Words: AI-Generated Essays', fontsize=11, fontweight='bold')
axes[1].axis('off')
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "05_word_clouds.png"), dpi=300)
plt.close(fig)

print("  All EDA figures generated and saved successfully.")

# -------------------------------------------------------------
# 3. Preprocessing Pipeline & TF-IDF Vectorization
# -------------------------------------------------------------
print("\n[Step 3] Text Preprocessing & TF-IDF Vectorization...")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

combined_df['cleaned_text'] = combined_df['text'].apply(preprocess_text)

X_raw = combined_df['cleaned_text']
y = combined_df['generated'].values

# Split into 80% train and 20% test
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.20, random_state=42, stratify=y
)

print(f"  Training set size: {len(X_train_raw):,} samples")
print(f"  Test set size: {len(X_test_raw):,} samples")

# TF-IDF Feature Extractor
tfidf = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=10000,
    sublinear_tf=True,
    min_df=3,
    stop_words='english'
)

X_train_tfidf = tfidf.fit_transform(X_train_raw)
X_test_tfidf = tfidf.transform(X_test_raw)

print(f"  TF-IDF feature matrix shape: {X_train_tfidf.shape}")

# -------------------------------------------------------------
# 4. Model Training & Cross-Validation
# -------------------------------------------------------------
print("\n[Step 4] Training machine learning models...")

models = {
    "Logistic Regression": LogisticRegression(C=1.0, max_iter=1000, random_state=42),
    "Multinomial Naive Bayes": MultinomialNB(alpha=0.1),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=30, random_state=42, n_jobs=-1),
    "Linear SVM": CalibratedClassifierCV(LinearSVC(C=1.0, random_state=42, max_iter=2000), cv=3)
}

results = {}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models.items():
    print(f"  Training {name}...")
    # 5-fold Cross-validation
    cv_scores = cross_val_score(model, X_train_tfidf, y_train, cv=cv, scoring='accuracy', n_jobs=-1)
    
    # Train on full train set
    model.fit(X_train_tfidf, y_train)
    
    # Predict on unseen test set
    y_pred = model.predict(X_test_tfidf)
    y_prob = model.predict_proba(X_test_tfidf)[:, 1] if hasattr(model, 'predict_proba') else model.decision_function(X_test_tfidf)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    
    results[name] = {
        'model': model,
        'cv_mean': float(cv_scores.mean()),
        'cv_std': float(cv_scores.std()),
        'accuracy': float(acc),
        'precision': float(prec),
        'recall': float(rec),
        'f1': float(f1),
        'roc_auc': float(auc),
        'y_pred': y_pred,
        'y_prob': y_prob
    }
    print(f"    Test Acc: {acc:.4f} | F1: {f1:.4f} | ROC-AUC: {auc:.4f} | 5-Fold CV Acc: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

# Word-Count-Only Baseline Model
print("  Evaluating Word-Count-Only Baseline Model...")
from sklearn.preprocessing import StandardScaler
scaler_len = StandardScaler()
X_train_wc = scaler_len.fit_transform(pd.DataFrame({'word_count': combined_df.loc[X_train_raw.index, 'word_count']}))
X_test_wc = scaler_len.transform(pd.DataFrame({'word_count': combined_df.loc[X_test_raw.index, 'word_count']}))

lr_wc = LogisticRegression(random_state=42)
cv_wc_scores = cross_val_score(lr_wc, X_train_wc, y_train, cv=cv, scoring='accuracy', n_jobs=-1)
lr_wc.fit(X_train_wc, y_train)
y_pred_wc = lr_wc.predict(X_test_wc)
y_prob_wc = lr_wc.predict_proba(X_test_wc)[:, 1]

wc_baseline = {
    'cv_mean': float(cv_wc_scores.mean()),
    'cv_std': float(cv_wc_scores.std()),
    'accuracy': float(accuracy_score(y_test, y_pred_wc)),
    'precision': float(precision_score(y_test, y_pred_wc)),
    'recall': float(recall_score(y_test, y_pred_wc)),
    'f1': float(f1_score(y_test, y_pred_wc)),
    'roc_auc': float(roc_auc_score(y_test, y_prob_wc))
}
print(f"    Baseline Acc: {wc_baseline['accuracy']:.4f} | F1: {wc_baseline['f1']:.4f} | ROC-AUC: {wc_baseline['roc_auc']:.4f} | 5-Fold CV Acc: {wc_baseline['cv_mean']:.4f} +/- {wc_baseline['cv_std']:.4f}")

# -------------------------------------------------------------
# 5. Results Evaluation & Plots
# -------------------------------------------------------------
print("\n[Step 5] Generating evaluation figures...")

# Fig 6: Confusion Matrices (2x2 grid)
fig, axes = plt.subplots(2, 2, figsize=(9, 8))
axes = axes.flatten()

for idx, (name, res) in enumerate(results.items()):
    cm = confusion_matrix(y_test, res['y_pred'])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Human (0)', 'AI (1)'])
    disp.plot(ax=axes[idx], cmap='Blues', colorbar=False, values_format='d')
    axes[idx].set_title(f"{name}\nAcc: {res['accuracy']*100:.2f}% | F1: {res['f1']*100:.2f}%", fontsize=10, fontweight='bold')
    axes[idx].grid(False)

plt.suptitle('Confusion Matrices on Test Set (N=1,244)', fontsize=13, fontweight='bold', y=0.99)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "06_confusion_matrices.png"), dpi=300)
plt.close(fig)

# Fig 7: ROC Curves
fig, ax = plt.subplots(figsize=(7, 5))
colors_roc = ['#2b6cb0', '#2f855a', '#c53030', '#805ad5']

for idx, (name, res) in enumerate(results.items()):
    fpr, tpr, _ = roc_curve(y_test, res['y_prob'])
    ax.plot(fpr, tpr, label=f"{name} (AUC = {res['roc_auc']:.4f})", color=colors_roc[idx], linewidth=2.0)

ax.plot([0, 1], [0, 1], linestyle='--', color='#718096', label='Random Guessing (AUC = 0.5000)')
ax.set_title('Receiver Operating Characteristic (ROC) Curves', fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('False Positive Rate (1 - Specificity)', fontsize=10)
ax.set_ylabel('True Positive Rate (Sensitivity)', fontsize=10)
ax.set_xlim([-0.01, 1.01])
ax.set_ylim([-0.01, 1.02])
ax.legend(loc='lower right', frameon=True, fontsize=9)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "07_roc_curves.png"), dpi=300)
plt.close(fig)

# Fig 8: Model Comparison Bar Chart
fig, ax = plt.subplots(figsize=(8, 4.5))
metrics_to_plot = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
model_names = list(results.keys())
x = np.arange(len(model_names))
width = 0.15

for i, m in enumerate(['accuracy', 'precision', 'recall', 'f1', 'roc_auc']):
    vals = [results[mn][m] * 100 for mn in model_names]
    rects = ax.bar(x + (i - 2) * width, vals, width, label=metrics_to_plot[i])

ax.set_ylabel('Score (%)', fontsize=10)
ax.set_title('Model Performance Comparison Across Core Evaluation Metrics', fontsize=12, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(model_names, fontsize=9.5, fontweight='bold')
ax.set_ylim(85, 101)
ax.legend(loc='lower left', ncol=5, frameon=True, fontsize=8.5)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "08_model_comparison_bar.png"), dpi=300)
plt.close(fig)

# Fig 9: Feature Importance / Top Informative N-grams (from Logistic Regression)
lr_model = results['Logistic Regression']['model']
feature_names = np.array(tfidf.get_feature_names_out())
coefs = lr_model.coef_[0]

# For AI: positive coefficients. Top 12 features sorted so largest is at the top of horizontal bar
top_ai_idx = np.argsort(coefs)[-12:]
# For Human: negative coefficients. Top 12 features sorted by absolute magnitude so largest is at top
top_human_idx = np.argsort(coefs)[:12][::-1]

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

axes[0].barh(feature_names[top_human_idx], np.abs(coefs[top_human_idx]), color='#2b6cb0', edgecolor='black', linewidth=0.5)
axes[0].set_title('Top Features Predictive of Human-Written Text', fontsize=10.5, fontweight='bold')
axes[0].set_xlabel('Absolute Weight Magnitude (|Coefficient|)', fontsize=9.5)

axes[1].barh(feature_names[top_ai_idx], coefs[top_ai_idx], color='#e53e3e', edgecolor='black', linewidth=0.5)
axes[1].set_title('Top Features Predictive of AI-Generated Text', fontsize=10.5, fontweight='bold')
axes[1].set_xlabel('Log-Odds Coefficient Weight', fontsize=9.5)

plt.suptitle('Logistic Regression: Most Discriminating TF-IDF Features', fontsize=12, fontweight='bold', y=0.98)
plt.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "09_feature_importance.png"), dpi=300)
plt.close(fig)

print("  All model evaluation figures saved.")

# -------------------------------------------------------------
# 6. Save Metrics to JSON for the IEEE Report
# -------------------------------------------------------------
report_metrics = {
    "total_samples": len(combined_df),
    "human_count": int(class_counts[0]),
    "ai_count": int(class_counts[1]),
    "train_size": len(X_train_raw),
    "test_size": len(X_test_raw),
    "tfidf_features": X_train_tfidf.shape[1],
    "eda": {
        "human_avg_words": float(eda_stats.loc[0, 'word_count']),
        "ai_avg_words": float(eda_stats.loc[1, 'word_count']),
        "human_avg_word_len": float(eda_stats.loc[0, 'avg_word_len']),
        "ai_avg_word_len": float(eda_stats.loc[1, 'avg_word_len']),
        "human_avg_sentences": float(eda_stats.loc[0, 'sentence_count']),
        "ai_avg_sentences": float(eda_stats.loc[1, 'sentence_count']),
    },
    "models": {}
}

for name, res in results.items():
    report_metrics["models"][name] = {
        "cv_mean": res["cv_mean"],
        "cv_std": res["cv_std"],
        "accuracy": res["accuracy"],
        "precision": res["precision"],
        "recall": res["recall"],
        "f1": res["f1"],
        "roc_auc": res["roc_auc"]
    }

report_metrics["word_count_baseline"] = wc_baseline

metrics_json_path = os.path.join(REP_DIR, "metrics.json")
with open(metrics_json_path, 'w') as f:
    json.dump(report_metrics, f, indent=2)

print(f"\n[Step 6] Metrics successfully saved to: {metrics_json_path}")

# -------------------------------------------------------------
# 7. Sample Inference Verification
# -------------------------------------------------------------
print("\n[Step 7] Testing real-time inference on unseen sample texts:")
test_samples = [
    (
        "Human Sample",
        "In my opinion, students should not be forced to take online classes exclusively. While computers are helpful for research and homework, learning in a physical classroom allows us to interact with friends, ask the teacher direct questions when confused, and build social communication skills. Personally, I found it very lonely to study from my bedroom all year."
    ),
    (
        "AI Sample",
        "The implementation of artificial intelligence within modern educational curricula presents both substantial advantages and notable challenges. On the one hand, personalized algorithms optimize individual learning trajectories. On the other hand, empirical evidence highlights ethical considerations regarding academic dishonesty and cognitive dependency."
    )
]

for label, sample in test_samples:
    cleaned = preprocess_text(sample)
    vec = tfidf.transform([cleaned])
    pred_label = lr_model.predict(vec)[0]
    pred_proba = lr_model.predict_proba(vec)[0]
    print(f"\n  [{label}]")
    print(f"    Text snippet: {sample[:100]}...")
    print(f"    Prediction: {'AI-Generated' if pred_label == 1 else 'Human-Written'}")
    print(f"    Probabilities: Human={pred_proba[0]*100:.2f}% | AI={pred_proba[1]*100:.2f}%")

print("\n" + "=" * 70)
print("Pipeline execution complete! All artifacts ready.")
print("=" * 70)
