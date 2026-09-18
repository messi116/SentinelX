# Week 4 — Day 19: Wazuh Alert JSON Study

## Objective

Study a real Wazuh alert JSON returned through the SentinelX Wazuh alert API and identify the fields required for future ingestion and normalization.

## Environment

- SentinelX Backend: FastAPI
- Wazuh: Wazuh Manager + Wazuh Indexer
- Endpoint: Windows agent `sigma`
- Agent ID: `002`
- Agent IP: `192.168.18.161`
- API endpoint: `/api/wazuh/alerts`
- Database: PostgreSQL

## Observed Wazuh Alert Structure

The observed alert contains the following major sections.

### Agent

The `agent` object identifies the endpoint that generated the telemetry.

Observed fields:

- `agent.ip`
- `agent.name`
- `agent.id`

Observed values:

- IP: `192.168.18.161`
- Name: `sigma`
- ID: `002`

### Manager

The `manager` object identifies the Wazuh manager.

Observed field:

- `manager.name`

Observed value:

- `wazuh`

### Data

The `data` object contains source-specific event information.

For the observed Windows event:

- `data.win.eventdata.data`
- `data.win.system.eventID`
- `data.win.system.eventSourceName`
- `data.win.system.level`
- `data.win.system.channel`
- `data.win.system.message`
- `data.win.system.computer`
- `data.win.system.eventRecordID`
- `data.win.system.severityValue`
- `data.win.system.providerName`
- `data.win.system.systemTime`

This demonstrates that Wazuh preserves detailed Windows Event Channel information inside the alert.

### Rule

The `rule` object describes the Wazuh detection that fired.

Observed fields:

- `rule.id`
- `rule.level`
- `rule.description`
- `rule.groups`
- `rule.firedtimes`
- `rule.mail`

Observed values:

- Rule ID: `60646`
- Level: `5`
- Description: `License activation (slui.exe) failed.`
- Fired times: `25`

### Decoder

The decoder identifies how Wazuh interpreted the event.

Observed field:

- `decoder.name`

Observed value:

- `windows_eventchannel`

### Input

The input object describes the telemetry input type.

Observed field:

- `input.type`

Observed value:

- `log`

### Timing and Identification

The alert contains:

- `@timestamp`
- `timestamp`
- `id`
- `location`

Observed location:

- `EventChannel`

## SentinelX Normalization Mapping

| SentinelX Field | Wazuh Source |
|---|---|
| timestamp | `@timestamp` / `timestamp` |
| source | Wazuh |
| host | `agent.name` / `data.win.system.computer` |
| event_type | `decoder.name` / source event type |
| severity | `rule.level` |
| source_ip | `agent.ip` |
| username | Source-specific event fields when available |
| message | `rule.description` / `data.win.system.message` |
| raw_data | Complete original Wazuh alert JSON |

## Evidence-First Design Decision

SentinelX should preserve the original Wazuh alert as evidence instead of discarding source-specific fields.

The normalized representation provides common searchable fields while `raw_data` preserves the complete original event.

This supports the evidence-first architecture and allows future investigation features to access fields that are not part of the normalized schema.

## Ingestion Implications

The future Wazuh ingestion service should:

1. Retrieve Wazuh alerts.
2. Preserve the original JSON.
3. Extract common fields.
4. Convert timestamps into a consistent format.
5. Map Wazuh rule severity to SentinelX severity.
6. Identify the originating host.
7. Preserve source-specific data.
8. Store the normalized event in PostgreSQL.

## Day 19 Result

Day 19 successfully identified the structure of a real Wazuh alert and established the initial mapping between Wazuh telemetry and SentinelX's normalized event model.

The next milestone is Day 20: build the Wazuh ingestion service.

Pipeline:

Wazuh
?
Alert JSON
?
SentinelX Ingestion Service
?
Normalization
?
PostgreSQL
