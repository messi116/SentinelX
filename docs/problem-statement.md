# SentinelX — Problem Statement

## Background

Modern Security Operations Centers receive security telemetry from
multiple heterogeneous sources such as endpoint security platforms,
network sensors, operating-system logs, authentication systems, and
security monitoring platforms.

These sources continuously generate large volumes of security events
and alerts.

## Problem

A major challenge for SOC analysts is that individual alerts often
provide only a limited view of an incident.

A multi-stage attack may generate multiple events across different
systems and time periods. These events may appear unrelated when
viewed individually even though they are part of the same attack
sequence.

The analyst therefore has to manually:

- correlate events,
- identify behavioral relationships,
- reconstruct the attack timeline,
- determine the likely attack progression,
- map activity to relevant MITRE ATT&CK techniques,
- assess the overall incident risk,
- and determine what evidence should be investigated next.

This manual process can increase investigation time and contribute to
alert fatigue.

## SentinelX Problem

SentinelX addresses the problem of fragmented security-event
investigation by developing an intelligent SOC investigation platform
that can transform related security events into a contextualized
incident narrative.

Instead of treating every alert as an isolated event, SentinelX will
investigate relationships between events using multiple contextual
dimensions such as:

- temporal proximity,
- affected host,
- user identity,
- process relationships,
- network relationships,
- behavioral similarity,
- security severity,
- and attack-technique relationships.

## Research Problem

The central research problem is:

> How can heterogeneous security events be intelligently correlated
> and reconstructed into an explainable attack story that improves
> incident understanding and prioritization for SOC analysts?

## Proposed Solution

SentinelX will combine:

1. Multi-source telemetry ingestion
2. Event normalization
3. Behavioral detection
4. Context-aware event correlation
5. Attack-story reconstruction
6. MITRE ATT&CK mapping
7. Contextual risk scoring
8. Evidence-based AI investigation
9. Threat-hunting capabilities
10. Analyst-focused visualization

## Core Research Question

Can an intelligent event-correlation and attack-story reconstruction
framework improve the contextual understanding and prioritization of
multi-stage security incidents compared with analyzing individual
security alerts independently?

## Expected Outcome

The expected outcome is a functional SOC investigation platform that
can transform fragmented security events into structured incidents
containing:

- related events,
- attack progression,
- supporting evidence,
- affected entities,
- MITRE ATT&CK techniques,
- contextual risk,
- confidence information,
- and AI-assisted investigation guidance.

## Important Design Principle

SentinelX will not rely on AI alone to determine whether an attack
occurred.

Security evidence, deterministic detection logic, correlation
mechanisms, and explainable scoring will provide the foundation.
AI will be used as an investigation-assistance layer operating on
structured evidence.