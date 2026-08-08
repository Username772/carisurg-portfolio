# Week 10: Deployment, System Integration & User Testing

## Interim Submission

### Project: AI-Assisted Emergency Department Triage

---

## 1. Message Design

### 1.1 Urgency-Tier Messages

| Urgency Tier | Colour | Alert Message | Action |
|---|---|---|---|
| **CRITICAL** | Red | **Act now: assess this patient immediately.** | Immediate assessment |
| **HIGH** | Orange | **Assess this patient as soon as possible.** | Prompt assessment |
| **MEDIUM** | Yellow/Amber | **Review this patient soon and confirm their priority.** | Review soon |
| **LOW** | Green | **Review this patient when practical.** | Routine review |

### 1.2 Message Design Principles

The messages use:

- Plain language
- An explicit action verb
- A consistent urgency structure
- No unnecessary clinical jargon
- Predictable escalation from Low to Critical
- Text that remains understandable without relying on colour alone

### 1.3 Design Rationale

**Critical:**  
"Act now" provides an immediate and unambiguous action.

**High:**  
"As soon as possible" communicates urgency without implying the immediate response required for Critical.

**Medium:**  
The message directs the nurse to review the patient and confirm priority rather than automatically accepting the AI recommendation.

**Low:**  
"When practical" communicates the lowest urgency while still requiring the patient to be reviewed.

---

## 2. Initial GUI Prototype

### 2.1 Prototype Purpose

The GUI is designed for the **main ED triage desk**, where a nurse reviews arriving patients and uses the AI system as a decision-support tool.

The prototype includes:

- Patient queue
- Urgency indicator for each patient
- Alert banner at the top
- "View Details" interaction
- Text-based urgency messages
- Colour as a secondary visual cue
- Clear separation between AI recommendation and clinician decision

### 2.2 Low-Fidelity Prototype Image


### ED Triage Dashboard

The low-fidelity prototype shows the main ED triage dashboard used by the nurse. It includes the patient queue, four urgency tiers, the Critical alert banner, and the **View Details** interaction.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3bfa8167-125f-440e-8b03-e224dac5fedb" />


### View Details Interaction

When the nurse selects **VIEW DETAILS**, the prototype displays supporting patient information while clearly identifying the AI output as a decision-support recommendation rather than a final clinical decision.

The details view includes:

- Patient identifier
- AI urgency tier
- Action-oriented urgency message
- Key observations
- AI decision-support notice
- **Confirm Review** option
- **Override / Change Priority** option


### 2.3 Prototype Features

#### Alert Banner

The alert banner is placed at the top of the screen so that a high-priority alert remains visible during patient-queue review.

#### Urgency Indicator

Each patient receives:

- A tier label
- A colour indicator
- An action-oriented message

Colour is not the only method used to communicate urgency.

#### Patient Queue

The queue allows the nurse to compare patients quickly and identify which patient requires attention first.

#### View Details

The "View Details" interaction allows the nurse to investigate the recommendation before making a clinical decision.

#### Human Oversight

The AI is presented as a **decision-support system**, not an autonomous triage decision-maker. The nurse retains responsibility for reviewing and overriding the recommendation when clinically appropriate.

---

## 3. Accessibility Considerations

### 3.1 Colour-Blindness

**Risk:**  
A user may be unable to distinguish urgency colours reliably.

**Design Response:**  
The system does not rely on colour alone. Every urgency tier includes:

- Written tier name
- Action-oriented message
- Colour indicator
- Consistent visual hierarchy

Example:

**CRITICAL — Act now: assess this patient immediately.**

---

### 3.2 Cognitive Load During Night Shifts

**Risk:**  
A tired clinician working during a busy handover may misread long or complicated messages.

**Design Response:**

Messages are:

- Short
- Written in plain language
- Action-oriented
- Consistent across all four tiers
- Designed for rapid interpretation

The Critical alert begins with **"Act now"** so the required response is immediately visible.

---

### 3.3 Noise and Environmental Distractions

**Risk:**  
The ED can be noisy, meaning an audio alert may be missed or misunderstood.

**Design Response:**  
Visual and text-based alerts are the primary communication method. Audio is supplementary rather than the only notification method.

---

## 4. Peer Testing Plan

### 4.1 Purpose

The peer-testing activity will evaluate whether users can correctly understand the four urgency tiers under conditions that simulate rapid decision-making.

Testing will focus on:

1. Message clarity
2. Correct ordering of urgency
3. Potential misinterpretation
4. Effect of colour
5. Cognitive load
6. Perceived actionability

### 4.2 Participants

At least **three cohort members** will test the prototype.

Each tester will independently review the messages and prototype.

### 4.3 Test 1: Words Without Colour

The four messages will be displayed without colour indicators.

Testers will be asked:

> "Rank these four messages from most urgent to least urgent."

Expected order:

**Critical → High → Medium → Low**

This tests whether the wording communicates urgency independently of colour.

### 4.4 Test 2: Messages With Colour

The same four messages will then be displayed using the prototype's colour system.

Testers will again rank the messages from most urgent to least urgent.

This allows comparison between:

- Text-only understanding
- Text + colour understanding

### 4.5 Test 3: Rapid Interpretation

Each tester will be shown an alert for approximately **10 seconds** and asked:

> "What action would you take?"

The response will be recorded.

### 4.6 Test 4: Misinterpretation Check

Testers will be asked:

- Which message was easiest to understand?
- Which message was most confusing?
- Did any message appear less urgent than intended?
- Did any message sound too similar to another tier?
- Would you know what action to take immediately?
- What would you change?

> **Note:** Actual peer-testing results will be documented in the Week 10 Final Submission after testing has been completed.

---

## 5. Planned Measures

### Primary Measures

**Urgency-order accuracy:**  
Whether the tester correctly ranks Critical, High, Medium, and Low.

**Action recognition:**  
Whether the tester identifies the appropriate action for each alert.

**Misinterpretation rate:**  
Number of times a tester interprets a tier as a different urgency level.

**Time to interpretation:**  
Approximate time required for the tester to state the required action.

### Qualitative Feedback

Short verbal feedback will be collected to identify:

- Confusing wording
- Unclear differences between tiers
- Excessive information
- Accessibility concerns
- Suggested improvements

---

## 6. Interim Submission Summary

The Week 10 interim prototype establishes a human-centred communication design for AI-assisted ED triage.

The four urgency tiers use short, action-oriented messages:

- **Critical:** Act now: assess this patient immediately.
- **High:** Assess this patient as soon as possible.
- **Medium:** Review this patient soon and confirm their priority.
- **Low:** Review this patient when practical.

The initial GUI provides a patient queue, urgency indicators, an alert banner, and a "View Details" interaction.

The design does not rely on colour alone and addresses:

- Colour-blindness
- Cognitive load
- Environmental noise

The next stage is to conduct peer testing with at least three cohort members. Actual peer-feedback results and any resulting design changes will be included in the **Week 10 Final Submission**.
