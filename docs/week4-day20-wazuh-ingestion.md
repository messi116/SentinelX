# Week 4 Day 20 — Wazuh Alert Ingestion

## Objective

Implement the SentinelX Wazuh ingestion service that retrieves real Wazuh alerts and persists them as SentinelX telemetry events in PostgreSQL.

## Architecture

Wazuh Indexer
? WazuhService
? WazuhIngestionService
? TelemetryEvent
? PostgreSQL

## Implementation

Created:

`backend/app/services/wazuh_ingestion.py`

The ingestion service:

- Retrieves recent alerts through the existing `WazuhService`.
- Reads the Wazuh alert timestamp.
- Extracts common telemetry fields.
- Creates a `TelemetryEvent`.
- Preserves the complete original Wazuh alert in `raw_data`.
- Persists the telemetry event to PostgreSQL.

## Verification

A real Wazuh alert was successfully ingested.

Test command:

`python backend/test_wazuh_ingestion.py`

Result:

`{'total_received': 1, 'ingested': 1}`

Database verification confirmed:

- Source: `wazuh`
- Event type: `rootcheck`
- Host: `wazuh`
- Severity: `12`
- Message: `Custom Alert: File Integrity Monitoring Event`
- Original raw Wazuh data preserved: `True`

Database record ID: `10`

## Evidence-First Design

The ingestion layer does not discard the original Wazuh alert. The complete alert is stored in `TelemetryEvent.raw_data`.

This allows later SentinelX components to perform:

- Detection
- Correlation
- MITRE mapping
- Risk scoring
- AI investigation
- Evidence reconstruction

without losing source-specific telemetry.

## Scope Boundary

Day 20 focuses on ingestion and persistence.

Detailed event normalization and richer field extraction are intentionally handled in Day 21.

## Result

Day 20 ingestion pipeline successfully retrieves real Wazuh telemetry and persists it into the SentinelX PostgreSQL database.
