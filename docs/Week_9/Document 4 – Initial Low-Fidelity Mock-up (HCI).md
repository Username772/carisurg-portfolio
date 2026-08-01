# Document 4 – Initial Low-Fidelity Mock-up (HCI)
**Project:** AI-Assisted Emergency Department Triage Dashboard

**Deployment:** Mercer General Hospital – Emergency Department

**Primary User:** ED Triage Nurse

**AI Model:** Logistic Regression (Clinical Decision Support)

## Mock-up Description
The dashboard is designed to support nurses during the triage process by presenting patient information, AI-generated recommendations, and the ability to accept or override the recommendation. The design prioritises simplicity, readability, and rapid decision-making during busy Emergency Department operations.

## AI-Assisted Emergency Department Triage Dashboard Wireframe

```text
+--------------------------------------------------------------------------------+
| MERCER GENERAL HOSPITAL                         User: Nurse Williams | 03:12 AM |
|                                                        Logout                  |
+--------------------------------------------------------------------------------+
| PATIENT QUEUE                         | PATIENT DETAILS                       |
|---------------------------------------|---------------------------------------|
| 🔴 Patient 001  Waiting               | Patient ID: 00124567                 |
| 🟠 Patient 002  In Triage             | Name: ********                       |
| 🟡 Patient 003  Waiting               | Age: 62                              |
| 🟢 Patient 004  Observation           | Sex: Female                          |
| 🔴 Patient 005  Waiting               | Chief Complaint: Chest Pain          |
|                                       | Arrival Time: 02:58 AM              |
+---------------------------------------+---------------------------------------+
| VITAL SIGNS                           | AI TRIAGE RECOMMENDATION            |
|---------------------------------------|---------------------------------------|
| Heart Rate:          122 bpm          | Predicted ESI Level                 |
| Blood Pressure:      88 / 56          |                                       |
| Respiratory Rate:    28 bpm           |             🔴 LEVEL 2               |
| Oxygen Saturation:   89 %             |                                       |
| Temperature:         101.2°F          | Confidence: 92%                     |
| Blood Glucose:       184 mg/dL        |                                       |
|                                       | Clinical Factors:                   |
| [ Retrieve EHR ]                      | • High heart rate                   |
|                                       | • Low oxygen saturation             |
|                                       | • Elevated temperature              |
+---------------------------------------+---------------------------------------+
| CLINICAL NOTES                        | NURSE DECISION                      |
|---------------------------------------|---------------------------------------|
| ___________________________________   | ○ Accept AI Recommendation          |
| ___________________________________   | ○ Override Recommendation           |
| ___________________________________   |                                       |
| ___________________________________   | Override Reason (optional):         |
|                                       | _________________________________   |
|                                       |                                       |
|                                       | [ View Explanation ]                 |
|                                       | [ Save Final Decision ]              |
+---------------------------------------+---------------------------------------+
```

## Interface Features
### Patient Queue

Displays patients waiting for triage with priority indicators.

#### Purpose:
* Improve situational awareness.
* Support patient flow management.

## Patient Information Panel
### Displays:
* Patient identifier
* Chief complaint
* Vital signs
* Information retrieved from the Electronic Health Record (EHR)

### Purpose:
Provide all clinically relevant information in a single location.

### AI Recommendation Panel
#### Displays:
* Predicted ESI level
* Confidence score
* Colour-coded urgency
* Brief explanation for the recommendation
#### Purpose:
Support transparent and explainable AI-assisted decision-making.

#### Nurse Action Panel

Provides options to:
* Accept the recommendation.
* Override the recommendation.
* View additional explanation.
* Save the final decision.
  
#### Purpose:
Ensure the nurse retains full clinical authority.

## Accessibility Features
The dashboard incorporates several Human–Computer Interaction (HCI) principles:
* High-contrast colours to improve visibility under varying lighting conditions.
* Large, readable fonts to reduce visual strain during extended shifts.
* Simple navigation with clearly labelled buttons.
* Colour combined with text and symbols to avoid relying on colour alone.
* Consistent layout to minimise cognitive load.

### Alignment with Week 9 Tutorial Guidance
The design reflects the clinical environment described in the Week 9 tutorial by considering:
* High ambient noise: prioritises visual information over audio alerts.
* Variable lighting: uses high-contrast elements and large text.
* Shift fatigue: presents only essential information and minimises unnecessary interactions.
* Limited workspace: fits a standard triage workstation without requiring additional hardware.
* Power interruptions: supports manual workflow continuation if the system becomes unavailable.

### Design Rationale
The interface was designed around the Week 8 decision to deploy the Logistic Regression model because it provides transparent and reproducible clinical decision support while allowing nurses to retain responsibility for all patient care decisions.

The interface intentionally focuses on presenting the AI recommendation clearly rather than automating clinical decisions. This supports clinician trust, reduces the risk of over-reliance on AI, and aligns with the project's objective of improving triage consistency without replacing professional judgement.
