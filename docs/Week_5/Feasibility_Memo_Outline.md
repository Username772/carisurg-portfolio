---

# Week 5 AI-Assisted Emergency Department Triage Dataset – Feasibility Memo (Outline)

**Prepared for:** Dr. De Fretias & Emergency Department Board

## 1. Executive Verdict

* Preliminary assessment of whether the dataset is suitable for AI-assisted triage prediction.
* Brief statement outlining the need for preprocessing and validation before model development.

---

## 2. Dataset Summary

* Overview of the emergency department dataset.
* Number of patient encounters and clinical variables.
* Target variable (Emergency Severity Index - ESI).
* Types of variables available:

  * Demographics
  * Arrival information
  * Triage vital signs
  * Chief complaints
  * Clinical disposition

---

## 3. Data Quality Assessment

### 3.1 Missing Data

* Summary of missingness analysis.
* Discussion of structured variable completeness.
 **Figure 1:** Missingness Matrix

### 3.2 Demographic Characteristics

* Summary of age, gender, race, and ethnicity.
* Importance of demographics for understanding the patient population.
* **Figure 2:** Race and Ethnicity Distribution

### 3.3 Chief Complaint Distribution

* Overview of the most common presenting complaints.
* Clinical relevance to emergency department triage.
* **Figure 3:** Top Chief Complaints

### 3.4 Vital Signs

* Overview of triage vital-sign distributions.
* Identification of potential outliers and clinical variability.
* **Figure 4:** Distribution of Triage Vital Signs Across ESI Levels

---

## 4. Top Three Reasons to Proceed

* Rich clinical information available.
* High completeness of structured variables.
* Large sample size suitable for predictive modelling.

---

## 5. Top Three Data Quality Concerns

* Class imbalance across ESI categories.
* High-dimensional chief complaint variables.
* Presence of potential clinical outliers.

---

## 6. Planned Top-10 Candidate Predictive Features

* Respiratory Rate
* Heart Rate
* Oxygen Saturation
* Systolic Blood Pressure
* Temperature
* Age
* Chief Complaint
* Pain Score
* Arrival Mode
* Previous Disposition

---

## 7. Limitations

* Single-site dataset.
* Need for preprocessing and feature engineering.
* Potential fairness and generalisability considerations.

---

## 8. Recommendation to the ED Board

* Summarise preliminary findings.
* Outline planned preprocessing and validation steps.
* State that a final feasibility recommendation will be confirmed after completion of the full exploratory analysis.
---
## Week 6 Next Steps

* Complete cleaning decisions
* Finalise data-quality assessment
* Produce top-10 feature shortlist
* Develop baseline triage prediction model
