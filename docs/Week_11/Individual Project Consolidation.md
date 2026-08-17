# Week 11: Individual Project Consolidation

## Purpose

This section consolidates my **individual project contributions** completed throughout Weeks 5–10 and documents the final state of my individual work for project handover.

Week 11 focuses on consolidation rather than developing a new model or prototype. The purpose of this submission is to organise, document, and finalise the individual artefacts developed throughout the project so that a first-time reader can understand the work, modelling decisions, system concept, limitations, and reproducibility considerations.

My individual modelling pathway used **Logistic Regression**. The group subsequently selected **Gradient Boosting** as its model for the group implementation and final presentation. Therefore, the modelling results and model decision documented in this individual submission represent **my individual project work** and should be distinguished from the group's final model selection.

---

## Repository Overview

This repository documents my individual contribution to the AI-assisted Emergency Department (ED) triage proof-of-concept developed throughout Weeks 5–11.

The individual project includes:

- Data exploration and preparation
- Baseline machine-learning modelling
- Model comparison and evaluation
- Feature engineering and model optimisation
- Logistic Regression modelling
- Reproducible project structure
- Handover documentation
- HCI/HRI prototype development
- Safety and failure-handling considerations
- Accessibility considerations
- Model limitations and deployment considerations

The repository is intended to provide a clear record of my individual work and allow another developer or researcher to understand the modelling workflow and supporting system artefacts.

---

## Final Individual Contribution

My completed individual work includes:

- Data exploration and preparation.
- Baseline machine-learning modelling.
- Model comparison and evaluation.
- Feature engineering and model optimisation.
- Selection of Logistic Regression as my preferred individual proof-of-concept model.
- Reproducible project structure and handover documentation.
- HCI/HRI prototype development.
- Safety and failure-handling considerations.
- Accessibility considerations.
- Documentation of limitations and deployment considerations.

These artefacts represent my individual contribution to the wider AI-assisted ED triage project.

---

## Individual Model Decision

For my **individual project work**, Logistic Regression was retained as my preferred proof-of-concept model.

Among the models evaluated during my individual modelling work, Logistic Regression achieved the strongest Macro-F1 result:

**Macro-F1: 0.495**

The model was selected based on its performance, interpretability, and suitability for a clinical decision-support context.

The model is intended for **clinical decision support only** and should not autonomously determine patient triage priority.

The limited ESI 1 recall remains an important safety limitation and indicates that further validation and model improvement would be required before any clinical deployment.

---

## Model Evaluation

The individual modelling work considered multiple approaches and used evaluation measures appropriate for the imbalanced ESI classification problem.

Key evaluation considerations included:

- Accuracy
- Macro-F1
- ESI 1 recall
- Comparison against baseline performance
- Model interpretability
- Clinical safety implications

Macro-F1 was emphasised because the ESI classes were imbalanced and overall accuracy alone could obscure poor performance on less frequent classes.

The limited recall for ESI 1 was treated as a significant safety concern because failure to identify a critically ill patient could have serious clinical consequences.

---

## Relationship to the Group Model

The individual and group projects followed different model-selection outcomes.

| Project Component | Individual Work | Group Work |
|---|---|---|
| Model | Logistic Regression | Gradient Boosting |
| Model Selection | Individual decision | Group decision |
| Results | Individual modelling results | Group modelling results |
| Final Presentation | Individual contribution where applicable | Group-selected approach |

The difference in model selection meant that some aspects of my individual modelling research could not be directly incorporated into the group's final model without modification.

I discussed the differences between the models with the group and continued contributing ideas and feedback toward the group's final project and presentation.

This individual repository therefore retains the Logistic Regression results because they accurately represent the work I completed individually.

---

## System Design

My individual project proposed an AI-assisted ED triage workflow based on a **human-in-the-loop** approach:

**Patient information → AI recommendation → Clinician review → Final clinical decision**

The AI system is intended to provide decision support rather than replace clinical judgement.

The proposed system includes:

- Patient information and triage data
- Machine-learning prediction
- Urgency communication
- Clinician review
- Human confirmation of the final triage decision
- Manual fallback procedures when the AI system is unavailable

The system concept was developed with the ED environment and potential Observation Unit deployment in mind.

---

## HCI/HRI Prototype

The individual project included human-centred interface concepts developed during Week 9.

### Nurse-Facing HCI

The proposed ED triage dashboard presents AI recommendations in a format intended to support rapid interpretation by clinical staff.

Design considerations included:

- Clear urgency levels
- Readable alert language
- Minimal ambiguity
- Appropriate visual hierarchy
- Clinician confirmation
- Avoidance of unnecessary alarm escalation

### Observation Unit HRI

An additional concept considered the potential use of a kiosk interface alongside a robot-assisted vital-sign station in the Observation Unit.

The design considered:

- Patient interaction
- Accessibility
- Physical proximity
- Sensor reliability
- Voice interaction in noisy environments
- Manual fallback procedures

These prototypes represent proof-of-concept designs rather than clinically deployed systems.

---

## Human-Centred Design and Safety

The individual project incorporated safety and human-centred considerations into the proposed AI-assisted triage workflow.

Key considerations included:

- Automation bias and over-reliance on AI.
- Alarm fatigue.
- Ambiguous alert interpretation.
- Screen legibility and accessibility.
- Failure of connected medical devices.
- AI or system unavailability.
- Manual fallback procedures.
- Accountability for the final clinical decision.
- Sensor and voice-recognition limitations.
- Physical safety considerations for the HRI environment.

The proposed system therefore maintains **human clinical oversight** as a core safety requirement.

---

## Failure Handling

The prototype considers several potential system failures.

| Failure | Proposed Response |
|---|---|
| EHR unavailable | Manual patient information entry |
| Device connection lost | Manual vital-sign entry |
| AI unavailable | Continue manual triage |
| Power interruption | Restore previous session where possible |
| Sensor failure | Clinician verification and manual measurement |
| Ambiguous AI output | Clinician review rather than automatic action |

These mechanisms are intended to prevent the AI system from becoming a single point of failure in the clinical workflow.

---

## Reproducibility and Handover

The individual repository has been organised so that another developer or researcher can understand the project, locate relevant artefacts, and reproduce the individual modelling workflow.

Key project components include:

- Source code
- Configuration
- Model artefact
- Documentation
- Model results
- HCI/HRI prototypes
- Safety considerations
- Handover documentation

The repository structure supports reproducibility and provides documentation of the decisions made throughout the individual project development process.

---

## Final Limitations

The individual proof of concept is limited by:

- Single-site Caribbean dataset.
- Class imbalance across ESI categories.
- Limited ESI 1 recall.
- No prospective clinical validation.
- No external validation.
- No live ED deployment.
- Further accessibility and usability testing required.
- Further evaluation and validation required before clinical implementation.

The model should therefore **not be treated as a clinically validated triage system**.

---

## Deployment Readiness

The individual system is **not ready for autonomous clinical deployment**.

Before a supervised pilot could be considered, further work would be required, including:

- External validation.
- Prospective clinical evaluation.
- Assessment of ESI 1 performance.
- Clinical safety review.
- Usability testing with intended users.
- Accessibility testing.
- Monitoring and audit procedures.
- Clear escalation and fallback procedures.
- Appropriate governance and data-protection review.

The proposed deployment position is therefore a **supervised proof-of-concept**, rather than autonomous clinical decision-making.

---

## Week 11 Completion

The **individual project work** is consolidated and documented in this repository.

My individual modelling work retained **Logistic Regression as the preferred proof-of-concept model**, based on the individual evaluation results, interpretability, and clinical decision-support requirements.

The group followed a separate model-selection process and ultimately selected **Gradient Boosting** for the group implementation and final presentation.

Although the individual and group models differ, my individual work contributed to the wider project through:

- Data analysis
- Machine-learning modelling
- Model evaluation
- Feature engineering
- Human-centred design
- HCI/HRI prototyping
- Safety analysis
- Failure handling
- Reproducibility
- Project handover

The final individual implementation remains a **proof of concept**, with human clinical oversight maintained as a core deployment requirement.

## Week 11 Completion

The individual project work is now consolidated and documented in the repository.

The final implementation remains a **proof of concept**, with Logistic Regression retained as the preferred model and human clinical oversight maintained as a core deployment requirement.
