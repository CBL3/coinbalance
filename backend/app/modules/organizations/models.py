from datetime import datetime, timezone
from uuid import uuid4

from app.extensions import db


class Organization(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    legal_name = db.Column(db.String(255), unique=True, nullable=False)
    display_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "legal_name": self.legal_name,
            "display_name": self.display_name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
