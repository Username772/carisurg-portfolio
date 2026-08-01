# Document 3 – System Requirements Notes
**Project:** AI-Assisted Emergency Department Triage System

**Organisation:** Mercer General Hospital

**Preferred Implementation:** Human–Computer Interaction (HCI)

**Selected AI Model:** Logistic Regression

**Purpose:** Interim System Requirements Notes

### 1. System Vision
The proposed system is an Artificial Intelligence (AI)-assisted clinical decision support application designed to assist Emergency Department (ED) triage nurses in assigning Emergency Severity Index (ESI) levels.
The system integrates the previously developed Logistic Regression model into a nurse-facing dashboard that analyses routinely collected triage information and provides an evidence-based ESI recommendation.
The system is intended to improve consistency, efficiency, and decision support while ensuring that all final clinical decisions remain the responsibility of qualified healthcare professionals.

### 2. Intended Users
Primary Users
Emergency Department Triage Nurses
Secondary Users
Emergency Physicians
Charge Nurses
Clinical IT Staff
Quality Improvement Team
Hospital Administration

### 3. System Inputs
The AI system requires the following information before generating a recommendation.
Patient Information
Patient identification number
Age (where available)
Existing Electronic Health Record (EHR) information

#### Clinical Observations
Heart Rate
Blood Pressure
Respiratory Rate
Oxygen Saturation
Body Temperature
Blood Glucose

#### Clinical Assessment
Chief complaint
Initial nurse observations
Additional assessment notes (optional)

#### Data Sources
The system receives information through:

| Source | Purpose |
|--------|---------|
| Manual nurse entry | Chief complaint and observations |
| Medical devices | Vital signs |
| Electronic Health Record (EHR) | Previous patient information |


### 4. AI Processing
The deployed Logistic Regression model processes the available clinical information and predicts an Emergency Severity Index (ESI) level.
The prediction is generated using the trained model selected during Weeks 6–8 based on its balance of predictive performance, transparency, interpretability, and computational efficiency.

### 5. System Outputs
The dashboard presents:
Predicted ESI Level (1–5)
Confidence score
Colour-coded urgency indicator
Brief explanation of the recommendation
Recommendation status

### 6. Human Workflow
The proposed workflow is:
Patient arrives at the ED triage desk.
Nurse records initial clinical assessment.
Vital signs are entered manually or imported from monitoring devices.
The system analyses the available information.
The Logistic Regression model predicts the patient's ESI level.
The recommendation is displayed to the nurse.
The nurse reviews the recommendation.
The nurse either:
accepts the recommendation, or
overrides it based on clinical judgement.
The final ESI level is recorded in the Electronic Health Record.
The patient proceeds through the normal clinical pathway.

### 7. Functional Requirements
The system shall:

* FR1
Allow authorised clinical staff to log in securely.

* FR2
Accept patient demographic and clinical information through manual entry or integrated systems.

* FR3
Retrieve available patient information from the Electronic Health Record (EHR).

* FR4
Receive vital signs from compatible monitoring devices where available.

* FR5
Generate an Emergency Severity Index (ESI) recommendation using the deployed Logistic Regression model.

* FR6
Display the predicted ESI level together with a confidence score.

* FR7
Provide a nurse override option for every recommendation.

* FR8
Record the final clinician decision together with any override.

* FR9
Maintain an audit log of recommendations and user actions.

* FR10
Continue supporting manual triage if the AI system becomes unavailable.

### 8. Non-Functional Requirements
Performance
The system should display recommendations within 2 seconds of receiving complete patient information.

Reliability
The system should remain available during normal Emergency Department operations and recover safely following temporary interruptions.

Usability
The interface should:
minimise unnecessary user interactions,
remain readable under varied lighting conditions,
support clinicians experiencing workload and fatigue,
present information consistently.

Security
The system must:
require authenticated access,
encrypt patient information,
maintain secure audit logs,
comply with hospital data governance requirements.

Maintainability
The system should allow future model updates without requiring major interface redesign.

### 9. Integration Requirements
The proposed system should integrate with:
Electronic Health Record (EHR)
Hospital authentication service
Vital sign monitoring devices
Audit logging system
Existing Emergency Department workflow
The AI recommendation should appear within the existing triage process to minimise disruption to established clinical practice.

### 10. Failure Handling
If one or more system components fail:
Failure
System Response
EHR unavailable
Continue using manual patient entry.
Device connection lost
Allow manual entry of vital signs.
AI unavailable
Continue with standard manual triage procedures.
Power interruption
Restore the previous session where possible after restart.


### 11. Assumptions
The proposed implementation assumes:
Nurses have received appropriate system training.
Clinical staff retain responsibility for all patient care decisions.
Existing hospital infrastructure supports secure EHR integration.
Medical devices are maintained and calibrated according to hospital procedures.
