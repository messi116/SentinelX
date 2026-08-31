# SentinelX — System Requirements

## 1. Functional Requirements

### FR-01 — Multi-Source Telemetry Ingestion

SentinelX shall ingest security telemetry from multiple supported
sources such as Wazuh, endpoint logs, network sensors, authentication
logs, and system logs.

### FR-02 — Event Normalization

SentinelX shall transform heterogeneous security events into a common
internal event representation.

The normalized event should contain relevant fields such as:

- timestamp
- source
- host
- user
- process
- source IP
- destination IP
- event type
- severity
- raw event
- metadata

### FR-03 — Security Detection

SentinelX shall identify suspicious behaviors using deterministic
detection logic and configurable detection rules.

### FR-04 — Context-Aware Correlation

SentinelX shall correlate potentially related events using multiple
contextual dimensions including:

- time
- host
- user
- process
- network entities
- event type
- severity
- behavioral similarity
- MITRE ATT&CK relationships

### FR-05 — Incident Generation

SentinelX shall group strongly related security events into
investigative incidents.

Each incident should contain:

- incident identifier
- related events
- affected hosts
- affected users
- timeline
- severity
- risk score
- confidence score
- evidence

### FR-06 — Attack Story Reconstruction

SentinelX shall reconstruct the likely progression of related
security activity into an understandable attack timeline.

### FR-07 — MITRE ATT&CK Mapping

SentinelX shall associate observed behaviors with relevant MITRE ATT&CK
techniques where sufficient evidence exists.

### FR-08 — Contextual Risk Scoring

SentinelX shall calculate incident risk using multiple factors rather
than relying solely on the severity of individual alerts.

### FR-09 — Evidence-Based AI Investigation

SentinelX shall provide AI-assisted investigation based on structured
security evidence.

The AI layer may assist with:

- incident summarization
- evidence interpretation
- attack progression explanation
- investigation prioritization
- analyst questions
- defensive investigation guidance

### FR-10 — Explainable Decisions

SentinelX shall provide supporting evidence for important detection,
correlation, and risk-assessment decisions.

### FR-11 — Threat Hunting

SentinelX shall allow analysts to search historical security events
and investigate suspicious activity.

### FR-12 — Incident Investigation Interface

SentinelX shall provide an analyst-focused interface for:

- incidents
- event timelines
- attack stories
- MITRE techniques
- evidence
- risk
- investigation notes

### FR-13 — Detection Rule Management

Authorized users shall be able to manage detection rules and
correlation parameters.

### FR-14 — Auditability

Important analyst and system actions shall be recorded for auditing
and investigation purposes.

---

# 2. Non-Functional Requirements

## NFR-01 — Security

Secrets, credentials, API keys, and database passwords shall not be
hard-coded into source code.

## NFR-02 — Modularity

SentinelX components shall be independently maintainable.

## NFR-03 — Scalability

The architecture should allow additional telemetry sources and
detection modules to be added without redesigning the entire system.

## NFR-04 — Explainability

Important security conclusions should be traceable to supporting
evidence.

## NFR-05 — Reliability

Malformed, incomplete, or unexpected telemetry should not cause the
entire processing pipeline to fail.

## NFR-06 — Performance

The system should process security events with acceptable latency
for SOC investigation workflows.

## NFR-07 — Maintainability

The project shall use structured code, documentation, testing, and
version control.

## NFR-08 — Extensibility

The architecture should support future integrations with additional
security data sources, models, and detection mechanisms.

## NFR-09 — Privacy

Sensitive security data should be handled according to appropriate
access-control and data-protection principles.

## NFR-10 — Testability

Core detection, normalization, correlation, risk-scoring, and AI
integration components should have automated tests where practical.

---

# 3. Security Requirements

## SR-01 — Authentication

The SentinelX analyst interface shall require authenticated access.

## SR-02 — Authorization

Access to administrative and investigation functions shall be
controlled according to user privileges.

## SR-03 — Secret Management

Application secrets shall be stored using environment variables or
an appropriate secret-management mechanism.

## SR-04 — Input Validation

External telemetry and API inputs shall be validated before
processing.

## SR-05 — API Security

Backend APIs shall implement appropriate authentication,
authorization, validation, and error handling.

## SR-06 — Audit Logging

Security-sensitive application actions shall generate audit records.

---

# 4. Research Evaluation Requirements

SentinelX shall be evaluated using controlled security scenarios.

Evaluation should investigate:

- event-correlation accuracy
- false correlation rate
- incident reconstruction quality
- MITRE ATT&CK mapping accuracy
- risk-prioritization effectiveness
- processing performance
- AI investigation usefulness
- explainability of security decisions

The evaluation will compare SentinelX's contextual investigation
approach with isolated alert analysis where appropriate.s