from typing import Any, Mapping


def get_connection_dsn(config: Mapping[str, Any]) -> str:
    return (
        f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DBNAME']}"
    )
