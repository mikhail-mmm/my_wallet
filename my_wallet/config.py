import os
from typing import Any, Mapping


def get_config() -> Mapping[str, Any]:
    return {
        "SECRET_KEY": os.environ.get("SECRET_KEY", "secret_key"),

        "POSTGRES_DBNAME": os.environ.get("POSTGRES_DBNAME", "my_wallet"),
        "POSTGRES_HOST": os.environ.get("POSTGRES_HOST", "127.0.0.1"),
        "POSTGRES_PORT": int(os.environ.get("POSTGRES_PORT", 5432)),
        "POSTGRES_USER": os.environ.get("POSTGRES_USER", "postgres"),
        "POSTGRES_PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),

        "FROM_EMAIL": "noreply@my-wallet.com",
        "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
        "MAILGUN_DOMAIN": os.environ.get("MAILGUN_DOMAIN"),

        "TWILLIO_SID": os.environ.get("TWILLIO_SID"),
        "TWILLIO_AUTH_TOKEN": os.environ.get("TWILLIO_AUTH_TOKEN"),
        "TWILLIO_FROM_NUMBER": os.environ.get("TWILLIO_FROM_NUMBER"),

        "TELEGRAM_BOT_TOKEN": os.environ.get("TELEGRAM_BOT_TOKEN"),
    }
