# SentinelX — Initial Data Model

## 1. Purpose

The SentinelX data model defines the primary security entities that
will be used throughout the investigation pipeline.

The model is designed around the following relationship:

Security Events
      ↓
Detection Findings
      ↓
Correlations
      ↓
Incidents
      ↓
Attack Story
      ↓
Evidence
      ↓
Risk Assessment
      ↓
AI Investigation

---

# 2. Security Event

A Security Event represents an individual observation received from a
security telemetry source.

Potential fields:

- event_id
- timestamp
- source
- host
- user
- process
- parent_process
- source_ip
- source_port
- destination_ip
- destination_port
- event_type
- severity
- raw_event
- metadata

The original raw event should be retained for traceability.

---

# 3. Detection Finding

A Detection Finding represents suspicious behavior identified by the
Detection Engine.

Potential fields:

- finding_id
- event_id
- detection_rule
- detection_type
- severity
- confidence
- description
- evidence
- created_at

A finding may reference one or more underlying events.

---

# 4. Correlation

A Correlation represents a relationship identified between multiple
events or findings.

Potential fields:

- correlation_id
- source_entities
- related_events
- correlation_type
- correlation_score
- confidence
- supporting_evidence
- created_at

Possible correlation types:

- temporal
- host-based
- user-based
- process-based
- network-based
- behavioral
- technique-based

---

# 5. Incident

An Incident represents a group of strongly related security activity.

Potential fields:

- incident_id
- title
- status
- severity
- risk_score
- confidence_score
- first_seen
- last_seen
- affected_hosts
- affected_users
- related_events
- related_findings
- created_at
- updated_at

---

# 6. Attack Story

An Attack Story represents the reconstructed progression of an
incident.

Potential fields:

- story_id
- incident_id
- timeline
- attack_stages
- observed_behaviors
- inferred_relationships
- confidence
- supporting_evidence

Observed facts and inferred relationships should remain
distinguishable.

---

# 7. MITRE Technique

A MITRE Technique represents an ATT&CK technique associated with
observed behavior.

Potential fields:

- technique_id
- technique_name
- tactic
- evidence
- confidence
- related_events
- related_incident

---

# 8. Evidence

Evidence represents information supporting a SentinelX conclusion.

Potential fields:

- evidence_id
- incident_id
- source_event
- evidence_type
- description
- timestamp
- confidence
- source_reference

Evidence should allow investigators to trace important conclusions
back to the original telemetry.

---

# 9. Risk Assessment

A Risk Assessment represents the contextual risk calculation for an
incident.

Potential fields:

- assessment_id
- incident_id
- risk_score
- risk_level
- contributing_factors
- confidence
- calculated_at

Potential risk factors include:

- event severity
- attack progression
- correlation strength
- asset importance
- user context
- behavioral indicators
- MITRE techniques
- evidence strength

---

# 10. AI Investigation

An AI Investigation represents an AI-assisted analysis session.

Potential fields:

- investigation_id
- incident_id
- evidence_context
- analyst_question
- AI_response
- model_information
- confidence
- created_at

AI responses should maintain a clear distinction between observed
evidence and generated interpretation.

---

# 11. Analyst Note

Analyst Notes allow SOC analysts to record investigation observations.

Potential fields:

- note_id
- incident_id
- analyst
- content
- created_at
- updated_at

---

# 12. Audit Record

Audit Records track security-sensitive actions performed within
SentinelX.

Potential fields:

- audit_id
- user
- action
- resource
- timestamp
- source_ip
- result

---

# 13. Entity Relationships

Initial conceptual relationships:

```text
EVENT
  |
  +---- Detection Finding
  |
  +---- Correlation
           |
           v
        INCIDENT
           |
     +-----+-----+
     |     |     |
     v     v     v
  ATT&CK  RISK  EVIDENCE
     |            |
     +------+-----+
            |
            v
       ATTACK STORY
            |
            v
     AI INVESTIGATION 


---

# 14. User

A User represents an authenticated SentinelX user or SOC analyst.

Potential fields:

* user_id
* username
* email
* password_hash
* role
* is_active
* created_at
* updated_at
* last_login

Possible roles:

* analyst
* senior_analyst
* administrator

Security-sensitive authentication information must be stored securely.

---

# 15. Host

A Host represents an endpoint or monitored system participating in the SentinelX security environment.

Potential fields:

* host_id
* hostname
* ip_address
* operating_system
* host_type
* agent_id
* environment
* criticality
* status
* first_seen
* last_seen

Host criticality may contribute to contextual risk assessment.

---

# 16. Alert

An Alert represents a security notification generated from a detection or telemetry source.

Potential fields:

* alert_id
* event_id
* finding_id
* source
* title
* description
* severity
* status
* confidence
* created_at
* acknowledged_at
* resolved_at

Possible alert states:

* new
* acknowledged
* investigating
* resolved
* closed

Alerts provide the analyst-facing representation of detected security activity.

---

# 17. Incident Event

An Incident Event represents the relationship between an incident and an underlying security event.

Potential fields:

* incident_event_id
* incident_id
* event_id
* relationship_type
* relevance_score
* added_at

This entity allows an incident to contain multiple related events while preserving event-level traceability.

---

# 18. Risk Score

A Risk Score represents a contextual risk value associated with an incident or security activity.

Potential fields:

* risk_score_id
* incident_id
* score
* risk_level
* severity_factor
* correlation_factor
* asset_factor
* behavioral_factor
* evidence_factor
* mitre_factor
* calculated_at

Possible risk levels:

* low
* medium
* high
* critical

Risk scoring should remain explainable by retaining the factors that contributed to the final score.

---

# 19. Investigation

An Investigation represents an analyst-driven security investigation.

Potential fields:

* investigation_id
* incident_id
* analyst_id
* investigation_type
* status
* hypothesis
* findings
* started_at
* completed_at
* created_at
* updated_at

Possible investigation types:

* incident investigation
* host investigation
* threat hunting
* alert investigation
* AI-assisted investigation

An investigation may contain analyst notes, evidence references, and AI-assisted analysis.

---

# 20. Threat Intelligence

A Threat Intelligence record represents contextual intelligence associated with an observable or security event.

Potential fields:

* intelligence_id
* indicator_type
* indicator_value
* source
* reputation
* confidence
* threat_type
* first_seen
* last_seen
* related_event
* related_incident
* retrieved_at

Possible indicator types include:

* IP address
* domain
* URL
* file hash
* hostname

Threat intelligence is intended to enrich investigations rather than replace SentinelX's internal detection and correlation logic.

---

# 21. Response Action

A Response Action represents an analyst-reviewed response recommendation or documented response activity.

Potential fields:

* response_action_id
* incident_id
* investigation_id
* action_type
* recommendation
* rationale
* priority
* status
* analyst_id
* created_at
* completed_at

Possible action types:

* investigate
* contain
* isolate
* block
* collect evidence
* reset credentials
* remediate
* monitor

SentinelX will primarily provide evidence-based recommendations. High-impact actions should remain under authorized analyst control.

---

# 22. Core Entity Relationship Model

The expanded SentinelX data model follows this conceptual relationship:

```text
                         USER
                          |
                          |
                    +-----+------+
                    |            |
                    v            v
               INVESTIGATION   AUDIT RECORD
                    |
                    |
                    v
SECURITY EVENT ---> DETECTION FINDING ---> ALERT
      |                   |
      |                   |
      v                   v
 INCIDENT EVENT       CORRELATION
      |                   |
      +---------+---------+
                |
                v
             INCIDENT
                |
       +--------+---------+----------------+
       |        |         |                |
       v        v         v                v
     HOST     RISK      MITRE          EVIDENCE
              SCORE     TECHNIQUE
                |          |
                +----+-----+
                     |
                     v
               ATTACK STORY
                     |
                     v
              AI INVESTIGATION
                     |
                     v
             RESPONSE ACTION

THREAT INTELLIGENCE
        |
        +------> EVENT / ALERT / INCIDENT
```

---

# 23. Key Relationships

### User → Investigation

One analyst may perform multiple investigations.

### Host → Security Event

A host may generate many security events.

### Security Event → Detection Finding

A security event may produce zero or more detection findings.

### Detection Finding → Alert

A detection finding may generate an analyst-facing alert.

### Security Event → Incident Event

Security events may be associated with incidents through the Incident Event relationship.

### Incident → Incident Event

An incident may contain multiple related events.

### Incident → Risk Score

An incident may have one or more risk assessments over its lifecycle.

### Incident → MITRE Technique

An incident may be associated with multiple MITRE ATT&CK techniques.

### Incident → Evidence

An incident may contain multiple evidence records.

### Incident → Investigation

An incident may have multiple investigation activities.

### Incident → Response Action

An incident may produce multiple analyst-reviewed response recommendations or actions.

### Incident → Attack Story

An incident may have an associated reconstructed attack story.

### Investigation → AI Investigation

An analyst investigation may contain one or more AI-assisted analysis sessions.

### Threat Intelligence → Event / Alert / Incident

Threat intelligence can enrich events, alerts, or incidents when matching indicators are identified.

---

# 24. Data Integrity Principles

SentinelX will follow these principles:

1. Original raw telemetry should be retained for traceability.
2. Security events should not be modified after ingestion without an audit trail.
3. Detection findings should reference supporting events.
4. Incidents should preserve relationships to their underlying events.
5. Risk scores should retain their contributing factors.
6. MITRE mappings should reference supporting evidence.
7. AI investigations should preserve the evidence context used for analysis.
8. Analyst actions should be auditable.
9. Security-sensitive user information should be protected.
10. Observed evidence and generated interpretation should remain distinguishable.

---

# 25. Database Design Objective

The database is designed to support the complete SentinelX investigation lifecycle:

**Telemetry → Normalization → Detection → Alert → Correlation → Incident → Evidence → Risk Assessment → MITRE Analysis → Investigation → AI Analysis → Response Support**

The relational structure should preserve traceability between each stage so that analysts can move from a high-level incident back to the original security telemetry that supports the conclusion.

---

# 26. Future Extensibility

The data model is intentionally modular and can be extended in future versions with entities such as:

* Detection Rules
* Asset Inventory
* Security Cases
* Playbooks
* Vulnerabilities
* Threat Actors
* Campaigns
* External Threat Intelligence Sources

These entities are not required for the initial implementation but can be integrated without redesigning the complete core investigation model.
