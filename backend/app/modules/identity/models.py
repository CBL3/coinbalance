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

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


class Role(db.Model):
    __tablename__ = "roles"
    __table_args__ = (
        db.UniqueConstraint("organization_id", "name", name="uq_roles_organization_name"),
    )

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=True, index=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    permissions = db.relationship("Permission", secondary=role_permissions, backref=db.backref("roles", lazy="dynamic"))
    organization = db.relationship("Organization", backref=db.backref("roles", lazy="dynamic"))

    @property
    def is_global(self) -> bool:
        return self.organization_id is None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "organization_id": self.organization_id,
            "name": self.name,
            "description": self.description,
            "permissions": [permission.name for permission in self.permissions],
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id = db.Column(db.String(36), db.ForeignKey("organizations.id"), nullable=True, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    display_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    roles = db.relationship("Role", secondary=user_roles, backref=db.backref("users", lazy="dynamic"))
    organization = db.relationship("Organization", backref=db.backref("users", lazy="dynamic"))

    def permission_names(self) -> set[str]:
        return {
            permission.name
            for role in self.roles
            for permission in role.permissions
            if role.is_global or role.organization_id == self.organization_id
        }

    def has_permission(self, permission_name: str) -> bool:
        return self.is_active and permission_name in self.permission_names()

    def is_system_admin(self) -> bool:
        return self.has_permission("system:admin")

    def can_access_organization(self, organization_id: str | None) -> bool:
        if self.is_system_admin():
            return True
        return organization_id is not None and organization_id == self.organization_id

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "organization_id": self.organization_id,
            "email": self.email,
            "display_name": self.display_name,
            "is_active": self.is_active,
            "permissions": sorted(self.permission_names()),
            "roles": [role.name for role in self.roles],
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
