"""
FastAPI settings for project.

Configure app level variables here.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from app.__version__ import __version__

# Load environment variables from .env file.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).parent.parent

# Build log path to be used within the application.
LOG_DIR = BASE_DIR.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True"

# Databases
DATABASES = {
    "default": os.environ.get("DATABASE_URI"),
}

# Logging
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

# OpenAPI
OPENAPI = {
    "openapi_url": "/openapi.json" if DEBUG else "",
    "title": "App",
    "description": "App Description",
    "contact": "",
    "version": __version__,
}
