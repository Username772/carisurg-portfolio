# Document 2 – Preferred Co-Design Canvas (HCI)

**Preferred Implementation:** Human–Computer Interaction (HCI)

**Deployment Location:** Mercer General Hospital Emergency Department Triage Desk

**AI Model:** Logistic Regression (Week 8 Selected Model)

## Problem
**Current Situation**

Emergency Department (ED) triage nurses at Mercer General Hospital are responsible for rapidly assessing patients and assigning an Emergency Severity Index (ESI) level based on their clinical presentation. During periods of high patient volume, frequent interruptions, and extended shifts, maintaining consistent triage decisions becomes increasingly challenging.

Although experienced clinicians use established triage protocols, variations in workload and fatigue may contribute to inconsistent prioritisation and longer waiting times for some patients.

## Proposed Solution
The proposed Human–Computer Interaction (HCI) system integrates the previously developed **Logistic Regression** model into a nurse-facing dashboard. The system analyses routinely collected triage information and generates an evidence-based recommendation for the patient's ESI level.

The recommendation is presented alongside a confidence score and supporting information to assist, rather than replace, clinical judgement. The nurse reviews the recommendation and retains full authority to accept or override the suggested triage level before finalising the patient's assessment.

## Stakeholders
**Primary Stakeholders**
* Emergency Department Triage Nurses
* Emergency Physicians
## Secondary Stakeholders
* Dr. De Fretias (Clinical Lead)
* Sister Patrice Alleyne (Nurse Manager)
* Martina Griffith (Clinical IT Lead)
* Mercer Integration Review Board
* Hospital Administration
* Patients

## Expected Benefits
**Clinical**
* Improved consistency in ESI classification.
* Faster patient prioritisation.
* Earlier identification of higher-acuity patients.
* Reduced variation in triage decisions.

## Operational
* Reduced nurse cognitive workload during busy shifts.
* More efficient patient flow.
* Better utilisation of clinical resources.
* Standardised decision support across staff.

## MVP (Minimum Viable Product)

The initial deployment focuses on the core functionality required to support Emergency Department triage while remaining simple, reliable, and practical for everyday clinical use.

The MVP includes:

Secure clinician login
Patient information entry and retrieval from the Electronic Health Record (EHR)
Automatic import of vital signs from compatible monitoring devices
Logistic Regression model generating an Emergency Severity Index (ESI) recommendation
Display of the predicted ESI level, confidence score, and brief AI explanation
Nurse ability to accept or override the AI recommendation
Automatic recording of the final triage decision and audit log

Advanced capabilities such as predictive patient flow analytics, robotic integration, and advanced clinical decision support are outside the scope of the MVP and may be introduced in future versions of the system.


## Ethics
The proposed system has been designed to support ethical, transparent, and safe use of Artificial Intelligence within a clinical environment.

## Human Oversight
The AI system functions solely as a clinical decision-support tool.
The triage nurse remains responsible for:
* assessing the patient,
* interpreting the AI recommendation,
* making the final clinical decision.
  
The AI never assigns an ESI level independently.

## Transparency
The system should clearly communicate:
* Predicted ESI level.
* Confidence score.
* Key clinical factors contributing to the recommendation.
* Whether the recommendation has been accepted or overridden.

This transparency supports clinician trust and accountability.

## Fairness
The deployed model avoids using fairness-sensitive demographic variables, such as race and ethnicity, because these showed minimal performance benefit during model development while introducing potential ethical concerns.

The system instead focuses on clinically relevant information, including:
* Vital signs
* Chief complaint
* Initial clinical assessment

This approach aligns with the project's objective of supporting equitable clinical decision-making.

## Privacy and Confidentiality
The system must protect patient information by:
* using authenticated user access,
* encrypting stored and transmitted data,
* complying with institutional governance policies,
* maintaining secure audit logs of system activity.

Only authorised healthcare professionals should have access to patient information and AI recommendations.

## Accountability
Every AI recommendation should be recorded together with:
* final clinician decision,
* override status,
* timestamp,
* authenticated user.

Maintaining an audit trail supports quality improvement, clinical governance, and future model evaluation.

## Safety
The system has been designed to minimise clinical risk by:
* allowing nurse override,
* supporting manual triage procedures if unavailable,
* presenting recommendations clearly,
* avoiding automated clinical actions.
If the system becomes unavailable, staff continue using existing hospital triage procedures without interruption.

## Guidelines / Human-Centred Design Principles

The dashboard was designed using human-centred design principles by presenting only the information required during triage, reducing unnecessary cognitive load, supporting rapid decision-making, and ensuring clinicians remain in control of all final patient decisions. High-contrast visual elements, consistent navigation, and clear AI explanations improve usability while maintaining transparency and patient safety.

The interface follows these design guidelines:

Consistency: Similar layouts, navigation, and controls are used throughout the interface to reduce learning time.
Visibility: Critical patient information and AI recommendations are immediately visible without unnecessary navigation.
Feedback: The system provides clear confirmation when recommendations are generated, accepted, overridden, or saved.
User Control: Nurses retain complete authority to override AI recommendations at any time.
Error Prevention: Confirmation prompts and validation checks reduce accidental data entry errors.
Accessibility: High-contrast colours, large fonts, simple icons, and colour combined with text improve usability for all clinicians.


## Environment
The system is intended for deployment within the Emergency Department triage area at Mercer General Hospital.

The design reflects the operational conditions described in the Week 9 tutorial.

## Physical Environment
The triage desk is a busy clinical workspace characterised by:
* high patient turnover,
* limited desk space,
* multiple clinicians working simultaneously,
* continuous interruptions.

The interface must remain usable despite these conditions.

## Environmental Constraints
The design considers several operational challenges identified in the tutorial materials:


**High Noise Levels**


The Emergency Department frequently exceeds normal conversational noise levels.

Therefore:
* visual alerts are prioritised,
* audio notifications are limited to critical events.

## Lighting Conditions
Variable lighting and screen glare may reduce visibility.

The interface therefore uses:
* high-contrast colours,
* large typography,
* simple icons,
* colour combined with text rather than colour alone.

## Staff Fatigue
Nurses commonly work extended shifts.

To reduce cognitive workload, the interface should:
* minimise unnecessary clicks,
* present only essential information,
* maintain a consistent screen layout,
* avoid unnecessary alerts.

## Power Instability
As discussed during the Week 9 tutorial, Caribbean healthcare facilities may experience temporary power interruptions or generator operation.

The system should therefore:
* automatically save entered information,
* recover previous sessions after restart,
* support graceful degradation,
* allow manual triage when unavailable.

## Workflow Integration
The system should integrate with existing hospital infrastructure by connecting to:
* Electronic Health Record (EHR)
* Vital sign monitoring devices
* Hospital authentication services
* Clinical audit logging

The AI system should complement existing workflows without introducing additional administrative burden.
