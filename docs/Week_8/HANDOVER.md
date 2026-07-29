# Project Handover

## Project Summary

This project was completed as part of the CariSurg Healthcare AI Programme to investigate whether machine learning could support Emergency Department (ED) triage by predicting Emergency Severity Index (ESI) levels from routinely collected triage data. The project followed a structured workflow beginning with data exploration and cleaning, followed by baseline model development, model optimisation, and reproducible software engineering practices. The final solution has been refactored into a modular Python project with reusable source code, configuration files, documentation, and automated sanity checks to support future development and maintenance.

---

## Final Model Decision

The final Phase 3 model is **Logistic Regression** with the hyperparameters defined in `config.yaml`.

Although a Small Multi-Layer Perceptron (MLP) achieved the highest Macro-F1 score (0.498), the improvement over Logistic Regression (0.492) was only 0.006. Logistic Regression was selected because it provides strong predictive performance while remaining transparent, reproducible, computationally efficient, and easier for clinicians to interpret.

---

## How to Run

1. Clone the project repository.

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Ensure the cleaned dataset is located at:

```text
data/triage_cleaned_v1.csv
```

4. Train the model using the project configuration:

```bash
python scripts/train.py --config config.yaml
```

The trained model will be saved to the location specified in `config.yaml`.

---

## Data Location and Governance

The project uses the cleaned emergency department triage dataset located in the `data/` directory.

The dataset consists of de-identified patient encounters collected from a single Caribbean healthcare institution for educational and research purposes. No personally identifiable patient information is included. Any future clinical deployment should comply with institutional governance, ethics approval, and applicable data protection policies.

---

## Known Limitations

* The dataset originates from a single healthcare institution and has not yet been externally validated using data from other hospitals.

* Emergency Severity Index (ESI) Level 1 cases are relatively uncommon, making prediction of the highest-acuity patients more challenging.

* Additional benchmarking, external validation, and prospective clinical evaluation should be completed before the model is considered for routine clinical deployment.
