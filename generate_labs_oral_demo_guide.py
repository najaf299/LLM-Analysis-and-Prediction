#!/usr/bin/env python3
"""
Generate a dedicated Oral Demonstration Master Guide PDF
covering IAI600 Labs 1, 2, 3, and 5.
"""

import os
from weasyprint import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSS = """
@page {
    size: A4;
    margin: 1.8cm 1.6cm 1.8cm 1.6cm;
    @bottom-center {
        content: "IAI600 Lab Demonstration Oral Exam Guide — Page " counter(page) " of " counter(pages);
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
    background: linear-gradient(135deg, #742a2a 0%, #c53030 100%);
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
}

.header-banner p {
    font-size: 10pt;
    margin: 0;
    color: #fed7d7;
    line-height: 1.4;
}

.badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.25);
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 8.5pt;
    font-weight: bold;
    margin-top: 8px;
}

h2 {
    font-size: 13.5pt;
    color: #742a2a;
    border-bottom: 2px solid #fed7d7;
    padding-bottom: 5px;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h3 {
    font-size: 11pt;
    color: #9b2c2c;
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

.callout-red {
    background-color: #fff5f5;
    border-color: #e53e3e;
    color: #9b2c2c;
}

.callout-blue {
    background-color: #ebf8ff;
    border-color: #3182ce;
    color: #2b6cb0;
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
    background-color: #9b2c2c;
    color: white;
    padding: 6px 9px;
    text-align: left;
    font-weight: 600;
    border: 1px solid #9b2c2c;
}

td {
    padding: 5px 9px;
    border: 1px solid #cbd5e0;
}

tr:nth-child(even) {
    background-color: #fff5f5;
}

.qa-card {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #c53030;
    border-radius: 4px;
    padding: 9px 12px;
    margin: 8pt 0;
    page-break-inside: avoid;
}

.qa-q {
    font-weight: bold;
    color: #742a2a;
    font-size: 9.6pt;
    margin-bottom: 4px;
}

.qa-a {
    color: #2d3748;
    font-size: 9.1pt;
}

.action-step {
    background: #edf2f7;
    padding: 6px 10px;
    border-radius: 4px;
    font-weight: bold;
    color: #2d3748;
    margin: 6pt 0;
}
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>IAI600: Oral Demonstration Guide (Labs 1, 2, 3, and 5)</title>
<style>""" + CSS + """</style>
</head>
<body>

<div class="header-banner">
    <div class="badge">IAI600: Introduction to AI &amp; Machine Learning (2.5 Credits)</div>
    <h1>Individual Oral Demonstration Master Guide</h1>
    <p><b>Instructor:</b> Rashid Ali &bull; <b>Mandatory Individual Examination</b><br>
    How to show your code running, explain every step, present results, and answer technical questions for <b>Labs 1, 2, 3, and 5</b>.</p>
</div>

<div class="callout callout-red">
    <div class="callout-title">⚠️ Exact Exam Requirements from Rashid Ali:</div>
    <ul>
        <li><b>Labs Tested:</b> Labs 1, 2, 3, and 5 ONLY (Labs 4, 6, and 7 are excluded).</li>
        <li><b>Core Topics:</b> Preprocessing pipeline, regression, classification, and clustering.</li>
        <li><b>Individual Requirement:</b> Each student is tested alone. Simply having completed the labs is NOT sufficient; you must demonstrate running code and explain the concepts.</li>
        <li><b>Four Requirements:</b> (1) Show your code running live &rarr; (2) Show the execution steps &rarr; (3) Present and explain results &rarr; (4) Answer technical questions.</li>
    </ul>
</div>

<h2>Table of Contents</h2>
<ol>
    <li><b>How the Oral Demonstration Works &amp; Strategy to Pass</b></li>
    <li><b>Lab 1: Preprocessing Pipeline</b> (California Housing &bull; Missing Data &bull; Encoding &bull; Scaling &bull; ColumnTransformer)</li>
    <li><b>Lab 2: Regression</b> (Linear Regression &bull; Cost Function MSE &bull; Gradient Descent &bull; Polynomial Features &bull; Regularization)</li>
    <li><b>Lab 3: Classification</b> (MNIST Digits &bull; SGDClassifier &bull; Confusion Matrix &bull; Precision/Recall &bull; ROC-AUC)</li>
    <li><b>Lab 5: Clustering</b> (Unsupervised Learning &bull; K-Means Algorithm &bull; Centroids &bull; Elbow Method &bull; Silhouette Score)</li>
    <li><b>Teacher's Technical Questions &amp; Exact Answers</b></li>
</ol>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>1. How the Oral Demonstration Works &amp; Strategy</h2>
<p>When your scheduled time slot begins:</p>
<ol>
    <li>Have Jupyter Notebook running in your terminal:
        <pre><code>cd ~/Downloads/handson-ml3-main && conda activate homl3 && jupyter notebook</code></pre>
    </li>
    <li>Open the corresponding notebook for the lab requested by the teacher:
        <ul>
            <li><b>Lab 1:</b> <code>02_end_to_end_machine_learning_project.ipynb</code></li>
            <li><b>Lab 2:</b> <code>04_training_linear_models.ipynb</code></li>
            <li><b>Lab 3:</b> <code>03_classification.ipynb</code></li>
            <li><b>Lab 5:</b> <code>09_unsupervised_learning.ipynb</code></li>
        </ul>
    </li>
    <li>Select the cell the teacher asks to see, press <b>Shift + Enter</b> to show it executing live, and explain the input, process, and output in plain English using the guide below.</li>
</ol>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>2. Lab 1: Data Preprocessing Pipeline</h2>
<p><b>Notebook:</b> <code>02_end_to_end_machine_learning_project.ipynb</code><br>
<b>Dataset:</b> California Housing Dataset (predicting median house value from geographical & demographic features).</p>

<div class="action-step">Step 1: Handling Missing Values (Imputation)</div>
<pre><code>from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis=1)
imputer.fit(housing_num)
X = imputer.transform(housing_num)</code></pre>
<ul>
    <li><b>What this does:</b> Some houses in the dataset have missing values in <code>total_bedrooms</code>. <code>SimpleImputer</code> computes the median of the numerical columns on the training set and fills in any missing entries.</li>
    <li><b>Why median instead of mean?</b> The mean is heavily skewed by extreme outliers (very rich mansions). The median is robust against outliers.</li>
</ul>

<div class="action-step">Step 2: Handling Categorical Attributes (One-Hot Encoding)</div>
<pre><code>from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing[["ocean_proximity"]])</code></pre>
<ul>
    <li><b>What this does:</b> <code>ocean_proximity</code> contains text labels (e.g., <i>"&lt;1H OCEAN"</i>, <i>"INLAND"</i>, <i>"NEAR BAY"</i>). Machine learning models require numbers.</li>
    <li><b>Why One-Hot Encoding?</b> If we assigned numbers 0, 1, 2, 3, the model would assume that category 2 is "twice as large" or closer to 3 than 0. One-Hot creates binary dummy columns (0 or 1) for each category, eliminating false numerical ordering.</li>
</ul>

<div class="action-step">Step 3: Feature Scaling (StandardScaler)</div>
<pre><code>from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
housing_scaled = scaler.fit_transform(housing_num)</code></pre>
<ul>
    <li><b>What this does:</b> Features have completely different scales (e.g., median income ranges from 0 to 15, while total rooms ranges from 6 to 39,000). <code>StandardScaler</code> subtracts the mean (&mu;) and divides by standard deviation (&sigma;), centering features around 0 with unit variance.</li>
    <li><b>Why scaling matters:</b> Algorithms like Gradient Descent, Support Vector Machines, and KNN perform poorly or converge very slowly if features are on vastly different scales.</li>
</ul>

<div class="action-step">Step 4: The Unified ColumnTransformer Pipeline</div>
<pre><code>from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('std_scaler', StandardScaler()),
])

full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),
])
housing_prepared = full_pipeline.fit_transform(housing)</code></pre>
<p><b>Explanation:</b> <code>ColumnTransformer</code> automatically routes numerical columns through the imputation and scaling pipeline, and categorical columns through OneHotEncoder, assembling everything into a single ready-to-train matrix.</p>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>3. Lab 2: Regression</h2>
<p><b>Notebook:</b> <code>04_training_linear_models.ipynb</code><br>
<b>Core Concept:</b> Predicting continuous target values using linear and polynomial models.</p>

<div class="action-step">Step 1: Linear Regression &amp; The Normal Equation</div>
<pre><code>from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.intercept_, lin_reg.coef_)</code></pre>
<ul>
    <li><b>Mathematical Equation:</b> $\hat{y} = \theta_0 + \theta_1 x_1 + \dots + \theta_n x_n$.</li>
    <li><b>Cost Function:</b> Mean Squared Error (MSE): $\text{MSE}(\theta) = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})^2$.</li>
    <li>Linear Regression finds parameter vector $\theta$ that minimizes this sum of squared errors.</li>
</ul>

<div class="action-step">Step 2: Gradient Descent (Batch vs. Stochastic)</div>
<ul>
    <li><b>Batch Gradient Descent:</b> Uses the entire training set to calculate gradients at every step. Accurate but slow on massive datasets.</li>
    <li><b>Stochastic Gradient Descent (SGD):</b> Picks a random instance at each step to compute gradients. Extremely fast, but bounces around instead of settling smoothly. Controlled using learning rate decay.</li>
</ul>

<div class="action-step">Step 3: Polynomial Regression &amp; Overfitting</div>
<pre><code>from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)</code></pre>
<ul>
    <li>When data is non-linear, we add powers of each feature (e.g., $x_1^2, x_1 x_2$) to create new features, allowing a linear model to fit curved relationships.</li>
    <li><b>Risk:</b> High degree polynomials (e.g., degree 10 or 300) severely <b>overfit</b> &mdash; memorizing noise in the training set and failing on new test data.</li>
</ul>

<div class="action-step">Step 4: Regularization (Ridge vs. Lasso)</div>
<ul>
    <li><b>Ridge Regression ($L_2$ Regularization):</b> Adds $\alpha \sum \theta_i^2$ penalty to the cost function. Keeps weights small, preventing any single feature from dominating.</li>
    <li><b>Lasso Regression ($L_1$ Regularization):</b> Adds $\alpha \sum |\theta_i|$ penalty. Drives unimportant feature weights completely to <b>zero</b>, performing automatic feature selection!</li>
</ul>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>4. Lab 3: Classification</h2>
<p><b>Notebook:</b> <code>03_classification.ipynb</code><br>
<b>Dataset:</b> MNIST (70,000 images of handwritten digits 0&ndash;9, 28&times;28 pixels).</p>

<div class="action-step">Step 1: Training a Binary Classifier (e.g., "Is this digit a 5?")</div>
<pre><code>from sklearn.linear_model import SGDClassifier
y_train_5 = (y_train == '5')
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)</code></pre>

<div class="action-step">Step 2: The Confusion Matrix</div>
<pre><code>from sklearn.metrics import confusion_matrix
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
cm = confusion_matrix(y_train_5, y_train_pred)</code></pre>
<table>
    <thead>
        <tr>
            <th></th>
            <th>Predicted Negative (Not 5)</th>
            <th>Predicted Positive (Is 5)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Actual Negative (Not 5)</b></td>
            <td><b>True Negative (TN)</b></td>
            <td><b>False Positive (FP)</b> (Type I Error)</td>
        </tr>
        <tr>
            <td><b>Actual Positive (Is 5)</b></td>
            <td><b>False Negative (FN)</b> (Type II Error)</td>
            <td><b>True Positive (TP)</b></td>
        </tr>
    </tbody>
</table>

<div class="action-step">Step 3: Precision, Recall, and F1-Score</div>
<ul>
    <li><b>Precision:</b> $\frac{\text{TP}}{\text{TP} + \text{FP}}$ &mdash; Of all instances predicted positive, what percentage was actually positive?</li>
    <li><b>Recall (Sensitivity):</b> $\frac{\text{TP}}{\text{TP} + \text{FN}}$ &mdash; Of all actual positives, what percentage did we successfully catch?</li>
    <li><b>F1-Score:</b> $\frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$ &mdash; Harmonic mean balancing both metrics.</li>
    <li><b>Precision/Recall Trade-off:</b> Increasing the decision threshold increases Precision but decreases Recall.</li>
</ul>

<div class="action-step">Step 4: The ROC Curve &amp; ROC-AUC</div>
<pre><code>from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)
auc = roc_auc_score(y_train_5, y_scores)</code></pre>
<ul>
    <li>Plots True Positive Rate vs False Positive Rate. An AUC of 1.0 represents a perfect classifier; 0.5 is random guessing.</li>
</ul>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>5. Lab 5: Clustering</h2>
<p><b>Notebook:</b> <code>09_unsupervised_learning.ipynb</code><br>
<b>Core Concept:</b> Unsupervised learning &mdash; discovering natural groupings in data without labels.</p>

<div class="action-step">Step 1: K-Means Clustering Algorithm</div>
<pre><code>from sklearn.cluster import KMeans
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
y_pred = kmeans.fit_predict(X)
print("Centroids coordinates:", kmeans.cluster_centers_)</code></pre>

<div class="callout callout-blue">
    <div class="callout-title">💡 How K-Means Works Step-by-Step (The Lloyd Algorithm):</div>
    <ol>
        <li>Randomly place $k$ centroids in the data space.</li>
        <li><b>Assignment Step:</b> Assign every data point to its closest centroid (Euclidean distance).</li>
        <li><b>Update Step:</b> Recompute each centroid's location as the mean (average) of all data points assigned to it.</li>
        <li>Repeat steps 2 and 3 until centroids stop moving (convergence).</li>
    </ol>
</div>

<div class="action-step">Step 2: Inertia and the Elbow Method</div>
<pre><code>inertias = []
for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=42).fit(X)
    inertias.append(km.inertia_)</code></pre>
<ul>
    <li><b>Inertia:</b> The sum of squared distances of samples to their closest cluster center. Lower is tighter.</li>
    <li><b>The Elbow Method:</b> As $k$ increases, inertia always drops. The optimal $k$ is located at the <b>"elbow"</b> of the curve &mdash; the point where increasing $k$ further yields diminishing returns.</li>
</ul>

<div class="action-step">Step 3: The Silhouette Score</div>
<pre><code>from sklearn.metrics import silhouette_score
score = silhouette_score(X, kmeans.labels_)</code></pre>
<ul>
    <li>Measures how close each sample is to other samples in its own cluster compared to samples in neighboring clusters.</li>
    <li>Ranges from -1 to +1:
        <ul>
            <li><b>+1:</b> Point is well inside its own cluster and far from others (ideal clustering).</li>
            <li><b>0:</b> Point is on the decision boundary between two clusters.</li>
            <li><b>-1:</b> Point may have been assigned to the wrong cluster.</li>
        </ul>
    </li>
</ul>

<hr style="border:none; border-top: 1px solid #e2e8f0; margin: 18px 0;">

<h2>6. Teacher's Technical Questions &amp; Exact Answers</h2>

<div class="qa-card">
    <div class="qa-q">Q1: "In Lab 1, why do we use fit_transform on training data, but only transform on test data?"</div>
    <div class="qa-a"><b>Your Answer:</b> <i>"Because fitting computes statistics like the mean, median, and variance. If we fit on the test data, our model peeks into the test set, creating 'data leakage'. To evaluate true real-world performance, all scaling and imputation rules must be learned strictly from the training set."</i></div>
</div>

<div class="qa-card">
    <div class="qa-q">Q2: "In Lab 2, how does Ridge regression prevent overfitting compared to standard Linear Regression?"</div>
    <div class="qa-a"><b>Your Answer:</b> <i>"Standard linear regression minimizes only the mean squared error, which can cause model weights to blow up when fitting noisy data. Ridge regression adds an L2 regularization penalty proportional to the sum of squared weights. This forces the model to keep weights as small as possible, resulting in a flatter, less sensitive curve that generalizes much better."</i></div>
</div>

<div class="qa-card">
    <div class="qa-q">Q3: "In Lab 3, why is accuracy a misleading metric when classifying rare events, and what do you use instead?"</div>
    <div class="qa-a"><b>Your Answer:</b> <i>"If only 1% of transactions are fraudulent, a dumb classifier that always predicts 'not fraud' will have 99% accuracy while catching zero fraud. On imbalanced data, accuracy is misleading. Instead, we use Precision, Recall, F1-Score, and the Area Under the ROC Curve (ROC-AUC), which evaluate true positive rates independently of class skew."</i></div>
</div>

<div class="qa-card">
    <div class="qa-q">Q4: "In Lab 5, what is the difference between Inertia and Silhouette Score in finding the optimal k in K-Means?"</div>
    <div class="qa-a"><b>Your Answer:</b> <i>"Inertia only measures how tight points are to their own cluster center, but it will always decrease towards zero as k increases towards the number of data points. Silhouette score is better because it compares the intra-cluster distance against the distance to the nearest neighboring cluster, giving a normalized score from -1 to +1 where the peak indicates true natural separation."</i></div>
</div>

<div class="qa-card">
    <div class="qa-q">Q5: "In Lab 1, why do we use One-Hot Encoding for nominal categories instead of integer labels (0, 1, 2)?"</div>
    <div class="qa-a"><b>Your Answer:</b> <i>"Integer encoding implies an artificial mathematical order (e.g., category 2 &gt; category 1). Linear models will mistakenly interpret this as a linear relationship. One-Hot Encoding creates independent binary columns for each category, allowing the algorithm to assign dedicated weights without assuming any numerical hierarchy."</i></div>
</div>

</body>
</html>
"""

pdf_output_path = os.path.join(BASE_DIR, "IAI600_Oral_Demonstration_Master_Guide_Labs_1_2_3_5.pdf")
HTML(string=html_content).write_pdf(pdf_output_path)
print(f"Generated Oral Demonstration Guide PDF at: {pdf_output_path}")
