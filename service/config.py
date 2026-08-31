"""Service configuration."""
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///accounts.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    TALISMAN_FORCE_HTTPS = os.getenv("FORCE_HTTPS", "false").lower() == "true"
