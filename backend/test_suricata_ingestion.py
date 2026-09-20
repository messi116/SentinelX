import json

from app.core.database import SessionLocal
from app.services.suricata_ingestion import suricata_ingestion_service


EVENT_FILE = r".\\sentinelx-suricata-event.json"


with open(EVENT_FILE, "r", encoding="utf-8") as f:
    event = json.load(f)


db = SessionLocal()

try:
    result = suricata_ingestion_service.ingest_event(
        db=db,
        event=event,
    )

    print("SURICATA INGESTION SUCCESS")
    print(result)

finally:
    db.close()
