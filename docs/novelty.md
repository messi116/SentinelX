# SentinelX — Research Novelty and Unique Contribution

## 1. Overview

SentinelX is designed as an intelligent SOC investigation platform
rather than a conventional SIEM dashboard.

The primary focus is not simply collecting alerts or displaying
security events. SentinelX focuses on understanding relationships
between security events and reconstructing the progression of
potential multi-stage attacks.

## 2. Core Novelty

The central concept of SentinelX is:

> Context-Aware Attack Story Reconstruction

Instead of presenting security alerts as isolated events, SentinelX
will attempt to determine whether multiple events are related and
represent them as a unified investigation story.

Example:

Authentication Anomaly
        ↓
Successful Authentication
        ↓
Suspicious Process Activity
        ↓
Privilege-Related Activity
        ↓
Sensitive Data Access
        ↓
Suspicious Network Communication

These events can then be represented as a single contextualized
incident rather than unrelated alerts.

## 3. Research Contributions

### 3.1 Multi-Dimensional Event Correlation

SentinelX will investigate relationships between events using
multiple contextual dimensions:

- temporal proximity
- source and destination
- affected host
- user identity
- process relationships
- network relationships
- behavioral similarity
- severity
- attack-technique relationships

This allows the system to move beyond simple rule-based alert grouping.

### 3.2 Attack Story Reconstruction

Related events will be organized into an attack progression.

The reconstructed incident will contain:

- event sequence
- affected entities
- observed behaviors
- supporting evidence
- possible attack stages
- MITRE ATT&CK techniques
- risk information
- confidence information

### 3.3 Contextual Risk Assessment

SentinelX will investigate contextual risk rather than relying only
on the severity of individual alerts.

Risk assessment may consider:

- event severity
- number of correlated events
- attack progression
- affected asset importance
- user context
- behavioral indicators
- MITRE ATT&CK techniques
- correlation confidence

### 3.4 Evidence-Based AI Investigation

AI will not independently decide whether an attack occurred.

Instead, SentinelX will first generate structured security evidence
through deterministic detection and correlation mechanisms.

The AI investigation layer will then use this evidence to assist the
analyst with:

- incident summarization
- investigation reasoning
- evidence interpretation
- possible attack progression
- investigation priorities
- recommended defensive investigation steps

### 3.5 Explainability

Each major SentinelX conclusion should be traceable to supporting
security evidence.

For example:

Risk: HIGH

Supporting evidence:

1. Multiple authentication anomalies
2. Successful authentication following failures
3. Suspicious process activity
4. Sensitive resource access
5. Related network activity

This allows an analyst to understand why SentinelX generated a
particular assessment.

## 4. Differentiation From Conventional SIEM Systems

Traditional security monitoring systems commonly emphasize:

- log collection
- alert generation
- dashboards
- search
- rule-based detection

SentinelX will focus on the investigation layer above individual
alerts:

Security Events
      ↓
Detection
      ↓
Correlation
      ↓
Behavioral Relationships
      ↓
Attack Story
      ↓
MITRE Mapping
      ↓
Contextual Risk
      ↓
Evidence-Based AI Investigation

## 5. Research Hypothesis

A context-aware event-correlation and attack-story reconstruction
approach can improve the contextual understanding and prioritization
of multi-stage security incidents compared with analyzing isolated
security alerts.

## 6. Expected Academic Contribution

The project will evaluate whether combining event correlation,
behavioral context, attack-story reconstruction, MITRE ATT&CK
mapping, contextual risk assessment, and evidence-based AI assistance
can reduce the cognitive effort required during SOC investigations.

## 7. Design Philosophy

SentinelX follows five principles:

1. Evidence before AI
2. Context before isolated alerts
3. Explainability before automation
4. Correlation before escalation
5. Analyst assistance rather than blind automation