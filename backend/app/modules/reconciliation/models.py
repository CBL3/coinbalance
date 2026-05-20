from datetime import datetime, timezone
from uuid import uuid4

from app.extensions import db


class ReconciliationRule(db.Model):
    __tablename__ = "reconciliation_rules"
    __table_args__ = (db.UniqueConstraint("organization_id", "code", name="uq_reconciliation_rules_org_code"),)

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=False, index=True)
    code = db.Column(db.String(120), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity_default = db.Column(db.String(50), nullable=False, default="medium")
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    metadata_json = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "organization_id": self.organization_id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "severity_default": self.severity_default,
            "is_active": self.is_active,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class ReconciliationRun(db.Model):
    __tablename__ = "reconciliation_runs"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=False, index=True)
    rule_id = db.Column(db.String(36), db.ForeignKey("reconciliation_rules.id"), nullable=False, index=True)
    actor_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=True, index=True)
    status = db.Column(db.String(50), nullable=False, default="pending")
    result_summary = db.Column(db.Text, nullable=True)
    metadata_json = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    rule = db.relationship("ReconciliationRule", backref=db.backref("runs", lazy="dynamic"))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "organization_id": self.organization_id,
            "rule_id": self.rule_id,
            "actor_id": self.actor_id,
            "status": self.status,
            "result_summary": self.result_summary,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


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
