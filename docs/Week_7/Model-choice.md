# Decision Journal – Week 7: Model Choice

**Date:** Week 7 – Model Optimisation & Trade-offs

## Context

* Week 6 established Logistic Regression as the strongest baseline model for predicting Emergency Severity Index (ESI) levels using the cleaned emergency department triage dataset.
* Week 7 investigated whether more sophisticated machine learning models could provide sufficient improvement to justify the additional computational cost and reduced interpretability.

---

## Alternatives Considered

* **Logistic Regression (Baseline)** – Simple, highly interpretable and achieved strong overall performance (Macro-F1 = 0.492).
* **Tuned Random Forest** – Performance improved after hyperparameter optimisation (Macro-F1 = 0.475) and provided moderate interpretability through feature importance.
* **Gradient Boosting** – Produced a Macro-F1 score of 0.416 but did not outperform the tuned Random Forest or Logistic Regression.
* **Small Multi-Layer Perceptron (MLP)** – Achieved the highest Macro-F1 score (0.498) but introduced greater model complexity and reduced interpretability.

---

## Decision

**The Logistic Regression model will remain the preferred model for Phase 3 while further benchmarking and validation are completed.**

---

## Reasoning

The Small MLP achieved the highest Macro-F1 score (0.498), but the improvement over the Logistic Regression baseline (0.492) was only 0.006, which may not justify the additional implementation complexity.
* Logistic Regression remains the most interpretable model, allowing clinicians to understand and explain model predictions more easily, which is important in emergency department decision-making.
* Additional evaluation of computational performance, inference time and external validation should be completed before replacing the current baseline with a more complex model.

---

## Things I Do Not Yet Know

* Whether the Small MLP maintains its performance advantage when evaluated on data collected from other hospitals within Barbados or the wider Caribbean.
* Whether the modest improvement in Macro-F1 would outweigh the additional computational, maintenance and operational costs associated with deploying a more complex model in routine clinical practice.

---

## Reflection

This week demonstrated that selecting the highest-performing machine learning model is not always the most appropriate decision in healthcare. Model selection should consider predictive performance alongside interpretability, computational requirements, deployment feasibility and patient safety. Future work will focus on validating these findings using additional datasets and completing the full deployment benchmark before recommending clinical implementation.
