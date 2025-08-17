# PostgreSQL

import os

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    },
}

INSTALLED_APPS = ("related_objects",)

SECRET_KEY = os.environ["SECRET_KEY"]
