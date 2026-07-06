# Feasibility Memo Outline – Week 5

## Preliminary Verdict

The emergency department triage dataset appears suitable for development of a baseline machine learning model, subject to appropriate handling of missing values, data quality issues, and validation of clinically important variables.

## Dataset Summary

The dataset contains emergency department patient encounters extracted from an electronic health record system. Variables include:

* Demographic information
* Triage-level assignment (ESI)
* Vital signs
* Clinical assessment variables
* Chief complaint indicators

The dataset provides information commonly used during emergency department triage and therefore has potential value for predictive modelling.

## Initial Data Quality Findings

### Missing Data

Several structured variables contain missing values that will require assessment before modelling.

### Data Types

The dataset contains numerical, categorical, and binary indicator variables. Some variables may require datatype conversion and standardisation.

### Outliers

Vital-sign variables should be reviewed against clinically plausible ranges to identify potential data-entry errors.

## Reasons to Proceed

### 1. Rich Clinical Information

The dataset contains multiple variables routinely used by clinicians when assigning triage priority.

### 2. Real-World Emergency Department Data

The dataset reflects actual clinical practice and emergency department workflows.

### 3. Large Feature Set

The number of available variables provides opportunities for identifying meaningful predictors of triage level.

## Main Concerns

### 1. Missing Values

Missing observations may affect model performance and require appropriate handling.

### 2. Potential Class Imbalance

The distribution of ESI categories may not be uniform and could affect predictive performance.

### 3. Feature Redundancy

Some variables may be highly correlated or clinically overlapping.

## Planned Visualisations

* Missingness heatmap
* ESI/Triage distribution
* Age distribution
* Race and ethnicity distribution
* Chief complaint frequency analysis

## Week 6 Next Steps

* Complete cleaning decisions
* Finalise data-quality assessment
* Produce top-10 feature shortlist
* Develop baseline triage prediction model
