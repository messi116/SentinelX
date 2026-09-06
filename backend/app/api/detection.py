from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.event import NormalizedEvent
from app.services.detection_service import evaluate_and_persist


router = APIRouter(
    prefix="/api/detection",
    tags=["Detection"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/evaluate")
def evaluate_event(
    event: NormalizedEvent,
    db: Session = Depends(get_db),
):
    findings = evaluate_and_persist(db, event)

    return {
        "event_type": event.event_type,
        "finding_count": len(findings),
        "findings": [
            {
                "id": finding.id,
                "rule_id": finding.rule_name,
                "detection_type": finding.detection_type,
                "description": finding.description,
                "severity": finding.severity,
                "confidence": finding.confidence,
                "status": finding.status,
            }
            for finding in findings
        ],
    }