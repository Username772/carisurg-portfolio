# Model Selection Results (Weeks 6– 7)

This document summarises the machine learning models evaluated during Weeks 6 and 7 of the AI-Assisted Emergency Department Triage project. It provides an audit trail of the model selection process and records the rationale for selecting the final model for Phase 3.

| Model | Key Hyperparameters | Accuracy | Precision | Recall | Macro-F1 | Training Time | Inference Time | Status |
|-------|----------------------|---------:|----------:|--------:|---------:|--------------|---------------|--------|
| Dummy Classifier | strategy="stratified" | 0.375 | N/A | 0.00 (ESI 1) | 0.204 | Not measured (interim) | Not measured (interim) | Baseline |
| Logistic Regression | max_iter=1000, random_state=42 | 0.667 | See Week 6 Report | 0.25 (ESI 1) | 0.492 | Not measured (interim) | Not measured (interim) | ✅ **Final Selected Model** |
| Decision Tree | max_depth=5, random_state=42 | 0.556 | See Week 6 Report | 0.00 (ESI 1) | 0.216 | Not measured (interim) | Not measured (interim) | Week 6 Baseline |
| Random Forest | Default | N/A | N/A | N/A | 0.390 | Not measured (interim) | Not measured (interim) | Evaluated |
| Tuned Random Forest | RandomizedSearchCV | N/A | N/A | N/A | 0.475 | Not measured (interim) | Not measured (interim) | Evaluated |
| Gradient Boosting | Default | N/A | N/A | N/A | 0.416 | Not measured (interim) | Not measured (interim) | Evaluated |
| Small Multi-Layer Perceptron (MLP) | Tuned neural network | N/A | N/A | N/A | 0.498 | Not measured (interim) | Not measured (interim) | Highest Macro-F1 |

## Final Model Decision

Although the Small Multi-Layer Perceptron (MLP) achieved the highest Macro-F1 score (0.498), Logistic Regression was selected as the final Phase 3 model.

The Small MLP improved the Macro-F1 score by only 0.006 (0.498 compared with 0.492), which was considered insufficient to justify the additional model complexity and reduced interpretability. Logistic Regression remains easier to explain, maintain and deploy within a clinical environment while still providing strong predictive performance.

This decision follows the conclusions documented in the Week 7 Decision Journal and the Week 7 Cost–Benefit Memo.

## Recommendation

Based on the evaluation conducted during Weeks 6 and 7, **Logistic Regression** is recommended as the final Phase 3 model for the AI-Assisted Emergency Department Triage project. Although the Small Multi-Layer Perceptron (MLP) achieved the highest Macro-F1 score (0.498), its improvement over Logistic Regression (0.492) was only 0.006. This marginal increase does not justify the additional model complexity and reduced interpretability at the current stage of the project.

Logistic Regression provides strong predictive performance while remaining transparent, computationally efficient, and easier for clinicians to understand and trust. It will therefore remain the pinned model for Phase 3, with additional benchmarking, inference-time testing, and external validation to be completed before any future deployment decisions.

## Notes

- Training time and inference time were not benchmarked during the interim submission and will be completed before the final Week 8 submission.
- The selected Logistic Regression model will remain the recommended Phase 3 model pending additional benchmarking and external validation before clinical deployment.
