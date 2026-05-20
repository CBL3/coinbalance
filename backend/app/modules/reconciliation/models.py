from datetime import datetime, timezone
from uuid import uuid4

from app.extensions import db


class ReconciliationFinding(db.Model):
    __tablename__ = "reconciliation_findings"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=False, index=True)
    rule_code = db.Column(db.String(120), nullable=False, index=True)
    severity = db.Column(db.String(50), nullable=False, default="medium")
    status = db.Column(db.String(50), nullable=False, default="new")
    description = db.Column(db.Text, nullable=False)
    metadata_json = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "organization_id": self.organization_id,
            "rule_code": self.rule_code,
            "severity": self.severity,
            "status": self.status,
            "description": self.description,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
