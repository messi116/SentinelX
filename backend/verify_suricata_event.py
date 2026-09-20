from app.core.database import SessionLocal
from app.models.telemetry_event import TelemetryEvent

db = SessionLocal()

try:
    event = (
        db.query(TelemetryEvent)
        .filter(TelemetryEvent.id == 11)
        .first()
    )

    if event:
        print("DATABASE VERIFICATION SUCCESS")
        print("ID:", event.id)
        print("Source:", event.source)
        print("Event Type:", event.event_type)
        print("Timestamp:", event.timestamp)
        print("Host:", event.host)
        print("Source IP:", event.source_ip)
        print("Destination IP:", event.destination_ip)
        print("Message:", event.message)
        print("Raw Data:", event.raw_data)
    else:
        print("EVENT NOT FOUND")

finally:
    db.close()
