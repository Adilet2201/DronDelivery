# settings.py (snippet)

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() in ("1","true","yes")

ALLOWED_HOSTS = [
    h.strip() for h in os.getenv("ALLOWED_HOSTS", "").split(",") if h.strip()
]

# Database
DATABASES = {
    "default": {
        "ENGINE":   "django.db.backends.postgresql",
        "NAME":     os.getenv("DATABASE_NAME"),
        "USER":     os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST":     os.getenv("DATABASE_HOST"),
        "PORT":     os.getenv("DATABASE_PORT"),
    }
}

# Static
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media & Storage
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

if os.getenv("AWS_STORAGE_BUCKET_NAME"):
    # switch to S3 in production
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_S3_ENDPOINT_URL      = os.getenv("AWS_S3_ENDPOINT_URL", None)  # optional
    AWS_STORAGE_BUCKET_NAME  = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME       = os.getenv("AWS_S3_REGION_NAME")
    AWS_ACCESS_KEY_ID        = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY    = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_SIGNATURE_VERSION = "s3v4"
    AWS_DEFAULT_ACL          = None
    MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/"
