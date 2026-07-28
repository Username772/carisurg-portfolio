# AI-Assisted Emergency Department Triage (Portfolio)

## Overview

This repository contains the Week 5–8 project completed as part of the **CariSurg Healthcare AI Programme**. The objective is to investigate whether machine learning can assist Emergency Department (ED) clinicians by predicting Emergency Severity Index (ESI) levels using routinely collected triage information.

The project follows a reproducible machine learning workflow, including data preparation, feature engineering, model development, model evaluation, and project refactoring into a modular Python package.

---

## Project Structure

```text
AI-Assisted-ED-Triage/
│
├── config.yaml
├── HANDOVER.md
├── requirements.txt
├── README.md
├── LICENSE (MIT)
├── .gitignore
│
├── data/
│   └── triage_cleaned_v1.csv → Placeholder for Week 0 dataset (not stored in repo for governance reasons)
│
├── docs/
|   ├── Week_1/*.pdf
|   ├── Week_5/*.md and *.pdf
|   ├── Week_6/*.md
|   ├── Week_7/*.md
│   └── model-selection.md
│
├── models/
│   └── logistic_regression.joblib
│
├── notebooks/
│   |── Week_0/*.ipynb
|   ├── Week_5/*.ipynb
|   |       ├── missingness_matrix.png
│   ├── Week_6/*.ipynb
│   └── Week_7/*.ipynb
│
├── scripts/
│   └── train.py
│
├── src/
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── utils.py
│
└── tests/
    ├── test_data.py
    └── test_model.py
```

---

## Final Model

The final Phase 3 model is **Logistic Regression**.

Although the Small Multi-Layer Perceptron (MLP) achieved the highest Macro-F1 score during Week 7, its improvement over Logistic Regression was only **0.006**. Logistic Regression was selected because it provides strong predictive performance while remaining interpretable, computationally efficient, and easier to maintain in a clinical environment.

---

## Requirements

* Python 3.10 or later
* pip

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Train the final model using:

```bash
python scripts/train.py --config config.yaml
```

The script will:

* Load the cleaned dataset.
* Perform feature engineering.
* Split the data into training and testing sets.
* Train the Logistic Regression model.
* Evaluate model performance.
* Save the trained model.

---

## Running the Tests

Run the project sanity checks with:

```bash
pytest
```

The tests verify:

* Dataset loading and expected schema.
* Successful execution of the model training pipeline.

---

## Dataset

The project uses the cleaned emergency department triage dataset:

```text
data/triage_cleaned_v1.csv
```

The dataset contains de-identified emergency department encounters collected from a Caribbean healthcare institution and is intended for educational and research purposes only.

---

## Model Selection

A summary of all models evaluated during Weeks 6 and 7 is available in:

```text
docs/model-selection.md
```

The document records the evaluation metrics, comparison of alternative models, and justification for selecting the final model.

---

## Documentation

Additional project documentation is located in the `docs/` directory:

* `HANDOVER.md` – Project handover for future developers.
* `model-selection.md` – Audit trail of model evaluation and final selection.

---

## Author

CariSurg Healthcare AI Programme

Week 8 – Reproducibility & Modular Project Design
