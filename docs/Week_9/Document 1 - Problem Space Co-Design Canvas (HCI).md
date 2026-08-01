# Document 1 – Problem Space Co-Design Canvas

## Problem Space Co-Design Canvas (HCI)
Implementation Setting
Emergency Department (ED) Triage Desk

## Problem
Emergency Department nurses at Mercer General Hospital must rapidly assess incoming patients to determine their Emergency Severity Index (ESI) level. During periods of high patient volume, time pressure, interruptions, and staff fatigue can make consistent triage more challenging. The current process relies heavily on manual assessment, increasing the risk of delays and variability in prioritisation.
The proposed Human–Computer Interaction (HCI) solution integrates the previously developed Logistic Regression model into a nurse-facing dashboard that provides an evidence-based ESI recommendation. The system is designed to support clinical decision-making while ensuring that the nurse remains responsible for the final triage decision.

## Primary User
Emergency Department Triage Nurse

## Secondary Users
Emergency Physicians
Charge Nurse
Clinical IT Staff
Hospital Quality Improvement Team

## System Input
The system receives information from three sources.
Manual Entry
The triage nurse enters:
Chief complaint
Initial observations
Missing clinical information
Electronic Health Record (EHR)
The system retrieves available patient information including:
Previous visits
Demographic information (where appropriate)
Existing clinical record
Medical Devices
Vital signs are automatically received from monitoring equipment including:
Heart Rate
Respiratory Rate
Blood Pressure
Oxygen Saturation
Temperature
Blood Glucose

## AI Processing
The deployed Logistic Regression model analyses the collected triage information and predicts the patient's Emergency Severity Index (ESI) level.


## System Output
The dashboard displays:
Predicted ESI Level (1–5)
Colour-coded urgency indicator
Prediction confidence
Brief explanation of the prediction
Recommendation status

## Human Action
The nurse:
Reviews the patient's clinical condition.
Reviews the AI recommendation.
Accepts or overrides the recommendation.
Records the final triage decision.
Continues normal clinical workflow.
Clinical judgement always overrides the AI recommendation.

## Benefits
Improved consistency of triage decisions.
Faster patient prioritisation.
Decision support during busy periods.
Reduced cognitive workload.
Transparent AI recommendations.

HCI-Specific Safety Considerations
Safety Concern
Why it Matters
Mitigation
Alarm fatigue
Too many alerts may cause clinicians to ignore important notifications.
Display alerts only for clinically significant recommendations and prioritise high-acuity cases.
Screen legibility
Poor visibility under bright lighting or fatigue may increase the risk of errors.
Use high-contrast colours, large fonts, and clear icons that remain readable throughout long shifts.
AI over-reliance
Nurses may trust the recommendation without performing an independent assessment.
Require the nurse to review the recommendation and provide an override option, reinforcing that the AI supports rather than replaces clinical judgement.


# Problem Space Co-Design Canvas (HRI)
Implementation Setting
Observation Unit Robotic Assessment Kiosk

## Problem
Patients admitted to the Observation Unit often require repeated monitoring while nursing staff manage multiple patients simultaneously. Routine physiological assessments consume valuable clinical time, particularly during busy periods.
A Human–Robot Interaction (HRI) solution could support nursing staff by collecting routine observations, interacting with patients through a touchscreen and voice interface, and transmitting information to the AI triage system. The robot would not make clinical decisions but would assist staff by automating data collection and highlighting patients who may require further assessment.

## Primary Users
Observation Unit Nurse

## Secondary Users
Patients
Emergency Physicians
Clinical Support Staff
Biomedical Engineering Team

## System Input
Patient Interaction
Patients provide:
Identification
Symptoms
Responses to assessment questions
Integrated Sensors
The robotic station measures:
Heart Rate
Blood Pressure
Oxygen Saturation
Temperature
Respiratory Rate
Electronic Health Record
The robot retrieves relevant patient information from the hospital information system where authorised.

## AI Processing
The Logistic Regression model analyses the collected information and predicts an Emergency Severity Index (ESI) level to support ongoing patient assessment.

## System Output
The robotic kiosk provides:
Visual status indicator
Voice instructions
Predicted ESI recommendation
Alert to supervising nurse
Updated patient record

## Human Action
The supervising nurse:
Reviews the robot's assessment.
Confirms or overrides the recommendation.
Performs additional clinical assessment if required.
Initiates appropriate treatment or escalation.
The robot never replaces clinical assessment.

## Benefits
Continuous monitoring support.
Reduced workload for routine assessments.
Earlier identification of deteriorating patients.
Improved workflow within the Observation Unit.

## HRI-Specific Safety Considerations
Safety Concern
Why it Matters
Mitigation
Physical proximity
The robot operates near patients and staff, increasing the risk of accidental contact.
Equip the robot with obstacle detection, controlled movement, and emergency stop functions.
Voice recognition in noisy environments
Background noise may affect speech recognition and patient communication.
Provide both touchscreen and voice input with manual confirmation before submission.
Sensor failure
Inaccurate or unavailable sensor readings may lead to incorrect recommendations.
Detect sensor faults automatically, notify staff immediately, and allow manual data entry as a fallback.


## Comparison of HCI and HRI
Aspect
HCI (ED Triage Desk)
HRI (Observation Unit)
Primary User
ED Triage Nurse
Observation Unit Nurse and Patient
Interaction
Screen-based dashboard
Physical robotic kiosk with touchscreen and sensors
Input Method
Manual entry, EHR, medical devices
Sensors, touchscreen, voice input, EHR
Output
ESI recommendation displayed on screen
ESI recommendation with visual and voice feedback
Human Role
Reviews and overrides recommendation
Supervises robot and confirms clinical decisions
Main Goal
Support rapid triage decisions
Support routine monitoring and patient assessment
