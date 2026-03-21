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
* **Robustness Metrics:** * **KS Statistic:** Measured the model's ability to separate good and bad applicants.
    * **PSI (Population Stability Index):** Monitored distribution shifts between train and test sets to ensure model stability.
  
### **Pipeline B: Advanced Integrated Pipeline (187 Features)**
* **Feature Set:** Expanded to 187 features by integrating external sources (`EXT_SOURCE_1/2/3`), credit bureau history, and previous applications.
* **Key Enhancements:**
    * **Supervised Learning:** Implemented **Decision Tree** for logic visualization and **Random Forest** for ensemble predictive power.
    * **Dimensionality Reduction:** Applied **PCA** to compress 187 features into **88 principal components** (80% variance retained).
    * **Unsupervised Segmentation:** Performed **K-Means (K=5)** on PCA-transformed data to identify hidden risk personas.

---

## 📏 Evaluation Framework
To ensure a fair comparison, Logic Regression, Decision Tree, Random Forest) were benchmarked using a consistent set of risk metrics:
1. **ROC-AUC:** Measures the overall ranking ability and predictive accuracy.
2. **KS Statistic (Kolmogorov-Smirnov):** Evaluates the maximum separation between "Good" and "Bad" loan applicants.
3. **PSI (Population Stability Index):** Quantifies the distribution shift between Training and Test sets to ensure the models are robust against data drift.

---

## 💻 Tech Stack
* **Language:** Python 3.12
* **ML Framework:** `scikit-learn` (Logistic Regression, Decision Tree, Random Forest, PCA, KMeans)
* **Data Handling:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `seaborn`, `plotly`

---
