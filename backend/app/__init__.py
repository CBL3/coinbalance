from flask import Flask

from app.api.v1 import api_v1
from app.api.v1.hardware import bp as hardware_bp
from app.config import Config
from app.extensions import db, migrate

# Import models to ensure they are registered with SQLAlchemy
from app.core import audit, integrity_journal
from app.core.auth import authenticate_request
from app.modules.evidence import models as evidence_models
from app.modules.identity import models as identity_models
from app.modules.organizations import models as organization_models
from app.modules.reconciliation import models as reconciliation_models


def create_app(config_class: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.before_request(authenticate_request)

    app.register_blueprint(api_v1, url_prefix="/api/v1")
    app.register_blueprint(hardware_bp)

    from app import cli
    app.cli.add_command(cli.init_db_command)

    return app
