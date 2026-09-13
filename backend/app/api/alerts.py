from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.alert import Alert


router = APIRouter(
    prefix="/api/alerts",
    tags=["Alerts"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_alert(
    title: str,
    severity: int,
    source: str,
    status: str = "new",
    description: str | None = None,
    db: Session = Depends(get_db),
):
    alert = Alert(
        title=title,
        severity=severity,
        source=source,
        status=status,
        description=description,
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return {
        "id": alert.id,
        "title": alert.title,
        "severity": alert.severity,
        "status": alert.status,
        "source": alert.source,
        "description": alert.description,
        "detected_at": alert.detected_at,
        "created_at": alert.created_at,
    }


@router.get("")
def list_alerts(
    limit: int = 50,
    db: Session = Depends(get_db),
):
    limit = min(max(limit, 1), 100)

    alerts = (
        db.query(Alert)
        .order_by(Alert.detected_at.desc())
        .limit(limit)
        .all()
    )

    return {
        "count": len(alerts),
        "alerts": [
            {
                "id": alert.id,
                "title": alert.title,
                "severity": alert.severity,
                "status": alert.status,
                "source": alert.source,
                "description": alert.description,
                "detected_at": alert.detected_at,
                "created_at": alert.created_at,
            }
            for alert in alerts
        ],
    }