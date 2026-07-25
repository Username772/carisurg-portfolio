# Model Selection Results 

## Model Comparison

The following models were evaluated during Weeks 6–7.

| Model | Key Hyperparameters | Accuracy | Macro F1 | Recall ESI 1 |
|---|---|---|---|---|
| Dummy Classifier | strategy=stratified | 0.375 | 0.204 | 0.00 |
| Decision Tree | max_depth=5, random_state=42 | 0.556 | 0.216 | 0.00 |
| **Logistic Regression (Winner)** | max_iter=1000, random_state=42 | **0.667** | **0.495** | **0.25** |

## Final Decision

Logistic Regression was selected as the recommended model.

The model achieved the strongest overall performance, with the highest accuracy and macro F1 score. It also identified some ESI Level 1 cases, unlike the Decision Tree and Dummy Classifier.

The final model choice will be pinned and configured during the final Week 8 submission.
