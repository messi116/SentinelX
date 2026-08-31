# SentinelX — Research Evaluation Framework

## 1. Purpose

The purpose of the evaluation is to determine whether SentinelX can
improve the investigation of multi-stage security incidents by
combining event correlation, attack-story reconstruction, contextual
risk assessment, MITRE ATT&CK mapping, and evidence-based AI assistance.

The evaluation will use controlled security scenarios and measurable
metrics.

---

# 2. Evaluation Objectives

The evaluation will investigate whether SentinelX can:

1. Correctly identify related security events.
2. Reduce incorrect event correlations.
3. Reconstruct multi-stage attack progression.
4. Correctly associate observed behavior with MITRE ATT&CK techniques.
5. Prioritize incidents using contextual risk.
6. Provide explainable investigation results.
7. Process telemetry with acceptable latency.
8. Provide useful AI-assisted investigation guidance.

---

# 3. Evaluation Scenarios

SentinelX will be evaluated using controlled scenarios representing
different security situations.

## Scenario A — Normal Activity

The environment contains legitimate user and system activity.

Expected result:

- minimal suspicious findings
- no unnecessary incident creation
- low contextual risk

---

## Scenario B — Authentication Anomaly

The environment contains multiple abnormal authentication events.

Expected result:

- authentication anomalies are detected
- related events are correlated
- appropriate evidence is presented
- risk reflects the complete context

---

## Scenario C — Suspicious Process Activity

The environment contains suspicious process behavior.

Expected result:

- process-related events are detected
- relevant events are correlated with surrounding activity
- supporting evidence is displayed

---

## Scenario D — Multi-Stage Attack

The environment contains a sequence of related security events.

Example:

Authentication Anomaly
        ↓
Successful Authentication
        ↓
Suspicious Process
        ↓
Privilege-Related Activity
        ↓
Sensitive Data Access
        ↓
Suspicious Network Communication

Expected result:

SentinelX should recognize the relationship between events and
construct a unified incident investigation story.

---

## Scenario E — Unrelated Events

The environment contains suspicious-looking events that are not part
of the same attack.

Expected result:

SentinelX should avoid incorrectly grouping unrelated events.

This scenario is important for measuring false correlation.

---

# 4. Evaluation Metrics

## 4.1 Event Correlation Accuracy

Measures how accurately SentinelX identifies genuinely related
security events.

Possible measurement:

Correlation Accuracy =
Correctly Related Events / Total Evaluated Relationships

---

## 4.2 False Correlation Rate

Measures how often SentinelX incorrectly groups unrelated events.

False Correlation Rate =
Incorrectly Correlated Relationships / Total Correlation Decisions

Lower values are preferred.

---

## 4.3 Incident Reconstruction Quality

Measures whether the reconstructed attack story correctly represents
the known scenario.

Evaluation factors:

- correct event ordering
- correct affected entities
- correct attack stages
- correct supporting evidence
- correct relationships

---

## 4.4 MITRE ATT&CK Mapping Accuracy

Measures whether observed behaviors are associated with appropriate
MITRE ATT&CK techniques.

Evaluation factors:

- technique identification
- tactic identification
- evidence supporting mapping
- mapping confidence

---

## 4.5 Risk Prioritization Effectiveness

Measures whether high-risk incidents receive higher priority than
lower-risk incidents.

Evaluation factors:

- incident severity
- attack progression
- correlation strength
- asset importance
- user context
- behavioral indicators
- evidence strength
- MITRE techniques

---

## 4.6 Explainability

Measures whether an analyst can understand why SentinelX produced a
particular result.

A result should identify:

- detected behavior
- supporting events
- correlation reasoning
- contributing risk factors
- confidence
- MITRE techniques where applicable

---

## 4.7 Processing Performance

Measures SentinelX processing performance.

Metrics may include:

- event ingestion latency
- normalization latency
- detection latency
- correlation latency
- incident generation latency
- overall processing time

---

## 4.8 AI Investigation Usefulness

Measures whether the AI investigation layer provides useful
assistance when analyzing structured security evidence.

Evaluation factors:

- relevance
- factual consistency with evidence
- investigation usefulness
- clarity
- identification of important evidence
- quality of suggested investigation priorities

AI output should not be treated as ground truth.

---

# 5. Baseline Comparison

Where practical, SentinelX will be compared against isolated alert
analysis.

Baseline approach:

```text
Individual Security Alerts
        ↓
Analyst Reviews Alerts Independently
        ↓
Manual Investigation