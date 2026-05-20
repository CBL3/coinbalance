"""identity audit foundation

Revision ID: 20260520_0001
Revises:
Create Date: 2026-05-20 17:10:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = "20260520_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "organizations",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("legal_name", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("legal_name"),
    )

    op.create_table(
        "permissions",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    op.create_table(
        "roles",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("organization_id", "name", name="uq_roles_organization_name"),
    )

    op.create_table(
        "users",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    op.create_table(
        "audit_events",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=True),
        sa.Column("actor_id", sa.String(length=36), nullable=True),
        sa.Column("event_type", sa.String(length=120), nullable=False),
        sa.Column("entity_type", sa.String(length=120), nullable=False),
        sa.Column("entity_id", sa.String(length=36), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["actor_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "evidence",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("sha256_hash", sa.String(length=64), nullable=False),
        sa.Column("storage_uri", sa.String(length=1024), nullable=False),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "integrity_journal_entries",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=True),
        sa.Column("actor_id", sa.String(length=36), nullable=True),
        sa.Column("subject_type", sa.String(length=120), nullable=False),
        sa.Column("subject_id", sa.String(length=36), nullable=True),
        sa.Column("event_type", sa.String(length=120), nullable=False),
        sa.Column("reference_id", sa.String(length=36), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
        sa.Column("previous_hash", sa.String(length=64), nullable=False),
        sa.Column("record_hash", sa.String(length=64), nullable=False),
        sa.ForeignKeyConstraint(["actor_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("record_hash"),
    )

    op.create_table(
        "reconciliation_findings",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=False),
        sa.Column("rule_code", sa.String(length=120), nullable=False),
        sa.Column("severity", sa.String(length=50), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "role_permissions",
        sa.Column("role_id", sa.String(length=36), nullable=False),
        sa.Column("permission_id", sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(["permission_id"], ["permissions.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("role_id", "permission_id"),
    )

    op.create_table(
        "user_roles",
        sa.Column("user_id", sa.String(length=36), nullable=False),
        sa.Column("role_id", sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "role_id"),
    )

    op.create_index("ix_audit_events_actor_id", "audit_events", ["actor_id"])
    op.create_index("ix_audit_events_entity_id", "audit_events", ["entity_id"])
    op.create_index("ix_audit_events_entity_type", "audit_events", ["entity_type"])
    op.create_index("ix_audit_events_event_type", "audit_events", ["event_type"])
    op.create_index("ix_audit_events_organization_id", "audit_events", ["organization_id"])
    op.create_index("ix_evidence_organization_id", "evidence", ["organization_id"])
    op.create_index("ix_evidence_sha256_hash", "evidence", ["sha256_hash"])
    op.create_index("ix_integrity_journal_entries_actor_id", "integrity_journal_entries", ["actor_id"])
    op.create_index("ix_integrity_journal_entries_event_type", "integrity_journal_entries", ["event_type"])
    op.create_index("ix_integrity_journal_entries_organization_id", "integrity_journal_entries", ["organization_id"])
    op.create_index("ix_integrity_journal_entries_reference_id", "integrity_journal_entries", ["reference_id"])
    op.create_index("ix_integrity_journal_entries_subject_id", "integrity_journal_entries", ["subject_id"])
    op.create_index("ix_integrity_journal_entries_subject_type", "integrity_journal_entries", ["subject_type"])
    op.create_index("ix_permissions_name", "permissions", ["name"])
    op.create_index("ix_reconciliation_findings_organization_id", "reconciliation_findings", ["organization_id"])
    op.create_index("ix_reconciliation_findings_rule_code", "reconciliation_findings", ["rule_code"])
    op.create_index("ix_roles_organization_id", "roles", ["organization_id"])
    op.create_index("ix_users_email", "users", ["email"])
    op.create_index("ix_users_organization_id", "users", ["organization_id"])


def downgrade():
    op.drop_index("ix_users_organization_id", table_name="users")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_roles_organization_id", table_name="roles")
    op.drop_index("ix_reconciliation_findings_rule_code", table_name="reconciliation_findings")
    op.drop_index("ix_reconciliation_findings_organization_id", table_name="reconciliation_findings")
    op.drop_index("ix_permissions_name", table_name="permissions")
    op.drop_index("ix_integrity_journal_entries_subject_type", table_name="integrity_journal_entries")
    op.drop_index("ix_integrity_journal_entries_subject_id", table_name="integrity_journal_entries")
    op.drop_index("ix_integrity_journal_entries_reference_id", table_name="integrity_journal_entries")
    op.drop_index("ix_integrity_journal_entries_organization_id", table_name="integrity_journal_entries")
    op.drop_index("ix_integrity_journal_entries_event_type", table_name="integrity_journal_entries")
    op.drop_index("ix_integrity_journal_entries_actor_id", table_name="integrity_journal_entries")
    op.drop_index("ix_evidence_sha256_hash", table_name="evidence")
    op.drop_index("ix_evidence_organization_id", table_name="evidence")
    op.drop_index("ix_audit_events_organization_id", table_name="audit_events")
    op.drop_index("ix_audit_events_event_type", table_name="audit_events")
    op.drop_index("ix_audit_events_entity_type", table_name="audit_events")
    op.drop_index("ix_audit_events_entity_id", table_name="audit_events")
    op.drop_index("ix_audit_events_actor_id", table_name="audit_events")
    op.drop_table("user_roles")
    op.drop_table("role_permissions")
    op.drop_table("reconciliation_findings")
    op.drop_table("integrity_journal_entries")
    op.drop_table("evidence")
    op.drop_table("audit_events")
    op.drop_table("users")
    op.drop_table("roles")
    op.drop_table("permissions")
    op.drop_table("organizations")
