# Week 4 Day 21 — Wazuh Event Normalization

## Objective

Normalize raw Wazuh security alerts into SentinelX's common `NormalizedEvent` schema while preserving the complete original alert as evidence.

## Implementation

The `EventNormalizer` converts Wazuh alerts into a consistent SentinelX event structure.

Normalized fields include:

- source
- event_type
- timestamp
- host
- username
- source_ip
- destination_ip
- source_port
- destination_port
- process_name
- process_id
- severity
- message
- raw_data

## Timestamp Handling

The normalizer supports both:

- `@timestamp`
- `timestamp`

ISO 8601 timestamps are converted into timezone-aware UTC datetime values.

Invalid or missing timestamps fall back to the current UTC time.

## Field Extraction

The normalizer safely extracts fields from common Wazuh structures.

Windows-specific host information can be obtained from:

- `agent.name`
- `data.win.system.computer`

Common identity and network fields include:

- `srcuser`
- `dstuser`
- `srcip`
- `dstip`
- `srcport`
- `dstport`

Process information can include:

- `process_name`
- `process`
- `process_id`
- `pid`

## Event Type

Wazuh decoder information is used as the normalized event type when available.

If decoder information is unavailable, the event falls back to:

`wazuh_alert`

## Evidence Preservation

The complete original Wazuh alert is stored in `raw_data`.

This ensures normalization does not destroy source evidence and allows SentinelX investigations to reference the original telemetry.

## Verification

Automated tests were created for:

1. Windows EventChannel alert
2. SSH authentication/network alert
3. Auditd process event
4. Alert with missing optional fields
5. Real Wazuh alert sample

Test results:

- Synthetic normalization tests: 4/4 passed
- Real Wazuh sample test: 1/1 passed

## Result

Wazuh telemetry can now be transformed into a consistent SentinelX event representation while maintaining the original alert as evidence.

This normalized representation provides the foundation for the next ingestion stages and cross-source correlation.
