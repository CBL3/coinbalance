"""reconciliation rules and runs

Revision ID: 20260520_0002
Revises: 20260520_0001
Create Date: 2026-05-20 18:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

revision = "20260520_0002"
down_revision = "20260520_0001"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "reconciliation_rules",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=False),
        sa.Column("code", sa.String(length=120), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("severity_default", sa.String(length=50), nullable=False, server_default=sa.text("'medium'")),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("1")),
        sa.Column("metadata_json", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("organization_id", "code", name="uq_reconciliation_rules_org_code"),
    )

    op.create_table(
        "reconciliation_runs",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("organization_id", sa.String(length=36), nullable=False),
        sa.Column("rule_id", sa.String(length=36), nullable=False),
        sa.Column("actor_id", sa.String(length=36), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False, server_default=sa.text("'pending'")),
        sa.Column("result_summary", sa.Text(), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.ForeignKeyConstraint(["rule_id"], ["reconciliation_rules.id"]),
        sa.ForeignKeyConstraint(["actor_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index("ix_reconciliation_rules_organization_id", "reconciliation_rules", ["organization_id"])
    op.create_index("ix_reconciliation_rules_code", "reconciliation_rules", ["code"])
    op.create_index("ix_reconciliation_runs_organization_id", "reconciliation_runs", ["organization_id"])
    op.create_index("ix_reconciliation_runs_rule_id", "reconciliation_runs", ["rule_id"])
    op.create_index("ix_reconciliation_runs_actor_id", "reconciliation_runs", ["actor_id"])


def downgrade():
    op.drop_index("ix_reconciliation_runs_actor_id", table_name="reconciliation_runs")
    op.drop_index("ix_reconciliation_runs_rule_id", table_name="reconciliation_runs")
    op.drop_index("ix_reconciliation_runs_organization_id", table_name="reconciliation_runs")
    op.drop_index("ix_reconciliation_rules_code", table_name="reconciliation_rules")
    op.drop_index("ix_reconciliation_rules_organization_id", table_name="reconciliation_rules")
    op.drop_table("reconciliation_runs")
    op.drop_table("reconciliation_rules")
