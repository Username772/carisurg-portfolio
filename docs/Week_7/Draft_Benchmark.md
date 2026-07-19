#Week 7 Interim Submission - Model Optimisation & Trade-offs - Draft Benchmark

---
**Draft Benchmark Table**

| Model                          |  Macro-F1 | Status    | Comments                                                                                        |
| ------------------------------ | :-------: | --------- | ----------------------------------------------------------------------------------------------- |
| Baseline (Logistic Regression) | **0.492** | Completed | Week 6 baseline used for comparison.                                                            |
| Random Forest                  | **0.390** | Completed | Lowest macro-F1 of the evaluated models.                                                        |
| Random Forest (Tuned)          | **0.475** | Completed | Hyperparameter tuning improved performance compared with the untuned Random Forest.             |
| Gradient Boosting              | **0.416** | Completed | Performed better than the untuned Random Forest but below the tuned Random Forest and baseline. |
| Small MLP                      | **0.498** | Completed | Achieved the highest macro-F1 in the current benchmark.                                         |


---

**Initial Benchmark Discussion**

Five models were benchmarked using macro-F1 to compare overall performance across all Emergency Severity Index (ESI) classes. The Small Multi-Layer Perceptron (MLP) achieved the highest macro-F1 score (0.498), narrowly outperforming the Week 6 Logistic Regression baseline (0.492). Hyperparameter tuning improved the Random Forest model from 0.390 to 0.475, demonstrating that optimisation increased predictive performance. Gradient Boosting achieved a macro-F1 of 0.416, outperforming the untuned Random Forest but remaining below the tuned Random Forest and baseline model. These initial findings suggest that more complex models can improve predictive performance; however, the improvements should also be evaluated alongside training time, inference time, and interpretability before making a deployment decision.


---

**Preliminary Recommendation**

Based on the current macro-F1 results, the Small MLP is the leading candidate for further evaluation. However, a final recommendation should only be made after completing the full six-axis benchmark, including accuracy, precision, recall, training time, inference time, and interpretability, as outlined in Week 7 Tutorial 3.
