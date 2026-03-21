# Home Credit Default Risk Analysis

This project predicts the probability of loan default for applicants using the **Home Credit** dataset. It demonstrates a complete data science lifecycle, featuring a comparative study between a baseline pipeline and an advanced feature-engineered pipeline.

* **Competition:** [Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk)
* **Dataset:** [Kaggle Data Link](https://www.kaggle.com/c/home-credit-default-risk/data)
---

## 🏗 Modeling Framework: Pipeline A vs. Pipeline B

The project is structured into two distinct pipelines to evaluate the impact of feature engineering and dimensionality:

### **Pipeline A: Traditional Credit Scoring (Baseline)**
* **Feature Set:** Focused on core applicant data (e.g., Income, Loan Amount, Age).
* **Preprocessing:** Implemented **WoE (Weight of Evidence) Binning** to transform raw variables into monotonic risk indicators.
* **Feature Selection:** Utilized **IV (Information Value)** to filter out weak predictors (maintaining variables with IV > 0.02).
* **Model:** Standard **Logistic Regression** to establish a baseline for credit scoring and probability of default (PD).

### **Pipeline B: Advanced Integrated Pipeline (187 Features)**
* **Feature Set:** Expanded to 187 features by integrating external sources (`EXT_SOURCE_1/2/3`), credit bureau history, and previous applications.
* **Key Enhancements:**
    * **Supervised Learning:** Implemented **Decision Tree** for logic visualization and **Random Forest** for ensemble predictive power.
    * **Dimensionality Reduction:** Applied **PCA** to compress 187 features into **88 principal components** (80% variance retained).
    * **Unsupervised Segmentation:** Performed **K-Means (K=5)** on PCA-transformed data to identify hidden risk personas.

---

## 📊 Key Results & Insights (Pipeline B)

By utilizing 187 features, we achieved significant risk differentiation across five customer clusters:

| Cluster ID | Default Rate | Avg Credit Score | Risk Level |
| :--- | :--- | :--- | :--- |
| **Cluster 0** | **9.90%** | 343.6 | **High Risk** |
| **Cluster 3** | 8.19% | 351.8 | Moderate Risk |
| **Cluster 4** | 5.71% | 373.7 | Low Risk |
| **Cluster 1** | 5.48% | 357.6 | Low Risk |
| **Cluster 2** | **5.35%** | **379.5** | **Premium Segment** |

---

## 📈 Model Performance Comparison
* **Logistic Regression (Pipeline A):** Provided stable interpretability with basic features.
* **Random Forest (Pipeline B):** Demonstrated superior AUC-ROC by capturing non-linear relationships among 187 features.
* **Clustering Analysis:** Validated the scoring model by showing a clear inverse relationship between cluster risk and credit scores.

---

## 💻 Tech Stack
* **Language:** Python 3.12
* **ML Framework:** `scikit-learn` (Logistic Regression, Decision Tree, Random Forest, PCA, KMeans)
* **Data Handling:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `seaborn`, `plotly`

---
