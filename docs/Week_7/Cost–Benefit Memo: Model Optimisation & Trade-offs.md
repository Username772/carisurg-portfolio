#Week 7 Cost–Benefit Memo: Model Optimisation & Trade-offs

**Prepared for:** Dr. De Fretias, Emergency Department (ED) Board, and Martina Griffith (Clinical IT Lead)
**Project:** CariSurg Healthcare AI Programme – Week 7
**Subject:** Cost–Benefit Evaluation of More Complex Machine Learning Models for Emergency Department Triage

## Executive Verdict

Based on the current benchmark results, the Small Multi-Layer Perceptron (MLP) achieved the highest overall Macro-F1 score (0.498). However, its improvement over the Week 6 Logistic Regression baseline (0.495) was marginal. At this stage, the additional complexity of the MLP is not yet sufficiently justified for clinical deployment, and further evaluation of computational cost, inference speed and interpretability is recommended before replacing the simpler baseline model.

---

# 1. Background

Following the successful completion of the Week 6 baseline evaluation, the Emergency Department Board requested an assessment of whether a more sophisticated machine learning model would provide sufficient clinical benefit to justify its additional complexity.

In addition to predictive performance, Mercer IT Governance requested that the evaluation consider practical deployment issues, including computational cost, inference speed and model interpretability. These factors are important because emergency department triage requires rapid, reliable and clinically explainable predictions.

The objective of this study was therefore not simply to identify the highest-scoring model, but to determine which model provides the most appropriate balance between predictive performance, interpretability and deployment feasibility.

---

# 2. Dataset and Methods

The analysis used the same cleaned emergency department triage dataset developed during Weeks 5 and 6. The dataset contains demographic information, presenting complaints, vital signs and triage observations collected from a single Caribbean healthcare institution.

The same train–test split from Week 6 was reused to ensure a fair comparison between the baseline and more complex models.

Additional clinical features were engineered from the original vital signs, including:

* Shock Index
* Pulse Pressure
* Estimated Mean Arterial Pressure (MAP)
* Oxygen Saturation to Respiratory Rate Ratio
* Tachypnoea indicator
* Hypoxia indicator
* Fever indicator
* Red Flag Count

Several machine learning models were evaluated:

* Logistic Regression (Week 6 baseline)
* Random Forest
* Tuned Random Forest
* Gradient Boosting
* Small Multi-Layer Perceptron (MLP)

Random Forest hyperparameters were optimised using RandomizedSearchCV with three-fold cross-validation and Macro-F1 as the optimisation metric.

Model performance was evaluated primarily using Macro-F1 because it gives equal importance to all Emergency Severity Index (ESI) classes, including the relatively rare but clinically important ESI Level 1 patients.

---

# 3. Benchmark Results

## Table 1. Model Performance Comparison

| Model                        |  Macro-F1 | Summary                                                                                          |
| ---------------------------- | --------: | ------------------------------------------------------------------------------------------------ |
| Baseline Logistic Regression | **0.492** | Strong baseline model with good overall balance and high interpretability.                       |
| Random Forest                | **0.390** | Lowest-performing complex model.                                                                 |
| Tuned Random Forest          | **0.475** | Hyperparameter tuning improved performance considerably but remained below the baseline.         |
| Gradient Boosting            | **0.416** | Improved over the untuned Random Forest but underperformed the tuned Random Forest and baseline. |
| Small MLP                    | **0.498** | Highest Macro-F1 achieved during Week 7.                                                         |

Hyperparameter tuning produced a substantial improvement in Random Forest performance, increasing the Macro-F1 score from 0.390 to 0.475. This demonstrates that appropriate model optimisation can improve predictive performance without altering the underlying dataset.

Despite this improvement, the tuned Random Forest remained below the Logistic Regression baseline.

The Small MLP achieved the highest Macro-F1 score (0.498). However, compared with the Week 6 baseline (0.492), the improvement was only 0.006, representing a relatively small gain considering the increased model complexity.

These findings indicate that although more sophisticated models may improve predictive performance, the magnitude of improvement should be carefully weighed against deployment costs, interpretability and operational complexity before implementation within a clinical environment.
