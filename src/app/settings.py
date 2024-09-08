import os
from pathlib import Path

from dotenv import load_dotenv

from app.__version__ import __version__

BASE_DIR = Path(__file__).parent.parent

LOG_DIR = BASE_DIR.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

load_dotenv()

DEBUG = os.environ.get("DEBUG") == "True"

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASE_URI = os.environ.get("DATABASE_URI")

# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # noqa: E501
        },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": LOG_DIR / "debug.log",
                "formatter": "verbose",
                "backupCount": 5,
                "maxBytes": 1024 * 1024 * 15,
            },
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["file", "console"],
                "level": "DEBUG",
                "propagate": True,
            }
        },
    },
}

# OpenAPI settings
OPENAPI = {
    "openapi_url": "/openapi.json" if DEBUG else "",
    "title": "App",
    "description": "App Description",
    "contact": "",
    "version": __version__,
}
