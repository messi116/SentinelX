from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base


class TelemetryEvent(Base):
    __tablename__ = "telemetry_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    source: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    event_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    host: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    username: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)

    source_ip: Mapped[str | None] = mapped_column(String(45), nullable=True, index=True)
    destination_ip: Mapped[str | None] = mapped_column(String(45), nullable=True)

    process_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    message: Mapped[str | None] = mapped_column(Text, nullable=True)

    severity: Mapped[int | None] = mapped_column(Integer, nullable=True)

    raw_data: Mapped[dict[str, Any] | None] = mapped_column(
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )