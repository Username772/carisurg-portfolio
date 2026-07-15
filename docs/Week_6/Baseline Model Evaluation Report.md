#Week 6 Interim Submission - CariSurg Healthcare AI Program
## AI-Assisted Triage: Data Exploration (Part 2 of 2)

**Date:** July 14, 2026

# Week 6 – Baseline Model Evaluation Report

---

## 1. Introduction

This report evaluates two baseline machine learning models, a **Logistic Regression** classifier and a **Decision Tree** classifier for predicting Emergency Severity Index (ESI) levels using the Mercer emergency department triage dataset. Their performance is compared against a stratified **DummyClassifier** baseline to determine whether the models provide meaningful predictive value beyond random guessing.

---

## 2. Model Results

### Table 1. Model Performance

| Model | Accuracy | Macro F1 | Recall (ESI 1) |
|-------|---------:|---------:|---------------:|
| Dummy Classifier | 0.375 | 0.204 | 0.00 |
| Logistic Regression | 0.667 | 0.495 | 0.25 |
| Decision Tree | 0.556 | 0.216 | 0.00 |

### Figure 1. Logistic Regression Confusion Matrix

![Figure 1 - Logistic Regression Confusion Matrix](docs/logistic_regression_confusion_matrix.png)

**Figure 1. Logistic Regression Confusion Matrix.** The confusion matrix for the Logistic Regression model showing the number of correct and incorrect predictions for each Emergency Severity Index (ESI) level.

The Logistic Regression model achieved the strongest overall performance, with an **accuracy of 66.7%**, substantially outperforming both the DummyClassifier baseline (**37.5%**) and the Decision Tree (**55.6%**). It also achieved the highest **Macro F1 score (0.495)**, indicating better balanced performance across all ESI classes.

### Figure 2. Decision Tree Confusion Matrix

![Figure 2 - Decision Tree Confusion Matrix](docs/decision_tree_confusion_matrix.png)

**Figure 2. Decision Tree Confusion Matrix.** The confusion matrix for the Decision Tree model showing the number of correct and incorrect predictions for each Emergency Severity Index (ESI) level.

The Decision Tree model achieved an **accuracy of 55.6%**, outperforming the Dummy Classifier but performing worse than the Logistic Regression model. Although the model was easy to interpret, it failed to correctly identify any **ESI Level 1** patients and frequently misclassified patients into **ESI Level 3**, indicating that it struggled to distinguish between different levels of clinical urgency.

The confusion matrix shows that the Decision Tree most frequently confused **ESI Level 2** with **ESI Level 3 (2,634 cases)** and **ESI Level 4** with **ESI Level 3 (1,769 cases)**. In addition, the model failed to correctly classify any **ESI Level 1** patients. This is a clinically important limitation because failing to recognise the most critically ill patients could delay urgent treatment and negatively affect patient outcomes.

The DummyClassifier served as a baseline representing random guessing while maintaining the class distribution. Both trained models exceeded this baseline, demonstrating that meaningful patterns were learned from the data.

---

## 3. Primary Metric Justification

The primary evaluation metric selected for this project is **Recall for ESI Level 1**.

In emergency triage, missing a critically ill patient has far greater clinical consequences than incorrectly classifying a stable patient as more urgent. Recall measures the proportion of actual ESI Level 1 patients that the model successfully identifies. Because ESI Level 1 represents the highest-acuity patients requiring immediate treatment, maximising recall helps reduce the likelihood that critically ill patients are overlooked. Although overall accuracy is useful, it can be misleading because the dataset contains far fewer ESI Level 1 cases than the other triage levels.

---

## 4. Failure-Mode Reflection

The greatest concern is the model's ability to identify **ESI Level 1** patients.

The Logistic Regression model correctly identified some critical patients, achieving a **recall of 0.25**, whereas the Decision Tree failed to identify any **ESI Level 1** patients. In addition, the Decision Tree frequently confused **ESI Level 2** with **ESI Level 3** and also misclassified many **ESI Level 4** patients as **ESI Level 3**.

### Figure 3. Decision Tree Visualization (max_depth = 5)

![Figure 3 - Decision Tree Visualization](docs/decision_tree_visualization.png)

**Figure 3. Decision Tree Visualization (max_depth = 5).** The trained Decision Tree showing the sequence of feature splits used to classify Emergency Severity Index (ESI) levels.

As shown in Figure 3, the decision tree first splits on **`cc_abdominalpain`**, suggesting that the model initially separates patients using a clinically relevant chief complaint. Although this makes the model easy to interpret, it still failed to correctly identify any **ESI Level 1** patients, indicating that additional features or more advanced modelling approaches would be needed before clinical deployment.

If deployed in a clinical setting, failing to identify an **ESI Level 1** patient could delay life-saving treatment and negatively affect patient outcomes.

---

## 5. Conclusion

Both baseline models outperformed the DummyClassifier, demonstrating that the dataset contains useful predictive information. Logistic Regression achieved the strongest overall performance and was better able to identify critically ill patients than the Decision Tree. However, neither model achieved sufficiently high recall for **ESI Level 1** to support clinical deployment. Future work should focus on improving performance for minority classes through additional feature engineering, class-balancing techniques, and validation using data from other hospitals.
