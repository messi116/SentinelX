from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.incident import Incident


router = APIRouter(
    prefix="/api/incidents",
    tags=["Incidents"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_incident(
    title: str,
    severity: int,
    description: str | None = None,
    risk_score: int | None = None,
    status: str = "open",
    confidence: int | None = None,
    db: Session = Depends(get_db),
):
    now = datetime.now(timezone.utc)

    incident = Incident(
        title=title,
        severity=severity,
        description=description,
        risk_score=risk_score,
        status=status,
        confidence=confidence,
        first_seen=now,
        last_seen=now,
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return {
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "risk_score": incident.risk_score,
        "status": incident.status,
        "confidence": incident.confidence,
        "first_seen": incident.first_seen,
        "last_seen": incident.last_seen,
        "created_at": incident.created_at,
    }


@router.get("")
def list_incidents(
    limit: int = 50,
    db: Session = Depends(get_db),
):
    limit = min(max(limit, 1), 100)

    incidents = (
        db.query(Incident)
        .order_by(Incident.last_seen.desc())
        .limit(limit)
        .all()
    )

    return {
        "count": len(incidents),
        "incidents": [
            {
                "id": incident.id,
                "title": incident.title,
                "description": incident.description,
                "severity": incident.severity,
                "risk_score": incident.risk_score,
                "status": incident.status,
                "confidence": incident.confidence,
                "first_seen": incident.first_seen,
                "last_seen": incident.last_seen,
                "created_at": incident.created_at,
            }
            for incident in incidents
        ],
    }