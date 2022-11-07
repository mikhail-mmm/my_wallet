import os
from typing import Any, Mapping, TypedDict


def get_config() -> Mapping[str, Any]:
    return {
        "postgres_dbname": os.environ.get("POSTGRES_DBNAME", "my_wallet"),
        "postgres_host": os.environ.get("POSTGRES_HOST", "127.0.0.1"),
        "postgres_port": int(os.environ.get("POSTGRES_PORT", 5432)),
        "postgres_user": os.environ.get("POSTGRES_USER", "postgres"),
        "postgres_password": os.environ.get("POSTGRES_PASSWORD", ""),
    }
