from typing import Any, Mapping


def get_connection_dsn(config: Mapping[str, Any]) -> str:
    return (
        f"postgresql://{config['postgres_user']}:{config['postgres_password']}@"
        f"{config['postgres_host']}:{config['postgres_port']}/{config['postgres_dbname']}"
    )
