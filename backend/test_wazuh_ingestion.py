import asyncio

from app.core.database import SessionLocal
from app.services.wazuh_ingestion import wazuh_ingestion_service


async def main():
    db = SessionLocal()

    try:
        result = await wazuh_ingestion_service.ingest_alerts(
            db,
            limit=1,
        )
        print(result)
    finally:
        db.close()


asyncio.run(main())
