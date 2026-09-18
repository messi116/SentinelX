from datetime import datetime, timezone
from typing import Any

from sqlalchemy.orm import Session

from app.models.telemetry_event import TelemetryEvent
from app.services.wazuh_service import wazuh_service


class WazuhIngestionService:
    async def ingest_alerts(
        self,
        db: Session,
        limit: int = 20,
    ) -> dict[str, Any]:
        result = await wazuh_service.get_alerts(limit=limit)

        alerts = result.get("alerts", [])
        ingested = 0

        for alert in alerts:
            timestamp_value = (
                alert.get("@timestamp")
                or alert.get("timestamp")
            )

            if not timestamp_value:
                continue

            timestamp = datetime.fromisoformat(
                timestamp_value.replace("Z", "+00:00")
            )

            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(
                    tzinfo=timezone.utc
                )

            agent = alert.get("agent", {})
            rule = alert.get("rule", {})
            decoder = alert.get("decoder", {})
            win = alert.get("data", {}).get("win", {})
            system = win.get("system", {})

            host = (
                agent.get("name")
                or system.get("computer")
            )

            source_ip = agent.get("ip")

            message = (
                rule.get("description")
                or system.get("message")
            )

            event_type = (
                decoder.get("name")
                or "wazuh_alert"
            )

            severity = rule.get("level")

            telemetry = TelemetryEvent(
                source="wazuh",
                event_type=event_type,
                timestamp=timestamp,
                host=host,
                source_ip=source_ip,
                message=message,
                severity=severity,
                raw_data=alert,
            )

            db.add(telemetry)
            ingested += 1

        db.commit()

        return {
            "total_received": len(alerts),
            "ingested": ingested,
        }


wazuh_ingestion_service = WazuhIngestionService()
