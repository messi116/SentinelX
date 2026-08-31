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