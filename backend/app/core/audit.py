from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.extensions import db


class AuditEvent(db.Model):
    __tablename__ = "audit_events"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=True, index=True)
    actor_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=True, index=True)
    event_type = db.Column(db.String(120), nullable=False, index=True)
    entity_type = db.Column(db.String(120), nullable=False, index=True)
    entity_id = db.Column(db.String(36), nullable=True, index=True)
    metadata_json = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    @classmethod
    def record_event(
        cls,
        event_type: str,
        entity_type: str,
        organization_id: str | None = None,
        actor_id: str | None = None,
        entity_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> "AuditEvent":
        event = cls(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            metadata_json=metadata or {},
        )
        db.session.add(event)
        db.session.flush()
        return event

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "organization_id": self.organization_id,
            "actor_id": self.actor_id,
            "event_type": self.event_type,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
