from datetime import datetime, timezone
from uuid import uuid4

from app.extensions import db


class Organization(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    legal_name = db.Column(db.String(255), nullable=False)
    display_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
