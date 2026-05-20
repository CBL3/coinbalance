import os
from pathlib import Path


def read_version() -> str:
    version_file = Path(__file__).resolve().parents[2] / "VERSION"
    if version_file.exists():
        return version_file.read_text(encoding="utf-8").strip()
    return os.getenv("COINBALANCE_VERSION", "0.1.0-alpha")


class Config:
    COINBALANCE_ENV = os.getenv("COINBALANCE_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///:memory:",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COINBALANCE_VERSION = os.getenv("COINBALANCE_VERSION", read_version())
    JSON_SORT_KEYS = False
