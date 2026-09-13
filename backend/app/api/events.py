from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.telemetry_event import TelemetryEvent
from app.schemas.event import NormalizedEvent


router = APIRouter(
    prefix="/api/events",
    tags=["Events"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_event(
    event: NormalizedEvent,
    db: Session = Depends(get_db),
):
    raw_data = dict(event.raw_data or {})

    # Preserve normalized fields that are not separate DB columns.
    if event.source_port is not None:
        raw_data["source_port"] = event.source_port

    if event.destination_port is not None:
        raw_data["destination_port"] = event.destination_port

    if event.process_id is not None:
        raw_data["process_id"] = event.process_id

    db_event = TelemetryEvent(
        source=event.source,
        event_type=event.event_type,
        timestamp=event.timestamp,
        host=event.host,
        username=event.username,
        source_ip=event.source_ip,
        destination_ip=event.destination_ip,
        process_name=event.process_name,
        message=event.message,
        severity=event.severity,
        raw_data=raw_data or None,
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return {
        "id": db_event.id,
        "source": db_event.source,
        "event_type": db_event.event_type,
        "timestamp": db_event.timestamp,
        "host": db_event.host,
        "username": db_event.username,
        "source_ip": db_event.source_ip,
        "destination_ip": db_event.destination_ip,
        "process_name": db_event.process_name,
        "severity": db_event.severity,
        "message": db_event.message,
        "raw_data": db_event.raw_data,
        "created_at": db_event.created_at,
    }


@router.get("")
def list_events(
    limit: int = 50,
    db: Session = Depends(get_db),
):
    limit = min(max(limit, 1), 100)

    events = (
        db.query(TelemetryEvent)
        .order_by(TelemetryEvent.timestamp.desc())
        .limit(limit)
        .all()
    )

    return {
        "count": len(events),
        "events": [
            {
                "id": event.id,
                "source": event.source,
                "event_type": event.event_type,
                "timestamp": event.timestamp,
                "host": event.host,
                "username": event.username,
                "source_ip": event.source_ip,
                "destination_ip": event.destination_ip,
                "process_name": event.process_name,
                "severity": event.severity,
                "message": event.message,
                "raw_data": event.raw_data,
                "created_at": event.created_at,
            }
            for event in events
        ],
    }