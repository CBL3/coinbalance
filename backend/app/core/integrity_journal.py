import hashlib
import json
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.extensions import db


class IntegrityJournalEntry(db.Model):
    __tablename__ = "integrity_journal_entries"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    timestamp = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    organization_id = db.Column(db.String(36), nullable=True, index=True)
    actor_id = db.Column(db.String(36), nullable=True, index=True)
    subject_type = db.Column(db.String(120), nullable=False, index=True)
    subject_id = db.Column(db.String(36), nullable=True, index=True)
    event_type = db.Column(db.String(120), nullable=False, index=True)
    reference_id = db.Column(db.String(36), nullable=True, index=True)
    metadata_json = db.Column(db.JSON, nullable=False, default=dict)

    previous_hash = db.Column(db.String(64), nullable=False)
    record_hash = db.Column(db.String(64), nullable=False, unique=True)

    @classmethod
    def calculate_hash(
        cls,
        timestamp: datetime,
        subject_type: str,
        event_type: str,
        previous_hash: str,
        metadata_json: dict[str, Any],
        organization_id: str | None = None,
        actor_id: str | None = None,
        subject_id: str | None = None,
        reference_id: str | None = None,
    ) -> str:
        payload = {
            "timestamp": timestamp.isoformat(),
            "organization_id": organization_id,
            "actor_id": actor_id,
            "subject_type": subject_type,
            "subject_id": subject_id,
            "event_type": event_type,
            "reference_id": reference_id,
            "previous_hash": previous_hash,
            "metadata_json": metadata_json,
        }
        encoded_payload = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded_payload).hexdigest()

    @classmethod
    def record_event(
        cls,
        subject_type: str,
        event_type: str,
        metadata: dict[str, Any] | None = None,
        organization_id: str | None = None,
        actor_id: str | None = None,
        subject_id: str | None = None,
        reference_id: str | None = None,
    ) -> "IntegrityJournalEntry":
        metadata = metadata or {}

        last_entry = cls.query.filter_by(organization_id=organization_id).order_by(
            cls.timestamp.desc()
        ).first()
        previous_hash = last_entry.record_hash if last_entry else "0" * 64
        new_timestamp = datetime.now(timezone.utc)

        new_hash = cls.calculate_hash(
            timestamp=new_timestamp,
            organization_id=organization_id,
            actor_id=actor_id,
            subject_type=subject_type,
            subject_id=subject_id,
            event_type=event_type,
            reference_id=reference_id,
            previous_hash=previous_hash,
            metadata_json=metadata,
        )

        new_entry = cls(
            timestamp=new_timestamp,
            organization_id=organization_id,
            actor_id=actor_id,
            subject_type=subject_type,
            subject_id=subject_id,
            event_type=event_type,
            reference_id=reference_id,
            metadata_json=metadata,
            previous_hash=previous_hash,
            record_hash=new_hash,
        )

        db.session.add(new_entry)
        db.session.flush()

        return new_entry

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "organization_id": self.organization_id,
            "actor_id": self.actor_id,
            "subject_type": self.subject_type,
            "subject_id": self.subject_id,
            "event_type": self.event_type,
            "reference_id": self.reference_id,
            "metadata": self.metadata_json,
            "previous_hash": self.previous_hash,
            "record_hash": self.record_hash,
        }
