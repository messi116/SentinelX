from datetime import datetime, timezone
from typing import Any

from sqlalchemy.orm import Session

from app.models.telemetry_event import TelemetryEvent


class SuricataIngestionService:
    def ingest_event(
        self,
        db: Session,
        event: dict[str, Any],
    ) -> dict[str, Any]:
        timestamp_value = event.get("timestamp")

        if not timestamp_value:
            raise ValueError("Suricata event is missing timestamp")

        timestamp = datetime.fromisoformat(
            timestamp_value.replace("Z", "+00:00")
        )

        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(
                tzinfo=timezone.utc
            )

        telemetry = TelemetryEvent(
            source="suricata",
            event_type=event.get("event_type", "suricata_event"),
            timestamp=timestamp,
            host=event.get("in_iface"),
            source_ip=event.get("src_ip"),
            destination_ip=event.get("dest_ip"),
            message=f"Suricata {event.get('event_type', 'event')} event",
            raw_data=event,
        )

        db.add(telemetry)
        db.commit()
        db.refresh(telemetry)

        return {
            "ingested": 1,
            "telemetry_event_id": telemetry.id,
            "event_type": telemetry.event_type,
        }


suricata_ingestion_service = SuricataIngestionService()
