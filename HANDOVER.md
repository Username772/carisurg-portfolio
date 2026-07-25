# Project Handover

## Project Summary

This project develops an AI-assisted Emergency Department (ED) triage prediction model using a de-identified clinical dataset. The aim is to predict Emergency Severity Index (ESI) levels using patient and clinical features to support triage decision-making.

The project involved data exploration, preprocessing, baseline modelling, and comparison of machine learning approaches to identify a suitable predictive model.

---

## Final Model Decision

The recommended final model is:

**Logistic Regression**

Logistic Regression was selected because it achieved the best performance compared with the other models tested. It produced the highest accuracy and macro F1 score while improving identification of high-acuity ESI Level 1 patients.

---

## How to Run

The final training workflow will be executed using:

```bash
python scripts/train.py --config config.yaml
