from datetime import datetime, timezone
from uuid import uuid4

from app.extensions import db


user_roles = db.Table(
    "user_roles",
    db.Column("user_id", db.String(36), db.ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    db.Column("role_id", db.String(36), db.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
)


role_permissions = db.Table(
    "role_permissions",
    db.Column("role_id", db.String(36), db.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
    db.Column("permission_id", db.String(36), db.ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True),
)


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=True)


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), nullable=True, index=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    permissions = db.relationship("Permission", secondary=role_permissions, backref=db.backref("roles", lazy="dynamic"))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), nullable=True, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    display_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    roles = db.relationship("Role", secondary=user_roles, backref=db.backref("users", lazy="dynamic"))
