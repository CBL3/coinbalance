from datetime import datetime, timezone
from uuid import uuid4

from app.extensions import db


class Evidence(db.Model):
    __tablename__ = "evidence"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    sha256_hash = db.Column(db.String(64), nullable=False, index=True)
    storage_uri = db.Column(db.String(1024), nullable=False)
    metadata_json = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
