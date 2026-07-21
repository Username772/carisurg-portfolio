# Week 7 Cost–Benefit Memo: Model Optimisation & Trade-offs

**Prepared for:** Dr. De Fretias, Emergency Department (ED) Board, and Martina Griffith (Clinical IT Lead)

**Project:** CariSurg Healthcare AI Programme – Week 7

**Subject:** Cost–Benefit Evaluation of More Complex Machine Learning Models for Emergency Department Triage

## Executive Verdict

Based on the current benchmark results, the Small Multi-Layer Perceptron (MLP) achieved the highest overall Macro-F1 score (0.498). However, its improvement over the Week 6 Logistic Regression baseline (0.492) was only 0.006, indicating a marginal increase in predictive performance. At this stage, the additional complexity of the MLP is not yet sufficiently justified for clinical deployment, and further evaluation of computational cost, inference speed and interpretability is recommended before replacing the simpler baseline model.

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
| Small MLP                    | **0.498** | Highest Macro-F1 achieved during Week 7, although only 0.006 higher than the Logistic Regression baseline.                                                       |

Hyperparameter tuning produced a substantial improvement in Random Forest performance, increasing the Macro-F1 score from 0.390 to 0.475. This demonstrates that appropriate model optimisation can improve predictive performance without altering the underlying dataset.

Despite this improvement, the tuned Random Forest remained below the Logistic Regression baseline.

The Small MLP achieved the highest Macro-F1 score (0.498). However, compared with the Week 6 baseline (0.492), the improvement was only 0.006, representing a relatively small gain considering the increased model complexity.

These findings indicate that although more sophisticated models may improve predictive performance, the magnitude of improvement should be carefully weighed against deployment costs, interpretability and operational complexity before implementation within a clinical environment.


# 4. Arguments Supporting the Recommended Model

Although the Small Multi-Layer Perceptron (MLP) produced only a modest improvement over the Logistic Regression baseline, it achieved the highest Macro-F1 score (0.498) among all models evaluated. This indicates that the MLP provided the strongest overall balance of predictive performance across all Emergency Severity Index (ESI) classes.

### Argument 1 – Highest Overall Predictive Performance

The Small MLP achieved the highest Macro-F1 score of all evaluated models. Macro-F1 was selected because it gives equal importance to every triage class, including the relatively uncommon but clinically important ESI Level 1 patients. A higher Macro-F1 suggests the model performs more consistently across both majority and minority classes.

### Argument 2 – Ability to Model Complex Relationships

Unlike Logistic Regression, which assumes a linear relationship between predictors and outcomes, the MLP can learn more complex non-linear relationships among patient demographics, presenting complaints and physiological observations. Emergency department triage decisions often involve interactions between multiple clinical variables, making this additional modelling capability potentially valuable.

### Argument 3 – Future Scalability

Although the current performance gain is small, neural networks generally provide greater flexibility as additional clinical variables become available. Future versions of the triage system may incorporate laboratory results, imaging information or electronic health record data, allowing a neural network to take advantage of richer clinical information.

---

# 5. Arguments Against the Recommended Model

Despite producing the highest Macro-F1 score, several factors limit the immediate suitability of the Small MLP for deployment within the emergency department.

### Argument 1 – Only a Marginal Improvement

The Small MLP achieved a Macro-F1 score of 0.498 compared with 0.492 for the Week 6 Logistic Regression model. This improvement of only 0.006 is unlikely to produce a meaningful clinical benefit on its own. Such a small increase should be interpreted cautiously before investing additional computational resources or increasing system complexity.

### Argument 2 – Reduced Interpretability

Logistic Regression provides transparent coefficients that can be more readily explained to clinicians, whereas neural networks operate largely as "black box" models. In a clinical environment, explainability is important because healthcare professionals must understand and trust the reasoning behind model recommendations before integrating them into patient care.

### Argument 3 – Greater Computational Complexity

Neural networks generally require more computational resources during both training and deployment than simpler statistical models. Although the Small MLP evaluated in this project is relatively lightweight, increased computational requirements may still affect scalability, maintenance and operational costs if deployed across multiple healthcare facilities.

---

# 6. Risks and Unknowns

Several limitations should be considered before progressing to clinical implementation.

The dataset represents patient encounters from a single Caribbean healthcare institution. Consequently, model performance may differ when applied to hospitals with different patient populations, workflows or clinical practices. External validation using data from additional hospitals within Barbados or the wider Caribbean would therefore be required before deployment.

The relatively small number of ESI Level 1 cases remains an important limitation. Although Macro-F1 provides a balanced measure of performance across all classes, further work should continue to prioritise improving the identification of critically ill patients, as delayed recognition could adversely affect patient outcomes.

This evaluation focused primarily on predictive performance. Additional benchmarking of training time, inference time and operational resource requirements should be completed before selecting a production model.

---

# 7. Final Recommendation

The Small Multi-Layer Perceptron achieved the highest Macro-F1 score during this evaluation. However, the improvement over the Logistic Regression baseline was modest. Considering the increased model complexity and reduced interpretability, there is currently insufficient evidence to recommend replacing the existing baseline model for clinical deployment.

Instead, the Logistic Regression model should remain the preferred candidate for Phase 3 while further benchmarking is undertaken. Future work should evaluate computational performance, inference speed, model explainability and external validation before considering implementation within routine emergency department practice.

---

# Conclusion

This study demonstrates that more sophisticated machine learning models do not necessarily provide sufficiently large performance improvements to justify their additional complexity. While the Small MLP achieved the highest Macro-F1 score, its advantage over the Logistic Regression baseline was minimal. The results therefore support a cautious approach in which predictive performance is balanced against interpretability, computational cost and clinical usability. This approach aligns with the objectives of the Emergency Department Board and Mercer IT Governance by ensuring that any future deployment is evidence-based, transparent and appropriate for a high-risk clinical environment.

