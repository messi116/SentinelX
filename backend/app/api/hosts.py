from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.host import Host


router = APIRouter(
    prefix="/api/hosts",
    tags=["Hosts"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_host(
    hostname: str,
    ip_address: str | None = None,
    operating_system: str | None = None,
    agent_id: str | None = None,
    source: str = "wazuh",
    is_active: bool = True,
    db: Session = Depends(get_db),
):
    host = Host(
        hostname=hostname,
        ip_address=ip_address,
        operating_system=operating_system,
        agent_id=agent_id,
        source=source,
        is_active=is_active,
        last_seen=datetime.now(timezone.utc),
    )

    db.add(host)
    db.commit()
    db.refresh(host)

    return {
        "id": host.id,
        "hostname": host.hostname,
        "ip_address": host.ip_address,
        "operating_system": host.operating_system,
        "agent_id": host.agent_id,
        "source": host.source,
        "is_active": host.is_active,
        "last_seen": host.last_seen,
        "created_at": host.created_at,
    }


@router.get("")
def list_hosts(
    limit: int = 50,
    db: Session = Depends(get_db),
):
    limit = min(max(limit, 1), 100)

    hosts = (
        db.query(Host)
        .order_by(Host.last_seen.desc())
        .limit(limit)
        .all()
    )

    return {
        "count": len(hosts),
        "hosts": [
            {
                "id": host.id,
                "hostname": host.hostname,
                "ip_address": host.ip_address,
                "operating_system": host.operating_system,
                "agent_id": host.agent_id,
                "source": host.source,
                "is_active": host.is_active,
                "last_seen": host.last_seen,
                "created_at": host.created_at,
            }
            for host in hosts
        ],
    }