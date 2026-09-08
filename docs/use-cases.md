\# SentinelX — Use Cases



\## 1. SOC Analyst Workflow



The primary SentinelX investigation workflow is:



\*\*Analyst → Login → View Alerts → Open Incident → Investigate Evidence → View Timeline → View MITRE Techniques → AI Analysis → Review Response Recommendation\*\*



This workflow is designed to help analysts move from an individual security alert toward contextual incident understanding and evidence-based decision support.



\---



\## 2. Use Case UC-01 — User Login



\### Description



An authorized SOC analyst logs into SentinelX to access security monitoring and investigation capabilities.



\### Primary Actor



SOC Analyst



\### Preconditions



\* The user has a registered SentinelX account.

\* The user has valid authentication credentials.

\* SentinelX backend and database services are available.



\### Main Flow



1\. Analyst opens the SentinelX login interface.

2\. Analyst provides authentication credentials.

3\. SentinelX validates the credentials.

4\. SentinelX authenticates the user.

5\. Analyst is granted access according to their authorization level.

6\. SentinelX displays the security operations dashboard.



\### Alternative Flow



If authentication fails, SentinelX rejects the login request and displays an appropriate authentication error.



\### Postconditions



The authenticated analyst can access authorized SentinelX functionality.



\---



\## 3. Use Case UC-02 — Alert Monitoring



\### Description



The analyst monitors incoming security alerts generated from integrated telemetry sources.



\### Primary Actor



SOC Analyst



\### Preconditions



\* Analyst is authenticated.

\* Security telemetry is being received.

\* Detection services are operational.



\### Main Flow



1\. Analyst opens the alert monitoring interface.

2\. SentinelX displays available security alerts.

3\. Analyst reviews alert severity and event information.

4\. Analyst filters or searches alerts when required.

5\. Analyst selects a relevant alert.

6\. SentinelX displays the associated security context.

7\. Analyst decides whether further investigation is required.



\### Postconditions



The analyst identifies alerts requiring investigation or additional analysis.



\---



\## 4. Use Case UC-03 — Incident Investigation



\### Description



The analyst investigates a security incident by examining related alerts, events, evidence, risk information, and attack context.



\### Primary Actor



SOC Analyst



\### Preconditions



\* Analyst is authenticated.

\* A security incident or suspicious activity exists.



\### Main Flow



1\. Analyst opens an incident.

2\. SentinelX displays incident information.

3\. Analyst reviews related detection findings.

4\. Analyst reviews supporting telemetry events.

5\. Analyst examines affected hosts and users.

6\. Analyst reviews the incident timeline.

7\. Analyst examines risk assessment information.

8\. Analyst reviews related MITRE ATT\&CK techniques.

9\. Analyst requests AI-assisted investigation when required.

10\. Analyst reviews the resulting investigation context.



\### Postconditions



The analyst obtains a contextual understanding of the incident and its supporting evidence.



\---



\## 5. Use Case UC-04 — Threat Hunting



\### Description



The analyst searches historical security telemetry to investigate suspicious behaviors or identify previously undetected attack patterns.



\### Primary Actor



SOC Analyst



\### Preconditions



\* Analyst is authenticated.

\* Historical security events are available.



\### Main Flow



1\. Analyst opens the threat-hunting interface.

2\. Analyst defines search criteria.

3\. SentinelX searches historical normalized events.

4\. SentinelX returns matching security events.

5\. Analyst examines event relationships and contextual information.

6\. Analyst identifies potentially suspicious activity.

7\. Analyst may initiate an investigation from relevant findings.



\### Postconditions



Potentially suspicious activity is identified for further investigation.



\---



\## 6. Use Case UC-05 — Host Investigation



\### Description



The analyst investigates the security activity associated with a specific endpoint or host.



\### Primary Actor



SOC Analyst



\### Preconditions



\* Analyst is authenticated.

\* Host telemetry exists in SentinelX.



\### Main Flow



1\. Analyst selects a host.

2\. SentinelX displays host-related security information.

3\. Analyst reviews events associated with the host.

4\. Analyst reviews detections involving the host.

5\. Analyst examines suspicious processes or activities where available.

6\. Analyst reviews network-related activity.

7\. Analyst examines related incidents and risk information.

8\. Analyst determines whether additional investigation is required.



\### Postconditions



The analyst obtains a host-specific security overview.



\---



\## 7. Use Case UC-06 — AI-Assisted Analysis



\### Description



The analyst requests AI-assisted analysis of an investigation using structured security evidence collected by SentinelX.



\### Primary Actor



SOC Analyst



\### Preconditions



\* Analyst is authenticated.

\* An investigation or incident contains relevant evidence.

\* AI service is configured and available.



\### Main Flow



1\. Analyst opens an investigation.

2\. Analyst requests AI analysis.

3\. SentinelX gathers relevant structured evidence.

4\. SentinelX provides the evidence to the AI investigation component.

5\. AI component analyzes the supplied security context.

6\. SentinelX presents the generated analysis to the analyst.

7\. Analyst reviews the findings and reasoning.

8\. Analyst compares AI analysis with available evidence.



\### Important Constraint



AI output is treated as analyst decision support and must not be considered an autonomous security authority.



\### Postconditions



The analyst receives contextual AI-assisted investigation support based on available evidence.



\---



\## 8. Use Case UC-07 — Response Recommendation



\### Description



SentinelX provides evidence-based response recommendations to assist the analyst in deciding appropriate investigation, containment, or remediation actions.



\### Primary Actor



SOC Analyst



\### Preconditions



\* An incident or suspicious activity has been investigated.

\* Relevant evidence and contextual information are available.



\### Main Flow



1\. Analyst reviews the incident.

2\. SentinelX evaluates available security context.

3\. SentinelX identifies relevant response considerations.

4\. SentinelX generates evidence-based response recommendations.

5\. Analyst reviews the recommendations.

6\. Analyst evaluates the recommendations against the available evidence.

7\. Analyst decides the appropriate response action.



\### Important Constraint



SentinelX provides recommendations and analyst support rather than independently executing high-impact response actions.



\### Postconditions



The analyst has actionable response guidance to support incident handling.



\---



\## 9. Use Case Relationships



The major use cases are connected through the following investigation lifecycle:



\*\*Login\*\*

↓

\*\*Alert Monitoring\*\*

↓

\*\*Incident Investigation\*\*

↓

\*\*Evidence Analysis\*\*

↓

\*\*Timeline Review\*\*

↓

\*\*MITRE ATT\&CK Analysis\*\*

↓

\*\*AI-Assisted Analysis\*\*

↓

\*\*Response Recommendation\*\*



Threat Hunting and Host Investigation can enter the workflow whenever additional contextual investigation is required.



\---



\## 10. System-Level Investigation Flow



```text

&#x20;                   ┌───────────────┐

&#x20;                   │  SOC Analyst  │

&#x20;                   └───────┬───────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                   ┌───────────────┐

&#x20;                   │     Login     │

&#x20;                   └───────┬───────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                 ┌───────────────────┐

&#x20;                 │  Alert Monitoring │

&#x20;                 └─────────┬─────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                 ┌───────────────────┐

&#x20;                 │ Incident          │

&#x20;                 │ Investigation     │

&#x20;                 └─────────┬─────────┘

&#x20;                           │

&#x20;            ┌──────────────┼──────────────┐

&#x20;            ▼              ▼              ▼

&#x20;      ┌──────────┐   ┌──────────┐   ┌──────────┐

&#x20;      │ Evidence │   │ Timeline │   │   MITRE  │

&#x20;      │ Analysis │   │  Review  │   │ Analysis │

&#x20;      └────┬─────┘   └────┬─────┘   └────┬─────┘

&#x20;           └───────────────┼──────────────┘

&#x20;                           ▼

&#x20;                 ┌───────────────────┐

&#x20;                 │   AI Analysis     │

&#x20;                 └─────────┬─────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                 ┌───────────────────┐

&#x20;                 │    Response       │

&#x20;                 │  Recommendation   │

&#x20;                 └───────────────────┘



&#x20;       ┌──────────────────┐

&#x20;       │  Threat Hunting  │

&#x20;       └────────┬─────────┘

&#x20;                │

&#x20;                ▼

&#x20;       ┌──────────────────┐

&#x20;       │ Further          │

&#x20;       │ Investigation    │

&#x20;       └──────────────────┘



&#x20;       ┌──────────────────┐

&#x20;       │ Host Investigation│

&#x20;       └────────┬─────────┘

&#x20;                │

&#x20;                ▼

&#x20;       ┌──────────────────┐

&#x20;       │ Host Context \&   │

&#x20;       │ Related Events   │

&#x20;       └──────────────────┘

```



\## 11. Security and Authorization Considerations



All SentinelX use cases operate within an authorized security environment.



Access to security data and investigation capabilities will be controlled through authentication and authorization mechanisms.



The platform will maintain separation between security analysis, AI-assisted investigation, and response decision-making to preserve analyst oversight and system safety.



